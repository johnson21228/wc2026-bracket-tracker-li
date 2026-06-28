#!/usr/bin/env python3
from pathlib import Path

css = Path("site/css/app.css").read_text()

errors = []

required = [
    "Pool/Standings button must stay behind transient panels and menus",
    ".top-right-player-controls",
    ".player-standings-button",
    ".pick-menu",
    ".group-panel",
    "z-index: 120",
    "z-index: 900",
]

for needle in required:
    if needle not in css:
        errors.append(f"Missing CSS stacking contract fragment: {needle}")

if errors:
    print("WC2026 Pool button behind panels verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Pool/Standings button stays behind menus and panels.")
