WB_SESSION:
Pixelated Runtime Flag Background

Changed:
- Added pixelated runtime flag background rule.
- Added `data/pixelated_flag_background_config.json`.
- Updated Game 1 shared board HTML to render the background as an image-based flag layer instead of a crisp emoji text layer.
- Uses `image-rendering: pixelated` and `crisp-edges`.
- Lowers background opacity so the bracket template and picks remain readable.
- Keeps the flag layer beneath the gradient/readability wash and bracket template.
- Defaults background to USA.
- First pick can auto-adopt the selected team as background.
- Manual background selection locks the background override.
- Created release:
  `releases/world_cup_game_board_v006_pixelated_flag_background.html`

Decision captured:
- Background flag should act as visual texture, not primary content.
- The bracket board remains the hero layer.
- Runtime/pick layers stay above.
