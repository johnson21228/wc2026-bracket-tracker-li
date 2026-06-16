#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG = ROOT / "site/assets/playfield/uniform_pick_card_gameboard.svg"
PNG = ROOT / "site/assets/playfield/uniform_pick_card_gameboard.png"
MANIFEST = ROOT / "site/data/geometry/uniform_pick_card_gameboard_manifest.json"
W, H = 1536, 1024
CARD_W, CARD_H = 140, 44
FINAL_W, FINAL_H = 210, 168
EXPECTED_ROUND_COUNTS = {"R32": 32, "R16": 16, "QF": 8, "SF": 4, "FINAL_FOUR": 1}
ROUND_SEQUENCE = [("R32","left","L-R32",16),("R32","right","R-R32",16),("R16","left","L-R16",8),("R16","right","R-R16",8),("QF","left","L-QF",4),("QF","right","R-QF",4),("SF","left","L-SF",2),("SF","right","R-SF",2),("FINAL_FOUR","center","CENTER-FINAL-FOUR",1)]

STROKE = "#AA9691"
CONNECTOR_OPACITY = "0.88"
SLOT_OPACITY = "0.92"
STANDARD_FILL = "#816A51"
STANDARD_FILL_OPACITY = "0.26"
R32_FILL = "#816A51"
R32_FILL_OPACITY = "0.52"
FINAL_FILL_OPACITY = "0.34"


def numeric(value: str):
    parsed = float(value)
    return int(parsed) if abs(parsed - round(parsed)) < 1e-9 else parsed

def esc(value: str) -> str:
    return value.replace("&", "&amp;").replace('"', "&quot;")

def build_svg() -> str:
    rects=[]; paths=[]; rect_meta=[]
    def card(x,y,w=CARD_W,h=CARD_H,round_name="",side="",idx=0,final=False):
        rx=10 if final else 6
        selectable = round_name == "R32"
        fill_opacity = FINAL_FILL_OPACITY if final else (R32_FILL_OPACITY if selectable else STANDARD_FILL_OPACITY)
        cls = "pick-card-slot slot-r32-selectable" if selectable else ("pick-card-slot slot-final-four" if final else "pick-card-slot slot-board-structure")
        rects.append(
            f'<rect class="{cls}" data-round="{round_name}" data-side="{side}" data-index="{idx}" '
            f'x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" '
            f'fill="{STANDARD_FILL}" fill-opacity="{fill_opacity}" '
            f'stroke="{STROKE}" stroke-opacity="{SLOT_OPACITY}" stroke-width="2" rx="{rx:g}" ry="{rx:g}" '
            f'vector-effect="non-scaling-stroke"/>'
        )
        rect_meta.append((round_name, side, idx))
        return {"x":x,"y":y,"w":w,"h":h,"cx":x+w/2,"cy":y+h/2,"left":x,"right":x+w,"top":y,"bottom":y+h}
    def path(d, sw=3):
        paths.append(f'<path class="connector-line" d="{esc(d)}" stroke="{STROKE}" stroke-opacity="{CONNECTOR_OPACITY}" stroke-width="{sw}" fill="none" stroke-linecap="square" stroke-linejoin="miter" vector-effect="non-scaling-stroke"/>')
    xL=[38,225,418,590]; xR=[1358,1165,978,806]; ys32=[118+i*48 for i in range(16)]
    left32=[card(xL[0],y,round_name="R32",side="left",idx=i+1) for i,y in enumerate(ys32)]
    right32=[card(xR[0],y,round_name="R32",side="right",idx=i+1) for i,y in enumerate(ys32)]
    def mids(cards): return [(cards[i]['cy']+cards[i+1]['cy'])/2 for i in range(0,len(cards),2)]
    left16=[card(xL[1], y-CARD_H/2, round_name="R16", side="left", idx=i+1) for i,y in enumerate(mids(left32))]
    right16=[card(xR[1], y-CARD_H/2, round_name="R16", side="right", idx=i+1) for i,y in enumerate(mids(right32))]
    left8=[card(xL[2], y-CARD_H/2, round_name="QF", side="left", idx=i+1) for i,y in enumerate(mids(left16))]
    right8=[card(xR[2], y-CARD_H/2, round_name="QF", side="right", idx=i+1) for i,y in enumerate(mids(right16))]
    left4=[card(xL[3], y-CARD_H/2, round_name="SF", side="left", idx=i+1) for i,y in enumerate(mids(left8))]
    right4=[card(xR[3], y-CARD_H/2, round_name="SF", side="right", idx=i+1) for i,y in enumerate(mids(right8))]
    final=card((W-FINAL_W)/2, (H-FINAL_H)/2, FINAL_W, FINAL_H, round_name="FINAL_FOUR", side="center", idx=1, final=True)
    def conn_left(a,b,stub=22):
        xj=a[0]['right']+stub; y1,y2,ym=a[0]['cy'],a[1]['cy'],b['cy']
        path(f'M {a[0]["right"]:g} {y1:g} H {xj:g} V {y2:g} H {a[1]["right"]:g} M {xj:g} {ym:g} H {b["left"]:g}')
    def conn_right(a,b,stub=22):
        xj=a[0]['left']-stub; y1,y2,ym=a[0]['cy'],a[1]['cy'],b['cy']
        path(f'M {a[0]["left"]:g} {y1:g} H {xj:g} V {y2:g} H {a[1]["left"]:g} M {xj:g} {ym:g} H {b["right"]:g}')
    for src,dst in [(left32,left16),(left16,left8),(left8,left4)]:
        for i,b in enumerate(dst): conn_left([src[2*i],src[2*i+1]],b)
    for src,dst in [(right32,right16),(right16,right8),(right8,right4)]:
        for i,b in enumerate(dst): conn_right([src[2*i],src[2*i+1]],b)
    left_trunk=760; right_trunk=776
    path(f'M {left4[0]["right"]:g} {left4[0]["cy"]:g} H {left_trunk:g}')
    path(f'M {left4[1]["right"]:g} {left4[1]["cy"]:g} H {left_trunk:g}')
    path(f'M {left_trunk:g} {left4[0]["cy"]:g} V {left4[1]["cy"]:g}')
    path(f'M {left_trunk:g} {final["cy"]:g} H {final["left"]:g}')
    path(f'M {right4[0]["left"]:g} {right4[0]["cy"]:g} H {right_trunk:g}')
    path(f'M {right4[1]["left"]:g} {right4[1]["cy"]:g} H {right_trunk:g}')
    path(f'M {right_trunk:g} {right4[0]["cy"]:g} V {right4[1]["cy"]:g}')
    path(f'M {right_trunk:g} {final["cy"]:g} H {final["right"]:g}')
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" data-layer-role="transparent-middle-gameboard" data-geometry-authority="uniform-svg-gameboard" data-presentation-style="material-brown-selectable-r32">',
        '<desc>Transparent material-colored bracket stencil. Pick-card slots use sampled tan fill and lightened brown linework; R32 rectangles carry stronger selectable-target fill. Background imagery is supplied by the bottom layer.</desc>',
        '<metadata>{"background":"transparent","geometryAuthority":"svg","presentation":"material-brown-selectable-r32","derivedManifest":"site/data/geometry/uniform_pick_card_gameboard_manifest.json"}</metadata>',
        '<defs><style><![CDATA[.connector-line{pointer-events:none}.pick-card-slot{pointer-events:none}.slot-r32-selectable{pointer-events:none}]]></style></defs>',
        '<g id="connector-linework" data-layer="linework" data-stroke-policy="lightened-brown-over-background">',
        *paths,
        '</g>',
        '<g id="pick-card-slots" data-layer="slot-outlines" data-fill-policy="material-r32-selectable-fill">',
        *rects,
        '</g>',
        '</svg>',
        ''
    ])

def find_rects(root):
    group=None
    for elem in root.iter():
        if elem.tag.endswith('g') and elem.attrib.get('id')=='pick-card-slots': group=elem; break
    if group is None: raise SystemExit("SVG missing <g id='pick-card-slots'>")
    return [e for e in list(group) if e.tag.endswith('rect')]

def build_manifest():
    root=ET.parse(SVG).getroot(); rects=find_rects(root); slots=[]; cursor=0
    for round_name, side, prefix, count in ROUND_SEQUENCE:
        for idx in range(1,count+1):
            rect=rects[cursor]; cursor+=1
            slot_id=prefix if prefix=='CENTER-FINAL-FOUR' else f'{prefix}-{idx:02d}'
            slot={
                "slotId":slot_id,
                "round":round_name,
                "side":side,
                "boundsPx":{"x":numeric(rect.attrib['x']),"y":numeric(rect.attrib['y']),"width":numeric(rect.attrib['width']),"height":numeric(rect.attrib['height'])},
                "rx":numeric(rect.attrib.get('rx','0')),
                "ry":numeric(rect.attrib.get('ry','0')),
                "source":"uniform_pick_card_gameboard.svg#pick-card-slots",
                "presentationClass":rect.attrib.get('class',''),
                "fillOpacity":numeric(rect.attrib.get('fill-opacity','0')),
                "stroke":rect.attrib.get('stroke')
            }
            if round_name in {'R32','R16','QF','SF'}: slot['roundIndex']=idx
            if round_name=='R32': slot['game1SelectableTarget']=True
            if round_name=='FINAL_FOUR': slot['specialRole']='finalFourPickCard'; slot['note']='Special center Final Four pick card; taller than standard pick cards.'
            slots.append(slot)
    return {
        "schemaVersion":4,
        "assetFamily":"uniform_pick_card_gameboard",
        "authority":"svg_geometry_source",
        "presentationRole":"transparent_middle_gameboard_layer",
        "presentationStyle":"material_brown_selectable_r32",
        "geometrySource":"site/assets/playfield/uniform_pick_card_gameboard.svg",
        "svgAsset":"assets/playfield/uniform_pick_card_gameboard.svg",
        "pngAsset":"assets/playfield/uniform_pick_card_gameboard.png",
        "nativeSizePx":{"width":W,"height":H},
        "boardModel":{"id":"uniform_pick_card_gameboard_v1_final_four_center_card","description":"Transparent middle-layer material-colored bracket with sampled tan pick-card fills, lightened brown linework, stronger R32 selectable-target fill, uniform pick-card geometry through semifinal, and one special twice-tall Final Four center card.","standardPickCardPx":{"width":CARD_W,"height":CARD_H},"finalFourPickCardPx":{"width":FINAL_W,"height":FINAL_H},"expectedPickCardRecords":61,"roundCounts":EXPECTED_ROUND_COUNTS},
        "presentationPolicy":{"background":"transparent","connectorStroke":STROKE,"slotStroke":STROKE,"r32SelectableFill":R32_FILL,"r32SelectableFillOpacity":numeric(R32_FILL_OPACITY),"standardSlotFillOpacity":numeric(STANDARD_FILL_OPACITY),"finalFourFillOpacity":numeric(FINAL_FILL_OPACITY)},
        "layerContract":["bottomBackgroundLayer","transparentSvgGameboardLineworkLayer","interactionHitTargetLayer","pickCardLayer","overlayUiLayer"],
        "slotPolicy":"SVG pick-card rectangles are geometry truth; R32 slots carry material-colored selectable-target fill for Game 1 presentation.",
        "migrationStatus":"game1_visible_board_and_r32_placement_use_uniform_svg_manifest_game2_not_migrated",
        "slots":slots
    }

def main():
    SVG.parent.mkdir(parents=True, exist_ok=True); MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    SVG.write_text(build_svg(), encoding='utf-8')
    MANIFEST.write_text(json.dumps(build_manifest(), indent=2)+'\n', encoding='utf-8')
    try:
        import cairosvg
        cairosvg.svg2png(url=str(SVG), write_to=str(PNG), output_width=W, output_height=H)
        print(f'Rendered {PNG}')
    except Exception as exc:
        print(f'PNG render skipped: {exc}')
    print(f'Wrote {SVG}'); print(f'Wrote {MANIFEST}')
if __name__=='__main__': main()
