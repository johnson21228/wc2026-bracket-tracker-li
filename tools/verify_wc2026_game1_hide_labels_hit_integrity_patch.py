#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
root = Path.cwd()
html_path = root / 'site/game1/index.html'
if not html_path.exists():
    raise SystemExit('Missing site/game1/index.html')
html = html_path.read_text(encoding='utf-8')
required = [
    'function applyGame1ManifestR32GeometryToSlotRules',
    'WC2026_GAME1_R32_RULE_HIT_INTEGRITY',
    'implementation labels hidden',
]
for token in required:
    if token not in html:
        raise SystemExit(f'Missing Game 1 hide-label/hit-integrity token: {token}')
if not re.search(r'\.slotLabel\s*,\s*\.pickRule[^{}]*\{[^}]*display\s*:\s*none\s*!important', html, re.S):
    raise SystemExit('Expected .slotLabel and .pickRule to be hidden with display:none !important')
# Verify source rule data keeps the expected adjacent winner/third-place semantics.
bundle_path = root / 'site/data/game1_data_bundle.js'
if not bundle_path.exists():
    raise SystemExit('Missing site/data/game1_data_bundle.js')
text = bundle_path.read_text(encoding='utf-8').strip()
if '=' not in text:
    raise SystemExit('Could not parse game1_data_bundle.js')
js = text.split('=', 1)[1].strip()
if js.endswith(';'):
    js = js[:-1]
data = json.loads(js)
by_pos = {int(r['position']): r for r in data['slotRules'] if r.get('round') == 'R32'}
expect = {
    6: '3 A/B/C/D/F',
    7: '1I',
    8: '3 C/D/F/G/H',
    14: '3 C/E/F/H/I',
    16: '3 E/H/I/J/K',
}
for pos, slot_rule in expect.items():
    actual = by_pos.get(pos, {}).get('slotRule')
    if actual != slot_rule:
        raise SystemExit(f'Unexpected R32 slot rule at position {pos}: expected {slot_rule!r}, got {actual!r}')
manifest_path = root / 'site/data/geometry/uniform_pick_card_gameboard_manifest.json'
if not manifest_path.exists():
    raise SystemExit('Missing uniform SVG manifest')
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
r32 = [s for s in manifest.get('slots', []) if s.get('round') == 'R32']
if len(r32) != 32:
    raise SystemExit(f'Expected 32 R32 manifest slots, found {len(r32)}')
for side, expected in [('left', 16), ('right', 16)]:
    count = len([s for s in r32 if s.get('side') == side])
    if count != expected:
        raise SystemExit(f'Expected {expected} {side} R32 manifest slots, found {count}')
print('WC2026 Game 1 hide-label and R32 hit-rule integrity checks passed.')
