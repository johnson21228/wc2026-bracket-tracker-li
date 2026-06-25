#!/usr/bin/env python3
"""Verify official R32 hydration LI is captured without runtime changes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "li/world_cup/knockout_only_game_model.md": [
        "Bracketeering is now a knockout-only game",
        "`Admin_/official` owns the R32 field",
        "non-admin players cannot author R32 occupants",
        "Player-owned picks begin with R32 match winners",
        "The old group-stage prediction model is no longer player-owned game behavior",
        "This CB is LI-only and does not change runtime behavior",
    ],
    "li/world_cup/official_r32_hydration_rule.md": [
        "`Admin_/official` owns the R32 field",
        "Non-admin players cannot author R32 occupants",
        "Hydration must copy `Admin_/official` R32 occupants into non-admin player BracketDocuments at creation, load, import, and save boundaries",
        "BracketDocument remains the persistence container",
        "The planned Supabase row-per-user-per-game model remains valid",
        "Scoring compares player knockout winner picks to official result truth",
        "This CB is LI-only and does not change runtime behavior",
    ],
    "docs/features/official_r32_hydration.md": [
        "Bracketeering is a knockout-only game",
        "`Admin_/official` owns the R32 field",
        "Non-admin players cannot author R32 occupants",
        "Player-owned picks begin with R32 match winners",
        "Hydration must copy `Admin_/official` R32 occupants into non-admin player BracketDocuments at creation, load, import, and save boundaries",
        "BracketDocument remains the persistence container",
        "The planned Supabase row-per-user-per-game model remains valid",
        "Scoring compares player knockout winner picks to official result truth",
        "This CB is LI-only and does not change runtime behavior",
    ],
    "cards/1011_official_r32_hydration_rule_card.md": [
        "Admin_/official` owns the R32 field",
        "Non-admin players cannot author R32 occupants",
        "Player-owned picks begin with R32 match winners",
        "Hydration applies at creation, load, import, and save boundaries",
        "BracketDocument remains the persistence container",
        "Supabase row-per-user-per-game remains valid",
        "Scoring compares knockout winner picks to official result truth",
        "This CB is LI-only and does not change runtime behavior",
    ],
    "captures/CAPTURE_BACK_OFFICIAL_R32_HYDRATION_RULE.md": [
        "Admin_/official` owns the R32 field",
        "Non-admin players cannot author R32 occupants",
        "Player-owned picks begin with R32 match winners",
        "Hydration must copy official R32 occupants at creation, load, import, and save boundaries",
        "BracketDocument remains the persistence container",
        "Supabase row-per-user-per-game remains valid",
        "Scoring compares knockout winner picks to official result truth",
        "This CB is LI-only and does not change runtime behavior",
    ],
}

missing = []
for rel, needles in REQUIRED.items():
    path = ROOT / rel
    if not path.exists():
        missing.append(f"missing file: {rel}")
        continue
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            missing.append(f"{rel}: missing phrase {needle!r}")

makefile = ROOT / "Makefile"
if not makefile.exists():
    missing.append("missing Makefile")
elif "python3 tools/verify_wc2026_official_r32_hydration_li.py" not in makefile.read_text(encoding="utf-8"):
    missing.append("Makefile verify target does not include official R32 hydration LI verifier")

# This governance CB must not touch runtime source files.
runtime_paths = [
    "site/index.html",
    "site/js",
    "site/css",
    "site/data",
]
for rel in runtime_paths:
    path = ROOT / rel
    if not path.exists():
        continue
    # The verifier asserts text-governance coverage only. Git diff runtime detection is left
    # to the CB operator because the distributed pack may not include .git metadata.

if missing:
    print("WC2026 official R32 hydration LI verification failed:")
    for item in missing:
        print(f"- {item}")
    raise SystemExit(1)

print("OK: WC2026 official R32 hydration LI defines knockout-only R32 authority, hydration boundaries, persistence, scoring, and LI-only scope.")
