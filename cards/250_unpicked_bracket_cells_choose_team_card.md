# Card 250: Render unpicked bracket cells as Choose Team

## Status

Implemented.

## Change

Empty/unpicked bracket cells render:

`Choose Team`

The text is centered in the cell using the existing unpicked-cell label path.

## Guardrail

Do not reintroduce internal slot IDs, source labels, or fallback slot identifiers into visible unpicked bracket cells.
