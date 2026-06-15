WB_SESSION:
Layered Playfield Bracket-Only

Changed:
- Refactors `game1_playfield.html` into a layered playfield.
- Bottom layer is a selected team flag resource, default USA.
- Adds gradient wash over the bottom layer.
- Middle layer is drawn with bracket graphics only.
- Title and bottom banner content are intentionally not part of the middle layer.
- Hotspots, picked flags, modal chooser, storage, export/import remain HTML/runtime layers.
- Created release:
  `releases/world_cup_game1_playfield_v004_layered_bracket_only.html`

Decision captured:
- No title or bottom banner text should be baked into the bracket graphics layer.
- Only bracket geometry belongs in the middle layer.
