#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME1 = ROOT / "site" / "game1" / "index.html"
REQUIRED = [
    ROOT / "li" / "world_cup" / "game1_choice_text_spacing_rule.md",
    ROOT / "docs" / "features" / "game1_choice_text_spacing_repair.md",
    ROOT / "cards" / "103_repair_game1_choice_text_spacing_card.md",
    ROOT / "prompts" / "repair_game1_choice_text_spacing.md",
    ROOT / "capture_back" / "CAPTURE_BACK_GAME1_CHOICE_TEXT_SPACING_REPAIR.md",
]
EXPECTED_GROUPS = {
    "R32-L-M4A": ["I"],
    "R32-L-M4B": ["C", "D", "F", "G", "H"],
    "R32-L-M7B": ["C", "E", "F", "H", "I"],
    "R32-L-M8B": ["E", "H", "I", "J", "K"],
    "R32-R-M3B": ["B", "E", "F", "I", "J"],
    "R32-R-M8B": ["D", "E", "I", "J", "L"],
}

def fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    raise SystemExit(1)

def main() -> None:
    for path in REQUIRED:
        if not path.exists():
            fail(f"Missing required artifact: {path.relative_to(ROOT)}")
    if not GAME1.exists():
        fail("Missing site/game1/index.html")
    html = GAME1.read_text(encoding="utf-8")
    for token in ["choiceText", "choiceTeamName", "choiceMeta", "choiceAbbr", "choiceGroup"]:
        if token not in html:
            fail(f"Chooser row missing {token}")
    compact_html = re.sub(r"\s+", "", html)
    if "game1_choice_text_spacing_repair" not in html:
        fail("Missing choice text spacing repair CSS marker")
    if "gap:12px" not in compact_html:
        fail("Choice text wrapper does not define an explicit visual gap")
    if "${teamName}</span><spanclass=\"choiceMeta" in compact_html:
        fail("Team name and metadata remain adjacent without choiceText wrapper")
    if "MexicoMEX" in html or "FranceFRA" in html or "SenegalSEN" in html:
        fail("Compressed example text appears in HTML")
    if "window.WC2026_GAME1_CHOICE_TEXT_SPACING_REPAIR" not in html:
        fail("Runtime spacing probe is missing")
    for slot, groups in EXPECTED_GROUPS.items():
        if slot not in html:
            fail(f"Expected hit/rule integrity slot {slot} not present")
        literal = ",".join(f'"{g}"' for g in groups)
        if literal not in html:
            fail(f"Expected group mapping for {slot} not encoded as [{literal}]")
    print("WC2026 Game 1 choice text spacing repair checks passed.")

if __name__ == "__main__":
    main()
