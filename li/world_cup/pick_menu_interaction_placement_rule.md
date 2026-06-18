# Pick Menu Interaction and Placement Rule

## Rule

A pick menu is a bracket-attached interaction surface. It must make pick state, source evidence, menu closure, and clear-pick behavior visible and reliable.

## Clear existing pick

When the selected bracket slot already has a pick, the pick menu must show a clear-pick action near the top of the menu.

The clear action must be visually distinct from team-choice actions and must not be hidden below long group/team lists.

Recommended placement:

1. Menu title / source title
2. Current pick summary
3. Clear pick action
4. Group source labels / group panel links
5. Candidate team choices

The clear-pick action clears the current slot pick through the model. If clearing the pick invalidates downstream picks, the model owns downstream invalidation and cascade clearing. The view may explain that downstream picks were cleared, but must not compute the cascade itself.

## Prominent close button

Every pick menu must include a prominent close button near the top edge of the menu.

The close button must close the menu without selecting a team, clearing a pick, opening a group panel, or mutating bracket state.

The menu may also close through outside-click or escape-key behavior, but those are secondary conveniences. The visible close button is required.

## Bracket-attached placement

A pick menu must be displayed next to the bracket slot that opened it.

The menu should feel attached to the slot, not detached into a global modal or distant panel.

The menu placement should prefer the side of the slot with the most available visible space. If the preferred placement would clip off the visible scrollable board area, the view must shift the menu up, down, left, or right so the full menu remains exposed.

## Scroll behavior

The pick menu belongs to the scrollable game board plane.

When the game board scrolls, the pick menu must scrolls with the game board and remain anchored to its source slot.

The menu must not be fixed to the browser viewport in a way that visually detaches it from the board slot.

## Clipping prevention

The menu must remain fully visible within the current visible board viewport whenever possible.

The view owns placement calculation and clipping avoidance. The model provides slot geometry, menu content, and pick state. The controller opens, closes, clears, and selects, but does not hardcode placement math or source labels.

## Group evidence links

When candidate choices are grouped by source group, each group label must remain visible and clickable as a group-panel evidence link.

Clicking a group label opens the group panel for that group. It must not select a team, clear a pick, close the menu unless the implementation intentionally opens the panel in the same surface, or mutate bracket state.

## MVC responsibility

Model owns:

- current pick
- whether clear-pick is available
- source title
- grouped candidate choices
- downstream invalidation rules
- group panel source references

View owns:

- menu rendering
- close button rendering
- clear-pick button rendering
- bracket-attached placement
- clipping avoidance within the scrollable board
- scrolling with the board plane

Controller owns:

- open menu for slot
- close menu
- clear pick action
- team choice action
- group panel open action

## Anti-patterns

Do not:

- hide clear-pick below a long candidate list
- make the user pick another team as the only way to replace a pick
- render close as a tiny or implicit-only affordance
- display the menu as a detached global modal
- fix the menu to the browser viewport while the board scrolls underneath it
- allow group-label clicks to select teams or clear picks
- compute source labels, eligibility, or cascade clearing in the view
