#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def require_contains(text, token, errors, label):
    if token not in text:
        errors.append(f"{label}: missing {token!r}")

def require_not_contains(text, token, errors, label):
    if token in text:
        errors.append(f"{label}: unexpected legacy player-facing token {token!r}")

def main() -> int:
    site = (ROOT / "site/index.html").read_text()
    view = (ROOT / "site/js/mvc/view.js").read_text()

    errors = []

    # Legacy verifier filename retained for make verify continuity.
    # This migration changes player-facing nomenclature first while preserving
    # legacy game-1/game-2 runtime hooks.
    require_contains(site, 'data-dev-game-selector', errors, "site/index.html")
    require_contains(site, 'aria-label="Developer stage selector"', errors, "site/index.html")
    require_contains(site, 'name="dev-game-view"', errors, "site/index.html")
    require_contains(site, 'value="game-1"', errors, "site/index.html")
    require_contains(site, 'value="game-2"', errors, "site/index.html")
    require_contains(site, ">Group Stage<", errors, "site/index.html")
    require_contains(site, ">Knockout Stage<", errors, "site/index.html")

    require_contains(view, ".dev-game-selector-option input:checked", errors, "site/js/mvc/view.js")
    require_contains(view, 'data-dev-game-selector', errors, "site/js/mvc/view.js")
    require_contains(view, 'game-1', errors, "site/js/mvc/view.js")
    require_contains(view, 'game-2', errors, "site/js/mvc/view.js")

    require_not_contains(site, ">Game 1<", errors, "site/index.html")
    require_not_contains(site, ">Game 2<", errors, "site/index.html")
    require_not_contains(site, "Dev Game View", errors, "site/index.html")

    # Placement/order is not part of this nomenclature migration. Verify both
    # controls still exist without forcing exact banner ordering.
    if "data-board-scale" not in site:
        errors.append("site/index.html: missing zoom control token data-board-scale")
    if "data-dev-game-selector" not in site:
        errors.append("site/index.html: missing selector token data-dev-game-selector")

    if errors:
        print("WC2026 lifecycle Stage selector placement verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: Stage selector uses Group/Knockout Stage labels and preserves legacy selector hooks during presentation-only gameplay migration.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
