#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROOT_OVERLAY_DIR_PREFIXES = ("wc2026_",)
ROOT_OVERLAY_DIR_SUFFIXES = ("_overlay",)
EXPLICIT_ROOT_RESIDUE = {
    "wc2026_bracket_tracker_cb_001",
    "wc2026_schedule_poster_input_artifact",
    "wc_repo",
}


def is_overlay_residue(path: Path) -> bool:
    name = path.name
    if name in EXPLICIT_ROOT_RESIDUE:
        return True
    return name.startswith(ROOT_OVERLAY_DIR_PREFIXES) and name.endswith(ROOT_OVERLAY_DIR_SUFFIXES)


def main() -> int:
    removed: list[str] = []

    for ds_store in ROOT.rglob(".DS_Store"):
        ds_store.unlink()
        removed.append(str(ds_store.relative_to(ROOT)))

    for child in ROOT.iterdir():
        if child.is_dir() and is_overlay_residue(child):
            shutil.rmtree(child)
            removed.append(str(child.relative_to(ROOT)) + "/")

    if removed:
        print("Removed hygiene residue:")
        for item in sorted(removed):
            print(f"- {item}")
    else:
        print("Repo hygiene already clean.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
