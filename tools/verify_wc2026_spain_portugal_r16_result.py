#!/usr/bin/env python3
import json
from pathlib import Path

errors = []
results = json.loads(Path("site/data/official_knockout_results.json").read_text(encoding="utf-8"))
matches = results.get("matches", [])
result_id = "r16-por-esp-2026-07-06"
rows = [match for match in matches if isinstance(match, dict) and match.get("resultId") == result_id]

if len(rows) != 1:
    errors.append(f"Expected exactly one {result_id} row; found {len(rows)}.")
else:
    row = rows[0]
    expected = {
        "round": "Round of 16",
        "siteWinnerSlotId": "L-QF-03",
        "siteSlotPair": ["L-R16-05", "L-R16-06"],
        "homeTeamId": "POR",
        "homeTeamName": "Portugal",
        "homeScore": 0,
        "awayTeamId": "ESP",
        "awayTeamName": "Spain",
        "awayScore": 1,
        "winnerTeamId": "ESP",
        "winnerTeamName": "Spain",
        "resultLabel": "Spain 1–0 Portugal",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"{result_id} must keep {key}={value!r}; found {row.get(key)!r}.")

truth = json.loads(Path("site/data/current/official_truth.json").read_text(encoding="utf-8"))
truth_picks = truth.get("picksBySlot", {})
if "L-QF-03" in truth_picks:
    errors.append("official_truth.json must not be polluted with the R16 winner in L-QF-03.")

if errors:
    print("WC2026 Spain Portugal R16 result verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Spain 1–0 Portugal official R16 result advances Spain to L-QF-03 without polluting R32 seed truth.")
