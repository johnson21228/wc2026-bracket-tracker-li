# Rule: Mouse-only board drag pan must be View-owned and touch-safe

The board may provide map-style drag panning for mouse users, but the behavior belongs to the View/navigation layer only.

The implementation must:

- use the existing `[data-board-scroll]` viewport
- pan by changing `scrollLeft` and `scrollTop`
- start only from primary left-button mouse pointer input
- explicitly ignore `event.pointerType === "touch"`
- avoid custom touch/pinch handlers in this step
- avoid `touch-action: none`
- preserve native iPad/iPhone browser scrolling and tap behavior
- exclude interactive controls, pick buttons, menus, group panels, rules panels, links, and form controls from drag start
- preserve existing zoom dropdown and Ctrl/Cmd-wheel zoom behavior

It must not change gameplay model state, pick validity, scoring, Supabase, Game 1/Game 2 data, storage, or BracketDocument behavior.
