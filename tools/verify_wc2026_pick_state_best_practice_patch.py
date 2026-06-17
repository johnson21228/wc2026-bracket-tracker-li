#!/usr/bin/env python3
from pathlib import Path
text = Path('site/index.html').read_text()
required = [
    'WC2026_DISABLE_SHORT_TERM_R16_AUTO_HOLD',
    'WC2026_DISABLE_SHORT_TERM_R16_HOLD_FOR_CANONICAL_STATE',
    'WC2026_R16_RENDER_SOURCE_GATED',
    'WC2026_ADVANCEMENT_RENDER_SOURCE_GATED',
    'WC2026_CLEAR_PICKS_CANONICAL_ALL_GAME1_STATE',
]
missing = [m for m in required if m not in text]
if missing:
    raise SystemExit('Missing best-practice markers: ' + ', '.join(missing))
for forbidden in [
    'WC2026_EMPTY_STATE_ONLY_R32_ENABLED_GUARD',
    'setTimeout(() => wc2026ShortTermApplyR16Hold(false), 0);',
    'WC2026_CLEAR_PICKS_CLEARS_ALL_STALE_GAME1_STORAGE\n\n      try { if (typeof applyGame1ManifestR32GeometryToSlotRules',
]:
    if forbidden in text:
        raise SystemExit('Forbidden stale pattern still present: ' + forbidden[:80])
if text.count('document.getElementById("clearPicks").addEventListener("click"') != 1:
    raise SystemExit('Expected exactly one clearPicks click handler')
if text.count('<script') != text.count('</script>'):
    raise SystemExit('Mismatched script tag count')
print('WC2026 pick-state best-practice verification passed.')
