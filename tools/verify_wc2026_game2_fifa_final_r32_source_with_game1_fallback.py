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

old_path = ROOT / "site/data/game2_seeded_r32_assignments.json"
if old_path.exists():
    raise SystemExit("Old seeded Game 2 R32 file should no longer be canonical: site/data/game2_seeded_r32_assignments.json")

data_path = ROOT / "site/data/game2_fifa_final_r32_assignments.json"
if not data_path.exists():
    raise SystemExit("Missing site/data/game2_fifa_final_r32_assignments.json")

payload = json.loads(data_path.read_text())
meta = payload.get("meta") or {}
if meta.get("source") != "fifa_final_truth_target":
    raise SystemExit("Game 2 FIFA-final R32 source must identify source=fifa_final_truth_target")
if meta.get("truthLevel") != "not_populated_yet":
    raise SystemExit("Game 2 FIFA-final R32 source must start as truthLevel=not_populated_yet")
if meta.get("currentRuntimeFallback") != "game1_r32_picks":
    raise SystemExit("Game 2 FIFA-final R32 source must declare Game 1 R32 picks as current runtime fallback")
notes = " ".join(meta.get("notes") or [])
if "must not be treated as FIFA-final truth" not in notes:
    raise SystemExit("Metadata must state Game 1 fallback is not FIFA-final truth")
if payload.get("assignments") != []:
    raise SystemExit("FIFA-final R32 assignment source should start empty until populated")

model = text("site/js/mvc/model.js")
require("site/js/mvc/model.js", 'game2FifaFinalR32Assignments: "data/game2_fifa_final_r32_assignments.json"')
if "game2_seeded_r32_assignments.json" in model:
    raise SystemExit("Old seeded filename must not remain in model URL surface")
require("site/js/mvc/model.js", "function normalizeGame2FifaFinalR32AssignmentsPayload(payload, teamById)")
require("site/js/mvc/model.js", 'payload?.meta?.source !== "fifa_final_truth_target"')
require("site/js/mvc/model.js", "const game2FifaFinalR32AssignmentsBySlotId")
require("site/js/mvc/model.js", "function fifaFinalR32Team(slotId)")
require("site/js/mvc/model.js", "function game1R32FallbackTeam(slotId)")
require("site/js/mvc/model.js", "function resolvedGame2R32Team(slotId)")
require("site/js/mvc/model.js", "function resolvedGame2FeederTeam(slotId)")
require("site/js/mvc/model.js", 'game2R32Source: "fifa_final_assignment"')
require("site/js/mvc/model.js", 'game2R32Source: "game1_r32_fallback"')
if "assignment_store" in model or "development_seed" in model or "test_seed_not_fifa_final" in model:
    raise SystemExit("Model should no longer use seeded/dev assignment-store source language for canonical Game 2 R32")

resolved = model[model.index("function resolvedGame2R32Team"):model.index("function resolvedGame2FeederTeam")]
if resolved.index("const fifaFinal = fifaFinalR32Team(slotId)") > resolved.index("const fallback = game1R32FallbackTeam(slotId)"):
    raise SystemExit("Populated FIFA-final assignment must be preferred before Game 1 fallback")
if 'game2R32Source: "game1_r32_fallback"' not in resolved:
    raise SystemExit("Game 1 fallback must be explicitly marked game1_r32_fallback")
if 'game2R32Source: "fifa_final_assignment"' not in resolved:
    raise SystemExit("FIFA-final assignment must be explicitly marked fifa_final_assignment")

require("site/js/mvc/model.js", "const feederTeams = feeders.map((feederId) => teamForFeederPath(feederId));")
require("site/js/mvc/view.js", "function displayTeamForSlot(slot)")
require("site/js/mvc/view.js", "slot.game2ResolvedTeam")
require("site/js/mvc/view.js", "data-game2-resolved-r32-source")
require("site/js/mvc/view.js", "button.disabled = !slot.pickable || !enabledForActiveGame")
require("site/js/mvc/controller.js", "Game 2 starts after the Round of 32 field.")
require("site/js/mvc/controller.js", "!slotAllowedForActiveGame(slot)")
require("Makefile", "python3 tools/verify_wc2026_game2_fifa_final_r32_source_with_game1_fallback.py")

for path in ["site/js/identity/SupabaseIdentitySurface.js", "site/js/config/supabase.public.js"]:
    if not (ROOT / path).exists():
        continue
print("OK: Game 2 R32 source is renamed to FIFA-final truth target and currently falls back to Game 1 R32 picks.")
