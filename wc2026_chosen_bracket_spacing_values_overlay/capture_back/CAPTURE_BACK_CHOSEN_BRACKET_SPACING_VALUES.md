WB_SESSION:
Capture Chosen Bracket Spacing Values

Changed:
- Captured Steve's selected bracket spacing values from the browser spacing tuner.
- Added the selected values as data.
- Added implementation script to apply these values to the static HTML defaults and tuner reset defaults.
- Creates release:
  `releases/world_cup_bracket_tracker_v005_chosen_spacing.html`

Selected values:
```css
--r16-top: 31px;
--r16-gap: 34px;
--qf-top: 95px;
--qf-gap: 164px;
--sf-top: 224px;
--sf-gap: 387px;
--final-top: 372px;
```

Reason:
- The previous aligned bracket spacing was too wide.
- Steve used the tuner to choose tighter visual alignment values.
- These values should be the current defaults while the source-adjacent pod layout remains a future improvement.

Files added:
- `data/chosen_bracket_spacing_values.css`
- `cards/017_capture_chosen_bracket_spacing_values_card.md`
- `docs/features/chosen_bracket_spacing_values_note.md`
- `capture_back/CAPTURE_BACK_CHOSEN_BRACKET_SPACING_VALUES.md`
- `tools/apply_chosen_bracket_spacing_values_overlay.py`
