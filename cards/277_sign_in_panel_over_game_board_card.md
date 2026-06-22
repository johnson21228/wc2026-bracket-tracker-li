# Card 277 — Sign-in panel over game board

## Intent
Keep the Supabase sign-in panel completely over the game board whenever opened.

## Problem
The identity surface button is fixed browser chrome, but the opened identity backdrop/panel can be visually under board popovers or other board-scaled/floating surfaces because board transient surfaces use high z-index values.

## Acceptance
- Sign-in compact button remains fixed upper-right browser chrome.
- Open sign-in backdrop covers the full viewport.
- Open sign-in panel outranks board pick menus, group panels, zoom controls, board surfaces, and board-scaled geometry.
- This is View/CSS layering only; it does not change Supabase persistence behavior.
