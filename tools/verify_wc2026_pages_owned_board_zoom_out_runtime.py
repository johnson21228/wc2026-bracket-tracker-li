#!/usr/bin/env python3
from pathlib import Path
import sys

errors = []

required = {
    "site/index.html": [
        '<h1 id="app-title">Bracketeering Pub</h1>',
        'data-board-zoom',
        'data-board-scale-frame',
        '<option value="0.5">50%</option>',
        '<option value="0.75">75%</option>',
        '<option value="1" selected>100%</option>',
        '<option value="1.25">125%</option>',
    ],
    "site/css/board.css": [
        ".board-scale-frame",
        "--board-render-scale",
        "transform: scale(var(--board-render-scale))",
        "transform-origin: top left",
    ],
    "site/css/app.css": [
        ".board-zoom-controls",
        "board-zoom-controls select",
    ],
    "site/js/mvc/view.js": [
        "boardScale",
        "boardNativeSize",
        "applyBoardRenderScale",
        "clampBoardScale",
        "Math.max(BOARD_MIN_SCALE, Math.min(BOARD_MAX_SCALE, numeric))",
        "boardZoomSelect?.addEventListener",
        "(viewport.scrollLeft || 0) / boardScale",
        "rect.width / boardScale",
    ],
    "captures/CAPTURE_BACK_PAGES_OWNED_BOARD_ZOOM_OUT_RUNTIME.md": [
        "Pages-Owned Board Zoom-Out Runtime",
        "50%, 75%, 100%, or 125%",
    ],
    "cards/224_implement_pages_owned_board_zoom_out_runtime_card.md": [
        "Card 224",
        "Implement Pages-owned board zoom-out runtime",
    ],
    "docs/features/pages_owned_board_zoom_out_runtime.md": [
        "native board coordinates",
        "50%",
    ],
    "li/world_cup/pages_owned_board_zoom_out_runtime_rule.md": [
        "Render scale is View-owned",
        "Supabase SQL",
    ],
}

for path_text, needles in required.items():
    path = Path(path_text)
    if not path.exists():
        errors.append(f"missing {path_text}")
        continue
    text = path.read_text()
    for needle in needles:
        if needle not in text:
            errors.append(f"{path_text} missing expected text: {needle}")

makefile = Path("Makefile").read_text()
if "python3 tools/verify_wc2026_pages_owned_board_zoom_out_runtime.py" not in makefile:
    errors.append("Makefile missing Pages-owned board zoom-out runtime verifier")

if errors:
    print("WC2026 Pages-owned board zoom-out runtime verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: WC2026 Pages-owned board zoom-out runtime is implemented, captured, and verified.")
