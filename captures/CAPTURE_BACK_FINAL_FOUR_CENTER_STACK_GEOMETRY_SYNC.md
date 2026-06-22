# Capture Back: Final Four Center-Stack Geometry Sync

## Intent

Synchronize derived geometry projections after updating the source-truth SVG Final Four center grouping.

## Source truth

`site/assets/playfield/uniform_pick_card_gameboard.svg`

## Runtime projection

The manifest now exposes explicit center-stack geometry slots:

- `FINAL-LEFT`
- `CHAMPION`
- `FINAL-RIGHT`

`CHAMPION` is twice the width and twice the height of the semifinal-winner cells.

## Model mapping

Canonical pick slots now point to matching geometry slot IDs for `FINAL-LEFT`, `CHAMPION`, and `FINAL-RIGHT`.

## Non-goals

No pick availability, pick menu, scoring, storage, Supabase, group data, or lifecycle-stage behavior changed.
