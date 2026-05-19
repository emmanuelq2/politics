import asyncio
import json
import time
import uuid
from pathlib import Path

from fastapi import FastAPI, Request, Cookie, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from questions import QUESTIONS
from scoring import full_analysis
import legifrance

app = FastAPI(title="French Political Pulse")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

DATA_FILE = Path("data/votes.json")
VOTER_FILE = Path("data/voter_ids.json")
_VOTES_FILE = Path("data/candidate_votes.json")

CANDIDATE_VOTES: dict = {}
if _VOTES_FILE.exists():
    try:
        CANDIDATE_VOTES = json.loads(_VOTES_FILE.read_text(encoding="utf-8"))
    except Exception:
        pass


# ── Data helpers ──────────────────────────────────────────────────────────────

def _empty_store() -> dict:
    return {
        "total_voters": 0,
        "responses": [],
        "dim_totals": {"eco": [], "econ": [], "ukraine": [], "police": []},
        "question_counts": {q["id"]: {} for q in QUESTIONS},
        "credibility_scores": [],
    }


def load_store() -> dict:
    if not DATA_FILE.exists():
        return _empty_store()
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_store(data: dict):
    DATA_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def load_voter_ids() -> set:
    if not VOTER_FILE.exists():
        return set()
    return set(json.loads(VOTER_FILE.read_text(encoding="utf-8")))


def save_voter_id(vid: str):
    ids = load_voter_ids()
    ids.add(vid)
    VOTER_FILE.write_text(json.dumps(list(ids)), encoding="utf-8")


def aggregate_stats(store: dict) -> dict:
    """Compute per-question percentages and dimension averages from stored data."""
    total = store["total_voters"]
    q_pcts = {}
    for qid, counts in store["question_counts"].items():
        q_total = sum(counts.values())
        q_pcts[qid] = {
            val: {"count": count, "pct": round(count / q_total * 100, 1) if q_total else 0}
            for val, count in counts.items()
        }

    dim_avgs = {}
    for dim, scores in store["dim_totals"].items():
        dim_avgs[dim] = round(sum(scores) / len(scores), 2) if scores else 0.0

    cred_scores = store.get("credibility_scores", [])
    avg_credibility = round(sum(cred_scores) / len(cred_scores), 1) if cred_scores else None

    return {
        "total": total,
        "q_pcts": q_pcts,
        "dim_avgs": dim_avgs,
        "avg_credibility": avg_credibility,
    }


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, voter_id: str = Cookie(default=None)):
    voter_ids = load_voter_ids()
    already_voted = bool(voter_id and voter_id in voter_ids)
    store = load_store()
    stats = aggregate_stats(store) if already_voted else None
    return templates.TemplateResponse(
        "ballot.html",
        {
            "request": request,
            "questions": QUESTIONS,
            "already_voted": already_voted,
            "stats": stats,
            "load_time": int(time.time()),
            "error": None,
        },
    )


@app.post("/vote", response_class=HTMLResponse)
async def vote(request: Request):
    form = await request.form()
    voter_id = request.cookies.get("voter_id")

    voter_ids = load_voter_ids()
    if voter_id and voter_id in voter_ids:
        return RedirectResponse("/results", status_code=303)

    # Validate all non-calibration questions answered
    answers = {}
    missing = []
    for q in QUESTIONS:
        val = form.get(q["id"])
        if val is None:
            missing.append(q["text"][:60] + "…")
        else:
            answers[q["id"]] = val

    if missing:
        store = load_store()
        return templates.TemplateResponse(
            "ballot.html",
            {
                "request": request,
                "questions": QUESTIONS,
                "already_voted": False,
                "stats": None,
                "load_time": form.get("load_time", 0),
                "error": f"Please answer all questions. Missing: {missing[0]}",
            },
            status_code=400,
        )

    # Compute submission speed
    try:
        load_time = int(form.get("load_time", 0))
        elapsed = time.time() - load_time if load_time else None
    except (ValueError, TypeError):
        elapsed = None

    # Run analysis
    analysis = full_analysis(answers, elapsed)

    # Persist vote
    store = load_store()
    store["total_voters"] += 1
    store["responses"].append({
        "id": str(uuid.uuid4()),
        "answers": answers,
        "dim_scores": analysis["dim_scores"],
        "credibility": analysis["credibility"],
        "profile": analysis["profile"]["name"],
    })
    for dim, score in analysis["dim_scores"].items():
        store["dim_totals"][dim].append(score)
    for qid, val in answers.items():
        store["question_counts"].setdefault(qid, {})
        store["question_counts"][qid].setdefault(val, 0)
        store["question_counts"][qid][val] += 1
    store["credibility_scores"].append(analysis["credibility"])
    save_store(store)

    # Set cookie and redirect to personal results
    new_vid = str(uuid.uuid4())
    save_voter_id(new_vid)

    # Store analysis in session via cookie (base64 JSON for simplicity)
    import base64
    analysis_payload = base64.b64encode(
        json.dumps({
            "dim_scores": analysis["dim_scores"],
            "contradictions": analysis["contradictions"],
            "credibility": analysis["credibility"],
            "profile_name": analysis["profile"]["name"],
            "profile_description": analysis["profile"]["description"],
            "profile_color": analysis["profile"]["color"],
            "dimension_labels": analysis["dimension_labels"],
            "is_troll": analysis["is_troll"],
            "is_suspicious": analysis["is_suspicious"],
            "party_calibration": analysis["party_calibration"],
        }, ensure_ascii=False).encode()
    ).decode()

    response = RedirectResponse("/results", status_code=303)
    response.set_cookie("voter_id", new_vid, max_age=60 * 60 * 24 * 365, httponly=True)
    response.set_cookie("last_analysis", analysis_payload, max_age=3600, httponly=False)
    return response


@app.get("/results", response_class=HTMLResponse)
async def results(request: Request, voter_id: str = Cookie(default=None)):
    voter_ids = load_voter_ids()
    if not voter_id or voter_id not in voter_ids:
        return RedirectResponse("/", status_code=303)

    store = load_store()
    stats = aggregate_stats(store)

    # Decode personal analysis from cookie
    import base64
    analysis_cookie = request.cookies.get("last_analysis")
    personal = None
    if analysis_cookie:
        try:
            personal = json.loads(base64.b64decode(analysis_cookie).decode())
        except Exception:
            pass

    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "questions": QUESTIONS,
            "stats": stats,
            "personal": personal,
            "candidate_votes": CANDIDATE_VOTES,
        },
    )


@app.get("/api/references/{question_id}")
async def api_references(question_id: str):
    data = await asyncio.to_thread(legifrance.fetch_live_references, question_id)
    return JSONResponse(content=data)


@app.post("/api/cache/clear")
async def api_cache_clear():
    await asyncio.to_thread(legifrance.clear_cache)
    return JSONResponse({"status": "cleared"})


@app.post("/reset")
async def reset(request: Request):
    save_store(_empty_store())
    VOTER_FILE.write_text("[]", encoding="utf-8")
    response = RedirectResponse("/", status_code=303)
    response.delete_cookie("voter_id")
    response.delete_cookie("last_analysis")
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
