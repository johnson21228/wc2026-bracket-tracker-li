#!/usr/bin/env python3
from pathlib import Path
import re

app_css = Path("site/css/app.css").read_text()
board_css = Path("site/css/board.css").read_text()
makefile = Path("Makefile").read_text()

errors = []

required_app_tokens = [
    "Card 277: sign-in panel is topmost browser chrome over the game board",
    "--wc-z-identity-panel: 20000",
    "--wc-z-identity-surface: 19900",
    ".supabase-identity-surface",
    "z-index: var(--wc-z-identity-surface) !important",
    ".identity-panel-backdrop",
    "z-index: var(--wc-z-identity-panel) !important",
    "position: fixed !important",
    "inset: 0 !important",
    ".identity-panel",
    "z-index: calc(var(--wc-z-identity-panel) + 1)",
]

for token in required_app_tokens:
    if token not in app_css:
        errors.append(f"missing app.css token: {token}")

for path in [
    Path("cards/277_sign_in_panel_over_game_board_card.md"),
    Path("li/world_cup/sign_in_panel_over_game_board_rule.md"),
    Path("captures/CAPTURE_BACK_SIGN_IN_PANEL_OVER_GAME_BOARD.md"),
]:
    if not path.exists():
        errors.append(f"missing artifact: {path}")

def css_var_number(css, name):
    match = re.search(rf"{re.escape(name)}\s*:\s*(\d+)", css)
    return int(match.group(1)) if match else None

identity_panel_z = css_var_number(app_css, "--wc-z-identity-panel")
pick_menu_z = css_var_number(board_css, "--wc-z-pick-menu")
group_panel_z = css_var_number(board_css, "--wc-z-group-panel")

if identity_panel_z is None:
    errors.append("missing numeric --wc-z-identity-panel")
if pick_menu_z is None:
    errors.append("missing numeric --wc-z-pick-menu")
if group_panel_z is None:
    errors.append("missing numeric --wc-z-group-panel")

if identity_panel_z is not None and pick_menu_z is not None and identity_panel_z <= pick_menu_z:
    errors.append(f"identity panel z-index {identity_panel_z} must outrank pick menu z-index {pick_menu_z}")
if identity_panel_z is not None and group_panel_z is not None and identity_panel_z <= group_panel_z:
    errors.append(f"identity panel z-index {identity_panel_z} must outrank group panel z-index {group_panel_z}")

if "tools/verify_wc2026_sign_in_panel_over_game_board.py" not in makefile:
    errors.append("Makefile missing sign-in panel verifier")

if errors:
    print("Sign-in panel over game board verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 sign-in panel is fixed topmost browser chrome over the game board and board floating surfaces.")
