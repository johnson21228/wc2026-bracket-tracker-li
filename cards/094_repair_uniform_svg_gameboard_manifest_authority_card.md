# Card 094 — Repair Uniform SVG Gameboard Manifest Authority

## Intent

Align the uniform SVG gameboard LI, manifest, generator, and verifier with the actual board model: one SVG geometry authority, one derived manifest, one derived PNG, and 61 pick-card records.

## Why

The first authority CB correctly introduced the asset family, but the verifier used generic 63-slot tournament math. The reviewed board intentionally uses one special center Final Four pick card instead of two finalist cards plus a champion card.

## Acceptance

- SVG remains the source-truth geometry artifact.
- Manifest bounds match the SVG pick-card rectangles.
- Verifier expects the current board model counts: R32 32, R16 16, QF 8, SF 4, FINAL_FOUR 1.
- Game 1 and Game 2 are not migrated yet.
