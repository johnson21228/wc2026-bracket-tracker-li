# Capture Back — July 4 R16 Extended Highlights

## Captured update

Added user-provided extended highlights URLs for the July 4 Round of 16 matches.

## Result records

- `r16-fra-par-2026-07-04` — France 1–0 Paraguay — `https://youtu.be/bQ5Z4Q8VQ8w`
- `r16-can-mor-2026-07-04` — Morocco 3–0 Canada — `https://youtu.be/QLFucR6SGr4`

## Data boundary

The URLs are stored on the existing official knockout result records in `site/data/official_knockout_results.json` as `extendedHighlightsUrl`.

This does not change scoring, winner projection, player picks, official R32 seed truth, or bracket topology.

## Verification

`tools/verify_wc2026_july_04_r16_extended_highlights.py` protects the two result IDs, their left-side topology, their winners, and their user-provided extended highlight URLs.
