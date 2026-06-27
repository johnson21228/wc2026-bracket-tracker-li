#!/usr/bin/env python3
from pathlib import Path

source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()

errors = []
if "Keep this board" in source:
    errors.append("Joined play must not preserve local board picks.")
if "Use saved picks" in source:
    errors.append("Old Use saved picks label must not remain.")
if "Saved picks have been loaded." not in source:
    errors.append("Joined-play message must use simple player-facing loaded-picks copy.")
if "Local draft picks are ignored for joined play" in source:
    errors.append("Joined-play message must not expose local draft technical language.")

if errors:
    raise SystemExit("\n".join(errors))

print("OK: Account save action targets joined Supabase bracket authority only.")
