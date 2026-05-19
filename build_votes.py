#!/usr/bin/env python3
"""
build_votes.py
One-time pipeline: fetches AN roll-call vote records and builds data/candidate_votes.json

Data source: data.assemblee-nationale.fr bulk JSON exports (no auth required)
  - Scrutins ZIP:  /static/openData/repository/{leg}/loi/scrutins/Scrutins.json.zip
  - Deputies ZIP:  /static/openData/repository/{leg}/amo/deputes_actifs.../AMO10_*.json.zip

Usage:
    python build_votes.py               # full build
    python build_votes.py --test        # verify API + parse one scrutin
    python build_votes.py --discover 16 "ukraine"   # search scrutins by keyword
    python build_votes.py --find-pa "Roussel" 16    # find PA number by name

Note on deputies not covered:
  - francois-xavier bellamy : MEP (European Parliament), not AN deputy
  - glucksmann               : MEP
  - bardella                 : MEP (was RN group leader but not AN deputy himself)
  - brossat                  : Senator (Paris), not AN
  - arthaud / poutou         : Never elected to AN
  - bayrou                   : Last AN mandate 2017, now PM
  - de_villepin              : Never AN deputy (was PM/Senator)
  - retailleau               : Senator (Vendée)
  - bertrand                 : Regional president (not current AN deputy)
  - lisnard                  : Mayor (Cannes)
  - zemmour / asselineau     : Never elected to any legislative body
  - philippot                : Last AN mandate in 14th legislature (2012-2017)
  - tondelier                : Party leader, never AN deputy
  - cazeneuve                : Former PM; last AN mandate before 2014
"""

import argparse
import io
import json
import sys
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import httpx

# ── Paths & constants ─────────────────────────────────────────────────────────
CACHE_DIR = Path("data/scrutins_cache")
OUT_FILE  = Path("data/candidate_votes.json")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

AN_BASE   = "https://data.assemblee-nationale.fr"
SLEEP     = 0.5   # polite delay between downloads

# ── Confirmed PA numbers (acteurRef in AN open data) ─────────────────────────
# Verified against 16th/17th legislature AMO10 datasets + AN research

CANDIDATE_PA: dict[str, str | None] = {
    # Left / Radical Left
    "arthaud":       None,        # LO — never AN deputy
    "poutou":        None,        # NPA — never AN deputy
    "melenchon":     None,        # Lost 2022 & 2024 elections, no 16th/17th mandate
    "autain":        "PA588884",  # 16th + 17th leg (left LFI Jul 2024, still deputy)
    "ruffin":        "PA722142",  # 16th + 17th leg (left LFI Jul 2024, still deputy)
    "roussel":       "PA720692",  # 16th leg only (PCF, lost seat Jul 2024)
    "brossat":       None,        # Senator Paris — not AN
    "guedj":         "PA1567",    # 17th leg (PS, elected Jul 2024)
    "faure_vallaud": "PA609332",  # Olivier Faure, 16th + 17th leg
    "hollande":      "PA1654",    # 17th leg only (elected Corrèze Jul 2024)

    # Greens / Ecologists
    "tondelier":     None,        # Les Écologistes party leader, never AN deputy
    "batho":         "PA335999",  # 16th + 17th leg (Génération Écologie)
    "s_rousseau":    "PA795076",  # 16th + 17th leg (EELV)

    # Centre-left
    "glucksmann":    None,        # MEP — not AN deputy
    "cazeneuve":     None,        # Ex-PM, no recent AN mandate

    # Centre / Macronist
    "bayrou":        None,        # Last AN mandate 2017; now PM
    "e_philippe":    None,        # Mayor Le Havre; ran 2024 but lost (check below)
    "attal":         "PA722190",  # 17th leg, elected Hauts-de-Seine 2024
    "darmanin":      None,        # Lost 2024 snap election in Tourcoing

    # Right
    "de_villepin":   None,        # Never AN deputy
    "retailleau":    None,        # Senator (Vendée)
    "bertrand":      None,        # Regional president, not current AN deputy
    "lisnard":       None,        # Mayor (Cannes), never AN deputy
    "wauquiez":      "PA267285",  # 16th + 17th leg

    # Far right
    "dupont_aignan": None,        # Lost seat 2024 snap elections
    "le_pen":        "PA720614",  # 16th + 17th leg (convicted Mar 2025, still deputy pending appeal)
    "bellamy":       None,        # François-Xavier Bellamy — MEP, not AN deputy
    "zemmour":       None,        # Never AN deputy
    "philippot":     None,        # Last mandate 14th leg (2012-17)
    "asselineau":    None,        # Never elected to AN
}

# Legislature in which each candidate's PA is primarily active
# (used to select the right scrutin ZIP for vote lookup)
CANDIDATE_LEG: dict[str, int] = {
    "autain":        16,
    "ruffin":        16,
    "roussel":       16,
    "guedj":         17,
    "faure_vallaud": 16,
    "hollande":      17,
    "batho":         16,
    "s_rousseau":    16,
    "attal":         17,
    "wauquiez":      16,
    "le_pen":        16,
}

NON_DEPUTY_REASON: dict[str, str] = {
    "arthaud":     "Never elected to AN (LO candidate)",
    "poutou":      "Never elected to AN (NPA candidate)",
    "melenchon":   "Lost 2022 and 2024 elections — no mandate in 16th or 17th legislature",
    "brossat":     "Senator (Paris) — not AN deputy",
    "tondelier":   "Party leader (Les Écologistes) — never AN deputy",
    "glucksmann":  "MEP (European Parliament) — not AN deputy",
    "cazeneuve":   "Former PM; no AN mandate since ~2014",
    "bayrou":      "Former AN deputy until 2017; now Prime Minister",
    "e_philippe":  "Mayor of Le Havre; lost 2024 snap election",
    "darmanin":    "Lost Tourcoing seat in 2024 snap elections",
    "de_villepin": "Former PM/Senator — never AN deputy",
    "retailleau":  "Senator (Vendée) — not AN deputy",
    "bertrand":    "Regional president — not current AN deputy",
    "lisnard":     "Mayor (Cannes) — never AN deputy",
    "bellamy":     "MEP (European Parliament) — François-Xavier Bellamy, not AN deputy",
    "zemmour":     "Never elected to any legislative body",
    "philippot":   "Last AN mandate in 14th legislature (2012–17)",
    "asselineau":  "Never elected to AN",
    "dupont_aignan": "Lost seat in 2024 snap elections",
}

# ── Key scrutins ──────────────────────────────────────────────────────────────
# pour_is_high: True = voting 'pour' = progressive/high score on our 1–4 axis

KEY_SCRUTINS: dict[str, list[dict]] = {
    "ukraine_support": [
        {
            "id": 3461, "leg": 16,
            "label": "Accord de sécurité franco-ukrainien (mars 2024)",
            "pour_is_high": True, "weight": 1.5,
        },
        {
            "id": 652, "leg": 16,
            "label": "Résolution soutien Ukraine, condamnation agression russe (nov. 2022)",
            "pour_is_high": True, "weight": 1.0,
        },
    ],
    "intersectionality": [
        {
            "id": 3289, "leg": 16,
            "label": "Constitutionnalisation du droit à l'IVG (jan. 2024)",
            "pour_is_high": True, "weight": 1.0,
        },
    ],
    "state_role": [
        {
            "id": 1240, "leg": 16,
            "label": "Motion de censure transpartisane (réforme retraites, mar. 2023)",
            "pour_is_high": True, "weight": 1.5,
        },
        {
            "id": 1241, "leg": 16,
            "label": "Motion de censure LFI/gauche (réforme retraites, mar. 2023)",
            "pour_is_high": True, "weight": 1.0,
        },
    ],
    "systemic_racism": [
        {
            "id": 3213, "leg": 16,
            "label": "Loi immigration — vote sur l'ensemble du texte (déc. 2023)",
            "pour_is_high": False, "weight": 1.0,
        },
    ],
    "eco_economy": [
        {
            "id": 1243, "leg": 16,
            "label": "Loi d'accélération du nucléaire (mar. 2023)",
            "pour_is_high": False, "weight": 1.0,
        },
    ],
}


# ── Download helpers ──────────────────────────────────────────────────────────

def _download_zip(url: str) -> zipfile.ZipFile:
    print(f"  Downloading {url.split('/')[-1]} ...")
    r = httpx.get(url, timeout=120, follow_redirects=True)
    r.raise_for_status()
    print(f"  -> {len(r.content)/1024/1024:.1f} MB")
    return zipfile.ZipFile(io.BytesIO(r.content))


def _get_scrutins_zip(legislature: int) -> zipfile.ZipFile:
    cache_path = CACHE_DIR / f"Scrutins_{legislature}.zip"
    if cache_path.exists():
        return zipfile.ZipFile(cache_path)
    url = f"{AN_BASE}/static/openData/repository/{legislature}/loi/scrutins/Scrutins.json.zip"
    zf = _download_zip(url)
    cache_path.write_bytes(zf.fp.read() if hasattr(zf, 'fp') else open(zf.filename, 'rb').read())
    return zf


def _load_scrutins_zip(legislature: int) -> zipfile.ZipFile:
    """Download + cache the full scrutins ZIP for a legislature."""
    cache_path = CACHE_DIR / f"Scrutins_{legislature}.zip"
    if not cache_path.exists():
        url = f"{AN_BASE}/static/openData/repository/{legislature}/loi/scrutins/Scrutins.json.zip"
        print(f"  Downloading legislature {legislature} scrutins...")
        r = httpx.get(url, timeout=120, follow_redirects=True)
        r.raise_for_status()
        cache_path.write_bytes(r.content)
        print(f"  -> {len(r.content)/1024/1024:.1f} MB cached")
    return zipfile.ZipFile(cache_path)


# ── Scrutin parsing ───────────────────────────────────────────────────────────

def _ensure_list(val) -> list:
    if val is None:
        return []
    if isinstance(val, list):
        return val
    return [val]


def find_scrutin_in_zip(zf: zipfile.ZipFile, scrutin_number: int) -> dict | None:
    """Search through a scrutin ZIP for a specific scrutin number."""
    target = str(scrutin_number)
    for fname in zf.namelist():
        data = json.loads(zf.read(fname))
        sc = data.get("scrutin", {})
        if str(sc.get("numero", "")) == target:
            return sc
    return None


def extract_vote(scrutin: dict, pa_number: str) -> str:
    """
    Return 'pour' | 'contre' | 'abstention' | 'nonVotant' | 'absent'
    for a deputy identified by their PA number (acteurRef).
    """
    ventilation = scrutin.get("ventilationVotes", {})
    organe_block = ventilation.get("organe", {})

    # organe can be a list or a single dict
    organes = _ensure_list(organe_block)

    for organe in organes:
        groupes_block = organe.get("groupes", {})
        groupes = _ensure_list(groupes_block.get("groupe", []))

        for groupe in groupes:
            vote_block = groupe.get("vote", {})
            decompte = vote_block.get("decompteNominatif", {})

            for position_key, position_label in [
                ("pours", "pour"),
                ("contres", "contre"),
                ("abstentions", "abstention"),
                ("nonVotants", "nonVotant"),
            ]:
                pos_block = decompte.get(position_key) or {}
                votants = _ensure_list(pos_block.get("votant", []))
                for v in votants:
                    if isinstance(v, dict) and v.get("acteurRef") == pa_number:
                        return position_label

    return "absent"


# ── Discovery ─────────────────────────────────────────────────────────────────

def discover_scrutins(legislature: int, query: str):
    """Print scrutins whose title contains the query string."""
    zf = _load_scrutins_zip(legislature)
    query_lower = query.lower()
    matches = []
    for fname in zf.namelist():
        data = json.loads(zf.read(fname))
        sc = data.get("scrutin", {})
        titre = sc.get("titre", "")
        if query_lower in titre.lower():
            matches.append({
                "id": sc.get("numero"),
                "date": sc.get("dateScrutin", "")[:10],
                "sort": sc.get("sort", ""),
                "titre": titre[:90],
            })
    matches.sort(key=lambda x: x["date"])
    print(f"\nLegislature {legislature} - '{query}' - {len(matches)} results:\n")
    print(f"{'ID':>6}  {'Date':<12}  {'Sort':<12}  Title")
    print("-" * 100)
    for m in matches:
        sort_val = m['sort']
        if isinstance(sort_val, dict):
            sort_str = sort_val.get('code', str(sort_val))[:12]
        else:
            sort_str = str(sort_val)[:12]
        titre = m['titre'].encode('ascii', 'replace').decode()
        print(f"{m['id']:>6}  {m['date']:<12}  {sort_str:<12}  {titre}")


def find_pa(name: str, legislature: int):
    """Search deputies ZIP for a name and print PA numbers."""
    url = (
        f"{AN_BASE}/static/openData/repository/{legislature}"
        f"/amo/deputes_actifs_mandats_actifs_organes"
        f"/AMO10_deputes_actifs_mandats_actifs_organes.json.zip"
    )
    try:
        zf = _download_zip(url)
    except Exception as e:
        print(f"Could not download deputies dataset: {e}")
        return
    name_lower = name.lower()
    found = []
    for fname in zf.namelist():
        if "/acteur/" not in fname:
            continue
        data = json.loads(zf.read(fname))
        a = data.get("acteur", {})
        uid = a.get("uid", {})
        pa = uid.get("#text", "") if isinstance(uid, dict) else str(uid)
        ident = a.get("etatCivil", {}).get("ident", {})
        nom = ident.get("nom", "")
        prenom = ident.get("prenom", "")
        if name_lower in nom.lower() or name_lower in prenom.lower():
            found.append((pa, prenom, nom))
    for entry in found:
        print(f"  PA={entry[0]}  {entry[1]} {entry[2]}")
    if not found:
        print(f"  No match for '{name}' in legislature {legislature}")


# ── Main build ────────────────────────────────────────────────────────────────

def build():
    print("\n=== AN Vote Pipeline — building candidate_votes.json ===\n")

    # Collect all legislatures needed
    legs_needed = set(CANDIDATE_LEG.get(k, 16) for k, v in CANDIDATE_PA.items() if v)
    for s_list in KEY_SCRUTINS.values():
        for s in s_list:
            legs_needed.add(s["leg"])

    # Load scrutin ZIPs
    print("Step 1 — Loading scrutin archives...")
    zips: dict[int, zipfile.ZipFile] = {}
    for leg in sorted(legs_needed):
        zips[leg] = _load_scrutins_zip(leg)
        print(f"  Leg {leg}: {len(zips[leg].namelist())} scrutins")

    # Pre-load target scrutins into memory
    print("\nStep 2 — Locating key scrutins...")
    loaded_scrutins: dict[tuple, dict] = {}
    for topic, scrutins in KEY_SCRUTINS.items():
        for s in scrutins:
            key = (s["id"], s["leg"])
            if key in loaded_scrutins:
                continue
            zf = zips.get(s["leg"])
            if not zf:
                print(f"  SKIP {s['id']}: no ZIP for leg {s['leg']}")
                continue
            sc = find_scrutin_in_zip(zf, s["id"])
            if sc:
                loaded_scrutins[key] = sc
                date = sc.get("dateScrutin", "")[:10]
                sort_ = sc.get("sort", "?")
                titre = sc.get("titre", "")[:60]
                print(f"  [{s['id']}] {date} ({sort_}) — {titre}")
            else:
                print(f"  NOT FOUND: scrutin {s['id']} in leg {s['leg']}")

    # Extract per-candidate votes
    print("\nStep 3 — Extracting votes per candidate...")
    candidates_out: dict[str, dict] = {}

    for cand_key, pa in CANDIDATE_PA.items():
        if pa is None:
            reason = NON_DEPUTY_REASON.get(cand_key, "Not an AN deputy")
            candidates_out[cand_key] = {
                "is_deputy": False,
                "reason": reason,
                "votes": {},
            }
            print(f"  SKIP  {cand_key}: {reason[:60]}")
            continue

        cand_leg = CANDIDATE_LEG.get(cand_key, 16)
        cand_votes: dict[str, dict] = {}

        for topic, scrutins in KEY_SCRUTINS.items():
            topic_entries = []
            for s in scrutins:
                if s["leg"] != cand_leg:
                    continue
                key = (s["id"], s["leg"])
                sc = loaded_scrutins.get(key)
                if not sc:
                    continue
                position = extract_vote(sc, pa)
                topic_entries.append({
                    "id": s["id"],
                    "label": s["label"],
                    "position": position,
                    "pour_is_high": s["pour_is_high"],
                    "weight": s.get("weight", 1.0),
                })

            if topic_entries:
                # Compute weighted net stance
                net_score = 0.0
                total_w = 0.0
                for e in topic_entries:
                    w = e["weight"]
                    if e["position"] in ("pour", "contre"):
                        val = 1.0 if e["position"] == "pour" else -1.0
                        if not e["pour_is_high"]:
                            val *= -1
                    else:
                        val = 0.0
                    net_score += val * w
                    total_w += w
                net = net_score / total_w if total_w else 0.0
                summary = "pro" if net > 0.15 else ("anti" if net < -0.15 else "mixed")

                cand_votes[topic] = {
                    "scrutins": topic_entries,
                    "summary": summary,
                }

        candidates_out[cand_key] = {
            "is_deputy": True,
            "pa": pa,
            "legislature": cand_leg,
            "votes": cand_votes,
        }
        vote_str = ", ".join(
            f"{t}={v['summary']}" for t, v in cand_votes.items()
        ) or "no matching scrutins for this legislature"
        print(f"  OK    {cand_key} ({pa}): {vote_str}")

    # Write output
    print("\nStep 4 — Writing output...")
    out = {
        "built_at": datetime.now(timezone.utc).isoformat(),
        "scrutins_used": {
            topic: [
                {"id": s["id"], "leg": s["leg"], "label": s["label"]}
                for s in scrutins
            ]
            for topic, scrutins in KEY_SCRUTINS.items()
        },
        "candidates": candidates_out,
    }
    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    n_dep = sum(1 for v in candidates_out.values() if v["is_deputy"])
    n_skip = sum(1 for v in candidates_out.values() if not v["is_deputy"])
    print(f"  Written to {OUT_FILE}")
    print(f"  Deputies with vote records: {n_dep}")
    print(f"  Non-deputies skipped:       {n_skip}")
    print("\nTo add more topics, run:")
    print("  python build_votes.py --discover 16 \"impot fortune\"")
    print("  python build_votes.py --discover 16 \"lanceur de balles\"")


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--discover", metavar="QUERY",
                        help="Search scrutins by keyword (requires --leg)")
    parser.add_argument("--leg", type=int, default=16,
                        help="Legislature number (default 16)")
    parser.add_argument("--find-pa", metavar="NAME",
                        help="Find deputy PA number by surname")
    parser.add_argument("--test", action="store_true",
                        help="Quick connectivity test")
    args = parser.parse_args()

    if args.test:
        print("Testing connectivity to data.assemblee-nationale.fr ...")
        r = httpx.get(f"{AN_BASE}/", timeout=10)
        print(f"  Status: {r.status_code}")
        zf = _load_scrutins_zip(16)
        sc = find_scrutin_in_zip(zf, 3289)
        if sc:
            print(f"  Scrutin 3289 found: {sc.get('titre','')[:60]}")
            vote = extract_vote(sc, "PA720614")  # Marine Le Pen
            print(f"  Marine Le Pen (PA720614) on IVG vote: {vote}")
        else:
            print("  Scrutin 3289 NOT found")
    elif args.discover:
        discover_scrutins(args.leg, args.discover)
    elif args.find_pa:
        find_pa(args.find_pa, args.leg)
    else:
        build()
