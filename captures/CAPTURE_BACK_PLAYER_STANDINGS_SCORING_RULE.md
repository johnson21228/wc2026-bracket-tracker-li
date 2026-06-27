# Capture Back: Player Standings Scoring Rule

## Outcome

Defined the Player Standings scoring model.

## Rule

Correct picks score by round:

- R16: 1 point
- R8: 2 points
- R4: 4 points
- R2: 8 points
- Champion/Winner: 16 points

A perfect bracket has 56 total points.

## Standings outputs

Player Standings should compute:

- earned points
- maximum possible points

Earned points come only from player picks that match resolved `Admin_/official` truth.

Maximum possible points is the player's current scoring ceiling from their existing bracket, excluding future picks made impossible by already-resolved official truth.
