# Game 2 Bracket Item Slot Fit

Game 2 has reached the point where seeded R32 teams can be shown, but the next step is to make them true bracket items that occupy the image-defined bracket geometry.

The shared middle-layer PNG currently defines the board geometry. The correct implementation path is to capture that image geometry into slot data and then render bracket items into those slots.

## Why this matters
If teams are placed visually near the R32 lanes, the UI may look close, but the game has no durable logic. Future rounds cannot reliably know where winners should advance.

If teams are placed into named bracket slots, the same model supports:

- R32 seeding
- R16 advancement
- QF/SF/Final placement
- storage by slot and item
- future generated geometry from data

## Required shape

```text
shared middle-layer PNG
  ↓
captured bracket slot geometry
  ↓
seeded bracket items
  ↓
player pick state
  ↓
advancement into future slots
```

## First-order card
See `cards/056_fit_game2_bracket_items_to_image_defined_slots_card.md`.
