#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
view = (ROOT / "site/js/mvc/view.js").read_text()
errors = []
def require(condition, message):
    if not condition: errors.append(message)
require('return normalizedSlotId.startsWith("R32") ? "" : "Choose Winner";' in view, "R32 empty labels must be blank/read-only")
require('return "Choose Winner";' in view, "later empty labels must remain Choose Winner")
require('return normalizedSlotId.startsWith("R32") ? "Choose Team" : "Choose Winner";' not in view, "stale Choose Team R32 empty label remains")
if errors:
    print("WC2026 empty pick label verification failed:")
    for e in errors: print(f"- {e}")
    raise SystemExit(1)
print("OK: R32 empty labels are blank/read-only while later empty slots use Choose Winner.")
