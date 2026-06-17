# Bracket Pick Finality Validation

The all-inclusive Game 1 surface needs to distinguish a stored pick from a pick that is still valid as a final choice.

A team can appear across multiple rounds only when it is advancing along one connected path. The same team cannot occupy multiple independent R32 source slots.

Validation functions:

- `window.WC2026_VALIDATE_BRACKET_PICK_FINALITY(slotId)`
- `window.WC2026_VALIDATE_ALL_BRACKET_PICK_FINALITY()`
- `window.WC2026_MARK_BRACKET_PICK_FINALITY()`

Rendered cards are marked with observed state:

- `data-choice-can-remain-final="true|false"`
- `data-choice-state="finalizable|invalid-finality|empty"`
- `data-choice-finality-reason="..."`

This does not automatically clear invalid picks. It observes whether the pick is allowed to remain final.
