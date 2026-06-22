# Card 258: Wire Final Four center-stack pick menu

## Status

Done.

## Decision

The explicit Final Four center-stack cells are first-class pick surfaces that use the existing model/controller/menu pipeline.

## Acceptance

- `FINAL-LEFT` is constrained by `L-SF-01` / `L-SF-02`.
- `FINAL-RIGHT` is constrained by `R-SF-01` / `R-SF-02`.
- `CHAMPION` is constrained by `FINAL-LEFT` / `FINAL-RIGHT`.
- `THIRD-PLACE-WINNER` remains constrained by semifinal losers.
- `CENTER-FINAL-FOUR` does not return as runtime pick-slot geometry.
