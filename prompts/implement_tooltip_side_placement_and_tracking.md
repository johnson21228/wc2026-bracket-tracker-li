# Implement Tooltip Side Placement and Tracking

Patch the World Cup bracket UI so tooltips do not cover the underlying pick.

Use the governing rule:

- `li/world_cup/tooltip_side_placement_and_tracking_rule.md`

Implement side placement where possible.

If tooltip content is clickable, preserve the tooltip while the pointer/touch moves from the pick into the tooltip.

Do not introduce arbitrary floating behavior. Tooltip placement should remain visually attached to the bracket pick and should respect board boundaries.

After implementation, provide:

- changed files
- manual test notes
- verify output
- pack output
