# Capture Back — Shared Pixel-Native Game Board Source

This Capture Back records the board-source simplification.

The Workbench now treats the high-definition 1536 × 1024 game board image as the shared board surface for both Game 1 and Game 2.

The essential invariant is:

> Every logical item must map to a pixel-defined region on the shared native board plane.

The visual board, hit-testing layer, render-item layer, and advancement logic must share the same native board coordinate system. Browser scaling is display-only.
