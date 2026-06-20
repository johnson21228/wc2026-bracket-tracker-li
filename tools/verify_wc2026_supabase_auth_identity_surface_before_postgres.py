#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    "cards/231_implement_supabase_auth_identity_surface_before_postgres_card.md",
    "docs/architecture/bracketeering_supabase_auth_identity_surface.md",
    "li/world_cup/supabase_auth_identity_surface_before_postgres_rule.md",
    "site/js/config/supabase.public.js",
    "site/js/services/SupabaseAuthService.js",
    "site/js/identity/SupabaseIdentitySurface.js",
    "tools/verify_wc2026_supabase_auth_identity_surface_before_postgres.py",
]

missing = [path for path in required if not (ROOT / path).exists()]
if missing:
    raise SystemExit("Missing Card 231 files: " + ", ".join(missing))

index = (ROOT / "site/index.html").read_text()
app_js = (ROOT / "site/js/app.js").read_text()
css = (ROOT / "site/css/app.css").read_text()
auth_service = (ROOT / "site/js/services/SupabaseAuthService.js").read_text()
surface = (ROOT / "site/js/identity/SupabaseIdentitySurface.js").read_text()
config = (ROOT / "site/js/config/supabase.public.js").read_text()
makefile = (ROOT / "Makefile").read_text()

checks = {
    "site index has upper-right identity mount": "data-supabase-identity-surface" in index,
    "app imports auth service": "SupabaseAuthService.js" in app_js and "createSupabaseAuthService" in app_js,
    "app imports identity surface": "SupabaseIdentitySurface.js" in app_js and "createSupabaseIdentitySurface" in app_js,
    "app starts identity surface": "identitySurface.start()" in app_js,
    "css styles identity surface": "supabase-identity-surface" in css and "identity-card" in css,
    "auth service uses Supabase client": "createClient" in auth_service,
    "auth service reads session": ".auth.getSession" in auth_service,
    "auth service listens for auth changes": ".auth.onAuthStateChange" in auth_service,
    "auth service uses magic link/OTP": ".auth.signInWithOtp" in auth_service,
    "auth service supports sign out": ".auth.signOut" in auth_service,
    "auth surface warns local persistence": "Local bracket for now" in surface,
    "auth surface contains sign-in copy": "Sign in to save" in surface,
    "config defaults disabled": "enabled: false" in config,
    "config warns no service role": "service_role" in config,
    "verifier wired into make verify": "verify_wc2026_supabase_auth_identity_surface_before_postgres.py" in makefile,
}

failed = [name for name, ok in checks.items() if not ok]
if failed:
    raise SystemExit("Card 231 verification failed: " + "; ".join(failed))

for forbidden in [".from(", "user_brackets", "profiles"]:
    if forbidden in auth_service:
        raise SystemExit(f"Auth service must not call Postgres persistence yet: found {forbidden}")

if "SupabaseBracketStore" in auth_service or "SupabaseBracketStore" in surface:
    raise SystemExit("Card 231 must not implement SupabaseBracketStore yet.")

print("OK: WC2026 Supabase Auth identity surface is implemented before Postgres persistence while localStorage remains active.")
