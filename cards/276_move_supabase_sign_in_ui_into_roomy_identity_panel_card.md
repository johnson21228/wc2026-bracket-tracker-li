# Card 276: Move Supabase sign-in UI into roomy identity panel

## Goal
Replace the cramped inline Supabase sign-in form with a compact identity button that opens a spacious sign-in panel.

## Acceptance
- The header identity surface is compact.
- The email input appears only in a panel with full width.
- Magic-link requests are cooldown guarded.
- Local bracket persistence remains the active store.
- Remote Supabase bracket persistence remains inactive.
- `make verify` includes the roomy identity panel verifier.
