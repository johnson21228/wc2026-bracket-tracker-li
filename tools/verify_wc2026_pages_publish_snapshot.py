#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path.cwd()
REQUIRED = [
    "tools/publish_pages_snapshot.py",
    "tools/verify_wc2026_pages_publish_snapshot.py",
    "li/repo/pages_publish_snapshot_rule.md",
    "li/workflow/pages_publish_projection_protocol.md",
    "docs/dev/pages_publish_snapshot_workflow.md",
    "cards/196_add_pages_publish_snapshot_workflow_card.md",
    "capture_back/CAPTURE_BACK_PAGES_PUBLISH_SNAPSHOT_WORKFLOW.md",
]


def fail(title: str, items: list[str]) -> None:
    print(title)
    for item in items:
        print(f"- {item}")
    sys.exit(1)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8", errors="replace")


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        fail("Missing Pages publish snapshot workflow files:", missing)

    makefile = read("Makefile")
    if "publish-pages:" not in makefile or "python3 tools/publish_pages_snapshot.py" not in makefile:
        fail("Makefile must expose publish-pages target backed by the publish script:", ["Makefile"])
    if "python3 tools/verify_wc2026_pages_publish_snapshot.py" not in makefile:
        fail("Makefile verify target must include the Pages publish snapshot verifier:", ["Makefile"])

    script = read("tools/publish_pages_snapshot.py")
    required_script_tokens = [
        "SITE_DIR = REPO_ROOT / \"site\"",
        "PAGES_BRANCH",
        "gh-pages",
        "pages-build.txt",
        ".nojekyll",
        "copy_site_to_pages_root",
        "git", "worktree", "push",
        "source=gh-pages",
    ]
    missing_script = [token for token in required_script_tokens if token not in script]
    if missing_script:
        fail("Pages publish script is missing required governance/runtime tokens:", [f"tools/publish_pages_snapshot.py: {t}" for t in missing_script])

    if "./site/" in script or "WORKTREE / \"site\"" in script:
        fail("Pages publish script must copy site/ contents to gh-pages root, not nest them under site/:", ["tools/publish_pages_snapshot.py"])

    li = read("li/repo/pages_publish_snapshot_rule.md") + "\n" + read("li/workflow/pages_publish_projection_protocol.md")
    required_li = [
        "site/ is the source truth",
        "gh-pages is generated deployment output",
        "Do not hand-edit gh-pages",
        "published snapshot",
    ]
    missing_li = [token for token in required_li if token not in li]
    if missing_li:
        fail("Pages publish LI must state source/snapshot governance:", [f"LI: {t}" for t in missing_li])

    doc = read("docs/dev/pages_publish_snapshot_workflow.md")
    required_doc = ["make publish-pages", "site/", "gh-pages", "index.html", "css/", "js/", "data/", "assets/"]
    missing_doc = [token for token in required_doc if token not in doc]
    if missing_doc:
        fail("Pages publish workflow doc is missing expected operator guidance:", [f"docs/dev/pages_publish_snapshot_workflow.md: {t}" for t in missing_doc])

    print("OK: WC2026 Pages publish snapshot workflow is captured and verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
