# Pick validity must not treat current group rank as a conflict

Card 208 defines the boundary between a user's bracket pick and the current group standings snapshot.

A group-stage ranking is evidence for context, not a reason to mark a preserved pick invalid by itself. A player may intentionally choose any team offered by the slot's source scope even when the current standings snapshot places that team in a different rank than the bracket source label.

## Rule

- The picker remains source-scoped: a slot still only offers teams from its encoded group or candidate group set.
- The application must preserve user picks that are valid team identifiers for a known slot.
- Current group rank, such as first or second in a standings snapshot, must not be used as an invalid-pick warning by itself.
- The red invalid-pick warning is reserved for structural conflicts such as duplicate Round-of-32 assignments, unknown team identifiers, or teams outside the slot's source scope.
- Standings remain visible in group panels and may inform the user's judgment, but they do not silently override or shame the user's projected pick.

## Rationale

This is a prediction game. A user may disagree with the current projection or may be making a what-if bracket while group play is still moving. The app should make the current group context visible without converting every disagreement with the current table into a red error.
