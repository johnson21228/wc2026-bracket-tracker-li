#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
html_path = root / "site/game1/index.html"
html = html_path.read_text()

required_files = [
    "li/world_cup/game1_r32_choice_menu_team_tile_spacing_rule.md",
    "docs/features/game1_r32_choice_menu_team_tile_spacing.md",
    "cards/107_repair_game1_r32_choice_menu_team_tile_spacing_card.md",
    "prompts/repair_game1_r32_choice_menu_team_tile_spacing.md",
    "capture_back/CAPTURE_BACK_GAME1_R32_CHOICE_MENU_TEAM_TILE_SPACING.md",
]
missing = [p for p in required_files if not (root / p).exists()]
if missing:
    raise SystemExit("Missing files: " + ", ".join(missing))

if "teamTile" not in html or "teamMeta" not in html or "teamName" not in html or "teamDetail" not in html:
    raise SystemExit("Expected live teamTile/teamMeta/teamName/teamDetail renderer markers")

if not re.search(r"\.teamMeta\s*\{[^}]*display\s*:\s*inline-flex", html, re.S):
    raise SystemExit(".teamMeta must be inline-flex")
if not re.search(r"\.teamMeta\s*\{[^}]*gap\s*:\s*(?:12px|14px|1[0-9]px|0\.75rem|\.75rem|1rem)", html, re.S):
    raise SystemExit(".teamMeta must define an explicit gap")
if not re.search(r"\.teamDetail\s*\{[^}]*margin-left\s*:\s*(?:10px|12px|14px|1[0-9]px|0\.75rem|\.75rem|1rem)", html, re.S):
    raise SystemExit(".teamDetail must define margin-left fallback")
if not re.search(r"\.teamDetail\s*\{[^}]*display\s*:\s*inline-block", html, re.S):
    raise SystemExit(".teamDetail must be inline-block for margin fallback")

# Ensure the current active renderer still uses structured spans, not flattened text.
if '<span class="teamName">${displayName(team)}</span><span class="teamDetail">' not in html:
    raise SystemExit("Expected structured teamName/teamDetail spans in tile renderer")

print("WC2026 Game 1 R32 choice menu team tile spacing checks passed.")
