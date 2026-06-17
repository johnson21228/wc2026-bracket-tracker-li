#!/usr/bin/env python3
from pathlib import Path

ROOT = Path.cwd()
errors = []

def require_file(path):
    p = ROOT / path
    if not p.exists():
        errors.append(f"Missing {path}")
        return ""
    return p.read_text(errors='replace')

html = require_file('site/game1/index.html')
for needle in [
    'BRACKET_LIFECYCLE_STORAGE_KEY',
    'GAME1_KNOCKOUT_PICKS_STORAGE_KEY',
    'GAME2_KNOCKOUT_PICKS_STORAGE_KEY',
    'BRACKET_LIFECYCLE_PHASES',
    'GAME1_R32_ASSIGNMENT',
    'GAME1_KNOCKOUT_PREDICTION',
    'GAME1_LOCKED_FOR_SCORING',
    'GAME2_OFFICIAL_R32',
    'GAME2_KNOCKOUT_LIVE',
    'normalizeBracketLifecycleState',
    'loadBracketLifecycleState',
    'saveBracketLifecycleState',
    'isGame1LifecyclePhase',
    'isGame2LifecyclePhase',
    'isKnockoutPickSlotId',
    'pickModeForSlotId',
    'window.WC2026_BRACKET_LIFECYCLE',
    'preservesGame1Evidence',
]:
    if needle not in html:
        errors.append(f"site/game1/index.html missing {needle}")

for path in [
    'cards/116_add_bracket_lifecycle_state_card.md',
    'docs/features/bracket_lifecycle_state.md',
    'li/world_cup/bracket_lifecycle_state_rule.md',
    'prompts/add_bracket_lifecycle_state.md',
    'capture_back/CAPTURE_BACK_BRACKET_LIFECYCLE_STATE.md',
]:
    text = require_file(path)
    for needle in ['game1_r32_assignment', 'game1_knockout_prediction', 'game2_official_r32', 'knockoutPicks']:
        if needle not in text:
            errors.append(f"{path} missing {needle}")

if errors:
    print('WC2026 bracket lifecycle state checks failed:')
    for e in errors:
        print('-', e)
    raise SystemExit(1)

print('WC2026 bracket lifecycle state checks passed.')
