# Dynamic bootstrap debug console rule

During clean-site development, the app entrypoint must mount developer diagnostics before loading fragile board modules.

Static imports in `site/js/app.js` should be limited to diagnostic/mount helpers. Board and feature modules should be dynamically imported after the developer console is visible.
