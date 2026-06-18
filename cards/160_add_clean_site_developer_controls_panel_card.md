# Card 160 — Add clean site developer controls panel

## Intent

Add a developer controls panel below the clean board surface so the rebuild can make layer state and module failures visible.

The panel must help answer:

- Is the app mount present?
- Did the board shell render?
- Is the background layer present?
- Which board truth resources are configured?
- Which layers are currently visible?

## Controls

Initial controls:

- Show background
- Show SVG gameboard placeholder state
- Show pick IDs placeholder state

Only the background layer exists in this card. SVG and pick IDs are intentionally reported as pending layers.

## Boundary

This card does not add:

- SVG rendering
- pick rendering
- menu behavior
- model state
- localStorage

## Acceptance

- A developer controls panel renders below the board.
- The panel shows configured board truth resources.
- The panel can toggle the background layer visibility.
- Pending controls for SVG and pick IDs are visible but disabled.
- `tools/verify_wc2026_developer_controls_panel.py` passes.
