# Capture Back — Game 1 R32 Assignment Layer

Game 1 has been rebuilt on the shared pixel-native board foundation.

The important preserved rule is:

```text
Game 1 and Game 2 share board resources, but keep separate game behavior.
```

Game 1 now adds only its own R32 assignment behavior on top of the shared board:

- pixel-native R32 slot controls
- team chooser
- localStorage assignment state
- JSON export

The board remains the 1536 × 1024 32-bit RGBA PNG at:

```text
site/assets/playfield/r32_bracket_geometry_overlay.png
```
