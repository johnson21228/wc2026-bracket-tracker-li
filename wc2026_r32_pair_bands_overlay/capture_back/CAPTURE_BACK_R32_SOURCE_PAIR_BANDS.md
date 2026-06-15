WB_SESSION:
Add Round-of-32 Source Pair Bands

Changed:
- Added UI requirement and implementation for subtle horizontal bands around each Round-of-32 match pair.
- Bands make it clearer which two teams form each R32 source match.
- Bands include a small match label and tooltip.
- Created release:
  `releases/world_cup_bracket_tracker_v004_r32_pair_bands.html`

Reason:
- Bracket alignment alone was not enough.
- Horizontal bands improve visual readability and screenshot recovery.

Files added:
- `li/world_cup/r32_source_pair_band_rule.md`
- `cards/014_add_r32_source_pair_bands_card.md`
- `docs/features/r32_source_pair_bands_note.md`
- `prompts/add_r32_pair_bands_to_html.md`

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `releases/world_cup_bracket_tracker_v004_r32_pair_bands.html`
