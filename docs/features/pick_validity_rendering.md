# Pick Validity Rendering

The bracket preserves a user's pick even when current standings or feeder paths make that pick invalid.

A filled pick cell stays visible as a compact identity token. When the model judges the pick invalid, the view adds a thin red outline and a red `!` badge. The warning is a rendering layer over preserved user intent.

## Why

Tournament data changes. A pick that made sense before a standings refresh may no longer match the current group order. The site should not silently delete that choice. It should make the problem visible so the user can decide what to repair.

## First runtime behavior

- The model computes `slot.pickValidity` for each slot view model.
- The view adds `.has-invalid-pick` to invalid picked cells.
- The view renders `.picked-cell-warning` with `!` inside the picked identity.
- The warning reason is exposed through `title` and ARIA labeling when available.
- The model no longer auto-clears invalid descendant picks by default.

## Acceptance

- Invalid picks are preserved in storage and visible on the board.
- Invalid picks receive a thin red outline.
- Invalid picks receive a red `!` marker.
- Valid picks keep the normal compact flag/code rendering.
- The pick renderer is the warning surface; the picker is not the only enforcement layer.
