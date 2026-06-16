# Game 1 R32 Choice Menu Team Tile Spacing Rule

The Game 1 R32 choice menu is the modal opened by tapping an R32 pick target.

Each selectable option in that menu is a team tile. The active renderer for the menu uses:

- `.teamTile`
- `.teamFlag`
- `.teamMeta`
- `.teamName`
- `.teamDetail`

The team tile label must be legible as two separated text regions:

- team name, for example `Brazil`
- metadata, for example `BRA · Group C`

The team abbreviation must never visually touch the team name.

Invalid:

```text
BrazilBRA · Group C
GermanyGER · Group E
Ivory CoastCIV · Group E
```

Valid:

```text
Brazil  BRA · Group C
Germany  GER · Group E
Ivory Coast  CIV · Group E
```

This spacing must be enforced on the live `.teamTile` renderer, not only on generic or older `.choice*` selectors.

The menu may keep structured spans, but CSS must provide an explicit gap or margin between `.teamName` and `.teamDetail`.
