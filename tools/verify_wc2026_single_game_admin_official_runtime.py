#!/usr/bin/env python3
from pathlib import Path

model = Path("site/js/mvc/model.js").read_text()
store = Path("site/js/services/SupabaseBracketStore.js").read_text()
account = Path("site/js/identity/AccountSaveActionSurface.js").read_text()

errors = []

# Current single-game LI:
# - game1 is canonical persisted game id.
# - Admin_ Supabase row may act as Admin_/official R32 authority during reset/migration.
# - persisted team IDs must resolve to canonical team catalog IDs; invalid IDs are cleared.
# - joined play uses Supabase saved bracket authority only; no local/saved conflict choice.

if "const DEFAULT_GAME_ID = \"game1\"" not in store:
    errors.append("SupabaseBracketStore must canonicalize persisted game id to game1.")

if "ADMIN_OFFICIAL_SUPABASE_USER_ID" not in store:
    errors.append("Admin_ Supabase user id must be explicit for Admin_/official migration authority.")

if "loaded Admin_ player row as Admin_/official R32 authority" not in store:
    errors.append("Admin_ player row must be accepted as Admin_/official R32 authority during reset/migration.")

if "clearUnknownTeamPicks" not in model:
    errors.append("Model must clear persisted picks with undefined canonical team IDs.")

if "WC2026 LI FAIL" not in model:
    errors.append("Model must loudly report LI failure for undefined persisted team IDs.")

if "Local draft picks are ignored for joined play" not in account:
    errors.append("Joined play must ignore local draft picks and use Supabase authority.")

for stale in [
    "You already have picks saved. Use saved picks or keep this board?",
    "Keep this board",
]:
    if stale in account:
        errors.append(f"Stale local/saved conflict UI remains: {stale}")

if errors:
    print("WC2026 single-game Admin_/official runtime verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: WC2026 single-game Admin_/official runtime uses game1, Admin_ migration authority, strict canonical team IDs, and joined Supabase-only play.")
