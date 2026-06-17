# Canonical Knockout Assignment Surface

The knockout choice menu is the assignment surface for the bracket cell that opened it.

This feature removes stacked assignment wrappers and installs a single canonical path:

```text
open cell menu -> choose team -> write storage -> render cell -> close menu
```

The surface owns:

- the active target slot ID,
- the target round,
- candidate rendering,
- tile click/pointer selection,
- round-specific storage, and
- immediate cell rendering.
