WB_SESSION:
Implement Square Flag Drop Targets

Changed:
- Updated static HTML/CSS to make bracket slots compact square flag-only targets.
- Bracket slots now visually show only flags when filled.
- Team identity is preserved as hover tooltip/title.
- Drop behavior remains limited to Round-of-32 slots.
- Created release:
  `releases/world_cup_bracket_tracker_v009_square_flag_drop_targets.html`

Reason:
- The prior drop target/display was still too wide.
- The bracket only needs the flag visually.
- Full team identity should be available by tooltip and preserved in exported state.

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `releases/world_cup_bracket_tracker_v009_square_flag_drop_targets.html`
