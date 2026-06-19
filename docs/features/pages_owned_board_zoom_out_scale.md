# Pages-Owned Board Zoom-Out Scale

## Purpose

The gameboard should be able to zoom out for overview use without rewriting the board coordinate system.

This is a Pages site View/Controller feature, not a storage or backend feature.

## Coordinate invariant

The board has native geometry. That native geometry is the authority for slots, hit targets, pick cards, menu anchors, group panels, and board layers.

```text
native board coordinate -> View render scale -> browser pixels
browser pixels -> View inverse scale -> native board coordinate
```

All board actors should keep using native gameboard coordinates. The View shell owns the conversion to and from rendered pixels.

## Why zoom-in currently works

Zoom-in is easy when the browser is effectively scrolling a fixed native board plane. The board can be larger than the viewport, and scroll exposes more of it.

Zoom-out requires an explicit render scale below `1.0` because the layout can no longer assume native board pixels equal rendered browser pixels.

## Safe implementation model

A safe implementation introduces one render-scale concept in the Pages site:

```text
boardScale = 1.0
boardScale = 0.75
boardScale = 0.5
```

The native board dimensions remain unchanged. The rendered board dimensions are derived from native dimensions times the scale.

Example:

```text
native:   1536 x 1024
75% view: 1152 x 768
50% view: 768 x 512
```

## Scope boundary

Zoom-out should not touch durable data:

- no Supabase SQL changes
- no RLS changes
- no `picks_json` changes
- no slot ID changes
- no pick ID changes
- no geometry-manifest rewrite for scaled coordinates

The Pages site owns the zoom control, hit testing conversion, and overlay placement conversion.

## Rollback

Keep this as one isolated implementation commit. Rollback should be:

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li

git revert <zoom-commit-sha>
make verify
make pack
```
