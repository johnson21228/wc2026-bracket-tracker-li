# Capture Back: Pages-Owned Board Zoom-Out Runtime

## Intent

Implement the previously captured Pages-owned board zoom-out scale plan.

## Runtime change

The public Pages View now owns a board render scale while preserving the native 1536×1024 board coordinate system.

## Contract

- Board geometry remains native.
- Pick slots, menus, and group panels continue to use native board coordinates.
- The View converts rendered scroll geometry back to native coordinates for placement.
- The rendered board can be viewed at 50%, 75%, 100%, or 125%.
- Supabase, pick IDs, model storage, and geometry manifests are not changed.

## Title cleanup

The temporary lowercase publish marker is reverted to `Bracketeering Pub`.
