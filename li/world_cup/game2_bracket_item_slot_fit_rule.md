# Game 2 Bracket Item Slot Fit Rule

Game 2 bracket items must be subordinate to bracket slot geometry.

## Current source posture
At the current development stage, the shared middle-layer gameboard PNG defines the visible bracket geometry for both Game 1 and Game 2.

Therefore, Game 2 must not place seeded teams as a loose list or approximate visual lane. It must capture the image-defined bracket boxes as explicit slot geometry and render bracket items into those slots.

## Terms

### Bracket slot
A bracket slot is a geometric location on the board. It answers: where does an item live?

Required fields should include:

- `slotId`
- `round`
- `x`
- `y`
- `w`
- `h`
- optional `feedsTo`
- optional `side`

### Bracket item
A bracket item is the movable game object occupying a slot. It answers: what team/pick currently lives there?

Required fields should include:

- `itemId`
- `slotId`
- `round`
- `team`
- `source`
- optional `status`

### Pick state
Pick state records the player's evolving choices. It must reference bracket items or slots rather than re-deriving visual positions.

## Required behavior
When Game 2 seeds the R32 board:

1. Read or embed R32 seed data.
2. Read or embed captured bracket slot geometry.
3. Create one bracket item per seeded R32 team.
4. Assign each bracket item to a slot.
5. Render each bracket item inside that slot's x/y/w/h bounds.
6. Store seeded board state by `slotId` and `itemId`.

## Migration path
Current stage:

```text
middle-layer PNG -> captured slot geometry -> bracket item rendering
```

Future stage:

```text
truth geometry data -> generated PNG/SVG -> bracket item rendering
```

The future truth geometry model should preserve the same slot IDs so Game 2 storage and advancement logic can survive the transition.

## Non-goals
This rule does not require full knockout advancement yet. It establishes the slot/item contract required before advancement can be reliable.
