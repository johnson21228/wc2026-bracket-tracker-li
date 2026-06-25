# Official R32 Hydration

## Feature definition
Bracketeering is a knockout-only game. The game begins after FIFA determines the official Round of 32 field.

`Admin_/official` owns the R32 field. Non-admin players cannot author R32 occupants. Non-admin player brackets may render those R32 occupants so every player starts from the same official field.

## Player action model
Player-owned picks begin with R32 match winners. Player choices then continue through R16, quarterfinals, semifinals, third-place/final as applicable, and champion selection.

The old group-stage prediction model is no longer player-owned game behavior.

## Hydration behavior
Hydration must copy `Admin_/official` R32 occupants into non-admin player BracketDocuments at creation, load, import, and save boundaries.

Hydration should make the official R32 field available to render and persist in the player's BracketDocument without giving the player authorship of those occupant values.

## Storage and backend fit
BracketDocument remains the persistence container.

The planned Supabase row-per-user-per-game model remains valid because each user can still have one persisted BracketDocument for the knockout-only game. The document contains hydrated official R32 occupants plus player-owned knockout winner picks.

## Scoring
Scoring compares player knockout winner picks to official result truth. R32 occupants are official seed data, not player-owned scoring inputs.

## CB boundary
This CB is LI-only and does not change runtime behavior. Runtime implementation and UI copy cleanup must be separate future CBs.

## Runtime implementation
The runtime/model boundary now hydrates official R32 occupants into non-admin BracketDocuments at creation, load, import, and save boundaries.

Runtime hydration treats `Admin_/official` as the R32 authority. Non-admin BracketDocuments may carry hydrated R32 entrant records with `source: "Admin_/official"`, `authority: "Admin_/official"`, and `playerAuthored: false`, but player action cannot author those entrant records.

Existing player knockout winner picks are preserved during hydration. Player-owned picks begin with R32 match winners and continue through later knockout rounds.

Runtime does not change player-facing copy. Runtime does not remove Game 1/Game 2 labels. UI copy cleanup remains a future CB after the model boundary is safe.

## Supabase Admin_/official source
Production official R32 hydration now reads the Supabase `Admin_/official` bracket row as the primary authority. The explicit runtime authority path is `SupabaseBracketStore.loadOfficialR32BracketAuthority`, which loads `user_id = "Admin_/official"`, `tournament_id = "wc2026"`, and `game_id = "game1"` from the existing row-per-user-per-game `user_brackets` table.

Static `site/data/official_round_of_32.json` is no longer the production authority. It remains a clearly named local/dev fallback only: `StaticJsonFallback:official_round_of_32`.

Hydrated non-admin R32 entrant records must retain `source: "Admin_/official"`, `authority: "Admin_/official"`, `playerAuthored: false`, and `hydratedFrom: "Supabase:Admin_/official"` when Supabase authority is available. Player actions still cannot author R32 entrants, and existing player-owned knockout winner picks are preserved.
