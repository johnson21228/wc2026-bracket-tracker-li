# Card 128: Short-Term R16 Hardcoded Hold

## Claim

Game 1 should temporarily hard-code one selected R32 winner into one R16 cell to prove R16 storage/rendering works.

## Target

- Source aliases: `L-R32-01`, `R32-L-M1A`
- Target: `L-R16-01`

## Acceptance

- Source R32 pick is found.
- `r16Picks["L-R16-01"]` is written.
- The R16 pick card renders.
- The value survives refresh through localStorage.
