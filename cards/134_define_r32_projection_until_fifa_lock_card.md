# Card 134: Define R32 Projection Until FIFA Lock

## Intent

Make the all-inclusive Game 1 state model explicit: Round of 32 assignments are editable projections until FIFA officially assigns/locks the bracket.

## Why

The current implementation drifted toward treating R32 as fixed source data. That is wrong for the all-inclusive game. Before the final FIFA assignment, R32 is a user-generated projection layer.

## Rule

R32 is not immutable until the R32 lock state is official.

## Acceptance

- Site exposes a stored R32 assignment phase.
- Default state is projection/unlocked.
- State can later become official/locked from FIFA.
- UI can observe the state.
- LI documents the distinction between projected R32 assignments and official R32 assignments.
