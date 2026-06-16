# R32 Pick Card Rendering and Tooltips

This feature captures the user-facing rendering rule for filled Round of 32 pick cards.

The visible card should stay simple: a large flag and a team name. Rule codes such as `2A` may exist as secondary metadata, but should not dominate the card. Printed or overlaid source slot labels should not show through filled cards in a confusing way.

Extended information belongs in a tooltip/details surface. For Game 1 this includes the slot rule, qualification path, eligible group source, and the action hint that the card can be clicked/tapped to change the pick.

This keeps the board readable while preserving the LI explanation needed to understand why a team is eligible for a specific R32 slot.
