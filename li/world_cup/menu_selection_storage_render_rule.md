# Menu Selection Storage Render Rule

A knockout choice menu is not merely a list of teams. It is an assignment surface for the bracket cell that opened it.

When a user chooses a team:

- the active bracket cell is the write target
- the selected team is persisted to that cell's round-specific pick storage
- the stored pick includes the assigned slot id
- the bracket pick layer is rendered immediately
- the menu closes after assignment

A menu selection that does not write and render the pick is a failed interaction.
