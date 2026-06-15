#!/usr/bin/env python3
from pathlib import Path
import json
import sys

required = [
    "LLM_READ_FIRST.md",
    "MAP.md",
    "li/world_cup/source_authority_rule.md",
    "li/world_cup/two_game_pool_model_rule.md",
    "li/world_cup/data_storage_rule.md",
    "data/game_1_round_of_32_picks.json",
    "data/game_2_bracket_picks.json",
    "cards/000_capture_initial_group_stage_schedule_from_poster_card.md",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print("Missing required files:")
    for p in missing:
        print("-", p)
    sys.exit(1)

for p in Path("data").glob("*.json"):
    json.loads(p.read_text(encoding="utf-8"))

print("WC2026 Bracket Tracker verification passed.")
