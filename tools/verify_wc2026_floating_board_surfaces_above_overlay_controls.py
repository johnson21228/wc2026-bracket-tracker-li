#!/usr/bin/env python3
from pathlib import Path
import re

css = Path("site/css/board.css").read_text()
errors = []

required_tokens = [
    "Card 265: floating board surfaces over app overlay controls",
    "--wc-z-app-overlay-control: 46",
    "--wc-z-floating-board-surface-host: 13000",
    "--wc-z-pick-menu: 13100",
    "--wc-z-group-panel: 13200",
    ".board-scroll:has(.r32-pick-menu-popover)",
    ".board-scroll:has(.pick-menu-popover)",
    ".board-scroll:has(.group-panel-popover)",
    "z-index: var(--wc-z-floating-board-surface-host)",
    "z-index: var(--wc-z-group-panel) !important",
]

for token in required_tokens:
    if token not in css:
        errors.append(f"missing CSS token: {token}")

def last_css_int_var(name):
    pattern = re.compile(re.escape(name) + r"\s*:\s*(\d+)")
    matches = pattern.findall(css)
    return int(matches[-1]) if matches else None

app_overlay_value = last_css_int_var("--wc-z-app-overlay-control")
host_value = last_css_int_var("--wc-z-floating-board-surface-host")
pick_value = last_css_int_var("--wc-z-pick-menu")
group_value = last_css_int_var("--wc-z-group-panel")

if None in [app_overlay_value, host_value, pick_value, group_value]:
    errors.append(
        "missing z-index variable definitions: "
        f"app={app_overlay_value}, host={host_value}, "
        f"pick={pick_value}, group={group_value}"
    )
else:
    if not (host_value > app_overlay_value):
        errors.append("floating board surface host must be above app overlay controls")
    if not (pick_value > host_value):
        errors.append("pick menu layer must be above floating board surface host")
    if not (group_value > pick_value):
        errors.append("group panel layer must be above pick menu layer")

for path in [
    Path("li/world_cup/floating_board_surfaces_above_overlay_controls_rule.md"),
    Path("docs/features/floating_board_surfaces_above_overlay_controls.md"),
    Path("captures/CAPTURE_BACK_FLOATING_BOARD_SURFACES_ABOVE_OVERLAY_CONTROLS.md"),
    Path("cards/265_floating_board_surfaces_above_overlay_controls_card.md"),
]:
    if not path.exists():
        errors.append(f"missing LI/capture/card file: {path}")

makefile = Path("Makefile").read_text()
verify_line = "python3 tools/verify_wc2026_floating_board_surfaces_above_overlay_controls.py"
if verify_line not in makefile:
    errors.append("Makefile verify target does not run floating surface overlay-control verifier")

if errors:
    raise SystemExit(
        "WC2026 floating board surface overlay-control verification failed:\n- "
        + "\n- ".join(errors)
    )

print("OK: pick menus and group panels are promoted above fixed overlay controls while open.")
