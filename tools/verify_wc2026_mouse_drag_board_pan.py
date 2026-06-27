#!/usr/bin/env python3
from pathlib import Path

view = Path("site/js/mvc/view.js").read_text()
css = Path("site/css/board.css").read_text()
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require("function installMouseBoardDragPan()" in view, "mouse drag pan installer must exist")
require("boardScroll.dataset.mouseDragPanInstalled" in view, "mouse drag pan must be installed once")
require('event.pointerType === "touch"' in view, "mouse drag pan must ignore touch pointer events")
require("event.pointerType && event.pointerType !== \"mouse\"" in view, "mouse drag pan must remain mouse-only")
require("isBoardPanInteractiveTarget(event.target)" in view, "mouse drag pan must exclude interactive targets")
require("BOARD_DRAG_PAN_THRESHOLD_PX" in view, "mouse drag pan threshold must remain explicit")
require("boardScroll.classList.add(\"is-drag-panning\")" in view, "mouse drag pan must expose drag-panning class")
require("boardScroll.scrollLeft" in view and "boardScroll.scrollTop" in view, "mouse drag pan must pan the board viewport")
require("installMouseBoardDragPan();" in view, "mouse drag pan must be installed from handler setup")

require("function installTouchBoardMapMode()" in view, "touch map mode may coexist as its own scoped installer")
require("installTouchBoardMapMode();" in view, "touch map mode must be installed separately from mouse drag pan")

mouse_start = view.index("function installMouseBoardDragPan()")
mouse_end = view.index("function installTouchBoardMapMode()", mouse_start)
mouse_block = view[mouse_start:mouse_end]
require("touchstart" not in mouse_block, "mouse drag pan block must not own touchstart")
require("touchmove" not in mouse_block, "mouse drag pan block must not own touchmove")
require("pinch" not in mouse_block.lower(), "mouse drag pan block must not own pinch logic")

touch_start = view.index("function installTouchBoardMapMode()")
touch_end = view.index("function installMouseBoardDoubleClickZoom()", touch_start)
touch_block = view[touch_start:touch_end]
require("touchstart" in touch_block and "touchmove" in touch_block, "touch gestures must be isolated to touch map mode")
require("pinchCenter(event)" in touch_block, "pinch logic must be isolated to touch map mode")

require(".game1-board-viewport.is-drag-panning" in css or ".is-drag-panning" in css, "drag-panning class should have CSS affordance")
require("touch-action: none" in css, "touch gesture ownership should be CSS-scoped to the board viewport")

if errors:
    print("WC2026 mouse drag board pan verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 mouse drag board pan remains mouse-only while touch map mode owns touch separately.")
