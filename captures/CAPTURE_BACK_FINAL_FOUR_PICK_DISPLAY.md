# Capture Back: Final Four pick display

## Intent

Render the center Final Four area as a player-facing display for the canonical final-four pick records:

- FINAL-LEFT
- FINAL-RIGHT
- CHAMPION
- THIRD-PLACE-WINNER

## Boundary

CENTER-FINAL-FOUR remains visual-only board geometry.

It is not restored as a normal pick-slot button.

## Runtime behavior

The center panel displays:

- the left semifinal winner pick
- the right semifinal winner pick
- the final winner / champion pick
- the third-place winner pick

The actual write path remains the existing pick controller and model `setPick` pipeline.

## Storage implication

This uses the existing canonical slot IDs that are already present in the durable BracketDocument target. No new storage surface is introduced.
