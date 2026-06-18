# Pick Menu Runtime v2

The pick menu is the primary user-facing bridge between bracket slots and model truth.

## Runtime behavior

When a slot is clicked, the controller asks the model for a complete pick-menu descriptor. The descriptor includes:

- slot id
- source title
- source label
- current pick
- clear-pick availability
- anchor bounds in board coordinates
- grouped candidate choices
- group-panel references

The view renders that descriptor without recomputing eligibility.

## Grouped choices

Group-derived choices are collected by group. Each group section has a visible label such as `Group C`. When group data is available, the label is clickable and opens the group standings panel for that group.

## Commands

The menu exposes separate commands:

- close menu
- clear current pick
- choose a team
- open a group panel

These actions must not overlap. A group-label click must not select a team. A close click must not mutate pick state. A clear-pick click must route through the model.

## Placement

The menu is rendered inside the board plane as an absolutely positioned board-attached surface. It is placed next to the source slot, shifted to avoid clipping, and scrolls with the game board.

## Runtime source boundary

The app consumes local JSON snapshots. It does not fetch, parse, or scrape ESPN from the browser runtime.
