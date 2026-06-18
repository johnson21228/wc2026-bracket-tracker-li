# Pick Menu Interaction and Placement

The pick menu should behave like part of the bracket board, not like a generic detached modal.

## User-facing behavior

When a user taps a pick slot, the menu opens next to that slot. The user should immediately understand:

- what source/rank/path they are choosing from
- what their current pick is, when one already exists
- how to clear the current pick
- how to close the menu without changing anything
- which group evidence can be opened from the grouped source labels
- which team choices are valid

## Clear pick

If the slot already has a pick, the menu shows a clear-pick action near the top. This must be above long lists of group/team candidates so clearing is always easy to find.

Clearing a pick goes through the model. If downstream picks become invalid, the model owns the cascade.

## Close button

The menu must include a prominent close button near the top edge. Outside-click and escape-key support may exist, but they do not replace the visible close affordance.

## Board-attached placement

The menu should be placed beside the slot that opened it. It should be shifted as needed to stay fully visible in the scrollable board viewport.

Because the menu belongs to the board plane, it scrolls with the board instead of staying fixed to the browser viewport.

## Group panel links

When choices are grouped by source group, the group label is clickable. The click opens the group panel for that group as evidence/context. It must not also select a team or clear a pick.

## Implementation boundary

The model supplies pick state, source title, clear-pick availability, grouped choices, group-panel references, and cascade rules.

The view renders the menu and computes board-attached placement/clipping behavior.

The controller wires open, close, clear, select, and group-panel actions.
