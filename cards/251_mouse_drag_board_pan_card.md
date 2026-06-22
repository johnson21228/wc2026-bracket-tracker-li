# Card 251: Add mouse-only map-style board drag pan

## Intent

Add the first Google Maps-like board navigation behavior without disturbing touch-screen browser navigation.

## Scope

Add mouse-only drag panning on empty board space. The behavior is View-owned and changes only the board viewport scroll position.

## Acceptance

- Mouse users can drag empty board space to pan the board.
- Dragging changes only `scrollLeft` and `scrollTop`.
- Touch users are not intercepted by custom board pan logic.
- The source explicitly guards `event.pointerType === "touch"` before drag pan starts.
- No custom touch/pinch gesture handlers are added.
- Pick buttons still open menus normally.
- Group buttons still open panels normally.
- Zoom dropdown still works.
- Ctrl/Cmd + wheel zoom still works.
- Floating menus/panels still dismiss or position correctly.
- `make verify` passes.
- `make pack` produces the updated pack.

## Non-goals

- Do not implement custom touch pinch.
- Do not implement touch pointer panning.
- Do not change pick logic, scoring, storage, Supabase, Game 1/Game 2 data, or BracketDocument.
