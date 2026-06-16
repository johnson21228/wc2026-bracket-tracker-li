# R32 Projection Until FIFA Lock

The all-inclusive game has two R32 realities.

## Projection phase

Before FIFA assigns the official Round of 32 bracket, every R32 cell is a projected assignment.

During projection:

- R32 cells can be assigned.
- R32 cells can be changed.
- R32 cells can be cleared.
- Downstream winner picks are provisional.
- Clearing/changing R32 must clear invalid downstream picks.

## Official phase

After FIFA assigns the official Round of 32 bracket, R32 cells become fixed source data.

During official phase:

- R32 cells are not user-editable assignment choices.
- R32 cells are official bracket occupants.
- User interaction focuses on picking winners.
- Downstream choices derive from official source slots.

## Site state

The site stores the phase in:

```text
wc2026.game1.r32.assignmentState
```

Default:

```json
{
  "state": "projection",
  "locked": false,
  "source": null,
  "label": "R32 projection: editable until FIFA lock"
}
```

Official lock:

```json
{
  "state": "official",
  "locked": true,
  "source": "fifa",
  "label": "Official FIFA R32: locked"
}
```
