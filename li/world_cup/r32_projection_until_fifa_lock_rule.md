# LI Rule: R32 Projection Until FIFA Lock

## Rule

Round of 32 assignment cells are editable projections until an explicit FIFA R32 lock state makes them official.

## Invariant

R32 is not immutable until the R32 lock state is official.

## Consequences

Before official lock:

- R32 picks are projected assignments.
- R32 picks may be cleared or changed.
- Downstream R16/QF/SF/final picks are provisional.
- Clearing or changing an upstream slot clears downstream dependent picks.

After official lock:

- R32 cells become official source data.
- R32 user assignment controls are disabled or changed to read-only.
- Winner picking continues from the official R32 bracket.

## Naming

Use `projectedR32Assignments` for user-authored pre-lock occupants.
Use `officialR32Assignments` for FIFA-authored post-lock occupants.
