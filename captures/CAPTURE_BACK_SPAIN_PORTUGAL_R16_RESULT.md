# Capture Back — Spain Portugal R16 Result

## Captured update

Added the user-supplied official Round of 16 result for Portugal vs Spain in Dallas.

## Result record

- `r16-por-esp-2026-07-06` — Spain 1–0 Portugal
- Spain advances from `L-R16-05` / `L-R16-06` into `L-QF-03`.

## Data boundary

The result is stored in `site/data/official_knockout_results.json` as an append-only official knockout result row.

This does not write the R16 winner into `site/data/current/official_truth.json`; that file remains the R32 seed truth source only.

## Verification

`tools/verify_wc2026_spain_portugal_r16_result.py` protects the result row, score, winner, left-side topology, and R32-only official truth boundary.
