#!/usr/bin/env python3
from pathlib import Path

SITE = Path("site/index.html")

FORBIDDEN = [
    "Developer note",
    "Game selector is currently UI-only",
    "It does not switch gameplay, scoring, storage, routes, Supabase state, data loading, or board rendering yet.",
]

REQUIRED = [
    "Bracketeering Rules",
    "Game 1 — Pick the Round of 32 field",
    "Game 2",
    'data-rules-panel-section="game-1"',
    'data-rules-panel-section="game-2"',
]


def main() -> int:
    html = SITE.read_text()
    errors = []

    for token in FORBIDDEN:
        if token in html:
            errors.append(f"forbidden developer-note text remains: {token}")

    for token in REQUIRED:
        if token not in html:
            errors.append(f"expected Rules panel token missing: {token}")

    if errors:
        print("Rules panel developer note verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 Rules panel no longer exposes developer-only game selector caveats.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
