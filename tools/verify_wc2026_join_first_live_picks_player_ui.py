#!/usr/bin/env python3
from pathlib import Path

source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()

errors = []
for stale in [
    "You already have picks saved. Use saved picks or keep this board?",
    "Use saved picks",
    "Keep this board",
]:
    if stale in source:
        errors.append(f"Stale joined-player conflict UI remains: {stale}")

if "Your picks have been loaded." not in source:
    errors.append("Joined-first UI must use simple player-facing loaded-picks copy.")
if "Local draft picks are ignored for joined play" in source:
    errors.append("Joined-first UI must not expose local draft technical language.")

if errors:
    raise SystemExit("\n".join(errors))

print("OK: join-first live picks UI no longer offers local/saved conflict choice.")
