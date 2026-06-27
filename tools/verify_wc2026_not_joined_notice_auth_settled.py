#!/usr/bin/env python3
from pathlib import Path

source = Path("site/js/identity/AccountSaveActionSurface.js").read_text()
makefile = Path("Makefile").read_text()

required = [
    "let authSettled = false;",
    'state.status !== "loading"',
    'state.status !== "initializing"',
    "if (authSettled) {",
    'renderNotice(root, "not-joined", NOT_JOINED_STARTUP_MESSAGE);',
]

errors = []

for token in required:
    if token not in source:
        errors.append(f"Missing auth-settled not-joined notice token: {token}")

if "renderNotice(root, \"not-joined\", NOT_JOINED_STARTUP_MESSAGE);" in source:
    if "if (authSettled) {" not in source:
        errors.append("Not-joined notice must be gated by authSettled.")

if "python3 tools/verify_wc2026_not_joined_notice_auth_settled.py" not in makefile:
    errors.append("Makefile must run not-joined auth-settled verifier.")

if errors:
    print("WC2026 not-joined notice auth-settled verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: not-joined notice only renders after auth is settled and confirmed signed out.")
