#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def text(path):
    return (ROOT / path).read_text()

def require(path, token):
    body = text(path)
    if token not in body:
        raise SystemExit(f"Missing {token!r} in {path}")

seed_path = ROOT / "site/data/game2_seeded_r32_assignments.json"
if not seed_path.exists():
    raise SystemExit("Missing site/data/game2_seeded_r32_assignments.json")

seed = json.loads(seed_path.read_text())
meta = seed.get("meta") or {}
if meta.get("source") != "development_seed":
    raise SystemExit("Seeded R32 store must identify source as development_seed")
if meta.get("truthLevel") != "test_seed_not_fifa_final":
    raise SystemExit("Seeded R32 store must mark itself test_seed_not_fifa_final")
if meta.get("replaceableByOfficialFifaAssignments") is not True:
    raise SystemExit("Seeded R32 store must be replaceable by official FIFA assignments")
if "not FIFA-final truth" not in meta.get("warning", ""):
    raise SystemExit("Seeded R32 store warning must say it is not FIFA-final truth")

assignments = seed.get("assignments") or []
if len(assignments) != 32:
    raise SystemExit(f"Expected 32 deterministic R32 seed assignments, found {len(assignments)}")

slot_ids = [entry.get("slotId") for entry in assignments]
team_ids = [entry.get("teamId") for entry in assignments]
if len(set(slot_ids)) != 32:
    raise SystemExit("Seeded R32 slot IDs must be unique")
if len(set(team_ids)) != 32:
    raise SystemExit("Seeded R32 team IDs must be unique")
for entry in assignments:
    slot_id = entry.get("slotId", "")
    if not (slot_id.startswith("L-R32-") or slot_id.startswith("R-R32-")):
        raise SystemExit(f"Seed assignment must target an active R32 slot, got {slot_id!r}")
    if entry.get("seedSource") != "development_seed":
        raise SystemExit(f"Seed assignment {slot_id} must mark seedSource as development_seed")
    for key in ["teamId", "label", "abbr"]:
        if not entry.get(key):
            raise SystemExit(f"Seed assignment {slot_id} missing {key}")

model = text("site/js/mvc/model.js")
require("site/js/mvc/model.js", 'game2SeededR32Assignments: "data/game2_seeded_r32_assignments.json"')
require("site/js/mvc/model.js", "function normalizeSeededR32AssignmentPayload(seedPayload, teamById)")
require("site/js/mvc/model.js", "const game2SeededR32AssignmentsBySlotId")
require("site/js/mvc/model.js", "function seededR32Team(slotId)")
require("site/js/mvc/model.js", "function teamForFeederPath(slotId)")
require("site/js/mvc/model.js", 'if (slot?.round === "R32") return seededR32Team(slotId);')
require("site/js/mvc/model.js", "const feederTeams = feeders.map((feederId) => teamForFeederPath(feederId));")

knockout_start = model.index("function getKnockoutChoices")
knockout_end = model.index("function getChoices")
knockout_segment = model[knockout_start:knockout_end]
if "getR32Choices" in knockout_segment:
    raise SystemExit("Game 2 knockout choices must not fallback to Game 1 R32 menus")
if "selectedTeam(feederId)" in knockout_segment:
    raise SystemExit("Game 2 knockout choices must use the seeded feeder seam, not selectedTeam-only feeder resolution")

r32_start = model.index("function getR32Choices")
r32_end = model.index("function getKnockoutChoices")
r32_segment = model[r32_start:r32_end]
if "development_seed" in r32_segment or "game2SeededR32" in r32_segment:
    raise SystemExit("Game 1 R32 choice logic must remain independent from seeded Game 2 store")

makefile = text("Makefile")
if "python3 tools/verify_wc2026_game2_seeded_r32_assignment_store.py" not in makefile:
    raise SystemExit("Makefile verify target must include seeded R32 assignment store verifier")

for forbidden_path in [
    "site/js/config/supabase.public.js",
    "site/js/services/SupabaseAuthService.js",
    "site/js/services/LocalStorageBracketStore.js",
    "site/data/current/group_standings.json",
    "site/data/current/group_matches.json",
    "site/data/current/match_highlights.json",
]:
    if not (ROOT / forbidden_path).exists():
        continue
    # Existence check only: this verifier intentionally requires no backend/storage/current-data edits.

print("OK: Game 2 seeded R32 assignment store is development-only and wired through an explicit model feeder seam.")
