# Site Entry Point Hygiene Rule

The repo has two intentional site entry points:

- `index.html` for the main tracker / Game 2 bracket surface
- `game1_playfield.html` for the Game 1 Round of 32 chooser playfield

Any feature card or Capture Back that changes site behavior must name the affected entry point.

Applied overlay working directories are not source of truth after their contents are captured into repo files. They must not remain at repo root or be included in packs.

## GitHub Pages root redirect exception

A root `index.html` is allowed only when it is a tiny GitHub Pages shim that redirects to `site/`.

The root shim must not become the app runtime. It may contain only metadata, a `site/` link, and redirect logic. The deployable app remains under `site/`.
