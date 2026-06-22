# Sign-in Panel Over Game Board Rule

The Supabase sign-in panel is browser chrome, not board geometry.

When opened, the identity backdrop and panel must render above the full game board, including:
- board plane
- pick cells
- champion aura
- pick menus
- group panels
- zoom and map controls

This rule is CSS layering only. It must not change pick data, board geometry, Supabase persistence, or localStorage behavior.
