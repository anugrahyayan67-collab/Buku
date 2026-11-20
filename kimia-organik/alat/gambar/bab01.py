# Gambar Bab 1: rumus garis, hibridisasi, resonansi asetat
import os, io, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab01/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'

# 1. rumus garis
def gbr(smi, w=520, h=300):
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions()
    o.bondLineWidth = 3; o.fixedFontSize = 30; o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74)})
    o.clearBackground = True; o.padding = 0.12
    rdMolDraw2D.PrepareAndDrawMolecule(d, Chem.MolFromSmiles(smi)); d.FinishDrawing()
    return Image.open(io.BytesIO(d.GetDrawingText()))
mol = [('CCCCCCO', 'heksan-1-ol'), ('CC(=O)OCCC(C)C', 'isopentil asetat'), ('C1=CCCCC1', 'sikloheksena')]
f, ax = plt.subplots(1, 3, figsize=(7.6, 2.2), dpi=220)
for a, (s, n) in zip(ax, mol):
    a.imshow(gbr(s)); a.axis('off'); a.set_title(n, fontsize=10, color=TUA, y=-0.12)
plt.tight_layout(); f.savefig(f'{F}/garis.png', bbox_inches='tight'); plt.close(f)

# 2. hibridisasi
def cuping(ax, ang, L=1.0, c=BIRU, a=0.55, kecil=True):
    x, y = np.cos(np.radians(ang)), np.sin(np.radians(ang))
    ax.add_patch(Ellipse((0.5 * L * x, 0.5 * L * y), L, 0.42 * L, angle=ang, fc=c, ec=TUA, lw=0.8, alpha=a))
    if kecil: ax.add_patch(Ellipse((-0.12 * x, -0.12 * y), 0.24, 0.16, angle=ang, fc=c, ec=TUA, lw=0.6, alpha=a * 0.7))
def p_orb(ax, ang, c=JG):
    for s in (1, -1):
        x, y = s * np.cos(np.radians(ang)), s * np.sin(np.radians(ang))
        ax.add_patch(Ellipse((0.42 * x, 0.42 * y), 0.8, 0.34, angle=ang, fc=c, ec=JT, lw=0.8, alpha=0.6))
f, ax = plt.subplots(1, 3, figsize=(7.6, 2.8), dpi=220)
for a in ax: a.set_xlim(-1.3, 1.3); a.set_ylim(-1.25, 1.25); a.set_aspect('equal'); a.axis('off')
# sp3: proyeksi tetrahedron
for ang, al in [(90, .65), (210, .65), (330, .65), (270, .3)]: cuping(ax[0], ang, 1.0 if al > .5 else 0.75, a=al)
ax[0].text(0.08, -0.62, '109,5°', fontsize=9, color=TUA); ax[0].set_title('sp³ · tetrahedral', color=TUA, fontsize=10, y=-0.08)
# sp2
p_orb(ax[1], 90)
for ang in (0, 120, 240): cuping(ax[1], ang)
ax[1].text(0.25, 0.32, '120°', fontsize=9, color=TUA); ax[1].text(0.08, 1.05, 'p', color=JT, fontsize=10, style='italic')
ax[1].set_title('sp² · segitiga datar', color=TUA, fontsize=10, y=-0.08)
# sp
p_orb(ax[2], 90); p_orb(ax[2], 35)
for ang in (0, 180): cuping(ax[2], ang)
ax[2].text(-0.2, -0.32, '180°', fontsize=9, color=TUA)
ax[2].set_title('sp · linear', color=TUA, fontsize=10, y=-0.08)
for a in ax: a.plot(0, 0, 'o', color=TUA, ms=5, zorder=5)
plt.tight_layout(); f.savefig(f'{F}/hibrid.png', bbox_inches='tight'); plt.close(f)

# 3. resonansi asetat (digambar manual)
f, ax = plt.subplots(figsize=(7.6, 2.2), dpi=220); ax.set_xlim(-0.4, 17.4); ax.set_ylim(0, 4.8); ax.axis('off'); ax.set_aspect('equal')
def asetat(x0, rangkap_atas, panah=False):
    C = (x0 + 1.6, 2.2); Me = (x0 + 0.2, 2.2); Oa = (x0 + 2.4, 3.5); Ob = (x0 + 2.4, 0.9)
    ax.plot(*zip(Me, C), color=TUA, lw=2); ax.text(Me[0] - 0.15, Me[1], 'H₃C', ha='right', va='center', fontsize=12, color=TUA)
    for O, r in [(Oa, rangkap_atas), (Ob, not rangkap_atas)]:
        v = np.array(O) - np.array(C); v /= np.linalg.norm(v); n = np.array([-v[1], v[0]])
        p0, p1 = np.array(C) + 0.15 * v, np.array(O) - 0.28 * v
        ax.plot(*zip(p0, p1), color=TUA, lw=2)
        if r: ax.plot(*zip(p0 + 0.13 * n, p1 + 0.13 * n), color=TUA, lw=2)
        ax.text(*O, 'O', ha='center', va='center', fontsize=13, color=JT, fontweight='bold')
        if not r: ax.text(O[0] + 0.42, O[1] + (0.3 if O[1] > 2 else -0.3), '−', fontsize=14, color=JT, ha='center', va='center')
    if panah:
        ax.add_patch(FancyArrowPatch((Ob[0] + 0.35, Ob[1] - 0.05), (C[0] + 0.55, (C[1] + Ob[1]) / 2 - 0.05), connectionstyle='arc3,rad=0.6', arrowstyle='-|>', mutation_scale=11, color=BIRU, lw=1.3))
        ax.add_patch(FancyArrowPatch((C[0] + 0.25, (C[1] + Oa[1]) / 2 + 0.1), (Oa[0] + 0.35, Oa[1] + 0.2), connectionstyle='arc3,rad=-0.6', arrowstyle='-|>', mutation_scale=11, color=BIRU, lw=1.3))
asetat(1.0, True, panah=True)
ax.text(5.15, 2.2, '↔', fontsize=20, ha='center', va='center', color=TUA)
asetat(6.9, False)
ax.text(10.95, 2.2, '≡', fontsize=18, ha='center', va='center', color=TUA)
# hibrida
x0 = 12.7; C = (x0 + 1.6, 2.2); Me = (x0 + 0.2, 2.2)
ax.plot(*zip(Me, C), color=TUA, lw=2); ax.text(Me[0] - 0.15, Me[1], 'H₃C', ha='right', va='center', fontsize=12, color=TUA)
for O in [(x0 + 2.4, 3.5), (x0 + 2.4, 0.9)]:
    v = np.array(O) - np.array(C); v /= np.linalg.norm(v); n = np.array([-v[1], v[0]])
    p0, p1 = np.array(C) + 0.15 * v, np.array(O) - 0.28 * v
    ax.plot(*zip(p0, p1), color=TUA, lw=2); ax.plot(*zip(p0 + 0.13 * n, p1 + 0.13 * n), color=TUA, lw=1.6, ls=(0, (2, 1.5)))
    ax.text(*O, 'O', ha='center', va='center', fontsize=13, color=JT, fontweight='bold')
    ax.text(O[0] + 0.5, O[1] + (0.3 if O[1] > 2 else -0.3), 'δ−', fontsize=11, color=JT, ha='center', va='center')
for x, t in [(2.6, 'penyumbang 1'), (8.5, 'penyumbang 2'), (14.3, 'hibrida resonansi')]: ax.text(x, 0.05, t, ha='center', fontsize=9, color=HJ)
f.savefig(f'{F}/resonansi.png', bbox_inches='tight'); plt.close(f)
print('ok')

# 4. diagram orbital molekul H2 dan pi etena
f, axs = plt.subplots(1, 2, figsize=(7.4, 3.0), dpi=220)
def dia(ax, kiri, kanan, ik, ak, judul, nel, lab=('σ', 'σ*')):
    ax.set_xlim(0, 10); ax.set_ylim(-3.2, 3.4); ax.axis('off')
    for x, t in [(1.5, kiri), (8.5, kanan)]:
        ax.plot([x - 0.7, x + 0.7], [0, 0], color=TUA, lw=2); ax.text(x, -0.55, t, ha='center', fontsize=9, color=TUA)
        ax.annotate('', (x, 0.35), (x, -0.05), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.3))
    for y, t, c in [(-2.0, lab[0], BIRU), (2.0, lab[1], JT)]:
        ax.plot([4.3, 5.7], [y, y], color=c, lw=2.4); ax.text(6.0, y, t + ('  (' + ik + ')' if y < 0 else '  (' + ak + ')'), va='center', fontsize=9, color=c)
        for x0 in (1.5, 8.5): ax.plot([x0 + (0.7 if x0 < 5 else -0.7), 4.3 if x0 < 5 else 5.7], [0, y], color=AB if False else '#9aa5b1', lw=0.8, ls=(0, (2, 2)))
    for dx, up in [(-0.18, True), (0.18, False)]:
        ax.annotate('', (5 + dx, -2.0 + (0.42 if up else -0.02)), (5 + dx, -2.0 + (0.02 if up else 0.42)), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.3))
    ax.text(5, 3.15, judul, ha='center', fontsize=10, color=TUA, fontweight='bold')
dia(axs[0], '1s (H)', '1s (H)', 'ikatan', 'antiikatan', 'H₂', 2)
dia(axs[1], '2p (C)', '2p (C)', 'HOMO', 'LUMO', 'π etena', 2, ('π', 'π*'))
plt.tight_layout(); f.savefig(f'{F}/om.png', bbox_inches='tight'); plt.close(f)
print('ok om')
