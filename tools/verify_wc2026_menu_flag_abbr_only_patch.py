#!/usr/bin/env python3
from pathlib import Path
import sys

site = Path('site/index.html')
if not site.exists():
    print('Menu flag+abbr-only verification failed: missing site/index.html')
    sys.exit(1)
text = site.read_text()
required = [
    'WC2026_MENU_FLAG_ABBR_ONLY_INSTALLED',
    'WC2026_MENU_FLAG_ABBR_ONLY_JS',
    'wc2026MenuFlagAbbrOnly',
    'wc2026MenuFlag',
    'wc2026MenuAbbr',
    'data.wc2026FlagAbbrOnly',
    'inferCode(item)',
    'findExistingFlagNode(item)',
    'MutationObserver',
    'MENU_SELECTOR',
    'ITEM_SELECTOR',
    'teamTile',
    'menuChoice',
    'countryChoice',
]
missing = [m for m in required if m not in text]
if missing:
    print('Menu flag+abbr-only verification failed: missing marker(s): ' + ', '.join(missing))
    sys.exit(1)
if text.count('WC2026_MENU_FLAG_ABBR_ONLY_INSTALLED') != 1:
    print('Menu flag+abbr-only verification failed: expected one installed CSS marker')
    sys.exit(1)
print('Menu flag+abbr-only rendering verification passed.')
