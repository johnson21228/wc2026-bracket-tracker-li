# Capture Back: Final Stack SVG Truth

## Intent

The Final Four center-stack geometry now follows the SVG-first authority model.

`site/assets/playfield/uniform_pick_card_gameboard.svg` is the visual geometry truth for the active board. The derived manifests are regenerated from the SVG slot rectangles for:

- `FINAL-LEFT`
- `FINAL-RIGHT`
- `CHAMPION`

## Layout

- `FINAL-LEFT` is centered between the two left semifinal feeder slots.
- `FINAL-RIGHT` mirrors `FINAL-LEFT` between the two right semifinal feeder slots.
- `CHAMPION` is the same size as the SF-winner slots and is centered on the SVG centerline near the upper bracket row.
- Connector linework flows from source slot centers into winner slots, then from the SF winners to the champion.

## Derived bounds

```json
{
  "FINAL-LEFT": {
    "x": 590,
    "y": 478,
    "width": 140,
    "height": 44
  },
  "CHAMPION": {
    "x": 698,
    "y": 118,
    "width": 140,
    "height": 44
  },
  "FINAL-RIGHT": {
    "x": 806,
    "y": 478,
    "width": 140,
    "height": 44
  }
}
```

## Verification

`tools/verify_wc2026_final_stack_svg_manifest_alignment.py` verifies that the SVG truth and derived manifests agree for the final-stack slots.
