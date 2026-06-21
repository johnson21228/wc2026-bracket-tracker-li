#!/usr/bin/env python3
import json
from pathlib import Path

MATCH_ID = "66456998"
POSTER_MATCH_ID = "GS-2026-06-21-H4"
HIGHLIGHT_URL = "https://youtu.be/w453UjgtQw4"

def main() -> int:
    errors = []

    matches = json.loads(Path("site/data/current/group_matches.json").read_text())["matches"]
    target = next(
        (
            match for match in matches
            if str(match.get("espnMatchId")) == MATCH_ID
            or str(match.get("matchId")) == MATCH_ID
            or str(match.get("posterMatchId")) == POSTER_MATCH_ID
        ),
        None,
    )

    if not target:
        errors.append("missing Spain-Saudi match")
    else:
        expected = {
            "status": "final",
            "groupId": "H",
            "homeTeamId": "ESP",
            "awayTeamId": "KSA",
            "homeScore": 4,
            "awayScore": 0,
            "summary": "Spain 4-0 Saudi Arabia",
        }
        for key, value in expected.items():
            if target.get(key) != value:
                errors.append(f"match {key} expected {value!r}, found {target.get(key)!r}")

    highlights = json.loads(Path("site/data/current/match_highlights.json").read_text())["highlights"]
    highlight = highlights.get(MATCH_ID)
    if not highlight:
        errors.append("missing Spain-Saudi highlight")
    else:
        if highlight.get("url") != HIGHLIGHT_URL:
            errors.append("Spain-Saudi highlight URL mismatch")
        if highlight.get("matchEvidence") != "Spain 4-0 Saudi Arabia":
            errors.append("Spain-Saudi highlight matchEvidence mismatch")

    standings = json.loads(Path("site/data/current/group_standings.json").read_text())
    group_h = standings["groups"]["H"]["entries"]
    spain = next((entry for entry in group_h if entry.get("teamId") == "ESP"), None)
    saudi = next((entry for entry in group_h if entry.get("teamId") == "KSA"), None)
    if not spain:
        errors.append("missing Spain in Group H standings")
    else:
        checks = {
            "played": 2,
            "wins": 1,
            "draws": 1,
            "losses": 0,
            "goalsFor": 4,
            "goalsAgainst": 0,
            "goalDifference": 4,
            "points": 4,
            "rank": 1,
        }
        for key, value in checks.items():
            if spain.get(key) != value:
                errors.append(f"Spain standings {key} expected {value!r}, found {spain.get(key)!r}")

    if not saudi:
        errors.append("missing Saudi Arabia in Group H standings")
    elif saudi.get("goalsAgainst") != 5 or saudi.get("played") != 2:
        errors.append("Saudi Arabia standings did not absorb 4-0 loss")

    evidence = Path("source/text/group_result_evidence_20260621_spain_saudi.json")
    capture = Path("captures/CAPTURE_BACK_SPAIN_SAUDI_RESULT_AND_HIGHLIGHT.md")
    card = Path("cards/245_capture_spain_saudi_result_card.md")
    for path in [evidence, capture, card]:
        if not path.exists():
            errors.append(f"missing {path}")

    if errors:
        print("WC2026 Spain-Saudi result verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 Spain 4-0 Saudi Arabia result, highlight, evidence, and Group H standings are captured.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
