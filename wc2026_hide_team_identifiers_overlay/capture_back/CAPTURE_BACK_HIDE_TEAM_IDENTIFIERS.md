WB_SESSION:
Hide Team Identifiers

Changed:
- Added CSS/HTML update to hide visible team identifier metadata in the public site.
- Preserved identifiers in underlying team data and exported state.
- Added LI rule, feature note, card, and implementation script.
- Created release:
  `releases/world_cup_bracket_tracker_v007_hide_team_identifiers.html`

Reason:
- Public bracket should be cleaner.
- Flags and team names are enough for normal users.
- Internal identifiers can remain available in data or future Steve's building controls.

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `releases/world_cup_bracket_tracker_v007_hide_team_identifiers.html`
