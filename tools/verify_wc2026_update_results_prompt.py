#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "prompts/update_results_from_web.md": [
        "UPDATE RESULTS",
        "patchable-final-candidate",
        "live-watchlist",
        "future-scheduled",
        "PATCH",
        "WATCH",
        "WAIT",
        "CONFLICT",
        "Do not patch a match as final unless",
        "Use current internet search",
        "site/data/current/group_matches.json",
        "source/text/",
        "make publish-pages",
    ],
    "docs/workflows/update_results_from_web.md": [
        "UPDATE RESULTS Workflow",
        "PATCH",
        "WATCH",
        "WAIT",
        "CONFLICT",
    ],
    "li/workflow/update_results_from_web_protocol.md": [
        "UPDATE RESULTS Protocol",
        "Final",
        "WATCH",
    ],
    "cards/202_capture_update_results_prompt_card.md": [
        "Card 202",
        "UPDATE RESULTS",
        "confirmed final results",
    ],
    "capture_back/CAPTURE_BACK_UPDATE_RESULTS_PROMPT.md": [
        "UPDATE RESULTS Prompt",
        "live/in-progress",
    ],
    "LLM_READ_FIRST.md": [
        "UPDATE RESULTS",
        "prompts/update_results_from_web.md",
    ],
}

errors = []
for rel, needles in checks.items():
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        continue
    text = path.read_text()
    for needle in needles:
        if needle not in text:
            errors.append(f"{rel} missing token: {needle}")

if errors:
    raise SystemExit("WC2026 UPDATE RESULTS prompt verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 UPDATE RESULTS prompt is captured and verified.")
