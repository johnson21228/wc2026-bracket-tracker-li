# Tooltip Side Placement and Tracking Rule

A World Cup bracket tooltip must not hide the bracket pick it explains.

The tooltip is an explanatory layer, not the primary selection surface.

## Rule

Place tooltip content beside the target pick whenever possible.

If the tooltip has clickable content, the pointer/touch active region must include both:

1. the original bracket pick target
2. the tooltip surface

The tooltip must not dismiss merely because the pointer moved from the pick toward the tooltip.

## Invariant

The user must be able to see the underlying pick while reading or interacting with the tooltip.
