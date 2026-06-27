# Rule: Player Standings Scoring Vocabulary

Player Standings is a scoring table, not a Group/Knockout category table.

## Display rule

The visible Player Standings table must use scoring vocabulary:

- `Score`
- `Max Possible`

The visible standings surface must not render or expose Group/Knockout as standings score column concepts.

## Runtime naming rule

Presentation-facing DOM classes and normalized row fields should use scoring vocabulary:

- `score`
- `maxPossible`
- `player-standings-score`
- `player-standings-max-possible`

Old names such as `groupPoints`, `knockoutPoints`, `player-standings-group-count`, and `player-standings-knockout-count` may only remain as temporary storage-boundary compatibility inputs.

They must not be used as visible standings display concepts.

## Authority

The scoring model is defined by Player Standings scoring LI and Max Possible reachability LI.
