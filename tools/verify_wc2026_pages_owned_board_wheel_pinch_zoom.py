#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def read(rel):
    return (ROOT / rel).read_text()


def fail(message, details):
    print(message, file=sys.stderr)
    for detail in details:
        print(f"- {detail}", file=sys.stderr)
    return 1


def main():
    required_files = [
        "captures/CAPTURE_BACK_PAGES_OWNED_BOARD_WHEEL_PINCH_ZOOM.md",
        "cards/225_implement_pages_owned_board_wheel_pinch_zoom_card.md",
        "docs/features/pages_owned_board_wheel_pinch_zoom.md",
        "li/world_cup/pages_owned_board_wheel_pinch_zoom_rule.md",
    ]
    missing = [rel for rel in required_files if not (ROOT / rel).exists()]
    if missing:
        return fail("Wheel/pinch zoom capture files missing:", missing)

    view = read("site/js/mvc/view.js")
    view_tokens = [
        "const BOARD_MIN_SCALE = 0.5;",
        "const BOARD_MAX_SCALE = 1.25;",
        "const BOARD_WHEEL_ZOOM_STEP",
        "return Math.max(BOARD_MIN_SCALE, Math.min(BOARD_MAX_SCALE, numeric));",
        "function syncBoardZoomSelect()",
        "data-board-zoom-custom",
        "function zoomBoardAroundPoint(nextScale, clientX, clientY)",
        "const wantsBoardZoom = event.ctrlKey || event.metaKey;",
        "event.preventDefault();",
        "zoomBoardAroundPoint(boardScale + (direction * BOARD_WHEEL_ZOOM_STEP), event.clientX, event.clientY);",
        'boardScroll?.addEventListener("wheel"',
        "{ passive: false }",
    ]
    missing_view = [token for token in view_tokens if token not in view]
    if missing_view:
        return fail("Wheel/pinch board zoom runtime tokens missing:", [f"site/js/mvc/view.js: {token}" for token in missing_view])

    makefile = read("Makefile")
    if "python3 tools/verify_wc2026_pages_owned_board_wheel_pinch_zoom.py" not in makefile:
        return fail("Makefile does not run wheel/pinch board zoom verifier:", ["Makefile"])

    print("OK: WC2026 Pages-owned board wheel/pinch zoom is implemented, clamped, and verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
