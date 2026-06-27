#!/usr/bin/env python3
from pathlib import Path

identity = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
store = Path("site/js/services/SupabaseProfileStore.js").read_text()
makefile = Path("Makefile").read_text()

errors = []

required_store = [
    "from(\"profiles\")",
    "display_name",
    "saveProfile",
    "getProfile",
    "upsert(",
    "onConflict: \"id\"",
]

required_identity = [
    "Profile",
    "Player name",
    "data-profile-display-name",
    "data-save-profile-display-name",
    'aria-label="Update player name"',
    'title="Update player name"',
    'event.key === "Enter"',
    "saveProfileDisplayNameNow",
    "profileStore.saveProfile({ userId, displayName })",
    "Player name has not been saved yet.",
    "Explicit send UI: leaving the field does not save.",
    "data-sign-out",
    "Log out",
]

for token in required_store:
    if token not in store:
        errors.append(f"Profile store missing public player-name token: {token}")

for token in required_identity:
    if token not in identity:
        errors.append(f"Identity UI missing player-name/Profile token: {token}")

if "python3 tools/verify_wc2026_supabase_profile_store_public_player_name.py" not in makefile:
    errors.append("Makefile must run public player-name verifier.")

for stale in [
    "Your public player name is what other players see.",
    "data-profile-save",
    "Picks:",
    "live after joining",
    "You can still explore the board before joining",
    "window.setTimeout(async () =>",
    "profileLiveSaveTimer",
    "profileLiveSaveDraft",
]:
    if stale in identity:
        errors.append(f"Stale public player-name/join copy remains: {stale}")

if errors:
    print("Join-first public player name verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Supabase profiles support public player names and Profile uses explicit Enter/send updates.")
