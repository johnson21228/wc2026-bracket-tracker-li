# Bracket Visual Alignment Rule

## Purpose

The knockout bracket should visually communicate how each later-round slot derives from earlier-round source matches.

The layout should not use arbitrary vertical placement that makes later-round slots feel disconnected.

## Alignment principle

Each later-round slot should be vertically centered relative to the source matches that feed it.

```text
R16 slot = centered between its two R32 source winners
QF slot  = centered between its two R16 source winners
SF slot  = centered between its two QF source winners
Final    = centered between its two SF source winners
Champion = centered from final winner
```

## Source mapping

Every later-round slot should have source references.

Example:

```json
{
  "slotId": "R16-L-S1",
  "sourceSlots": ["R32-L-M1A", "R32-L-M1B", "R32-L-M2A", "R32-L-M2B"],
  "sourceMatches": ["R32-L-M1", "R32-L-M2"]
}
```

## UI rule

The bracket should make it visually clear that:

```text
R32-M1 + R32-M2 feed R16-S1
R16-S1 + R16-S2 feed QF-S1
QF-S1 + QF-S2 feed SF-S1
SF-L + SF-R feed Final
```

## Implementation guidance

Avoid hard-coded arbitrary spacer heights when they produce visual drift.

Prefer a layout model where each round is positioned from the source match tree.

Acceptable first implementation:

- use CSS grid/flex with calculated vertical gaps
- represent each match as a fixed-height block
- center later-round slots over the combined height of their source block

## Screenshot rule

The bracket should be readable in a screenshot so that the source path from R32 to Champion is visually recoverable.
