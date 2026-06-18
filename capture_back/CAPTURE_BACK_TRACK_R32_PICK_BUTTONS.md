# Capture Back — Track R32 pick buttons

## Decision

Game 1 needs observable pick-button tracking.

## Why

The board has invisible geometry and translucent pick controls. A user needs to see what is pickable before committing a click. A developer also needs to inspect whether the button layer has rendered, whether buttons are enabled, and which slot is being targeted.

## Implementation

Patch `R32PickMenuLayer` so each button reports:

- FIFA slot id
- FIFA label
- geometry slot id
- enabled/pickable state
- candidate count
- eligible groups
- last tracking phase: hover, focus, click, clear

Add visual pre-select highlighting through CSS.

## Result

The controller still owns all pick rules. The view now makes pickability visible and trackable.
