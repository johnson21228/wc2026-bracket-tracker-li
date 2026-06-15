WB_SESSION:
Force Adjacent Pane Layout

Changed:
- Added CSS to force the two major panes to sit directly next to each other.
- Targets the page-level `.main` grid and `.panel` spacing.
- Created release:
  `releases/world_cup_bracket_tracker_v013_force_adjacent_panes.html`

Reason:
- Prior changes narrowed elements but did not remove the large gap between the two major panes.
- The gap is controlled by page-level layout, not by bracket slot width.

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `releases/world_cup_bracket_tracker_v013_force_adjacent_panes.html`
