# Capture Back: Player Standings Max Possible Reachability

## Outcome

Captured the refined Max Possible rule for Player Standings.

## Clarification

A player earns Score points when their pick matches `Admin_/official` truth.

For Max Possible, unresolved Admin slots count only when the player's pick could still come about.

That means:

- Admin unresolved + player pick still reachable = possible points remain.
- Admin unresolved + player pick already eliminated by prior official truth = no possible points.
- Admin resolved + player matches = earned and still included in Max Possible.
- Admin resolved + player misses = no points and no remaining possible points.

This prevents eliminated future picks from inflating a player's ceiling.
