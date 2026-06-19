# Site-Running Public Play Invariant Rule

The public-play migration must keep the site running at every step.

## Invariant

Before, during, and after backend work, the site must remain usable as a local/static bracket game.

The following must remain true unless an intentional replacement is captured and verified:

- `site/index.html` loads without a backend account.
- anonymous/local pick behavior works.
- local storage remains a fallback.
- export/import remains available or has an intentional replacement.
- `make verify` and `make pack` pass before commit.
- `make opensite` or equivalent local site review remains available.
- Pages publish is not treated as proof of correctness unless the local site and verifier path pass first.

## Public-play additions must be progressive

Additions should be layered in this order:

1. define canonical storage model
2. route local storage through the model
3. define remote store contract
4. add account UI shell
5. add backend schema and RLS
6. implement remote store
7. add save/load/sync status
8. add submit/lock
9. verify invite-ready public play

A backend outage must not make anonymous/local review impossible.
