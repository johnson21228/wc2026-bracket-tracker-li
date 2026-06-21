#!/usr/bin/env python3
from pathlib import Path

def require(text, token, label, errors):
    if token not in text:
        errors.append(f"missing {label}: {token}")

def main():
    errors = []
    model = Path("site/js/mvc/model.js").read_text()
    require(model, 'const CENTER_FINAL_FOUR_SLOT_ID = "CENTER-FINAL-FOUR";', "center final four slot constant", errors)
    require(model, "function isVisualOnlyGeometrySlot", "visual-only geometry predicate", errors)
    require(model, 'slot?.slotId === CENTER_FINAL_FOUR_SLOT_ID', "CENTER-FINAL-FOUR visual-only rule", errors)
    require(model, 'slot?.round === "FINAL_FOUR"', "FINAL_FOUR round visual-only rule", errors)
    require(model, "function pickSurfaceSlots", "pick-surface slot filter", errors)
    require(model, "return pickSurfaceSlots(slots).map((slot) => {", "slot view models exclude visual-only geometry", errors)
    require(model, "totalSlots: pickSurfaceSlots(slots).length", "summary excludes visual-only geometry", errors)

    if errors:
        print("Center Final Four visual-only verification failed: " + "; ".join(errors))
        return 1

    print("OK: CENTER-FINAL-FOUR remains SVG geometry only and is not rendered as a pick-slot button.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
