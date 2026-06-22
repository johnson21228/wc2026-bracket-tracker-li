# Card 256: Single geometry truth LI

## Status

Done.

## Problem

WC2026 geometry LI could be read as allowing multiple geometry truths across SVG, JSON manifest, PNG, CSS, and runtime code.

## Decision

Make the authority chain explicit:

- `uniform_pick_card_gameboard.svg` is source-truth geometry.
- `uniform_pick_card_gameboard_manifest.json` is generated/runtime projection.
- `uniform_pick_card_gameboard.png` is rendered derivative.

## Final Four note

The current single tall `FINAL_FOUR` card is legacy/current behavior. Future upper/lower semifinal-winner and final-winner cells must be added to source-truth geometry first, then synchronized into the generated manifest.

## Acceptance

- One geometry truth is named.
- JSON is not an independent hand-maintained truth.
- PNG is not truth.
- CSS and runtime code cannot define canonical slot bounds.
- No gameplay behavior changes.
