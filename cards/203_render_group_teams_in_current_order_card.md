# Card 203: Render group teams in current standings order

## Intent

Ensure group-scoped team displays use the current standings order instead of the original group draw order whenever standings are available.

## Change

- Add LI for current group order rendering.
- Add documentation for the display-order contract.
- Add a model helper that resolves group teams through current standings entries.
- Use that helper for R32 pick choices, grouped pick-menu choices, and group rail flags.
- Add verification that Group A renders as `MEX, KOR, CZE, RSA` after the current standings snapshot.

## Boundary

This card does not search the internet, refresh scores, or recompute official standings. It renders the checked-in current standings model more consistently.
