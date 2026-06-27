#!/usr/bin/env python3
from pathlib import Path

source = Path("site/js/identity/SupabaseIdentitySurface.js").read_text()
makefile = Path("Makefile").read_text()

required_source = [
    "Join the Pool",
    "Playing Bracketeering requires you to join the Pool.",
    "Use Google sign-in to avoid email verification. If you use email, check your spam folder if the sign-in link does not appear in your inbox.",
    "Not joined yet.",
    "Profile",
    "Edit your player name or log out.",
    "Edit your player name below, or log out.",
    "Joined status:",
    "Joined",
]

required_docs = [
    "captures/CAPTURE_BACK_JOIN_REQUIRED_DIALOG_COPY.md",
    "cards/1030_join_required_dialog_copy_card.md",
    "li/world_cup/join_required_dialog_copy_rule.md",
]

forbidden = [
    "You can still explore the board before joining",
    "Continue with Google, email yourself a sign-in link, or keep playing locally on this browser",
    "keep playing locally",
    "No account needed for local play",
    "Local bracket remains active",
    "You can still explore before joining",
    "Your picks are live.",
]

errors = []

for token in required_source:
    if token not in source:
        errors.append(f"Missing required Join/Profile dialog copy: {token}")

for token in forbidden:
    if token in source:
        errors.append(f"Forbidden stale Join/Profile dialog copy remains: {token}")

for doc in required_docs:
    path = Path(doc)
    if not path.exists():
        errors.append(f"Missing CB artifact: {doc}")

if "python3 tools/verify_wc2026_join_required_dialog_copy.py" not in makefile:
    errors.append("Makefile must run verify_wc2026_join_required_dialog_copy.py")

if errors:
    print("WC2026 join required dialog copy verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Join/Profile dialog requires joining the Pool and signed-in Profile only supports player-name editing and logout.")
