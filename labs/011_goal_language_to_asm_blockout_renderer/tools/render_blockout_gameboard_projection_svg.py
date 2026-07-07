#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
CAPTURES = ROOT / "captures"

def ensure_generated() -> None:
    if not (DIST / "pit_line_segments.json").exists():
        subprocess.run(["python3", "tools/generate_blockout_renderer.py"], cwd=ROOT, check=True)

def svg_line(x1, y1, x2, y2, klass="grid"):
    return f'<line class="{klass}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" />'

def project(intent, x, y, z):
    p = intent["projection"]
    return (
        p["origin_x"] + x*p["x_axis"]["dx"] + y*p["y_axis"]["dx"] + z*p["z_axis"]["dx"],
        p["origin_y"] + x*p["x_axis"]["dy"] + y*p["y_axis"]["dy"] + z*p["z_axis"]["dy"],
    )

def main() -> None:
    ensure_generated()

    intent = json.loads((ROOT / "goal" / "renderer_intent.json").read_text(encoding="utf-8"))
    segments = json.loads((DIST / "pit_line_segments.json").read_text(encoding="utf-8"))
    pit = intent["pit"]
    w, d, h = pit["width"], pit["depth"], pit["height"]

    points = []
    for z in range(h + 1):
        for y in range(d + 1):
            for x in range(w + 1):
                points.append(project(intent, x, y, z))

    min_x = min(x for x, y in points) - 24
    max_x = max(x for x, y in points) + 24
    min_y = min(y for x, y in points) - 24
    max_y = max(y for x, y in points) + 28
    width = max_x - min_x
    height = max_y - min_y

    def tx(x): return x - min_x
    def ty(y): return y - min_y

    drawn_lines = []
    for s in segments:
        start = tuple(s["start"])
        end = tuple(s["end"])
        klass = "grid"

        # Visual classes:
        #   top   = top gameboard grid, z=0
        #   depth = rails descending into the pit, z changes
        #   side  = lower z-level projection rings, z is constant below top
        if start[2] == 0 and end[2] == 0:
            klass = "top"
        elif start[2] != end[2]:
            klass = "depth"
        elif start[2] == end[2] and start[2] > 0:
            klass = "side"

        drawn_lines.append(svg_line(tx(s["x1"]), ty(s["y1"]), tx(s["x2"]), ty(s["y2"]), klass))

    cell = [(2,2,0), (3,2,0), (3,3,0), (2,3,0)]
    cell_points = [project(intent, *p) for p in cell]
    cell_path = " ".join(f"{tx(x)},{ty(y)}" for x, y in cell_points)

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '  <title id="title">Lab 011 gameboard projection preview</title>',
        '  <desc id="desc">A projected 5 by 5 by 12 pit generated from renderer_intent.json, showing top grid, side/depth rails, and z-level projections.</desc>',
        '  <style>',
        '    .bg { fill: #11131a; }',
        '    .top { stroke: #f7d85c; stroke-width: 2; vector-effect: non-scaling-stroke; }',
        '    .side { stroke: #66d9ef; stroke-width: 1.3; opacity: 0.78; vector-effect: non-scaling-stroke; }',
        '    .depth { stroke: #ff7a7a; stroke-width: 1.8; opacity: 0.92; vector-effect: non-scaling-stroke; }',
        '    .grid { stroke: #9aa0a6; stroke-width: 1; opacity: 0.55; vector-effect: non-scaling-stroke; }',
        '    .cell { fill: #ffffff; opacity: 0.16; stroke: #ffffff; stroke-width: 1; vector-effect: non-scaling-stroke; }',
        '    .label { fill: #e8eaed; font: 10px monospace; }',
        '    .small { fill: #b8bec8; font: 8px monospace; }',
        '  </style>',
        f'  <rect class="bg" x="0" y="0" width="{width}" height="{height}" />',
        f'  <polygon class="cell" points="{cell_path}" />',
        *["  " + line for line in drawn_lines],
        '  <text class="label" x="8" y="14">Lab 011 gameboard projection</text>',
        '  <text class="small" x="8" y="28">5x5x12 pit · top grid + side/depth projections · generated from renderer_intent.json</text>',
        '</svg>',
        ''
    ]
    svg = "\n".join(svg_parts)

    CAPTURES.mkdir(parents=True, exist_ok=True)
    out = CAPTURES / "blockout_gameboard_projection.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
