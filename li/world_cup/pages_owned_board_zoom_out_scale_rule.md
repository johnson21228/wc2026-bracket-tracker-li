# Pages-Owned Board Zoom-Out Scale Rule

Board zoom is Pages site View/Controller behavior.

Supabase/Postgres must not own or influence board zoom.

## Rule

```text
All board actors speak native gameboard coordinates.
Only the Pages View shell converts native coordinates to rendered screen coordinates.
```

## Requirements

- Native geometry remains the authority.
- Zoom scale is a render concern.
- Pointer coordinates entering the controller are converted back to native board coordinates.
- Menu and panel anchors are derived from native coordinates, then rendered through the current scale.
- Durable pick state remains slot/pick data, not screen-pixel data.
- Supabase stores durable model data only and does not know about board zoom.

## Backout invariant

The zoom-out feature must be isolated enough to revert without data migration or backend changes.
