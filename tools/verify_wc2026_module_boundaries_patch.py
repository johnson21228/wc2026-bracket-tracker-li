#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import sys

ROOT = Path.cwd()


def fail(message: str) -> None:
    print(message)
    sys.exit(1)


def load_json(path: str):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        fail(f"Could not read JSON {path}: {exc}")


def main() -> int:
    teams = load_json("site/data/teams_from_flags_images.json").get("teams", [])
    if len(teams) != 48:
        fail(f"Expected 48 teams in site/data/teams_from_flags_images.json, found {len(teams)}")

    groups = load_json("site/data/groups_from_flags_images.json").get("groups", {})
    if len(groups) != 12:
        fail(f"Expected 12 groups in site/data/groups_from_flags_images.json, found {len(groups)}")
    bad_groups = {group: len(members) for group, members in groups.items() if len(members) != 4}
    if bad_groups:
        fail(f"Expected 4 teams per group; found {bad_groups}")

    slot_rules = load_json("site/data/game1_r32_slot_menu_rules.json").get("slots", [])
    if len(slot_rules) != 32:
        fail(f"Expected 32 Game 1 R32 slot menu rules, found {len(slot_rules)}")

    missing_bounds = [s.get("slotId") or s.get("logicalId") for s in slot_rules if not s.get("boundsPx") or not s.get("hitRegionPx")]
    if missing_bounds:
        fail(f"Game 1 slots missing pixel bounds/hit regions: {missing_bounds}")

    missing_qual = [s.get("slotId") or s.get("logicalId") for s in slot_rules if not s.get("qualifierKind") or not s.get("eligibleGroups")]
    if missing_qual:
        fail(f"Game 1 slots missing qualification/menu rules: {missing_qual}")

    third_place = [s for s in slot_rules if s.get("qualifierKind") == "third_place_pool"]
    if not third_place:
        fail("Expected explicit third-place pool slots in Game 1 R32 slot rules")
    weak_third = [s.get("slotId") or s.get("logicalId") for s in third_place if len(s.get("eligibleGroups", [])) < 2]
    if weak_third:
        fail(f"Third-place slots must list candidate group pools: {weak_third}")

    print("WC2026 module boundary data-shape checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
