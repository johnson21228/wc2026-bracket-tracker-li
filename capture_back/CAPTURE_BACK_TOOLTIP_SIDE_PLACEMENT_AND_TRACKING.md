# Capture Back: Tooltip Side Placement and Tracking

## Summary

Bracket tooltips should not cover the underlying pick, slot, flag, or selectable bracket item they explain.

A tooltip that appears directly on top of the target creates a perception and interaction problem: the user loses sight of the thing they are trying to understand or choose.

## Decision

Move bracket tooltips to the side of the underlying pick whenever space allows.

The tooltip should be visually associated with the pick, but should not obscure the pick.

## Interaction Rule

If the tooltip contains a clickable target, pointer/touch tracking must allow the user to move from the pick into the tooltip without dismissing it prematurely.

The active hover/tap region should include:

- the underlying pick target
- the tooltip surface
- any intentional bridge/gap region needed to move between them

## Boundary

This card does not implement tooltip runtime code.

It defines the product and LI rule for the next patch.
