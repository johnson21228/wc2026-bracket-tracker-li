# Card 135: Define bracket pick finality validation

## Intent

A stored pick should be able to answer whether it can remain final given the entire bracket graph.

## Rule

A stored pick is finalizable only if the same team appears in exactly one independent bracket source path. A team may appear in multiple rounds only when it is advancing along the same connected path.

## Acceptance

- The browser exposes `window.WC2026_VALIDATE_BRACKET_PICK_FINALITY(slotId)`.
- The browser exposes `window.WC2026_VALIDATE_ALL_BRACKET_PICK_FINALITY()`.
- Rendered pick cards receive `data-choice-can-remain-final`, `data-choice-state`, and `data-choice-finality-reason`.
- Duplicate independent R32 placement invalidates affected picks.
- Downstream picks with missing or unreachable feeder picks are invalid.
