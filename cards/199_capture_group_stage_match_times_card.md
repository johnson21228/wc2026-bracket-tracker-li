# Card 199 — Capture full group-stage match times

## Intent

Fill the 72-match group-stage data model with explicit published kickoff times so group panel rows do not fall back to `Time TBD`.

## Acceptance

- All 72 group-stage matches in runtime/current data have kickoff fields.
- Poster-derived fixture models are enriched with the same time evidence.
- The evidence source is captured in `source/text/`.
- A verifier protects the 72-match count and visible late-group fixtures.
