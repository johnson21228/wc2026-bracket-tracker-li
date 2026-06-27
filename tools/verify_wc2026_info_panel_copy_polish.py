#!/usr/bin/env python3
from pathlib import Path


def main() -> int:
    html = Path("site/index.html").read_text()
    makefile = Path("Makefile").read_text()
    errors = []

    required = [
        "First, register to join the “Pool.”",
        "Using Google sign-in helps you avoid having to find an email that might go to your spam folder.",
        "You will need to choose your player name.",
        "There is no tiebreaker at the moment.",
    ]

    forbidden = [
        "First you need to register to get into the “Pool”.",
        "Using Google options avoids finding the email that might go to your spam folder.",
        "You will need to assign your player name.",
        "There is no tie breaker at the moment.",
        "The game has two parts",
        "Group Stage Picks lock",
        "Knockout Stage picks are locked",
    ]

    for token in required:
        if token not in html:
            errors.append(f"missing polished Info panel copy: {token}")

    for token in forbidden:
        if token in html:
            errors.append(f"stale Info panel copy remains: {token}")

    if "python3 tools/verify_wc2026_info_panel_copy_polish.py" not in makefile:
        errors.append("Makefile verify target must run Info panel copy polish verifier")

    if errors:
        print("Info panel copy polish verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: Info panel copy uses polished player-facing wording.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
