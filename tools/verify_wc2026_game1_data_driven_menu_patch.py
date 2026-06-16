#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(msg: str) -> None:
    print(f"WC2026 Game 1 data-driven menu verification failed: {msg}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"could not load {path}: {exc}")


def main() -> None:
    game1_html = ROOT / "site" / "game1" / "index.html"
    bundle_path = ROOT / "site" / "data" / "game1_data_bundle.js"
    slot_rules_path = ROOT / "site" / "data" / "game1_r32_slot_menu_rules.json"
    teams_path = ROOT / "site" / "data" / "teams_from_flags_images.json"
    groups_path = ROOT / "site" / "data" / "groups_from_flags_images.json"

    for path in [game1_html, bundle_path, slot_rules_path, teams_path, groups_path]:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    html = game1_html.read_text(encoding="utf-8")
    if '<script src="../data/game1_data_bundle.js"></script>' not in html:
        fail("site/game1/index.html must load ../data/game1_data_bundle.js before the runtime script")
    if re.search(r"const\s+SLOT_RULES\s*=\s*\[", html):
        fail("site/game1/index.html still embeds a SLOT_RULES array literal")
    if re.search(r"const\s+GROUPS\s*=\s*\{\s*\"A\"\s*:", html):
        fail("site/game1/index.html still embeds the GROUPS data literal")
    if "window.WC2026_GAME1_DATA" not in html:
        fail("site/game1/index.html must bind runtime data from window.WC2026_GAME1_DATA")

    bundle = bundle_path.read_text(encoding="utf-8")
    if "window.WC2026_GAME1_DATA" not in bundle:
        fail("site/data/game1_data_bundle.js must expose window.WC2026_GAME1_DATA")
    if "game1_r32_slot_menu_rules.json" not in bundle:
        fail("bundle should declare its source JSON files")

    slots_doc = load_json(slot_rules_path)
    teams_doc = load_json(teams_path)
    groups_doc = load_json(groups_path)

    slots = slots_doc.get("slots")
    teams = teams_doc.get("teams")
    groups = groups_doc.get("groups")
    if not isinstance(slots, list) or len(slots) != 32:
        fail("site/data/game1_r32_slot_menu_rules.json must contain 32 slots")
    if not isinstance(teams, list) or len(teams) != 48:
        fail("site/data/teams_from_flags_images.json must contain 48 teams")
    if not isinstance(groups, dict) or len(groups) != 12:
        fail("site/data/groups_from_flags_images.json must contain 12 groups")

    group_ids = set(groups.keys())
    for group_id in "ABCDEFGHIJKL":
        if group_id not in group_ids:
            fail(f"missing group {group_id}")

    slot_ids = set()
    logical_ids = set()
    for slot in slots:
        slot_id = slot.get("slotId")
        logical_id = slot.get("logicalId")
        eligible = slot.get("eligibleGroups")
        if not slot_id or slot_id in slot_ids:
            fail(f"missing or duplicate slotId: {slot_id}")
        if not logical_id or logical_id in logical_ids:
            fail(f"missing or duplicate logicalId: {logical_id}")
        if not isinstance(eligible, list) or not eligible:
            fail(f"slot {slot_id} must declare eligibleGroups")
        unknown = sorted(set(eligible) - group_ids)
        if unknown:
            fail(f"slot {slot_id} references unknown eligible groups: {unknown}")
        slot_ids.add(slot_id)
        logical_ids.add(logical_id)

    teams_by_group = {group_id: 0 for group_id in group_ids}
    for team in teams:
        group_id = team.get("group")
        if group_id not in teams_by_group:
            fail(f"team {team.get('name')} has unknown group {group_id}")
        teams_by_group[group_id] += 1
        if not (team.get("flagEmoji") or team.get("flag")):
            fail(f"team {team.get('name')} is missing a flag")
    for group_id, count in teams_by_group.items():
        if count != 4:
            fail(f"group {group_id} must have 4 teams; found {count}")

    print("WC2026 Game 1 data-driven menu verification passed.")


if __name__ == "__main__":
    main()
