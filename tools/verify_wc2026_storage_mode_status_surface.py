#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8", errors="ignore")

def require(condition, message, errors):
    if not condition:
        errors.append(message)

def main():
    errors = []

    app = read("site/js/app.js")
    surface = read("site/js/identity/StorageModeSurface.js")
    css = read("site/css/app.css")
    makefile = read("Makefile")
    controller = read("site/js/mvc/controller.js")
    view = read("site/js/mvc/view.js")

    require('import { createStorageModeSurface } from "./identity/StorageModeSurface.js";' in app,
            "App must import the storage mode status surface.", errors)
    require("const bracketStoreOptions = await devSupabaseBracketStoreOptions(authService);" in app,
            "App must keep explicit bracket store options for status rendering.", errors)
    require("createStorageModeSurface({" in app and "remoteActive: bracketStoreOptions.remoteActive === true" in app,
            "App must render storage status from actual active store state.", errors)
    require("return { remoteActive: false }" in app and "remoteActive: true" in app,
            "Dev Supabase store selection must report whether remote mode is actually active.", errors)

    require('DEV_SUPABASE_STORE_FLAG = "devSupabaseBracketStore"' in surface,
            "Storage surface must know the hidden dev Supabase flag.", errors)
    require('"Playing locally"' in surface,
            "Storage surface must show Playing locally for normal gameplay.", errors)
    require('"Remote save test mode"' in surface,
            "Storage surface must show Remote save test mode only for active remote testing.", errors)
    require("remoteRequested && !signedIn" in surface,
            "Storage surface must handle dev flag requested without a signed-in session.", errors)
    require("createStorageModeSurface" in surface and "authService?.currentState?.()" in surface,
            "Storage surface must derive signed-in state from auth service without starting remote storage.", errors)
    require("bracketStore" not in surface and "saveUserBracket" not in surface and "loadUserBracket" not in surface,
            "Storage surface must not perform bracket persistence.", errors)

    require(".storage-mode-status" in css and "pointer-events: none" in css,
            "Storage mode status must be visible but non-interactive browser chrome.", errors)
    require("top: max(12px, env(safe-area-inset-top));" in css and "right: calc(max(12px, env(safe-area-inset-right)) + min(340px, 42vw) + 12px);" in css,
            "Storage mode status must live in the upper-right account chrome, left of login info.", errors)
    require("left: auto;" in css and "bottom: auto;" in css,
            "Storage mode status must no longer be anchored to the lower-left corner.", errors)
    require('python3 tools/verify_wc2026_storage_mode_status_surface.py' in makefile,
            "Makefile verify must include storage mode status verifier.", errors)

    for rel, text in {
        "site/js/mvc/controller.js": controller,
        "site/js/mvc/view.js": view,
    }.items():
        require("StorageMode" not in text and "SupabaseBracketStore" not in text and "user_brackets" not in text,
                f"{rel} must not own storage mode or Supabase persistence.", errors)

    if errors:
        print("Storage mode status surface verification failed: " + "; ".join(errors))
        return 1

    print("OK: storage mode status surface is visible, truthful, and does not enable remote save by default.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
