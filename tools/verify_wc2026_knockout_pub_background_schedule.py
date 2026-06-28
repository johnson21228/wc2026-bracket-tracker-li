#!/usr/bin/env python3
import json
from pathlib import Path

schedule_path = Path("site/data/current/knockout_pub_background_schedule.json")
truth_path = Path("site/data/current/official_truth.json")

schedule = json.loads(schedule_path.read_text())
truth = json.loads(truth_path.read_text())
truth_picks = truth.get("picksBySlot", {})

expected_slot_by_match = {
    73: ("L-R32-01", "L-R32-02"),
    74: ("L-R32-03", "L-R32-04"),
    75: ("L-R32-05", "L-R32-06"),
    76: ("L-R32-07", "L-R32-08"),
    77: ("L-R32-09", "L-R32-10"),
    78: ("L-R32-11", "L-R32-12"),
    79: ("L-R32-13", "L-R32-14"),
    80: ("L-R32-15", "L-R32-16"),
    81: ("R-R32-01", "R-R32-02"),
    82: ("R-R32-03", "R-R32-04"),
    83: ("R-R32-05", "R-R32-06"),
    84: ("R-R32-07", "R-R32-08"),
    85: ("R-R32-09", "R-R32-10"),
    86: ("R-R32-11", "R-R32-12"),
    87: ("R-R32-13", "R-R32-14"),
    88: ("R-R32-15", "R-R32-16"),
}

errors = []

if schedule.get("runtimeUse") is not False:
    errors.append("schedule must be marked runtimeUse=false")

matches = schedule.get("matches", [])
if len(matches) != 32:
    errors.append(f"expected 32 knockout matches, found {len(matches)}")

by_id = {int(m.get("match_id")): m for m in matches if m.get("match_id") is not None}

for match_id, (home_slot, away_slot) in expected_slot_by_match.items():
    match = by_id.get(match_id)
    if not match:
        errors.append(f"missing match {match_id}")
        continue

    for side, slot_id in [("home_team", home_slot), ("away_team", away_slot)]:
        truth_record = truth_picks.get(slot_id, {})
        truth_pick = truth_record.get("pick", {})
        truth_code = truth_pick.get("teamCode") or truth_record.get("teamCode") or truth_pick.get("teamId") or truth_record.get("teamId")
        truth_name = truth_pick.get("teamName") or truth_record.get("teamName")

        image_team = match.get(side, {})
        image_code = image_team.get("code")
        image_name = image_team.get("name")

        # Only enforce slots that are currently resolved in official_truth.
        if truth_code and truth_name:
            if image_code != truth_code:
                errors.append(f"match {match_id} {side} code expected {truth_code} from {slot_id}, found {image_code}")
            if image_name != truth_name:
                errors.append(f"match {match_id} {side} name expected {truth_name} from {slot_id}, found {image_name}")

if by_id.get(79, {}).get("image_label") != "USA vs BIH":
    errors.append("match 79 image_label must be USA vs BIH")

if errors:
    print("WC2026 knockout pub background schedule verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: knockout pub background schedule is non-runtime and agrees with resolved current official truth.")
