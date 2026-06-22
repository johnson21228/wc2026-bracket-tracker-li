#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import sys
import subprocess
def is_allowed_pages_root_redirect(path):
    """Allow only a tiny GitHub Pages root shim that redirects to site/."""
    if path.name != "index.html" or not path.exists():
        return False
    html = path.read_text(errors="ignore")
    has_meta_redirect = 'http-equiv="refresh"' in html and 'url=site/' in html
    has_js_redirect = 'window.location.replace("site/"' in html or "window.location.replace('site/'" in html
    has_site_link = 'href="site/"' in html or "href='site/'" in html
    forbidden_runtime_refs = [
        'src="js/',
        "src='js/",
        'href="css/',
        "href='css/",
        'data/current/',
        'site/js/',
        'site/css/',
    ]
    return (
        has_meta_redirect
        and has_js_redirect
        and has_site_link
        and not any(marker in html for marker in forbidden_runtime_refs)
    )

ROOT = Path.cwd()

REQUIRED = [
    "README.md",
    "LLM_READ_FIRST.md",
    "MAP.md",
    "site/index.html",
    "site/css/app.css",
    "site/css/board.css",
    "site/css/dev.css",
    "site/js/app.js",
    "site/js/services/assetPaths.js",
    "site/js/services/domMounts.js",
    "site/js/services/DebugConsole.js",
    "site/js/board/BoardShell.js",
    "site/js/board/BackgroundLayer.js",
    "site/js/dev/DeveloperFrame.js",
    "site/assets/board/pub_background_game1.jpeg",
    "site/assets/board/gameboard.svg",
    "site/data/geometry/gameboard_manifest.json",
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

    forbidden = []
    for name in FORBIDDEN_ROOT_FILES:
        candidate = ROOT / name
        if not candidate.exists():
            continue
        if name == "index.html" and is_allowed_pages_root_redirect(candidate):
            continue
        forbidden.append(name)
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

    for page in ["site/index.html"]:
        assert_html(page)

    root_html = read("site/index.html")
    shell_required = [
        '<main id="wc2026-app"',
        '<script type="module" src="js/app.js',
        'href="assets/board/pub_background_game1.jpeg"',
        'href="assets/playfield/uniform_pick_card_gameboard.svg"',
        'href="css/app.css',
        'href="css/board.css',
        'href="css/dev.css',
    ]
    missing_shell = [token for token in shell_required if token not in root_html]
    if missing_shell:
        fail("Clean modular site shell tokens missing:", [f"site/index.html: {token}" for token in missing_shell])

    forbidden_shell = [
        "hitLayer",
        ".hotspot",
        "slotFillOpacity",
        "eligibleTeamsForSlot",
        "const STORAGE_KEY",
        "localStorage",
        "readJson(",
        "RENDER_STORED",
        "winnerPicks",
        "knockoutPicks",
        "choiceLockState",
    ]
    present_forbidden = [token for token in forbidden_shell if token in root_html]
    if present_forbidden:
        fail("Clean modular site shell contains legacy/runtime tokens:", [f"site/index.html: {token}" for token in present_forbidden])

    asset_paths = read("site/js/services/assetPaths.js")
    asset_required = [
        'backgroundImage: "assets/board/pub_background_game1.jpeg"',
        'svgGameboardDefinition: "assets/playfield/uniform_pick_card_gameboard.svg"',
        'geometryManifest: "data/geometry/gameboard_manifest.json"',
    ]
    missing_assets = [token for token in asset_required if token not in asset_paths]
    if missing_assets:
        fail("Clean modular asset path tokens missing:", [f"site/js/services/assetPaths.js: {token}" for token in missing_assets])

    board_shell = read("site/js/board/BoardShell.js")
    board_required = [
        "pixel-native-board-plane",
        "createBackgroundLayer",
        "truthResources.backgroundImage",
    ]
    missing_board = [token for token in board_required if token not in board_shell]
    if missing_board:
        fail("Clean modular board shell tokens missing:", [f"site/js/board/BoardShell.js: {token}" for token in missing_board])

    background_layer = read("site/js/board/BackgroundLayer.js")
    background_required = [
        'document.createElement("img")',
        "layer.src = backgroundImage",
        "bottom-background-authority",
    ]
    missing_background = [token for token in background_required if token not in background_layer]
    if missing_background:
        fail("Clean modular background layer tokens missing:", [f"site/js/board/BackgroundLayer.js: {token}" for token in missing_background])

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

    subprocess.run(
        [sys.executable, "tools/verify_wc2026_modular_source_boundary.py"],
        cwd=ROOT,
        check=True,
    )

    print("WC2026 Bracket Tracker verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Clean modular site root tokens are verified by module boundary checks in current workflow.
