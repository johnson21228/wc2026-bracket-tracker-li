WB_SESSION:
Game 1 Modal Chooser Runtime Storage

Changed:
- Uses the provided USA-themed playfield image as the background.
- Keeps the image as the simple game board.
- Adds transparent R32 hotspots.
- Clicking/tapping a hotspot opens an external chooser modal/window.
- The chooser is populated from group/flag data and official slot rules.
- Picks are saved in browser localStorage.
- Picked flags render over the background at the hotspot.
- Chooser includes a delete/remove pick action.
- Export/import JSON remains available.
- Created release:
  `releases/world_cup_game1_playfield_v003_modal_chooser.html`

Decision captured:
- Do not use a complicated control-heavy background.
- Use click-to-open chooser frame/window for user selection.
