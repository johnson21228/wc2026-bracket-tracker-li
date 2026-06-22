# Card 257: Sync Final Four center-stack geometry

## Status

Done.

## Decision

Synchronize generated/runtime manifest projections from the updated source-truth SVG.

## Result

- `FINAL-LEFT` is explicit source-derived geometry.
- `CHAMPION` is explicit source-derived geometry and is twice as wide/tall.
- `FINAL-RIGHT` is explicit source-derived geometry.
- Canonical final-four pick slots point to their matching geometry slots.
- `CENTER-FINAL-FOUR` is no longer runtime pick-slot geometry.
