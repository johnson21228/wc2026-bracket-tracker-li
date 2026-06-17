from pathlib import Path
text = Path('site/game1/index.html').read_text(encoding='utf-8')
required = [
    'WC2026_SHORT_TERM_R16_HOLD_START',
    'window.WC2026_SHORT_TERM_R16_HOLD',
    'L-R16-01',
    'R32-L-M1A',
    'L-R32-01',
    'r16Picks[TARGET_R16_SLOT_ID]',
    'saveR16Picks(r16Picks)',
    'renderOneR16Pick(rule, storedPick)',
    'short-term-r16-hardcoded-hold-v001',
]
missing = [r for r in required if r not in text]
if missing:
    raise SystemExit('Missing short-term R16 hold markers: ' + ', '.join(missing))
print('Short-term R16 hardcoded hold verification passed.')
