# Game 1 R16 Winner Picks

Game 1 can now act as the first continuation phase of the long-lived bracket workspace.

Before this card, Game 1 only assigned teams into Round of 32 slots. This enhancement allows a Round of 16 slot to become pickable once both of its associated Round of 32 source slots have teams.

## Rule

For each side of the board:

- `R16-01` is fed by `R32-01` and `R32-02`
- `R16-02` is fed by `R32-03` and `R32-04`
- and so on through `R16-08`

A Round of 16 winner may be chosen only when both source R32 slots have assigned teams.

## Storage

R32 slot assignments remain in the existing Game 1 storage record.

R16 winner picks are stored separately so that future officialization and scoring can distinguish:

- predicted R32 slot assignment
- predicted knockout advancement
- official FIFA R32 truth
- Game 2 official-truth knockout picks

## Boundaries

This is a Game 1 runtime enhancement only. It does not alter Game 2 and does not move the SVG/manifest authority.
