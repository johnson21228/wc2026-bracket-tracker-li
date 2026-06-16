# Prompt: Define R32 Projection Until FIFA Lock

Patch the WC2026 all-inclusive Game 1 site so that R32 assignment state is explicit.

Requirements:

- Add a site-visible R32 assignment phase.
- Default phase is projection/unlocked.
- Official FIFA lock is a separate future state.
- UI should be able to observe whether R32 can be edited.
- Do not treat R32 assignments as immutable before FIFA lock.
- Preserve existing pick storage and rendering behavior.
