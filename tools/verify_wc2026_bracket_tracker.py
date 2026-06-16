#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import sys

ROOT = Path.cwd()

REQUIRED = [
    "README.md",
    "LLM_READ_FIRST.md",
    "MAP.md",
    "site/index.html",
    "site/game1/index.html",
    "site/game2/index.html",
    "site/assets/playfield/game1_pub_options_background.jpeg",
    "site/assets/playfield/r32_bracket_geometry_overlay.png",
    "li/repo/site_entrypoint_hygiene_rule.md",
    "li/repo/github_pages_site_surface_rule.md",
    "li/world_cup/game2_official_seed_and_game1_tiebreaker_rule.md",
    "docs/rules/game2_official_seed_and_game1_tiebreaker.md",
]

FORBIDDEN_ROOT_FILES = ["index.html", "game1_playfield.html"]
ROOT_OVERLAY_PREFIXES = ("wc2026_", "wc_")
ROOT_OVERLAY_SUFFIXES = ("_overlay",)
EXPLICIT_ROOT_RESIDUE = {
    "wc2026_bracket_tracker_cb_001",
    "wc2026_schedule_poster_input_artifact",
    "wc_repo",
    "wc_cleanup_overlay",
    "wc_site_deploy_overlay",
    "wc_game2_start_overlay",
    "wc_game2_seed_overlay",
    "wc_verifier_fix_overlay",
    "wc_verifier_rebuild_overlay",
}


def fail(title: str, items: list[str]) -> None:
    print(title)
    for item in items:
        print(f"- {item}")
    sys.exit(1)


def is_overlay_residue(path: Path) -> bool:
    name = path.name
    if name in EXPLICIT_ROOT_RESIDUE:
        return True
    return name.startswith(ROOT_OVERLAY_PREFIXES) and name.endswith(ROOT_OVERLAY_SUFFIXES)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8", errors="replace")


def assert_html(path: str) -> None:
    text = read(path).lower()
    if "<html" not in text or "</html>" not in text:
        fail("HTML entry point is malformed:", [path])


def require_tokens(label: str, path: str, tokens: list[str]) -> None:
    text = read(path)
    missing = [token for token in tokens if token not in text]
    if missing:
        fail(f"{label} tokens missing:", [f"{path}: {token}" for token in missing])


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail("Missing required files:", missing)

    forbidden = [p for p in FORBIDDEN_ROOT_FILES if (ROOT / p).exists()]
    if forbidden:
        fail("Root HTML entrypoints are stale; deployable site must live under site/:", forbidden)

    ds_store_files = sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob(".DS_Store"))
    if ds_store_files:
        fail("macOS metadata files must be removed before verify/pack:", ds_store_files)

    root_residue = sorted(
        child.name + "/"
        for child in ROOT.iterdir()
        if child.is_dir() and is_overlay_residue(child)
    )
    if root_residue:
        fail("Applied overlay working directories must not remain at repo root:", root_residue)

    readme = read("README.md")
    if "WC2026 Bracket Tracker" not in readme:
        fail("README identity is stale or incorrect:", ["README.md"])
    if "site/" not in readme:
        fail("README must describe the deployable site/ folder:", ["README.md"])

    for page in ["site/index.html", "site/game1/index.html", "site/game2/index.html"]:
        assert_html(page)

    require_tokens(
        "Site landing page",
        "site/index.html",
        ["game1/", "game2/"],
    )

    require_tokens(
        "Game 1 layered board",
        "site/game1/index.html",
        [
            "game1_pub_options_background.jpeg",
            "r32_bracket_geometry_overlay.png",
            "hitLayer",
            ".hotspot",
            "slotFillOpacity",
            "eligibleTeamsForSlot",
        ],
    )

    storage_count = read("site/game1/index.html").count("const STORAGE_KEY")
    if storage_count != 1:
        fail("Game 1 must contain exactly one const STORAGE_KEY declaration:", [f"found {storage_count}"])

    game2 = read("site/game2/index.html")
    if "game1_pub_options_background.jpeg" not in game2 or "r32_bracket_geometry_overlay.png" not in game2:
        fail("Game 2 must share the layered board foundation:", ["site/game2/index.html"])

    for folder in [ROOT / "data", ROOT / "site" / "data"]:
        if not folder.exists():
            continue
        bad_json: list[str] = []
        for p in sorted(folder.glob("*.json")):
            try:
                json.loads(p.read_text(encoding="utf-8"))
            except Exception as exc:  # noqa: BLE001
                bad_json.append(f"{p.relative_to(ROOT)}: {exc}")
        if bad_json:
            fail("Invalid JSON data files:", bad_json)

    require_tokens(
        "Game 2 official seed tiebreaker LI",
        "li/world_cup/game2_official_seed_and_game1_tiebreaker_rule.md",
        ["official", "Game 1", "tiebreaker"],
    )

    print("WC2026 Bracket Tracker verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Game 1 reset visible hit layer tokens are verified by static page checks in current workflow.

# Game 1 reset visible hit layer tokens are verified by static page checks in current workflow.
