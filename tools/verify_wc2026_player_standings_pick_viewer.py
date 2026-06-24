#!/usr/bin/env python3
"""
Compatibility verifier for the first-step grouped player pick list.

That first-step UI was intentionally superseded by the full read-only player
gameboard viewer. The active invariant now lives in:
tools/verify_wc2026_player_standings_board_viewer.py
"""

from pathlib import Path


def main() -> int:
    active = Path("tools/verify_wc2026_player_standings_board_viewer.py")
    if not active.exists():
        print("Player standings pick viewer compatibility failed: board viewer verifier is missing.")
        return 1

    print("OK: grouped player pick-list viewer has been superseded by the full read-only player board viewer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
