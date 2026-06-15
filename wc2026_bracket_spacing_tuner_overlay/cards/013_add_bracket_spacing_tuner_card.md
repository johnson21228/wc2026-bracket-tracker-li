# Card 013 — Add Bracket Spacing Tuner

## Intent

Add a temporary visual tuning control to the static HTML so the human can adjust bracket spacing in the browser.

## Why

The bracket alignment is close but the vertical spacing is too wide. Rather than guessing in CSS, the page should expose the important layout values as sliders so the user can tune visually.

## Acceptance

- Site has a spacing tuner panel.
- Sliders control R16, QF, SF, and Final vertical layout values.
- User can copy the selected CSS values.
- New release is created.
- Once values are chosen, a later CB should lock the values and optionally remove/hide the tuner.
