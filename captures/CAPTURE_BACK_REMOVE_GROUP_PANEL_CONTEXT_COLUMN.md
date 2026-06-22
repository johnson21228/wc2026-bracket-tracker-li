# Capture Back — Remove group panel Context column

## Decision
Remove the visible `Context` column from the player-facing group standings panel.

## Preserved behavior
- Underlying standings data remains unchanged.
- Ranking logic remains unchanged.
- Group panel open/close behavior remains unchanged.
- Completed match cards and highlight links remain unchanged.
- Game 1 pick menus and pick validity remain unchanged.

## Implementation note
This is a View-only cleanup. If qualification context remains useful internally, it may stay in the model/data, but it should not render as a visible standings-table column.
