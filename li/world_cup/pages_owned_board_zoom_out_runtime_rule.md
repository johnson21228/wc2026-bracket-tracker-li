# Pages-Owned Board Zoom-Out Runtime Rule

The Pages View may scale the board for display, but all logical board actors speak native board coordinates.

Rules:

- Native board geometry remains 1536×1024.
- Render scale is View-owned.
- Pick slots and model data must not be rewritten for scale.
- Menus and group panels must convert rendered browser measurements back to native board coordinates.
- Supabase SQL, durable pick storage, pick IDs, and geometry manifests are out of scope.
