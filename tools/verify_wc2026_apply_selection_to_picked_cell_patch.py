from pathlib import Path

text = Path("site/game1/index.html").read_text(encoding="utf-8")
required = [
    "WC2026_APPLY_SELECTION_TO_PICKED_CELL",
    "selection-applied-to-picked-cell-v001",
    "assignedSlotId",
    "assignmentTargetSlotId",
    "r16Picks[",
    "saveR16Picks",
    "advancementPicks[",
    "saveAdvancementPicks",
    "window.game1KnockoutPicks",
    "renderPicks();",
    "closeMenu();",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing apply-selection-to-picked-cell markers: " + ", ".join(missing))
print("Apply selection to picked cell verification passed.")
