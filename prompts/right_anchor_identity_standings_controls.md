CB: right-anchor Join/Profile and Standings viewport controls

Goal:
Position the existing Join/Profile button and existing Player Standings button as a stable top-right browser chrome cluster on both desktop and touch browsers.

Required behavior:
- Do not clone Join/Profile.
- Do not clone Standings.
- Join/Profile remains auth-state controlled:
  - show Join when not joined/signed in as current runtime does
  - show Profile when joined/signed in as current runtime does
- Standings remains always shown according to current runtime rules.
- Preserve current button sizing:
  - Join/Profile remains current circular icon size
  - Standings remains current pill/button size
- Positioning:
  - Standings right edge aligns to the browser viewport right edge, respecting safe-area inset.
  - Join/Profile is immediately to the left of Standings with a small fixed gap.
  - Cluster remains fixed-size viewport chrome and is not affected by board zoom/pan.
  - Works on desktop browser and iPhone/iPad Safari touch mode.
- Implementation should use the existing visible DOM buttons, not generated duplicates.
- Use visualViewport and safe-area CSS where appropriate.
- Remove/supersede the previous R16-left-edge anchoring behavior if present.
- Add/adjust verifier so it fails if the runtime clones buttons or anchors to R16 instead of right viewport edge.

Verification:
- make verify
- make pack
- Local visual check at:
  http://localhost:8002/site/?v=right-anchored-controls
