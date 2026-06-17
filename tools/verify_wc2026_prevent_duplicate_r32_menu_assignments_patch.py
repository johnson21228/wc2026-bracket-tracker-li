#!/usr/bin/env python3
from pathlib import Path
import sys

site = Path('site/index.html')
if not site.exists():
    print('Prevent duplicate R32 menu assignment verification failed: missing site/index.html')
    sys.exit(1)
text = site.read_text()
required = [
    'WC2026_PREVENT_DUPLICATE_R32_MENU_ASSIGNMENTS_CSS',
    'WC2026_PREVENT_DUPLICATE_R32_MENU_ASSIGNMENTS_JS',
    'installPreventDuplicateR32MenuAssignments',
    'getUsedR32TeamCodesExceptCurrentSlot',
    'collectCodesFromR32LocalStorage',
    'collectCodesFromVisibleR32Slots',
    'filterMenu(menu)',
    'rejectDuplicateSelection',
    'wc2026DuplicateR32Choice',
    'data-wc2026-r32-duplicate-choice',
    'Already picked in another R32 slot',
    'stopImmediatePropagation',
]
missing = [m for m in required if m not in text]
if missing:
    print('Prevent duplicate R32 menu assignment verification failed: missing marker(s): ' + ', '.join(missing))
    sys.exit(1)
if text.count('WC2026_PREVENT_DUPLICATE_R32_MENU_ASSIGNMENTS_JS') != 1:
    print('Prevent duplicate R32 menu assignment verification failed: expected one JS marker')
    sys.exit(1)
print('Prevent duplicate R32 menu assignment verification passed.')
