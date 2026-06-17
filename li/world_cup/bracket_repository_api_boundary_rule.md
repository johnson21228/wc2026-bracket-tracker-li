# Bracket repository API boundary rule

The WC2026 site must access model and bracket persistence through a repository boundary.

Requirements:

- Static GitHub Pages mode may read committed JSON and write localStorage.
- Shared multi-user mode must use a server/API boundary.
- SQLite must live behind the server/API boundary, not directly in browser code.
- UI rendering must not depend on the persistence mechanism.
- User bracket shape and pick values must stay stable across adapters.
