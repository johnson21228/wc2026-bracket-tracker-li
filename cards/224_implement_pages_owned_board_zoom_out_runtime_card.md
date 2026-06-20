# Card 224: Implement Pages-owned board zoom-out runtime

## Goal

Allow the Bracketeering Pub board to zoom out below native size without changing the native board coordinate system.

## Acceptance

- The app has a board zoom control with 50%, 75%, 100%, and 125%.
- The board is wrapped in a render-scale frame.
- The native board plane remains 1536×1024.
- Render scale uses CSS transform on the native plane and explicit frame dimensions for layout.
- Menu and group-panel placement convert rendered scroll bounds back to native board coordinates.
- The hero title is restored to `Bracketeering Pub`.
- `make verify` passes.

## Safety

No Supabase SQL, pick storage, pick IDs, game model data, or geometry manifests are changed.
