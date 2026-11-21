# Gambar Bab 5: peta isomer, enansiomer butan-2-ol, asam tartarat, Fischer
import os, io, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab05/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'

# 1. peta isomer
f, ax = plt.subplots(figsize=(7.2, 3.4), dpi=220); ax.set_xlim(0, 20); ax.set_ylim(0, 10); ax.axis('off')
def kotak(x, y, w, h, t, fc='#eef4fa', ec=TUA, fs=8.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08,rounding_size=0.25', fc=fc, ec=ec, lw=1))
    ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=fs, color=TUA)
def panah(x1, y1, x2, y2, t='', dx=0.15):
    ax.annotate('', (x2, y2), (x1, y1), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1))
    if t: ax.text((x1 + x2) / 2 + dx, (y1 + y2) / 2, t, fontsize=7.8, color=JT, va='center')
kotak(6.5, 8.2, 7, 1.4, 'isomer (rumus molekul sama)', '#e8f1fa')
panah(8.5, 8.1, 4.2, 6.3, 'sambungan beda', -3.6); panah(11.5, 8.1, 15.0, 6.3, 'sambungan sama', 0.3)
kotak(0.6, 4.9, 6.4, 1.3, 'isomer konstitusi\n(butana / 2-metilpropana)', '#fdf1e6', JT)
kotak(12.0, 4.9, 6.4, 1.3, 'stereoisomer\n(susunan ruang beda)', '#e8f1fa')
panah(13.6, 4.8, 11.2, 2.8, 'bayangan cermin', -3.4); panah(16.8, 4.8, 17.4, 2.8, 'bukan', 0.25)
kotak(7.6, 1.2, 5.4, 1.4, 'enansiomer\n((R)/(S)-butan-2-ol)', '#e9f6f1', HJ)
kotak(14.2, 1.2, 5.6, 1.4, 'diastereomer\n(cis/trans-but-2-ena, meso)', '#e9f6f1', HJ)
kotak(0.6, 1.2, 5.6, 1.4, 'konformer: bukan isomer\n(anti/gauche-butana)', '#f4f4f4', '#9aa5b1', 8)
f.savefig(f'{F}/peta.png', bbox_inches='tight'); plt.close(f)

def rd(smi, w=420, h=320, fs=28):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions()
    o.bondLineWidth = 2; o.fixedFontSize = fs; o.addStereoAnnotation = True; o.padding = 0.15
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 35: (0.55, 0.2, 0.1)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))

# 2. enansiomer butan-2-ol
f, ax = plt.subplots(1, 3, figsize=(7.0, 2.6), dpi=220, gridspec_kw={'width_ratios': [1, 0.12, 1]})
for a in ax: a.axis('off')
ax[0].imshow(rd('C[C@@H](O)CC')); ax[2].imshow(rd('C[C@H](O)CC'))
ax[1].axvline(0.5, color=BIRU, lw=2, ls=(0, (4, 3))); ax[1].set_xlim(0, 1); ax[1].text(0.5, -0.06, 'cermin', ha='center', fontsize=8, color=BIRU, transform=ax[1].transAxes, bbox=dict(fc='white', ec='none', pad=1))
ax[0].set_title('(R)-butan-2-ol', color=TUA, fontsize=9.5, y=-0.12); ax[2].set_title('(S)-butan-2-ol', color=TUA, fontsize=9.5, y=-0.12)
plt.tight_layout(); f.savefig(f'{F}/enansiomer.png', bbox_inches='tight'); plt.close(f)

# 3. asam tartarat (Fischer manual)
def fischer(ax, kiri, kanan, judul, meso=False):
    ax.set_xlim(-2, 2); ax.set_ylim(-2.6, 2.4); ax.set_aspect('equal'); ax.axis('off')
    ax.plot([0, 0], [-1.6, 1.6], color=TUA, lw=2)
    for y, l, r in [(0.55, kiri[0], kanan[0]), (-0.55, kiri[1], kanan[1])]:
        ax.plot([-0.9, 0.9], [y, y], color=TUA, lw=2)
        ax.text(-1.05, y, l, ha='right', va='center', fontsize=10, color=JT if l == 'OH' else TUA)
        ax.text(1.05, y, r, ha='left', va='center', fontsize=10, color=JT if r == 'OH' else TUA)
    ax.text(0, 1.8, 'COOH', ha='center', fontsize=10, color=TUA); ax.text(0, -2.05, 'COOH', ha='center', fontsize=10, color=TUA)
    if meso: ax.plot([-1.8, 1.8], [0, 0], color=BIRU, lw=1.4, ls=(0, (4, 3)))
    ax.set_title(judul, color=TUA, fontsize=9.5, y=-0.1)
f, ax = plt.subplots(1, 3, figsize=(6.6, 2.7), dpi=220)
fischer(ax[0], ['H', 'HO'], ['OH', 'H'], '(R,R)')
fischer(ax[1], ['HO', 'H'], ['H', 'OH'], '(S,S)')
fischer(ax[2], ['H', 'H'], ['OH', 'OH'], 'meso (R,S)', True)
plt.tight_layout(); f.savefig(f'{F}/tartarat.png', bbox_inches='tight'); plt.close(f)

# 4. Fischer gliseraldehida dan arti 3D
f, ax = plt.subplots(1, 2, figsize=(5.8, 2.7), dpi=220)
a = ax[0]; a.set_xlim(-2, 2); a.set_ylim(-2.2, 2.2); a.set_aspect('equal'); a.axis('off')
a.plot([0, 0], [-1.3, 1.3], color=TUA, lw=2); a.plot([-1.2, 1.2], [0, 0], color=TUA, lw=2)
a.text(0, 1.5, 'CHO', ha='center', fontsize=10, color=TUA); a.text(0, -1.75, 'CH$_2$OH', ha='center', fontsize=10, color=TUA)
a.text(-1.35, 0, 'H', ha='right', va='center', fontsize=10, color=TUA); a.text(1.35, 0, 'OH', ha='left', va='center', fontsize=10, color=JT)
a.set_title('proyeksi Fischer', color=TUA, fontsize=9.5, y=-0.08)
b = ax[1]; b.set_xlim(-2, 2); b.set_ylim(-2.2, 2.2); b.set_aspect('equal'); b.axis('off')
for (x2, y2), w in [((-1.2, 0.05), 'tebal'), ((1.2, 0.05), 'tebal')]:
    b.add_patch(Polygon([(0, 0.05), (x2, y2 + 0.13), (x2, y2 - 0.13)], fc=TUA, ec=TUA))
for y2 in (1.3, -1.3):
    for t in np.linspace(0.12, 0.95, 8):
        hw = 0.12 * t; b.plot([-hw, hw], [y2 * t, y2 * t], color=TUA, lw=1.4)
b.text(0, 1.5, 'CHO', ha='center', fontsize=10, color=TUA); b.text(0, -1.75, 'CH$_2$OH', ha='center', fontsize=10, color=TUA)
b.text(-1.35, 0.05, 'H', ha='right', va='center', fontsize=10, color=TUA); b.text(1.35, 0.05, 'OH', ha='left', va='center', fontsize=10, color=JT)
b.set_title('arti 3D: datar = depan, tegak = belakang', color=TUA, fontsize=9, y=-0.08)
plt.tight_layout(); f.savefig(f'{F}/fischer.png', bbox_inches='tight'); plt.close(f)
print('ok')

# ================= gambar tambahan =================
import io, sys, numpy as np; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rdkit import Chem
from rdkit.Chem import rdCIPLabeler
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Ellipse, Polygon, FancyBboxPatch
from lewis import molekul, MERAH
def simpan(f, n): f.savefig(f'{F}/{n}.png', bbox_inches='tight'); plt.close(f)
def T(ax, x, y, s, c=TUA, fs=10, **k): ax.text(x, y, s, ha=k.pop('ha', 'center'), va=k.pop('va', 'center'), color=c, fontsize=fs, **k)
def rd(smi, w=440, h=320, bl=42, fs=26, notes=None, hl=(), cip=False, hs=False):
    m = Chem.MolFromSmiles(smi)
    if hs: m = Chem.AddHs(m, onlyOnAtoms=tuple(a.GetIdx() for a in m.GetAtoms() if a.GetChiralTag() != Chem.ChiralType.CHI_UNSPECIFIED))
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = 0.12; o.fixedBondLength = bl
    o.annotationFontScale = 0.8; o.addStereoAnnotation = cip
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.1, 0.54, 0.42), 35: (0.55, 0.2, 0.1), 1: (0.05, 0.15, 0.28)}); o.setBackgroundColour((1, 1, 1, 0))
    for i, t in (notes or {}).items(): m.GetAtomWithIdx(i).SetProp('atomNote', t)
    hl = list(hl)
    rdMolDraw2D.PrepareAndDrawMolecule(d, m, highlightAtoms=hl, highlightAtomColors={i: (0.94, 0.63, 0.38) for i in hl}, highlightBonds=[])
    d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def pusat(smi):
    m = Chem.MolFromSmiles(smi); return [i for i, _ in Chem.FindMolChiralCenters(m, includeUnassigned=True, useLegacyImplementation=False)]

# 5. mencari pusat kiral
D = [('CCCC(C)Br', '2-bromopentana: 1 pusat kiral'), ('CCC(Br)CC', '3-bromopentana: tidak ada\n(dua gugus etil sama)'),
     ('CC(C)Cc1ccc(cc1)C(C)C(=O)O', 'ibuprofen: 1 pusat kiral'), ('CC(C)C1CCC(C)CC1O', 'mentol: 3 pusat kiral')]
f, ax = plt.subplots(1, 4, figsize=(7.6, 2.4), dpi=220)
for a, (s, t) in zip(ax, D): a.imshow(rd(s, w=420, h=340, bl=40, fs=24, hl=pusat(s))); a.axis('off'); a.set_title(t, fontsize=8.2, color=TUA, y=-0.25)
plt.tight_layout(); simpan(f, 'pusatkiral')

# 6. prioritas CIP pada (R)-butan-2-ol dan aturan setir
f, ax = plt.subplots(1, 2, figsize=(7.2, 2.9), dpi=220, gridspec_kw={'width_ratios': [1, 1.15]})
ax[0].imshow(rd('CC[C@@H](C)O', w=460, h=360, bl=60, fs=30, hs=True, notes={4: '1', 1: '2', 3: '3', 5: '4'})); ax[0].axis('off')
ax[0].set_title('prioritas: OH (1) > CH₂CH₃ (2) > CH₃ (3) > H (4)', fontsize=8.5, color=TUA, y=-0.12)
a = ax[1]; a.set_xlim(0, 10); a.set_ylim(0, 6.4); a.set_aspect('equal'); a.axis('off')
for cx, arah, lab, c in [(2.5, -1, 'R (rectus)\nsearah jarum jam', HJ), (7.5, 1, 'S (sinister)\nberlawanan arah', JT)]:
    pts = {1: (cx, 4.6), 2: (cx + 1.4 * (-arah), 2.6), 3: (cx - 1.4 * (-arah), 2.6)}
    a.add_patch(Circle((cx, 3.3), 0.25, color=TUA)); a.text(cx, 3.3, '4', color='white', fontsize=7, ha='center', va='center')
    for k, (x, y) in pts.items(): a.add_patch(Circle((x, y), 0.38, fc=MUDA, ec=TUA, lw=0.8)); a.text(x, y, str(k), ha='center', va='center', fontsize=9, color=TUA, fontweight='bold')
    a.add_patch(FancyArrowPatch((cx + 0.5 * (-arah) * -1 * -1 * 1, 4.75), (cx + 1.6 * (-arah), 3.1), connectionstyle=f'arc3,rad={0.45 * arah}', arrowstyle='-|>', mutation_scale=11, color=c, lw=1.5))
    a.text(cx, 1.1, lab, ha='center', fontsize=8.5, color=c, fontweight='bold')
a.text(5, 6.1, 'gugus prioritas 4 di belakang; telusuri 1 → 2 → 3', ha='center', fontsize=8.3, color=TUA)
plt.tight_layout(); simpan(f, 'cip')

# 7. polarimeter
f, ax = plt.subplots(figsize=(7.4, 2.2), dpi=220); ax.set_xlim(0, 30); ax.set_ylim(0, 8); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Circle((1.6, 4), 1.0, fc='#ffe9a8', ec=TUA)); T(ax, 1.6, 1.8, 'sumber cahaya\n(lampu Na, 589 nm)', fs=7.5)
for x in (3.5, 4.5, 5.5): ax.annotate('', (x + 0.8, 4), (x, 4), arrowprops=dict(arrowstyle='-|>', color=JG, lw=1.0))
ax.add_patch(Rectangle((7.0, 2.6), 0.4, 2.8, fc=MUDA, ec=TUA)); T(ax, 7.2, 1.8, 'polarisator', fs=7.5)
ax.plot([8.6, 8.6], [3.0, 5.0], color=BIRU, lw=2); T(ax, 8.6, 6.0, 'cahaya\nterpolarisasi', fs=7.3, c=BIRU)
ax.add_patch(FancyBboxPatch((10.0, 3.1), 7.5, 1.8, boxstyle='round,pad=0.1', fc='#f3e7da', ec=JT)); T(ax, 13.75, 4.0, 'tabung sampel', fs=8, c=JT); T(ax, 13.75, 2.3, 'panjang $l$, konsentrasi $c$', fs=7.5, c=JT)
ax.plot([19.0, 19.6], [3.0, 5.0], color=BIRU, lw=2); ax.plot([19.3, 19.3], [3.0, 5.0], color='#bbbbbb', lw=1, ls='--')
T(ax, 19.3, 5.8, 'diputar α', fs=8.5, c=MERAH)
ax.add_patch(Rectangle((21.5, 2.6), 0.4, 2.8, fc=MUDA, ec=TUA)); T(ax, 21.7, 1.8, 'analisator\n(diputar)', fs=7.5)
ax.add_patch(Ellipse((25.0, 4), 1.6, 1.2, fc='white', ec=TUA)); ax.add_patch(Circle((25.0, 4), 0.35, color=TUA)); T(ax, 25.0, 1.8, 'pengamat', fs=7.5)
T(ax, 15, 7.4, '[α] = α / ($l$ · $c$),  $l$ dalam dm, $c$ dalam g mL$^{-1}$', fs=8.5)
simpan(f, 'polarimeter')

# 8. efedrina dan pseudoefedrina
f, ax = plt.subplots(1, 2, figsize=(6.8, 2.6), dpi=220)
for a, (s, t) in zip(ax, [('CN[C@@H](C)[C@H](O)c1ccccc1', '(1R,2S)-efedrina\ntitik leleh 34 °C'), ('CN[C@@H](C)[C@@H](O)c1ccccc1', '(1S,2S)-pseudoefedrina\ntitik leleh 119 °C')]):
    a.imshow(rd(s, w=480, h=340, bl=42, fs=24, cip=True)); a.axis('off'); a.set_title(t, fontsize=9, color=TUA, y=-0.2)
f.text(0.5, 0.55, 'diastereomer:\nberbeda pada\nsatu pusat saja', ha='center', va='center', fontsize=8.3, color=JT)
plt.tight_layout(w_pad=4); simpan(f, 'efedrina')

# 9. empat stereoisomer 2-bromo-3-klorobutana
f, ax = plt.subplots(figsize=(6.8, 4.4), dpi=220); ax.set_xlim(0, 20); ax.set_ylim(0, 13); ax.axis('off')
S4 = [('C[C@@H](Br)[C@@H](C)Cl', '(2R,3R)', (4, 10.2)), ('C[C@H](Br)[C@H](C)Cl', '(2S,3S)', (16, 10.2)), ('C[C@@H](Br)[C@H](C)Cl', '(2R,3S)', (4, 2.8)), ('C[C@H](Br)[C@@H](C)Cl', '(2S,3R)', (16, 2.8))]
for s, t, (x, y) in S4: pasang(ax, rd(s, w=420, h=300, bl=48, fs=26), x - 3.5, x + 3.5, y - 2.3, y + 2.3, zorder=2); T(ax, x, y - 2.7, t, fs=9.5, fontweight='bold')
for (x1, y1), (x2, y2), lab, c in [((7.8, 10.2), (12.2, 10.2), 'enansiomer', HJ), ((7.8, 2.8), (12.2, 2.8), 'enansiomer', HJ), ((4, 7.2), (4, 5.6), 'diastereomer', JT), ((16, 7.2), (16, 5.6), 'diastereomer', JT), ((7.5, 7.4), (12.5, 5.4), 'diastereomer', JT)]:
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='<|-|>', mutation_scale=9, color=c, lw=1.2))
    ax.text((x1 + x2) / 2 + (1.6 if x1 == x2 else 1.2), (y1 + y2) / 2 + (0 if x1 == x2 else 0.9), lab, ha='center', fontsize=8, color=c)
ax.text(10, 12.6, 'dua pusat kiral → 2² = 4 stereoisomer', ha='center', fontsize=9.5, color=TUA, fontweight='bold')
simpan(f, 'empat')

# 10. dimetilsikloheksana
D = [('C[C@@H]1CCCC[C@@H]1C', 'cis-1,2: meso'), ('C[C@@H]1CCCC[C@H]1C', 'trans-1,2: kiral (sepasang enansiomer)'), ('C[C@@H]1CCC[C@H](C)C1', 'cis-1,3: meso'),
     ('C[C@@H]1CCC[C@@H](C)C1', 'trans-1,3: kiral (sepasang enansiomer)'), ('C[C@H]1CC[C@@H](C)CC1', 'cis-1,4: akiral'), ('C[C@H]1CC[C@H](C)CC1', 'trans-1,4: akiral')]
f, ax = plt.subplots(2, 3, figsize=(7.4, 4.0), dpi=220)
for a, (s, t) in zip(ax.flat, D): a.imshow(rd(s, w=420, h=320, bl=40, fs=24)); a.axis('off'); a.set_title(t, fontsize=8.3, color=TUA, y=-0.16)
plt.tight_layout(); simpan(f, 'dimetil')

# 11. alena kiral
f, ax = plt.subplots(figsize=(6.6, 2.6), dpi=220); ax.set_xlim(0, 24); ax.set_ylim(0, 9); ax.set_aspect('equal'); ax.axis('off')
for cx, flip in [(6, 1), (18, -1)]:
    c1, c2, c3 = np.array([cx - 2, 4.5]), np.array([cx, 4.5]), np.array([cx + 2, 4.5])
    ax.plot(*zip(c1, c2), color=TUA, lw=2); ax.plot(*zip(c1 + [0, 0.3], c2 + [0, 0.3]), color=TUA, lw=2)
    ax.plot(*zip(c2, c3), color=TUA, lw=2); ax.plot(*zip(c2 + [0, -0.3], c3 + [0, -0.3]), color=TUA, lw=2)
    for p in (c1, c2, c3): ax.plot(*p, 'o', color=TUA, ms=4)
    ax.plot([c1[0], c1[0] - 1.3], [4.5, 6.3], color=TUA, lw=1.6); ax.text(c1[0] - 1.6, 6.7, 'Cl' if flip > 0 else 'H', color=HJ if flip > 0 else TUA, fontsize=10, ha='center', fontweight='bold')
    ax.plot([c1[0], c1[0] - 1.3], [4.5, 2.7], color=TUA, lw=1.6); ax.text(c1[0] - 1.6, 2.2, 'H' if flip > 0 else 'Cl', color=TUA if flip > 0 else HJ, fontsize=10, ha='center', fontweight='bold')
    ax.fill([c3[0], c3[0] + 1.6, c3[0] + 1.4], [4.5, 3.4, 3.1], color=TUA); ax.text(c3[0] + 1.9, 3.0, 'Cl', color=HJ, fontsize=10, ha='center', fontweight='bold')
    for t in np.linspace(0.15, 1, 5):
        p = c3 + np.array([1.5, 1.2]) * t; ax.plot([p[0] - 0.12 * t, p[0] + 0.12 * t], [p[1] + 0.12 * t, p[1] - 0.12 * t], color=TUA, lw=1)
    ax.text(c3[0] + 1.85, 6.0, 'H', color=TUA, fontsize=10, ha='center', fontweight='bold')
ax.plot([12, 12], [1.0, 8.0], color='#9aa5b1', lw=1, ls='--'); ax.text(12, 8.4, 'cermin', ha='center', fontsize=8.5, color='#777777')
ax.text(12, 0.3, 'ClCH=C=CHCl: kedua ujung saling tegak lurus, sehingga molekul tidak dapat ditumpuk pada bayangannya', ha='center', fontsize=8, color=TUA)
simpan(f, 'alena')

# 12. E/Z
D = [('C/C=C\\C', '(Z)-but-2-ena\nprioritas tinggi sepihak'), ('C/C=C/C', '(E)-but-2-ena\nprioritas tinggi berseberangan'),
     ('Br/C(Cl)=C/C', '(E)-1-bromo-1-kloropropena\nBr > Cl; CH₃ > H'), ('CCCCCCCC/C=C\\CCCCCCCC(=O)O', 'asam oleat: (Z)')]
f, ax = plt.subplots(1, 4, figsize=(7.6, 2.3), dpi=220)
for a, (s, t) in zip(ax, D): a.imshow(rd(s, w=440, h=320, bl=60 if 'CCCCCCCC' not in s else 30, fs=28 if 'CCCC' not in s else 24)); a.axis('off'); a.set_title(t, fontsize=8, color=TUA, y=-0.25)
plt.tight_layout(); simpan(f, 'EZ')

# 13. resolusi
f, ax = plt.subplots(figsize=(7.4, 3.0), dpi=220); ax.set_xlim(0, 30); ax.set_ylim(0, 12); ax.axis('off')
def kot(x, y, w, h, t, fc='#eef4fa', ec=TUA):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.1,rounding_size=0.3', fc=fc, ec=ec, lw=1)); ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=8.2, color=TUA)
def pan(a, b, t=''):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=10, color=TUA, lw=1.1))
    if t: ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + 0.45, t, ha='center', fontsize=7.6, color=JT)
kot(0.0, 4.6, 5.4, 2.6, 'asam rasemik:\n(R)-asam +\n(S)-asam')
pan((5.9, 5.9), (8.4, 5.9), ''); ax.text(7.15, 8.0, '+ (R)-amina', ha='center', fontsize=7.6, color=JT)
kot(8.7, 4.3, 6.2, 3.2, 'dua garam\ndiastereomer (R,R)\ndan (S,R): kelarutan\nberbeda', fc='#fdf1e6', ec=JT)
pan((15.1, 6.8), (17.6, 9.0), ''); ax.text(14.6, 9.2, 'kristalisasi', fontsize=7.6, color=JT); pan((15.0, 5.2), (17.6, 2.8))
kot(17.8, 8.0, 5.2, 2.4, 'garam (R,R)\nmengkristal'); kot(17.8, 1.6, 5.2, 2.4, 'garam (S,R)\ntetap larut')
pan((23.2, 9.2), (25.0, 9.2), 'H⁺'.replace('⁺', '$^+$')); pan((23.2, 2.8), (25.0, 2.8), 'H$^+$')
kot(25.2, 8.0, 4.5, 2.4, '(R)-asam\nmurni'); kot(25.2, 1.6, 4.5, 2.4, '(S)-asam\nmurni')
simpan(f, 'resolusi')

# 14. enansiomer dalam obat dan bau
D = [('CC1=CC[C@H](CC1=O)C(C)=C', '(R)-karvon:\nbau daun mint'), ('CC1=CC[C@@H](CC1=O)C(C)=C', '(S)-karvon:\nbau biji jintan'),
     ('C[C@H](C(=O)O)c1ccc(CC(C)C)cc1', '(S)-ibuprofen:\nenansiomer aktif'), ('N[C@@H](Cc1ccc(O)c(O)c1)C(=O)O', 'L-DOPA, (S):\nobat Parkinson')]
f, ax = plt.subplots(1, 4, figsize=(7.6, 2.3), dpi=220)
for a, (s, t) in zip(ax, D): a.imshow(rd(s, w=440, h=340, bl=32, fs=22)); a.axis('off'); a.set_title(t, fontsize=8.3, color=TUA, y=-0.25)
plt.tight_layout(); simpan(f, 'obat')
print('ok tambahan')

# ================= versi render WebGL (3D) =================
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3d'))
from r3d import render, spek_molekul, tampil, koord, atom_ikat, kamera_terbaik
TMP = os.path.join(F, '_r3d'); os.makedirs(TMP, exist_ok=True)
def bingkai(f, rect): a = f.add_axes(rect); a.axis('off'); return a
def satuan(v): v = np.asarray(v, float); return v / np.linalg.norm(v)
J = []; LAB = {}
# enansiomer butan-2-ol: (R) dan bayangan cerminnya (S) = koordinat x dicerminkan, kamera dicerminkan
m, P, atom, ik = koord('C[C@@H](O)CC')
c = 1; nb = {a.GetSymbol() + str(a.GetIdx()): a.GetIdx() for a in m.GetAtomWithIdx(c).GetNeighbors()}
h = [i for k, i in nb.items() if k[0] == 'H'][0]; o = 2; me = 0; et = 3
P = P - P[c]; vo, vh = satuan(P[o]), satuan(P[h])
# susun: O ke atas (+z), H ke belakang (+y, menjauhi kamera yang memandang dari -y)
z = vo; y = satuan(vh - vh.dot(z) * z); x = np.cross(y, z); P = P @ np.array([x, y, z]).T
cam = satuan([0.42, -1, 0.22])
for nm, sx in (('R', 1), ('S', -1)):
    Q = P * [sx, 1, 1]; at = [(e, Q[i]) for i, (e, _) in enumerate(atom)]
    lp = {'OH': Q[o], 'CH$_3$': Q[me], 'C$_2$H$_5$': Q[4], 'H': Q[h], '_c': Q[c]}
    LAB[nm] = list(lp)
    J.append((dict(spek_molekul(at, ik), w=980, h=640, zoom=2.5, camdir=list(cam * [sx, 1, 1]), up=[0, 0, 1], target=[0, 0, 0.1], labels=[list(map(float, v)) for v in lp.values()]), f'{TMP}/e_{nm}.png'))
# alena ClCH=C=CHCl: geometri dibangun manual (ujung kiri di bidang xz, ujung kanan di bidang xy)
c60, s60 = 0.5, np.sqrt(3) / 2; C1, C2, C3 = np.array([-1.31, 0, 0]), np.zeros(3), np.array([1.31, 0, 0])
P2 = np.array([C1, C2, C3, C1 + 1.75 * np.array([-c60, 0, s60]), C1 + 1.08 * np.array([-c60, 0, -s60]), C3 + 1.75 * np.array([c60, -s60, 0]), C3 + 1.08 * np.array([c60, s60, 0])])
el2 = ['C', 'C', 'C', 'Cl', 'H', 'Cl', 'H']; ik2 = [(0, 1, 2), (1, 2, 2), (0, 3), (0, 4), (2, 5), (2, 6)]
for nm, sx in (('a', 1), ('b', -1)):
    Q = P2 * [sx, 1, 1]; at = [(e, Q[i]) for i, e in enumerate(el2)]
    J.append((dict(spek_molekul(at, ik2, ganda={(0, 1): [0, 1, 0], (1, 2): [0, 0, 1]}), w=800, h=640, zoom=2.3, camdir=list(satuan([0.6 * sx, -1, 0.6])), target=[0, 0, 0.1], up=[0, 0, 1]), f'{TMP}/al_{nm}.png'))
# untuk ganda ikatan alena: tiap C=C memakai bidang p-nya sendiri; spek_molekul memakai satu arah 'ganda' — atur ulang
PR = render(J)

f = plt.figure(figsize=(7.0, 3.0), dpi=220)
for k, (nm, t) in enumerate([('R', '(R)-butan-2-ol'), ('S', '(S)-butan-2-ol')]):
    a = bingkai(f, [0.0 if k == 0 else 0.53, 0.12, 0.47, 0.88]); fn = f'{TMP}/e_{nm}.png'
    tampil(a, fn); pr = np.array(PR[fn]); pc = pr[-1]
    for l, q in zip(LAB[nm][:-1], pr[:-1]):
        d = satuan(q - pc); off = {'OH': 0, 'H': 85}.get(l, 165)
        if l == 'H': d = satuan(d + [0, -0.9])
        if l == 'OH': q = q + [(80 if nm == 'R' else -80), 0]
        a.text(*(q + d * off), l, ha='center', va='center', fontsize=10, color=TUA, fontweight='bold')
    f.text(0.235 if k == 0 else 0.765, 0.03, t, ha='center', fontsize=10, color=TUA)
f.add_artist(plt.Line2D([0.5, 0.5], [0.1, 0.95], color=BIRU, lw=1.6, ls=(0, (4, 3)))); f.text(0.5, 0.04, 'cermin', ha='center', fontsize=8.5, color=BIRU)
f.savefig(f'{F}/enansiomer.png', bbox_inches='tight'); plt.close(f)
f = plt.figure(figsize=(7.0, 2.6), dpi=220)
for k, nm in enumerate('ab'): a = bingkai(f, [0.0 if k == 0 else 0.53, 0.16, 0.47, 0.84]); tampil(a, f'{TMP}/al_{nm}.png')
f.add_artist(plt.Line2D([0.5, 0.5], [0.16, 0.98], color='#9aa5b1', lw=1, ls='--')); f.text(0.5, 1.0, 'cermin', ha='center', fontsize=8.5, color='#777777')
f.text(0.5, 0.03, 'ClCH=C=CHCl: kedua ujung saling tegak lurus (Cl hijau, H putih), sehingga molekul tidak dapat ditumpuk pada bayangannya', ha='center', fontsize=8, color=TUA)
f.savefig(f'{F}/alena.png', bbox_inches='tight'); plt.close(f)
print('ok webgl')
