WB_SESSION:
Compact Bracket CSS Reflow

Changed:
- Updated static HTML/CSS so match bands, connectors, later-round slots, columns, and final area are tied to the compact square flag tiles.
- Retuned spacing tuner defaults to compact values.
- Created release:
  `releases/world_cup_bracket_tracker_v010_compact_reflow.html`

Reason:
- The drop target/display was made compact, but surrounding controls remained too wide.
- The bracket needed a full CSS reflow around the smaller item.

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `releases/world_cup_bracket_tracker_v010_compact_reflow.html`
