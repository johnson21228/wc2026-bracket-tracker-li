#!/usr/bin/env python3
from pathlib import Path

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

surface_path = Path("site/js/standings/PlayerStandingsSurface.js")
store_path = Path("site/js/standings/SupabasePlayerStandingsStore.js")
css_path = Path("site/css/app.css")
makefile_path = Path("Makefile")
card_path = Path("cards/284_player_standings_pick_viewer_card.md")
capture_path = Path("captures/CAPTURE_BACK_PLAYER_STANDINGS_PICK_VIEWER.md")
doc_path = Path("docs/features/player_standings_pick_viewer.md")
li_path = Path("li/world_cup/player_standings_pick_viewer_rule.md")

surface = surface_path.read_text() if surface_path.exists() else ""
store = store_path.read_text() if store_path.exists() else ""
css = css_path.read_text() if css_path.exists() else ""
makefile = makefile_path.read_text() if makefile_path.exists() else ""

require(surface_path.exists(), "PlayerStandingsSurface.js must exist.")
require(store_path.exists(), "SupabasePlayerStandingsStore.js must exist.")
require(css_path.exists(), "site/css/app.css must exist.")

require('data-player-picks-open' in surface, "Player name cells must expose a dedicated picks-open hook.")
require('class="player-standings-player-button"' in surface, "Player name cells must render as real buttons.")
require('type="button"' in surface, "Player picks controls must be non-submit buttons.")
require('aria-haspopup="region"' in surface and 'aria-expanded' in surface,
        "Player picks buttons must expose accessible disclosure state.")
require('renderPlayerPicksViewer' in surface and 'data-player-picks-viewer' in surface,
        "Surface must render a read-only player picks viewer.")
require('role="region"' in surface and 'aria-labelledby="player-picks-viewer-title"' in surface,
        "Picks viewer must be screen-reader reasonable.")
require('data-player-picks-close' in surface and 'Close player picks' in surface,
        "Picks viewer must include a clear close button.")
require('groupedPickEntries' in surface and 'PICK_ROUND_GROUPS' in surface,
        "Picks viewer must group picks by tournament round.")
for label in ["Round of 32", "Round of 16", "Quarterfinal", "Semifinal", "Final", "Champion / Third place"]:
    require(label in surface, f"Picks viewer must include round grouping label: {label}")
require('picksBySlot' in surface and 'row?.picksBySlot' in surface,
        "Picks viewer must render from each row's picksBySlot.")
require('Unpicked' in surface, "Picks viewer must show player-facing Unpicked copy for empty slots.")
require('escapeHtml' in surface and 'escapeHtml(row.publicPlayerName)' in surface,
        "Public player names and pick labels must be escaped before HTML rendering.")
require('publicPlayerName' in surface and 'playerName' in surface,
        "Surface must preserve public player name normalization.")

require('bracket_json' in store and 'picksBySlotFromBracket' in store,
        "Standings store must continue extracting picksBySlot from bracket_json.")
require('display_name' in store and 'PROFILES_TABLE = "profiles"' in store,
        "Standings store must continue using profiles.display_name as the public name source.")
require('select("id, display_name")' in store,
        "Profiles query must select only public profile fields needed for standings names.")
require('select("user_id, tournament_id, game_id, status, visibility, bracket_json, updated_at")' in store,
        "Bracket query must not select private account fields such as email.")

for forbidden in ['.insert(', '.upsert(', '.update(', '.delete(', 'saveUserBracket', 'LocalStorageBracketStore', 'SupabaseBracketStore(']:
    require(forbidden not in surface, f"Player standings pick viewer must remain read-only and not introduce {forbidden}.")
for forbidden in ['email', 'raw_user_meta_data', 'auth.uid()', 'auth_id']:
    require(forbidden not in surface, f"Picks viewer surface must not render/reference private identifier token: {forbidden}")
    require(forbidden not in store, f"Standings store must not select/reference private identifier token: {forbidden}")

require('.player-standings-player-button' in css, "CSS must make player names visibly actionable.")
require('.player-picks-viewer' in css and '.player-picks-round' in css and '.player-picks-item' in css,
        "CSS must style the read-only picks viewer, round groups, and pick rows.")
require(':focus-visible' in css and '.player-picks-close' in css,
        "CSS must include visible keyboard focus and close button styling.")

require(card_path.exists(), "Card 284 must capture the player standings pick viewer work.")
require(capture_path.exists(), "Capture Back must record the player standings pick viewer change.")
require(doc_path.exists(), "Feature doc must describe player standings pick viewer behavior.")
require(li_path.exists(), "LI rule must protect the read-only standings pick viewer contract.")
require('python3 tools/verify_wc2026_player_standings_pick_viewer.py' in makefile,
        "Makefile verify must include player standings pick viewer verifier.")

if errors:
    raise SystemExit("Player standings pick viewer verification failed: " + "; ".join(errors))

print("OK: Player standings names open read-only grouped picks from picksBySlot without exposing private identifiers or writes.")
