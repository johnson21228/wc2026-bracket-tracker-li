#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        print(f"WC2026 R32 pick button tracking verification failed: {message}", file=sys.stderr)
        raise SystemExit(1)


def read(rel):
    path = ROOT / rel
    require(path.exists(), f"missing file: {rel}")
    return path.read_text(encoding="utf-8")


def node_check(rel):
    result = subprocess.run(["node", "--check", str(ROOT / rel)], text=True, capture_output=True)
    require(result.returncode == 0, f"JS syntax failed for {rel}: {result.stderr or result.stdout}")


def main():
    layer = read("site/js/board/R32PickMenuLayer.js")
    css = read("site/css/board.css")
    makefile = read("Makefile")

    for rel in [
        "cards/181_track_r32_pick_buttons_card.md",
        "capture_back/CAPTURE_BACK_TRACK_R32_PICK_BUTTONS.md",
        "docs/features/track_r32_pick_buttons.md",
        "li/world_cup/track_r32_pick_buttons_rule.md",
    ]:
        require((ROOT / rel).exists(), f"missing Card 181 file: {rel}")

    node_check("site/js/board/R32PickMenuLayer.js")
    node_check("site/js/controllers/Game1R32PickController.js")
    node_check("site/js/board/BoardShell.js")

    require("trackButton" in layer, "layer must track button hover/focus/click")
    require("wc2026:r32PickButtonTracked" in layer, "layer must dispatch tracking event")
    require("r32TrackedFifaLabel" in layer, "layer must expose tracked FIFA label")
    require("preselectState" in layer, "button must expose preselect state")
    require("is-preselectable" in layer, "pickable buttons must get preselectable class")
    require("is-preselect-highlight" in layer, "hover/focus must render preselect highlight")
    require("is-active-selection" in layer, "click must mark active selection")
    require("r32-pick-button-tracker-chip" in layer, "layer must render button tracking chip")
    require("controller.setPick" in layer, "selection must still go through controller")

    require(".r32-pick-slot-button.is-preselectable" in css, "CSS must render preselectable buttons")
    require(".r32-pick-slot-button.is-preselect-highlight" in css, "CSS must render hover/focus preselect highlight")
    require(".r32-pick-button-tracker-chip" in css, "CSS must render tracking chip")
    require("tools/verify_wc2026_track_r32_pick_buttons.py" in makefile, "Makefile verify must run Card 181 verifier")

    print("WC2026 R32 pick button tracking verification passed.")


if __name__ == "__main__":
    main()
