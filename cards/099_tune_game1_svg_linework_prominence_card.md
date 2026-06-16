# Card 099 — Tune Game 1 SVG Linework Prominence

## Intent

Make the uniform SVG bracket linework more prominent after browser review while preserving the transparent middle-layer model.

## Change

- Keep the SVG as transparent geometry/presentation layer.
- Keep pick-card fill at `#816A51`.
- Move connector and slot-outline linework from `#542C23` halfway toward white, to `#AA9691`.
- Preserve stronger R32 selectable-target fill affordance.
- Preserve manifest-driven Game 1 R32 placement.
- Keep Game 2 unmigrated.

## Acceptance

- Full bracket linework reads more clearly.
- Bottom image remains visible through the SVG.
- R32 targets remain visibly selectable.
- Verifiers pass.
