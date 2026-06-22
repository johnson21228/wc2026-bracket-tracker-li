#!/usr/bin/env python3
from pathlib import Path
import json

SCOTLAND_FLAG = '🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f'

ROOT = Path(__file__).resolve().parents[1]
errors = []

json_targets = [
    ROOT / "site/data/teams_from_flags_images.json",
    ROOT / "site/data/groups_from_flags_images.json",
    ROOT / "site/data/model/teams.json",
    ROOT / "site/data/teams.json",
    ROOT / "data/teams_from_flags_images.json",
    ROOT / "data/groups_from_flags_images.json",
    ROOT / "data/teams.json",
]

found = 0

def walk(obj, path):
    global found
    if isinstance(obj, dict):
        values = {str(v).strip().lower() for v in obj.values() if isinstance(v, str)}
        is_scotland = (
            "sco" in values
            or "scotland" in values
            or obj.get("id") == "SCO"
            or obj.get("abbr") == "SCO"
            or obj.get("code") == "SCO"
            or obj.get("teamId") == "SCO"
            or obj.get("name") == "Scotland"
        )
        if is_scotland:
            found += 1
            flag_values = [obj.get(key) for key in ["flag", "emoji", "flagEmoji"] if key in obj]
            if not flag_values:
                errors.append(f"{path}: Scotland row has no flag/emoji field")
            elif SCOTLAND_FLAG not in flag_values:
                errors.append(f"{path}: Scotland flag/emoji is not the full Scotland emoji tag sequence")
        for key, value in obj.items():
            walk(value, f"{path}.{key}")
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            walk(value, f"{path}[{index}]")

for target in json_targets:
    if not target.exists():
        continue
    walk(json.loads(target.read_text()), str(target.relative_to(ROOT)))

bundle = ROOT / "site/data/game1_data_bundle.js"
if bundle.exists():
    text = bundle.read_text()
    if "Scotland" in text and SCOTLAND_FLAG not in text:
        errors.append("site/data/game1_data_bundle.js: Scotland appears without full Scotland emoji tag sequence")

if found == 0:
    errors.append("No Scotland/SCO rows found in checked JSON data")

if errors:
    print("WC2026 Scotland flag emoji data verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Scotland/SCO emoji data uses the full Scotland flag emoji tag sequence.")
