# Card 081 — Tune R32 Pick Card Single Tooltip and Name Fit

## Intent

Tune the Round of 32 pick-card rendering surface so selected teams are legible and only one details surface is shown.

## Acceptance

- Filled pick cards do not set a native `title` tooltip.
- A single reusable custom details surface is used.
- Team names are fit by card width and font-size adjustment before ellipsis fallback.
- Cards remain clickable/tappable to reopen the chooser.
- Verification passes.
