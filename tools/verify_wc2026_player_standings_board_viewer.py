#!/usr/bin/env python3
from pathlib import Path

active = Path("tools/verify_wc2026_player_standings_no_pick_links.py")
if not active.exists():
    print("Player standings board viewer compatibility failed: no-pick-links verifier is missing.")
    raise SystemExit(1)

print("OK: Player Standings board viewer link has been superseded by no-pick-links standings.")
