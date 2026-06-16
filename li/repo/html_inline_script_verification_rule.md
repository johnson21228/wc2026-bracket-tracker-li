# HTML Inline Script Verification Rule

When a verifier needs to parse JavaScript embedded in an HTML page, it must not run `node --check` directly against the `.html` file.

The verifier must extract inline JavaScript from `<script>` blocks into a temporary `.js` file, then run syntax checking against that JavaScript file.

This avoids verifier failures caused by Node treating `.html` as an unknown module extension.

This is a verifier concern only. It must not change runtime behavior.
