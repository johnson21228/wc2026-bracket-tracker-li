# Capture Back — Game 2 Scrollable Board-Only Review

Game 2 has been moved into a scrollable board-only source review posture.

The board is rendered at its native 1536 × 1024 pixel size. The browser scrolls around the board instead of scaling it down to fit the window.

This preserves the pixel-native model:

- the board image is the current geometry authority;
- every future logical item must map to a native pixel-defined region;
- hit testing and rendering should use the same pixel plane;
- display scaling must not create a second coordinate system.
