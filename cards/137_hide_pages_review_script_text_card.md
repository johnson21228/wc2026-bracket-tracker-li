# Card 137 — Hide Pages review script text

## Intent
Repair the Pages review acceptance patch so its JavaScript executes as script instead of rendering as visible text below the board.

## Acceptance
- `site/index.html` contains the Pages review pick acceptance block inside a `<script>` element.
- The block no longer appears as visible page copy.
- Existing bracket verification still passes.
