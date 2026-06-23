# Capture Back: Pick Slot Button Label Centering

## Problem

Some pick-slot button labels can appear visually off-center, especially when a slot has a rendered value, candidate, or compact identity state.

## Product correction

Pick-slot labels and values should remain centered inside their button frame.

This is a visual rendering contract only. It must not change pick ownership, Game 1/Game 2 state, lifecycle stage behavior, or pick write behavior.

## Acceptance

- Pick-slot labels are horizontally centered.
- Pick-slot values are centered within the button frame.
- Picked-cell values remain centered.
- Unpicked prompts remain centered.
- The fix does not restore R16+ preselect hover highlighting.
- Existing pick behavior remains unchanged.
