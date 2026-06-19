# TODO: Public Multi-User Play

## Near-term implementation path

1. Define canonical pick-state schema and slot manifest.
2. Route local storage/export through canonical pick-state JSON.
3. Add a `BracketRepository` mode boundary with local storage as the active implementation.
4. Define `RemoteBracketStore` contract without backend dependency.
5. Add signed-out account UI shell and save-mode status.
6. Add Supabase schema/RLS docs and local config pattern.
7. Implement Supabase auth and remote bracket save/load.
8. Add local-to-account migration.
9. Add submit/lock behavior.
10. Add invite-ready verification.

## Keep-site-running checklist

Each step must preserve:

- anonymous local play
- current site load/render behavior
- export/import or explicit replacement
- `make verify`
- `make pack`
- local site review path

## Deferred

- scoring and leaderboard
- private pools
- admin dashboard
- custom server API
- payment processing
