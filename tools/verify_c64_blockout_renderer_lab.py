#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "labs" / "011_goal_language_to_asm_blockout_renderer"
LI = ROOT / "li" / "labs" / "011_goal_language_to_asm_blockout_renderer.md"

if not LI.exists():
    raise SystemExit("Missing Lab 011 LI")

for phrase in ["Goal Language to ASM", "geometry intent", "deterministic"]:
    if phrase not in LI.read_text(encoding="utf-8"):
        raise SystemExit(f"Lab 011 LI missing phrase: {phrase}")

result = subprocess.run(["make", "-C", str(LAB), "verify"], cwd=ROOT)
if result.returncode != 0:
    raise SystemExit(result.returncode)

print("OK: root Lab 011 Blockout renderer verifier passed.")
