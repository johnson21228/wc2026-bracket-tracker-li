#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "li/world_cup/public_multi_user_play_rule.md": [
        "public site address",
        "anonymous local draft",
        "signed-in saved draft",
        "site-running invariant",
        "Supabase",
    ],
    "li/world_cup/canonical_pick_state_storage_model_rule.md": [
        "Game 1 expected pick count: 64",
        "Game 2 expected pick count: 32",
        "third-place winner",
        "semifinal losers",
        "LocalStorageBracketStore",
        "RemoteBracketStore",
    ],
    "li/world_cup/site_running_public_play_invariant_rule.md": [
        "site must remain usable",
        "anonymous/local pick behavior works",
        "local storage remains a fallback",
        "make verify",
        "make pack",
    ],
    "docs/architecture/wc2026_public_multi_user_play_architecture.md": [
        "invite-ready",
        "Canonical pick-state JSON",
        "LocalStorageBracketStore OR RemoteBracketStore",
        "two JSON documents per user",
    ],
    "docs/architecture/wc2026_canonical_pick_state_storage_model.md": [
        "Game 1 expected total: 64 picks",
        "Game 2 expected total: 32 picks",
        "THIRD-PLACE-WINNER",
        "Final Four",
    ],
    "docs/backend/wc2026_inexpensive_backend_options.md": [
        "Supabase Auth",
        "Row Level Security",
        "user_brackets",
        "service role key must never be committed",
    ],
    "docs/dev/todo_public_multi_user_play.md": [
        "Route local storage/export through canonical pick-state JSON",
        "Add Supabase schema/RLS docs",
        "Keep-site-running checklist",
    ],
    "captures/CAPTURE_BACK_PUBLIC_MULTI_USER_PLAY_LI.md": [
        "Game 1 stores 64 picks",
        "Game 2 stores 32 picks",
        "site-running invariant",
    ],
}

card_paths = [
    "cards/211_define_canonical_public_play_pick_state_storage_card.md",
    "cards/212_route_local_storage_through_canonical_pick_state_card.md",
    "cards/213_define_remote_bracket_store_contract_card.md",
    "cards/214_add_signed_in_user_ui_shell_card.md",
    "cards/215_add_supabase_backend_schema_card.md",
    "cards/216_implement_supabase_remote_bracket_store_card.md",
    "cards/217_add_save_load_sync_status_card.md",
    "cards/218_add_submit_lock_bracket_behavior_card.md",
    "cards/219_add_invite_ready_public_play_verification_card.md",
]

errors = []
for rel, needles in checks.items():
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            errors.append(f"{rel} missing expected text: {needle}")

for rel in card_paths:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing card {rel}")

makefile = ROOT / "Makefile"
if not makefile.exists():
    errors.append("missing Makefile")
elif "tools/verify_wc2026_public_multi_user_play_li.py" not in makefile.read_text(encoding="utf-8"):
    errors.append("Makefile verify target does not include public multi-user play LI verifier")

# Ensure no accidental backend secret placeholders were added as real env names with values.
secret_patterns = ["service_role", "SERVICE_ROLE", "supabase_service", "SUPABASE_SERVICE"]
for rel in list(checks) + card_paths:
    path = ROOT / rel
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    for pat in secret_patterns:
        if pat in text and "never" not in text.lower():
            errors.append(f"{rel} may reference backend secret pattern without warning context: {pat}")

if errors:
    for err in errors:
        print(err)
    sys.exit(1)

print("OK: WC2026 public multi-user play LI, canonical storage model, and site-running invariant are captured and verified.")
