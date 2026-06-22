# Mouse double-click zoom rule

The Bracketeering board may own mouse double-click zoom as a View-only navigation gesture.

The double-click gesture may change only board viewport navigation state:

- board scale
- board scroll position
- floating menu dismissal/repositioning through existing View hooks

It must not change:

- picks
- pick validity
- scoring
- local or remote storage
- Supabase
- BracketDocument
- Game 1/Game 2 data
- match/result data

Mouse double-click zoom must be ignored when the interaction starts on pick buttons, group buttons, menus, panels, rules controls, banner controls, zoom controls, links, form inputs, or other interactive app surfaces.

Touch double-tap must not be intercepted by this feature. Custom touch pan/pinch belongs in a separate dedicated gesture-controller change.
