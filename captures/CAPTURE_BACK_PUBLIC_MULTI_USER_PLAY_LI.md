# Capture Back: Public Multi-User Play LI

## Capture

The WC2026 Bracketeering Pub site should evolve toward an invite-ready public play surface where people can use a site address, sign in, save picks, submit picks, and return later from another device.

The implementation should be inexpensive and progressive. The first backend target is Supabase Auth + Postgres, but the immediate next engineering target is not a backend connection. The immediate target is a canonical pick-state storage model that the current local store can use first.

## Key decisions

- Keep the frontend static/public if possible.
- Preserve local-only play as anonymous mode and fallback.
- Store one user bracket document per game.
- Game 1 stores 64 picks.
- Game 2 stores 32 picks.
- Champion and third-place winner are explicit stored picks.
- Third-place winner is selected from the semifinal losers.
- The Final Four UI can manage finalists, champion, and third-place winner with one menu, but storage records the resulting slots.
- The site-running invariant is part of the LI: every step must keep the site loadable and usable locally unless intentionally replaced and verified.

## Implementation cards added

- 211 define canonical public-play pick-state storage
- 212 route local storage through canonical pick-state
- 213 define remote bracket store contract
- 214 add signed-in user UI shell
- 215 add Supabase backend schema and RLS setup
- 216 implement Supabase remote bracket store
- 217 add save/load/sync status and local-to-account migration
- 218 add submit/lock bracket behavior
- 219 add invite-ready public play verification
