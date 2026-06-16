Repair the Game 1 R32 choice menu team tile spacing.

Target the live `.teamTile` renderer, not only `.choice*` selectors. Ensure `.teamName` and `.teamDetail` are separated by layout gap/margin so labels render as `Brazil  BRA · Group C`, never `BrazilBRA · Group C`.
