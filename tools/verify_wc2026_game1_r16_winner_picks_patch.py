#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = ROOT / "site" / "game1" / "index.html"
text = index.read_text()
required = [
    "WC2026_GAME1_R16_WINNER_PICKS",
    "wc2026.game1.r16.winnerPicks",
    "function r16SlotRulesFromManifest",
    "function createR16Hotspots",
    "function openR16Menu",
    "function assignR16Winner",
    "function renderR16Picks",
    "uniform_pick_card_gameboard_manifest.js",
]
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("Missing Game 1 R16 winner-pick markers: " + ", ".join(missing))

li = ROOT / "li" / "world_cup" / "game1_r16_winner_pick_rule.md"
doc = ROOT / "docs" / "features" / "game1_r16_winner_picks.md"
card = ROOT / "cards" / "111_add_game1_r16_winner_picks_card.md"
for path in (li, doc, card):
    if not path.exists():
        raise SystemExit(f"Missing expected artifact: {path}")

print("WC2026 Game 1 R16 winner-pick checks passed.")
