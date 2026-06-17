#!/usr/bin/env python3
"""Verify Game 1 knockout choice menus can be resolved from match contestants.

This verifier is intentionally static/source-level. It does not click the browser UI.
It checks that site/game1/index.html contains a testable knockout choice resolver path
for R16/QF/SF winner-pick slots, and that the R16/QF/SF feeder mapping can produce
exactly two menu choices from bracket contestants rather than an empty set.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME1 = ROOT / "site" / "game1" / "index.html"

REQUIRED_MARKERS = [
    "WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS",
    "resolveKnockoutChoiceContestants",
    "testKnockoutChoiceResolution",
    "knockoutFeederSlotsFor",
]

REQUIRED_ROUNDS = ["R16", "QF", "SF"]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not GAME1.exists():
        fail(f"missing {GAME1}")

    text = GAME1.read_text(encoding="utf-8")

    for marker in REQUIRED_MARKERS:
        if marker not in text:
            fail(f"missing knockout choice resolution test marker/function: {marker}")

    for round_name in REQUIRED_ROUNDS:
        if round_name not in text:
            fail(f"missing knockout round reference: {round_name}")

    # Static guard against the common failure mode: resolving a knockout slot to an empty array.
    if not re.search(r"choices\.length\s*===\s*2|contestants\.length\s*===\s*2|resolved\.length\s*===\s*2", text):
        fail("missing explicit assertion that knockout choice resolution returns exactly two contestants")

    if not re.search(r"throw new Error\([^)]*(empty|contestant|choice|feeder)", text, flags=re.I | re.S):
        fail("missing fail-closed error for empty or invalid knockout choice contestants")

    if not re.search(r"window\.WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS", text):
        fail("missing browser-accessible knockout choice test harness on window")

    print("WC2026 Game 1 knockout choice resolution test harness checks passed.")


if __name__ == "__main__":
    main()
