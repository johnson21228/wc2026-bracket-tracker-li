# Game 1 Choice Legibility and Hit-Rule Integrity

This capture repairs the Game 1 chooser row presentation and adds verification around R32 rule-to-menu integrity.

The immediate UI defect was compressed option text such as:

`FranceFRA · Group I`

That is hard to read and makes the chooser feel like implementation output. The player-facing row should separate the team name from metadata:

`France  FRA · Group I`

The repair makes the chooser row use separate DOM parts for the flag, team name, abbreviation, and group label.

The same capture also checks that the selected R32 hit target resolves to the correct rule and eligible team groups. This protects the prior third-place slot issue where a menu could show a neighboring winner-group rule instead of the third-place pool rule.

The rule data remains available for runtime diagnostics and verification even when implementation labels are hidden from the game board UI.
