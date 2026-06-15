WB_SESSION:
Tighten Outer Pane Gutter

Changed:
- Reduced the horizontal gap between the left team pane and bracket pane.
- Added CSS variable `--pane-gutter: 8px`.
- Patched page-level grid spacing and panel margins.
- Created release:
  `releases/world_cup_bracket_tracker_v014_tight_outer_pane_gutter.html`

Reason:
- The previous layout still had a large black gap between the two major panes.
- The desired layout uses the same small gap as other UI spacing.

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `releases/world_cup_bracket_tracker_v014_tight_outer_pane_gutter.html`
