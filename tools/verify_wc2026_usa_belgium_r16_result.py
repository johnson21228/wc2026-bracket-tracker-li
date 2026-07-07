#!/usr/bin/env python3
import json
from pathlib import Path

errors = []
results = json.loads(Path("site/data/official_knockout_results.json").read_text(encoding="utf-8"))
matches = results.get("matches", [])
result_id = "r16-usa-bel-2026-07-06"
rows = [match for match in matches if isinstance(match, dict) and match.get("resultId") == result_id]

if len(rows) != 1:
    errors.append(f"Expected exactly one {result_id} row; found {len(rows)}.")
else:
    row = rows[0]
    expected = {
        "round": "Round of 16",
        "siteWinnerSlotId": "L-QF-04",
        "siteSlotPair": ["L-R16-07", "L-R16-08"],
        "homeTeamId": "USA",
        "homeTeamName": "United States",
        "homeScore": 1,
        "awayTeamId": "BEL",
        "awayTeamName": "Belgium",
        "awayScore": 4,
        "winnerTeamId": "BEL",
        "winnerTeamName": "Belgium",
        "resultLabel": "Belgium 4–1 United States",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"{result_id} must keep {key}={value!r}; found {row.get(key)!r}.")

truth = json.loads(Path("site/data/current/official_truth.json").read_text(encoding="utf-8"))
truth_picks = truth.get("picksBySlot", {})
if "L-QF-04" in truth_picks:
    errors.append("official_truth.json must not be polluted with the R16 winner in L-QF-04.")

if errors:
    print("WC2026 USA Belgium R16 result verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Belgium 4–1 United States official R16 result advances Belgium to L-QF-04 without polluting R32 seed truth.")
