# iPhone Touch Map Mode

This feature adds a touch-specific map interaction path for iPhone Safari.

The existing desktop behavior remains mouse-owned:
- mouse drag pans the board
- double-click zooms the board
- ctrl/meta wheel zooms the board

The touch path is separate:
- one-finger drag pans the board viewport
- two-finger pinch zooms the board around the pinch midpoint
- interactive controls and pick targets are excluded from gesture capture
- the board viewport uses `touch-action: none` and safe-area-aware fixed controls so browser-page zoom does not push the + / − controls off screen
