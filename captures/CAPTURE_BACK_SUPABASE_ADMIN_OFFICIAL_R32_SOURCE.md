# Capture Back — Supabase Admin_/official R32 Source

## Summary
Official R32 hydration is now sourced from the Supabase `Admin_/official` bracket row as the primary production authority.

## What changed
- Added an explicit `loadOfficialR32BracketAuthority` method to `SupabaseBracketStore`.
- Added `BracketRepository.loadOfficialR32Source`, which tries Supabase Admin_/official first and only then falls back to static JSON.
- Tagged Supabase-derived hydration as `Supabase:Admin_/official`.
- Renamed static authority usage as `StaticJsonFallback:official_round_of_32`.
- Kept R32 entrant authoring blocked for non-admin players.
- Preserved player-owned knockout winner picks during hydration.

## Boundaries preserved
- Runtime/model/store only.
- BracketDocument remains the persistence container.
- Supabase remains row-per-user-per-game.
- Local anonymous play remains supported.
- No player-facing copy cleanup.
- No Game 1/Game 2 label cleanup.

## Acceptance
The verifier fails if production hydration only reads static `site/data/official_round_of_32.json`. It passes only when the Supabase `Admin_/official` load path is present and BracketRepository prefers it before static fallback.
