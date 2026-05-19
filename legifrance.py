"""
Legifrance / PISTE API client.

Requires PISTE_CLIENT_ID and PISTE_CLIENT_SECRET in .env (or environment).
Falls back gracefully when unconfigured.

Token is refreshed automatically before expiry.
Results are cached in data/legifrance_cache.json for CACHE_TTL seconds (default 24h).
"""

import json
import os
import threading
import time
from pathlib import Path
from typing import Optional

import httpx
from dotenv import load_dotenv

load_dotenv()

PISTE_CLIENT_ID: str = os.getenv("PISTE_CLIENT_ID", "")
PISTE_CLIENT_SECRET: str = os.getenv("PISTE_CLIENT_SECRET", "")
PISTE_API_KEY: str = os.getenv("PISTE_API_KEY", "")
PISTE_SANDBOX: bool = os.getenv("PISTE_SANDBOX", "false").lower() == "true"

if PISTE_SANDBOX:
    _TOKEN_URL = "https://sandbox-oauth.aife.economie.gouv.fr/api/oauth/token"
    _API_BASE = "https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app"
else:
    _TOKEN_URL = "https://oauth.piste.gouv.fr/api/oauth/token"
    _API_BASE = "https://api.piste.gouv.fr/dila/legifrance/lf-engine-app"

_CACHE_FILE = Path("data/legifrance_cache.json")
CACHE_TTL = int(os.getenv("PISTE_CACHE_TTL", 86400))  # 24 h default

_token: Optional[str] = None
_token_expiry: float = 0.0
_lock = threading.Lock()

# ── Per-question search config ────────────────────────────────────────────────
# fond: JORF (Official Gazette) | LEGI (codes & statutes)

QUESTION_QUERIES: dict[str, dict] = {
    "eco_activism": {
        "fond": "JORF",
        "query": "Soulèvements de la Terre dissolution",
        "heading": "Live from Légifrance — dissolution & Conseil d'État",
    },
    "eco_economy": {
        "fond": "LEGI",
        "query": "loi énergie-climat stratégie nationale bas-carbone",
        "heading": "Live from Légifrance — Loi Énergie-Climat & SNBC",
    },
    "wealth_tax": {
        "fond": "JORF",
        "query": "contribution différentielle hauts revenus impôt sur la fortune",
        "heading": "Live from Légifrance — fiscalité des hauts revenus",
    },
    "intersectionality": {
        "fond": "LEGI",
        "query": "interruption volontaire de grossesse égalité salariale femmes",
        "heading": "Live from Légifrance — IVG & égalité professionnelle",
    },
    "ukraine_support": {
        "fond": "JORF",
        "query": "Ukraine soutien militaire aide défense",
        "heading": "Live from Légifrance — textes d'aide à l'Ukraine",
    },
    "ukraine_origins": {
        "fond": "JORF",
        "query": "Ukraine Russie agression résolution reconnaissance",
        "heading": "Live from Légifrance — résolutions sur l'agression russe",
    },
    "systemic_racism": {
        "fond": "JORF",
        "query": "déontologie policière discrimination raciale contrôle identité",
        "heading": "Live from Légifrance — déontologie & discriminations",
    },
    "lbd_armament": {
        "fond": "LEGI",
        "query": "lanceur balles défense maintien ordre armes",
        "heading": "Live from Légifrance — réglementation LBD",
    },
    "state_role": {
        "fond": "JORF",
        "query": "service public privatisation protection sociale nationalisation",
        "heading": "Live from Légifrance — rôle de l'État",
    },
}


# ── Auth ──────────────────────────────────────────────────────────────────────

def is_configured() -> bool:
    return bool(PISTE_CLIENT_ID and PISTE_CLIENT_SECRET) or bool(PISTE_API_KEY)


def _api_headers(token: Optional[str] = None) -> dict:
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if PISTE_API_KEY:
        headers["KeyId"] = PISTE_API_KEY
    return headers


def _get_token() -> Optional[str]:
    global _token, _token_expiry
    if not is_configured():
        return None
    with _lock:
        if _token and time.time() < _token_expiry - 60:
            return _token
        try:
            r = httpx.post(
                _TOKEN_URL,
                data={
                    "grant_type": "client_credentials",
                    "client_id": PISTE_CLIENT_ID,
                    "client_secret": PISTE_CLIENT_SECRET,
                    "scope": "openid",
                },
                timeout=10,
            )
            r.raise_for_status()
            body = r.json()
            _token = body["access_token"]
            _token_expiry = time.time() + body.get("expires_in", 3600)
            return _token
        except Exception:
            return None


# ── Cache ─────────────────────────────────────────────────────────────────────

def _load_cache() -> dict:
    if _CACHE_FILE.exists():
        try:
            return json.loads(_CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def _save_cache(cache: dict) -> None:
    _CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")


# ── Search ────────────────────────────────────────────────────────────────────

def _build_search_payload(query: str, fond: str, size: int = 5) -> dict:
    return {
        "recherche": {
            "champs": [
                {
                    "typeChamp": "ALL",
                    "criteres": [
                        {
                            "typeRecherche": "TOUS_LES_MOTS_DANS_UN_CHAMP",
                            "valeur": query,
                            "operateur": "ET",
                        }
                    ],
                    "operateur": "ET",
                }
            ],
            "filtres": [],
            "pageNumber": 1,
            "pageSize": size,
            "sort": "PERTINENCE",
            "typePagination": "DEFAUT",
        },
        "fond": fond,
    }


def _parse_results(raw: list, fond: str) -> list[dict]:
    refs = []
    for item in raw:
        titles = item.get("titles") or []
        if not titles:
            continue

        title_obj = titles[0]
        # cid is the clean document ID (without the _date suffix on id field)
        text_id = title_obj.get("cid") or title_obj.get("id", "")
        if not text_id:
            continue

        # Strip <mark> highlight tags injected by the search engine
        label = title_obj.get("title") or title_obj.get("titre") or text_id
        label = label.replace("<mark>", "").replace("</mark>", "")[:140]

        # Date — sentinel value 2999 means "no date"
        raw_date = (
            item.get("date")
            or title_obj.get("startDate")
            or title_obj.get("dateVersion")
            or ""
        )
        date = str(raw_date)[:10] if raw_date and "2999" not in str(raw_date) else ""

        url = (
            f"https://www.legifrance.gouv.fr/jorf/id/{text_id}"
            if fond == "JORF"
            else f"https://www.legifrance.gouv.fr/loda/id/{text_id}"
        )

        refs.append({"label": label, "url": url, "date": date})
    return refs


def _call_search(token: Optional[str], query: str, fond: str, size: int = 5) -> list[dict]:
    try:
        r = httpx.post(
            f"{_API_BASE}/search",
            json=_build_search_payload(query, fond, size),
            headers=_api_headers(token),
            timeout=15,
        )
        r.raise_for_status()
        body = r.json()
        raw = body.get("results", [])
        return _parse_results(raw, fond)
    except Exception:
        return []


# ── Public interface ──────────────────────────────────────────────────────────

def fetch_live_references(question_id: str) -> dict:
    """
    Return live Légifrance references for a question.

    Response schema:
      {
        "configured": bool,          # False if PISTE credentials missing
        "heading": str,              # section heading for the UI
        "refs": [{"label", "url", "date"}, ...],
        "cached": bool,
        "error": str | None
      }
    """
    if not is_configured():
        return {"configured": False, "heading": "", "refs": [], "cached": False, "error": None}

    if question_id not in QUESTION_QUERIES:
        return {"configured": True, "heading": "", "refs": [], "cached": False, "error": None}

    config = QUESTION_QUERIES[question_id]
    cache = _load_cache()
    now = time.time()

    if question_id in cache and now - cache[question_id].get("ts", 0) < CACHE_TTL:
        return {
            "configured": True,
            "heading": config["heading"],
            "refs": cache[question_id]["refs"],
            "cached": True,
            "error": None,
        }

    token = _get_token() if (PISTE_CLIENT_ID and PISTE_CLIENT_SECRET) else None
    if not token and not PISTE_API_KEY:
        return {
            "configured": True,
            "heading": config["heading"],
            "refs": [],
            "cached": False,
            "error": "auth_failed",
        }

    refs = _call_search(token, config["query"], config["fond"])
    cache[question_id] = {"ts": now, "refs": refs}
    _save_cache(cache)

    return {
        "configured": True,
        "heading": config["heading"],
        "refs": refs,
        "cached": False,
        "error": None,
    }


def clear_cache() -> None:
    _save_cache({})
