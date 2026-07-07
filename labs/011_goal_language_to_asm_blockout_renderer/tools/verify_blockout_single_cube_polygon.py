#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
svg_path = ROOT / "captures" / "blockout_single_cube_polygon_preview.svg"
red_svg_path = ROOT / "captures" / "blockout_single_cube_red_shaded_faces.svg"
json_path = ROOT / "dist" / "single_cube_polygon_faces.json"

for path in [svg_path, red_svg_path, json_path]:
    if not path.exists():
        raise SystemExit(f"Missing single-cube artifact: {path.relative_to(ROOT)}")

svg = red_svg_path.read_text(encoding="utf-8")
for required in [
    "<polygon",
    "top_face",
    "north_wall",
    "east_wall",
    "south_wall",
    "west_wall",
    "solid red shaded faces",
    "red_light",
    "red_mid",
    "red_mid_dark",
    "red_dark",
    "red_deep",
]:
    if required not in svg:
        raise SystemExit(f"Red shaded cube SVG missing marker: {required}")

data = json.loads(json_path.read_text(encoding="utf-8"))
if data.get("projection") != "top_down_perspective_rings":
    raise SystemExit("Single-cube polygon proof is not using top_down_perspective_rings")

if data.get("cube", {}).get("palette") != "solid_red_shaded":
    raise SystemExit("Single-cube proof does not declare solid_red_shaded palette")

palette = data.get("palette", {})
for required in ["red_light", "red_mid", "red_mid_dark", "red_dark", "red_deep"]:
    if required not in palette:
        raise SystemExit(f"Missing palette entry: {required}")

faces = data.get("faces", [])
if len(faces) != 5:
    raise SystemExit(f"Expected 5 cube faces, found {len(faces)}")

names = {face["name"] for face in faces}
expected = {"top_face", "north_wall", "east_wall", "south_wall", "west_wall"}
if names != expected:
    raise SystemExit(f"Unexpected cube face set: {names}")

for face in faces:
    pts = face.get("points", [])
    if len(pts) != 4:
        raise SystemExit(f"Face is not a quad: {face}")
    for p in pts:
        if not 0 <= p["x"] <= 255:
            raise SystemExit(f"Face x coordinate out of C64 byte range: {face}")
        if not 0 <= p["y"] <= 199:
            raise SystemExit(f"Face y coordinate out of C64 screen range: {face}")

print("OK: solid red shaded single cube polygon proof verified.")
