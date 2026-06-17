# Menu Selection Storage and Render

The knockout choice menu is an assignment surface for the bracket cell that opened it.

When the user selects a team from the menu, the app must:

1. Resolve the active bracket cell.
2. Normalize the selected team into a stored pick.
3. Save the pick into the correct storage object.
4. Re-render the bracket pick layer.
5. Close the menu.

## Storage Targets

- R16 cells write to `r16Picks`.
- Later knockout cells write to `advancementPicks`.

## Rendering

Rendering is not optional. A stored pick that is not rendered is incomplete UI state.
