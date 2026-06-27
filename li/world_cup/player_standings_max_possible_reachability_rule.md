# Rule: Player Standings Max Possible Reachability

Player Standings `Max Possible` must represent the player's real remaining scoring ceiling, not merely the value of unresolved slots.

## Core rule

A player pick counts toward `Max Possible` only if that pick could still become site-owned official truth.

Admin empty/unresolved is necessary but not sufficient.

For an unresolved scoring slot:

- If the player has no pick, the slot contributes 0 to Max Possible.
- If the player has a pick and that team can still reach that slot, the slot contributes that slot's weight to Max Possible.
- If the player has a pick but prior resolved site-owned official truth has already eliminated that team from reaching that slot, the slot contributes 0 to Max Possible.

## Resolved slots

For a resolved scoring slot:

- If the player's pick matches site-owned official truth, the slot contributes its weight to both `Score` and `Max Possible`.
- If the player's pick does not match site-owned official truth, the slot contributes 0 to both `Score` and `Max Possible`.

## Reachability

A team is no longer reachable for a future slot when a required earlier slot in that team's bracket path has been resolved by site-owned official truth to a different team.

Example:

If a player picked Brazil to win R16, R8, R4, R2, and Champion, but site-owned official truth resolves Brazil as losing in R16, then Brazil's later R8/R4/R2/Champion picks no longer count toward Max Possible.

## Authority

site-owned official truth is the only source of elimination and scoring truth.

Normal player picks do not eliminate teams by themselves. They only define that player's selected path.
