# Card 1012: Official R32 Hydration Runtime Boundary

## Goal
Implement the LI-defined runtime/model boundary for official R32 hydration without UI copy cleanup.

## Files
- `site/js/model/UserBracketModel.js`
- `site/js/services/StaticJsonModelSource.js`
- `site/js/services/BracketRepository.js`
- `site/js/mvc/model.js`
- `docs/features/official_r32_hydration.md`
- `captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RUNTIME.md`
- `tools/verify_wc2026_official_r32_hydration_runtime.py`
- `Makefile`

## Acceptance
- Admin_/official is the authority for R32 occupants.
- Non-admin BracketDocuments may contain hydrated R32 occupants, but those records are marked official and non-player-authored.
- Non-admin players cannot author R32 occupants through the canonical model setter.
- Hydration happens at creation, load, import, and save boundaries.
- Existing player knockout winner picks are preserved.
- BracketDocument remains the persistence container.
- Supabase row-per-user-per-game remains valid.
- Runtime does not change player-facing copy.
- Runtime does not remove old Game 1/Game 2 labels.
