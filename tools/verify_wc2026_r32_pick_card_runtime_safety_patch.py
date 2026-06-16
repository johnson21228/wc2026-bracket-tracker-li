#!/usr/bin/env python3
from pathlib import Path
import re

root = Path.cwd()
html_path = root / "site/game1/index.html"
html = html_path.read_text()

required = [
    "pickCard",
    "pickFlag",
    "pickName",
    "function r32CardDisplayName(team)",
    "card.replaceChildren",
]
missing = [s for s in required if s not in html]
if missing:
    raise SystemExit("Missing expected R32 pick-card runtime markers: " + ", ".join(missing))

# Guard against the exact failure: quoted JS string values split by raw physical newlines.
if re.search(r'"[^"]*\n[^"]*"', html):
    # This regex can also match escaped text in HTML broadly; specifically forbid the known bad table.
    bad_patterns = [
        '"Saudi\nArabia"',
        '"South\nAfrica"',
        '"New\nZealand"',
        '"Cape\nVerde"',
        '"South\nKorea"',
        '"Ivory\nCoast"',
        '"DR\nCongo"',
    ]
    for pattern in bad_patterns:
        if pattern in html:
            raise SystemExit("Found raw newline inside JavaScript team-name string literal: " + pattern.replace("\n", "\\n"))

if 'return displayName(team);' not in html and 'R32_CARD_NAME_BREAKS[name] || name' not in html:
    raise SystemExit("r32CardDisplayName helper does not have a recognized safe return path")

for rel in [
    "li/world_cup/r32_pick_card_runtime_safety_rule.md",
    "docs/features/r32_pick_card_runtime_repair.md",
    "cards/084_repair_r32_pick_card_runtime_safety_card.md",
]:
    if not (root / rel).exists():
        raise SystemExit(f"Missing expected LI artifact: {rel}")

print("WC2026 R32 pick-card runtime safety repair checks passed.")
