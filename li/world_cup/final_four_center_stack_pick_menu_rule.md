# Final Four Center-Stack Pick Menu Rule

Final Four center-stack cells must use the existing precedent-aware pick menu pipeline.

Required precedent constraints:

- `FINAL-LEFT` depends on `L-SF-01` and `L-SF-02`.
- `FINAL-RIGHT` depends on `R-SF-01` and `R-SF-02`.
- `CHAMPION` depends on `FINAL-LEFT` and `FINAL-RIGHT`.
- `THIRD-PLACE-WINNER` remains constrained to the two semifinal losers.

The view may preselect the clicked cell only by passing its canonical slot ID into the existing controller/menu path. It must not create a parallel menu system or bypass model validation.
