# Capture Back: Pages-Owned Board Zoom-Out Scale

## Intent

Capture the reversible architecture decision for making the Bracketeering gameboard zoom out without changing durable data, slot geometry, or Supabase persistence.

## Decision

The Pages site owns all View and Controller behavior. Board zoom is View/Controller behavior and must remain inside the Pages site.

Supabase/Postgres must not know about board zoom. Supabase stores durable model state only.

## Rule

```text
All board actors speak native gameboard coordinates.
Only the Pages View shell converts native coordinates to rendered screen coordinates.
```

## Why this is safe

The gameboard already has a native coordinate system. The zoom-out change should preserve that system and add a render-scale layer around it.

Native board truth remains stable:

- slot IDs do not change
- pick IDs do not change
- geometry manifests do not change
- stored pick JSON does not change
- Supabase SQL/RLS does not change

The View may render the board at smaller scales such as 75% or 50%, but the runtime model and controller intent continue to use native board coordinates.

## Desired implementation shape

Future implementation should add a board render scale owned by the Pages site, for example:

```text
50% | 75% | 100% | 125% | 150% | Fit
```

At each scale:

- native geometry remains the authority
- visible board dimensions are derived from native size × render scale
- pointer coordinates are converted from rendered coordinates back to native board coordinates
- menu and panel anchors convert native coordinates to rendered screen positions
- storage and persistence remain unchanged

## Backout posture

This should be one isolated View-layer feature commit. Backout should be a normal `git revert` of the zoom feature commit.

No durable data migration should be required.
