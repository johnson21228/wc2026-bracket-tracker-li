# Capture Back: Pages-owned board wheel/pinch zoom

## Intent

Extend the Pages-owned board zoom runtime so the bracket board can zoom from wheel/pinch-style events, not only from the preset dropdown.

## Runtime behavior

- Board zoom remains View-owned.
- The native board coordinate plane remains authoritative.
- Normal scrolling remains available.
- Modified wheel events (`ctrlKey` or `metaKey`) zoom the board.
- Browser pinch gestures that arrive as `ctrlKey` wheel events zoom the board.
- Zoom is clamped to a reasonable range: 50% minimum and 125% maximum.
- Zoom is pointer-centered so the visible board location does not jump to top-left.

## Product rule

Players should be able to zoom out far enough to see more of the bracket board without losing the native hit-test model.
