# Game 1 Uniform SVG Board Layer Rule

Game 1 may switch its visible gameboard layer to the uniform SVG gameboard asset only after the uniform SVG gameboard manifest has been established and Game 1 can read the manifest as a read-only contract probe.

The visible board asset for this step is:

```text
site/assets/playfield/uniform_pick_card_gameboard.svg
```

This SVG remains the source-truth geometry authority for the uniform gameboard family. The PNG remains a derived visual/review artifact, and the manifest remains the app-readable geometry contract.

Layer preservation rule:

- the pub/background layer remains below the board layer
- the SVG gameboard layer replaces only the previous board image element
- the hit-target layer remains above the board and continues using the existing Game 1 R32 slot rules for this step
- the pick-card layer remains above the board and continues using the existing Game 1 R32 slot rules for this step
- the chooser/menu/tooltip layers remain unchanged

This CB is a visual board-layer switch only. It must not migrate Game 1 pick-card placement or Game 1 hit-target placement to the uniform manifest yet. It must not switch Game 2.

After this CB, Game 1 should expose a board-plane marker indicating that the uniform SVG board is visible while manifest-driven placement is still deferred.
