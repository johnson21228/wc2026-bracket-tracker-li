# Pages-Owned Board Zoom-Out Runtime

The Bracketeering Pub board supports View-owned render scaling.

The native board plane remains the source of truth for board coordinates. The View wraps that native plane in a render-scale frame, scales the plane visually, and sizes the frame to the rendered dimensions so zooming out changes the scrollable layout.

Available zoom levels:

- 50%
- 75%
- 100%
- 125%

The View converts scroll bounds and DOM anchor rectangles back into native board coordinates before placing menus and group panels.
