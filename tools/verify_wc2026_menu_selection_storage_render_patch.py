from pathlib import Path

html = Path("site/game1/index.html")
text = html.read_text(encoding="utf-8")

required = [
    "WC2026_MENU_SELECTION_STORAGE_RENDER_START",
    "wc2026MenuAssignmentSlotId",
    "wc2026NormalizeStoredPick",
    "wc2026PersistAndRenderAssignment",
    "assignR16Winner = function wc2026AssignR16WinnerWithStorageRender",
    "assignAdvancementWinner = function wc2026AssignAdvancementWinnerWithStorageRender",
    "r16Picks",
    "saveR16Picks",
    "advancementPicks",
    "saveAdvancementPicks",
    "assignedSlotId",
    "renderPicks",
    "WC2026_MENU_SELECTION_STORAGE_RENDER_CONTRACT",
]

missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing menu selection storage/render markers: " + ", ".join(missing))

print("Menu selection storage/render verification passed.")
