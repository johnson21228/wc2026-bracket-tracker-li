#!/usr/bin/env python3
from pathlib import Path
import json, sys, xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
def fail(msg): print(msg, file=sys.stderr); raise SystemExit(1)
def read(rel):
    p=ROOT/rel
    if not p.exists(): fail(f"Missing required file: {rel}")
    return p.read_text(encoding='utf-8')
for rel in ["li/world_cup/game1_transparent_svg_middle_layer_rule.md","docs/geometry/game1_transparent_svg_middle_layer.md","cards/097_repair_game1_transparent_svg_middle_layer_card.md","prompts/repair_game1_transparent_svg_middle_layer.md","capture_back/CAPTURE_BACK_GAME1_TRANSPARENT_SVG_MIDDLE_LAYER.md","tools/generate_uniform_pick_card_gameboard.py","site/assets/playfield/uniform_pick_card_gameboard.svg","site/assets/playfield/uniform_pick_card_gameboard.png","site/data/geometry/uniform_pick_card_gameboard_manifest.json","site/data/geometry/uniform_pick_card_gameboard_manifest.js"]:
    if not (ROOT/rel).exists(): fail(f"Missing required file: {rel}")
svg_path=ROOT/'site/assets/playfield/uniform_pick_card_gameboard.svg'
svg_text=svg_path.read_text(encoding='utf-8')
for forbidden in ['checker','proof v2','Final Four pick card twice as tall','url(#checker)']:
    if forbidden in svg_text: fail(f"Transparent SVG still contains proof/opaque marker: {forbidden}")
for required in ['data-layer-role="transparent-middle-gameboard"','id="connector-linework"','id="pick-card-slots"','fill="none"']:
    if required not in svg_text: fail(f"Transparent SVG missing marker: {required}")
try: root=ET.parse(svg_path).getroot()
except Exception as exc: fail(f"SVG is not parseable XML: {exc}")
for elem in root.iter():
    if not elem.tag.endswith('rect'): continue
    x,y,w,h=elem.attrib.get('x'),elem.attrib.get('y'),elem.attrib.get('width'),elem.attrib.get('height')
    fill=elem.attrib.get('fill','')
    if x in {'0','0.0',None} and y in {'0','0.0',None} and w in {'1536','1536.0'} and h in {'1024','1024.0'} and fill not in {'none','transparent',''}:
        fail('SVG contains an opaque full-board rectangle')
    if fill.startswith('url('): fail('SVG contains patterned fill; middle layer must be transparent')
manifest=json.loads(read('site/data/geometry/uniform_pick_card_gameboard_manifest.json'))
if manifest.get('presentationRole')!='transparent_middle_gameboard_layer': fail('Manifest must declare presentationRole transparent_middle_gameboard_layer')
if manifest.get('migrationStatus')!='game1_visible_board_and_r32_placement_use_uniform_svg_manifest_game2_not_migrated': fail('Manifest migrationStatus must reflect Game 1 placement migration and Game 2 not migrated')
slots=manifest.get('slots',[])
if len(slots)!=61: fail(f"Expected 61 manifest slots; found {len(slots)}")
if len([s for s in slots if s.get('round')=='R32'])!=32: fail('Expected 32 R32 manifest slots')
html=read('site/game1/index.html')
for marker in ['src="../assets/playfield/uniform_pick_card_gameboard.svg"','game1_pub_options_background.jpeg','data-board-layer-role="transparent-svg-linework"','applyUniformSvgR32ManifestGeometryToGame1SlotRules','uniform-svg-r32-manifest','window.WC2026_GAME1_UNIFORM_SVG_GEOMETRY_MAP','class="pickLayer" id="pickLayer"','class="hitLayer" id="hitLayer"']:
    if marker not in html: fail(f"Game 1 missing transparent middle-layer marker: {marker}")
for stale in ['data-placement-mode="legacy-game1-r32-slot-rules"','game1-uniform-svg-board-visible-placement-deferred','legacy-game1-r32-slot-rules']:
    if stale in html: fail(f"Game 1 still contains stale placement marker: {stale}")
game2_path=ROOT/'site/game2/index.html'
if game2_path.exists():
    game2=game2_path.read_text(encoding='utf-8')
    if 'uniform_pick_card_gameboard_manifest.js' in game2 or 'src="../assets/playfield/uniform_pick_card_gameboard.svg"' in game2:
        fail('Game 2 must not consume the uniform SVG board in this Game 1 repair')
print('WC2026 Game 1 transparent SVG middle-layer checks passed.')
