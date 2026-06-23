#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    app = Path("site/js/app.js").read_text()
    css = Path("site/css/app.css").read_text()
    surface = Path("site/js/identity/AccountSaveActionSurface.js").read_text()
    model = Path("site/js/mvc/model.js").read_text()
    controller = Path("site/js/mvc/controller.js").read_text()
    makefile = Path("Makefile").read_text()

    require('import { createAccountSaveActionSurface } from "./identity/AccountSaveActionSurface.js";' in app,
            "App must import the joined live-picks surface.", errors)
    require("createAccountSaveActionSurface({" in app and "model," in app,
            "App must mount joined live-picks persistence with the model.", errors)

    require("function getAccountSaveBracketDocument" in model and 'buildRemoteBracketDocument("account-save-button")' in model,
            "Model must still expose canonical BracketDocument snapshots at the persistence boundary.", errors)
    require("function importAccountBracketDocument" in model and "importPicksSnapshot({ picks: incomingPicks })" in model,
            "Model must still import joined bracket picks through the canonical local pick import path.", errors)

    require("AUTOSAVE_DELAY_MS" in surface and "scheduleAutosave" in surface and "wc2026:picks-changed" in surface,
            "Joined picks must autosave from pick-change events using a debounce.", errors)
    require("loadUserBracket(playerUserId)" in surface and "saveUserBracket(bracketDocument)" in surface,
            "Joined live picks must use SupabaseBracketStore behind the BracketStore seam.", errors)
    require("You already have picks saved. Use saved picks or keep this board?" in surface,
            "Existing joined bracket conflicts must be handled once with a player-facing choice.", errors)
    require("Use saved picks" in surface and "Keep this board" in surface,
            "Conflict UI must offer the two required choices.", errors)
    require('"Saving…"' in surface and '"Picks saved"' in surface and '"Could not save — retrying"' in surface,
            "Joined live picks must use status-only autosave copy.", errors)
    require("localStorage" not in surface,
            "Joined live-picks surface must not use localStorage directly.", errors)

    forbidden_player_commands = ["Save Picks", "Load Saved", "Try Save Again", "Unsaved changes", "Current picks saved", "Account persistence ready"]
    for token in forbidden_player_commands:
        require(token not in surface, f"Player-facing joined live-picks surface must not expose old command/copy: {token}", errors)

    require("wc2026:account-picks-loaded" in controller and "Loaded your joined picks." in controller,
            "Controller must redraw after joined picks are loaded without old save/load copy.", errors)

    require(".join-live-picks-status" in css and ".join-live-picks-conflict" in css,
            "Joined live-picks status/conflict UI must have browser chrome styling.", errors)
    require(".storage-mode-status" not in css,
            "Persistent local storage pill CSS must remain removed.", errors)

    require("python3 tools/verify_wc2026_account_save_action_target.py" in makefile,
            "Makefile verify must include this joined persistence verifier.", errors)

    if errors:
        print("Joined live-picks persistence verification failed: " + "; ".join(errors))
        return 1

    print("OK: joined player persistence is live autosave with one-time conflict handling and no Save/Load player commands.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
