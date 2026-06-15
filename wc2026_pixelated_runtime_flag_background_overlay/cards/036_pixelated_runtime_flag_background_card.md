# Card 036 — Pixelated Runtime Flag Background

## Acceptance

- Background flag defaults to USA.
- Background flag is rendered through an image layer.
- Rendering uses `image-rendering: pixelated` / `crisp-edges`.
- Background opacity is low enough for the board overlay to remain readable.
- First player pick can automatically become the background team.
- Manual background selection locks that override.
- Export/import state preserves background team.
- Release file is created.
