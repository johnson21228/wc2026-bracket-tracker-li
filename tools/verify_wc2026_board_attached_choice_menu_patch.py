#!/usr/bin/env python3
"""Verify WC2026 board-attached choice menu patch."""
from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()
SITE = ROOT / "site" / "index.html"
REQUIRED_FILES = [
    ROOT / "cards" / "144_anchor_choice_menu_to_board_scroll_surface_card.md",
    ROOT / "docs" / "features" / "board_attached_choice_menu.md",
    ROOT / "li" / "world_cup" / "board_attached_choice_menu_rule.md",
    ROOT / "prompts" / "verify_board_attached_choice_menu.md",
    ROOT / "tools" / "verify_wc2026_board_attached_choice_menu_patch.py",
]
REQUIRED_SITE_MARKERS = [
    "WC2026_BOARD_ATTACHED_CHOICE_MENU_START",
    "WC2026_BOARD_ATTACHED_CHOICE_MENU_END",
    "WC2026_BOARD_ATTACHED_CHOICE_MENU_CSS_START",
    "WC2026_DROP_CLOSE_ON_SCROLL_START",
    "WC2026_BOARD_SCROLL_DOES_NOT_CLOSE_CHOICE_MENU",
    "WC2026_BOARD_ATTACHED_CHOICE_MENU_INSTALLED",
    "WC2026_ATTACH_OPEN_CHOICE_MENUS_TO_BOARD",
    "wc2026-board-attached-choice-menu",
    "MutationObserver",
    "board.appendChild(menu)",
    "window.removeEventListener(\"scroll\"",
    "document.removeEventListener(\"touchmove\"",
]


def fail(message: str) -> None:
    raise SystemExit(f"Board-attached choice menu verification failed: {message}")


def main() -> None:
    if not SITE.exists():
        fail("missing site/index.html")
    text = SITE.read_text(encoding="utf-8")
    for marker in REQUIRED_SITE_MARKERS:
        if marker not in text:
            fail(f"missing site marker: {marker}")
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(f"missing expected repo file: {path.relative_to(ROOT)}")
    if text.count("WC2026_BOARD_ATTACHED_CHOICE_MENU_START") != 1:
        fail("expected one board-attached choice menu JS marker")
    if text.count("WC2026_BOARD_ATTACHED_CHOICE_MENU_CSS_START") != 1:
        fail("expected one board-attached choice menu CSS marker")
    print("Board-attached choice menu verification passed.")


if __name__ == "__main__":
    main()
