# Open Apps After Apply Rule

Every Capture Back apply workflow for this Workbench must open the user-facing app surfaces after the overlay is applied.

## Rule

When an apply command changes this repository, the terminal block must include `open` commands for the app surfaces that need human visual review.

For the WC2026 Bracket Tracker, the default post-apply review surfaces are:

- `site/index.html`
- `site/game1/index.html`
- `site/game2/index.html`

## Reason

The two game surfaces are the product. Passing repository verification is necessary but not sufficient. Visual behavior can regress even when text-token verification passes.

Opening the apps after every apply keeps the Workbench loop grounded in the running product surface.

## Minimum Apply Shape

A normal apply block should follow this shape:

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li

unzip -o ~/Downloads/<overlay>.zip -d .
python3 <overlay_dir>/<apply_script>.py

make verify
make pack

git status --short

open site/index.html
open site/game1/index.html
open site/game2/index.html
```

## Targeted Exceptions

If an overlay is explicitly LI-only and does not touch the site runtime, it may open the changed LI/docs files instead of both game apps. Any overlay that touches `site/`, `data/`, `assets/`, or game behavior should open both Game 1 and Game 2.

## Preservation

Future Capture Backs that revise apply-command guidance must preserve this rule unless the user explicitly approves a replacement review protocol.
