#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "site/js/mvc/model.js": [
        "getPickMenu",
        "getGroupedPickChoices",
        "currentPick",
        "canClear",
        "panelAvailable",
        "sourceTitleForSlot",
    ],
    "site/js/mvc/view.js": [
        "pick-menu-close-button",
        "pick-menu-clear-top",
        "data-group-panel-action",
        "placePickMenu",
        "scrolls with the game board",
        "renderGroupPanel",
    ],
    "site/js/mvc/controller.js": [
        "onCloseMenu",
        "onClearPick",
        "onGroupPanelOpen",
        "getPickMenu",
        "getGroupContext",
    ],
    "site/css/board.css": [
        "pick-menu-topbar",
        "pick-menu-group-label",
        "pick-menu-clear-top",
        "group-panel-popover",
    ],
    "docs/features/pick_menu_runtime_v2.md": [
        "grouped candidate choices",
        "scrolls with the game board",
        "does not fetch, parse, or scrape ESPN",
    ],
    "cards/186_implement_pick_menu_runtime_v2_card.md": [
        "Card 186",
        "Implement Pick Menu Runtime v2",
    ],
    "capture_back/CAPTURE_BACK_PICK_MENU_RUNTIME_V2.md": [
        "Pick Menu Runtime v2",
        "does not scrape ESPN",
    ],
}

missing = []
for rel, required_terms in checks.items():
    path = ROOT / rel
    if not path.exists():
        missing.append(f"missing file: {rel}")
        continue
    text = path.read_text()
    for term in required_terms:
        if term not in text:
            missing.append(f"{rel} is missing required term: {term}")

if missing:
    raise SystemExit("WC2026 pick menu runtime v2 verification failed:\n- " + "\n- ".join(missing))

print("WC2026 pick menu runtime v2 verification passed.")
