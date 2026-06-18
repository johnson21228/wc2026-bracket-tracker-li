#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "cards/185_define_pick_menu_interaction_placement_li_card.md",
    "li/world_cup/pick_menu_interaction_placement_rule.md",
    "docs/features/pick_menu_interaction_placement.md",
    "capture_back/CAPTURE_BACK_PICK_MENU_INTERACTION_PLACEMENT_LI.md",
]

REQUIRED_TERMS = {
    "li/world_cup/pick_menu_interaction_placement_rule.md": [
        "clear-pick action near the top",
        "prominent close button",
        "displayed next to the bracket slot",
        "scrollable game board plane",
        "scrolls with the game board",
        "fully visible within the current visible board viewport",
        "group-panel evidence link",
        "Model owns",
        "View owns",
        "Controller owns",
        "must not select a team",
        "must not be fixed to the browser viewport",
    ],
    "docs/features/pick_menu_interaction_placement.md": [
        "clear-pick action near the top",
        "prominent close button",
        "placed beside the slot",
        "scrolls with the board",
        "group label is clickable",
    ],
}


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    sys.exit(1)


def main() -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            fail(f"Missing required file: {rel}")

    for rel, terms in REQUIRED_TERMS.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        missing = [term for term in terms if term not in text]
        if missing:
            fail(f"{rel} is missing required terms: {missing}")

    makefile = ROOT / "Makefile"
    text = makefile.read_text(encoding="utf-8")
    expected = "python3 tools/verify_wc2026_pick_menu_interaction_placement_li.py"
    if expected not in text:
        fail("Makefile verify target does not run pick menu interaction placement LI verifier")

    print("WC2026 pick menu interaction placement LI verification passed.")


if __name__ == "__main__":
    main()
