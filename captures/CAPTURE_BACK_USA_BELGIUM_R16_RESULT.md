# Capture Back — USA Belgium R16 Result

## Captured update

Added the user-supplied official Round of 16 result for United States vs Belgium.

## Result record

- `r16-usa-bel-2026-07-06` — Belgium 4–1 United States
- Belgium advances from `L-R16-07` / `L-R16-08` into `L-QF-04`.

## Data boundary

The result is stored in `site/data/official_knockout_results.json` as an append-only official knockout result row.

This does not write the R16 winner into `site/data/current/official_truth.json`; that file remains the R32 seed truth source only.

## Verification

`tools/verify_wc2026_usa_belgium_r16_result.py` protects the result row, score, winner, left-side topology, and R32-only official truth boundary.
