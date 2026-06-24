#!/usr/bin/env python3
from pathlib import Path

checks = {
    "li/repo/paste_back_terminal_output_contract_rule.md": [
        "Paste Back Terminal Output Contract Rule",
        "successful noisy commands must be redirected to temp logs",
        "paste-back output must include compact PASS/FAIL lines",
        "successful verifier lists must not be pasted by default",
        "successful zip file lists must not be pasted by default",
        "full logs may be shown only when diagnosing failure",
    ],
    "docs/dev/paste_back_terminal_output_contract.md": [
        "This repo treats terminal output pasted into the II client as a compact signal surface.",
        "full successful make verify output",
        "full successful make pack zip listings",
        "VERIFY: PASS",
        "PACK: PASS",
        "PUBLISH: PASS",
        "tail -n 120 /tmp/wc2026_publish.log",
    ],
}

for path, tokens in checks.items():
    text = Path(path).read_text()
    for token in tokens:
        if token not in text:
            raise SystemExit(f"Missing token in {path}: {token}")

makefile = Path("Makefile").read_text()
if "tools/verify_wc2026_paste_back_terminal_output_contract.py" not in makefile:
    raise SystemExit("Makefile must run paste-back terminal output contract verifier")

print("OK: paste-back terminal output contract is captured and enforced.")
