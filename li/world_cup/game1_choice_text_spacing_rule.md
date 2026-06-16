# Game 1 Choice Text Spacing Rule

Player-facing chooser choices must keep the team name visually separated from team metadata.

- The country/team name is a distinct text unit.
- The team abbreviation is a distinct metadata unit.
- Group metadata is a distinct metadata unit.
- There must be visible spacing between the team name and the abbreviation.
- The UI must not render compressed strings such as `MexicoMEX`, `FranceFRA`, or `SenegalSEN`.

Chooser rows should use separate spans for flag, team name, and metadata. CSS must provide a real visual gap; relying only on normal inline whitespace is not enough. Hit/rule integrity remains coupled to this UI rule: making choices legible must not change slot rule, allowed group set, pointer resolution, or manifest-derived hit zone.
