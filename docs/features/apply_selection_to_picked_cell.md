# Apply Selection to Picked Cell

The knockout choice menu is not a general team picker. It is an assignment surface for the bracket cell that opened it.

## Interaction Contract

1. User taps a bracket cell.
2. The menu opens adjacent to that cell.
3. The menu records that cell as its assignment target.
4. User selects a team.
5. The selected team is written to the target cell's storage.
6. The bracket pick layer re-renders.
7. The menu closes.

## Storage Contract

- R16 cell selections are stored in `r16Picks`.
- Later knockout cell selections are stored in `advancementPicks`.
- Every stored value includes `assignedSlotId` and `assignmentTargetSlotId`.

This makes the assignment auditable and prevents the menu from becoming detached from the bracket cell it is supposed to fill.
