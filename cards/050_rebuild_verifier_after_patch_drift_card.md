# Card 050: Rebuild Verifier After Patch Drift

## Intent
Restore repo verification after multiple CB overlays left `tools/verify_wc2026_bracket_tracker.py` syntactically invalid.

## Acceptance
- Verifier compiles.
- `make verify` reaches semantic repo checks instead of Python parse errors.
- Verifier reflects current site-layer architecture rather than stale root HTML / opaque board assumptions.
