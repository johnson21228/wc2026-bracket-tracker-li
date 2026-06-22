#!/usr/bin/env python3
from pathlib import Path
import sys

errors = []

required_files = [
    "li/world_cup/single_geometry_truth_rule.md",
    "docs/geometry/wc2026_single_geometry_truth.md",
    "li/world_cup/uniform_svg_gameboard_authority_rule.md",
    "docs/geometry/uniform_svg_gameboard_authority.md",
    "captures/CAPTURE_BACK_SINGLE_GEOMETRY_TRUTH_LI.md",
    "cards/256_single_geometry_truth_li_card.md",
]

for path in required_files:
    if not Path(path).exists():
        errors.append(f"missing required file: {path}")

combined = "\n".join(
    Path(path).read_text()
    for path in required_files
    if Path(path).exists()
)

required_phrases = [
    "one geometry truth",
    "site/assets/playfield/uniform_pick_card_gameboard.svg",
    "source-truth",
    "site/data/geometry/uniform_pick_card_gameboard_manifest.json",
    "generated/runtime projection",
    "site/assets/playfield/uniform_pick_card_gameboard.png",
    "rendered visual derivative",
    "JSON is not an independent",
    "CSS",
    "must not define canonical slot bounds",
    "FINAL_FOUR",
    "legacy/current behavior",
    "center-stack",
]

for phrase in required_phrases:
    if phrase not in combined:
        errors.append(f"missing required LI phrase: {phrase}")

authority_doc = Path("li/world_cup/uniform_svg_gameboard_authority_rule.md").read_text()
if "JSON manifest is a generated/runtime projection" not in authority_doc:
    errors.append("uniform SVG authority rule must state JSON manifest is generated/runtime projection")

geometry_doc = Path("docs/geometry/uniform_svg_gameboard_authority.md").read_text()
if "SVG/source geometry is the source-truth board geometry" not in geometry_doc:
    errors.append("uniform SVG geometry doc must state SVG/source geometry is source truth")

final_four_paths = [
    "docs/features/final_four_pick_display.md",
    "li/world_cup/final_four_pick_display_rule.md",
]
for path in final_four_paths:
    if Path(path).exists():
        text = Path(path).read_text()
        if "legacy/current geometry behavior, not permanent geometry truth" not in text:
            errors.append(f"{path} must mark single FINAL_FOUR geometry as legacy/current, not permanent truth")

# Guard against reintroducing stage pick gates while doing this LI-only work.
for path in [
    "site/js/mvc/controller.js",
    "site/js/mvc/view.js",
]:
    if Path(path).exists():
        text = Path(path).read_text()
        for token in [
            'activeGame === "game-1" && slot.round !== "R32"',
            'activeGame === "game-2" && slot.round === "R32"',
            "Round of 32 picking is disabled",
            "Game 2 pick menu is not ready",
        ]:
            if token in text:
                errors.append(f"stage-gated pick/menu token returned in {path}: {token}")

if errors:
    print("Single geometry truth LI verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: WC2026 LI names one source-truth SVG geometry with generated JSON projection and rendered PNG derivative.")
