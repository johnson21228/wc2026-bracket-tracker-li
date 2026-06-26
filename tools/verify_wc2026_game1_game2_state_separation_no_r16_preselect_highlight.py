#!/usr/bin/env python3
# Superseded by tools/verify_wc2026_single_game_admin_official_runtime.py.
# Legacy check: game1 game2 state separation.
import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
result = subprocess.run([sys.executable, str(ROOT / "tools/verify_wc2026_single_game_admin_official_runtime.py")])
if result.returncode != 0:
    raise SystemExit(result.returncode)
print("OK: legacy game1 game2 state separation verifier superseded by one-game Admin_/official runtime rule.")
