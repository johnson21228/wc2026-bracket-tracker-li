# Capture Back: Final Four Center-Stack Pick Menu

## Intent

Wire the explicit Final Four center-stack cells into the existing precedent-aware pick menu path.

## Runtime behavior

- `FINAL-LEFT` uses `L-SF-01` / `L-SF-02` as precedent.
- `FINAL-RIGHT` uses `R-SF-01` / `R-SF-02` as precedent.
- `CHAMPION` uses selected `FINAL-LEFT` / `FINAL-RIGHT` as precedent.
- `THIRD-PLACE-WINNER` remains constrained to semifinal losers.

## Boundary

No new menu system was introduced. The controller still preselects the clicked slot by setting `activeSlotId`, and the view opens the existing pick menu from `model.getPickMenu(activeSlotId)`.

## Non-goals

No lifecycle-stage pick gating, storage, scoring, Supabase, group data, current results, or R32/R16/QF/SF behavior changed.
