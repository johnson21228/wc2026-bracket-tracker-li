#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
failures = []

def read(path):
    p = ROOT / path
    if not p.exists():
        failures.append(f"Missing {path}")
        return ""
    return p.read_text(encoding="utf-8")

def require(path, token):
    text = read(path)
    if token not in text:
        failures.append(f"{path} missing token: {token}")
    return text

model = read("site/js/mvc/model.js")
makefile = read("Makefile")

for path in [
    "li/world_cup/current_group_order_rendering_rule.md",
    "docs/features/current_group_order_rendering.md",
    "cards/203_render_group_teams_in_current_order_card.md",
    "capture_back/CAPTURE_BACK_CURRENT_GROUP_ORDER_RENDERING.md",
]:
    require(path, "current")

for token in [
    "function groupTeamsInCurrentOrder(groupId)",
    "const standings = getGroupStandings(normalizedGroupId);",
    "const entries = standings?.entries || [];",
    "entry.teamId || entry.id || entry.abbr",
    "return uniqueTeams(groups.flatMap((groupId) => groupTeamsInCurrentOrder(groupId)));",
    "const groupChoices = groupTeamsInCurrentOrder(groupId)",
    "const teams = groupTeamsInCurrentOrder(groupId).slice(0, 4).map",
]:
    if token not in model:
        failures.append(f"model.js missing current group order token: {token}")

if "python3 tools/verify_wc2026_current_group_order_rendering.py" not in makefile:
    failures.append("Makefile verify target must run current group order verifier")

standings_path = ROOT / "site/data/current/group_standings.json"
if standings_path.exists():
    standings = json.loads(standings_path.read_text(encoding="utf-8"))
    group_a = standings.get("groups", {}).get("A", {}).get("entries", [])
    observed = [entry.get("teamId") or entry.get("id") or entry.get("abbr") for entry in group_a]
    expected = ["MEX", "KOR", "CZE", "RSA"]
    if observed[:4] != expected:
        failures.append(f"Group A current order should be {expected}, found {observed[:4]}")
else:
    failures.append("Missing site/data/current/group_standings.json")

# Keep raw group order as model fallback only. These exact runtime display paths should be gone.
for forbidden in [
    "uniqueTeams(groups.flatMap((groupId) => groupsById.get(groupId) || []))",
    "const groupChoices = (groupsById.get(groupId) || [])",
    "const teams = (groupsById.get(groupId) || []).slice(0, 4).map",
]:
    if forbidden in model:
        failures.append(f"Raw group order remains in a current-display path: {forbidden}")

if failures:
    print("WC2026 current group order rendering verification failed:")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print("OK: WC2026 group displays use current standings order with stable fallback.")
