#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

errors = []

harness = ROOT / "tools/run_wc2026_supabase_remote_smoke_path.js"
guard = ROOT / "site/js/services/RemoteStoreActivationGuard.js"
makefile = ROOT / "Makefile"

if not harness.exists():
    errors.append("missing guarded Supabase remote smoke harness")
else:
    text = harness.read_text()
    required_tokens = [
        "WC2026_SUPABASE_REMOTE_SMOKE",
        "WC2026_SUPABASE_SMOKE_USER_ID",
        "assertRemoteStoreActivationAllowed",
        "explicitDeveloperSmoke: true",
        "publicRuntime: false",
        "SupabaseBracketStore",
        "createEmptyBracketDocument",
        "saveUserBracket",
        "loadUserBracket",
        "persistSession: false",
        "autoRefreshToken: false",
        "detectSessionInUrl: false",
    ]
    for token in required_tokens:
        if token not in text:
            errors.append(f"harness missing required token: {token}")

    forbidden_tokens = [
        "document.querySelector",
        "window.location",
        "localStorage",
        "createRemoteActiveBracketSessionPlaceholder",
    ]
    for token in forbidden_tokens:
        if token in text:
            errors.append(f"harness must not touch public runtime/browser state: {token}")

if not guard.exists():
    errors.append("missing RemoteStoreActivationGuard")
else:
    guard_text = guard.read_text()
    if "explicitDeveloperSmoke" not in guard_text:
        errors.append("RemoteStoreActivationGuard must expose explicitDeveloperSmoke")
    if "publicRuntime" not in guard_text:
        errors.append("RemoteStoreActivationGuard must distinguish publicRuntime")
    if "DEFAULT_REMOTE_STORE_ACTIVATION_GUARD.assertRemoteStoreEnabled()" not in guard_text:
        errors.append("RemoteStoreActivationGuard must remain fail-closed for normal remote activation")

if not makefile.exists():
    errors.append("missing Makefile")
else:
    make_text = makefile.read_text()
    if "node tools/run_wc2026_supabase_remote_smoke_path.js" in make_text:
        errors.append("live remote smoke harness must not run as part of make verify")

site_files = [
    "site/index.html",
    "site/js/app.js",
    "site/js/mvc/controller.js",
    "site/js/mvc/view.js",
    "site/js/services/BracketRepository.js",
    "site/js/services/ActiveBracketSession.js",
]

for rel in site_files:
    path = ROOT / rel
    if path.exists() and "run_wc2026_supabase_remote_smoke_path" in path.read_text():
        errors.append(f"public runtime must not reference remote smoke harness: {rel}")

if errors:
    print("WC2026 guarded Supabase remote smoke path verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 guarded Supabase remote smoke path is explicit, developer-only, and not wired into public runtime.")
