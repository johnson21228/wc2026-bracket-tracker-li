#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

errors = []

svg_path = Path("site/assets/playfield/uniform_pick_card_gameboard.svg")
manifest_path = Path("site/data/geometry/uniform_pick_card_gameboard_manifest.json")

svg = svg_path.read_text()
manifest = json.loads(manifest_path.read_text())

required_ids = ["FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"]
for slot_id in required_ids:
    if slot_id not in svg:
        errors.append(f"source-truth SVG missing {slot_id}")

slots = manifest.get("slots", [])
by_id = {slot.get("slotId"): slot for slot in slots}

for slot_id in required_ids:
    if slot_id not in by_id:
        errors.append(f"manifest missing {slot_id}")

if "CENTER-FINAL-FOUR" in by_id:
    errors.append("CENTER-FINAL-FOUR must not remain runtime pick-slot geometry")

counts = manifest.get("boardModel", {}).get("roundCounts", {})
expected = {"R32": 32, "R16": 16, "QF": 8, "SF": 4, "SF_WINNER": 2, "CHAMPION": 1}
for key, value in expected.items():
    if counts.get(key) != value:
        errors.append(f"roundCounts[{key}] expected {value}, found {counts.get(key)}")

if counts.get("FINAL_FOUR"):
    errors.append("roundCounts must not keep FINAL_FOUR after center-stack geometry sync")

if not errors:
    left = by_id["FINAL-LEFT"]["boundsPx"]
    champion = by_id["CHAMPION"]["boundsPx"]
    right = by_id["FINAL-RIGHT"]["boundsPx"]

    if left["width"] != right["width"] or left["height"] != right["height"]:
        errors.append("FINAL-LEFT and FINAL-RIGHT must have matching dimensions")

    if champion["width"] != 2 * left["width"] or champion["height"] != 2 * left["height"]:
        errors.append("CHAMPION must be twice the width and height of FINAL-LEFT / FINAL-RIGHT")

if errors:
    print("Uniform SVG gameboard verification failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK: uniform SVG gameboard uses source-derived Final Four center-stack geometry.")
