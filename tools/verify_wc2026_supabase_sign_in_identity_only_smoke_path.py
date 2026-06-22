#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

errors = []

site_index = ROOT / "site/index.html"
identity_surface = ROOT / "site/js/identity/SupabaseIdentitySurface.js"
auth_service = ROOT / "site/js/services/SupabaseAuthService.js"
bracket_repository = ROOT / "site/js/services/BracketRepository.js"
active_session = ROOT / "site/js/services/ActiveBracketSession.js"
supabase_store = ROOT / "site/js/services/SupabaseBracketStore.js"
makefile = ROOT / "Makefile"

required_files = [
    site_index,
    identity_surface,
    auth_service,
    bracket_repository,
    active_session,
    supabase_store,
]

for path in required_files:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")

index_text = site_index.read_text() if site_index.exists() else ""
identity_text = identity_surface.read_text() if identity_surface.exists() else ""
auth_text = auth_service.read_text() if auth_service.exists() else ""
repo_text = bracket_repository.read_text() if bracket_repository.exists() else ""
session_text = active_session.read_text() if active_session.exists() else ""
store_text = supabase_store.read_text() if supabase_store.exists() else ""
make_text = makefile.read_text() if makefile.exists() else ""

# The UI should no longer be hard-paused.
if 'data-auth-disabled="true"' in index_text:
    errors.append("site index still hard-disables Supabase auth UI with data-auth-disabled=true")

for token in [
    "signInWithMagicLink",
    "signOut",
    "onAuthStateChange",
    "getCurrentSession",
]:
    if token not in auth_text:
        errors.append(f"SupabaseAuthService missing identity-only auth capability: {token}")

for token in [
    "SupabaseIdentitySurface",
    "signIn",
    "signOut",
    "signed",
    "local",
]:
    if token not in identity_text:
        errors.append(f"SupabaseIdentitySurface missing expected identity-only UI token: {token}")

# Identity-only means no remote bracket persistence has been activated.
active_runtime_text = "\n".join([repo_text, session_text, identity_text, auth_text, index_text])

if "new SupabaseBracketStore" in active_runtime_text:
    errors.append("active site runtime must not instantiate SupabaseBracketStore in the identity-only smoke path")

if "createRemoteActiveBracketSession" in active_runtime_text and "createRemoteActiveBracketSessionPlaceholder" not in active_runtime_text:
    errors.append("identity-only smoke path must not create a real remote active bracket session")

if "user_brackets" in active_runtime_text:
    errors.append("identity-only active runtime must not directly reference user_brackets persistence")

if "supabase.from" in active_runtime_text or ".from(\"user_brackets\")" in active_runtime_text or ".from('user_brackets')" in active_runtime_text:
    errors.append("identity-only active runtime must not write/read Supabase bracket tables")

if "LocalStorageBracketStore" not in repo_text:
    errors.append("BracketRepository must continue to default to LocalStorageBracketStore")

if "createLocalActiveBracketSession" not in repo_text:
    errors.append("BracketRepository must continue to create the local active bracket session")

# The SupabaseBracketStore file may exist, but it must remain isolated from the active runtime.
if "class SupabaseBracketStore" not in store_text and "function SupabaseBracketStore" not in store_text and "SupabaseBracketStore" not in store_text:
    errors.append("SupabaseBracketStore should still exist for later guarded persistence activation")

if "verify_wc2026_supabase_sign_in_identity_only_smoke_path.py" not in make_text:
    errors.append("Makefile must include identity-only smoke path verifier")

if "run_wc2026_supabase_remote_smoke_path.js" in make_text and "node tools/run_wc2026_supabase_remote_smoke_path.js" in make_text:
    errors.append("Makefile must not run the live remote Supabase smoke harness")

if errors:
    print("WC2026 Supabase sign-in identity-only smoke path verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 Supabase sign-in UI is enabled as an identity-only smoke path while bracket persistence remains local.")
