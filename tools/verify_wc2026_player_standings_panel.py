#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text()

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    app = read("site/js/app.js")
    surface = read("site/js/standings/PlayerStandingsSurface.js")
    css = read("site/css/app.css")
    makefile = read("Makefile")
    card = read("cards/1007_add_player_standings_button_and_panel_card.md")
    capture = read("captures/CAPTURE_BACK_PLAYER_STANDINGS_BUTTON_PANEL.md")

    require('createPlayerStandingsSurface' in app and './standings/PlayerStandingsSurface.js' in app,
            "App must import the player standings surface.", errors)
    require('standingsSurface.start();' in app,
            "App must start the player standings surface.", errors)

    require('data-player-standings-open' in surface and 'Standings' in surface,
            "Player-facing Standings button must be created.", errors)
    require('data-player-standings-panel' in surface and 'role", "dialog"' in surface,
            "Standings panel must be a floating dialog surface.", errors)
    require('publicPlayerName' in surface,
            "Standings rows must use public player names.", errors)
    require('email' not in surface.lower(),
            "Standings surface must not expose email fields or labels.", errors)

    require('<th scope="col">Group</th>' in surface,
            "Standings table must display a Group column.", errors)
    require('<th scope="col">Knockout</th>' in surface,
            "Standings table must display a Knockout column.", errors)
    require('<th scope="col">Total</th>' not in surface,
            "Standings table must not display Total column.", errors)
    require('<th scope="col">Picks</th>' not in surface,
            "Standings table must not display Picks column.", errors)
    require('Knockout · TB' not in surface,
            "Standings table must not display combined Knockout/TB label.", errors)
    require('b.total - a.total' in surface
            and 'b.knockoutPoints - a.knockoutPoints' in surface
            and 'b.tiebreakerScore - a.tiebreakerScore' in surface
            and 'localeCompare' in surface,
            "Standings rows must sort by total, knockout, tiebreaker, then player name.", errors)

    forbidden_write_tokens = [
        '.insert(', '.upsert(', '.update(', '.delete(', 'saveUserBracket',
        'createUser', 'writeStandings', 'persistStandings'
    ]
    for token in forbidden_write_tokens:
        require(token not in surface,
                f"Standings panel must be read-only and not contain write token {token}.", errors)

    require('Loading standings…' in surface
            and 'No players yet' in surface
            and 'Sign in to join the standings' in surface
            and 'Standings unavailable' in surface,
            "Standings panel must provide loading/empty/signed-out/error states.", errors)

    require('.player-standings-panel' in css and '.standings-icon-button' in css,
            "Standings button and panel must have player-facing CSS.", errors)

    require('python3 tools/verify_wc2026_player_standings_panel.py' in makefile,
            "Makefile verify must include the player standings verifier.", errors)

    require('participation' in card.lower() and 'participation' in capture.lower(),
            "Card and capture must document participation-first standings intent.", errors)

    if errors:
        print("Player standings panel verification failed: " + "; ".join(errors))
        return 1

    print("OK: player Standings button and read-only participation panel are captured, wired, and verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
