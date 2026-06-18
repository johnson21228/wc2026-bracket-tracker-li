# Game 1 R32 pick controller rule

Game 1 R32 projection pick rules must be enforced by a controller, not by the rendered menu layer.

The controller must decide:

- whether a menu is enabled
- which teams are legal candidates
- whether a selected team is valid for the slot
- whether a selected team is already used elsewhere in the projected R32 board
- how the selected pick is written back to the data model

The rendered R32 pick menu layer may display controller output and forward user actions, but it must not become the source of rule truth.

Pre-lock candidate rules:

- `group-winner`: all teams from the group.
- `group-runner-up`: all teams from the group.
- `third-place-candidate-set`: all teams from all listed groups.

Post-lock official FIFA assignment remains a separate official R32/Annex C layer.
