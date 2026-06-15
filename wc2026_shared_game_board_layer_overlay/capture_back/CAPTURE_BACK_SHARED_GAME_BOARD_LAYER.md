WB_SESSION:
Shared Game Board Layer

Changed:
- Added the clean 32-team bracket template image:
  `assets/playfield/r32_bracket_game_board_template.png`
- Updated `game1_playfield.html` to use the template as the shared game board surface.
- Preserved bottom background flag layer, default USA.
- Added gradient/readability wash.
- Added runtime title layer above the board image.
- Preserved R32 hotspot modal chooser for Game 1.
- Picks render over the matching R32 cells with flag and team name.
- Added board config:
  `data/game_board_layer_config.json`
- Created release:
  `releases/world_cup_game_board_v005_shared_template.html`

Decision captured:
- This is a reusable game board.
- Game 1 uses it to pick the Round of 32.
- Game 2 will later use it to start from the given Round of 32 and pick winners through final champion.
- Future title, banner, scoring, and game mode layers should be added above the board, not baked into it.
