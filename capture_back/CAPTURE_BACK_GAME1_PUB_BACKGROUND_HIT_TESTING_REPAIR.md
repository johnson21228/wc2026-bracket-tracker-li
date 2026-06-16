# Capture Back — Game 1 Pub Background and Hit Testing Repair

The Game 1 pub background JPEG existed but was visually hidden by the near-opaque board template. This capture back repairs the layer stack by making opacity tunable and exposing hit-zone debugging.

Runtime expectations:
- Pub background image is decorative and non-interactive.
- Board template is decorative and non-interactive.
- Hit targets remain above all decorative layers.
- The chooser opens when a Round-of-32 slot is clicked.
