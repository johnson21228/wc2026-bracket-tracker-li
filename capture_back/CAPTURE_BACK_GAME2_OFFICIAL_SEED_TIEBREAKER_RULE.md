# Capture Back — Game 2 Official Seed and Game 1 Tiebreaker Rule

## Captured Decision

Game 2 should use a fixed Round-of-32 seed as bracket truth. During development that seed can be random/demo data. Later it can be official FIFA/live-result data.

Game 1 remains valuable because the user's Game 1 Round-of-32 picks can be compared with the fixed/official Round of 32. Correct slot/team matches can be rendered on the Game 2 Round-of-32 items and used as a tiebreaker.

## Boundary

Game 1 picks are not allowed to mutate the Game 2 bracket after fixed/official Round-of-32 data exists. They are comparison metadata only.

## Implementation Direction

Future Game 2 implementation should support:

- fixed Round-of-32 seed rendering with flag and country
- optional Game 1 comparison metadata
- visible correct/missed annotations
- `Game 1 R32 correct: N / 32` tiebreaker display
- progressive knockout winner picking from the fixed seed
- downstream invalidation when upstream knockout picks change or clear
