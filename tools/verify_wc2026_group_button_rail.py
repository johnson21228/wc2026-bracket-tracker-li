#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "li/world_cup/group_button_rail_rule.md": [
        "group-button rail",
        "2×2 square flag grid",
        "Group A through Group L",
        "accessible label",
        "must not scrape ESPN",
    ],
    "docs/features/group_button_rail.md": [
        "2×2 square grid",
        "renderGroupRail",
        "getGroupRail",
        "onGroupPanelOpen",
    ],
    "cards/191_define_and_implement_group_button_rail_card.md": [
        "Card 191",
        "Gameboard Group Button Rail",
    ],
    "capture_back/CAPTURE_BACK_GROUP_BUTTON_RAIL.md": [
        "group button rail",
        "2×2 square flag grid",
    ],
    "site/js/mvc/model.js": [
        "getGroupRail",
        "accessibleLabel",
        "Group A",
        "Group L",
    ],
    "site/js/mvc/view.js": [
        "renderGroupRail",
        "data-group-rail-layer",
        "group-rail-flag-grid",
        "data-group-rail-button",
        "onGroupPanelOpen",
    ],
    "site/css/board.css": [
        "board-group-rail-layer",
        "group-rail-tile",
        "group-rail-flag-grid",
        "grid-template-columns: repeat(2",
    ],
}

missing = []
for rel, terms in checks.items():
    path = ROOT / rel
    if not path.exists():
        missing.append(f"missing file: {rel}")
        continue
    text = path.read_text()
    for term in terms:
        if term not in text:
            missing.append(f"{rel} is missing required term: {term}")

if missing:
    raise SystemExit("WC2026 group button rail verification failed:\n- " + "\n- ".join(missing))

print("WC2026 group button rail verification passed.")
