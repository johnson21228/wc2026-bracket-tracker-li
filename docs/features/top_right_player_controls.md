# Top-right player controls

Profile/Join and Player Standings are browser chrome, not board geometry.

The identity control shows Join when the player has not joined and Profile when the player has joined. Player Standings is always shown when its runtime button exists. The two controls are placed in one fixed top-right viewport cluster with CSS `position: fixed` and `right: calc(env(safe-area-inset-right, 0px) + 16px)` so desktop browser resize and touch safe areas are handled by browser layout.

This replaces the previous R16-left-edge anchored experiment. The controls are not anchored with board-slot measurement or `getBoundingClientRect`.

## Correction

The final implementation is CSS-owned. It does not move, clone, scan, or reparent buttons. SupabaseIdentitySurface continues to own Join/Profile. PlayerStandingsSurface continues to own Standings. CSS pins the existing renderer-owned controls to the browser viewport right edge.
