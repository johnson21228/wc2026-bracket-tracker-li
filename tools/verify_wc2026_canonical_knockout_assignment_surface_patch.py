from pathlib import Path

text = Path("site/game1/index.html").read_text(encoding="utf-8")
required = [
    "WC2026_CANONICAL_KNOCKOUT_ASSIGNMENT_SURFACE_START",
    "window.WC2026_KNOCKOUT_ASSIGNMENT_SURFACE",
    "wc2026CanonicalApplySelection",
    "r16Picks[slotId] = storedPick",
    "advancementPicks[slotId] = storedPick",
    "saveR16Picks(r16Picks)",
    "saveAdvancementPicks(advancementPicks)",
    "wc2026CanonicalRenderCell",
    "openR16Menu = function openCanonicalR16Menu",
    "menu.dataset.assignmentTargetSlotId = slotId",
]
forbidden = [
    "WC2026_ANCHORED_KNOCKOUT_CHOICE_MENU_START",
    "WC2026_APPLY_SELECTION_TO_PICKED_CELL_FALLBACK_START",
    "WC2026_MENU_SELECTION_STORAGE_RENDER_START",
]
missing = [s for s in required if s not in text]
present_forbidden = [s for s in forbidden if s in text]
if missing:
    raise SystemExit("Missing canonical assignment surface markers: " + ", ".join(missing))
if present_forbidden:
    raise SystemExit("Competing assignment wrapper markers still present: " + ", ".join(present_forbidden))
print("Canonical knockout assignment surface verification passed.")
