#!/usr/bin/env python3
from pathlib import Path

VIEW = Path("site/js/mvc/view.js")
view = VIEW.read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require("function playerFacingEmptyPickText(slot)" in view, "missing player-facing empty pick label function")
require('round === "R32" || slotId.startsWith("R32")' in view, "R32 empty labels must be distinguished by round or slot id")
require('return "Choose Team";' in view, "R32 empty labels must remain Choose Team")
require('return "Choose Winner";' in view, "R16 and later empty labels must be Choose Winner")
require("function unpickedSlotDisplayText(slot)" in view, "missing unpicked slot display wrapper")
require("return playerFacingEmptyPickText(slot);" in view, "unpicked cells must use playerFacingEmptyPickText(slot)")

for obsolete in [
    'if (slotId === "CHAMPION") return "Champion";',
    'if (slotId === "THIRD-PLACE-WINNER") return "3rd place";',
    'return "Pick";',
]:
    require(obsolete not in view, f"obsolete empty label remains: {obsolete}")

if errors:
    print("WC2026 empty pick label verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 empty pick labels use Choose Team for R32 and Choose Winner for R16 and later rounds.")
