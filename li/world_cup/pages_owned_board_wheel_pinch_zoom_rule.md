# Pages-owned board wheel/pinch zoom rule

Board zoom must be View-owned and must not rewrite native board geometry.

Requirements:

- Wheel/pinch zoom must call the same render-scale path used by the board zoom dropdown.
- Minimum zoom-out must be pinned to a reasonable value, currently 50%.
- Maximum zoom-in must remain bounded, currently 125%.
- Normal scrolling must remain normal scrolling unless the wheel event is a zoom-modified event.
- Pointer-centered zoom should preserve the visible board focus.
