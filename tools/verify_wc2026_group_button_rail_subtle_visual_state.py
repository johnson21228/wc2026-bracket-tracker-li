#!/usr/bin/env python3
"""Verify Card 193 group button rail subtle visual state."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS = ROOT / "site" / "css" / "board.css"
LI = ROOT / "li" / "world_cup" / "group_button_rail_rule.md"
DOC = ROOT / "docs" / "features" / "group_button_rail.md"
CARD = ROOT / "cards" / "193_refine_group_button_rail_subtle_visual_state_card.md"
CB = ROOT / "capture_back" / "CAPTURE_BACK_GROUP_BUTTON_RAIL_SUBTLE_VISUAL_STATE.md"


def require(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")
    return path.read_text()


def main() -> None:
    css = require(CSS)
    li = require(LI)
    doc = require(DOC)
    require(CARD)
    require(CB)

    if "Card 193: group button rail subtle visual state" not in css:
        raise SystemExit("Missing Card 193 CSS marker in board.css")

    base_match = re.search(r"\.group-rail-tile\s*\{(?P<body>[^}]*)\}", css, re.S)
    if not base_match:
        raise SystemExit("Missing .group-rail-tile base CSS rule")
    base_body = base_match.group("body")
    opacity_match = re.search(r"opacity\s*:\s*([.0-9]+)", base_body)
    if not opacity_match:
        raise SystemExit("Missing default opacity on .group-rail-tile")
    opacity = float(opacity_match.group(1))
    if not (0 < opacity < 1):
        raise SystemExit(f"Default .group-rail-tile opacity must be subtle (<1), found {opacity}")

    active_selectors = [
        ".group-rail-tile:hover",
        ".group-rail-tile:focus-visible",
        ".group-rail-tile:active",
        ".group-rail-tile.is-active",
    ]
    for selector in active_selectors:
        if selector not in css:
            raise SystemExit(f"Missing active selector: {selector}")

    active_rule_match = re.search(
        r"\.group-rail-tile:hover\s*,\s*\.group-rail-tile:focus-visible\s*,\s*\.group-rail-tile:active\s*,\s*\.group-rail-tile\.is-active\s*\{(?P<body>[^}]*)\}",
        css,
        re.S,
    )
    if not active_rule_match:
        raise SystemExit("Missing grouped active state CSS rule for group rail tile")
    if not re.search(r"opacity\s*:\s*1\b", active_rule_match.group("body")):
        raise SystemExit("Active group rail tile state must set opacity: 1")

    for text, label in ((li, "LI"), (doc, "docs")):
        lowered = text.lower()
        for phrase in ("subtle", "translucent", "fully opaque"):
            if phrase not in lowered:
                raise SystemExit(f"Missing phrase '{phrase}' in {label}")

    print("OK: group button rail subtle visual state is captured and verified.")


if __name__ == "__main__":
    main()
