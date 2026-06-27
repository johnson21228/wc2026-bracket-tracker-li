#!/usr/bin/env python3
from pathlib import Path


def main() -> int:
    index = Path("site/index.html").read_text()
    errors = []

    required_tokens = [
        "Bracketeering Info",
        "World Cup Bracketeering Hub",
        "How to play",
        "First, register to join the “Pool.”",
        "Tap the button that looks like a person",
        "Using Google sign-in helps you avoid having to find an email that might go to your spam folder",
        "You will need to choose your player name",
        "There is no tiebreaker at the moment",
    ]

    for token in required_tokens:
        if token not in index:
            errors.append(f"expected Info panel token missing: {token}")

    forbidden_tokens = [
        "Developer note",
        "Development preview",
        "Game 1 Rules:",
        "Game 2 Preview",
        "official FIFA-supplied",
        "The game has two parts",
        "Part one results are used as a tiebreaker",
        "Group Stage Picks lock at 11:59 PM ET",
        "Knockout Stage picks are locked when the first knockout match begins",
        "Press the join button to play the game with others",
    ]

    for token in forbidden_tokens:
        if token in index:
            errors.append(f"forbidden/stale Info panel token remains: {token}")

    if errors:
        print("Info panel developer note verification failed:")
        print("; ".join(errors))
        return 1

    print("OK: WC2026 Info panel is current, player-facing, and exposes no developer-only caveats.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
