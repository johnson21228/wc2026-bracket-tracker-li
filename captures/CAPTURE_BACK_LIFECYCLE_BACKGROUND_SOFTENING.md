# Capture Back: Lifecycle Background Softening

## Intent

Reduce the visual dominance of both Bracketeering Hub lifecycle-stage background images.

## Change

The shared `.board-background-layer` opacity is reduced from `.72` to `.48`.

Because both Group Stage and Knockout Stage use the same board background layer, both presentation backgrounds receive the same softening behavior.

## Invariants

- Lifecycle stage remains presentation-only.
- Stage switching still controls background/rules presentation only.
- R16/R32/QF/SF/final pickability is unchanged.
- Pick menus remain stage-independent.
- Preselection remains stage-independent.
- No image assets were changed.
- No storage or scoring behavior was changed.

## Verification

- `tools/verify_wc2026_lifecycle_background_softening.py`
- existing lifecycle-stage presentation-only verifiers
- existing background verifiers
- `make verify`
- `make pack`
