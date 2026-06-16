#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "li/world_cup/uniform_svg_gameboard_authority_rule.md",
    "docs/geometry/uniform_svg_gameboard_authority.md",
    "cards/093_adopt_uniform_svg_gameboard_authority_card.md",
    "cards/094_repair_uniform_svg_gameboard_manifest_authority_card.md",
    "prompts/adopt_uniform_svg_gameboard_authority.md",
    "prompts/repair_uniform_svg_gameboard_manifest_authority.md",
    "capture_back/CAPTURE_BACK_UNIFORM_SVG_GAMEBOARD_AUTHORITY.md",
    "capture_back/CAPTURE_BACK_UNIFORM_SVG_GAMEBOARD_MANIFEST_AUTHORITY_REPAIR.md",
    "tools/generate_uniform_pick_card_gameboard.py",
    "site/assets/playfield/uniform_pick_card_gameboard.svg",
    "site/assets/playfield/uniform_pick_card_gameboard.png",
    "site/data/geometry/uniform_pick_card_gameboard_manifest.json",
]
EXPECTED_COUNTS = {"R32": 32, "R16": 16, "QF": 8, "SF": 4, "FINAL_FOUR": 1}
EXPECTED_TOTAL = sum(EXPECTED_COUNTS.values())

def fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    raise SystemExit(1)

def as_num(v):
    n = float(v)
    return int(n) if abs(n - round(n)) < 1e-9 else n

def svg_pick_rects(svg: Path):
    try:
        root = ET.parse(svg).getroot()
    except Exception as exc:
        fail(f"SVG is not well-formed XML: {exc}")
    group = None
    for elem in root.iter():
        if elem.tag.endswith("g") and elem.attrib.get("id") == "pick-card-slots":
            group = elem
            break
    if group is None:
        fail("SVG missing <g id='pick-card-slots'>")
    return [elem for elem in list(group) if elem.tag.endswith("rect")]

def main() -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            fail(f"Missing required file: {rel}")

    svg = ROOT / "site/assets/playfield/uniform_pick_card_gameboard.svg"
    svg_text = svg.read_text(encoding="utf-8")
    for marker in ["connector-linework", "pick-card-slots"]:
        if marker not in svg_text:
            fail(f"SVG missing expected marker: {marker}")

    rects = svg_pick_rects(svg)
    if len(rects) != EXPECTED_TOTAL:
        fail(f"Expected {EXPECTED_TOTAL} SVG pick-card rects for current board model; found {len(rects)}")

    manifest_path = ROOT / "site/data/geometry/uniform_pick_card_gameboard_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("authority") != "svg_geometry_source":
        fail("Manifest must declare authority = svg_geometry_source")
    if manifest.get("svgAsset") != "assets/playfield/uniform_pick_card_gameboard.svg":
        fail("Manifest svgAsset must point to uniform_pick_card_gameboard.svg")
    if manifest.get("pngAsset") != "assets/playfield/uniform_pick_card_gameboard.png":
        fail("Manifest pngAsset must point to uniform_pick_card_gameboard.png")

    slots = manifest.get("slots", [])
    if len(slots) != EXPECTED_TOTAL:
        fail(f"Expected {EXPECTED_TOTAL} manifest slots for current board model; found {len(slots)}")
    counts = Counter(s.get("round") for s in slots)
    for round_name, expected in EXPECTED_COUNTS.items():
        if counts.get(round_name) != expected:
            fail(f"Expected {expected} {round_name} slots; found {counts.get(round_name)}")

    model = manifest.get("boardModel", {})
    if model.get("expectedPickCardRecords") != EXPECTED_TOTAL:
        fail("Manifest boardModel.expectedPickCardRecords must be 61")
    if model.get("roundCounts") != EXPECTED_COUNTS:
        fail("Manifest boardModel.roundCounts must match current 61-card board model")

    final = [s for s in slots if s.get("slotId") == "CENTER-FINAL-FOUR"]
    if len(final) != 1:
        fail("Manifest must contain exactly one CENTER-FINAL-FOUR slot")
    bounds = final[0].get("boundsPx", {})
    if bounds.get("height") != 168 or bounds.get("width") != 210:
        fail("CENTER-FINAL-FOUR must be 210 x 168 in this authority artifact")

    for idx, (slot, rect) in enumerate(zip(slots, rects), start=1):
        b = slot.get("boundsPx", {})
        expected = {"x": as_num(rect.attrib["x"]), "y": as_num(rect.attrib["y"]), "width": as_num(rect.attrib["width"]), "height": as_num(rect.attrib["height"])}
        if b != expected:
            fail(f"Manifest slot {idx} {slot.get('slotId')} bounds {b} do not match SVG rect {expected}")

    li = (ROOT / "li/world_cup/uniform_svg_gameboard_authority_rule.md").read_text(encoding="utf-8")
    for phrase in ["SVG", "source-truth geometry", "Game 1 and Game 2", "FINAL_FOUR", "61 pick-card records"]:
        if phrase not in li:
            fail(f"LI rule missing phrase: {phrase}")

    # Game 1 may now display/read the uniform SVG board. Game 2 must not be migrated by Game 1 CBs.
    game2_path = ROOT / "site/game2/index.html"
    if game2_path.exists():
        game2 = game2_path.read_text(encoding="utf-8")
        if "uniform_pick_card_gameboard_manifest.js" in game2 or 'src="../assets/playfield/uniform_pick_card_gameboard.svg"' in game2:
            fail("Game 2 must not consume the uniform SVG board until an explicit Game 2 migration CB")

    print("WC2026 uniform SVG gameboard authority/manifest checks passed.")

if __name__ == "__main__":
    main()
