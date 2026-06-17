# Capture Back — Pub background truth asset

## Change

Promoted the pub background image into the clean board-truth asset structure.

## Promoted asset

- from: `site/assets/playfield/game1_pub_options_background.jpeg`
- to: `site/assets/board-truth/backgrounds/pub_background.jpeg`

## Render update

The clean site background layer now renders from:

- `site/assets/board-truth/backgrounds/pub_background.jpeg`

## Test

Added:

- `tools/verify_wc2026_pub_background_truth_asset.py`

The verifier checks that the promoted asset exists, matches the discovered source byte-for-byte, and is the path used by the clean site module service.
