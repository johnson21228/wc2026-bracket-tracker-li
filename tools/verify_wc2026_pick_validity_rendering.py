#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

def require(path, token):
    text = read(path)
    if token not in text:
        raise SystemExit(f"Missing token in {path}: {token}")

# LI/docs/card/capture
for path, tokens in {
    "li/world_cup/pick_validity_rendering_rule.md": [
        "A user pick is durable user intent",
        "thin red outline",
        "red `!` marker",
        "Auto-clearing invalid picks is not the default behavior",
    ],
    "docs/features/pick_validity_rendering.md": [
        "thin red outline",
        "red `!` badge",
        "The model no longer auto-clears invalid descendant picks by default",
    ],
    "cards/205_preserve_picks_render_invalid_warnings_card.md": ["Card 205", "thin red outline", "red `!` marker"],
    "capture_back/CAPTURE_BACK_PICK_VALIDITY_RENDERING.md": ["thin red outline", "red `!` marker"],
}.items():
    for token in tokens:
        require(path, token)

# Model must compute validity and preserve picks.
model = read("site/js/mvc/model.js")
for token in [
    "function pickValidityForSlot",
    "not one of the current feeder teams for this winner slot",
    "validityChoices = choices.length ? choices : knownFeederChoices",
    "getFinalFourKnownFeederChoicesForValidity",
    "function getKnownFeederChoicesForValidity",
    "function standingsEntryForTeam",
    "pickValidityForSlot",
    "duplicateR32Pick",
    "pickValidity: pickValidityForSlot(slot, team)",
    "preserve invalid picks; render pick validity instead of auto-clearing",
]:
    if token not in model:
        raise SystemExit(f"Missing model token: {token}")

set_pick_block = model[model.find("function setPick") : model.find("function clearPick")]
if "if (!validation.valid)" in set_pick_block or "cascadeClearInvalidDescendants()" in set_pick_block:
    raise SystemExit("setPick must preserve picks instead of blocking/clearing invalid picks")

# View/CSS must render invalid warning state.
for token in [
    "picked-cell-warning",
    "has-invalid-pick",
    "slot.pickValidity?.state === \"invalid\"",
    "slot.pickValidity.reason || \"Invalid pick\"",
]:
    require("site/js/mvc/view.js", token)

for token in [
    "Card 205: invalid pick warning rendering",
    ".pick-slot-button.has-invalid-pick",
    "outline: 1px solid rgba(255, 64, 64, .95)",
    ".picked-cell-warning",
    "background: rgba(180, 0, 0, .92)",
]:
    require("site/css/board.css", token)

require("Makefile", "tools/verify_wc2026_pick_validity_rendering.py")
print("OK: WC2026 pick validity rendering preserves invalid picks and renders red warnings.")
