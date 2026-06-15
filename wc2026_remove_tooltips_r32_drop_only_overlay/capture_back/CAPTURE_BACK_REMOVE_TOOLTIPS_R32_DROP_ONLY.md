WB_SESSION:
Remove Tooltips And Enforce R32 Drop Only

Changed:
- Removed current slot tooltip behavior from the static HTML.
- Removed visible later-round slot labels for now.
- Enforced direct drag/drop only for Round-of-32 slots.
- Later rounds now act as passive advancement placeholders.
- Created release:
  `releases/world_cup_bracket_tracker_v006_r32_drop_only_no_tooltips.html`

Reason:
- Current tooltips are premature.
- Drop placement is only wanted for Round-of-32 seeding.
- Later rounds should be populated later by winner selection, official results, or scoring logic.

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `releases/world_cup_bracket_tracker_v006_r32_drop_only_no_tooltips.html`
