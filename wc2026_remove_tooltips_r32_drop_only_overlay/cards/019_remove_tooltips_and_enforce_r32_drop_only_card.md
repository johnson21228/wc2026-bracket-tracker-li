# Card 019 — Remove Tooltips And Enforce R32 Drop Only

## Intent

Simplify the current bracket UI.

## Changes

- Remove slot tooltips for now.
- Remove visible later-round slot labels for now.
- Allow drag/drop only into Round-of-32 slots.
- Later rounds show a passive placeholder such as `Advances here`.

## Acceptance

- R32 slots accept dropped teams.
- R16, QF, SF, Final, and Champion do not accept dropped teams.
- Later-round slots do not show tooltips.
- Export/import still works.
- New static HTML release is created.
