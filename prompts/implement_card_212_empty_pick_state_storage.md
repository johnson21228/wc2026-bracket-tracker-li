# Prompt: Implement Card 212 Empty Pick-State Local Storage

Use this prompt after the empty pick-state storage LI refinement is committed.

## Goal

Implement Card 212 so the current local/static Bracketeering Pub site initializes, saves, loads, and exports a complete canonical pick-state document while preserving current local play.

## Constraints

- Do not add Supabase or remote storage in this card.
- Do not add login UI in this card.
- Preserve current localStorage behavior or migrate it safely.
- Keep the site running at every step.
- Game 1 must initialize 64 required slots.
- Game 2 must initialize 32 required slots.
- Empty slots must be explicit.
- Champion and third-place winner must be explicit required slots.
- `make verify` and `make pack` must pass.

## Expected result

The site remains local-only but now uses the same complete pick-state storage document that the future server will store.
