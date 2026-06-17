#!/usr/bin/env python3
from pathlib import Path
p = Path('site/index.html')
if not p.exists():
    raise SystemExit('site/index.html not found')
text = p.read_text()
required = [
    'WC2026_RETARGET_OPEN_CHOICE_MENU_ON_PICKABLE_TAP',
    'installRetargetOpenChoiceMenuOnPickableTap',
    'retargetOpenMenuToTappedPickableItem',
    'dispatchOpenClick',
    'choice-menu-retargeted',
    'document.addEventListener("pointerdown", retargetOpenMenuToTappedPickableItem, true)',
    'document.addEventListener("click", retargetOpenMenuToTappedPickableItem, true)',
]
missing = [s for s in required if s not in text]
if missing:
    raise SystemExit('Retarget open choice menu verification failed: missing ' + ', '.join(missing))
print('Retarget open choice menu verification passed.')
