# Lifecycle Stage Presentation-Only Rule

Lifecycle stage is presentation-only for picking and rendering.

Pick availability is determined only by precedent availability.

The selected stage may change the Group Stage background, Knockout Stage background, and rules/help/status copy. The selected stage must not disable pick cells, change bracket rendering rules, change pick highlighting rules, or block pick pre-selection.

A pick cell is selectable when the upstream team/candidate inputs needed for that pick exist. Empty downstream picks may remain unavailable only because their precedent is missing, not because the selected stage is Group Stage or Knockout Stage.

Legacy game-1/game-2 hooks may remain during migration, but they must be treated as presentation hooks, not gameplay gates.


Lifecycle presentation-only gameplay invariant:

- lifecycle stage is presentation-only
- selected stage must not change bracket rendering rules
- selected stage must not change pick highlighting rules
- selected stage must not block pick pre-selection
- pick availability is determined only by precedent availability
- Group Stage background may still use pub_background_game1
- Knockout Stage background may still use knockout_pub_background

