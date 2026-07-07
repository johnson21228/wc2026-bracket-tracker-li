#!/usr/bin/env python3
from pathlib import Path
import json

path = Path("site/data/official_knockout_results.json")
data = json.loads(path.read_text(encoding="utf-8"))
matches = data.get("matches", [])

rows = [m for m in matches if isinstance(m, dict) and m.get("resultId") == "r16-sui-col-2026-07-07"]
errors = []

if len(rows) != 1:
    errors.append(f"Expected exactly one SUI/COL R16 result row; found {len(rows)}.")
else:
    row = rows[0]
    expected = {
        "round": "Round of 16",
        "status": "final",
        "resultType": "penalties",
        "siteWinnerSlotId": "R-QF-04",
        "homeTeamId": "SUI",
        "homeScore": 0,
        "awayTeamId": "COL",
        "awayScore": 0,
        "homePenaltyScore": 4,
        "awayPenaltyScore": 3,
        "winnerTeamId": "SUI",
        "decidedBy": "penalties",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"SUI/COL row must have {key}={value!r}; found {row.get(key)!r}.")
    if row.get("siteSlotPair") != ["R-R16-07", "R-R16-08"]:
        errors.append(f"SUI/COL row must feed from R-R16-07/R-R16-08; found {row.get('siteSlotPair')!r}.")
    if row.get("penaltyScoreByTeamId") != {"SUI": 4, "COL": 3}:
        errors.append(f"SUI/COL penaltyScoreByTeamId is wrong: {row.get('penaltyScoreByTeamId')!r}.")
    label = row.get("resultLabel", "")
    if "Switzerland" not in label or "4–3" not in label or "penalties" not in label:
        errors.append(f"SUI/COL resultLabel does not describe the penalty result clearly: {label!r}.")

ids = [m.get("resultId") for m in matches if isinstance(m, dict)]
dupes = sorted({result_id for result_id in ids if result_id and ids.count(result_id) > 1})
if dupes:
    errors.append("Duplicate official knockout result IDs found: " + ", ".join(dupes))

if errors:
    print("WC2026 Switzerland Colombia knockout result verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Switzerland 0–0 Colombia; Switzerland advances 4–3 on penalties.")
