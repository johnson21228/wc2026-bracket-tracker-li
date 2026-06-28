#!/usr/bin/env python3
from pathlib import Path
import re

view = Path("site/js/mvc/view.js").read_text()

errors = []

required = [
    "function resolvedSlotTooltipText(slot, pick)",
    "pick?.teamName",
    "slot?.teamName",
    "return `${teamName} (${teamCode})`",
    "resolvedSlotTooltipText(slot, pick)",
]

for needle in required:
    if needle not in view:
        errors.append(f"Missing R32 tooltip team-name contract fragment: {needle}")

if not re.search(r"\.title\s*=\s*resolvedSlotTooltipText\(slot,\s*pick\)", view):
    errors.append("No slot title assignment uses resolvedSlotTooltipText(slot, pick).")

if errors:
    print("WC2026 R32 tooltip team-name verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: R32 slot tooltips prefer resolved team name/code.")
