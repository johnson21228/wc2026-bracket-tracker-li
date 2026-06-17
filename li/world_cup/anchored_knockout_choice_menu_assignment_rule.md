# Anchored Knockout Choice Menu Assignment Rule

A knockout choice menu is an assignment surface for the bracket cell that opened it.

## Rule

When a bracket cell opens a knockout choice menu:

- the menu must be visually adjacent to the opening cell when possible
- all tooltip surfaces must close
- the menu must preserve the opening cell as the write target
- selecting a team must write the team into that opening cell

## Invariant

The user must always be able to answer:

    Which bracket cell will this menu fill?

If that answer is unclear, the menu is not properly anchored.
