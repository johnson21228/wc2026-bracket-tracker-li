# Capture Back — Game 1 R32 pick controller

## Decision

Game 1 R32 projection picks need a controller boundary.

## Why

The pick menu is no longer just a visual overlay. It owns game rules:

- whether a slot can be changed
- which teams can appear in the menu
- whether a selection is legal
- where the selection is persisted

Those rules should not live in DOM rendering code.

## Implementation

Add:

```text
site/js/controllers/Game1R32PickController.js
```

Refactor:

```text
site/js/board/R32PickMenuLayer.js
```

The board layer becomes a view. The controller becomes the authority for all menu and pick decisions.

## Boundary

This is still the pre-lock Game 1 projection model.

Official post-lock third-place assignment remains a separate FIFA Annex C layer.
