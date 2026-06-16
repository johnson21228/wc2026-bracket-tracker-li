# Game 1 Choice Legibility and Hit-Rule Integrity Rule

Game 1 chooser options must be legible player-facing pick choices, not compressed implementation text.

## Choice row wording

Each chooser row must visually separate:

- the country/team display name
- the team abbreviation
- the group metadata

The team name and metadata must not concatenate. For example, the UI must read like:

- `France  FRA · Group I`
- `Senegal  SEN · Group I`

It must never render as:

- `FranceFRA · Group I`
- `SenegalSEN · Group I`

## Implementation rule

The chooser row must use separate DOM spans/classes for:

- flag
- team name
- team abbreviation
- group metadata

Spacing must be provided by CSS and by explicit readable separators, not by accidental text flow.

## Hit-rule integrity rule

The menu shown for an R32 pick card must come from the R32 rule associated with the SVG/manifest slot that the user selected.

The visible slot, hit target, and menu choices must agree on:

- slot id
- rule short label
- rule long label
- allowed groups
- eligible teams

Third-place slots must show teams only from the groups named in that slot rule. Winner and runner-up slots must show teams only from that single group.

Implementation/debug labels may be hidden from the player-facing UI, but their rule data must remain available for verification and diagnostics.
