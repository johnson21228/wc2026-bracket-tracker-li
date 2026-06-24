# R32 Pick Validity Hue Rendering

Picked R32 cells should visually communicate whether the pick is currently valid against the current group standings.

## Rule

- Valid picked R32 cells use a green filled-cell hue.
- Invalid picked R32 cells use a red filled-cell hue.
- The hue is attached to the filled pick rendering, not to the bracket frame.

## Group Stage suppression boundary

When a later-round cell is frame-only suppressed during Group Stage, it must not show red or green validity fill. The frame-only state remains visually quiet.

This preserves the distinction between:
- R32 filled pick cells, which can show validity state
- R16+ Group Stage frame-only cells, which should not advertise future-round picks or validity


## Fill requirement

The validity hue must be visible in the picked cell fill, not just the outline. A valid R32 pick should read as green-filled; an invalid R32 pick should read as red-filled.


The fill color is required for R32 validity hue rendering.
