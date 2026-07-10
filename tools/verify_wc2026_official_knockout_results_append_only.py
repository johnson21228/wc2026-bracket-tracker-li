#!/usr/bin/env python3
import json
from pathlib import Path

errors = []
path = Path("site/data/official_knockout_results.json")
results = json.loads(path.read_text())
matches = results.get("matches", [])

if not isinstance(matches, list):
    errors.append("official_knockout_results.json must contain a matches array.")
    matches = []

ids = [match.get("resultId") for match in matches if isinstance(match, dict)]
duplicates = sorted({result_id for result_id in ids if result_id and ids.count(result_id) > 1})
if duplicates:
    errors.append("official_knockout_results.json has duplicate resultId rows: " + ", ".join(duplicates))

def require_result(result_id, expected):
    rows = [match for match in matches if isinstance(match, dict) and match.get("resultId") == result_id]
    if len(rows) != 1:
        errors.append(f"Expected exactly one protected result row for {result_id}; found {len(rows)}.")
        return
    row = rows[0]
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"{result_id} must keep {key}={value!r}; found {row.get(key)!r}.")

require_result("r32-rsa-can-2026-06-28", {
    "siteWinnerSlotId": "L-R16-03",
    "homeTeamId": "RSA",
    "homeScore": 0,
    "awayTeamId": "CAN",
    "awayScore": 1,
    "winnerTeamId": "CAN",
})

require_result("r32-bra-jpn-2026-06-29", {
    "siteWinnerSlotId": "R-R16-01",
    "homeTeamId": "BRA",
    "homeScore": 2,
    "awayTeamId": "JPN",
    "awayScore": 1,
    "winnerTeamId": "BRA",
})

require_result("r32-civ-nor-2026-07-01", {
    "siteWinnerSlotId": "R-R16-02",
    "homeTeamId": "CIV",
    "homeScore": 1,
    "awayTeamId": "NOR",
    "awayScore": 2,
    "winnerTeamId": "NOR",
})

require_result("r32-fra-swe-2026-06-30", {
    "siteWinnerSlotId": "L-R16-02",
    "homeTeamId": "FRA",
    "homeScore": 3,
    "awayTeamId": "SWE",
    "awayScore": 0,
    "winnerTeamId": "FRA",
})

require_result("r32-mex-ecu-2026-06-30", {
    "siteWinnerSlotId": "R-R16-03",
    "homeTeamId": "MEX",
    "homeScore": 2,
    "awayTeamId": "ECU",
    "awayScore": 0,
    "winnerTeamId": "MEX",
})


require_result("r16-bra-nor-2026-07-05", {
    "siteWinnerSlotId": "R-QF-01",
    "homeTeamId": "BRA",
    "homeScore": 1,
    "awayTeamId": "NOR",
    "awayScore": 2,
    "winnerTeamId": "NOR",
})



require_result("r16-mex-eng-2026-07-05", {
    "siteWinnerSlotId": "R-QF-02",
    "homeTeamId": "MEX",
    "homeScore": 2,
    "awayTeamId": "ENG",
    "awayScore": 3,
    "winnerTeamId": "ENG",
})



require_result("r16-sui-col-2026-07-07", {
    "siteWinnerSlotId": "R-QF-04",
    "homeTeamId": "SUI",
    "homeScore": 0,
    "awayTeamId": "COL",
    "awayScore": 0,
    "winnerTeamId": "SUI",
    "resultType": "penalties",
    "homePenaltyScore": 4,
    "awayPenaltyScore": 3,
})
require_result("qf-esp-bel-2026-07-10", {
    "round": "Quarter-final",
    "siteWinnerSlotId": "L-SF-02",
    "siteSlotPair": ["L-QF-03", "L-QF-04"],
    "homeTeamId": "ESP",
    "homeScore": 2,
    "awayTeamId": "BEL",
    "awayScore": 1,
    "winnerTeamId": "ESP",
    "resultLabel": "Spain 2–1 Belgium",
    "advancementLabel": "Spain advances to face France in the semifinal",
})


truth = json.loads(Path("site/data/current/official_truth.json").read_text())
truth_picks = truth.get("picksBySlot", {})
non_r32 = sorted(slot_id for slot_id in truth_picks if "-R32-" not in slot_id)
if non_r32:
    errors.append("official_truth.json must remain R32 seed only; non-R32 slots found: " + ", ".join(non_r32))

if errors:
    print("WC2026 official knockout results append-only verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: official knockout results preserve CAN/RSA, include BRA/JPN, avoid duplicates, and keep official_truth R32-only.")
