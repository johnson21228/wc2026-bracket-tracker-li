# Capture Back — Game 1 Scrollable Shared Board Only

Game 1 has been aligned to the same simple board-only review posture as Game 2.

The shared board is the 1536 × 1024 32-bit RGBA PNG at `site/assets/playfield/r32_bracket_geometry_overlay.png`.

This preserves the separation between shared board resources and separate game logic. Game 1 chooser logic should return as a pixel-native layer over this board, not as a competing geometry system.
