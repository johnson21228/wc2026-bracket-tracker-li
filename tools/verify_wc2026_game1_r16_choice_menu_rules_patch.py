#!/usr/bin/env python3
from pathlib import Path

required = [
    Path('cards/112_define_game1_r16_choice_menu_rules_card.md'),
    Path('docs/features/game1_r16_choice_menu_rules.md'),
    Path('li/world_cup/game1_r16_choice_menu_rule.md'),
    Path('prompts/define_game1_r16_choice_menu_rules.md'),
    Path('capture_back/CAPTURE_BACK_GAME1_R16_CHOICE_MENU_RULES.md'),
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit('Missing Game 1 R16 choice menu rule files: ' + ', '.join(missing))
rule = Path('li/world_cup/game1_r16_choice_menu_rule.md').read_text()
for phrase in ['two source R32 slots', 'exactly the two teams', 'stored separately from R32 assignment state']:
    if phrase not in rule:
        raise SystemExit(f'Missing expected rule phrase: {phrase}')
print('WC2026 Game 1 R16 choice menu rule checks passed.')
