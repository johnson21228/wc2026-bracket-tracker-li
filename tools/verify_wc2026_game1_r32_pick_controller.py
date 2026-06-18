#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        print(f"WC2026 Game 1 R32 pick controller verification failed: {message}", file=sys.stderr)
        raise SystemExit(1)


def read(rel):
    path = ROOT / rel
    require(path.exists(), f"missing file: {rel}")
    return path.read_text(encoding="utf-8")


def node_check(rel):
    result = subprocess.run(["node", "--check", str(ROOT / rel)], text=True, capture_output=True)
    require(result.returncode == 0, f"JS syntax failed for {rel}: {result.stderr or result.stdout}")


def main():
    controller = read("site/js/controllers/Game1R32PickController.js")
    layer = read("site/js/board/R32PickMenuLayer.js")
    makefile = read("Makefile")

    for rel in [
        "cards/180_game1_r32_pick_controller_card.md",
        "capture_back/CAPTURE_BACK_GAME1_R32_PICK_CONTROLLER.md",
        "docs/features/game1_r32_pick_controller.md",
        "li/world_cup/game1_r32_pick_controller_rule.md",
    ]:
        require((ROOT / rel).exists(), f"missing Card 180 file: {rel}")

    node_check("site/js/controllers/Game1R32PickController.js")
    node_check("site/js/board/R32PickMenuLayer.js")
    node_check("site/js/board/BoardShell.js")

    require("class Game1R32PickController" in controller, "controller class must exist")
    require("createGame1R32PickController" in controller, "controller factory must exist")
    require("GAME1_R32_PICKABLE_STATES" in controller, "controller must own lifecycle enablement")
    require("GROUP_STAGE_OPEN" in controller and "R32_PROJECTION_LIVE" in controller, "controller must gate projection states")
    require("candidateTeamsForSlot" in controller, "controller must own menu contents")
    require("validatePick" in controller, "controller must validate picks")
    require("setPick" in controller and "clearPick" in controller, "controller must own selection persistence")
    require("duplicateEntry" in controller, "controller must block duplicate teams")
    require("wc2026.game1.r32ProjectionPicks.v1" in controller, "controller must persist to Game 1 R32 storage key")

    require("../controllers/Game1R32PickController.js" in layer, "R32PickMenuLayer must import controller")
    require("controller.getSlotViewModels" in layer, "view must render controller slot models")
    require("controller.setPick" in layer, "view must send selections through controller")
    require("controller.clearPick" in layer, "view must clear through controller")
    require("candidateTeamsForSlot" not in layer, "view must not own candidate logic")
    require("GAME1_R32_PICKABLE_STATES" not in layer, "view must not own lifecycle gate")

    require("tools/verify_wc2026_game1_r32_pick_controller.py" in makefile, "Makefile verify must run Card 180 verifier")

    print("WC2026 Game 1 R32 pick controller verification passed.")


if __name__ == "__main__":
    main()
