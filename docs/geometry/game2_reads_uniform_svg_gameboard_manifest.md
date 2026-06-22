# Game 2 Reads Uniform SVG Gameboard Manifest

This capture adds a read-only manifest probe to Game 2. The purpose is to establish that Game 2 can see and validate the same uniform SVG-derived geometry contract that Game 1 now uses.

## Read-only contract

Game 2 loads:

```text
site/data/geometry/uniform_pick_card_gameboard_manifest.js
```

The page validates the current board model:

```text
R32 = 32
R16 = 16
QF = 8
SF = 4
FINAL_FOUR = 1
Total = 61
```

## What does not change

This step intentionally does not switch Game 2 to the uniform SVG visual board. It does not move Game 2 cards, hit targets, or advancement destinations.

The next steps can be reviewed separately:

1. Switch Game 2 transparent SVG middle-layer board.
2. Map R32 seeded cards to manifest slots.
3. Map advancement destinations to R16/QF/SF/Final Four manifest slots.

<!-- WC2026_SINGLE_GEOMETRY_TRUTH_START -->
## Single Geometry Truth

WC2026 board geometry has one canonical truth.

The source-truth board geometry artifact is:

- `site/assets/playfield/uniform_pick_card_gameboard.svg`

The app-readable runtime projection is:

- `site/data/geometry/uniform_pick_card_gameboard_manifest.json`

The rendered/review derivative is:

- `site/assets/playfield/uniform_pick_card_gameboard.png`

Canonical rule:

- SVG/source geometry is the source-truth board geometry.
- JSON manifest is a generated/runtime projection of the SVG/source geometry.
- PNG is a rendered derivative for review, fallback, or visual inspection.
- Runtime code may read JSON for convenience, but JSON must not become an independent hand-maintained geometry truth.
- CSS may style rendered surfaces, but CSS must not define canonical slot bounds.
- View/controller/model code must not invent pick-cell geometry that is absent from the source-truth geometry.
- Geometry changes must update the source-truth SVG first, then regenerate or synchronize the JSON projection from that same source.

This prevents SVG, JSON, PNG, CSS, and runtime code from becoming competing geometry authorities.
<!-- WC2026_SINGLE_GEOMETRY_TRUTH_END -->
