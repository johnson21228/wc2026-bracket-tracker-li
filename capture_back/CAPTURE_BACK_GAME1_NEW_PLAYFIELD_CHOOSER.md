WB_SESSION:
Update Game 1 Playfield Background And Tap Chooser

Changed:
- Replaced Game 1 playfield background with the new USA-themed single-frame image.
- Added/updated hit-test areas for all 32 Round-of-32 cells.
- On tap/click, the slot picker shows the official slot rule and a team chooser limited by the relevant group set.
- Picked teams appear as flags on the image.
- Export/import JSON still captures player picks.
- Created release:
  `releases/world_cup_game1_playfield_v002_usa_background.html`

Reason:
- The image is now intended to be the main UI surface for Game 1.
- Game 1 is "Pick the Round of 32" by selecting which team fills each official slot.

Files expected:
- `assets/playfield/r32_usa_single_frame_playfield.jpeg`
- `game1_playfield.html`
- `releases/world_cup_game1_playfield_v002_usa_background.html`
