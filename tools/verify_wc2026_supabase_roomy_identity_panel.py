#!/usr/bin/env python3
from pathlib import Path

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

index = Path("site/index.html").read_text()
identity = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
auth = Path("site/js/services/SupabaseAuthService.js").read_text()
css = Path("site/css/app.css").read_text()
makefile = Path("Makefile").read_text()
app_js = Path("site/js/app.js").read_text() if Path("site/js/app.js").exists() else ""
controller_js = Path("site/js/mvc/controller.js").read_text() if Path("site/js/mvc/controller.js").exists() else ""
repository_js = Path("site/js/services/BracketRepository.js").read_text() if Path("site/js/services/BracketRepository.js").exists() else ""

require('data-auth-disabled="true"' not in index, "identity surface must not be disabled in HTML")
require('data-auth-mode="identity-panel"' in index, "identity surface must advertise identity-panel mode")
require("identity-panel-backdrop" in identity, "identity surface must render a roomy panel backdrop")
require("identity-panel-form" in identity, "identity surface must render panel form instead of cramped header form")
require("supabase-auth-email-panel" in identity, "identity panel must provide a dedicated full email input")
require("data-identity-panel-open" in identity, "compact header button must open the identity panel")
require("signInWithMagicLink" in identity, "identity panel must use explicit magic-link auth contract")
require("cooldownUntil" in identity and "Wait ${cooldownSeconds}s" in identity, "identity panel must throttle repeated magic-link clicks")
require("identity-signin-form" not in identity, "old inline header sign-in form must be removed")
require("signInWithMagicLink" in auth and "getCurrentSession" in auth, "auth service must expose identity-only auth methods")
require("identity-panel-backdrop" in css and "width: min(560px" in css, "CSS must style roomy identity panel")
require(".identity-panel-form input" in css and "width: 100%" in css, "panel email input must be full width")
require("Card 276: roomy Supabase identity panel" in css, "CSS must capture Card 276 intent")
require("verify_wc2026_supabase_roomy_identity_panel.py" in makefile, "make verify must include roomy identity panel verifier")

active_runtime = "\n".join([app_js, controller_js, repository_js])
require("new SupabaseBracketStore" not in active_runtime, "active runtime must not instantiate SupabaseBracketStore")
require("createSupabaseBracketStore" not in active_runtime, "active runtime must not create SupabaseBracketStore")
require("RemoteBracketStore" not in active_runtime, "active runtime must not switch to a remote bracket store")

if errors:
    print("WC2026 Supabase roomy identity panel verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 Supabase sign-in opens a roomy identity panel while bracket persistence remains local.")
