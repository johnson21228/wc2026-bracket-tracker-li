#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

errors = []

svg = Path("site/assets/playfield/uniform_pick_card_gameboard.svg").read_text()
manifest = json.loads(Path("site/data/geometry/uniform_pick_card_gameboard_manifest.json").read_text())
model = json.loads(Path("site/data/model/bracket_slots.json").read_text())
manifest_js = Path("site/data/geometry/uniform_pick_card_gameboard_manifest.js").read_text()

def attrs(tag):
    return dict(re.findall(r'([A-Za-z_:][-A-Za-z0-9_:.]*)="([^"]*)"', tag))

rects = {}
for tag in re.findall(r"<rect\b[^>]*>", svg):
    a = attrs(tag)
    sid = a.get("data-slot-id") or a.get("id")
    cls = a.get("class", "")
    if sid in {"FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"}:
        rects[sid] = a
    elif "slot-final-left" in cls:
        rects["FINAL-LEFT"] = a
    elif "slot-champion" in cls:
        rects["CHAMPION"] = a
    elif "slot-final-right" in cls:
        rects["FINAL-RIGHT"] = a

for sid in ["FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"]:
    if sid not in rects:
        errors.append(f"source-truth SVG missing {sid}")

slots = {s.get("slotId"): s for s in manifest.get("slots", [])}
for sid in ["FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"]:
    if sid not in slots:
        errors.append(f"manifest missing {sid}")
    if sid not in manifest_js:
        errors.append(f"manifest JS missing {sid}")

if "CENTER-FINAL-FOUR" in slots:
    errors.append("CENTER-FINAL-FOUR must not be runtime pick-slot geometry in manifest")

if not errors:
    def num(a, k): return float(a[k])
    left = {k: num(rects["FINAL-LEFT"], k) for k in ["x", "y", "width", "height"]}
    champ = {k: num(rects["CHAMPION"], k) for k in ["x", "y", "width", "height"]}
    right = {k: num(rects["FINAL-RIGHT"], k) for k in ["x", "y", "width", "height"]}

    if left["width"] != right["width"] or left["height"] != right["height"]:
        errors.append("FINAL-LEFT and FINAL-RIGHT dimensions must match")
    if champ["width"] != 2 * left["width"] or champ["height"] != 2 * left["height"]:
        errors.append("CHAMPION must be twice the width and height of the semifinal-winner cells")
    if not (left["y"] < champ["y"] < right["y"]):
        errors.append("Final Four center stack y-order must be FINAL-LEFT, CHAMPION, FINAL-RIGHT")

    for sid in ["FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"]:
        mb = slots[sid].get("boundsPx", {})
        for key in ["x", "y", "width", "height"]:
            if float(mb.get(key)) != float(rects[sid][key]):
                errors.append(f"{sid} manifest {key} does not match SVG")
        if "uniform_pick_card_gameboard.svg" not in slots[sid].get("source", ""):
            errors.append(f"{sid} manifest source does not point to SVG")

canonical = {s.get("slotId"): s for s in model.get("canonicalPickSlots", [])}
for sid in ["FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"]:
    if canonical.get(sid, {}).get("geometrySlotId") != sid:
        errors.append(f"{sid} canonical pick slot must point to matching geometrySlotId")

for path in [
    "captures/CAPTURE_BACK_FINAL_FOUR_CENTER_STACK_GEOMETRY_SYNC.md",
    "cards/257_sync_final_four_center_stack_geometry_card.md",
    "docs/geometry/final_four_center_stack_geometry.md",
    "li/world_cup/final_four_center_stack_geometry_rule.md",
]:
    if not Path(path).exists():
        errors.append(f"missing artifact: {path}")

if errors:
    print("Final Four center-stack geometry verification failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("OK: Final Four center-stack SVG geometry, manifests, and model geometrySlotId references are synchronized.")
