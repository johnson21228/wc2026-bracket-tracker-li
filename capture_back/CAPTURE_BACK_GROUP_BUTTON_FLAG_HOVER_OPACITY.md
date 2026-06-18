# Capture Back: Group Button Flag Hover Opacity

## Intent

Group button rail flags should be visually present but quiet at rest. When the user hovers, focuses, touches, or otherwise tracks over a group tile, the flags inside that tile should become fully opaque.

## Boundary

This CB is CSS/LI only. It does not change group panel anchoring, pick state, group data, controller wiring, or model behavior.

## Runtime contract

- `.group-rail-flag` has a translucent default opacity.
- `.group-rail-tile:hover .group-rail-flag` becomes fully opaque.
- `.group-rail-tile:focus-visible .group-rail-flag` becomes fully opaque.
- `.group-rail-tile:active .group-rail-flag` becomes fully opaque.
- `.group-rail-tile.is-active .group-rail-flag` becomes fully opaque.
