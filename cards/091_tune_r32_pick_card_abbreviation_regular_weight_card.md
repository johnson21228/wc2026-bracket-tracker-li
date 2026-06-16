# Card 091 — Tune R32 Pick Card Abbreviation Regular Weight

## Intent

The R32 pick card abbreviation should not be bold. It should use the same calm, regular-weight metrics on every filled R32 card.

## Change

- Add LI for regular-weight abbreviation rendering.
- Patch Game 1 R32 pick-card abbreviation CSS away from heavy/bold values.
- Preserve flag + abbreviation compact-card structure.
- Preserve tooltip/details full-name behavior.

## Acceptance

- Filled R32 pick cards show the team abbreviation.
- The abbreviation is not bold/heavy.
- Every R32 pick card uses the same abbreviation style.
- Existing pick state and tooltip behavior still work.
