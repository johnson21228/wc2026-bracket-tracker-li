# Capture Back: Floating controls fixed-size during board zoom

## Context

The WC2026 Bracketeering Hub supports Pages-owned board zoom, mouse wheel / pinch zoom, and map-style floating controls.

## Captured change

Browser/player floating controls are fixed viewport chrome and must not scale with the board.

## Rule

The gameboard content may zoom and pan. Browser controls must remain fixed-size.

## Runtime surfaces

Fixed-size browser chrome includes:

- map zoom + / − controls
- info panel button
- auth identity surface
- fixed status/info overlays
- lifecycle/stage selector if later surfaced as viewport chrome

## Verification

`tools/verify_wc2026_floating_controls_fixed_size_during_zoom.py` verifies:

- board zoom transform remains scoped to `.pixel-native-board-plane`
- `.board-scale-frame` remains a render-size wrapper, not the transform owner
- map controls and identity surface are outside board scroll/plane markup
- fixed control CSS explicitly blocks transform/zoom inheritance
- Makefile runs this verifier
