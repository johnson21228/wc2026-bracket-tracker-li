# Card 038 — Clean Repo Hygiene

## Intent

Normalize the WC2026 Bracket Tracker repo after overlay-heavy iteration so future site work starts from a clean source tree.

## Changes

- Restore root README identity as the WC2026 Bracket Tracker LI repo.
- Document the two intentional site entry points.
- Add a repo hygiene rule for site entry points and overlay residue.
- Add `tools/clean_repo_hygiene.py` to remove macOS metadata and applied overlay working directories.
- Harden `make pack` to exclude overlay residue and `.DS_Store` files.
- Expand verification to fail closed on missing site entry points, missing playfield assets, stale README identity, `.DS_Store`, and root overlay working directories.

## Acceptance

```bash
python3 tools/clean_repo_hygiene.py
make verify
make pack
git status --short
```
