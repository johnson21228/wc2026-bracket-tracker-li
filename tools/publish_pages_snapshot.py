#!/usr/bin/env python3
"""Fail-closed publisher for the Workbench-owned GitHub Pages surface.

Source truth stays on the normal repo branch under site/.
The gh-pages branch is generated deployment output and should not be edited by hand.

This publisher is intentionally strict when called from `make publish-pages`:
- main/source must be clean;
- source HEAD must be pushed to origin/main;
- gh-pages is rebuilt from site/;
- critical deployed JSON is polled and compared against source before success.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = REPO_ROOT / "site"
WORKTREE = Path(os.environ.get("WC2026_PAGES_WORKTREE", "/tmp/wc2026-pages-publish"))
REMOTE = os.environ.get("WC2026_PAGES_REMOTE", "origin")
PAGES_BRANCH = os.environ.get("WC2026_PAGES_BRANCH", "gh-pages")
SOURCE_BRANCH = os.environ.get("WC2026_PAGES_SOURCE_BRANCH", "main")
PAGES_URL = os.environ.get(
    "WC2026_PAGES_URL",
    "https://johnson21228.github.io/wc2026-bracket-tracker-li/",
).rstrip("/") + "/"
VERIFY_ATTEMPTS = int(os.environ.get("WC2026_PAGES_VERIFY_ATTEMPTS", "30"))
VERIFY_SLEEP_SECONDS = float(os.environ.get("WC2026_PAGES_VERIFY_SLEEP_SECONDS", "5"))

CRITICAL_JSON_PATHS = [
    "data/current/group_matches.json",
    "data/current/group_standings.json",
    "data/current/match_highlights.json",
]

REQUIRED_SITE_PATHS = [
    "index.html",
    "css/board.css",
    "css/app.css",
    "js/app.js",
    "data/current/group_matches.json",
    "data/current/group_standings.json",
    "data/current/match_highlights.json",
]

CANARY_MATCHES = {
    "GS-2026-06-19-C3": ("Brazil 3-0 Haiti", "final", 3, 0),
    "66456934": ("Scotland 0-1 Morocco", "final", 0, 1),
    "66456946": ("Turkey 0-1 Paraguay", "final", 0, 1),
    "66456944": ("United States 2-0 Australia", "final", 2, 0),
}


def run(args: list[str], cwd: Path = REPO_ROOT, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("$", " ".join(args))
    return subprocess.run(args, cwd=cwd, text=True, check=check)


def capture(args: list[str], cwd: Path = REPO_ROOT, check: bool = True) -> str:
    print("$", " ".join(args))
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def require_clean_source(allow_dirty: bool) -> None:
    status = subprocess.check_output(["git", "status", "--short"], cwd=REPO_ROOT, text=True).strip()
    if status and not allow_dirty:
        print("Refusing to publish with uncommitted source changes:")
        print(status)
        print("Commit/stash first, or rerun with --allow-dirty for an intentional local snapshot.")
        raise SystemExit(2)


def require_source_head_pushed(strict: bool) -> None:
    if not strict:
        return
    branch = capture(["git", "branch", "--show-current"])
    if branch != SOURCE_BRANCH:
        print(f"Refusing strict publish from branch {branch!r}; expected {SOURCE_BRANCH!r}.")
        raise SystemExit(2)
    run(["git", "fetch", REMOTE, SOURCE_BRANCH])
    local = capture(["git", "rev-parse", "HEAD"])
    remote = capture(["git", "rev-parse", f"{REMOTE}/{SOURCE_BRANCH}"])
    if local != remote:
        print(f"Refusing strict publish: HEAD {local[:12]} is not pushed to {REMOTE}/{SOURCE_BRANCH} {remote[:12]}.")
        print(f"Run: git push {REMOTE} {SOURCE_BRANCH}")
        raise SystemExit(2)


def require_site_surface() -> None:
    missing = [p for p in REQUIRED_SITE_PATHS if not (SITE_DIR / p).exists()]
    if missing:
        print("Cannot publish; site/ surface is missing required files:")
        for item in missing:
            print(f"- site/{item}")
        raise SystemExit(2)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_hash(path: Path) -> str:
    value = json.loads(path.read_text(encoding="utf-8"))
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return sha256_bytes(payload)


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
        run(["git", "worktree", "add", "-B", PAGES_BRANCH, str(WORKTREE), f"{REMOTE}/{PAGES_BRANCH}"])
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
    source_commit = capture(["git", "rev-parse", "HEAD"])
    source_short = source_commit[:12]
    lines = [
        "published-from-site",
        f"publishedAt={stamp}",
        f"sourceCommit={source_commit}",
        "criticalJsonSha256:",
    ]
    for published_path in CRITICAL_JSON_PATHS:
        source_path = SITE_DIR / published_path
        lines.append(f"  {published_path}={canonical_json_hash(source_path)}")
    lines.append("")
    (WORKTREE / "pages-build.txt").write_text("\n".join(lines), encoding="utf-8")
    print(f"Prepared gh-pages snapshot from source {source_short}.")


def assert_projected_files_match() -> None:
    mismatches: list[str] = []
    for published_path in CRITICAL_JSON_PATHS:
        source_path = SITE_DIR / published_path
        pages_path = WORKTREE / published_path
        if canonical_json_hash(source_path) != canonical_json_hash(pages_path):
            mismatches.append(published_path)
    if mismatches:
        print("Refusing to publish: gh-pages worktree projection mismatched source site/ data:")
        for path in mismatches:
            print(f"- {path}")
        raise SystemExit(2)
    print("OK: gh-pages worktree critical JSON matches source site/ critical JSON.")


def publish(push: bool, force_redeploy: bool) -> None:
    run(["git", "add", "-A"], cwd=WORKTREE)
    status = subprocess.check_output(["git", "status", "--short"], cwd=WORKTREE, text=True).strip()
    if status:
        print(status)
        run(["git", "commit", "-m", "Publish WC2026 Pages snapshot"], cwd=WORKTREE)
    elif force_redeploy:
        print("No gh-pages snapshot changes; creating empty commit to force Pages redeploy.")
        run(["git", "commit", "--allow-empty", "-m", "Force WC2026 Pages redeploy"], cwd=WORKTREE)
    else:
        print("No gh-pages snapshot changes.")

    if push:
        run(["git", "push", REMOTE, PAGES_BRANCH], cwd=WORKTREE)


def ensure_pages_source() -> None:
    try:
        run(["gh", "api", "--method", "PUT", "repos/:owner/:repo/pages", "-f", "source=gh-pages"], check=False)
        run(["gh", "api", "repos/:owner/:repo/pages", "--jq", "{html_url, status, source}"], check=False)
    except FileNotFoundError:
        print("gh CLI not found; skipping Pages source confirmation.")


def load_live_json(url: str) -> Any:
    request = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def canonical_json_value_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return sha256_bytes(payload)


def extract_matches(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    if isinstance(data, dict):
        for key in ("matches", "groupMatches", "items", "data"):
            value = data.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]
        for value in data.values():
            if isinstance(value, list) and value and isinstance(value[0], dict):
                return value
    return []


def assert_canary_matches(group_matches_data: Any) -> None:
    matches = extract_matches(group_matches_data)
    by_id: dict[str, dict[str, Any]] = {}
    for match in matches:
        match_id = str(match.get("matchId", ""))
        espn_id = str(match.get("espnMatchId", ""))
        if match_id:
            by_id[match_id] = match
        if espn_id:
            by_id[espn_id] = match

    failures: list[str] = []
    for key, (summary, status, home_score, away_score) in CANARY_MATCHES.items():
        match = by_id.get(key)
        if not match:
            failures.append(f"{key}: missing")
            continue
        observed = (match.get("summary"), match.get("status"), match.get("homeScore"), match.get("awayScore"))
        expected = (summary, status, home_score, away_score)
        if observed != expected:
            failures.append(f"{key}: expected {expected}, observed {observed}")
    if failures:
        print("Live canary match verification failed:")
        for failure in failures:
            print(f"- {failure}")
        raise AssertionError("canary match verification failed")


def verify_live_data(source_commit: str) -> None:
    cache_buster = source_commit[:12]
    expected_hashes = {
        path: canonical_json_hash(SITE_DIR / path)
        for path in CRITICAL_JSON_PATHS
    }

    last_error: str | None = None
    for attempt in range(1, VERIFY_ATTEMPTS + 1):
        try:
            live_values: dict[str, Any] = {}
            live_hashes: dict[str, str] = {}
            for path in CRITICAL_JSON_PATHS:
                url = f"{PAGES_URL}{path}?v={cache_buster}-{attempt}"
                value = load_live_json(url)
                live_values[path] = value
                live_hashes[path] = canonical_json_value_hash(value)

            mismatches = [path for path in CRITICAL_JSON_PATHS if expected_hashes[path] != live_hashes[path]]
            if mismatches:
                last_error = "stale live JSON: " + ", ".join(mismatches)
            else:
                assert_canary_matches(live_values["data/current/group_matches.json"])
                print("OK: live Pages critical JSON matches source site/ critical JSON.")
                return
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, AssertionError) as exc:
            last_error = str(exc)

        if attempt < VERIFY_ATTEMPTS:
            print(
                f"Live Pages verification attempt {attempt}/{VERIFY_ATTEMPTS} failed: {last_error}. "
                f"Retrying in {VERIFY_SLEEP_SECONDS:g}s..."
            )
            time.sleep(VERIFY_SLEEP_SECONDS)

    print("Live Pages verification failed after publish.")
    if last_error:
        print(last_error)
    print("Pages publish is not complete until live data verifies.")
    raise SystemExit(3)


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish site/ to gh-pages root as a fail-closed Pages snapshot.")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow publishing with uncommitted source changes.")
    parser.add_argument("--no-verify", action="store_true", help="Skip make verify before publishing.")
    parser.add_argument("--no-push", action="store_true", help="Commit locally in gh-pages worktree but do not push.")
    parser.add_argument("--strict", action="store_true", help="Require clean source and pushed origin/main HEAD.")
    parser.add_argument("--verify-live", action="store_true", help="Poll live Pages data and compare it against source JSON before success.")
    parser.add_argument("--force-redeploy", action="store_true", help="Create an empty gh-pages commit when projection is unchanged.")
    args = parser.parse_args()

    os.chdir(REPO_ROOT)
    require_site_surface()
    require_clean_source(args.allow_dirty)
    require_source_head_pushed(args.strict)

    if not args.no_verify:
        run(["make", "verify"])

    ensure_worktree()
    try:
        clear_snapshot()
        copy_site_to_pages_root()
        assert_projected_files_match()
        source_commit = capture(["git", "rev-parse", "HEAD"])
        publish(push=not args.no_push, force_redeploy=args.force_redeploy)

        if not args.no_push:
            ensure_pages_source()

        if args.verify_live and not args.no_push:
            verify_live_data(source_commit)
    finally:
        if WORKTREE.exists():
            run(["git", "worktree", "remove", "--force", str(WORKTREE)], check=False)
        run(["git", "worktree", "prune"], check=False)

    print("Pages publish complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
