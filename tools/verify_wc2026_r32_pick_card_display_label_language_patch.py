from pathlib import Path
import json
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def fail(msg: str) -> None:
    raise SystemExit(msg)


def load_teams():
    path = ROOT / "site/data/teams_from_flags_images.json"
    data = json.loads(path.read_text())
    return data.get("teams", data)


def main() -> None:
    html_path = ROOT / "site/game1/index.html"
    if not html_path.exists():
        fail("Missing site/game1/index.html")
    html = html_path.read_text()

    for rel in [
        "li/world_cup/r32_pick_card_display_label_rule.md",
        "docs/features/r32_pick_card_display_label_repair.md",
        "cards/087_repair_r32_pick_card_display_label_language_card.md",
    ]:
        if not (ROOT / rel).exists():
            fail(f"Missing {rel}")

    teams = load_teams()
    if len(teams) != 48:
        fail(f"Expected 48 teams, found {len(teams)}")
    bad = [t.get("name", "?") for t in teams if len(str(t.get("abbr", "")).strip()) != 3]
    if bad:
        fail("Teams without a three-letter abbr: " + ", ".join(bad))

    if "function r32PickCardLabel" not in html:
        fail("Missing canonical r32PickCardLabel(team) helper")
    if "Card label" not in html and "3-letter label" not in html:
        fail("Tooltip/details copy must use Card label or 3-letter label")
    if re.search(r"\bCode:\s*\$\{", html):
        fail("Tooltip/details still contains ambiguous Code: dynamic label")
    if "r32PickCardLabel(pick)" not in html and "r32PickCardLabel(team)" not in html:
        fail("R32 pick card rendering does not use r32PickCardLabel")

    scripts = "\n".join(re.findall(r"<script[^>]*>([\s\S]*?)</script>", html))
    if scripts.strip():
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write(scripts)
            tmp = f.name
        try:
            res = subprocess.run(["node", "--check", tmp], text=True, capture_output=True)
            if res.returncode != 0:
                fail("site/game1/index.html script parse failed:\n" + res.stderr)
        except FileNotFoundError:
            pass

    print("WC2026 R32 pick-card display label language checks passed.")


if __name__ == "__main__":
    main()
