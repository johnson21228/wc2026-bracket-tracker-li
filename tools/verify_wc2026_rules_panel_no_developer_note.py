#!/usr/bin/env python3
from pathlib import Path

SITE = Path("site/index.html")

FORBIDDEN = [
    "Developer note",
    "Game selector is currently UI-only",
    "It does not switch gameplay, scoring, storage, routes, Supabase state, data loading, or board rendering yet.",
    "data-rules-panel-section",
    "rules-panel-active-label",
    "Showing Game 1 rules",
    "Showing Game 2 rules",
]

REQUIRED = [
    "Bracketeering Rules",
    "How Bracketeering Hub works",
    "Group Stage Rules:",
    "Knockout Stage Preview",
    "Development preview",
]


def main() -> int:
    html = SITE.read_text()
    errors = []

    for token in FORBIDDEN:
        if token in html:
            errors.append(f"forbidden Rules panel text remains: {token}")

    for token in REQUIRED:
        if token not in html:
            errors.append(f"expected single Rules panel token missing: {token}")

    if errors:
        print("Rules panel lifecycle-stage nomenclature verification failed: " + "; ".join(errors))
        return 1

    print("OK: WC2026 Rules panel is single-display, uses lifecycle-stage naming, and exposes no developer-only caveats.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
