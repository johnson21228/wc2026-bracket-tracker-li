#!/usr/bin/env python3
from pathlib import Path

account = Path("site/js/identity/AccountSaveActionSurface.js").read_text()
store = Path("site/js/services/SupabaseBracketStore.js").read_text()

errors = []
if "Keep this board" in account or "Use saved picks" in account:
    errors.append("Joined-player local/saved conflict path must not remain.")
if "Your picks have been loaded." not in account:
    errors.append("Joined-player surface must use simple player-facing loaded-picks copy.")
if "Local draft picks are ignored for joined play" in account:
    errors.append("Joined-player surface must not expose local draft technical language.")
if "loadUserBracket" not in store:
    errors.append("SupabaseBracketStore must load joined saved bracket.")

if errors:
    raise SystemExit("\n".join(errors))

print("OK: active Supabase bracket store is joined-play authority without local conflict choice.")
