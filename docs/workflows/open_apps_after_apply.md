# Open Apps After Apply Workflow

This Workbench uses two user-facing app surfaces:

- Game 1: Round-of-32 qualifier selection
- Game 2: seeded bracket/champion picker

Every non-trivial apply should end by opening the current app surfaces:

```bash
open site/index.html
open site/game1/index.html
open site/game2/index.html
```

This makes the browser a required review surface, not an optional follow-up.

## Why this matters

Recent regressions showed that a page can verify at the repository level while losing visible behavior such as hit testing, group-filtered menus, or seeded board placement. The Workbench must therefore treat the app surfaces as evidence.

## Evidence expected after apply

The human should be able to answer:

- Does Game 1 still open?
- Does Game 1 still show/click the R32 slots?
- Does Game 1 still filter tap menus by slot group?
- Does Game 2 still open?
- Does Game 2 still show the intended seeded/geometry surface?

The Apply is incomplete until the relevant app surface has been opened for review.
