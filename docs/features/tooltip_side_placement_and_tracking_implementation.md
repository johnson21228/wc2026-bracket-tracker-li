# Tooltip Side Placement and Tracking Implementation

Game 1 now includes a side-placement tooltip layer.

The layer creates a single floating tooltip element and positions it beside the active pick. It favors side placement and falls back to bounded viewport placement when there is not enough room.

## Tracking Model

The active tooltip region includes:

- the original pick target
- the tooltip surface
- a small bridge region between them

This allows users to move into clickable tooltip content without premature dismissal.

## Clickable Tooltip Actions

A pick may expose an action through:

    data-tooltip-action-href
    data-tooltip-action-label

The tooltip remains open while the pointer moves from the pick into the tooltip.
