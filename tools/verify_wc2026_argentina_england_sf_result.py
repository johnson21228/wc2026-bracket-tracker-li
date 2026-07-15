#!/usr/bin/env python3

import json
from pathlib import Path

RESULTS_PATH = Path("site/data/official_knockout_results.json")
MODEL_PATH = Path("site/js/mvc/model.js")
VIEW_PATH = Path("site/js/mvc/view.js")
BOARD_CSS_PATH = Path("site/css/board.css")
RESULT_ID = "sf-eng-arg-2026-07-15"

data = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
model_source = MODEL_PATH.read_text(encoding="utf-8")
view_source = VIEW_PATH.read_text(encoding="utf-8")
board_css_source = BOARD_CSS_PATH.read_text(encoding="utf-8")
matches = data.get("matches")

assert isinstance(matches, list), "matches must be a list"
assert 'matchDisplay: knockoutMatchDisplayForSlot("FINAL-LEFT")' in model_source
assert 'matchDisplay: knockoutMatchDisplayForSlot("FINAL-RIGHT")' in model_source
assert "row.matchDisplay?.completed && row.matchDisplay.resultLabel" in view_source
assert "pick.matchDisplay?.completed && pick.matchDisplay.resultLabel" in view_source
assert "value.textContent = pick.matchDisplay.resultLabel" in view_source
assert ".final-four-pick-row.has-official-result .final-four-pick-value" in board_css_source

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
    "matchNumber": 102,
    "round": "Semi-final",
    "status": "final",
    "siteWinnerSlotId": "FINAL-RIGHT",
    "siteSlotPair": ["R-SF-01", "R-SF-02"],
    "homeTeamId": "ENG",
    "homeTeamName": "England",
    "homeScore": 1,
    "awayTeamId": "ARG",
    "awayTeamName": "Argentina",
    "awayScore": 2,
    "winnerTeamId": "ARG",
    "winnerTeamName": "Argentina",
    "resultLabel": "England 1–2 Argentina",
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

for feeder_id in (
    "qf-nor-eng-2026-07-11",
    "qf-arg-sui-2026-07-11",
    "sf-fra-esp-2026-07-14",
):
    assert feeder_id in result_ids
    assert result_ids.index(feeder_id) < result_ids.index(RESULT_ID)

print(
    "OK: Argentina defeated England 2–1 in semifinal 102, "
    "Argentina advances to FINAL-RIGHT, and official truth remains append-only."
)
