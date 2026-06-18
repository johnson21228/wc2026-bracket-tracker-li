#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def require(condition, message):
    if not condition:
        print(f"WC2026 FIFA R32 bridge verification failed: {message}", file=sys.stderr)
        raise SystemExit(1)

def read_json(rel):
    path = ROOT / rel
    require(path.exists(), f"missing JSON file: {rel}")
    return json.loads(path.read_text(encoding="utf-8"))

def bounds_for(slot):
    return slot.get("boundsPx") or slot.get("bounds") or slot.get("box")

def main():
    required_files = [
        "source/images/game1_fifa_to_board_mapping_reference_20260617.png",
        "source/text/fifa_r32_slot_extraction_20260617.md",
        "source/text/fifa_r32_slot_extraction_20260617.json",
        "site/data/model/fifa_r32_logical_slot_order.json",
        "site/data/geometry/game1_fifa_slot_geometry_map.json",
        "site/data/geometry/gameboard_manifest.json",
        "site/js/board/FifaSlotMapLayer.js",
        "site/js/board/BoardShell.js",
        "site/js/dev/DeveloperFrame.js",
        "site/css/board.css",
        "docs/geometry/game1_fifa_r32_extraction_logic_geometry_render_bridge.md",
        "li/world_cup/fifa_r32_extraction_logic_geometry_bridge_rule.md",
    ]
    for rel in required_files:
        require((ROOT / rel).exists(), f"missing required file: {rel}")

    logic = read_json("site/data/model/fifa_r32_logical_slot_order.json")
    bridge = read_json("site/data/geometry/game1_fifa_slot_geometry_map.json")
    geometry = read_json("site/data/geometry/gameboard_manifest.json")
    extraction = read_json("source/text/fifa_r32_slot_extraction_20260617.json")

    logic_slots = logic.get("slots", [])
    bridge_slots = bridge.get("slots", [])
    extraction_slots = extraction.get("slots", [])
    geometry_slots = geometry.get("slots", [])

    require(len(logic_slots) == 32, f"expected 32 logical R32 slots, found {len(logic_slots)}")
    require(len(bridge_slots) == 32, f"expected 32 bridge R32 slots, found {len(bridge_slots)}")
    require(len(extraction_slots) == 32, f"expected 32 extraction R32 slots, found {len(extraction_slots)}")

    logic_ids = [slot.get("fifaSlotId") for slot in logic_slots]
    bridge_ids = [slot.get("fifaSlotId") for slot in bridge_slots]
    extraction_ids = [slot.get("fifaSlotId") for slot in extraction_slots]

    require(len(set(logic_ids)) == 32, "logical FIFA slot IDs must be unique")
    require(logic_ids == bridge_ids, "bridge FIFA slot order must match logical slot order")
    require(logic_ids == extraction_ids, "extraction FIFA slot order must match logical slot order")

    labels = [slot.get("fifaLabel") for slot in logic_slots]
    require(labels[0] == "1E", "first logical slot should be 1E")
    require(labels[-1] == "3 DEIJL", "last logical slot should be 3 DEIJL")
    require("3 ABCDF" in labels, "missing third-place slot 3 ABCDF")
    require("3 CEFHI" in labels, "missing third-place slot 3 CEFHI")

    geometry_by_id = {slot.get("slotId"): slot for slot in geometry_slots}
    missing_geometry = [
        slot.get("geometrySlotId")
        for slot in bridge_slots
        if slot.get("geometrySlotId") not in geometry_by_id
    ]
    require(not missing_geometry, f"bridge references missing geometry slots: {missing_geometry}")

    no_bounds = [
        slot.get("geometrySlotId")
        for slot in bridge_slots
        if not bounds_for(geometry_by_id[slot.get("geometrySlotId")])
    ]
    require(not no_bounds, f"bridge references geometry slots without bounds: {no_bounds}")

    board_shell_text = (ROOT / "site/js/board/BoardShell.js").read_text(encoding="utf-8")
    dev_frame_text = (ROOT / "site/js/dev/DeveloperFrame.js").read_text(encoding="utf-8")
    board_css_text = (ROOT / "site/css/board.css").read_text(encoding="utf-8")
    layer_text = (ROOT / "site/js/board/FifaSlotMapLayer.js").read_text(encoding="utf-8")

    require("createFifaSlotMapLayer" in board_shell_text, "BoardShell must render FIFA slot map layer")
    require("showFifaSlotMap" in board_shell_text, "BoardShell must default showFifaSlotMap dataset")
    require("Show FIFA slot map" in dev_frame_text, "DeveloperFrame must expose FIFA slot map toggle")
    require("showFifaSlotMap" in dev_frame_text, "DeveloperFrame must mutate showFifaSlotMap dataset")
    require("board-fifa-slot-map-layer" in board_css_text, "board.css must style FIFA slot map layer")
    require("[data-show-fifa-slot-map=\"false\"]" in board_css_text, "board.css must hide FIFA slot map by default")
    require("fifa-slot-map-label" in layer_text, "FifaSlotMapLayer must render label elements")

    print("WC2026 FIFA R32 bridge verification passed.")

if __name__ == "__main__":
    main()
