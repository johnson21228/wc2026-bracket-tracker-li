#!/usr/bin/env python3
from pathlib import Path


def main() -> int:
    source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()
    makefile = Path("Makefile").read_text()
    errors = []

    required = [
        'const JOINED_PICKS_LOADED_MESSAGE = "Your picks have been loaded.";',
        'const NOT_JOINED_STARTUP_MESSAGE = "Playing Bracketeering requires you to join the pool. Tap the button with the person icon to join. Tap the button with the “i” to get information about playing the game.";',
        'renderStatus(root, "not-joined", NOT_JOINED_STARTUP_MESSAGE);',
        '<p>${JOINED_PICKS_LOADED_MESSAGE}</p>',
    ]

    forbidden = [
        "Your saved joined bracket was loaded.",
        "Local draft picks are ignored for joined play.",
        "You are not joined yet. Your picks are saved on this device.",
        "localStorage",
    ]

    for token in required:
        if token not in source:
            errors.append(f"missing startup guidance token: {token}")

    for token in forbidden:
        if token in source:
            errors.append(f"technical/stale player-facing token remains: {token}")

    if "python3 tools/verify_wc2026_not_joined_startup_guidance.py" not in makefile:
        errors.append("Makefile verify target must run not-joined startup guidance verifier")

    if errors:
        print("Not-joined startup guidance verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: not-joined startup guidance and joined loaded-picks copy are player-facing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
