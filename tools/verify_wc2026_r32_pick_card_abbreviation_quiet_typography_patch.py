#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
GAME1 = ROOT / "site" / "game1" / "index.html"
REQUIRED = [
    ROOT / "li" / "world_cup" / "r32_pick_card_abbreviation_quiet_typography_rule.md",
    ROOT / "docs" / "features" / "r32_pick_card_abbreviation_quiet_typography.md",
    ROOT / "cards" / "092_tune_r32_pick_card_abbreviation_quiet_typography_card.md",
    ROOT / "capture_back" / "CAPTURE_BACK_R32_PICK_CARD_ABBREVIATION_QUIET_TYPOGRAPHY.md",
]


def fail(msg: str) -> None:
    raise SystemExit(msg)


def main() -> None:
    for path in REQUIRED:
        if not path.exists():
            fail(f"Missing required artifact: {path.relative_to(ROOT)}")
    html = GAME1.read_text(encoding="utf-8")
    marker = "wc2026-r32-pick-card-abbreviation-quiet-typography"
    if marker not in html:
        fail("Missing quiet typography CSS marker in site/game1/index.html")
    if "r32TeamAbbreviation(pick)" not in html:
        fail("Game 1 must still render compact card text from r32TeamAbbreviation(pick).")
    quiet_block_match = re.search(r"/\* wc2026-r32-pick-card-abbreviation-quiet-typography \*/(?P<block>.*?)</style>", html, re.S)
    if not quiet_block_match:
        fail("Could not locate final quiet typography CSS block before </style>.")
    block = quiet_block_match.group("block")
    for expected in ["font-weight: 500", "letter-spacing: .02em", "font-family: ui-sans-serif", "text-transform: uppercase"]:
        if expected not in block:
            fail(f"Quiet typography block missing expected declaration: {expected}")
    if re.search(r"font-weight\s*:\s*(8|9)\d\d", block):
        fail("Quiet typography block must not use heavy 800/900+ weights.")
    print("WC2026 R32 pick-card abbreviation quiet-typography checks passed.")


if __name__ == "__main__":
    main()
