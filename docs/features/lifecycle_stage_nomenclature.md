# Lifecycle Stage Nomenclature

The Bracketeering Pub gameboard should use lifecycle-stage naming instead of game-modality naming.

## Canonical property

```text
gameLifecycle.stage
```

## Enum values

```text
group_stage
knockout
```

## Player-facing labels

```text
group_stage -> Group Stage
knockout    -> Knockout Stage
```

## Why

The player is not switching between unrelated games. The player is viewing the same Bracketeering Pub gameboard at different World Cup lifecycle stages.

The banner control should therefore read like a stage selector, not a game selector.

## Compatibility

Existing runtime hooks may still use legacy game identifiers while the migration is underway:

```text
game1 -> group_stage
game2 -> knockout
```

Those identifiers are compatibility plumbing, not the player-facing model.
