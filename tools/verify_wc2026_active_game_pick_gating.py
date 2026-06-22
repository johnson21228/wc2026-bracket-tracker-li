#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    site_files = [
        ROOT / "site/js/mvc/view.js",
        ROOT / "site/js/mvc/controller.js",
        ROOT / "site/css/app.css",
        ROOT / "site/css/board.css",
    ]
    combined = "\n".join(path.read_text() for path in site_files if path.exists())

    forbidden = [
        "is-disabled-by-active-game",
        "data-disabled-by-active-game",
        "data-active-game-disabled",
        "disabled-by-active-game",
        "only accepts Round of 32 picks",
        "starts after the Round of 32 field",
    ]

    errors = [f"stage-only gameplay gate remains: {token}" for token in forbidden if token in combined]

    if errors:
        print("WC2026 lifecycle stage presentation-only pick gating verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: lifecycle stage is presentation-only; no active-game pick gating remains in runtime surfaces.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
