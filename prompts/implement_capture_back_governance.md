# Prompt — Implement Capture Back Governance

Use this prompt when creating future CB overlays for this repo.

## Required behavior

Write all new Capture Back report markdown files to `captures/`.

Do not create root-level `CAPTURE_BACK_*.md` files.

Do not place new CB reports in `capture_back/` unless an explicit migration/preservation card requires it.

Every apply script should print the written report path, for example:

```text
wrote captures/CAPTURE_BACK_EXAMPLE.md
```

## Verification

Run:

```bash
python3 tools/verify_capture_back_governance.py
make verify
make pack
```
