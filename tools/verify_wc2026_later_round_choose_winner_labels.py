#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIEW = ROOT / "site/js/mvc/view.js"

view = VIEW.read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

require("function emptyPickLabelForSlot(slotId)" in view,
        "missing emptyPickLabelForSlot(slotId)")
require('return normalizedSlotId.startsWith("R32") ? "TBD" : "";' in view,
        "R32 empty labels must render TBD while later waiting rounds stay blank")
require("function playerFacingEmptyPickText(slot)" in view,
        "missing playerFacingEmptyPickText(slot)")
require('if (round === "R32" || slotId.startsWith("R32")) return "TBD";' in view,
        "R32 player-facing empty labels must render TBD")
require('if (!slot?.pickable || !slotEnabledByPrecedent(slot)) return "";' in view, "later-round waiting slots must render blank")
require('return "Choose Winner";' in view,
        "later-round ready empty slots must use Choose Winner")
require('return "Choose Team";' not in view,
        "stale Choose Team label must not remain as an R32 render source")
require('.classList.add("is-tbd")' in view,
        "R32 TBD label must get small TBD styling hook")

if errors:
    print("WC2026 later-round Choose Winner label verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: R32 empty labels render small TBD, later waiting slots stay blank, and ready slots use Choose Winner.")
