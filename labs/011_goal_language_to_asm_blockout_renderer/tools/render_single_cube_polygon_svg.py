#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
CAPTURES = ROOT / "captures"

def ensure_generated() -> None:
    if not (DIST / "projection_metadata.json").exists():
        subprocess.run(["python3", "tools/generate_blockout_renderer.py"], cwd=ROOT, check=True)

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

def ring_for_z(intent: dict, z: int) -> dict:
    rings = sorted(intent["projection"]["depth_rings"], key=lambda r: r["z"])
    if z <= rings[0]["z"]:
        return dict(rings[0])
    if z >= rings[-1]["z"]:
        return dict(rings[-1])
    for a, b in zip(rings, rings[1:]):
        if a["z"] <= z <= b["z"]:
            span = b["z"] - a["z"]
            t = 0 if span == 0 else (z - a["z"]) / span
            return {
                "z": z,
                "width": round(lerp(a["width"], b["width"], t)),
                "height": round(lerp(a["height"], b["height"], t)),
            }
    raise ValueError(f"No ring for z={z}")

def project(intent: dict, x: int, y: int, z: int) -> tuple[int, int]:
    p = intent["projection"]
    pit = intent["pit"]
    ring = ring_for_z(intent, z)
    left = p["center_x"] - ring["width"] / 2
    top = p["center_y"] - ring["height"] / 2
    sx = round(left + x * ring["width"] / pit["width"])
    sy = round(top + y * ring["height"] / pit["depth"])
    return sx, sy

def face(points: list[tuple[int, int]], name: str, shade: str) -> dict:
    return {
        "name": name,
        "shade": shade,
        "points": [{"x": x, "y": y} for x, y in points],
    }

def svg_poly(points: list[dict], klass: str) -> str:
    pts = " ".join(f"{p['x']},{p['y']}" for p in points)
    return f'<polygon class="{klass}" points="{pts}" />'

def main() -> None:
    ensure_generated()

    intent = json.loads((ROOT / "goal" / "renderer_intent.json").read_text(encoding="utf-8"))
    if intent["projection"].get("type") != "top_down_perspective_rings":
        raise SystemExit("Single-cube polygon proof requires top_down_perspective_rings")

    # One cube in the pit. It occupies one board cell and one depth step.
    cube = {
        "x": 2,
        "y": 2,
        "z": 3,
        "width": 1,
        "depth": 1,
        "height": 1,
    }

    x0, y0, z0 = cube["x"], cube["y"], cube["z"]
    x1, y1, z1 = x0 + cube["width"], y0 + cube["depth"], z0 + cube["height"]

    # Top face at shallower z. Bottom face at deeper z.
    a = project(intent, x0, y0, z0)
    b = project(intent, x1, y0, z0)
    c = project(intent, x1, y1, z0)
    d = project(intent, x0, y1, z0)

    e = project(intent, x0, y0, z1)
    f = project(intent, x1, y0, z1)
    g = project(intent, x1, y1, z1)
    h = project(intent, x0, y1, z1)

    faces = [
        face([e, f, b, a], "north_wall", "dark"),
        face([f, g, c, b], "east_wall", "mid"),
        face([g, h, d, c], "south_wall", "darkest"),
        face([h, e, a, d], "west_wall", "mid_dark"),
        face([a, b, c, d], "top_face", "light"),
    ]

    xs = []
    ys = []
    for one_face in faces:
        for p in one_face["points"]:
            xs.append(p["x"])
            ys.append(p["y"])

    min_x = min(xs) - 24
    max_x = max(xs) + 24
    min_y = min(ys) - 24
    max_y = max(ys) + 28
    width = max_x - min_x
    height = max_y - min_y

    def shifted(face_data: dict) -> dict:
        return {
            **face_data,
            "points": [{"x": p["x"] - min_x, "y": p["y"] - min_y} for p in face_data["points"]],
        }

    shifted_faces = [shifted(f) for f in faces]

    polygons = []
    for fdata in shifted_faces:
        polygons.append(svg_poly(fdata["points"], f"cube {fdata['name']} {fdata['shade']}"))

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '  <title id="title">Lab 011 single cube shaded polygon proof</title>',
        '  <desc id="desc">One projected cube inside the perspective pit, decomposed into shaded polygon faces.</desc>',
        '  <style>',
        '    .bg { fill: #11131a; }',
        '    .cube { stroke: #f8f8f2; stroke-width: 1.2; vector-effect: non-scaling-stroke; }',
        '    .light { fill: #f7d85c; }',
        '    .mid { fill: #d6b84c; }',
        '    .mid_dark { fill: #a88d38; }',
        '    .dark { fill: #7c6729; }',
        '    .darkest { fill: #55461d; }',
        '    .label { fill: #e8eaed; font: 9px monospace; }',
        '  </style>',
        f'  <rect class="bg" x="0" y="0" width="{width}" height="{height}" />',
        *["  " + poly for poly in polygons],
        '  <text class="label" x="6" y="12">single cube · shaded polygon faces</text>',
        '</svg>',
        '',
    ]

    CAPTURES.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)

    svg_path = CAPTURES / "blockout_single_cube_polygon_preview.svg"
    json_path = DIST / "single_cube_polygon_faces.json"

    svg_path.write_text("\n".join(svg_parts), encoding="utf-8")
    json_path.write_text(json.dumps({
        "source": "goal/renderer_intent.json",
        "projection": intent["projection"]["type"],
        "purpose": "single cube shaded polygon proof before C64 bitmap/span fill",
        "cube": cube,
        "faces": faces,
    }, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {svg_path}")
    print(f"Wrote {json_path}")
    print("Generated one shaded cube as polygon faces.")

if __name__ == "__main__":
    main()
