# Top-right player controls rule

Profile/Join and Player Standings are one player-control browser-chrome cluster.

Required behavior:
- the identity slot shows Join when not joined;
- the identity slot shows Profile when joined;
- Player Standings is always shown when the standings runtime button exists;
- both controls retain fixed 44px circular button sizing;
- the cluster is aligned to the right edge of the browser viewport with CSS `position: fixed` and `right: calc(env(safe-area-inset-right, 0px) + 16px)`;
- the cluster must not use R16 slot anchoring, left-edge placement, or `getBoundingClientRect` geometry measurement.

## Correction

The final implementation is CSS-owned. It does not move, clone, scan, or reparent buttons. SupabaseIdentitySurface continues to own Join/Profile. PlayerStandingsSurface continues to own Standings. CSS pins the existing renderer-owned controls to the browser viewport right edge.
