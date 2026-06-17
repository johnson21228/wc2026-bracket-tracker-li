# Anchored Knockout Choice Menu Assignment

The knockout choice menu is the surface used to assign a winner to a bracket cell.

It should be visually adjacent to the bracket cell that opened it. The user should be able to see the relationship:

    this cell opened this menu
    this menu will fill this cell

## Required Behavior

When the menu opens:

1. Close all tooltip surfaces.
2. Record the opening bracket cell as the assignment target.
3. Position the menu beside that cell when possible.
4. Render only candidates that can fill that cell.
5. On selection, write the chosen team into the opening cell.
6. Close the menu and re-render picks.

## Why This Matters

The bracket board is a game surface. A menu is not a detached form control; it is part of the bracket interaction. Detached menus make it unclear where the selected value will go.
