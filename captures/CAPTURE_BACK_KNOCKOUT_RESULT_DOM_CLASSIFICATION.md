# Capture Back: Knockout Result DOM Classification

R16+ knockout picks now receive stable DOM classification aliases for official result state.

## Behavior

When a non-R32 slot has an official comparison state, the pick button receives:

- `is-knockout-result-classified`
- `is-knockout-result-correct`
- `is-knockout-result-incorrect`
- `is-knockout-result-unreachable`

It also receives:

- `data-knockout-result-state="correct"`
- `data-knockout-result-state="incorrect"`
- `data-knockout-result-state="unreachable"`

## Guardrails

This is classification only.

It does not change:

- official truth data
- knockout result data
- scoring
- winner derivation
- Supabase writes
- player pick storage

The model decides truth. The view labels the DOM. CSS paints the labels.
