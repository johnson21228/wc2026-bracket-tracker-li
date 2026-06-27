#!/usr/bin/env python3
from pathlib import Path

identity = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
profile_store = Path("site/js/services/SupabaseProfileStore.js").read_text()
app = Path("site/js/app.js").read_text()
makefile = Path("Makefile").read_text()

errors = []

required_identity = [
    "Join the Pool",
    "Playing Bracketeering requires you to join the Pool.",
    "Use Google sign-in to avoid email verification.",
    "check your spam folder",
    "Profile",
    "Edit your player name or log out.",
    "Edit your player name below, or log out.",
    "Player name",
    "data-profile-display-name",
    "profileStore.saveProfile({ userId, displayName })",
    "window.setTimeout(async () =>",
    "data-sign-out",
    "Log out",
]

for token in required_identity:
    if token not in identity:
        errors.append(f"Identity UI missing player-name/Profile token: {token}")

required_store = [
    '.from("profiles")',
    ".upsert(",
    "display_name",
    "userId",
]

for token in required_store:
    if token not in profile_store:
        errors.append(f"Profile store missing Supabase public player-name token: {token}")

if "createSupabaseIdentitySurface({" not in app or "profileStore" not in app:
    errors.append("App must mount identity surface with profileStore.")

if "python3 tools/verify_wc2026_supabase_profile_store_public_player_name.py" not in makefile:
    errors.append("Makefile verify must keep public player-name verifier wired.")

for stale in [
    "Your public player name is what other players see.",
    "Update player name",
    "data-profile-save",
    "Picks:",
    "live after joining",
    "You can still explore the board before joining",
    "keep playing locally",
    "No account needed for local play",
    "Local bracket remains active",
]:
    if stale in identity:
        errors.append(f"Stale public player-name/join copy remains: {stale}")

if errors:
    print("Join-first public player name verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Supabase profile store supports live player-name editing without stale local-play/Profile copy.")
