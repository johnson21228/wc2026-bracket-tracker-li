# Rule: Lifecycle stage is the canonical game phase nomenclature

The canonical Bracketeering Pub phase property is:

```text
gameLifecycle.stage
```

Allowed values:

```text
group_stage
knockout
```

Player-facing labels:

```text
Group Stage
Knockout Stage
```

## Rule

Do not describe the banner stage control as a game-modality selector. Do not make “Game selector” the player-facing concept for this control.

The stage selector chooses the Bracketeering Pub lifecycle stage of the gameboard.

## Compatibility

Legacy game1/game2 runtime hooks may remain temporarily to avoid a broad behavioral rewrite:

```text
legacy game1/game2 -> gameLifecycle.stage bridge
```

They should be treated as compatibility identifiers, not the product language.

## Boundary

The nomenclature change must not alter scoring, picks, storage, Supabase, or BracketDocument behavior.

WRITE is private. READ can be shared when game rules allow it.
