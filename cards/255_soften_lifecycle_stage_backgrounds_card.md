# Card 255: Soften lifecycle-stage backgrounds

## Status

Done.

## Problem

The Group Stage and Knockout Stage background images were too visually dominant behind bracket cells and floating surfaces.

## Decision

Use a shared CSS-only opacity adjustment on `.board-background-layer`.

## Acceptance

- Group Stage background is softer.
- Knockout Stage background is softer.
- Stage switching remains presentation-only.
- Pick menus, including R16 menus, remain stage-independent.
- No gameplay, storage, scoring, or image-asset changes.

## Verification

- `python3 tools/verify_wc2026_lifecycle_background_softening.py`
- `make verify`
- `make pack`
