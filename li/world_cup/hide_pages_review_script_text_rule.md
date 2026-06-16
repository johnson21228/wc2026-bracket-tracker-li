# Hide Pages review script text rule

Runtime JavaScript patches in `site/index.html` must be inside `<script>` elements. A marked JavaScript repair block must never be left as raw body text because it becomes visible in the review surface and prevents reliable interaction review.
