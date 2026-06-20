#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "cards/230_define_supabase_identity_ui_surface_card.md",
    "docs/architecture/bracketeering_supabase_identity_ui_surface.md",
    "li/world_cup/supabase_identity_ui_surface_rule.md",
]

REQUIRED_TEXT = {
    "cards/230_define_supabase_identity_ui_surface_card.md": [
        "upper-right identity/status surface",
        "not a custom authentication system",
        "Supabase owns the hard identity/auth machinery",
        "Sign in to save",
        "Same BracketDocument. Different store.",
        "BracketRepository → LocalStorageBracketStore",
        "BracketRepository → SupabaseBracketStore",
        "Do not build public player-pick views yet",
        "Do not let board/menu/controller code call Supabase directly",
        "Pages owns View/Controller/runtime model",
        "Supabase owns Auth/Postgres/RLS/persistence",
    ],
    "docs/architecture/bracketeering_supabase_identity_ui_surface.md": [
        "thin site-owned shell around Supabase Auth",
        "Top-right: Identity/status surface",
        "User signs in",
        "Supabase Auth provides current user id",
        "user_brackets.picks_json",
        "Same `BracketDocument`. Different store.",
        "The board and pick controllers should not know which store is active",
        "Do not build custom auth",
    ],
    "li/world_cup/supabase_identity_ui_surface_rule.md": [
        "thin site-owned shell around Supabase Auth",
        "The site must not implement custom authentication",
        "Same `BracketDocument`. Different store.",
        "Board views and pick controllers must not know whether persistence is localStorage or Supabase",
        "no direct Supabase calls from board/menu/controller code",
    ],
}

makefile = ROOT / "Makefile"
if not makefile.exists():
    raise SystemExit("Missing Makefile")
make_text = makefile.read_text()
if "python3 tools/verify_wc2026_supabase_identity_ui_surface.py" not in make_text:
    raise SystemExit("Makefile must run verify_wc2026_supabase_identity_ui_surface.py")

for rel in REQUIRED_FILES:
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"Missing required file: {rel}")
    text = path.read_text()
    for needle in REQUIRED_TEXT[rel]:
        if needle not in text:
            raise SystemExit(f"{rel} missing required text: {needle}")

print("OK: WC2026 Supabase identity UI surface is defined as a thin site-owned shell around Supabase Auth.")
