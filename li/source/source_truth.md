# Source Truth

## Purpose

This LI defines the source-of-truth order for a Workbench.

## Source truth order

1. Human/domain owner judgment.
2. Current repo source files and governing LI.
3. Git history.
4. Tests, verifiers, generators, and Makefile targets.
5. Continuity cards and source-context maps.
6. Generated history artifacts.
7. Packs and exports.
8. LLM interpretation.

## Rule

The repo is the continuity-bearing artifact.

An LLM may suggest changes. A human or team accepts changes by applying, reviewing, verifying, committing, and preserving them in the repo.

<!-- WC2026_SINGLE_GEOMETRY_TRUTH_START -->
## Single Geometry Truth

WC2026 board geometry has one canonical truth.

The source-truth board geometry artifact is:

- `site/assets/playfield/uniform_pick_card_gameboard.svg`

The app-readable runtime projection is:

- `site/data/geometry/uniform_pick_card_gameboard_manifest.json`

The rendered/review derivative is:

- `site/assets/playfield/uniform_pick_card_gameboard.png`

Canonical rule:

- SVG/source geometry is the source-truth board geometry.
- JSON manifest is a generated/runtime projection of the SVG/source geometry.
- PNG is a rendered derivative for review, fallback, or visual inspection.
- Runtime code may read JSON for convenience, but JSON must not become an independent hand-maintained geometry truth.
- CSS may style rendered surfaces, but CSS must not define canonical slot bounds.
- View/controller/model code must not invent pick-cell geometry that is absent from the source-truth geometry.
- Geometry changes must update the source-truth SVG first, then regenerate or synchronize the JSON projection from that same source.

This prevents SVG, JSON, PNG, CSS, and runtime code from becoming competing geometry authorities.
<!-- WC2026_SINGLE_GEOMETRY_TRUTH_END -->
