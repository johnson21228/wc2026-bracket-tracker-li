# GitHub Pages Site Surface Rule

The WC2026 Workbench repo must distinguish between the Workbench control surface and the deployable product surface.

- Workbench files live at repo root, `li/`, `cards/`, `capture_back/`, `source/`, `docs/`, `prompts/`, and `tools/`.
- Public website files live under `site/`.
- Site pages must reference dependencies inside `site/assets/` and `site/data/`.
- Root `index.html` must not be treated as the deployed website.
- `make verify` must fail if stale root public entrypoints return.
