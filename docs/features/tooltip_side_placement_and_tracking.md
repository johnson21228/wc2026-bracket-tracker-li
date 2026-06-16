# Tooltip Side Placement and Tracking

The bracket UI should avoid covering the thing being explained.

A tooltip is a support layer. It should not become an occluding layer over the pick, slot, flag, or bracket item.

## Desired Placement

Default placement:

    pick / slot  ->  tooltip to the side

The tooltip may appear to the right, left, above, or below depending on available board space, but the first preference is side placement that preserves visibility of the pick.

## Interactive Tooltip Tracking

If the tooltip contains a clickable target, the active interaction area must include both the original pick and the tooltip.

This prevents the tooltip from disappearing while the user is moving toward a button, menu item, or link inside the tooltip.

## Dismissal

The tooltip may dismiss when:

- pointer leaves both the pick and tooltip region
- user taps elsewhere
- user makes a pick
- escape/cancel is invoked

## Small Screen Fallback

If no side placement is possible, the tooltip should use the least-occluding placement and preserve enough visibility to keep the pick understandable.
