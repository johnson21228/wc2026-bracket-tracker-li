# Game 1 Scrollable Shared Board-Only Review

This capture makes Game 1 visually match the Game 2 board-only review surface.

The purpose is to confirm the shared board geometry before rebuilding Game 1's chooser layer.

## Current Game 1 surface

- Native board size: 1536 × 1024
- Board image: `site/assets/playfield/r32_bracket_geometry_overlay.png`
- Background: board-attached pub layer
- Display: native-size scrollable plane
- Visible controls: none

## Later reintroduction

Game 1's R32 chooser, group filtering, hit targets, and rendered picks should be layered back onto this same pixel-native board. They must not create a separate visual board or use a different board image.
