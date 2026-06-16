from pathlib import Path
import json
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "site/game1/index.html"
TEAMS = ROOT / "site/data/teams_from_flags_images.json"
RULE = ROOT / "li/world_cup/r32_pick_card_abbreviation_display_rule.md"


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)


def main() -> None:
    html = HTML.read_text()
    require(RULE.exists(), "Missing R32 pick-card abbreviation display LI rule")
    require("function compactTeamCode" in html, "Missing compactTeamCode helper")
    require("class=\"pickCode\"" in html, "Pick card does not render pickCode")
    require("tooltipHtmlForPick" in html and "Click/tap to change pick" in html, "Missing full-name tooltip/details rendering")
    require("displayName(pick)</strong>" in html, "Tooltip must render full team name")
    render_block = re.search(r"function renderPicks\(\)[\s\S]*?function openMenu", html)
    require(render_block is not None, "Could not locate renderPicks block")
    block = render_block.group(0)
    require("pickName" not in block, "Compact R32 pick card must not render full-name pickName")
    require("pickRule" not in block, "Compact R32 pick card must not render slot rule text")
    require("title=" not in block and ".title" not in block, "Do not use native title tooltip in pick-card rendering")

    teams = json.loads(TEAMS.read_text())
    require(len(teams) == 48, f"Expected 48 teams, found {len(teams)}")
    bad = [t for t in teams if len(str(t.get("abbr", "")).strip()) != 3]
    require(not bad, "All 48 teams must have a three-letter abbr")

    # Parse script with Node to catch syntax regressions in inline JS.
    m = re.search(r"<script>([\s\S]*)</script>", html)
    require(m is not None, "Missing inline script")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(m.group(1))
        js_path = f.name
    result = subprocess.run(["node", "--check", js_path], text=True, capture_output=True)
    require(result.returncode == 0, "Game 1 inline script failed JS parse check:\n" + result.stderr)
    print("WC2026 R32 pick-card abbreviation display checks passed.")

if __name__ == "__main__":
    main()
