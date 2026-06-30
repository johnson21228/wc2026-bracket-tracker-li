#!/usr/bin/env python3
import json
from pathlib import Path

errors = []

truth = json.loads(Path("site/data/current/official_truth.json").read_text())
truth_picks = truth.get("picksBySlot", {})
non_r32 = sorted(slot_id for slot_id in truth_picks if "-R32-" not in slot_id)
if non_r32:
    errors.append("official_truth.json must remain R32-only; found: " + ", ".join(non_r32))

results = json.loads(Path("site/data/official_knockout_results.json").read_text())
matches = results.get("matches", [])

def require_result(result_id, expected):
    rows = [match for match in matches if match.get("resultId") == result_id]
    if len(rows) != 1:
        errors.append(f"official_knockout_results.json must contain exactly one {result_id} row.")
        return
    row = rows[0]
    for key, value in expected.items():
        if row.get(key) != value:
            errors.append(f"{result_id} must have {key}={value!r}; found {row.get(key)!r}.")

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

model = Path("site/js/mvc/model.js").read_text()
standings = Path("site/js/standings/SupabasePlayerStandingsStore.js").read_text()

for token in [
    'officialKnockoutResults: "data/official_knockout_results.json"',
    "mergeOfficialKnockoutResultsIntoDocument",
    "pickRecordFromOfficialKnockoutResult",
]:
    if token not in model:
        errors.append(f"model.js missing {token}")

for token in [
    'const SITE_OFFICIAL_KNOCKOUT_RESULTS_URL = "data/official_knockout_results.json";',
    "picksBySlotFromOfficialKnockoutResults",
    "SITE_OFFICIAL_KNOCKOUT_RESULTS_SOURCE",
]:
    if token not in standings:
        errors.append(f"SupabasePlayerStandingsStore.js missing {token}")

if errors:
    print("WC2026 knockout result truth verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: knockout winners are stored in official_knockout_results.json and derived without polluting R32 seed truth.")
