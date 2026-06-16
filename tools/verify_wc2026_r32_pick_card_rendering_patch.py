#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path.cwd()
required = [
    "li/world_cup/r32_pick_card_rendering_rule.md",
    "li/world_cup/r32_pick_card_tooltip_rule.md",
    "docs/features/r32_pick_card_rendering_and_tooltips.md",
    "cards/079_capture_r32_pick_card_rendering_rule_card.md",
    "cards/080_capture_r32_pick_card_tooltip_rule_card.md",
    "prompts/tune_r32_pick_card_rendering_and_tooltips.md",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("Missing R32 pick-card LI files:")
    for p in missing:
        print(f"- {p}")
    sys.exit(1)

html_path = ROOT / "site/game1/index.html"
if not html_path.exists():
    print("Missing site/game1/index.html")
    sys.exit(1)
html = html_path.read_text()
checks = {
    "larger pick flag": ".pickFlag { font-size: 31px;",
    "tooltip css": ".pickCard::after { content: attr(data-tooltip);",
    "pick layer above hit layer": ".pickLayer { z-index: 3; pointer-events: none; }",
    "pick card pointer events": "pointer-events: auto; overflow: visible; cursor: pointer;",
    "tooltip helper": "function r32PickTooltipText(pick, rule)",
    "accessible card label": "function r32PickAriaLabel(pick, rule)",
    "card title tooltip": "card.setAttribute(\"title\", tooltip);",
    "click card to reopen menu": "card.addEventListener(\"click\", ev => openMenu(rule, ev));",
    "quiet visible rule": "<span class=\"pickRule\" aria-hidden=\"true\">",
}
failed = [name for name, needle in checks.items() if needle not in html]
if failed:
    print("R32 pick-card rendering patch checks failed:")
    for name in failed:
        print(f"- {name}")
    sys.exit(1)

if "aria-hidden=\"true\"></div>" in html and "pickLayer" in html:
    print("pickLayer still appears aria-hidden; filled cards should be inspectable")
    sys.exit(1)

print("WC2026 R32 pick-card rendering and tooltip checks passed.")
