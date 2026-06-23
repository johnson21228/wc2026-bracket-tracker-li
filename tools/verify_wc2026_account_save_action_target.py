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
    makefile = Path("Makefile").read_text()

    require('import { createAccountSaveActionSurface } from "./identity/AccountSaveActionSurface.js";' in app,
            "App must import AccountSaveActionSurface.", errors)
    require("createAccountSaveActionSurface({" in app and "remoteActive: bracketStoreOptions.remoteActive === true" in app,
            "App must mount account save action near auth/account chrome and preserve dev remote awareness.", errors)
    require("StorageModeSurface" not in app,
            "App must not mount the old persistent local storage pill.", errors)

    require('"Save Picks"' in surface and '"Sign in to save"' in surface,
            "Account save action must expose a Save Picks target and signed-out explanation.", errors)
    require('"Account save target"' in surface,
            "Account save action must identify that persistence is an explicit account-save target.", errors)
    require("saveUserBracket" not in surface and "loadUserBracket" not in surface and "SupabaseBracketStore" not in surface,
            "Account save action target must not wire remote persistence yet.", errors)
    require("disabled: true" in surface,
            "Save Picks target must remain disabled until the persistence wiring CB.", errors)

    require(".account-save-action" in css and ".account-save-action-button" in css,
            "Account save action must have browser chrome styling.", errors)
    require(".storage-mode-status" not in css,
            "Persistent local storage pill CSS must be removed.", errors)

    require("python3 tools/verify_wc2026_account_save_action_target.py" in makefile,
            "Makefile verify must include account save action target verifier.", errors)

    if errors:
        print("Account save action target verification failed: " + "; ".join(errors))
        return 1

    print("OK: persistent local storage pill is replaced by a first-class account Save Picks action target without enabling remote writes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
