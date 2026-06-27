#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
view = (ROOT / "site/js/mvc/view.js").read_text()
errors = []
def require(condition, message):
    if not condition: errors.append(message)
require('return normalizedSlotId.startsWith("R32") ? "TBD" : "";' in view, "R32 empty labels must render TBD")
require('if (!slot?.pickable || !slotEnabledByPrecedent(slot)) return "";' in view, "later-round waiting slots must render blank")
require('return "Choose Winner";' in view, "later ready empty labels must remain Choose Winner")
require('return normalizedSlotId.startsWith("R32") ? "Choose Team" : "Choose Winner";' not in view, "stale Choose Team R32 empty label remains")
require('.classList.add("is-tbd")' in view, "R32 TBD label must get small TBD styling hook")
if errors:
    print("WC2026 empty pick label verification failed:")
    for e in errors: print(f"- {e}")
    raise SystemExit(1)
print("OK: R32 empty labels render small TBD, later waiting slots stay blank, and ready slots use Choose Winner.")
