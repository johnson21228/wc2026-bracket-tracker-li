# Card 292: Player Standings Scoring Rule

## Intent

Define Player Standings scoring before runtime implementation.

## Scoring

- R16: 1 point per correct pick
- R8: 2 points per correct pick
- R4: 4 points per correct pick
- R2: 8 points per correct pick
- Champion/Winner: 16 points

Perfect bracket budget: 56 points.

## Acceptance

- Earned points compare player picks against `Admin_/official` truth.
- Maximum possible points represents the player's remaining ceiling from their existing picks.
- Unresolved official slots do not score yet.
- Eliminated future picks no longer count as possible.
