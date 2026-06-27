# Card 1023 — Use Knockout Pub Background as Runtime Default

## Intent

Make the generated knockout pub calendar background the image the site actually uses at runtime.

## Runtime asset

- `site/assets/board/knockout_pub_background.jpeg`

## Source/reference asset

- `source/images/wc2026_knockout_pub_calendar_background.jpeg`

## Acceptance

- The site preload points to the knockout background.
- The initial board background image points to the knockout background.
- The asset path service points to the knockout background.
- Legacy active-game background aliases both resolve to the knockout background so no old group-stage fallback appears.
- The change remains presentation-only.
- `make verify` and `make pack` pass.
