# Capture Back: Single Geometry Truth LI

## Intent

Correct WC2026 geometry LI so the repo has one geometry truth.

## Canonical geometry authority

- SVG/source geometry is truth.
- JSON manifest is a generated/runtime projection.
- PNG is a rendered visual derivative.

## Source-truth artifact

`site/assets/playfield/uniform_pick_card_gameboard.svg`

## Runtime projection

`site/data/geometry/uniform_pick_card_gameboard_manifest.json`

## Rendered derivative

`site/assets/playfield/uniform_pick_card_gameboard.png`

## Final Four correction

The current single tall `FINAL_FOUR` center card is legacy/current behavior, not permanent geometry truth.

Future center-stack cells must originate in the source-truth geometry before appearing in the generated/runtime manifest.

## Gameplay invariants

This LI update does not change:

- pick availability
- pick menus
- R16/R32/QF/SF/final pickability
- lifecycle-stage presentation-only behavior
- storage
- scoring
- Supabase readiness
- localStorage behavior
