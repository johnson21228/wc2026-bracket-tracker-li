#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
metadata_path = root / "site/data/knockout_match_display_metadata.json"
model_path = root / "site/js/mvc/model.js"
view_path = root / "site/js/mvc/view.js"
truth_path = root / "site/data/current/official_truth.json"

payload = json.loads(metadata_path.read_text())
matches = payload.get("matches", [])
assert payload.get("schema") == "wc2026.knockout_match_display_metadata.v1"
assert len(matches) == 32, f"expected 32 knockout display metadata rows, found {len(matches)}"

seen = set()
for match in matches:
    slot = match.get("siteWinnerSlotId")
    assert slot and slot not in seen, f"missing/duplicate siteWinnerSlotId: {slot}"
    seen.add(slot)
    assert isinstance(match.get("extendedHighlightsUrl"), str), f"extendedHighlightsUrl must be a string for {slot}"
    assert match.get("date"), f"missing date for {slot}"
    assert match.get("kickoffIso"), f"missing kickoffIso for {slot}"
    assert match.get("fixtureLabel"), f"missing fixtureLabel for {slot}"

model = model_path.read_text()
view = view_path.read_text()
assert "knockoutMatchDisplayMetadata" in model
assert "knockoutMatchDisplayForSlot" in model
assert "teamNameForKnockoutSourceSlot" in model
assert "fixtureLabelForKnockoutDisplay" in model
assert "const matchDisplay = knockoutMatchDisplayForSlot(slotId)" in model
assert "pickable: choices.length > 0 || Boolean(matchDisplay)" in model
assert "groups: matchDisplay ? [] : getGroupedPickChoices(slotId)" in model
assert "choices: matchDisplay ? [] : choices" in model
assert "canClear: Boolean(currentPick) && !matchDisplay" in model
assert "Match result" in view
assert "Match details" in view
assert "Extended highlights" in view
assert truth_path.exists(), "official_truth.json missing; verifier does not modify it"

print("OK: knockout match display metadata is present and wired into the pick/result menu.")
