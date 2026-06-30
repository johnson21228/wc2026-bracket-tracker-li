#!/usr/bin/env python3
import json
from pathlib import Path

truth = json.loads(Path("site/data/current/official_truth.json").read_text(encoding="utf-8"))
picks = truth.get("picksBySlot", {})

if picks.get("L-R32-07", {}).get("teamId") != "NED":
    raise SystemExit("official_truth L-R32-07 must remain Netherlands entrant")

if picks.get("L-R32-08", {}).get("teamId") != "MAR":
    raise SystemExit("official_truth L-R32-08 must remain Morocco entrant")

results = json.loads(Path("site/data/official_knockout_results.json").read_text(encoding="utf-8"))
matches = results.get("matches", [])

rows = [
    row for row in matches
    if isinstance(row, dict)
    and (
        row.get("resultId") == "R32-NED-MAR-2026-06-29"
        or row.get("matchId") == "53452547"
        or (
            row.get("homeTeamId") == "NED"
            and row.get("awayTeamId") == "MAR"
        )
    )
]

if len(rows) != 1:
    raise SystemExit(f"Expected exactly one NED-MAR official knockout result row, found {len(rows)}")

row = rows[0]

expected = {
    "homeTeamId": "NED",
    "awayTeamId": "MAR",
    "winnerTeamId": "MAR",
    "homeScore": 2,
    "awayScore": 2,
    "homePenaltyScore": 2,
    "awayPenaltyScore": 3,
    "decidedBy": "penalties",
}

for key, value in expected.items():
    if row.get(key) != value:
        raise SystemExit(f"NED-MAR result {key} expected {value!r}, found {row.get(key)!r}")

blob = json.dumps(row, ensure_ascii=False, sort_keys=True)
for token in ["Netherlands", "Morocco", "3–2"]:
    if token not in blob:
        raise SystemExit(f"NED-MAR result missing token: {token}")

print("OK: official knockout results record Morocco penalty win over Netherlands, while entrant truth is preserved.")
