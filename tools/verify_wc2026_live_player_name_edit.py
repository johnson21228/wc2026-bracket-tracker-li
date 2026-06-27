#!/usr/bin/env python3
from pathlib import Path

surface = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
css = Path("site/css/app.css").read_text()

errors = []

required_surface_tokens = [
    'data-profile-display-name',
    'data-save-profile-display-name',
    'aria-label="Update player name"',
    'title="Update player name"',
    'saveProfileDisplayNameNow',
    'event.key === "Enter"',
    'profileStore.saveProfile({ userId, displayName })',
    'Player name has not been saved yet.',
    'Explicit send UI: leaving the field does not save.',
    'data-sign-out',
]

for token in required_surface_tokens:
    if token not in surface:
        errors.append(f"Missing player-name send-action token: {token}")

required_css_tokens = [
    ".identity-profile-name-send-row",
    ".identity-profile-send-button",
    ".identity-profile-send-button:disabled",
]

for token in required_css_tokens:
    if token not in css:
        errors.append(f"Missing player-name send-action CSS token: {token}")

try:
    input_listener = surface.split('input?.addEventListener("input"', 1)[1].split('input?.addEventListener("keydown"', 1)[0]
    if "profileStore.saveProfile" in input_listener or "saveProfileDisplayNameNow" in input_listener or "setTimeout" in input_listener:
        errors.append("Player-name input listener must only update local draft/dirty state; it must not save or schedule save.")
except IndexError:
    errors.append("Could not find player-name input listener followed by keydown listener.")

try:
    save_function = surface.split("async function saveProfileDisplayNameNow", 1)[1].split('const input = actions.querySelector("[data-profile-display-name]")', 1)[0]
    if "profileStore.saveProfile({ userId, displayName })" not in save_function:
        errors.append("Explicit save function must call profileStore.saveProfile once.")
except IndexError:
    errors.append("Could not isolate saveProfileDisplayNameNow function.")

try:
    blur_listener = surface.split('input?.addEventListener("blur"', 1)[1].split('actions.querySelector("[data-save-profile-display-name]")', 1)[0]
    if "saveProfileDisplayNameNow" in blur_listener or "profileStore.saveProfile" in blur_listener:
        errors.append("Blur must not save player-name edits.")
except IndexError:
    errors.append("Could not find blur listener before send-button click listener.")

if "profileLiveSaveTimer" in surface or "profileLiveSaveDraft" in surface:
    errors.append("Old player-name live-save timer/draft state must be removed.")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    raise SystemExit(1)

print("OK: signed-in Profile player-name field uses explicit Enter/send action and does not autosave on input or blur.")
