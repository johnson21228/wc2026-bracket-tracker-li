# Player Standings Scoring

Player Standings computes earned points and maximum possible points by comparing player picks against site-owned official result truth.

## Weights

- R16 correct pick: 1 point
- R8 correct pick: 2 points
- R4 correct pick: 4 points
- R2 correct pick: 8 points
- Champion/Winner correct pick: 16 points

A perfect bracket has a 56-point budget.

## Earned points

Earned points are awarded only for resolved official slots where the player's canonical team ID matches the site-owned official truth canonical team ID.

## Maximum possible points

Maximum possible points is the player's current bracket ceiling: earned points plus unresolved future points that are still reachable from the player's existing picks.
