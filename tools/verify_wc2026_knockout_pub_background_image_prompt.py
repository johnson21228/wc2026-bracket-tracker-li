#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

checks = {
    "prompts/update_knockout_pub_background_image.md": [
        "UPDATE KNOCKOUT PUB BACKGROUND IMAGE",
        "site/assets/board/pub_background_game1.jpeg",
        "site/data/current/knockout_matches.json",
        "site/data/current/official_truth.json",
        "Base image",
        "Flag vs Flag",
        "TBD",
        "date at the top",
        "one row for each match",
        "as tall as it can be",
        "Do not rely on memory",
        "Do not guess teams",
        "make verify",
        "make pack",
    ],
    "docs/workflows/update_knockout_pub_background_image.md": [
        "UPDATE KNOCKOUT PUB BACKGROUND IMAGE Workflow",
        "knockout_matches.json",
        "official_truth.json",
        "Flag vs Flag",
        "TBD",
    ],
    "li/world_cup/knockout_pub_background_image_prompt_rule.md": [
        "Knockout Pub Background Image Prompt Rule",
        "schedule authority",
        "known R32 team-occupant truth",
        "Flags should be as tall",
    ],
    "cards/1021_knockout_pub_background_image_prompt_card.md": [
        "Card 1021",
        "Knockout Pub Background Image Prompt",
        "Verification is wired into `make verify`",
    ],
    "captures/CAPTURE_BACK_KNOCKOUT_PUB_BACKGROUND_IMAGE_PROMPT.md": [
        "Knockout Pub Background Image Prompt",
        "Flag vs Flag",
        "projection only",
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

makefile = ROOT / "Makefile"
if not makefile.exists():
    errors.append("missing file: Makefile")
elif "python3 tools/verify_wc2026_knockout_pub_background_image_prompt.py" not in makefile.read_text():
    errors.append("Makefile missing knockout pub background image prompt verifier")

if errors:
    raise SystemExit("WC2026 knockout pub background image prompt verification failed:\n- " + "\n- ".join(errors))

print("OK: WC2026 knockout pub background image prompt is captured and verified.")
