#!/usr/bin/env python3
from pathlib import Path

source = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()

required = [
    "Join the Pool",
    "Playing Bracketeering requires you to join the Pool.",
    "Use Google sign-in to avoid email verification.",
    "check your spam folder",
    "Not joined yet.",
    "Sign in with Google, or use email verification.",
    "Profile",
    "Edit your player name or log out.",
    "Edit your player name below, or log out.",
    "Joined status:",
    "Joined",
    "data-profile-display-name",
    "data-sign-out",
]

forbidden = [
    "You can still explore the board before joining",
    "keep playing locally",
    "No account needed for local play",
    "Local bracket remains active",
    "Join to keep picks live and enter standings",
    "Your picks are live.",
    "data-profile-save",
    "Save player name",
]

errors = []
for token in required:
    if token not in source:
        errors.append(f"Missing required signed-in/join dialog token: {token}")
for token in forbidden:
    if token in source:
        errors.append(f"Stale Join/Profile dialog copy remains: {token}")

if errors:
    print("Join-first signed-in identity UI polish verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: signed-in identity UI supports live player-name editing/logout and signed-out dialog requires joining.")
