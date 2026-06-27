#!/usr/bin/env python3
from pathlib import Path
import re


def main() -> int:
    source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()
    makefile = Path("Makefile").read_text()
    errors = []

    source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()

    not_joined_branch = re.search(
        r'if \(!joined\) \{(?P<body>.*?)\n    \}',
        source,
        re.S,
    )
    if not not_joined_branch:
        errors.append("missing explicit !joined branch for startup guidance")
    else:
        body = not_joined_branch.group("body")
        if "renderNotice(root, \"not-joined\", NOT_JOINED_STARTUP_MESSAGE);" not in body:
            errors.append("not-joined startup guidance must only render from the !joined branch")

    joined_regions = source.replace(not_joined_branch.group("body") if not_joined_branch else "", "")
    if "NOT_JOINED_STARTUP_MESSAGE" in joined_regions and 'const NOT_JOINED_STARTUP_MESSAGE' not in joined_regions:
        errors.append("not-joined startup message leaked outside the !joined branch")


    required = [
        'const JOINED_PICKS_LOADED_MESSAGE = "Saved picks have been loaded.";',
        'const NOT_JOINED_STARTUP_MESSAGE = "Playing Bracketeering requires you to join the pool. Tap the button with the person icon to join. Tap the button with the “i” to get information about playing the game.";',
        'renderNotice(root, "not-joined", NOT_JOINED_STARTUP_MESSAGE);',
        "function renderNotice(root, state, message)",
        "data-dismiss-join-live-picks-notice",
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
