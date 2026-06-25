# Capture Back: Official R32 Hydration Rule

## Change
Defined the official R32 hydration LI for the simplified knockout-only Bracketeering game model.

## Intent
Make the model boundary explicit before runtime work:
- Bracketeering is now a knockout-only game.
- `Admin_/official` owns the R32 field.
- Non-admin players cannot author R32 occupants.
- Non-admin player brackets may render official R32 occupants.
- Player-owned picks begin with R32 match winners.
- Hydration must copy official R32 occupants at creation, load, import, and save boundaries.
- BracketDocument remains the persistence container.
- Supabase row-per-user-per-game remains valid.
- Scoring compares knockout winner picks to official result truth.
- The old group-stage prediction model is no longer player-owned game behavior.

## Boundary
This CB is LI-only and does not change runtime behavior. Future runtime CBs should implement the hydration rule, then future UI CBs should remove or rename Game 1/Game 2 and group-prediction language.

## Verification
- `python3 tools/verify_wc2026_official_r32_hydration_li.py`
- `make verify`
- `make pack`
