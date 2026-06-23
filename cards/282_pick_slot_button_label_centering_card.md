# Card 282: Pick Slot Button Label Centering

## Intent

Fix pick-slot button labels that appear visually off-center.

## Change

Add a verified CSS rendering contract so pick-slot labels and values use centered alignment within their button frame.

## Acceptance

- Pick-slot labels and values center in the button.
- Picked values center.
- Unpicked prompts center.
- R16+ preselect hover remains suppressed.
- `make verify` and `make pack` pass.
