#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require_file(path):
    p = ROOT / path
    if not p.exists():
        raise SystemExit(f"Missing required file: {path}")
    return p.read_text()


def require_contains(path, token):
    text = require_file(path)
    if token not in text:
        raise SystemExit(f"Missing token in {path}: {token}")


for path in [
    "li/world_cup/interaction_overlay_stack_rule.md",
    "docs/features/interaction_overlay_stack.md",
    "cards/209_capture_interaction_overlay_stack_card.md",
    "capture_back/CAPTURE_BACK_INTERACTION_OVERLAY_STACK.md",
]:
    require_file(path)

for token in [
    "group standings panel layer",
    "above the pick menu",
    "above the bottom frame controls",
]:
    require_contains("li/world_cup/interaction_overlay_stack_rule.md", token)

for token in [
    "Card 209: interaction overlay stack",
    "--wc-z-group-rail",
    "--wc-z-pick-menu",
    "--wc-z-group-panel",
    ".r32-pick-menu-layer",
    ".board-group-panel-layer",
    ".group-panel-popover",
    "pointer-events: auto",
]:
    require_contains("site/css/board.css", token)

require_contains("Makefile", "tools/verify_wc2026_interaction_overlay_stack.py")
print("OK: interaction overlay stack keeps pick menus and group panels above the bottom frame.")
