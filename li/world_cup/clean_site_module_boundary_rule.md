# Clean site module boundary rule

The WC2026 clean site must be built from Living Intent, data, assets, and modules rather than copied or patched from legacy runtime code.

## HTML boundary

`site/new/index.html` is a shell only.

It may contain:

- document metadata
- preload links for board truth resources
- stylesheet links
- a single app mount
- a module entrypoint script

It must not contain:

- board rendering implementation
- pick rendering implementation
- menu implementation
- localStorage reads
- legacy render bridges
- legacy pick keys

## Module boundary

Rendering and behavior must live in JavaScript modules.

Initial module groups:

- `site/new/js/services/` for base services and truth-resource paths
- `site/new/js/board/` for board plane and layers
- `site/new/js/model/` for later canonical pool model
- `site/new/js/controllers/` for later game/menu orchestration

## Board truth resources

The clean site owns these truth resources:

1. `site/assets/playfield/game1_pub_options_background.jpeg`
2. `site/assets/playfield/uniform_pick_card_gameboard.svg`
3. `site/data/geometry/uniform_pick_card_gameboard_manifest.json`

The first render checkpoint renders only the background image layer. The SVG and manifest are retained as truth resources for later layers.

## Legacy stance

`source/legacy_snapshots/` is archaeology only.

Legacy code must not be copied into `site/new/`.
