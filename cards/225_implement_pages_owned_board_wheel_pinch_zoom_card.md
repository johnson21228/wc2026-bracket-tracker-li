# Card 225: Implement Pages-owned board wheel/pinch zoom

## Outcome

The board zoom runtime now supports modified wheel and browser pinch-style zoom events in addition to the preset selector.

## Acceptance

- `make verify` passes.
- Board zoom is clamped between 50% and 125%.
- Wheel/pinch zoom calls the same render-scale path as the dropdown.
- Normal board scroll remains available.
- Zoom keeps the pointer-centered board point stable.
