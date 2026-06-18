#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()
REQUIRED = [
    Path("cards/183_define_group_standings_panel_li_card.md"),
    Path("li/world_cup/group_standings_panel_rule.md"),
    Path("docs/features/group_standings_panel.md"),
    Path("capture_back/CAPTURE_BACK_GROUP_STANDINGS_PANEL_LI.md"),
]


def require_contains(path: Path, text: str) -> None:
    body = (ROOT / path).read_text()
    if text not in body:
        raise SystemExit(f"Missing required text in {path}: {text}")


def main() -> int:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            raise SystemExit(f"Missing required file: {rel}")

    rule = Path("li/world_cup/group_standings_panel_rule.md")
    require_contains(rule, "single site runtime")
    require_contains(rule, "site/data/current/group_standings.json")
    require_contains(rule, "not as direct browser scraping")
    require_contains(rule, "Model loads group standings")
    require_contains(rule, "View renders the standings panel")
    require_contains(rule, "Controller opens and closes the panel")
    require_contains(rule, "FIFA-constrained group-source slots")
    require_contains(rule, "must not invent a highlight URL")

    print("WC2026 group standings panel LI verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
