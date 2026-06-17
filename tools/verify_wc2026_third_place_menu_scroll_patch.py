#!/usr/bin/env python3
"""Verify WC2026 long 3rd-place menu internal scroll patch."""
from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()
SITE = ROOT / "site" / "index.html"
REQUIRED_FILES = [
    ROOT / "cards" / "138_repair_third_place_menu_scroll_card.md",
    ROOT / "docs" / "features" / "third_place_menu_scroll.md",
    ROOT / "li" / "world_cup" / "third_place_menu_scroll_rule.md",
    ROOT / "prompts" / "verify_third_place_menu_scroll.md",
    ROOT / "tools" / "verify_wc2026_third_place_menu_scroll_patch.py",
]
REQUIRED_SITE_MARKERS = [
    "WC2026_LONG_CHOICE_MENU_INTERNAL_SCROLL_START",
    "WC2026_LONG_CHOICE_MENU_INTERNAL_SCROLL_END",
    "WC2026_LONG_CHOICE_MENU_INTERNAL_SCROLL_INSTALLED",
    "WC2026_IS_CHOICE_MENU_SCROLL_TARGET",
    "overscroll-behavior: contain",
    "-webkit-overflow-scrolling: touch",
    "touch-action: pan-y",
    "document.addEventListener(\"wheel\"",
    "document.addEventListener(\"touchmove\"",
    "event.stopPropagation()",
]


def fail(message: str) -> None:
    raise SystemExit(f"Third-place menu scroll verification failed: {message}")


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
    if text.count("WC2026_LONG_CHOICE_MENU_INTERNAL_SCROLL_START") != 2:
        fail("expected one CSS marker and one JS marker for long menu scrolling")
    marker = text.find("WC2026_PAGES_REVIEW_PICK_ACCEPTANCE_START")
    if marker != -1:
        prev_script = text.rfind("<script", 0, marker)
        prev_script_close = text.rfind("</script>", 0, marker)
        if prev_script <= prev_script_close:
            fail("pages review pick acceptance JS marker appears outside a script tag")
    print("Third-place menu scroll patch verification passed.")


if __name__ == "__main__":
    main()
