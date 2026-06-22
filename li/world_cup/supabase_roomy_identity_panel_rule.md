# Supabase Roomy Identity Panel Rule

Supabase sign-in UI must be a thin site-owned identity surface, not a persistence activation surface.

The header may expose only a compact identity button/status. Email entry, auth status, and errors belong in a roomy panel.

Activating or improving this panel must not switch the active bracket store away from localStorage and must not write player brackets to Supabase. Remote bracket persistence requires a separate explicit activation card and verifier.
