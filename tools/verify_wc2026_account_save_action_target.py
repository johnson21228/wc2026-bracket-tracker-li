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
    view = Path("site/js/mvc/view.js").read_text()

    require('import { createAccountSaveActionSurface } from "./identity/AccountSaveActionSurface.js";' in app,
            "App must import AccountSaveActionSurface.", errors)
    require("createAccountSaveActionSurface({" in app and "model," in app and "remoteActive: bracketStoreOptions.remoteActive === true" in app,
            "App must mount account persistence with model plus dev remote awareness.", errors)
    require("StorageModeSurface" not in app,
            "App must not mount the old persistent local storage pill.", errors)

    require("function getAccountSaveBracketDocument" in model and 'buildRemoteBracketDocument("account-save-button")' in model,
            "Model must expose a canonical BracketDocument snapshot for explicit account saving.", errors)
    require("function importAccountBracketDocument" in model and "importPicksSnapshot({ picks: incomingPicks })" in model,
            "Model must import saved account BracketDocument picks through the existing local pick import path.", errors)
    require("getAccountSaveBracketDocument," in model and "importAccountBracketDocument," in model,
            "Model API must expose account save/load methods.", errors)

    require('"Save Picks"' in surface and '"Sign in to save and load picks"' in surface,
            "Account persistence surface must expose signed-out save/load explanation.", errors)
    require('"Load Saved"' in surface and '"Saved account picks found"' in surface,
            "Signed-in account persistence must expose a saved-picks load surface.", errors)
    require('"Account persistence ready"' in surface and '"Saved to account"' in surface,
            "Signed-in account persistence must show account persistence status.", errors)
    require("loadUserBracket(accountUserId)" in surface and "saveUserBracket(bracketDocument)" in surface,
            "Account persistence must check/load and save through SupabaseBracketStore.", errors)
    require("localPickCount() === 0" in surface and 'render("remote-found")' in surface,
            "Remote picks may auto-load only when there are no local picks; conflicts must stay explicit.", errors)
    require("loadSavedPicksFromAccount({ automatic: false })" in surface,
            "Saved account picks must be explicitly loadable when local picks exist.", errors)
    require("localStorage" not in surface,
            "Account persistence surface must not use localStorage directly.", errors)

    require("wc2026:account-picks-loaded" in controller and "redraw();" in controller,
            "Controller must redraw after account picks are loaded without owning Supabase persistence.", errors)
    for rel, text in {
        "site/js/mvc/controller.js": controller,
        "site/js/mvc/view.js": view,
    }.items():
        require("SupabaseBracketStore" not in text and "saveUserBracket" not in text and "loadUserBracket" not in text and "user_brackets" not in text,
                f"{rel} must not own account persistence.", errors)

    require(".account-save-action" in css and ".account-save-action-button" in css,
            "Account persistence surface must have browser chrome styling.", errors)
    require(".storage-mode-status" not in css,
            "Persistent local storage pill CSS must be removed.", errors)

    require("python3 tools/verify_wc2026_account_save_action_target.py" in makefile,
            "Makefile verify must include account persistence verifier.", errors)

    if errors:
        print("Account persistence verification failed: " + "; ".join(errors))
        return 1

    print("OK: signed-in account persistence is the primary save/load surface with explicit conflict-safe restore.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
