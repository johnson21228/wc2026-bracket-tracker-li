# Card 017 — Capture Chosen Bracket Spacing Values

## Intent

Capture Steve's chosen bracket spacing values after visual tuning in the browser.

## Values

```css
--r16-top: 31px;
--r16-gap: 34px;
--qf-top: 95px;
--qf-gap: 164px;
--sf-top: 224px;
--sf-gap: 387px;
--final-top: 372px;
```

## Acceptance

- Values are stored in `data/chosen_bracket_spacing_values.css`.
- Static HTML defaults are updated to these values.
- Spacing tuner reset defaults use these values.
- New static release is created.
