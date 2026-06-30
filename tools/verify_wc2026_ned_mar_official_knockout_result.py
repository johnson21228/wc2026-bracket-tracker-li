#!/usr/bin/env python3
import json
from pathlib import Path

seed = json.loads(Path("site/data/current/official_truth.json").read_text(encoding="utf-8"))
results = json.loads(Path("site/data/official_knockout_results.json").read_text(encoding="utf-8"))

picks = seed.get("picksBySlot", {})
matches = results.get("matches", [])

# Seed truth must remain entrant-only.
if picks.get("L-R32-07", {}).get("teamId") != "NED":
    raise SystemExit("L-R32-07 must remain Netherlands R32 entrant in official_truth.json.")

if picks.get("L-R32-08", {}).get("teamId") != "MAR":
    raise SystemExit("L-R32-08 must remain Morocco R32 entrant in official_truth.json.")

rows = [
    row for row in matches
    if isinstance(row, dict)
    and (
        row.get("resultId") == "r32-ned-mar-2026-06-29"
        or row.get("matchId") == "53452547"
        or (
            row.get("homeTeamId") == "NED"
            and row.get("awayTeamId") == "MAR"
        )
    )
]

if len(rows) != 1:
    raise SystemExit(f"Expected exactly one NED-MAR official knockout result row, found {len(rows)}.")

row = rows[0]

expected = {
    "resultId": "r32-ned-mar-2026-06-29",
    "matchId": "53452547",
    "round": "R32",
    "status": "final",
    "resultType": "penalties",
    "siteWinnerSlotId": "L-R16-04",
    "homeTeamId": "NED",
    "homeTeamName": "Netherlands",
    "homeScore": 1,
    "awayTeamId": "MAR",
    "awayTeamName": "Morocco",
    "awayScore": 1,
    "homePenaltyScore": 2,
    "awayPenaltyScore": 3,
    "winnerTeamId": "MAR",
    "winnerTeamName": "Morocco",
    "decidedBy": "penalties",
}

for key, value in expected.items():
    if row.get(key) != value:
        raise SystemExit(f"NED-MAR {key} expected {value!r}, found {row.get(key)!r}.")

if row.get("siteSlotPair") != ["L-R32-07", "L-R32-08"]:
    raise SystemExit(f"NED-MAR siteSlotPair is wrong: {row.get('siteSlotPair')!r}")

blob = json.dumps(row, ensure_ascii=False, sort_keys=True)
for token in ["Netherlands 1–1 Morocco", "Morocco advances 3–2", "NED 1–1 MAR"]:
    if token not in blob:
        raise SystemExit(f"NED-MAR result row missing display token: {token}")

# No official knockout result may mark Netherlands as winner for this match.
for candidate in rows:
    if candidate.get("winnerTeamId") == "NED":
        raise SystemExit("NED-MAR truth incorrectly marks Netherlands as winner.")

print("OK: NED-MAR truth is correct: entrants preserved, Morocco advances to L-R16-04, score 1–1, penalties 3–2.")
