# Uniform SVG Gameboard Authority

This geometry family introduces a shared SVG gameboard for both World Cup bracket games.

## What is source truth?

The SVG is the source truth for geometry:

- `site/assets/playfield/uniform_pick_card_gameboard.svg`

The manifest is the runtime contract:

- `site/data/geometry/uniform_pick_card_gameboard_manifest.json`

The PNG is a rendered derivative:

- `site/assets/playfield/uniform_pick_card_gameboard.png`

The PNG exists for review and fallback. It is not the source of geometry.

## Current count

The current board model intentionally contains 61 visible pick-card rectangles:

| Round | Count |
| --- | ---: |
| R32 | 32 |
| R16 | 16 |
| QF | 8 |
| SF | 4 |
| FINAL_FOUR | 1 |

The center `FINAL_FOUR` pick card is a special object. It is a single tall center card, not two finalist cards plus a champion card.

## Layering preserved

The new SVG does not collapse the existing layered UI structure. It sits in the gameboard layer.

Background art remains below it. Hit targets, rendered pick cards, and UI overlays remain above it.

## Both games

Game 1 and Game 2 should eventually consume the same manifest for board slot geometry. Game-specific logic may interpret the same slot rectangles differently, but neither game should invent its own bracket geometry.

## Verification requirement

Verification must compare the manifest against the SVG, not against generic tournament math. The expected count is defined by this board model.

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
