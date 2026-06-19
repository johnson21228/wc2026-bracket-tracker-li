# Card 223: Add Pages-Owned Board Zoom-Out Scale

## Intent

Allow the Bracketeering gameboard to zoom out while keeping native board geometry and durable pick data unchanged.

## Product rule

```text
All View and Controller work stays inside the Pages site.
Supabase is durable Model persistence only.
```

## Architecture rule

```text
All board actors speak native gameboard coordinates.
Only the Pages View shell converts native coordinates to rendered screen coordinates.
```

## Scope

- Add or confirm one Pages-owned board render scale concept.
- Allow board display scale below `1.0`, such as `0.75` and `0.5`.
- Keep source board geometry in native coordinates.
- Keep pick targets, menu anchors, and group-panel anchors aligned at every supported scale.
- Keep controller intent expressed as slot IDs, pick IDs, and native board coordinates.
- Keep stored pick state unchanged.

## Non-scope

- Do not change Supabase SQL.
- Do not change `picks_json` contract.
- Do not change slot IDs or pick IDs.
- Do not rewrite geometry manifests for 50% or 75% sizes.
- Do not move View/Controller behavior into Supabase.

## Expected touched area

Likely implementation files:

- `site/css/board.css`
- `site/js/board/BoardShell.js`
- `site/js/mvc/view.js`
- optionally `site/js/board/R32PickMenuLayer.js`
- optionally `site/js/dev/DeveloperFrame.js`

Expected verification:

- add/update a verifier that proves board zoom-out is Pages-owned
- prove native geometry authority is preserved
- prove storage/model/Supabase files are not part of the zoom-out feature

## Acceptance

- Board can render below 100% without changing native geometry truth.
- Pick buttons remain aligned with native board slots at zoom-out scales.
- Pick menus remain anchored to selected slots at zoom-out scales.
- Group panels remain anchored/clamped correctly at zoom-out scales.
- Stored bracket data remains slot/pick model data, not screen-pixel data.
- Supabase/model persistence files remain unchanged by zoom-out implementation.
- The feature can be backed out with a single revert commit.
