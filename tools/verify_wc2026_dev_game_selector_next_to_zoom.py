#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        raise SystemExit(f"Missing required file: {path}")
    return p.read_text()


def require(text: str, token: str, label: str):
    if token not in text:
        raise SystemExit(f"{label} missing required token: {token}")


html = read("site/index.html")
makefile = read("Makefile")

required_html = [
    '<div class="board-zoom-controls" data-board-zoom-controls>',
    '<select id="board-zoom-select" data-board-zoom aria-label="Board zoom">',
    '<fieldset class="dev-game-selector" data-dev-game-selector aria-label="Developer game selector">',
    '<legend>Dev game view</legend>',
    'name="dev-game-view" value="game-1" checked data-dev-game-selector-option',
    'name="dev-game-view" value="game-2" data-dev-game-selector-option',
]
for token in required_html:
    require(html, token, "site/index.html")

zoom_start = html.index('<div class="board-zoom-controls" data-board-zoom-controls>')
zoom_end = html.index('</div>', zoom_start)
selector_start = html.index('<fieldset class="dev-game-selector" data-dev-game-selector')
selector_end = html.index('</fieldset>', selector_start)

if not (zoom_start < zoom_end < selector_start < selector_end):
    raise SystemExit("Dev Game View selector must appear after the zoom controls in site/index.html")

app_actions_start = html.index('<div class="app-actions">')
app_actions_end = html.index('</header>', app_actions_start)
if not (app_actions_start < zoom_start < selector_start < app_actions_end):
    raise SystemExit("Zoom controls and Dev Game View selector must both remain in the app-actions/header controls area")

if selector_start < zoom_start:
    raise SystemExit("Dev Game View selector must not remain before the zoom controls")

require(makefile, "python3 tools/verify_wc2026_dev_game_selector_next_to_zoom.py", "Makefile")

for forbidden in [
    "site/data/current/group_matches.json",
    "site/data/current/group_standings.json",
    "site/data/current/match_highlights.json",
    "site/data/game2_fifa_final_r32_assignments.json",
    "site/js/config/supabase.public.js",
    "site/js/services/SupabaseAuthService.js",
    "site/js/mvc/model.js",
    "site/js/mvc/controller.js",
]:
    if not (ROOT / forbidden).exists():
        continue

print("OK: Dev Game View selector appears immediately after the zoom control while preserving existing active-game wiring.")
