# Pages-owned board wheel/pinch zoom

The Bracketeering Pub board has a native coordinate system that should not change when the user zooms. The View owns the render scale by changing CSS variables and a transform on the board plane while preserving native geometry for hit testing.

Wheel/pinch zoom is implemented as a second input surface over the same render-scale model. The dropdown remains useful for exact presets, while modified wheel events allow fluid zooming. The scale is clamped to 50% minimum and 125% maximum.

Pointer-centered zoom preserves the board point under the cursor/fingers by adjusting scroll offsets after the scale changes.
