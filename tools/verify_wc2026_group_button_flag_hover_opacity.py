#!/usr/bin/env python3
"""Verify Card 195 group button flag hover opacity."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = ROOT / "site" / "css" / "board.css"
VIEW = ROOT / "site" / "js" / "mvc" / "view.js"
LI = ROOT / "li" / "world_cup" / "group_button_flag_hover_opacity_rule.md"
DOC = ROOT / "docs" / "features" / "group_button_flag_hover_opacity.md"
CARD = ROOT / "cards" / "195_refine_group_button_flag_hover_opacity_card.md"
CB = ROOT / "capture_back" / "CAPTURE_BACK_GROUP_BUTTON_FLAG_HOVER_OPACITY.md"


def require(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")
    return path.read_text()


def main() -> None:
    css = require(CSS)
    view = require(VIEW)
    li = require(LI)
    doc = require(DOC)
    require(CARD)
    require(CB)

    if "group-rail-flag" not in view:
        raise SystemExit("site/js/mvc/view.js must render group rail flags with class group-rail-flag")

    if "Card 195: group button flag hover opacity" not in css:
        raise SystemExit("Missing Card 195 CSS marker in board.css")

    base = re.search(r"\.group-rail-flag\s*\{(?P<body>[^}]*)\}", css, re.S)
    if not base:
        raise SystemExit("Missing .group-rail-flag base CSS rule")
    opacity = re.search(r"opacity\s*:\s*([.0-9]+)", base.group("body"))
    if not opacity:
        raise SystemExit("Missing default opacity on .group-rail-flag")
    value = float(opacity.group(1))
    if not (0 < value < 1):
        raise SystemExit(f"Default .group-rail-flag opacity must be subtle (<1), found {value}")

    required = [
        ".group-rail-tile:hover .group-rail-flag",
        ".group-rail-tile:focus-visible .group-rail-flag",
        ".group-rail-tile:active .group-rail-flag",
        ".group-rail-tile.is-active .group-rail-flag",
    ]
    for selector in required:
        if selector not in css:
            raise SystemExit(f"Missing flag active selector: {selector}")

    active_rule = re.search(
        r"\.group-rail-tile:hover\s+\.group-rail-flag\s*,\s*\.group-rail-tile:focus-visible\s+\.group-rail-flag\s*,\s*\.group-rail-tile:active\s+\.group-rail-flag\s*,\s*\.group-rail-tile\.is-active\s+\.group-rail-flag\s*\{(?P<body>[^}]*)\}",
        css,
        re.S,
    )
    if not active_rule:
        raise SystemExit("Missing grouped active flag opacity rule")
    if not re.search(r"opacity\s*:\s*1\b", active_rule.group("body")):
        raise SystemExit("Active group rail flags must set opacity: 1")

    for text, label in ((li, "LI"), (doc, "docs")):
        lowered = text.lower()
        for phrase in ("translucent", "fully opaque", "flags"):
            if phrase not in lowered:
                raise SystemExit(f"Missing phrase '{phrase}' in {label}")

    print("OK: group button flag hover opacity is captured and verified.")


if __name__ == "__main__":
    main()
