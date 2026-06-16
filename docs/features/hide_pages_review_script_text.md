# Hide Pages review script text

The Pages review pick acceptance repair injected JavaScript into `site/index.html`. On the public Pages build the block appeared as visible text below the board, which means it was not inside a `<script>` element.

This repair wraps the marked `WC2026_PAGES_REVIEW_PICK_ACCEPTANCE` block in a script element so the browser executes it and does not render it as page text.
