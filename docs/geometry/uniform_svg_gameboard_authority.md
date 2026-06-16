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
