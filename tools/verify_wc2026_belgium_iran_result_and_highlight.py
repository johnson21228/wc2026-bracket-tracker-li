#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATCH_ID = "66456986"
HIGHLIGHT_URL = "https://youtu.be/YbiEe9pOV-s"

matches = json.loads((ROOT / "site/data/current/group_matches.json").read_text())
standings = json.loads((ROOT / "site/data/current/group_standings.json").read_text())
highlights = json.loads((ROOT / "site/data/current/match_highlights.json").read_text())
evidence_path = ROOT / "source/text/group_result_evidence_20260621_belgium_iran.json"

errors = []


def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from walk(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from walk(item)


def text(obj):
    return json.dumps(obj, ensure_ascii=False).lower()


def is_match(obj):
    t = text(obj)
    return MATCH_ID in t or ("belgium" in t and "iran" in t)


def score_values(obj):
    vals = []
    for key in ("homeScore", "scoreHome", "home_score", "team1Score", "score1"):
        if key in obj:
            vals.append(("home", obj[key]))
    for key in ("awayScore", "scoreAway", "away_score", "team2Score", "score2"):
        if key in obj:
            vals.append(("away", obj[key]))
    if isinstance(obj.get("home"), dict) and "score" in obj["home"]:
        vals.append(("home", obj["home"]["score"]))
    if isinstance(obj.get("away"), dict) and "score" in obj["away"]:
        vals.append(("away", obj["away"]["score"]))
    if isinstance(obj.get("score"), dict):
        for key, value in obj["score"].items():
            lk = str(key).lower()
            if "home" in lk:
                vals.append(("home", value))
            if "away" in lk:
                vals.append(("away", value))
    return vals


found = [
    m for m in walk(matches)
    if isinstance(m, dict)
    and (
        m.get("matchId") == "GS-2026-06-21-G3"
        or (
            m.get("groupId") == "G"
            and m.get("homeTeamId") == "BEL"
            and m.get("awayTeamId") in {"IRN", "IRI"}
        )
    )
]
if not found:
    errors.append("Belgium-Iran match was not found")
else:
    match = found[0]
    st = text(match)
    if not any(token in st for token in ("complete", "completed", "final", '"ft"', "full time")):
        errors.append("Belgium-Iran match is not marked final/complete")
    vals = score_values(match)
    if vals:
        for side, value in vals:
            try:
                if int(value) != 0:
                    errors.append(f"Belgium-Iran {side} score is not 0: {value}")
            except (TypeError, ValueError):
                errors.append(f"Belgium-Iran {side} score is not numeric: {value}")
    else:
        # Fallback for competitor-shaped data.
        mt = text(match)
        if '"score": 0' not in mt and '"score": "0"' not in mt:
            errors.append("Belgium-Iran scores are not visibly recorded as 0-0")

highlight_text = json.dumps(highlights, ensure_ascii=False)
if MATCH_ID not in highlight_text and "Belgium" not in highlight_text:
    errors.append("Belgium-Iran highlight entry is not keyed or labeled")
if HIGHLIGHT_URL not in highlight_text:
    errors.append("Belgium-Iran highlight URL is missing")

if not evidence_path.exists():
    errors.append("Belgium-Iran evidence file is missing")
else:
    evidence = json.loads(evidence_path.read_text())
    if evidence.get("matchId") != MATCH_ID:
        errors.append("Belgium-Iran evidence matchId is wrong")
    if evidence.get("highlight", {}).get("url") != HIGHLIGHT_URL:
        errors.append("Belgium-Iran evidence highlight URL is wrong")
    match_evidence = evidence.get("match", {})
    if match_evidence.get("homeScore") != 0 or match_evidence.get("awayScore") != 0:
        errors.append("Belgium-Iran evidence does not record 0-0")
    if match_evidence.get("status") != "FT":
        errors.append("Belgium-Iran evidence does not record FT")

standings_text = json.dumps(standings, ensure_ascii=False).lower()
for token in ("belgium", "iran"):
    if token not in standings_text:
        errors.append(f"Group G standings no longer include {token}")

if errors:
    print("Belgium-Iran result/highlight verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Belgium-Iran 0-0 result, highlight, evidence, and Group G standings are captured.")
