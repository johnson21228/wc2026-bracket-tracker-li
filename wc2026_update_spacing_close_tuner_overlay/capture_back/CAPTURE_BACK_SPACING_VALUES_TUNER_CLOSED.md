WB_SESSION:
Capture Updated Spacing Values And Close Tuner

Changed:
- Captured updated bracket spacing values.
- Updated HTML/CSS defaults and tuner slider/reset values.
- Set the bracket spacing tuner/details control to closed by default.
- Created release:
  `releases/world_cup_bracket_tracker_v015_spacing_values_tuner_closed.html`

Selected values:
```css
--r16-top: 24px;
--r16-gap: 22px;
--qf-top: 90px;
--qf-gap: 155px;
--sf-top: 217px;
--sf-gap: 406px;
--final-top: 318px;
```

Reason:
- Steve visually tuned the bracket and selected updated spacing values.
- The layout control is useful for building, but should not be open by default.

Files expected to change:
- `index.html`
- `html/world_cup_bracket_tracker.html`
- `html_world_cup_bracket_tracker_v001.html`
- `data/chosen_bracket_spacing_values_v2.css`
- `releases/world_cup_bracket_tracker_v015_spacing_values_tuner_closed.html`
