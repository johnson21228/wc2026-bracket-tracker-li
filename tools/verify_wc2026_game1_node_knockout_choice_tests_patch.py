#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / 'tools' / 'run_wc2026_game1_knockout_choice_resolution_tests.js'
GAME1 = ROOT / 'site' / 'game1' / 'index.html'

def fail(msg: str) -> None:
    print(f'ERROR: {msg}', file=sys.stderr)
    sys.exit(1)

if not GAME1.exists():
    fail('missing site/game1/index.html')
if not RUNNER.exists():
    fail('missing Node knockout choice resolution runner')
text = RUNNER.read_text(encoding='utf-8')
for marker in [
    'WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS',
    'vm.runInContext',
    'testKnockoutChoiceResolution',
    'R16-1',
    'QF-1',
    'SF-1',
    'expected exactly two contestants',
]:
    if marker not in text:
        fail(f'missing runner marker: {marker}')

html = GAME1.read_text(encoding='utf-8')
if 'WC2026_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS' not in html:
    fail('missing browser harness marker that the Node runner extracts')

print('WC2026 Game 1 Node knockout choice resolution test runner checks passed.')
