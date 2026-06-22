# Capture Back: Mouse-only map-style board drag pan

## Request

Add mouse-only map-style board drag pan without disturbing touch navigation.

## Decision

The first map-style board behavior is intentionally mouse-only. It uses the existing board scroll viewport and scrolls via `scrollLeft` and `scrollTop`. It does not alter board geometry, pick logic, scoring, storage, Supabase, Game 1/Game 2 data, or BracketDocument.

## Touch boundary

Do not disturb iPad/iPhone browser touch navigation. Touch users keep native browser scrolling and normal tap behavior. This capture intentionally avoids custom `touchstart`, `touchmove`, custom pinch, touch pointer panning, and `touch-action: none`.

## Verification

A targeted verifier checks that:

- the View owns a mouse drag-pan installer
- touch pointer input is explicitly ignored
- pan uses `scrollLeft` / `scrollTop`
- a small threshold protects clicks from becoming pans
- interactive controls are excluded
- grab/grabbing cursor affordance exists
- no custom touch/pinch handlers are introduced
- `make verify` runs the verifier
