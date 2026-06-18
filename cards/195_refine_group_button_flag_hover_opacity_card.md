# Card 195: Refine Group Button Flag Hover Opacity

## Problem

The group rail tile itself becomes fully opaque on interaction, but the flags inside the tile also need their own clear interaction affordance.

## Decision

Flags inside a group rail tile remain somewhat translucent at rest and become fully opaque when the tile is hovered, focused, active, or otherwise marked active.

## Boundary

CSS-only runtime change. No controller/model/pick/panel-placement behavior changes.
