#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path.cwd()

REQUIRED = [
    "li/world_cup/modular_mvc_tdd_source_rule.md",
    "li/world_cup/static_html_release_rule.md",
    "docs/architecture/wc2026_modular_mvc_tdd_source_boundary.md",
    "cards/151_remove_static_single_file_architecture_goal_card.md",
    "prompts/remove_static_single_file_architecture_goal.md",
    "capture_back/CAPTURE_BACK_REMOVE_STATIC_SINGLE_FILE_ARCHITECTURE_GOAL.md",
]

BANNED_CURRENT_LI_PHRASES = [
    "remain usable as a single static HTML file",
    "single static HTML file",
    "single HTML file",
    "single-file portability",
    "static-single-file portability",
    "static HTML portability",
    "strive for a single",
]

REQUIRED_RULE_TOKENS = [
    "Modular MVC/TDD",
    "Do not preserve or introduce a monolithic HTML portability goal",
    "Model",
    "View",
    "Controller",
    "TDD rule",
]


def fail(title: str, items: list[str]) -> None:
    print(title)
    for item in items:
        print(f"- {item}")
    sys.exit(1)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")


def main() -> int:
    missing = [rel for rel in REQUIRED if not (ROOT / rel).exists()]
    if missing:
        fail("Missing modular source boundary files:", missing)

    removed = ROOT / "li/world_cup/mvc_tdd_static_html_bridge_rule.md"
    if removed.exists():
        fail("Static HTML bridge LI must be removed:", [str(removed.relative_to(ROOT))])

    current_li_files = sorted((ROOT / "li").rglob("*.md"))
    banned_hits: list[str] = []
    for path in current_li_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for phrase in BANNED_CURRENT_LI_PHRASES:
            if phrase.lower() in text.lower():
                banned_hits.append(f"{path.relative_to(ROOT)}: {phrase}")

    if banned_hits:
        fail("Current LI still encourages static-monolithic architecture:", banned_hits)

    rule = read("li/world_cup/modular_mvc_tdd_source_rule.md")
    missing_tokens = [token for token in REQUIRED_RULE_TOKENS if token not in rule]
    if missing_tokens:
        fail("Modular MVC/TDD source rule is missing required tokens:", missing_tokens)

    static_rule = read("li/world_cup/static_html_release_rule.md")
    if "single static HTML file" in static_rule or "single HTML file" in static_rule:
        fail("Static hostable rule still uses monolithic framing:", ["li/world_cup/static_html_release_rule.md"])
    if "multiple HTML, JavaScript, CSS, JSON, image, and data assets" not in static_rule:
        fail("Static hostable rule must explicitly allow modular asset deployment:", ["li/world_cup/static_html_release_rule.md"])

    readme = read("README.md")
    if "static-first" in readme.lower():
        fail("README still describes the repo as static-first:", ["README.md"])

    print("WC2026 modular MVC/TDD source boundary verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
