# LI Rule — Prevent Duplicate R32 Menu Assignments

For any R32 assignment menu, including third-place candidate menus:

- Compute `usedTeamCodes` from current R32 assignments.
- Exclude the slot currently being edited from `usedTeamCodes`.
- Hide or disable any candidate whose team code is already in `usedTeamCodes`.
- Reject duplicate selections defensively before the pick is written.
- Do not apply this rule to knockout advancement picks where the same team naturally appears downstream after advancing.

The canonical model is:

```text
availableCandidates(slot) = baseCandidates(slot) - assignedTeams(otherR32Slots)
```

The current slot's assigned team is allowed while editing that slot.
