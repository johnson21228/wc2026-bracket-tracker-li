#!/usr/bin/env python3
from pathlib import Path
import json
import sys

errors = []
manifest = json.loads(Path("site/data/geometry/uniform_pick_card_gameboard_manifest.json").read_text())
slot_ids = {s.get("slotId") for s in manifest.get("slots", [])}

if "CENTER-FINAL-FOUR" in slot_ids:
    errors.append("CENTER-FINAL-FOUR must not be runtime pick-slot geometry after center-stack sync")

for sid in ["FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"]:
    if sid not in slot_ids:
        errors.append(f"missing explicit center-stack geometry: {sid}")

if errors:
    print("CENTER-FINAL-FOUR replacement verification failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("OK: CENTER-FINAL-FOUR is replaced by explicit source-derived center-stack geometry.")
