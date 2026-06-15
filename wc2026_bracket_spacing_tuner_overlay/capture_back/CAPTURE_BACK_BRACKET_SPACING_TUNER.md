WB_SESSION:
Add Bracket Spacing Tuner

Changed:
- Added a browser-based spacing tuner for bracket visual layout.
- The tuner exposes R16, QF, SF, and Final vertical spacing values as sliders.
- The tuner lets the user copy chosen CSS values for later Capture Back.
- Created release:
  `releases/world_cup_bracket_tracker_v003_spacing_tuner.html`

Reason:
- The aligned bracket spacing was too wide.
- Stage 0 workflow should allow human visual tuning instead of guessing CSS.

Next:
- Open `index.html`.
- Adjust sliders until the bracket looks right.
- Copy chosen CSS values.
- Paste values back for the next CB/implementation overlay.
