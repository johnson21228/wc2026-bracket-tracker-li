# WC2026 Single Geometry Truth Rule

WC2026 board geometry has one truth.

## Source-truth geometry

`site/assets/playfield/uniform_pick_card_gameboard.svg` is the source-truth board geometry artifact.

It defines the canonical board geometry that future pick-cell and linework changes must originate from.

## Generated/runtime projection

`site/data/geometry/uniform_pick_card_gameboard_manifest.json` is an app-readable generated projection of the source-truth SVG/source geometry.

Runtime code may read this manifest for convenience. The manifest must not become an independent hand-maintained geometry truth.

## Rendered derivative

`site/assets/playfield/uniform_pick_card_gameboard.png` is a rendered visual derivative for review, fallback, and visual inspection.

It is not geometry truth.

## Prohibited drift

The repo must not allow competing geometry authorities:

- SVG truth versus hand-maintained JSON truth
- CSS-defined canonical slot bounds
- runtime-invented pick-cell bounds
- PNG-derived canonical geometry
- permanent gameplay geometry that exists only in View code

## Final Four correction path

The current single tall `FINAL_FOUR` center card is legacy/current behavior, not permanent geometry truth.

The target direction is explicit center-stack geometry:

- upper semifinal-winner cell
- shorter final-winner / champion cell
- lower semifinal-winner cell
- third-place winner cell when required

Those cells must be introduced in source-truth geometry first, then synchronized into the generated/runtime manifest.
