# Capture Back: Lifecycle Stage Nomenclature

## Intent

Switch the player-facing and LI nomenclature away from “game modality” / “Game selector” and toward the contest lifecycle concept:

- `gameLifecycle.stage`
- `group_stage` / `knockout`
- player labels: `Group Stage` / `Knockout Stage`
- banner control label: `Stage selector`

## Product rule

The Bracketeering Pub contest is one gameboard surface whose lifecycle stage changes as the World Cup advances.

`gameLifecycle.stage` describes where the contest is in tournament time. It is not the same concept as a developer game view, a storage document, a Supabase user, or a bracket-pick source.

## Migration rule

The runtime may temporarily preserve legacy `game1` / `game2` hooks as compatibility identifiers while the player-facing language moves to lifecycle stage naming.

Compatibility mapping:

- legacy `game1` -> `gameLifecycle.stage = "group_stage"` -> `Group Stage`
- legacy `game2` -> `gameLifecycle.stage = "knockout"` -> `Knockout Stage`

## Boundaries

This CB must not change:

- pick data
- scoring rules
- BracketDocument persistence shape
- Supabase SQL/RLS
- WRITE/READ policy; WRITE is private, READ can be shared when game rules allow it

## Verification

`tools/verify_wc2026_lifecycle_stage_nomenclature.py` verifies the new stage naming, banner control wording, migration compatibility hooks, and LI rule.
