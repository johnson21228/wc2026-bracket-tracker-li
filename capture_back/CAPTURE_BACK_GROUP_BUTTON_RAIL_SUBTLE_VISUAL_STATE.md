# Capture Back: Group Button Rail Subtle Visual State

## Intent

Refine the group button rail so the group buttons are visible but quiet while at rest, then become fully opaque when the user hovers, focuses, touches, or otherwise tracks over them.

## Scope

This capture back is intentionally limited to the group rail visual emphasis rule.

It does **not** change group panel placement, controller wiring, view event routing, group panel anchoring, pick menu behavior, data storage, or match evidence rendering.

## Runtime contract

- Group rail buttons are partially translucent at rest.
- Group rail buttons become fully opaque on hover, focus-visible, active, or `.is-active` state.
- Active visual emphasis may strengthen background, border, shadow, or saturation.
- Active visual emphasis must not change tile size, group order, flag grid layout, or rail position.
- The 2×2 flag grid remains readable at rest and active.

## Files

- `li/world_cup/group_button_rail_rule.md`
- `docs/features/group_button_rail.md`
- `site/css/board.css`
- `tools/verify_wc2026_group_button_rail_subtle_visual_state.py`
- `cards/193_refine_group_button_rail_subtle_visual_state_card.md`
