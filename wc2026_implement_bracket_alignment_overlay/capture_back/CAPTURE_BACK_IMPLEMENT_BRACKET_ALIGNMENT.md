WB_SESSION:
Implement Bracket Visual Alignment

Changed:
- Updated static HTML bracket layout to align later rounds to source matches.
- Simplified public page header/instructions.
- Added source labels/tooltips for R16, QF, SF, Final, and Champion slots.
- Created a new release copy:
  `releases/world_cup_bracket_tracker_v002_aligned_bracket.html`

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `releases/world_cup_bracket_tracker_v002_aligned_bracket.html`

Acceptance:
- `make verify` passes.
- `make pack` passes.
- `open index.html` shows the aligned bracket.
