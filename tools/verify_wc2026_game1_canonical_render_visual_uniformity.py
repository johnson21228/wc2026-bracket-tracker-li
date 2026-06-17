#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
html_path = ROOT / "site" / "index.html"
html = html_path.read_text()

required = [
    "WC2026_GAME1_CANONICAL_PICK_STATE_MODEL",
    "WC2026_CARD155_RENDER_FROM_CANONICAL_PICK_STATE",
    "WC2026_CARD155_PATCH_ADORNMENTS_FROM_CANONICAL_PICK_STATE",
    "WC2026_CARD156_CANONICAL_RENDER_VISUAL_UNIFORMITY",
    "r16PickCard",
    "advancePickCard",
    "storedKnockoutPickCard",
]
missing = [s for s in required if s not in html]
if missing:
    print("Missing required canonical render visual uniformity markers/content:")
    for item in missing:
        print(f"- {item}")
    sys.exit(1)

match = re.search(
    r"/\* WC2026_CARD156_CANONICAL_RENDER_VISUAL_UNIFORMITY_START \*/(.*?)/\* WC2026_CARD156_CANONICAL_RENDER_VISUAL_UNIFORMITY_END \*/",
    html,
    re.S,
)
if not match:
    print("Missing Card 156 CSS normalization block.")
    sys.exit(1)

block = match.group(1)
for token in [
    ".r16PickCard",
    ".advancePickCard",
    ".storedKnockoutPickCard",
    "[data-r32-slot-fit=\"true\"]",
    "[data-choice-can-remain-final]",
    ":hover",
    ":focus-visible",
]:
    if token not in block:
        print(f"Card 156 CSS block missing expected selector/token: {token}")
        sys.exit(1)

for forbidden in ["0 12px 28px", "outline: 3px solid rgba(255,255,255,.92) !important;\n}"]:
    if forbidden in block and "hover" not in block:
        print(f"Card 156 CSS block appears to include forbidden persistent heavy style: {forbidden}")
        sys.exit(1)

# Persistent normalization should explicitly remove outline from baseline cards.
if "outline: none !important" not in block:
    print("Card 156 CSS block must remove persistent outlines from baseline rendered knockout cards.")
    sys.exit(1)

for path in [
    ROOT / "cards" / "156_normalize_canonical_rendered_knockout_visual_state_card.md",
    ROOT / "docs" / "features" / "game1_canonical_render_visual_uniformity.md",
    ROOT / "li" / "world_cup" / "game1_canonical_render_visual_uniformity_rule.md",
]:
    if not path.exists():
        print(f"Missing Card 156 supporting artifact: {path}")
        sys.exit(1)

print("WC2026 Game 1 canonical render visual uniformity verification passed.")
