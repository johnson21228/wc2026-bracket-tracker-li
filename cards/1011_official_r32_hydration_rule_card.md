# Card 1011: Official R32 Hydration Rule

## Goal
Define the official R32 hydration LI for the simplified knockout-only Bracketeering game before runtime implementation.

## Files
- `li/world_cup/knockout_only_game_model.md`
- `li/world_cup/official_r32_hydration_rule.md`
- `docs/features/official_r32_hydration.md`
- `captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RULE.md`
- `tools/verify_wc2026_official_r32_hydration_li.py`
- `Makefile`

## Acceptance
- Bracketeering is defined as a knockout-only game.
- `Admin_/official` owns the R32 field.
- Non-admin players cannot author R32 occupants.
- Non-admin player brackets may render official R32 occupants.
- Player-owned picks begin with R32 match winners.
- Hydration applies at creation, load, import, and save boundaries.
- BracketDocument remains the persistence container.
- Supabase row-per-user-per-game remains valid.
- Scoring compares knockout winner picks to official result truth.
- The old group-stage prediction model is no longer player-owned game behavior.
- This CB is LI-only and does not change runtime behavior.
