# Card 253: Rename game modality to lifecycle stage

## Goal

Use lifecycle-stage language for the banner control and Bracketeering Pub game phase.

## Decision

The canonical concept is:

```text
gameLifecycle.stage
```

Allowed stage values:

```text
group_stage
knockout
```

Player labels:

```text
group_stage -> Group Stage
knockout    -> Knockout Stage
```

## Implementation scope

- Rename player-facing banner control language from game/modality language to stage language.
- Add lifecycle-stage data hooks beside any legacy game selector hooks.
- Preserve legacy `game1` / `game2` hooks during migration.
- Add LI and verification.

## Non-goals

- Do not change picks.
- Do not change scoring.
- Do not change Supabase.
- Do not change BracketDocument persistence.
- Do not remove compatibility with existing active-game runtime wiring in this card.

## Acceptance

- Banner control says Stage / Stage selector.
- Options are Group Stage and Knockout Stage.
- LI names `gameLifecycle.stage` as canonical.
- Verifier passes under `make verify`.
