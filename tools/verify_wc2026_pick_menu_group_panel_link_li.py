#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "li/world_cup/pick_menu_group_panel_link_rule.md": [
        "collect choices by group",
        "show the group label",
        "opens the group standings panel",
        "model owns choice eligibility and group identity",
        "view owns grouped rendering",
        "controller owns the event",
        "must not scrape ESPN",
    ],
    "docs/features/pick_menu_group_panel_link.md": [
        "choices collected by group",
        "open the shared group standings panel",
        "3RD A/E/H/I/J",
    ],
    "capture_back/CAPTURE_BACK_PICK_MENU_GROUP_PANEL_LINK_LI.md": [
        "group-derived choices",
        "clickable/tappable",
        "local group panel",
        "browser runtime consumes local checked-in JSON",
    ],
    "cards/184_define_pick_menu_group_panel_link_li_card.md": [
        "Card 184",
        "pick-menu group panel link LI",
    ],
}

missing = []
for rel, needles in REQUIRED.items():
    path = ROOT / rel
    if not path.exists():
        missing.append(f"missing file: {rel}")
        continue
    text = path.read_text()
    for needle in needles:
        if needle not in text:
            missing.append(f"{rel} missing required text: {needle}")

makefile = ROOT / "Makefile"
if not makefile.exists():
    missing.append("missing Makefile")
else:
    text = makefile.read_text()
    if "python3 tools/verify_wc2026_pick_menu_group_panel_link_li.py" not in text:
        missing.append("Makefile verify target must run pick menu group panel link LI verifier")

if missing:
    print("WC2026 pick menu group panel link LI verification failed:")
    for item in missing:
        print(f"- {item}")
    raise SystemExit(1)

print("WC2026 pick menu group panel link LI verification passed.")
