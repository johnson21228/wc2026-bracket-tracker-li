#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def read(path):
    p = ROOT / path
    if not p.exists():
        fail(f"Missing required file: {path}")
    return p.read_text(encoding="utf-8")

html = read("site/game1/index.html")
manifest_text = read("site/data/geometry/uniform_pick_card_gameboard_manifest.json")
shim = read("site/data/geometry/uniform_pick_card_gameboard_manifest.js")

for path in [
    "li/world_cup/game1_reads_uniform_svg_gameboard_manifest_rule.md",
    "docs/geometry/game1_reads_uniform_svg_gameboard_manifest.md",
    "cards/095_game1_read_uniform_svg_gameboard_manifest_card.md",
    "prompts/read_uniform_svg_gameboard_manifest_in_game1.md",
    "capture_back/CAPTURE_BACK_GAME1_READ_UNIFORM_SVG_GAMEBOARD_MANIFEST.md",
]:
    read(path)

manifest = json.loads(manifest_text)
slots = manifest.get("slots") or []
if len(slots) != 61:
    fail(f"Expected 61 slots in uniform manifest; found {len(slots)}")
counts = {}
for slot in slots:
    round_name = slot.get("round")
    counts[round_name] = counts.get(round_name, 0) + 1
    b = slot.get("boundsPx") or {}
    for key in ["x", "y"]:
        if key not in b:
            fail(f"Slot {slot.get('slotId')} missing boundsPx.{key}")
    if not (("w" in b or "width" in b) and ("h" in b or "height" in b)):
        fail(f"Slot {slot.get('slotId')} missing width/height bounds")
expected = {"R32":32, "R16":16, "QF":8, "SF":4, "FINAL_FOUR":1}
if counts != expected:
    fail(f"Unexpected round counts: {counts}; expected {expected}")

if "window.WC2026_UNIFORM_PICK_CARD_GAMEBOARD_MANIFEST" not in shim:
    fail("Manifest shim does not expose window.WC2026_UNIFORM_PICK_CARD_GAMEBOARD_MANIFEST")
if "uniform_pick_card_gameboard_manifest.js" not in html:
    fail("Game 1 does not load the uniform manifest JS shim")
for marker in [
    "UNIFORM_SVG_GAMEBOARD_MANIFEST",
    "validateUniformSvgGameboardManifestForGame1",
    "uniformSvgManifestProbe",
]:
    if marker not in html:
        fail(f"Game 1 missing manifest-read marker: {marker}")

# Game 1 may now show the uniform SVG board, but placement must still be deferred.
if "uniform_pick_card_gameboard.svg" in html:
    if "legacy-game1-r32-slot-rules" not in html:
        fail("Game 1 uniform SVG visual is present but placement mode is not explicitly deferred to legacy R32 slot rules")

# Game 2 is intentionally not migrated by this card.
game2_path = ROOT / "site/game2/index.html"
if game2_path.exists():
    game2 = game2_path.read_text(encoding="utf-8")
    if "uniform_pick_card_gameboard_manifest.js" in game2:
        fail("Game 2 should not load the uniform manifest in this Game 1-only probe")

print("WC2026 Game 1 uniform SVG manifest read checks passed.")
