# Capture Back: Top-right player controls

Replaced the R16-left-edge anchored Profile/Join + Standings experiment with a simpler browser-chrome control cluster.

Outcome:
- Join/Profile and Standings are grouped at the top-right of the browser window.
- Join appears when not joined; Profile appears when joined.
- Standings remains always available when its button exists.
- All controls keep fixed 44px circular sizing.
- Placement uses CSS right alignment, not board geometry measurement.

## Correction

The final implementation is CSS-owned. It does not move, clone, scan, or reparent buttons. SupabaseIdentitySurface continues to own Join/Profile. PlayerStandingsSurface continues to own Standings. CSS pins the existing renderer-owned controls to the browser viewport right edge.
