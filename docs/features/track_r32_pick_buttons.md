# Track R32 pick buttons

The R32 pick menu layer renders a DOM button for every FIFA R32 slot that has both logic and geometry.

Each button exposes:

```text
.r32-pick-slot-button
```

The button dataset includes:

```text
fifaSlotId
fifaLabel
geometrySlotId
qualifierKind
eligibleGroups
candidateCount
pickEnabled
pickability
preselectState
```

The layer dataset includes last-tracked button state:

```text
r32TrackedPhase
r32TrackedFifaSlotId
r32TrackedFifaLabel
r32TrackedCandidateCount
r32TrackedPickability
```

The page dispatches:

```text
wc2026:r32PickButtonTracked
```

on hover/focus/click/clear.

The click still routes through `Game1R32PickController` for menu legality and selection persistence.
