#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

app = (ROOT / "site/js/app.js").read_text()
surface = (ROOT / "site/js/standings/PlayerStandingsSurface.js").read_text()
store = (ROOT / "site/js/standings/SupabasePlayerStandingsStore.js").read_text()
css = (ROOT / "site/css/app.css").read_text()
makefile = (ROOT / "Makefile").read_text()

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

# Current join-first standings contract:
# - App wires the standings surface and Supabase standings store.
# - Browser-module imports may be cache-busted with ?v=...
# - Standings are joined/Supabase shared state, not local/saved conflict UI.

require("./standings/PlayerStandingsSurface.js" in app,
        "App must import player standings surface.")
require("./standings/SupabasePlayerStandingsStore.js" in app,
        "App must import Supabase player standings store.")
require("createPlayerStandingsSurface({" in app,
        "App must mount player standings surface.")
require("createSupabasePlayerStandingsStore" in app,
        "App must create Supabase standings store.")
require("profileStore" in app,
        "App must provide profile store to standings surface.")
require("standingsStore" in app,
        "App must provide standings store to standings surface.")

require("data-player-standings-panel" in surface,
        "Standings panel must keep the player standings panel hook.")
require("standings-icon-button" in surface,
        "Standings surface must provide the standings button.")
require("syncStandingsButtonState" in surface,
        "Standings button must sync joined/not-joined state.")
require("button.hidden = !canOpen" in surface and "button.disabled = !canOpen" in surface,
        "Standings must be hidden/disabled until joined and stored picks are readable.")
require("Join to enter the pool." in surface,
        "Signed-out standings copy must use Join-first wording.")
require("Loading standings…" in surface,
        "Standings panel must provide loading state.")
require("No players yet" in surface,
        "Standings panel must provide empty state.")
require("Standings unavailable" in surface,
        "Standings panel must provide error state.")
require("refreshStorageReady" in surface and "stored picks can be read" in surface,
        "Standings must run a stored-picks read preflight before showing/opening.")
require("fallbackParticipationRows" in surface,
        "Standings must still provide participation fallback rows.")
require("publicNameFromAuthState" in surface,
        "Standings must use public player names instead of raw identity.")

require("createSupabasePlayerStandingsStore" in store,
        "Supabase standings store module must define the store.")
require("listPlayerStandings" in store,
        "Supabase standings store must list player standings.")
require("canReadStoredPicks" in store,
        "Supabase standings store must expose stored-picks read preflight.")
require("user_brackets" in store,
        "Supabase standings store must read joined bracket rows.")

for forbidden in [
    "Sign in to join the standings",
    "login",
    "Save Picks",
    "Load Saved",
    "Use saved picks",
    "Keep this board",
    "You already have picks saved",
    "email",
]:
    require(forbidden not in surface,
            f"Standings surface must not expose stale login/save/load/private identity copy: {forbidden}")

require(".player-standings-control" in css and ".standings-icon-button" in css,
        "Standings control must have visible browser chrome styling.")
require("@media (max-width: 560px)" in css,
        "Standings button must stack safely on narrow screens.")
require(".standings-icon-button.is-join-required" in css or ".standings-icon-button:disabled" in css,
        "Disabled Join-required standings state must have styling.")

require("python3 tools/verify_wc2026_player_standings_panel.py" in makefile,
        "Makefile verify must include player standings verifier.")

if errors:
    print("Join-first player standings panel verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player standings panel is Join-first, cache-busted import tolerant, disabled until joined, and Supabase-backed.")
