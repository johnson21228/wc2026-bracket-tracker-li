#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path.cwd()
html=(root/'site/game1/index.html').read_text(encoding='utf-8')
required=[
 'function resolveGame1R32RuleFromPointer',
 'function openMenuForResolvedGame1R32Rule',
 'window.WC2026_GAME1_R32_POINTER_RULE_RESOLVER',
 'data-active-slot-id',
 'pointer-resolved-manifest-slot',
 'openMenuForResolvedGame1R32Rule(rule, ev)'
]
missing=[s for s in required if s not in html]
if missing:
    print('Missing Game 1 R32 pointer rule integrity markers: '+', '.join(missing), file=sys.stderr)
    sys.exit(1)
if 'Winner Group I' not in html or 'Best third-place team from Groups C/D/F/G/H' not in html:
    print('Expected adjacent Winner Group I and third-place pool rule text not found', file=sys.stderr)
    sys.exit(1)
for rel in [
 'li/world_cup/game1_r32_pointer_rule_integrity_rule.md',
 'docs/features/game1_r32_pointer_rule_integrity.md',
 'cards/100_repair_game1_r32_pointer_rule_integrity_card.md',
 'capture_back/CAPTURE_BACK_GAME1_R32_POINTER_RULE_INTEGRITY.md'
]:
    if not (root/rel).exists():
        print(f'Missing {rel}', file=sys.stderr)
        sys.exit(1)
print('WC2026 Game 1 R32 pointer rule integrity checks passed.')
