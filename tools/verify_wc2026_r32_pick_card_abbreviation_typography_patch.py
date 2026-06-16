#!/usr/bin/env python3
from __future__ import annotations
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME1 = ROOT / "site" / "game1" / "index.html"
TEAMS = ROOT / "site" / "data" / "teams_from_flags_images.json"
REQUIRED = [
    ROOT / "li/world_cup/r32_pick_card_abbreviation_typography_rule.md",
    ROOT / "docs/features/r32_pick_card_abbreviation_typography_fit.md",
    ROOT / "cards/090_tune_r32_pick_card_abbreviation_typography_card.md",
    ROOT / "capture_back/CAPTURE_BACK_R32_PICK_CARD_ABBREVIATION_TYPOGRAPHY.md",
]

def fail(msg: str) -> None:
    raise SystemExit(msg)

def extract_scripts(html: str) -> str:
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, flags=re.S | re.I)
    return "\n;\n".join(scripts)

def main() -> None:
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]
    if missing:
        fail("Missing expected R32 abbreviation typography files:\n- " + "\n- ".join(missing))

    html = GAME1.read_text()
    for needle in [
        "R32 pick-card abbreviation typography fit",
        "font-size: 24px !important",
        "font-weight: 950 !important",
        "font-family: \"Avenir Next Condensed\"",
        "font-size: 30px !important",
        "r32TeamAbbreviation(pick)",
        "R32 abbreviation cards use fixed shared typography",
    ]:
        if needle not in html:
            fail(f"Missing expected Game 1 typography marker: {needle}")
    forbidden = [
        "node --check site/game1/index.html",
        "pickName.textContent = r32PickFullName",
        "pickName.textContent = displayName",
    ]
    for needle in forbidden:
        if needle in html:
            fail(f"Forbidden legacy rendering marker remains: {needle}")

    data = json.loads(TEAMS.read_text())
    teams = data.get("teams", data if isinstance(data, list) else [])
    bad = [t for t in teams if len(str(t.get("abbr", "")).strip()) != 3]
    if len(teams) < 48 or bad:
        fail("Expected all 48 teams to have 3-letter abbr values.")

    scripts = extract_scripts(html)
    if scripts.strip():
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write(scripts)
            temp = f.name
        subprocess.run(["node", "--check", temp], check=True)

    print("WC2026 R32 pick-card abbreviation typography checks passed.")

if __name__ == "__main__":
    main()
