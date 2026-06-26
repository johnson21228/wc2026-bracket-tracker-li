#!/usr/bin/env python3
from pathlib import Path

source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()

errors = []
if "Keep this board" in source:
    errors.append("Joined play must not preserve local board picks.")
if "Use saved picks" in source:
    errors.append("Old Use saved picks label must not remain.")
if "Local draft picks are ignored for joined play" not in source:
    errors.append("Joined-play message must explain local draft picks are ignored.")

if errors:
    raise SystemExit("\n".join(errors))

print("OK: Account save action targets joined Supabase bracket authority only.")
