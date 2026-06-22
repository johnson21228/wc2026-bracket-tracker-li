#!/usr/bin/env python3
from pathlib import Path

view = Path("site/js/mvc/view.js").read_text()
makefile = Path("Makefile").read_text()
capture = Path("captures/CAPTURE_BACK_LATER_ROUND_CHOOSE_WINNER_LABELS.md").read_text()
card = Path("cards/263_later_round_choose_winner_labels_card.md").read_text()
rule = Path("li/world_cup/later_round_choose_winner_labels_rule.md").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require("function emptyPickLabelForSlot(slotId)" in view, "missing slot-aware empty pick label helper")
require('normalizedSlotId.startsWith("R32") ? "Choose Team" : "Choose Winner"' in view, "helper must keep R32 as Choose Team and later rounds as Choose Winner")
require("function updateEmptyPickLabels()" in view, "missing empty pick label updater")
require("updateEmptyPickLabels();" in view, "render/update path must call empty pick label updater")
require("data-pick-id" in view and "data-slot-id" in view and "data-bracket-slot-id" in view, "updater must inspect known slot id hooks")
require("tools/verify_wc2026_later_round_choose_winner_labels.py" in makefile, "Makefile must run later-round label verifier")

for label, text in [("capture", capture), ("card", card), ("rule", rule)]:
    require("Choose Winner" in text, f"{label} must capture Choose Winner language")
    require("R16" in text or "later" in text.lower(), f"{label} must describe later-round scope")

if errors:
    print("WC2026 later-round Choose Winner label verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 empty pick labels use Choose Team for R32 and Choose Winner for R16 and later rounds.")
