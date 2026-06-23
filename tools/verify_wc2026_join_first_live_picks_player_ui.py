#!/usr/bin/env python3
from pathlib import Path

errors = []

paths = {
    "identity": Path("site/js/identity/SupabaseIdentitySurface.js").read_text(),
    "live_picks": Path("site/js/identity/AccountSaveActionSurface.js").read_text(),
    "standings": Path("site/js/standings/PlayerStandingsSurface.js").read_text(),
    "controller": Path("site/js/mvc/controller.js").read_text(),
    "css": Path("site/css/app.css").read_text(),
    "card": Path("cards/279_join_first_live_picks_player_ui_card.md").read_text(),
    "capture": Path("captures/CAPTURE_BACK_JOIN_FIRST_LIVE_PICKS_PLAYER_UI.md").read_text(),
    "doc": Path("docs/architecture/wc2026_join_first_live_picks_player_ui.md").read_text(),
    "li": Path("li/world_cup/join_first_live_picks_player_ui_rule.md").read_text(),
    "makefile": Path("Makefile").read_text(),
}

required_runtime_tokens = [
    ("identity", "Join"),
    ("identity", "Profile"),
    ("identity", "Joined as"),
    ("identity", "Join to enter standings."),
    ("identity", "Join the game to keep picks live and enter standings."),
    ("live_picks", "AUTOSAVE_DELAY_MS"),
    ("live_picks", "scheduleAutosave"),
    ("live_picks", "wc2026:picks-changed"),
    ("live_picks", "saveUserBracket(bracketDocument)"),
    ("live_picks", "loadUserBracket(playerUserId)"),
    ("live_picks", "You already have picks saved. Use saved picks or keep this board?"),
    ("live_picks", "Use saved picks"),
    ("live_picks", "Keep this board"),
    ("live_picks", "Saving…"),
    ("live_picks", "Picks saved"),
    ("live_picks", "Could not save — retrying"),
    ("standings", "Join to enter standings."),
    ("standings", "syncStandingsButtonState"),
    ("standings", "button.disabled = !joined"),
    ("controller", "Loaded your joined picks."),
    ("css", ".join-live-picks-status"),
    ("css", ".join-live-picks-conflict"),
]

for key, token in required_runtime_tokens:
    if token not in paths[key]:
        errors.append(f"missing {token!r} in {key}")

for key in ["identity", "live_picks", "standings"]:
    for forbidden in [
        "Save Picks",
        "Load Saved",
        "Remote store",
        "Storage mode",
        "Account persistence ready",
        "Sign in to save",
        "Sign in to save and load picks",
        "Bracket persistence:",
    ]:
        if forbidden in paths[key]:
            errors.append(f"old persistence/login copy remains in {key}: {forbidden}")

for key in ["card", "capture", "doc", "li"]:
    for token in ["Join", "Standings", "Profile", "picks are live", "autosave", "Save Picks", "Load Saved"]:
        if token not in paths[key]:
            errors.append(f"LI artifact {key} missing required concept: {token}")

if "python3 tools/verify_wc2026_join_first_live_picks_player_ui.py" not in paths["makefile"]:
    errors.append("Makefile verify must include join-first verifier.")

if errors:
    raise SystemExit("WC2026 Join-first live picks verification failed: " + "; ".join(errors))

print("OK: WC2026 Join-first player UI is implemented with Join, Standings, Profile, live autosave, and no Save/Load player flow.")
