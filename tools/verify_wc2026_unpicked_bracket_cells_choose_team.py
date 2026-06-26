#!/usr/bin/env python3
from pathlib import Path

VIEW = Path("site/js/mvc/view.js")
view = VIEW.read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require("function emptyPickLabelForSlot(slotId)" in view, "missing emptyPickLabelForSlot(slotId)")
require('return normalizedSlotId.startsWith("R32") ? "" : "Choose Winner";' in view,
        "R32 empty labels must be blank while R16+ empty labels remain Choose Winner")
require("function playerFacingEmptyPickText(slot)" in view, "missing player-facing empty pick label function")
require('if (round === "R32" || slotId.startsWith("R32")) return "";' in view,
        "R32 player-facing empty labels must be blank/read-only")
require('return "Choose Winner";' in view, "R16 and later empty labels must be Choose Winner")
require("function unpickedSlotDisplayText(slot)" in view, "missing unpicked slot display wrapper")
require("return playerFacingEmptyPickText(slot);" in view, "unpicked cells must use playerFacingEmptyPickText(slot)")

for obsolete in [
    'return normalizedSlotId.startsWith("R32") ? "Choose Team" : "Choose Winner";',
    'if (round === "R32" || slotId.startsWith("R32")) return "Choose Team";',
    'return "Choose Team";',
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

print("OK: R32 empty labels are blank/read-only while R16 and later empty slots use Choose Winner.")
