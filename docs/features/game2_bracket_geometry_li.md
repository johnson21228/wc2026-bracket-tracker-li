# Game 2 Bracket Geometry LI

The current Game 2 bracket geometry is image-defined. The transparent geometry PNG defines the visual board. The next step is to capture its slots as data, so seeded teams and later winner picks are placed into the board rather than rendered as a separate list.

## Current stage

```text
transparent bracket geometry PNG
  ↓ implies
slot positions and connector topology
  ↓ captured as
bracket geometry slot JSON
  ↓ consumed by
Game 2 bracket-item runtime
```

## Mature stage

```text
bracket geometry slot JSON
  ↓ generates
SVG/PNG geometry layer
  ↓ also drives
runtime item placement and advancement logic
```

## Why this matters

If the image and runtime geometry are not governed by the same notion, Game 2 can regress into separate visual and logical systems: one thing is drawn, another thing is clickable, and a third thing is stored. The WB should prevent that by naming the geometry contract now.

## Minimum next implementation

Add `site/data/game2_bracket_geometry_slots.json` with percent-based slots aligned to the current board image. Then render seeded R32 bracket items into those slots.
