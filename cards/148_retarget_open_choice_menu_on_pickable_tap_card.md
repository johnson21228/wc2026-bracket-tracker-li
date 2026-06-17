# Card 148 — Retarget Open Choice Menu on Pickable Tap

## Intent
When a choice menu is already open, tapping another pickable bracket item should close/supersede the old menu and open the newly tapped item's menu from the same tap.

## Rule
A tap on another pickable item is not merely an outside-tap close. It is a retarget operation.

## Acceptance
- Tap item A: menu opens for A.
- Tap item B while A's menu is open: menu opens for B without requiring a second tap.
- New menu remains board-attached and adjacent to the new item.
- Selection still closes and saves.
- Outside non-pickable tap may still close.
