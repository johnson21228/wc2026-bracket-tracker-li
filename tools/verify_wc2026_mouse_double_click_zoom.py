#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"missing required file: {rel}")
    return path.read_text()

def main() -> int:
    errors = []
    view = read("site/js/mvc/view.js")
    makefile = read("Makefile")
    doc = read("docs/features/mouse_double_click_zoom.md")
    rule = read("li/world_cup/mouse_double_click_zoom_rule.md")
    capture = read("captures/CAPTURE_BACK_MOUSE_DOUBLE_CLICK_ZOOM.md")
    card = read("cards/252_mouse_double_click_zoom_card.md")

    required_view_tokens = [
        ("BOARD_DOUBLE_CLICK_ZOOM_STEP", "missing dedicated double-click zoom step constant"),
        ("function installMouseBoardDoubleClickZoom()", "missing mouse double-click zoom installer"),
        ("dataset.mouseDoubleClickZoomInstalled", "missing idempotent double-click installer guard"),
        ("addEventListener(\"dblclick\"", "missing dblclick listener"),
        ("lastBoardPointerDownType === \"touch\"", "double-click zoom must not intercept touch double-tap"),
        ("lastBoardPointerDownType && lastBoardPointerDownType !== \"mouse\"", "double-click zoom must remain mouse-only"),
        ("isBoardPanInteractiveTarget(event.target)", "double-click zoom must exclude interactive controls"),
        ("event.preventDefault();", "double-click zoom should prevent browser text/image selection only for accepted mouse double-clicks"),
        ("zoomBoardAroundPoint(boardScale + BOARD_DOUBLE_CLICK_ZOOM_STEP, event.clientX, event.clientY)", "double-click zoom must reuse pointer-centered board zoom"),
        ("installMouseBoardDoubleClickZoom();", "double-click zoom installer must be invoked"),
    ]
    for token, message in required_view_tokens:
        if token not in view:
            errors.append(message)

    if "touchstart" in view or "touchmove" in view:
        errors.append("double-click zoom CB must not add custom touchstart/touchmove handlers")

    dblclick_index = view.find('addEventListener("dblclick"')
    if dblclick_index != -1:
        listener_slice = view[dblclick_index:dblclick_index + 900]
        if 'if (isBoardPanInteractiveTarget(event.target)) return;' not in listener_slice:
            errors.append("dblclick listener should return before zooming on interactive controls")
        if 'zoomBoardAroundPoint' not in listener_slice:
            errors.append("dblclick listener should zoom through zoomBoardAroundPoint")

    if "python3 tools/verify_wc2026_mouse_double_click_zoom.py" not in makefile:
        errors.append("Makefile must run mouse double-click zoom verifier")

    for rel, text in [
        ("docs/features/mouse_double_click_zoom.md", doc),
        ("li/world_cup/mouse_double_click_zoom_rule.md", rule),
        ("captures/CAPTURE_BACK_MOUSE_DOUBLE_CLICK_ZOOM.md", capture),
        ("cards/252_mouse_double_click_zoom_card.md", card),
    ]:
        for token in ["double-click", "zoom", "touch", "pick"]:
            if token not in text:
                errors.append(f"{rel} should mention {token}")

    if errors:
        print("WC2026 mouse double-click zoom verification failed: " + "; ".join(errors))
        return 1
    print("OK: WC2026 board has mouse-only double-click zoom around pointer while preserving touch and pick interactions.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
