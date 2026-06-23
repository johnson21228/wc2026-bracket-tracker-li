#!/usr/bin/env python3
from pathlib import Path

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

store_path = Path("site/js/standings/SupabasePlayerStandingsStore.js")
surface_path = Path("site/js/standings/PlayerStandingsSurface.js")
app_path = Path("site/js/app.js")

store = store_path.read_text() if store_path.exists() else ""
surface = surface_path.read_text() if surface_path.exists() else ""
app = app_path.read_text() if app_path.exists() else ""

require(store_path.exists(), "SupabasePlayerStandingsStore.js must exist.")
require('from(USER_BRACKETS_TABLE)' in store or '.from("user_brackets")' in store, "Standings store must read from user_brackets.")
require('USER_BRACKETS_TABLE = "user_brackets"' in store, "Standings store must name user_brackets as source table.")
require('PROFILES_TABLE = "profiles"' in store, "Standings store must name profiles as public player source table.")
require('from(PROFILES_TABLE)' in store or '.from("profiles")' in store, "Standings store must read profiles.")
require('display_name' in store, "Standings store must read public display_name.")
require('bracket_json' in store, "Standings store must read bracket_json.")
require('picksBySlot' in store, "Standings store must read picksBySlot.")
require('getSharedSupabaseClient' in store, "Standings store must use the shared Supabase browser client boundary.")

for forbidden in ['email', 'insert(', 'upsert(', 'update(', 'delete(', 'saveUserBracket']:
    require(forbidden not in store, f"Standings store must not expose/write via {forbidden}.")

require('createSupabasePlayerStandingsStore' in app, "app.js must import/create storage-backed standings store.")
require('standingsStore = createSupabasePlayerStandingsStore' in app, "app.js must instantiate standingsStore.")
require('createPlayerStandingsSurface({ root, authService, profileStore, standingsStore })' in app,
        "app.js must pass standingsStore to PlayerStandingsSurface.")

require('standingsStore?.listPlayerStandings?.()' in surface,
        "PlayerStandingsSurface must read rows through standingsStore.")
require('fallbackParticipationRows' in surface,
        "PlayerStandingsSurface may keep fallback participation rows only after storage read.")
require('picksCount' in surface,
        "PlayerStandingsSurface must visibly reflect saved picks participation.")
require('email' not in surface,
        "PlayerStandingsSurface must not render or reference raw email.")

for forbidden in ['.insert(', '.upsert(', '.update(', '.delete(', 'saveUserBracket']:
    require(forbidden not in surface, f"PlayerStandingsSurface must remain read-only: {forbidden}")

if errors:
    raise SystemExit("Storage-backed player standings verification failed: " + "; ".join(errors))

print("OK: Player Standings is storage-backed, reads public names and picks, and remains read-only.")
