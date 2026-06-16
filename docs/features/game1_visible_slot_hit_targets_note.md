# Game 1 Visible Slot Hit Targets

The Game 1 playfield uses a layered model:

1. Pub background image.
2. Transparent bracket geometry PNG.
3. Runtime DOM hit targets and picks.
4. Modal chooser.

The hit target layer is intentionally visible by default. The opacity is controlled by CSS variables and page sliders so the slot surfaces can be tuned without editing the PNG assets.
