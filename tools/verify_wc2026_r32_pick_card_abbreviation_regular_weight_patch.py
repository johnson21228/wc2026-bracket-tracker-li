#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GAME1 = ROOT / "site/game1/index.html"
REQ = [
    ROOT / "li/world_cup/r32_pick_card_abbreviation_regular_weight_rule.md",
    ROOT / "docs/features/r32_pick_card_abbreviation_regular_weight.md",
    ROOT / "cards/091_tune_r32_pick_card_abbreviation_regular_weight_card.md",
    ROOT / "prompts/tune_r32_pick_card_abbreviation_regular_weight.md",
    ROOT / "capture_back/CAPTURE_BACK_R32_PICK_CARD_ABBREVIATION_REGULAR_WEIGHT.md",
]

def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def main():
    for p in REQ:
        if not p.exists():
            fail(f"Missing required file: {p.relative_to(ROOT)}")
    html = GAME1.read_text()
    if "r32TeamAbbreviation" not in html:
        fail("Game 1 must keep r32TeamAbbreviation helper for compact card labels.")
    if "r32-abbr-regular-weight" not in html and "r32-pick-abbr" not in html:
        fail("Game 1 should contain an R32 abbreviation typography marker/class.")
    heavy_patterns = [
        r"\.pick-name[^}]*font-weight\s*:\s*(?:700|800|900|950|bold|bolder|black)",
        r"\.r32-pick-abbr[^}]*font-weight\s*:\s*(?:700|800|900|950|bold|bolder|black)",
        r"\.filled-pick[^}]*font-weight\s*:\s*(?:700|800|900|950|bold|bolder|black)",
    ]
    for pat in heavy_patterns:
        if re.search(pat, html, flags=re.I | re.S):
            fail("R32 pick-card abbreviation CSS still appears to use bold/heavy weight.")
    if not re.search(r"font-weight\s*:\s*(?:400|500|normal)", html, flags=re.I):
        fail("Expected regular/medium font-weight in Game 1 HTML.")
    print("WC2026 R32 pick-card abbreviation regular-weight checks passed.")

if __name__ == "__main__":
    main()
