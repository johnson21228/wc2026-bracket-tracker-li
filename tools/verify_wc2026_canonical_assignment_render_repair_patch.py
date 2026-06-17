from pathlib import Path

html = Path('site/game1/index.html')
text = html.read_text(encoding='utf-8')

required = [
    'WC2026_CANONICAL_ASSIGNMENT_RENDER_REPAIR_START',
    'function wc2026RenderAssignmentToPickedCell',
    'function wc2026RenderPickedCellIfMissing',
    'wc2026RenderAssignmentToPickedCell(targetRule, storedPick, round, targetSlotId)',
    'menu.dataset.assignmentSlotId = String(rule.slotId || "")',
    'menu.dataset.assignmentRound = round',
    'renderOneR16Pick(targetRule, pick)',
    'renderOneAdvancementPick(targetRule, pick)',
]

missing = [item for item in required if item not in text]
if missing:
    raise SystemExit('Missing canonical assignment render repair markers: ' + ', '.join(missing))

print('Canonical knockout assignment render repair verification passed.')
