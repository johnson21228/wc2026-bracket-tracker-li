#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def require(condition, message):
    if not condition:
        print(f"WC2026 R32 pick menu from FIFA bridge verification failed: {message}", file=sys.stderr)
        raise SystemExit(1)

def read(rel):
    path = ROOT / rel
    require(path.exists(), f"missing file: {rel}")
    return path.read_text(encoding="utf-8")

def main():
    layer = read("site/js/board/R32PickMenuLayer.js")
    controller = read("site/js/controllers/Game1R32PickController.js")
    board_shell = read("site/js/board/BoardShell.js")
    board_css = read("site/css/board.css")
    makefile = read("Makefile")

    for rel in [
        "site/data/model/fifa_r32_logical_slot_order.json",
        "site/data/geometry/game1_fifa_slot_geometry_map.json",
        "site/data/geometry/gameboard_manifest.json",
        "docs/features/game1_r32_pick_menus_from_fifa_bridge.md",
        "li/world_cup/game1_r32_pick_menu_from_fifa_bridge_rule.md",
        "cards/179_r32_pick_menus_from_fifa_bridge_card.md",
        "capture_back/CAPTURE_BACK_R32_PICK_MENUS_FROM_FIFA_BRIDGE.md",
    ]:
        require((ROOT / rel).exists(), f"missing Card 179 required file: {rel}")

    require("createR32PickMenuLayer" in layer, "R32PickMenuLayer must export createR32PickMenuLayer")
    require("fifa_r32_logical_slot_order.json" in layer, "R32PickMenuLayer must read FIFA logic map")
    require("game1_fifa_slot_geometry_map.json" in layer, "R32PickMenuLayer must read FIFA bridge map")
    require("GROUP_STAGE_OPEN" in layer + controller and "R32_PROJECTION_LIVE" in layer + controller, "R32 menus must be gated by pre-lock lifecycle states")
    require("third-place-candidate-set" in layer + controller or "third-place qualifier" in layer + controller, "R32 menus must handle third-place candidate sets")
    require("wc2026.game1.r32ProjectionPicks.v1" in layer + controller, "R32 menu picks must have local storage key")
    require("createR32PickMenuLayer" in board_shell, "BoardShell must append R32 pick menu layer")
    require("board-r32-pick-menu-layer" in board_css, "board.css must style R32 pick menu layer")
    require("tools/verify_wc2026_r32_pick_menus_from_fifa_bridge.py" in makefile, "Makefile verify must run Card 179 verifier")

    print("WC2026 R32 pick menu from FIFA bridge verification passed.")

if __name__ == "__main__":
    main()
