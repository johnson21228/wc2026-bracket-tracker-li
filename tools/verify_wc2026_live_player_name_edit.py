#!/usr/bin/env python3
from pathlib import Path

source = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
makefile = Path("Makefile").read_text()

required = [
    "data-profile-display-name",
    "profileLiveSaveTimer",
    "profileLiveSaveDraft",
    "addEventListener(\"input\"",
    "window.setTimeout(async () =>",
    "profileStore.saveProfile({ userId, displayName })",
    "Player name saved.",
    "data-sign-out",
    "loadProfileForState(latestState)",
]

forbidden = [
    "data-profile-save",
    "Save player name",
    "Public player name saved.",
    "No account needed for local play",
    "keep playing locally",
    "You can still explore the board before joining",
]

errors = []
for token in required:
    if token not in source:
        errors.append(f"Missing live player-name edit token: {token}")

for token in forbidden:
    if token in source:
        errors.append(f"Stale Profile/join copy or save-button token remains: {token}")

if "python3 tools/verify_wc2026_live_player_name_edit.py" not in makefile:
    errors.append("Makefile must run live player-name edit verifier.")

if errors:
    print("WC2026 live player-name edit verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: signed-in Profile player-name field live-saves to Supabase and keeps logout.")
