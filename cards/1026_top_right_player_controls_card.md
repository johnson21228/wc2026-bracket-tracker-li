# Card 1026: Top-right player controls

## Goal
Keep Join/Profile and Player Standings visible as fixed top-right player controls.

## Result
The broken R16-left-edge anchoring behavior was replaced with a simple browser-chrome cluster aligned to the right edge of the viewport.

## Verification
`python3 tools/verify_wc2026_top_right_player_controls.py`

## Correction

The final implementation is CSS-owned. It does not move, clone, scan, or reparent buttons. SupabaseIdentitySurface continues to own Join/Profile. PlayerStandingsSurface continues to own Standings. CSS pins the existing renderer-owned controls to the browser viewport right edge.
