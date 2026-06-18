#!/usr/bin/env python3
"""Publish the Workbench-owned site/ surface as a GitHub Pages snapshot.

Source truth stays on the normal repo branch under site/.
The gh-pages branch is generated deployment output and should not be edited by hand.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = REPO_ROOT / "site"
WORKTREE = Path(os.environ.get("WC2026_PAGES_WORKTREE", "/tmp/wc2026-pages-publish"))
REMOTE = os.environ.get("WC2026_PAGES_REMOTE", "origin")
PAGES_BRANCH = os.environ.get("WC2026_PAGES_BRANCH", "gh-pages")

REQUIRED_SITE_PATHS = [
    "index.html",
    "css/board.css",
    "js/app.js",
    "data/current/group_matches.json",
]


def run(args: list[str], cwd: Path = REPO_ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("$", " ".join(args))
    return subprocess.run(args, cwd=cwd, text=True, check=check)


def capture(args: list[str], cwd: Path = REPO_ROOT) -> str:
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def require_clean_source(allow_dirty: bool) -> None:
    status = capture(["git", "status", "--short"])
    if status and not allow_dirty:
        print("Refusing to publish with uncommitted source changes:")
        print(status)
        print("Commit/stash first, or rerun with --allow-dirty for an intentional local snapshot.")
        sys.exit(2)


def require_site_surface() -> None:
    missing = [p for p in REQUIRED_SITE_PATHS if not (SITE_DIR / p).exists()]
    if missing:
        print("Cannot publish; site/ surface is missing required files:")
        for item in missing:
            print(f"- site/{item}")
        sys.exit(2)


def ensure_worktree() -> None:
    if WORKTREE.exists():
        run(["git", "worktree", "remove", "--force", str(WORKTREE)], check=False)
        shutil.rmtree(WORKTREE, ignore_errors=True)
    run(["git", "worktree", "prune"], check=False)

    has_remote_branch = subprocess.run(
        ["git", "ls-remote", "--exit-code", "--heads", REMOTE, PAGES_BRANCH],
        cwd=REPO_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    ).returncode == 0

    if has_remote_branch:
        run(["git", "fetch", REMOTE, PAGES_BRANCH])
        run(["git", "worktree", "add", str(WORKTREE), PAGES_BRANCH])
    else:
        run(["git", "worktree", "add", "--detach", str(WORKTREE)])
        run(["git", "checkout", "--orphan", PAGES_BRANCH], cwd=WORKTREE)
        run(["git", "rm", "-rf", "."], cwd=WORKTREE, check=False)


def clear_snapshot() -> None:
    for child in WORKTREE.iterdir():
        if child.name == ".git":
            continue
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()


def copy_site_to_pages_root() -> None:
    for child in SITE_DIR.iterdir():
        if child.name == ".DS_Store":
            continue
        dest = WORKTREE / child.name
        if child.is_dir():
            shutil.copytree(child, dest, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__"))
        else:
            shutil.copy2(child, dest)

    (WORKTREE / ".nojekyll").write_text("", encoding="utf-8")
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    source_commit = capture(["git", "rev-parse", "--short", "HEAD"])
    (WORKTREE / "pages-build.txt").write_text(
        f"published-from-site {stamp} source={source_commit}\n",
        encoding="utf-8",
    )


def publish(push: bool) -> None:
    run(["git", "add", "-A"], cwd=WORKTREE)
    status = capture(["git", "status", "--short"], cwd=WORKTREE)
    if status:
        print(status)
        run(["git", "commit", "-m", "Publish WC2026 Pages snapshot"], cwd=WORKTREE)
        if push:
            run(["git", "push", REMOTE, PAGES_BRANCH], cwd=WORKTREE)
    else:
        print("No gh-pages snapshot changes.")
        if push:
            run(["git", "push", REMOTE, PAGES_BRANCH], cwd=WORKTREE, check=False)


def ensure_pages_source() -> None:
    # The repo currently accepts the simple legacy source value: gh-pages.
    # Do not fail publishing if gh is unavailable or the API is temporarily inconsistent.
    try:
        run(["gh", "api", "--method", "PUT", "repos/:owner/:repo/pages", "-f", "source=gh-pages"], check=False)
        run(["gh", "api", "repos/:owner/:repo/pages", "--jq", "{html_url, status, source}"], check=False)
    except FileNotFoundError:
        print("gh CLI not found; skipping Pages source confirmation.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish site/ to gh-pages root as a Pages snapshot.")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow publishing with uncommitted source changes.")
    parser.add_argument("--no-verify", action="store_true", help="Skip make verify before publishing.")
    parser.add_argument("--no-push", action="store_true", help="Commit locally in gh-pages worktree but do not push.")
    args = parser.parse_args()

    os.chdir(REPO_ROOT)
    require_site_surface()
    require_clean_source(args.allow_dirty)

    if not args.no_verify:
        run(["make", "verify"])

    ensure_worktree()
    clear_snapshot()
    copy_site_to_pages_root()
    publish(push=not args.no_push)

    if not args.no_push:
        ensure_pages_source()

    print("Pages snapshot publish complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
