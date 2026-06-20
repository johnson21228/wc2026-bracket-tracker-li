#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> int:
    index = (ROOT / "site/index.html").read_text()
    view = (ROOT / "site/js/mvc/view.js").read_text()
    model = (ROOT / "site/js/mvc/model.js").read_text()
    controller = (ROOT / "site/js/mvc/controller.js").read_text()
    local_store = (ROOT / "site/js/services/LocalStorageBracketStore.js").read_text()

    forbidden_index_tokens = {
        'data-action="export-picks"': "Export picks button must not be player-facing",
        'data-action="import-picks"': "Import picks button must not be player-facing",
        "data-import-picks-file": "Import file control must not be player-facing",
        "Export picks": "Export picks text must not render in player UI",
        "Import picks": "Import picks text must not render in player UI",
        "Capture Picks": "Capture Picks text must not render in player UI",
        "Capture picks": "Capture picks text must not render in player UI",
    }
    for token, message in forbidden_index_tokens.items():
        if token in index:
            fail(message)

    forbidden_view_tokens = {
        'querySelector(\'[data-action="export-picks"]\')': "view must not bind player-facing export button",
        'querySelector(\'[data-action="import-picks"]\')': "view must not bind player-facing import button",
        'querySelector(\'[data-import-picks-file]\')': "view must not bind player-facing import file input",
        "new FileReader()": "view must not expose player-facing import file flow",
    }
    for token, message in forbidden_view_tokens.items():
        if token in view:
            fail(message)

    # Preserve internal model/controller helpers until Supabase persistence is stable.
    for token in ["exportPicksSnapshot", "importPicksSnapshot"]:
        if token not in model:
            fail(f"internal {token} helper should remain available in model")
    for token in ["LocalStorageBracketStore", "normalizeBracketDocument"]:
        if token not in local_store:
            fail(f"localStorage bracket persistence seam missing token {token}")
    if "createBracketController" not in controller or "setHandlers" not in controller:
        fail("controller/view handler seam must remain in place")

    print("OK: player-facing Capture/Export/Import UI is removed while storage helpers remain internal.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
