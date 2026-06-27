# Player Standings Scoring Vocabulary

Player Standings should read and behave as a scoring table.

The visible table columns are:

- Score
- Max Possible

The implementation should avoid leaking older Group/Knockout scoring names into the presentation layer. Legacy `groupPoints` and `knockoutPoints` values may be accepted temporarily at the storage boundary while the runtime migrates to `score` and `maxPossible`.
