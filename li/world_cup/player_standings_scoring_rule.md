# Rule: Player Standings Scoring

Player Standings must compute each player's earned points and maximum possible points from the player's submitted/live bracket picks compared against `Admin_/official` result truth.

## Round weights

Correct picks score by round:

- R16 correct pick: 1 point
- R8 correct pick: 2 points
- R4 correct pick: 4 points
- R2 correct pick: 8 points
- Champion/Winner correct pick: 16 points

## Perfect bracket budget

For a full knockout bracket:

- 8 R16 winner slots × 1 point = 8
- 4 R8 winner slots × 2 points = 8
- 2 R4 winner slots × 4 points = 8
- 2 R2 finalist slots × 8 points = 16
- 1 Champion/Winner slot × 16 points = 16

Total perfect score: 56 points.

## Earned points

A player's earned points are the sum of weighted player picks that match resolved `Admin_/official` result truth.

A slot scores only when:

1. The player has a pick for that slot.
2. `Admin_/official` has resolved truth for that slot.
3. The player's canonical picked team ID equals the official canonical team ID for that slot.

Unresolved official slots score zero for now. They are not wrong yet.

## Maximum possible points

A player's maximum possible points is the player's current ceiling from their existing bracket.

It is computed as:

- all points already earned, plus
- weighted points from unresolved future slots that the player can still get right, provided the player's picked team is still viable under already-resolved official truth.

A future pick is no longer possible when earlier resolved official truth has eliminated the player's selected team from reaching that future slot.

## Authority

`Admin_/official` is the only source of scoring truth.

Normal player picks never define official results. Normal player picks are compared against `Admin_/official` truth.

## Display

Player Standings should be able to display both:

- earned points
- maximum possible points

Example display shape:

`14 / 42 possible`

where `14` is earned and `42` is the player's current maximum possible score.
