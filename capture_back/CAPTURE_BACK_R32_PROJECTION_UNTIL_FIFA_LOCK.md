# Capture Back: R32 Projection Until FIFA Lock

## User intent

The all-inclusive game must not treat Round of 32 assignments as fixed source truth until FIFA officially assigns the Round of 32 bracket.

Before the FIFA assignment lock, R32 cells are editable projected assignments. They can be changed or cleared. Downstream winner picks are provisional and must be invalidated when their upstream projected R32 assignment changes or disappears.

After the FIFA assignment lock, R32 cells become official source data. User interaction moves from assigning R32 occupants to picking winners from the official bracket.

## Captured rule

R32 is not immutable until the R32 lock state is official.

## Storage reality

The site needs a phase/state object, not an implicit assumption:

```json
{
  "r32State": "projection",
  "r32Locked": false,
  "r32LockSource": null,
  "r32LockLabel": "R32 projection: editable until FIFA lock"
}
```

After FIFA lock:

```json
{
  "r32State": "official",
  "r32Locked": true,
  "r32LockSource": "fifa",
  "r32LockLabel": "Official FIFA R32: locked"
}
```

## Product consequence

- Before lock: R32 choices are editable projections.
- Before lock: R32 clear/change must clear dependent downstream picks.
- After lock: R32 slots are official, fixed source assignments.
- After lock: users pick R16/QF/SF/final winners, not R32 occupants.
