#!/usr/bin/env python3

import json
from pathlib import Path

RESULTS_PATH = Path("site/data/official_knockout_results.json")
RESULT_ID = "sf-fra-esp-2026-07-14"

data = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
matches = data.get("matches")

assert isinstance(matches, list), "matches must be a list"

matching = [
    match
    for match in matches
    if isinstance(match, dict) and match.get("resultId") == RESULT_ID
]

assert len(matching) == 1, (
    f"Expected exactly one {RESULT_ID} result, found {len(matching)}"
)

result = matching[0]

expected = {
    "matchId": "53452533",
    "matchNumber": 101,
    "round": "Semi-final",
    "status": "final",
    "siteWinnerSlotId": "FINAL-LEFT",
    "siteSlotPair": ["L-SF-01", "L-SF-02"],
    "homeTeamId": "FRA",
    "homeTeamName": "France",
    "homeScore": 0,
    "awayTeamId": "ESP",
    "awayTeamName": "Spain",
    "awayScore": 2,
    "winnerTeamId": "ESP",
    "winnerTeamName": "Spain",
    "resultLabel": "France 0–2 Spain",
}

for key, expected_value in expected.items():
    actual_value = result.get(key)
    assert actual_value == expected_value, (
        f"{RESULT_ID} {key}: expected {expected_value!r}, "
        f"found {actual_value!r}"
    )

assert "World Cup Final" in result.get("advancementLabel", "")
assert "third-place" in result.get("advancementLabel", "").lower()

result_ids = [
    match.get("resultId")
    for match in matches
    if isinstance(match, dict)
]

assert result_ids[-1] == RESULT_ID, (
    f"{RESULT_ID} must be the newest append-only result"
)

assert "qf-fra-mar-2026-07-09" in result_ids
assert "qf-esp-bel-2026-07-10" in result_ids
assert result_ids.index("qf-fra-mar-2026-07-09") < result_ids.index(RESULT_ID)
assert result_ids.index("qf-esp-bel-2026-07-10") < result_ids.index(RESULT_ID)

print(
    "OK: Spain defeated France 2–0 in semifinal 101, "
    "Spain advances to FINAL-LEFT, and official truth remains append-only."
)
