#!/usr/bin/env python3
from pathlib import Path

source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()

errors = []
if "You already have picks saved. Use saved picks or keep this board?" in source:
    errors.append("Old saved-vs-current-board conflict prompt must not remain.")
if "Keep this board" in source:
    errors.append("Joined play must not offer Keep this board.")
if "Your picks have been loaded." not in source:
    errors.append("Joined play must use simple player-facing loaded-picks copy.")
if "Local draft picks are ignored for joined play" in source:
    errors.append("Joined play must not expose local draft technical language.")

if errors:
    raise SystemExit("\n".join(errors))

print("OK: Supabase identity surface uses joined-play saved bracket authority, not local/saved conflict choice.")
