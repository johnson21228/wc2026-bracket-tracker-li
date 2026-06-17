#!/usr/bin/env python3
from pathlib import Path

root = Path.cwd()
runner = root / "tools" / "run_wc2026_game1_knockout_choice_resolution_tests.js"
text = runner.read_text(encoding="utf-8")
required = [
    "const DATA_BUNDLE = path.join(ROOT, 'site', 'data', 'game1_data_bundle.js');",
    "function loadGame1DataBundle(context)",
    "vm.runInContext(source, context, { filename: 'site/data/game1_data_bundle.js' });",
    "context.GAME1_DATA = context.window.WC2026_GAME1_DATA;",
    "loadGame1DataBundle(context);",
    "dataBundleLoaded: Boolean(context.window.WC2026_GAME1_DATA)",
]
missing = [s for s in required if s not in text]
if missing:
    raise SystemExit("Missing Node knockout data-loading repair markers:\n" + "\n".join(f"- {m}" for m in missing))
print("WC2026 Game 1 Node knockout data-loading repair checks passed.")
