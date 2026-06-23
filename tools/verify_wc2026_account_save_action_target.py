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
    makefile = Path("Makefile").read_text()
    controller = Path("site/js/mvc/controller.js").read_text()
    view = Path("site/js/mvc/view.js").read_text()

    require('import { createAccountSaveActionSurface } from "./identity/AccountSaveActionSurface.js";' in app,
            "App must import AccountSaveActionSurface.", errors)
    require("createAccountSaveActionSurface({" in app and "model," in app and "remoteActive: bracketStoreOptions.remoteActive === true" in app,
            "App must mount account save action near auth/account chrome and pass the model plus dev remote awareness.", errors)
    require("StorageModeSurface" not in app,
            "App must not mount the old persistent local storage pill.", errors)

    require("function getAccountSaveBracketDocument" in model and 'buildRemoteBracketDocument("account-save-button")' in model,
            "Model must expose a canonical BracketDocument snapshot for explicit account saving.", errors)
    require("getAccountSaveBracketDocument," in model,
            "Model API must return getAccountSaveBracketDocument.", errors)

    require('"Save Picks"' in surface and '"Sign in to save"' in surface,
            "Account save action must expose a Save Picks target and signed-out explanation.", errors)
    require('"Save to account"' in surface and '"Saved to account"' in surface,
            "Account save action must communicate explicit account persistence status.", errors)
    require("new SupabaseBracketStore()" in surface and "saveUserBracket(bracketDocument)" in surface,
            "Save Picks must wire exactly one explicit SupabaseBracketStore save.", errors)
    require("getAccountSaveBracketDocument({ userId: accountUserId })" in surface,
            "Save Picks must save the current local-first model snapshot for the signed-in account.", errors)
    require("localStorage" not in surface and "loadUserBracket" not in surface,
            "Account save action must not use localStorage directly or load/overwrite remote picks.", errors)

    require(".account-save-action" in css and ".account-save-action-button" in css,
            "Account save action must have browser chrome styling.", errors)
    require(".storage-mode-status" not in css,
            "Persistent local storage pill CSS must be removed.", errors)

    require("python3 tools/verify_wc2026_account_save_action_target.py" in makefile,
            "Makefile verify must include account save action verifier.", errors)

    for rel, text in {
        "site/js/mvc/controller.js": controller,
        "site/js/mvc/view.js": view,
    }.items():
        require("SupabaseBracketStore" not in text and "saveUserBracket" not in text and "user_brackets" not in text,
                f"{rel} must not own account persistence.", errors)

    if errors:
        print("Account save action verification failed: " + "; ".join(errors))
        return 1

    print("OK: Save Picks explicitly writes the current local-first bracket to account storage without automatic remote writes or remote load.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
