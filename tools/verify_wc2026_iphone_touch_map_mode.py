#!/usr/bin/env python3
from pathlib import Path

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

view = Path("site/js/mvc/view.js").read_text()
css = Path("site/css/board.css").read_text()
rule = Path("li/world_cup/iphone_touch_map_mode_rule.md").read_text()
doc = Path("docs/features/iphone_touch_map_mode.md").read_text()
capture = Path("captures/CAPTURE_BACK_IPHONE_TOUCH_MAP_MODE.md").read_text()
card = Path("cards/290_iphone_touch_map_mode_card.md").read_text()

require("function installTouchBoardMapMode()" in view, "view must install a scoped touch map-mode handler")
require("boardScroll.dataset.touchMapModeInstalled" in view, "touch map mode must be installed once per board viewport")
require('touchMode = "pan' in view, "touch map mode must support one-finger pan")
require('touchMode = "pinch"' in view, "touch map mode must support two-finger pinch")
require("pinchCenter(event)" in view, "pinch zoom must use a midpoint")
require("zoomBoardAroundPoint(pinchStartScale * ratio" in view, "pinch zoom must reuse board-plane zoom around a point")
require('addEventListener("touchstart"' in view, "touchstart handler must exist")
require('addEventListener("touchmove"' in view, "touchmove handler must exist")
require('addEventListener("touchend"' in view, "touchend handler must exist")
require("{ passive: false }" in view, "touch handlers must be non-passive so board-scoped preventDefault can work")
require("event.preventDefault()" in view, "touch map mode must suppress browser page gestures within board viewport")
require("isBoardPanInteractiveTarget(event.target)" in view, "touch map mode must exclude interactive targets")
require("installMouseBoardDragPan();" in view, "desktop mouse drag pan must remain installed")
require("installMouseBoardDoubleClickZoom();" in view, "desktop double-click zoom must remain installed")
require("boardScroll?.addEventListener(\"wheel\"" in view, "desktop wheel zoom must remain wired")
require("installTouchBoardMapMode();" in view, "touch map mode must be called during handler install")

require(".game1-board-viewport" in css and "touch-action: none" in css, "board viewport must own touch gestures")
require("overscroll-behavior: contain" in css, "board viewport must contain browser overscroll")
require("env(safe-area-inset-right)" in css, "zoom controls must respect right safe-area")
require("env(safe-area-inset-bottom)" in css, "zoom controls must respect bottom safe-area")
require("touch-action: manipulation" in css, "interactive controls must remain tappable")

for label, text in {
    "rule": rule,
    "doc": doc,
    "capture": capture,
    "card": card,
}.items():
    require("iPhone" in text or "touch" in text, f"{label} must document iPhone/touch map mode")

for forbidden in [
    "SupabaseBracketStore.js",
    "saveOfficialR32BracketAuthority",
    "bracket_kind",
]:
    require(forbidden not in rule + doc + capture + card, f"touch CB docs must not alter persistence scope: {forbidden}")

if errors:
    print("WC2026 iPhone touch map mode verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: iPhone Safari touch map mode is scoped, safe-area-aware, and preserves desktop board behavior.")
