#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME1 = ROOT / "site" / "game1" / "index.html"
REQUIRED = [
    ROOT / "li" / "world_cup" / "game1_choice_legibility_hit_rule.md",
    ROOT / "docs" / "features" / "game1_choice_legibility_hit_rule.md",
    ROOT / "cards" / "102_repair_game1_choice_legibility_hit_rule_card.md",
    ROOT / "prompts" / "repair_game1_choice_legibility_hit_rule.md",
    ROOT / "capture_back" / "CAPTURE_BACK_GAME1_CHOICE_LEGIBILITY_HIT_RULE.md",
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

    if "choiceTeamName" not in html or "choiceAbbr" not in html or "choiceGroup" not in html:
        fail("Chooser row does not use separate choiceTeamName / choiceAbbr / choiceGroup spans")
    if "choiceMeta" not in html:
        fail("Chooser row is missing a dedicated choiceMeta span")
    if "${teamName} ${teamAbbr}" not in html and "data-choice-text" not in html:
        fail("Chooser row does not expose a readable separated team-name/team-abbreviation string")
    if "FranceFRA" in html or "SenegalSEN" in html:
        fail("Compressed sample choice text appears in Game 1 HTML")
    if "margin-left:auto" in re.sub(r"\s+", "", html.split(".choice .meta", 1)[-1][:160]) and "choiceMeta" not in html:
        fail("Legacy auto-pushed .choice .meta pattern appears to remain active without new choiceMeta markup")

    if "window.WC2026_GAME1_CHOICE_LEGIBILITY_HIT_RULE" not in html:
        fail("Runtime choice legibility / hit rule probe is missing")

    for slot, groups in EXPECTED_GROUPS.items():
        group_literal = ",".join(f'"{g}"' for g in groups)
        if slot not in html:
            fail(f"Expected slot {slot} not present in Game 1 HTML")
        # The runtime probe may encode expected groups in JSON-like arrays.
        if group_literal not in html:
            fail(f"Expected group mapping for {slot} not encoded as [{group_literal}]")

    print("WC2026 Game 1 choice legibility and hit-rule integrity checks passed.")


if __name__ == "__main__":
    main()
