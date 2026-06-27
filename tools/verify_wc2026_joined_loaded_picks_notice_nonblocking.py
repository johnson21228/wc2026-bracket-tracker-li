#!/usr/bin/env python3
from pathlib import Path

text = Path("site/js/identity/AccountSaveActionSurface.js").read_text()

errors = []

if "<p>${JOINED_PICKS_LOADED_MESSAGE}</p>" in text:
    errors.append("Saved-picks loaded message must not be embedded in the blocking notice template.")

if "renderNotice(" in text and "renderNotice(root" in text:
    for line in text.splitlines():
        if "renderNotice(" in line and "JOINED_PICKS_LOADED_MESSAGE" in line:
            errors.append("Saved-picks loaded message must not render through blocking renderNotice().")

if 'renderStatus(root, "loaded", JOINED_PICKS_LOADED_MESSAGE)' not in text:
    errors.append("Saved-picks loaded message should render through non-blocking renderStatus().")

if 'const JOINED_PICKS_LOADED_MESSAGE = "Saved picks have been loaded."' not in text:
    errors.append("Expected joined loaded-picks copy is missing or changed unexpectedly.")

if errors:
    print("Joined loaded-picks notice verifier failed:")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print("OK: joined loaded-picks message is non-blocking status, not a modal notice.")
