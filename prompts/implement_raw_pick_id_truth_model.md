# Prompt: Implement Raw Pick ID Truth Model

Use this prompt for the next implementation pass after the raw pick ID truth model is captured.

## Instruction

Inspect the current repository storage and projection model. Add a canonical raw pick ID manifest that separates durable pick identity from visual board projection.

## Requirements

- Add `site/data/model/canonical_pick_ids.json`.
- Define 64 stable raw pick IDs for Game 1.
- Define 32 stable raw pick IDs for Game 2.
- Keep `bracket_slots.json` as projection/UI geometry authority.
- Add a projection mapping only where needed.
- Make empty pick state initialize from raw pick IDs, not from board geometry.
- Preserve current local/static site behavior.
- Add a verifier that proves raw pick IDs are unique, stable-looking, count-correct, and not geometry-derived.

## Invariant

```text
pickId is truth.
visual slot is projection.
UI geometry may change.
pickId must not change.
```
