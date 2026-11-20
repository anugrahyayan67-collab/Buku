# Gambar Bab 5: peta isomer, enansiomer butan-2-ol, asam tartarat, Fischer
import os, io, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
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
    o.bondLineWidth = 3; o.fixedFontSize = fs; o.addStereoAnnotation = True; o.padding = 0.15
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 35: (0.55, 0.2, 0.1)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))

# 2. enansiomer butan-2-ol
f, ax = plt.subplots(1, 3, figsize=(7.0, 2.6), dpi=220, gridspec_kw={'width_ratios': [1, 0.12, 1]})
for a in ax: a.axis('off')
ax[0].imshow(rd('C[C@@H](O)CC')); ax[2].imshow(rd('C[C@H](O)CC'))
ax[1].axvline(0.5, color=BIRU, lw=2, ls=(0, (4, 3))); ax[1].set_xlim(0, 1); ax[1].text(0.5, 0.02, 'cermin', ha='center', fontsize=8, color=BIRU, transform=ax[1].transAxes)
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
