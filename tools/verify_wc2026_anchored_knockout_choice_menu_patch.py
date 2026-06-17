from pathlib import Path

html = Path("site/game1/index.html")
text = html.read_text(encoding="utf-8")
required = [
    "WC2026_ANCHORED_KNOCKOUT_CHOICE_MENU_START",
    "wc2026OpenAnchoredKnockoutChoiceMenu",
    "wc2026AssignChoiceToOpeningCell",
    "wc2026PositionChoiceMenuAdjacentToRule",
    "wc2026CloseAllTooltipSurfaces",
    "menu.dataset.assignmentTargetSlotId",
    "assigns this bracket cell",
    "openAnchoredR16WinnerChoiceMenu",
    "WC2026_ANCHORED_KNOCKOUT_CHOICE_MENU",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing anchored knockout choice menu markers: " + ", ".join(missing))

# Ensure the patch explicitly writes to stored pick state, not just through a floating callback.
assignment_required = [
    "r16Picks[rule.slotId]",
    "saveR16Picks(r16Picks)",
    "advancementPicks[rule.slotId]",
    "saveAdvancementPicks(advancementPicks)",
]
missing_assignment = [item for item in assignment_required if item not in text]
if missing_assignment:
    raise SystemExit("Missing explicit bracket-cell assignment writes: " + ", ".join(missing_assignment))

print("Anchored knockout choice menu assignment verification passed.")
