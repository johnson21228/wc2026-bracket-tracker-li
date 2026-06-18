# Card 175 — Repair pick identifier developer toggle

## Intent

The pick identifier layer exists, but the developer frame does not expose the show/hide control.

## Evidence

`BoardShell.js` imports `PickIdentifierLayer.js` and sets `data-show-pick-identifiers`, but `DeveloperFrame.js` lacks `Show pick identifiers`.

## Change

Add a developer frame toggle:

```text
Show pick identifiers
```

The toggle controls:

```text
boardPlane.dataset.showPickIdentifiers
```

## Acceptance

- Developer frame includes `Show pick identifiers`.
- The control uses `toggle-pick-identifiers`.
- Copyable developer properties include `showPickIdentifiers`.
- The existing pick identifier layer remains unchanged.
- `make verify` and `make pack` pass.
