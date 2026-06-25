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
