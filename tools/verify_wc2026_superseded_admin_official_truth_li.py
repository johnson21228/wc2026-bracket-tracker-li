#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

superseded_files = [
    "li/world_cup/single_game_admin_official_runtime_rule.md",
    "li/world_cup/hydrate_only_supabase_admin_r32_into_player_picks_rule.md",
    "li/world_cup/admin_r32_hydration_compatibility_model_rule.md",
    "li/world_cup/admin_official_full_bracket_editor_mode_rule.md",
    "li/world_cup/admin_official_r32_editor_mode_rule.md",
    "li/world_cup/official_r32_hydration_rule.md",
    "docs/features/single_game_admin_official_runtime.md",
    "docs/features/hydrate_only_supabase_admin_r32_into_player_picks.md",
    "docs/features/admin_r32_hydration_compatibility_model.md",
    "docs/features/admin_official_full_bracket_editor_mode.md",
    "docs/features/admin_official_r32_editor_mode.md",
    "docs/features/official_r32_hydration.md",
    "docs/features/admin_official_results_truth.md",
    "docs/features/force_player_r32_matches_admin_official.md",
    "cards/1013_supabase_admin_official_r32_source_card.md",
    "cards/1014_admin_official_results_truth_card.md",
    "cards/1016_force_player_r32_matches_admin_official_card.md",
    "cards/1017_admin_official_r32_editor_mode_card.md",
    "cards/1018_admin_official_full_bracket_editor_mode_card.md",
    "cards/1020_admin_r32_hydration_compatibility_model_card.md",
]

for rel in superseded_files:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing superseded historical file: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    if "Superseded by site-owned official truth" not in text:
        errors.append(f"missing supersession marker: {rel}")
    if "The Supabase `Admin_/official` official bracket row is no longer an official truth source." not in text:
        errors.append(f"missing explicit Admin row removal marker: {rel}")

current_truth_files = [
    "li/world_cup/site_owned_official_truth_rule.md",
    "docs/features/site_owned_official_truth.md",
    "li/world_cup/player_standings_scoring_rule.md",
    "docs/features/player_standings_scoring.md",
    "li/world_cup/player_standings_max_possible_reachability_rule.md",
    "docs/features/player_standings_max_possible_reachability.md",
]

for rel in current_truth_files:
    text = (ROOT / rel).read_text(encoding="utf-8")
    if "`Admin_/official` result truth" in text or "`Admin_/official` truth" in text:
        errors.append(f"current scoring/reachability still names Admin_/official truth: {rel}")
    if "Admin_/official is the only source of scoring truth" in text:
        errors.append(f"current file still makes Admin_/official scoring authority: {rel}")

makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
if "python3 tools/verify_wc2026_superseded_admin_official_truth_li.py" not in makefile:
    errors.append("Makefile verify must include superseded Admin_/official LI verifier")

if errors:
    print("WC2026 superseded Admin_/official truth LI verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Supabase Admin_/official official-truth LI is superseded by site-owned official truth.")
