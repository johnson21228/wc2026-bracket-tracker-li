#!/usr/bin/env python3
from pathlib import Path
import json
import re

SVG_PATH = Path("site/assets/playfield/uniform_pick_card_gameboard.svg")
JSON_MANIFESTS = [
    Path("site/data/geometry/gameboard_manifest.json"),
    Path("site/data/geometry/uniform_pick_card_gameboard_manifest.json"),
]
JS_MANIFEST = Path("site/data/geometry/uniform_pick_card_gameboard_manifest.js")

SVG_WIDTH = 1536
EXPECTED = {"FINAL-LEFT", "CHAMPION", "FINAL-RIGHT"}

def parse_attrs(tag: str) -> dict:
    return dict(re.findall(r'([\w:-]+)="([^"]*)"', tag))

def num(value: str):
    value = float(value)
    return int(value) if value.is_integer() else value

def read_svg_slots():
    svg = SVG_PATH.read_text()
    slots = {}

    for tag in re.findall(r"<rect\b[^>]*>", svg):
        attrs = parse_attrs(tag)
        slot_id = attrs.get("data-slot-id")
        if slot_id not in EXPECTED:
            continue

        slots[slot_id] = {
            "x": num(attrs["x"]),
            "y": num(attrs["y"]),
            "width": num(attrs["width"]),
            "height": num(attrs["height"]),
            "round": attrs.get("data-round"),
            "side": attrs.get("data-side"),
        }

    return slots

def read_js_manifest(path: Path):
    text = path.read_text()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"Could not parse JS manifest payload from {path}")
    return json.loads(text[start:end + 1])

def collect_manifest_slots(data):
    slots = {}

    def walk(value):
        if isinstance(value, dict):
            slot_id = value.get("slotId")
            if slot_id in EXPECTED:
                bounds = value.get("boundsPx") or value.get("bounds")
                if bounds:
                    slots[slot_id] = {
                        "x": bounds["x"],
                        "y": bounds["y"],
                        "width": bounds["width"],
                        "height": bounds["height"],
                    }
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(data)
    return slots

def bounds_only(slots):
    return {
        slot_id: {
            "x": slot["x"],
            "y": slot["y"],
            "width": slot["width"],
            "height": slot["height"],
        }
        for slot_id, slot in slots.items()
    }

def main():
    errors = []

    svg_slots = read_svg_slots()
    missing = EXPECTED - set(svg_slots)
    if missing:
        errors.extend(f"source-truth SVG missing {slot_id}" for slot_id in sorted(missing))
    else:
        left = svg_slots["FINAL-LEFT"]
        champion = svg_slots["CHAMPION"]
        right = svg_slots["FINAL-RIGHT"]

        if left["width"] != 140 or left["height"] != 44:
            errors.append("FINAL-LEFT must use standard pick-card size 140x44.")
        if right["width"] != 140 or right["height"] != 44:
            errors.append("FINAL-RIGHT must use standard pick-card size 140x44.")
        if champion["width"] != 140 or champion["height"] != 44:
            errors.append("CHAMPION must use standard pick-card size 140x44.")

        if champion["y"] >= left["y"] or champion["y"] >= right["y"]:
            errors.append("CHAMPION must sit above FINAL-LEFT and FINAL-RIGHT.")

        if left["y"] != right["y"]:
            errors.append("FINAL-LEFT and FINAL-RIGHT must share the same y coordinate.")

        svg_center_x = SVG_WIDTH / 2
        champion_center_x = champion["x"] + champion["width"] / 2
        if abs(champion_center_x - svg_center_x) > 1:
            errors.append(f"CHAMPION must be centered on SVG centerline {svg_center_x}; got {champion_center_x}.")

        left_center_x = left["x"] + left["width"] / 2
        right_center_x = right["x"] + right["width"] / 2
        if abs((svg_center_x - left_center_x) - (right_center_x - svg_center_x)) > 1:
            errors.append("FINAL-LEFT and FINAL-RIGHT must be mirrored around the SVG centerline.")

        if left.get("round") != "SF_WINNER":
            errors.append("FINAL-LEFT SVG slot must be data-round=SF_WINNER.")
        if right.get("round") != "SF_WINNER":
            errors.append("FINAL-RIGHT SVG slot must be data-round=SF_WINNER.")
        if champion.get("round") != "CHAMPION":
            errors.append("CHAMPION SVG slot must be data-round=CHAMPION.")

    svg_bounds = bounds_only(svg_slots)

    for path in JSON_MANIFESTS:
        manifest_slots = collect_manifest_slots(json.loads(path.read_text()))
        if manifest_slots != svg_bounds:
            errors.append(f"{path} center-stack geometry must be derived from source-truth SVG. manifest={manifest_slots} svg={svg_bounds}")

    js_slots = collect_manifest_slots(read_js_manifest(JS_MANIFEST))
    if js_slots != svg_bounds:
        errors.append(f"{JS_MANIFEST} center-stack geometry must be derived from source-truth SVG. manifest={js_slots} svg={svg_bounds}")

    if errors:
        print("Final Four center-stack geometry verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: Final Four center-stack geometry uses SVG truth with same-size top-center champion and mirrored SF winner slots.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
