#!/usr/bin/env python3
"""Verify LI/docs align with Admin R32 hydration compatibility model."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def require(condition, message):
    if not condition:
        errors.append(message)

makefile = read("Makefile")
require("verify_wc2026_admin_r32_hydration_compatibility_model_li.py" in makefile, "Makefile must run the Admin R32 compatibility LI verifier.")

compat = read("li/world_cup/admin_r32_hydration_compatibility_model_rule.md")
for token in [
    "Admin_/official owns R32 occupant truth",
    "Player BracketDocuments may contain R32 entrant records only as Supabase Admin_/official hydrated mirror entries",
    "playerAuthored: false",
    "copied ONLY from the Supabase Admin_/official official bracket document",
    "must never be copied into normal player BracketDocuments",
    "Existing player R16++ picks must survive R32 hydration",
]:
    require(token in compat, f"Compatibility LI must contain: {token}")

# Known stale source files must now be updated or explicitly superseded.
app_modules = read("li/world_cup/app_module_boundaries_rule.md")
require("let a player assign one eligible team to each Game 1 R32 slot" not in app_modules, "App module boundaries must not say normal players assign R32 occupants.")
require("let players pick R32/R16/QF/SF/final/champion winners" not in app_modules, "App module boundaries must distinguish R32 match winners from R32 occupants.")
require("let Admin_/official assign official team occupants" in app_modules, "App module boundaries must name Admin_/official as R32 occupant author.")
require("hydrate ONLY R32 entrant slots from Supabase Admin_/official" in app_modules, "App module boundaries must preserve hydration compatibility rule.")

r32_rendering = read("li/world_cup/r32_pick_card_rendering_rule.md")
require("player's predicted qualifier" not in r32_rendering, "R32 rendering rule must not describe normal-player predicted qualifiers.")
require("Admin_/official hydrated occupant" in r32_rendering, "R32 rendering rule must describe Admin_/official hydrated occupants.")
require("playerAuthored: false" in r32_rendering, "R32 rendering rule must state hydrated records are non-player-authored.")

unified = read("docs/features/unified_game1_game2_bracket_lifecycle.md")
require("superseded by the current knockout-only Admin_/official R32 authority model" in unified, "Unified lifecycle note must be explicitly superseded by current Admin R32 authority model.")
require("player predicted R32 slot occupant" not in unified, "Unified lifecycle note must not retain player-predicted R32 occupant data distinction.")
require("Admin_/official R32 slot occupant" in unified, "Unified lifecycle note must name Admin R32 occupant truth.")

controller = read("docs/features/game1_r32_pick_controller.md")
require("player to project every Round of 32 slot" not in controller, "R32 pick controller doc must not present old player projection as current behavior.")
require("Legacy note" in controller and "Admin_/official owns R32 occupant truth" in controller, "R32 pick controller doc must be marked legacy/superseded.")

force_doc = read("docs/features/force_player_r32_matches_admin_official.md")
require("strip/ignore all R32 occupant values" not in force_doc, "Force-player-R32 doc must not claim all player R32 values are simply ignored after compatibility hydration.")
require("copy ONLY Supabase Admin_/official R32 entrants into player `picksBySlot`" in force_doc, "Force-player-R32 doc must describe player picksBySlot materialization.")
require("R32 `setPick` calls remain rejected" in force_doc, "Force-player-R32 doc must keep normal player R32 edit rejection.")

lifecycle = read("li/world_cup/bracket_lifecycle_state_rule.md")
require("user-predicted R32 assignments" not in lifecycle, "Lifecycle rule must not preserve user-predicted R32 occupant assignments as current evidence.")
require("Supabase Admin_/official R32 occupant truth mirrored into player BracketDocuments" in lifecycle, "Lifecycle rule must describe mirrored Admin R32 evidence.")

card116 = read("cards/116_add_bracket_lifecycle_state_card.md")
require("user-predicted R32 assignment picks" not in card116, "Lifecycle card must not retain user-predicted R32 occupant assignment picks.")
require("Admin_/official R32 occupant truth mirrored into player BracketDocuments" in card116, "Lifecycle card must describe mirrored Admin R32 truth.")

# New docs/card/capture must exist and carry the narrow copy rule.
for rel in [
    "docs/features/admin_r32_hydration_compatibility_model.md",
    "captures/CAPTURE_BACK_ADMIN_R32_HYDRATION_COMPATIBILITY_MODEL.md",
    "cards/1020_admin_r32_hydration_compatibility_model_card.md",
]:
    text = read(rel)
    require("Admin_/official" in text, f"{rel} must name Admin_/official.")
    require("playerAuthored: false" in text, f"{rel} must state playerAuthored:false.")

# Runtime hydration doc must still protect the narrow copy boundary.
hydrate_rule = read("li/world_cup/hydrate_only_supabase_admin_r32_into_player_picks_rule.md")
require("Copy ONLY R32 entrant slots from Supabase Admin_/official" in hydrate_rule, "Hydration rule must keep only-R32 Supabase Admin copy boundary.")
require("Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place picks" in hydrate_rule, "Hydration rule must block Admin later-round copy.")

if errors:
    print("WC2026 Admin R32 hydration compatibility LI verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: LI/docs align with Admin R32 hydration compatibility model and no longer describe normal-player R32 occupant authoring as current behavior.")
