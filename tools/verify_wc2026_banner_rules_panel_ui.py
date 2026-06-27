#!/usr/bin/env python3
from pathlib import Path


def main() -> int:
    index = Path("site/index.html").read_text()
    errors = []

    required_tokens = [
        "World Cup Bracketeering Hub",
        "Bracketeering Info",
        "How to play",
        "First you need to register to get into the “Pool”",
        "Tap the button that looks like a person",
        "Using Google options avoids finding the email that might go to your spam folder",
        "You will need to assign your player name",
        "Tap or click each bracket slot and pick a winning team",
        "The winner gets $50",
        "410-925-7495",
        "Navigate the game board like Google Maps",
        "Scoring",
        "1 point for each correct Round of 32 winner",
        "2 points for each correct Round of 16 winner",
        "4 points for each correct Quarterfinal winner",
        "8 points for each correct Semifinal winner",
        "16 points for correctly picking the World Cup champion",
        "There is no tie breaker at the moment",
        "Have fun",
    ]

    for token in required_tokens:
        if token not in index:
            errors.append(f"missing Info panel token: {token}")

    stale_tokens = [
        "The game has two parts",
        "Part one results are used as a tiebreaker",
        "Group Stage Picks lock at 11:59 PM ET",
        "Knockout Stage picks are locked when the first knockout match begins",
        "Please, just have fun making picks",
        "Press the join button to play the game with others",
    ]

    for token in stale_tokens:
        if token in index:
            errors.append(f"stale Info panel token still present: {token}")

    if errors:
        print("Info panel UI verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: WC2026 Info panel uses current one-game Bracketeering Hub copy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
