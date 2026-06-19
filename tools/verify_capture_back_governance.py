#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(path, description=None):
    if not (ROOT / path).exists():
        errors.append(f"missing {description or path}: {path}")

root_reports = sorted(p.name for p in ROOT.glob("CAPTURE_BACK_*.md"))
if root_reports:
    errors.append("root-level Capture Back reports are not allowed: " + ", ".join(root_reports))

require("captures", "current Capture Back directory")
require("captures/CAPTURE_BACK_CB_GOVERNANCE.md", "CB governance Capture Back report")
require("li/repo/capture_back_governance_rule.md", "CB governance LI rule")
require("docs/repo/capture_back_governance.md", "CB governance doc")
require("cards/220_enforce_capture_back_governance_card.md", "CB governance card")
require("prompts/implement_capture_back_governance.md", "CB governance prompt")

makefile = ROOT / "Makefile"
if makefile.exists():
    txt = makefile.read_text()
    if "python3 tools/verify_capture_back_governance.py" not in txt:
        errors.append("Makefile verify target does not run tools/verify_capture_back_governance.py")
else:
    errors.append("missing Makefile")

map_file = ROOT / "MAP.md"
if map_file.exists():
    txt = map_file.read_text()
    required = [
        "captures/",
        "CAPTURE_BACK_CB_GOVERNANCE.md",
        "capture_back_governance_rule.md",
    ]
    for token in required:
        if token not in txt:
            errors.append(f"MAP.md missing expected Capture Back governance reference: {token}")
else:
    errors.append("missing MAP.md")

if errors:
    print("WC2026 Capture Back governance verification failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("OK: Capture Back governance keeps current reports in captures/ and blocks root CB churn.")
