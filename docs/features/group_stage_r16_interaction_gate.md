# Group Stage R16+ Interaction Gate

During Group Stage presentation, later-round bracket cells are shown as frame-only placeholders. The UI must not invite or accept pick-menu interaction on those cells.

## Rule

When Group Stage presentation is active:

- R32 cells remain pickable.
- R16+ cells remain visible as bracket structure.
- R16+ cells suppress fill, label, value, team identity, pickable cursor, and pick-menu invocation.

When Knockout Stage presentation is active:

- R16+ cells regain normal pick rendering and pick interaction.

## Boundary

This rule is View/Controller-facing. It must not erase stored picks or prevent the model from holding future-round picks.
