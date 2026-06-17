#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path.cwd()
html = root / "site" / "index.html"
rule = root / "li" / "world_cup" / "game1_pick_state_authority_rule.md"
card = root / "cards" / "151_define_game1_pick_state_authority_card.md"
doc = root / "docs" / "features" / "game1_pick_state_authority.md"

missing_files = [str(p) for p in [html, rule, card, doc] if not p.exists()]
if missing_files:
    print("Missing required files:", *missing_files, sep="\n- ")
    sys.exit(1)

text = html.read_text()
problems = []

required_markers = [
    "WC2026_DISABLE_SHORT_TERM_R16_HOLD_FOR_CANONICAL_STATE",
    "WC2026_SOURCE_GATED_KNOCKOUT_MENU_OPEN",
    "WC2026_MENU_NO_PRESELECT_HIGHLIGHT",
    "WC2026_CLEAR_PICKS_CANONICAL_ALL_GAME1_STATE",
]
for marker in required_markers:
    if marker not in text:
        problems.append(f"Missing marker: {marker}")

# The stored knockout render bridge must not render stored R16/advance picks immediately after only checking `if (!pick) return;`.
unsafe_r16 = re.search(
    r"const pick = storedPickForSlot\(rule\.slotId\);\s*if \(!pick\) return;\s*const before = Array\.from\(document\.querySelectorAll\(`\.r16PickCard",
    text,
    re.S,
)
unsafe_adv = re.search(
    r"const pick = storedPickForSlot\(rule\.slotId\);\s*if \(!pick\) return;\s*const before = Array\.from\(document\.querySelectorAll\(`\.advancePickCard",
    text,
    re.S,
)
if unsafe_r16:
    problems.append("Stored R16 render path renders any stored pick without feeder validity check.")
if unsafe_adv:
    problems.append("Stored advancement render path renders any stored pick without feeder validity check.")

if "WC2026_SOURCE_GATE_STORED_KNOCKOUT_RENDER" not in text and ("renderStoredR16Picks" in text or "renderStoredAdvancementPicks" in text):
    problems.append("Missing WC2026_SOURCE_GATE_STORED_KNOCKOUT_RENDER marker for stored knockout render boundary.")

# Heavy/current-choice menu state should not be active in the choice list.
for snippet in [
    'isCurrentChoice ? " isCurrentChoice" : ""',
    'isCurrentChoice ? "true" : "false"',
    'isCurrentChoice ? " ✓" : ""',
]:
    if snippet in text:
        problems.append(f"Menu current-choice visual state still present: {snippet}")

if problems:
    print("WC2026 Game 1 pick state authority verification failed:")
    for p in problems:
        print(f"- {p}")
    sys.exit(1)

print("WC2026 Game 1 pick state authority verification passed.")
