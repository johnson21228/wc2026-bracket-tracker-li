from pathlib import Path
import json
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "site/game1/index.html"
TEAMS = ROOT / "site/data/teams_from_flags_images.json"
RULE = ROOT / "li/world_cup/r32_pick_card_abbreviation_display_rule.md"


def require(cond, msg):
    if not cond:
        raise SystemExit(msg)


def load_teams():
    data = json.loads(TEAMS.read_text())
    if isinstance(data, dict) and "teams" in data:
        return data["teams"]
    return data


def main():
    require(RULE.exists(), "Missing R32 pick-card abbreviation display rule")
    html = HTML.read_text()
    require("function r32PickCardCode" in html or "function compactTeamCode" in html, "Missing compact pick-card code helper")
    require("r32PickCardCode(pick)" in html or "compactTeamCode(pick)" in html, "Filled pick rendering does not use compact code helper")
    require("pick.abbr" not in re.sub(r"function r32PickCardCode[\s\S]*?}\n", "", html), "Rendering should go through helper, not ad-hoc pick.abbr outside helper")

    # The compact pick HTML should not intentionally render full-name helpers/classes.
    compact_blocks = re.findall(r"innerHTML\s*=\s*`([^`]*pick[^`]*)`", html)
    joined = "\n".join(compact_blocks)
    require("pickName" not in joined, "Compact R32 card still contains pickName")
    require("displayName(pick)" not in joined, "Compact R32 card still renders displayName(pick)")
    require("fullName" not in joined, "Compact R32 card should not render fullName on card face")

    teams = load_teams()
    require(len(teams) == 48, f"Expected 48 teams, found {len(teams)}")
    bad = [t for t in teams if len(str(t.get("abbr", "")).strip()) != 3]
    require(not bad, "All 48 teams must have a three-letter abbr")

    m = re.search(r"<script[^>]*>([\s\S]*)</script>", html)
    require(m is not None, "Missing inline script")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(m.group(1))
        js_path = f.name
    result = subprocess.run(["node", "--check", js_path], text=True, capture_output=True)
    require(result.returncode == 0, "Game 1 inline script failed JS parse check:\n" + result.stderr)
    print("WC2026 R32 pick-card abbreviation repair checks passed.")


if __name__ == "__main__":
    main()
