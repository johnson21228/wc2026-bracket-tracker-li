# Mouse-only map-style board drag pan

The Bracketeering board supports a first map-style navigation behavior for mouse users: click and drag empty board space to pan the board viewport.

This is a View-owned navigation behavior. It changes only the board scroll viewport (`scrollLeft` and `scrollTop`) and does not change picks, scoring, storage, Supabase, Game 1/Game 2 data, or the canonical BracketDocument.

Touch navigation remains browser-owned in this step. iPad and iPhone users keep native browser scrolling and normal tap behavior. This feature does not add custom `touchstart`, `touchmove`, custom pinch, or touch pointer panning.

The drag pan starts only for primary left-button mouse pointer input on non-interactive board space. Pick buttons, group buttons, menus, panels, links, form controls, rules controls, and selector controls are excluded so tap/click gameplay behavior remains intact.
