# Official R32 Hydration Rule

## Rule
`Admin_/official` owns the R32 field. Non-admin players cannot author R32 occupants.

Non-admin player brackets may render R32 occupants, but those occupants are official input copied from `Admin_/official`, not player-owned picks.

## Hydration boundary
Hydration must copy `Admin_/official` R32 occupants into non-admin player BracketDocuments at creation, load, import, and save boundaries.

Hydration is a model-boundary rule. It keeps every non-admin BracketDocument aligned to the same official FIFA R32 field while preserving player ownership of knockout winner choices.

## Persistence
BracketDocument remains the persistence container. The official R32 occupants may be present inside each non-admin BracketDocument after hydration, but their authority remains `Admin_/official`.

The planned Supabase row-per-user-per-game model remains valid. Each user's row can persist one BracketDocument for the game; the R32 occupant subfield is hydrated official data, and the player-owned pick subfield remains the user's knockout winner picks.

## Scoring
Scoring compares player knockout winner picks to official result truth. Scoring does not compare player-authored group-stage predictions or player-authored R32 occupants, because those are no longer player-owned game behavior.

## Implementation order
This CB is LI-only and does not change runtime behavior.

Future runtime CBs should implement this hydration rule at creation, load, import, and save boundaries. Future UI CBs should remove or rename Game 1/Game 2 and group-prediction language after the runtime model is safe.
