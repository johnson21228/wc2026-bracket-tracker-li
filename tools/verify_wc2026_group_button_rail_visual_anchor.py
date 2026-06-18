#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
checks = {
    "li/world_cup/group_button_rail_rule.md": [
        "partially translucent",
        "fully opaque",
        "hover",
        "focuses",
        "button that launched it",
        "scrollable gameboard plane",
    ],
    "docs/features/group_button_rail.md": [
        "partially translucent",
        "fully opaque",
        "launching group control",
        "board-attached",
    ],
    "site/css/board.css": [
        "group-rail-tile",
        "opacity: .66",
        "group-rail-tile:hover",
        "group-rail-tile:focus-visible",
        "group-rail-tile:active",
        "group-panel-popover",
    ],
    "site/js/mvc/view.js": [
        "boardBoundsForElement",
        "placeGroupPanel",
        "anchorBoundsPx",
        "onGroupPanelOpen?.(group.groupId, boardBoundsForElement",
        "openGroupPanel(groupContext, anchorBoundsPx",
    ],
    "site/js/mvc/controller.js": [
        "onGroupPanelOpen(groupId, anchorBoundsPx",
        "view.openGroupPanel(groupContext, anchorBoundsPx)",
    ],
    "cards/192_refine_group_button_rail_visual_anchor_card.md": [
        "Card 192",
        "Visual Emphasis",
        "Anchored Panel",
    ],
    "capture_back/CAPTURE_BACK_GROUP_BUTTON_RAIL_VISUAL_ANCHOR.md": [
        "Group Button Rail Visual Anchor",
        "partially translucent",
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
    raise SystemExit("WC2026 group button rail visual anchor verification failed:\n- " + "\n- ".join(missing))

print("WC2026 group button rail visual anchor verification passed.")
