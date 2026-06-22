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
EXPECTED = {"FINAL-LEFT", "FINAL-RIGHT", "CHAMPION"}
SVG_WIDTH = 1536


def parse_attrs(tag: str) -> dict:
    return dict(re.findall(r'([\w:-]+)="([^"]*)"', tag))


def num(value: str):
    value = float(value)
    return int(value) if value.is_integer() else value


def svg_final_stack_bounds():
    svg = SVG_PATH.read_text()
    found = {}
    for tag in re.findall(r"<rect\b[^>]*>", svg):
        attrs = parse_attrs(tag)
        if "pick-card-slot" not in attrs.get("class", ""):
            continue
        round_name = attrs.get("data-round")
        side = attrs.get("data-side")

        slot_id = None
        if round_name == "SF_WINNER" and side == "left":
            slot_id = "FINAL-LEFT"
        elif round_name == "SF_WINNER" and side == "right":
            slot_id = "FINAL-RIGHT"
        elif round_name == "CHAMPION" and side == "center":
            slot_id = "CHAMPION"

        if slot_id:
            found[slot_id] = {
                "x": num(attrs["x"]),
                "y": num(attrs["y"]),
                "width": num(attrs["width"]),
                "height": num(attrs["height"]),
            }
    return found


def collect_manifest_bounds(data):
    found = {}

    def walk(value):
        if isinstance(value, dict):
            slot_id = value.get("slotId")
            if slot_id in EXPECTED:
                bounds = value.get("boundsPx") or value.get("bounds")
                if bounds:
                    found[slot_id] = {
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
    return found


def read_js_manifest(path):
    text = path.read_text()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"Could not parse JSON payload from {path}")
    return json.loads(text[start:end + 1])


def main():
    errors = []
    svg_bounds = svg_final_stack_bounds()

    if set(svg_bounds) != EXPECTED:
        errors.append(f"SVG final-stack slots mismatch: found {sorted(svg_bounds)} expected {sorted(EXPECTED)}")
    else:
        left = svg_bounds["FINAL-LEFT"]
        right = svg_bounds["FINAL-RIGHT"]
        champion = svg_bounds["CHAMPION"]

        if champion["width"] != left["width"] or champion["height"] != left["height"]:
            errors.append("CHAMPION must be the same pick-card size as FINAL-LEFT/FINAL-RIGHT.")
        if champion["y"] >= left["y"]:
            errors.append("CHAMPION must be above the SF winner slots.")

        svg_center_x = SVG_WIDTH / 2
        champion_center_x = champion["x"] + champion["width"] / 2
        if abs(champion_center_x - svg_center_x) > 1:
            errors.append(f"CHAMPION must be centered on SVG centerline: got {champion_center_x}, expected {svg_center_x}.")

        left_center_x = left["x"] + left["width"] / 2
        right_center_x = right["x"] + right["width"] / 2
        if abs((svg_center_x - left_center_x) - (right_center_x - svg_center_x)) > 1:
            errors.append("FINAL-LEFT and FINAL-RIGHT must be mirrored around the SVG centerline.")

    for path in JSON_MANIFESTS:
        data = json.loads(path.read_text())
        found = collect_manifest_bounds(data)
        if found != svg_bounds:
            errors.append(f"{path} final-stack bounds do not match SVG. found={found} svg={svg_bounds}")

    js_data = read_js_manifest(JS_MANIFEST)
    js_found = collect_manifest_bounds(js_data)
    if js_found != svg_bounds:
        errors.append(f"{JS_MANIFEST} final-stack bounds do not match SVG. found={js_found} svg={svg_bounds}")

    if errors:
        print("Final-stack SVG manifest alignment failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: final-stack SVG truth and derived manifests agree for FINAL-LEFT, CHAMPION, and FINAL-RIGHT.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
