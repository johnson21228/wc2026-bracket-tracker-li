# Card 208: Remove current-rank pick conflict

## Intent

Keep picks source-scoped, but stop treating disagreement with the current group standings rank as an invalid pick.

## Change

- Preserve user picks that are inside the slot's encoded source scope.
- Remove the model's winner/runner-up current-rank invalidity check from picked-cell validity.
- Keep structural warning paths such as duplicate Round-of-32 assignments.
- Add LI, docs, capture-back, and verification.

## Acceptance

- `pickValidityForSlot()` no longer emits a warning such as "this slot expects the Group X winner/runner-up" based on `entry.rank`.
- Duplicate Round-of-32 picks can still be rendered as warnings.
- Slot source-scope checks remain intact.
- `make verify` runs the Card 208 verifier.
