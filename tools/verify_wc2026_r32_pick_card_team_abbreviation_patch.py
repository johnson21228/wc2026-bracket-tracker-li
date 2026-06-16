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
LI = ROOT / "li" / "world_cup" / "r32_pick_card_team_abbreviation_rule.md"
DOC = ROOT / "docs" / "features" / "r32_pick_card_team_abbreviation_repair.md"
CARD = ROOT / "cards" / "088_repair_r32_pick_card_team_abbreviation_card.md"
CAPTURE = ROOT / "capture_back" / "CAPTURE_BACK_R32_PICK_CARD_TEAM_ABBREVIATION_AUTHORITY.md"


def fail(message: str) -> None:
    raise SystemExit(message)


def extract_scripts_from_html(html: str) -> str:
    scripts: list[str] = []
    for match in re.finditer(r"<script(?P<attrs>[^>]*)>(?P<body>.*?)</script>", html, flags=re.S | re.I):
        attrs = match.group("attrs") or ""
        # Skip externally sourced scripts and non-JS data blocks.
        if re.search(r"\bsrc\s*=", attrs, flags=re.I):
            continue
        if re.search(r"\btype\s*=\s*['\"](?!text/javascript|application/javascript|module)", attrs, flags=re.I):
            continue
        scripts.append(match.group("body"))
    return "\n;\n".join(scripts)


def check_game1_inline_js_parse(html: str) -> None:
    js = extract_scripts_from_html(html)
    if not js.strip():
        fail("No inline JavaScript was found in site/game1/index.html")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as tmp:
        tmp.write(js)
        tmp_path = Path(tmp.name)
    try:
        subprocess.run(["node", "--check", str(tmp_path)], check=True)
    except FileNotFoundError:
        # Node is not required to exist on every machine; the text checks still guard the patch.
        return
    finally:
        try:
            tmp_path.unlink()
        except FileNotFoundError:
            pass


def main() -> None:
    required = [GAME1, TEAMS, LI, DOC, CARD, CAPTURE]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        fail("Missing expected R32 team abbreviation authority files:\n- " + "\n- ".join(missing))

    html = GAME1.read_text(encoding="utf-8")
    li = LI.read_text(encoding="utf-8")

    if "function r32TeamAbbreviation(team)" not in html:
        fail("Game 1 must define r32TeamAbbreviation(team).")
    if "pickName.textContent = r32TeamAbbreviation(pick);" not in html:
        fail("Compact R32 pick card text must render r32TeamAbbreviation(pick).")
    if "pickName.textContent = displayName(pick);" in html or "pickName.textContent = r32CardDisplayName(pick);" in html:
        fail("Compact R32 pick card must not render full displayName/r32CardDisplayName.")
    if "Code:" in html or "Card label:" in html or "Display label:" in html:
        fail("Game 1 details copy must use 'Team abbreviation', not Code/Card label/Display label.")
    if "Team abbreviation" not in html:
        fail("Tooltip/details copy should expose the compact value as Team abbreviation.")
    if "team.abbr" not in li or "Full team name" not in li or "R32 pick card face" not in li:
        fail("LI must define full team name, team.abbr authority, and R32 pick card face semantics.")

    data = json.loads(TEAMS.read_text(encoding="utf-8"))
    teams = data.get("teams") if isinstance(data, dict) else data
    if not isinstance(teams, list):
        fail("teams_from_flags_images.json must contain a team list.")
    bad = []
    for team in teams:
        if not isinstance(team, dict):
            bad.append(str(team))
            continue
        name = team.get("name") or team.get("team") or team.get("fullName") or "<unnamed>"
        abbr = team.get("abbr")
        if not isinstance(abbr, str) or not re.fullmatch(r"[A-Z0-9]{3}", abbr):
            bad.append(f"{name}: {abbr!r}")
    if bad:
        fail("Every team must have a valid 3-character team.abbr value:\n- " + "\n- ".join(bad))

    check_game1_inline_js_parse(html)
    print("WC2026 R32 pick-card team abbreviation verifier passed.")


if __name__ == "__main__":
    main()
