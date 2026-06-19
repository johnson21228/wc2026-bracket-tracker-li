# Card 212: Route Local Storage Through Canonical Pick State

## Intent

Make localStorage the first implementation of the canonical user bracket storage model.

## Scope

- Preserve current anonymous/local play behavior.
- Normalize current picks into canonical `picksBySlot` JSON.
- Hydrate the site from canonical JSON.
- Keep export/import behavior compatible with the canonical shape.

## Acceptance

- The site still runs without login or backend.
- Local picks save and reload through the canonical shape.
- Game 1 can represent 64 picks.
- Game 2 can represent 32 picks.
- Third-place winner can be represented as a first-class stored slot.
- `make verify` and `make pack` pass.
