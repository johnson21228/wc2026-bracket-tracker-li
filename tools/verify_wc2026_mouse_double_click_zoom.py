#!/usr/bin/env python3
from pathlib import Path

view = Path("site/js/mvc/view.js").read_text()
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require("function installMouseBoardDoubleClickZoom()" in view, "mouse double-click zoom installer must exist")
require("boardScroll.dataset.mouseDoubleClickZoomInstalled" in view, "double-click zoom must be installed once")
require("lastBoardPointerDownType" in view, "double-click zoom must track pointer type")
require('lastBoardPointerDownType === "touch"' in view, "double-click zoom must ignore touch-origin double clicks")
require('lastBoardPointerDownType !== "mouse"' in view, "double-click zoom must stay mouse-only")
require('boardScroll.addEventListener("dblclick"' in view, "double-click zoom must use dblclick event")
require("BOARD_DOUBLE_CLICK_ZOOM_STEP" in view, "double-click zoom step must remain explicit")
require("zoomBoardAroundPoint(boardScale + BOARD_DOUBLE_CLICK_ZOOM_STEP" in view, "double-click zoom must reuse board zoom around pointer")
require("installMouseBoardDoubleClickZoom();" in view, "mouse double-click zoom must be installed from handler setup")

require("function installTouchBoardMapMode()" in view, "touch map mode may coexist as its own scoped installer")
require("installTouchBoardMapMode();" in view, "touch map mode must be installed separately from mouse double-click zoom")

touch_start = view.index("function installTouchBoardMapMode()")
double_start = view.index("function installMouseBoardDoubleClickZoom()")
touch_block = view[touch_start:double_start]
double_block = view[double_start:]

require("touchstart" in touch_block and "touchmove" in touch_block, "touch handlers must be isolated to touch map mode")
require("touchstart" not in double_block, "double-click zoom block must not own touchstart")
require("touchmove" not in double_block, "double-click zoom block must not own touchmove")
require("pinchCenter(event)" in touch_block, "pinch logic must be isolated to touch map mode")
require("pinchCenter(event)" not in double_block, "double-click zoom block must not own pinch logic")

if errors:
    print("WC2026 mouse double-click zoom verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 mouse double-click zoom remains mouse-only while touch map mode owns touch separately.")
