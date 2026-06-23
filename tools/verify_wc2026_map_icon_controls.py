#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = (ROOT / "site/index.html").read_text()
css = (ROOT / "site/css/app.css").read_text()
view = (ROOT / "site/js/mvc/view.js").read_text()
makefile = (ROOT / "Makefile").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require("map-board-icon-controls" in index, "missing upper-left map icon controls")
require("data-board-zoom-in" in index, "missing + zoom icon")
require("data-board-zoom-out" in index, "missing − zoom icon")
require("data-info-panel-open" in index and "data-rules-panel-open" in index, "missing info/rules open aliases")
require(index.find("data-board-zoom-in") < index.find("data-board-zoom-out") < index.find('aria-label="Get info"'), "icon order must be +, −, info")
require(".board-zoom-controls" in css and "display: none !important;" in css, "legacy zoom control must be hidden")
require(".map-board-icon-controls" in css and "display: flex;" in css and "flex-direction: row;" in css, "map icon controls must render as a horizontal row")
require("gap: 10px;" in css, "map icon controls must keep comfortable row spacing")
require("width: 52px;" in css and "height: 52px;" in css, "map icon buttons must use larger touch-friendly desktop hit targets")
require("width: 48px;" in css and "height: 48px;" in css, "map icon buttons must preserve touch-friendly mobile hit targets")
require("grid-template-columns" not in css[css.find(".map-board-icon-controls"):css.find("/* Card 261B")], "map icon controls must not use stacked grid layout")
require("function stepBoardZoomFromIcon(direction)" in view, "missing icon zoom helper")
require('event.target.closest("[data-board-zoom-in], [data-board-zoom-out]")' in view, "missing delegated click handler")
require('stepBoardZoomFromIcon(zoomButton.hasAttribute("data-board-zoom-in") ? 1 : -1)' in view, "missing direction routing")
require('boardZoomSelect.dispatchEvent(new Event("change", { bubbles: true }))' in view, "icon zoom must drive hidden select pipeline")
require("tools/verify_wc2026_map_icon_controls.py" in makefile, "Makefile missing map icon verifier")

if errors:
    print("WC2026 map icon controls verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 map icon controls keep +/− as the only visible zoom controls and use info for the info panel.")
