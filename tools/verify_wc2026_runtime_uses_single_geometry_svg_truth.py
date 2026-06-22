#!/usr/bin/env python3
from pathlib import Path
import json
import re

ASSET_PATHS = Path("site/js/services/assetPaths.js")
BOARD_SHELL = Path("site/js/board/BoardShell.js")
SVG_LAYER = Path("site/js/board/SvgGameboardLayer.js")
MANIFESTS = [
    Path("site/data/geometry/gameboard_manifest.json"),
    Path("site/data/geometry/uniform_pick_card_gameboard_manifest.json"),
]
SOURCE_SVG = Path("site/assets/playfield/uniform_pick_card_gameboard.svg")
EXPECTED_RUNTIME = 'svgGameboardDefinition: "assets/playfield/uniform_pick_card_gameboard.svg"'
STALE_RUNTIME = 'svgGameboardDefinition: "assets/board/gameboard.svg"'
EXPECTED_SLOTS = {"FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"}

def main():
    errors = []

    asset_text = ASSET_PATHS.read_text()
    if EXPECTED_RUNTIME not in asset_text:
        errors.append("assetPaths.js must point runtime svgGameboardDefinition at assets/playfield/uniform_pick_card_gameboard.svg")
    if STALE_RUNTIME in asset_text:
        errors.append("assetPaths.js must not point runtime svgGameboardDefinition at stale assets/board/gameboard.svg")

    board_shell = BOARD_SHELL.read_text()
    if "await createSvgGameboardLayer" not in board_shell or "svgGameboardDefinition: truthResources.svgGameboardDefinition" not in board_shell:
        errors.append("BoardShell must pass truthResources.svgGameboardDefinition into SvgGameboardLayer")

    svg_layer = SVG_LAYER.read_text()
    if "fetch(svgGameboardDefinition)" not in svg_layer:
        errors.append("SvgGameboardLayer must fetch the provided svgGameboardDefinition runtime truth")

    if not SOURCE_SVG.exists():
        errors.append(f"missing source-truth SVG: {SOURCE_SVG}")
    else:
        svg = SOURCE_SVG.read_text()
        for slot_id in EXPECTED_SLOTS:
            if f'data-slot-id="{slot_id}"' not in svg:
                errors.append(f"source-truth SVG missing data-slot-id={slot_id}")
        if "final-stack-connector" not in svg:
            errors.append("source-truth SVG must include final-stack connector linework")

    for path in MANIFESTS:
        data = json.loads(path.read_text())
        if data.get("svgAsset") != "assets/playfield/uniform_pick_card_gameboard.svg":
            errors.append(f"{path} svgAsset must be assets/playfield/uniform_pick_card_gameboard.svg")
        if data.get("geometrySource") != "site/assets/playfield/uniform_pick_card_gameboard.svg":
            errors.append(f"{path} geometrySource must be site/assets/playfield/uniform_pick_card_gameboard.svg")

    if errors:
        print("Runtime single geometry SVG truth verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: runtime gameboard linework fetches the single source-truth playfield SVG, not stale board/gameboard.svg.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
