#!/usr/bin/env python3
from pathlib import Path
import re

index = Path("site/index.html").read_text()
app_css = Path("site/css/app.css").read_text()
board_css = Path("site/css/board.css").read_text()
makefile = Path("Makefile").read_text()

errors = []

def require(text, token, label):
    if token not in text:
        errors.append(f"missing {label}: {token}")

require(app_css, "Card 266: browser floating controls stay fixed-size while the board zooms", "CSS rule")
require(app_css, ".map-board-icon-controls,", "map controls fixed-size selector")
require(app_css, ".supabase-identity-surface,", "identity fixed-size selector")
require(app_css, "transform: none !important;", "fixed controls transform reset")
require(app_css, "zoom: 1 !important;", "fixed controls zoom reset")
require(app_css, "position: fixed !important;", "fixed viewport positioning")
require(app_css, "contain: layout style;", "fixed control containment")
require(app_css, "inline-size: 52px;", "desktop fixed button inline size")
require(app_css, "block-size: 52px;", "desktop fixed button block size")

require(board_css, ".pixel-native-board-plane", "board plane selector")
require(board_css, "transform: scale(var(--board-render-scale));", "board-plane zoom transform")
require(board_css, ".board-scale-frame", "board scale frame selector")
require(board_css, "--board-render-w-px", "board scale frame render width variable")
require(board_css, "--board-render-h-px", "board scale frame render height variable")

board_scale_block = re.search(r"\.board-scale-frame\s*\{(?P<body>.*?)\}", board_css, re.S)
if not board_scale_block:
    errors.append("could not find .board-scale-frame CSS block")
elif "transform:" in board_scale_block.group("body"):
    errors.append(".board-scale-frame must not own a transform; it should only size the rendered board")

plane_block = re.search(r"\.pixel-native-board-plane\s*\{(?P<body>.*?)\}", board_css, re.S)
if not plane_block:
    errors.append("could not find .pixel-native-board-plane CSS block")
elif "transform: scale(var(--board-render-scale));" not in plane_block.group("body"):
    errors.append(".pixel-native-board-plane must remain the scoped board zoom transform owner")

board_scroll_start = index.find('data-board-scroll')
board_plane_start = index.find('data-board-plane')
map_controls_start = index.find('data-map-board-icon-controls')
identity_start = index.find('data-supabase-identity-surface')

if min(board_scroll_start, board_plane_start, map_controls_start, identity_start) < 0:
    errors.append("missing expected board/control markup data attributes")
else:
    if map_controls_start > board_scroll_start:
        errors.append("map board icon controls must appear outside/before the board scroll surface")
    if identity_start > board_scroll_start:
        errors.append("identity surface must appear outside/before the board scroll surface")
    if map_controls_start > board_plane_start:
        errors.append("map board icon controls must not be inside board plane")
    if identity_start > board_plane_start:
        errors.append("identity surface must not be inside board plane")

for path in [
    "li/world_cup/floating_controls_fixed_size_during_zoom_rule.md",
    "cards/266_keep_floating_controls_fixed_size_during_zoom_card.md",
    "captures/CAPTURE_BACK_FLOATING_CONTROLS_FIXED_SIZE_DURING_ZOOM.md",
]:
    if not Path(path).exists():
        errors.append(f"missing captured artifact: {path}")

if "tools/verify_wc2026_floating_controls_fixed_size_during_zoom.py" not in makefile:
    errors.append("Makefile missing floating controls fixed-size verifier")

if errors:
    print("Floating controls fixed-size during zoom verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 browser floating controls remain fixed-size viewport chrome while board zoom stays scoped to the board plane.")
