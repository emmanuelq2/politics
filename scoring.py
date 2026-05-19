import math
from questions import QUESTIONS, POLITICAL_PROFILES, CONTRADICTION_PAIRS, PARTY_EXPECTED


def compute_dimension_scores(answers: dict) -> dict:
    """Returns average score per dimension (eco, econ, ukraine, police) from 1.0 to 4.0."""
    dim_scores = {"eco": [], "econ": [], "ukraine": [], "police": []}
    for q in QUESTIONS:
        dim = q["dimension"]
        if dim == "calibration":
            continue
        val = answers.get(q["id"])
        if val is None:
            continue
        for opt in q["options"]:
            if opt["value"] == val and opt["score"] is not None:
                dim_scores[dim].append(opt["score"])
                break
    return {dim: (sum(scores) / len(scores)) if scores else 0 for dim, scores in dim_scores.items()}


def find_contradictions(answers: dict) -> list:
    """Returns list of contradiction dicts found in the answers."""
    found = []
    for q1_id, q1_val, q2_id, q2_val, severity, explanation in CONTRADICTION_PAIRS:
        if answers.get(q1_id) == q1_val and answers.get(q2_id) == q2_val:
            found.append({"q1": q1_id, "q2": q2_id, "severity": severity, "explanation": explanation})
    return found


def check_party_calibration(answers: dict, dim_scores: dict) -> dict | None:
    """Check if declared party (Q10) matches computed dimension scores."""
    party = answers.get("political_alignment")
    if not party or party == "none":
        return None
    expected_ranges = PARTY_EXPECTED.get(party)
    if expected_ranges is None:
        return None

    mismatches = []
    for dim, (lo, hi) in expected_ranges.items():
        actual = dim_scores.get(dim, 0)
        if actual < lo - 0.5 or actual > hi + 0.5:
            mismatches.append({
                "dimension": dim,
                "expected": f"{lo}–{hi}",
                "actual": round(actual, 1),
            })
    return {"party": party, "mismatches": mismatches} if mismatches else None


def compute_credibility(contradictions: list, submission_seconds: float | None, party_calibration: dict | None) -> int:
    """Returns an authenticity credibility score 0–100."""
    score = 100
    for c in contradictions:
        score -= 30 if c["severity"] == "major" else 15
    if party_calibration and party_calibration["mismatches"]:
        score -= 15 * len(party_calibration["mismatches"])
    if submission_seconds is not None and submission_seconds < 25:
        score -= 20  # answered 10 questions in under 25 seconds → bot/troll
    return max(0, score)


def assign_profile(dim_scores: dict, declared_party: str | None = None) -> dict:
    """Returns the closest political profile using Euclidean distance.

    Abstentionniste is only assigned when the voter explicitly declared 'none'
    AND their scores cluster near the political centre (no score deviates far
    from 2.5), preventing centrist but opinionated voters from being mislabelled.
    """
    abstentionniste = next(p for p in POLITICAL_PROFILES if p["name"] == "Abstentionniste")
    candidates = [p for p in POLITICAL_PROFILES if p["name"] != "Abstentionniste"]

    best_profile = candidates[0]
    best_dist = float("inf")
    for profile in candidates:
        v = profile["vector"]
        dist = math.sqrt(sum((dim_scores.get(d, 2.5) - v[d]) ** 2 for d in v))
        if dist < best_dist:
            best_dist = dist
            best_profile = profile

    # Override with Abstentionniste only when explicitly declared AND genuinely centrist
    if declared_party == "none":
        max_deviation = max(abs(dim_scores.get(d, 2.5) - 2.5) for d in ["eco", "econ", "ukraine", "police"])
        if max_deviation < 1.2:
            return abstentionniste

    return best_profile


def label_dimension(score: float, dim: str) -> str:
    """Human-readable label for a dimension score."""
    labels = {
        "eco": ["Pro-growth / climate skeptic", "Green growth centrist", "Ecologist", "Radical ecologist / degrowth"],
        "econ": ["Trickle-down / economic liberal", "Moderate centrist", "Social democrat", "Anti-capitalist redistributor"],
        "ukraine": ["Pro-Russian / neutralist", "Diplomatic solution", "Moderate support", "Full military support"],
        "police": ["Law-and-order / police authority", "Moderate reformist", "Police accountability", "Abolish systemic racism / disarm"],
    }
    opts = labels.get(dim, [])
    idx = min(3, max(0, round(score) - 1))
    return opts[idx] if opts else ""


def full_analysis(answers: dict, submission_seconds: float | None = None) -> dict:
    dim_scores = compute_dimension_scores(answers)
    contradictions = find_contradictions(answers)
    party_cal = check_party_calibration(answers, dim_scores)
    credibility = compute_credibility(contradictions, submission_seconds, party_cal)
    profile = assign_profile(dim_scores, declared_party=answers.get("political_alignment"))
    dimension_labels = {d: label_dimension(s, d) for d, s in dim_scores.items()}
    return {
        "dim_scores": dim_scores,
        "contradictions": contradictions,
        "party_calibration": party_cal,
        "credibility": credibility,
        "profile": profile,
        "dimension_labels": dimension_labels,
        "is_troll": credibility < 40,
        "is_suspicious": 40 <= credibility < 65,
    }
