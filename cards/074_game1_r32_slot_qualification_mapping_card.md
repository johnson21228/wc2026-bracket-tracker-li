# Card 074 — Restore Game 1 R32 slot qualification mapping

## Intent
Restore the Game 1 logic where every R32 slot knows its qualification meaning before a team is assigned.

## Rule
A tap on a slot opens a group-filtered menu based on the slot's rule: group winner, group runner-up, or best third-place candidate pool.

## Acceptance
- Game 1 uses the shared pixel-native board.
- Every R32 slot displays its short rule label.
- Tapping a slot opens the group/team menu filtered by that slot.
- Third-place slots expose only candidate groups for that slot.
- `make verify` and `make pack` pass.
