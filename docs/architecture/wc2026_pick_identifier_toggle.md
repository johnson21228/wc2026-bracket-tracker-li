# WC2026 pick identifier developer toggle

The pick identifier layer is diagnostic. Developers use it to verify that visible board slots map to stable pick IDs.

The developer frame exposes a `Show pick identifiers` toggle that sets `boardPlane.dataset.showPickIdentifiers`.

The CSS layer visibility follows that dataset value.
