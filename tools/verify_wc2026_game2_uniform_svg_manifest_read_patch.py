#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
GAME2 = ROOT / "site" / "game2" / "index.html"
MANIFEST_JS = ROOT / "site" / "data" / "geometry" / "uniform_pick_card_gameboard_manifest.js"
LI = ROOT / "li" / "world_cup" / "game2_reads_uniform_svg_gameboard_manifest_rule.md"
DOC = ROOT / "docs" / "geometry" / "game2_reads_uniform_svg_gameboard_manifest.md"
CARD = ROOT / "cards" / "109_game2_read_uniform_svg_gameboard_manifest_card.md"
PROMPT = ROOT / "prompts" / "read_uniform_svg_gameboard_manifest_in_game2.md"
CAPTURE = ROOT / "capture_back" / "CAPTURE_BACK_GAME2_READ_UNIFORM_SVG_GAMEBOARD_MANIFEST.md"

errors = []
for path in [GAME2, MANIFEST_JS, LI, DOC, CARD, PROMPT, CAPTURE]:
    if not path.exists():
        errors.append(f"missing expected file: {path.relative_to(ROOT)}")

if GAME2.exists():
    text = GAME2.read_text(encoding="utf-8")
    required = [
        '../data/geometry/uniform_pick_card_gameboard_manifest.js',
        'WC2026_GAME2_UNIFORM_SVG_MANIFEST_PROBE',
        'validateUniformSvgGameboardManifestForGame2',
        'uniformSvgManifestMode = "game2-read-only-manifest-probe"',
        'uniformSvgGame2GeometryMigration = "not-started"',
        'R32: 32',
        'R16: 16',
        'QF: 8',
        'SF: 4',
        'FINAL_FOUR: 1',
    ]
    for needle in required:
        if needle not in text:
            errors.append(f"Game 2 missing expected manifest probe text: {needle}")
    if 'uniform_pick_card_gameboard.svg' in text or 'uniform_pick_card_gameboard.png' in text:
        errors.append("Game 2 should not switch visible board asset in this read-only CB")
    if 'r32_bracket_geometry_overlay.png' not in text:
        errors.append("Game 2 visible board source should remain the existing geometry overlay in this read-only CB")

if errors:
    for e in errors:
        print(e)
    sys.exit(1)
print("WC2026 Game 2 uniform SVG manifest read checks passed.")
