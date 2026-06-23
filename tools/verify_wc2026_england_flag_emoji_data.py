#!/usr/bin/env python3
import json
from pathlib import Path

ENGLAND_FLAG = (
    "\U0001F3F4"
    "\U000E0067"
    "\U000E0062"
    "\U000E0065"
    "\U000E006E"
    "\U000E0067"
    "\U000E007F"
)

paths = [
    Path("site/data/current/group_matches.json"),
    Path("site/data/current/group_standings.json"),
    Path("site/data/current/fifa_r32.json"),
]

errors = []

def is_england_name(value):
    return isinstance(value, str) and value.strip().lower() == "england"

def check_node(node, path, trail="root"):
    if isinstance(node, dict):
        is_team_record = (
            node.get("teamId") == "ENG"
            or node.get("teamCode") == "ENG"
            or is_england_name(node.get("teamName"))
            or is_england_name(node.get("name"))
        )

        if is_team_record:
            if node.get("emoji") != ENGLAND_FLAG and node.get("flagEmoji") != ENGLAND_FLAG and node.get("teamEmoji") != ENGLAND_FLAG:
                errors.append(f"{path}:{trail} is an England team record without the full England flag emoji sequence")

        if node.get("homeTeamId") == "ENG" or is_england_name(node.get("homeTeamName")):
            if node.get("homeTeamEmoji") != ENGLAND_FLAG and node.get("homeFlagEmoji") != ENGLAND_FLAG:
                errors.append(f"{path}:{trail} has England as home team without the full England flag emoji sequence")

        if node.get("awayTeamId") == "ENG" or is_england_name(node.get("awayTeamName")):
            if node.get("awayTeamEmoji") != ENGLAND_FLAG and node.get("awayFlagEmoji") != ENGLAND_FLAG:
                errors.append(f"{path}:{trail} has England as away team without the full England flag emoji sequence")

        for key, value in node.items():
            check_node(value, path, f"{trail}.{key}")

    elif isinstance(node, list):
        for index, value in enumerate(node):
            check_node(value, path, f"{trail}[{index}]")

for path in paths:
    if path.exists():
        check_node(json.loads(path.read_text()), path)

if errors:
    print("England flag emoji verification failed:")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("OK: England/ENG emoji data uses the full England flag emoji tag sequence.")
