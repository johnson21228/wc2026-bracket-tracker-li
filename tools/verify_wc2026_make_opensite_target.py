#!/usr/bin/env python3
from pathlib import Path

makefile = Path("Makefile")
if not makefile.exists():
    raise SystemExit("Makefile is missing")

text = makefile.read_text()
required_terms = [
    "opensite:",
    "stopsite:",
    "python3 -m http.server 8000 -d site",
    "open http://localhost:8000",
    "/tmp/wc2026-bracket-tracker-site.pid",
    "/tmp/wc2026-bracket-tracker-site.log",
]
missing = [term for term in required_terms if term not in text]
if missing:
    raise SystemExit("Makefile opensite/stopsite target verification failed; missing: " + ", ".join(missing))

if "python3 tools/verify_wc2026_make_opensite_target.py" not in text:
    raise SystemExit("Makefile verify target does not run verify_wc2026_make_opensite_target.py")

print("WC2026 make opensite target verification passed.")
