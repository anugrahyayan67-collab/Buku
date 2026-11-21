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
    o.clearBackground = True; o.padding = 0.12; o.fixedBondLength = 45
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

# ================= gambar tambahan =================
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lewis import molekul, lengkung, resonansi, panah, MERAH
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle, Arc
import matplotlib.ticker
koma = lambda v: f'{v:g}'.replace('.', ',').replace('-', '−')
fmt = matplotlib.ticker.FuncFormatter(lambda q, _: koma(round(q, 3)))
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def T(ax, x, y, s, c=TUA, fs=10, **k): ax.text(x, y, s, ha=k.pop('ha', 'center'), va=k.pop('va', 'center'), color=c, fontsize=fs, **k)
def simpan(f, n): f.savefig(f'{F}/{n}.png', bbox_inches='tight'); plt.close(f)

# 5. orbital atom karbon
f, ax = kanv(7.4, 2.9, (0, 26), (0, 10))
for y, lab, n in [(1.2, '1s', 1), (3.6, '2s', 1), (6.0, '2p', 3)]:
    for i in range(n):
        x = 2.2 + i * 1.5; ax.add_patch(Rectangle((x, y), 1.2, 1.0, fc='white', ec=TUA, lw=1.2))
    T(ax, 1.4, y + 0.5, lab, fs=10)
for x, y, s in [(2.8, 1.2, 'ud'), (2.8, 3.6, 'ud'), (2.8, 6.0, 'u'), (4.3, 6.0, 'u')]:
    if 'u' in s: ax.annotate('', (x - 0.2, y + 0.9), (x - 0.2, y + 0.1), arrowprops=dict(arrowstyle='-|>', color=BIRU, lw=1.4))
    if 'd' in s: ax.annotate('', (x + 0.2, y + 0.1), (x + 0.2, y + 0.9), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.4))
ax.annotate('', (0.6, 8.0), (0.6, 0.8), arrowprops=dict(arrowstyle='-|>', color='#888888', lw=1)); T(ax, 0.6, 8.6, 'energi', fs=8, c='#777777')
T(ax, 5.2, 9.4, 'karbon: 1s² 2s² 2p²', fs=9.5, fontweight='bold')
T(ax, 4.0, 9.4, '', fs=1)
# bentuk orbital
def lobe(ax, cx, cy, ang, c, L=1.5):
    for sg, cc in [(1, c), (-1, c)]:
        x, y = cx + sg * 0.75 * np.cos(np.radians(ang)) * L / 1.5, cy + sg * 0.75 * np.sin(np.radians(ang)) * L / 1.5
        ax.add_patch(Ellipse((x, y), L, 0.75 * L / 1.5, angle=ang, fc=cc, ec=TUA, lw=0.8, alpha=0.65 if sg > 0 else 0.35))
cx = 11.0; ax.add_patch(Circle((cx, 4.6), 1.3, fc=MUDA, ec=TUA, lw=0.8, alpha=0.7)); ax.plot(cx, 4.6, 'o', color=TUA, ms=2.5); T(ax, cx, 2.4, 'orbital s', fs=9)
for i, (ang, nm) in enumerate([(0, '$p_x$'), (90, '$p_y$'), (35, '$p_z$')]):
    x0 = 15.6 + i * 3.6; ax.plot([x0 - 1.6, x0 + 1.6], [4.6, 4.6], color='#cccccc', lw=0.6); ax.plot([x0, x0], [3.0, 6.2], color='#cccccc', lw=0.6)
    lobe(ax, x0, 4.6, ang, JG); ax.plot(x0, 4.6, 'o', color=TUA, ms=2.5); T(ax, x0, 2.4, nm, fs=10)
T(ax, 19.2, 8.6, 'tiga orbital p, saling tegak lurus', fs=9)
simpan(f, 'orbital')

# 6. struktur Lewis metanol dan metanal
f, ax = kanv(7.0, 2.6, (0, 24), (0, 8.4))
molekul(ax, {'C': (0, 0, 'C'), 'O': (1.3, 0, 'O'), 'H1': (-1.1, 0, 'H'), 'H2': (0, 1.1, 'H'), 'H3': (0, -1.1, 'H'), 'H4': (2.4, 0, 'H')},
        [('C', 'O', 1), ('C', 'H1', 1), ('C', 'H2', 1), ('C', 'H3', 1), ('O', 'H4', 1)], lp={'O': [90, 270]}, ox=4.2, oy=4.4, s=1.6)
T(ax, 5.8, 0.8, 'metanol, CH₃OH\n14 e valensi: 5 ikatan + 2 pb', fs=8.5)
molekul(ax, {'C': (0, 0, 'C'), 'O': (1.3, 0, 'O'), 'H1': (-0.8, 0.8, 'H'), 'H2': (-0.8, -0.8, 'H')},
        [('C', 'O', 2), ('C', 'H1', 1), ('C', 'H2', 1)], lp={'O': [45, -45]}, ox=16.5, oy=4.4, s=1.6)
T(ax, 17.6, 0.8, 'metanal, H₂C=O\n12 e valensi: 4 ikatan + 2 pb', fs=8.5)
simpan(f, 'lewis')

# 7. muatan formal: pola C, N, O
f, ax = kanv(7.4, 5.4, (0, 27), (0, 20))
for j, t in enumerate(['muatan +1', 'netral', 'muatan −1']): T(ax, 9 + j * 7, 19.4, t, fs=9.5, fontweight='bold', c=[MERAH, TUA, BIRU][j])
rows = [('karbon', [({'X': (0, 0, 'C'), 'a': (-1, 0, 'H'), 'b': (0.5, 0.87, 'H'), 'c': (0.5, -0.87, 'H')}, [('X', 'a', 1), ('X', 'b', 1), ('X', 'c', 1)], {}, {'X': ('+', 0)}, 'karbokation\n3 ikatan, 0 pb'),
                     ({'X': (0, 0, 'C'), 'a': (-1, 0, 'H'), 'b': (1, 0, 'H'), 'c': (0, 1, 'H'), 'd': (0, -1, 'H')}, [('X', 'a', 1), ('X', 'b', 1), ('X', 'c', 1), ('X', 'd', 1)], {}, {}, '4 ikatan, 0 pb'),
                     ({'X': (0, 0, 'C'), 'a': (-1, 0, 'H'), 'b': (0.5, 0.87, 'H'), 'c': (0.5, -0.87, 'H')}, [('X', 'a', 1), ('X', 'b', 1), ('X', 'c', 1)], {'X': [0]}, {'X': ('-', 120)}, 'karbanion\n3 ikatan, 1 pb')]),
        ('nitrogen', [({'X': (0, 0, 'N'), 'a': (-1, 0, 'H'), 'b': (1, 0, 'H'), 'c': (0, 1, 'H'), 'd': (0, -1, 'H')}, [('X', 'a', 1), ('X', 'b', 1), ('X', 'c', 1), ('X', 'd', 1)], {}, {'X': ('+', 45)}, 'ion amonium\n4 ikatan, 0 pb'),
                      ({'X': (0, 0, 'N'), 'a': (-1, 0, 'H'), 'b': (0.5, 0.87, 'H'), 'c': (0.5, -0.87, 'H')}, [('X', 'a', 1), ('X', 'b', 1), ('X', 'c', 1)], {'X': [0]}, {}, '3 ikatan, 1 pb'),
                      ({'X': (0, 0, 'N'), 'a': (-1, 0, 'H'), 'b': (0.5, 0.87, 'H')}, [('X', 'a', 1), ('X', 'b', 1)], {'X': [0, 240]}, {'X': ('-', 305)}, 'ion amida\n2 ikatan, 2 pb')]),
        ('oksigen', [({'X': (0, 0, 'O'), 'a': (-1, 0, 'H'), 'b': (0.5, 0.87, 'H'), 'c': (0.5, -0.87, 'H')}, [('X', 'a', 1), ('X', 'b', 1), ('X', 'c', 1)], {'X': [0]}, {'X': ('+', 120)}, 'ion hidronium\n3 ikatan, 1 pb'),
                     ({'X': (0, 0, 'O'), 'a': (-1, 0, 'H'), 'b': (0.5, 0.87, 'H')}, [('X', 'a', 1), ('X', 'b', 1)], {'X': [0, 240]}, {}, '2 ikatan, 2 pb'),
                     ({'X': (0, 0, 'O'), 'a': (-1, 0, 'H')}, [('X', 'a', 1)], {'X': [0, 90, 270]}, {'X': ('-', 45)}, 'ion hidroksida\n1 ikatan, 3 pb')])]
for i, (nm, items) in enumerate(rows):
    y = 15.2 - i * 6.0; T(ax, 1.6, y, nm, fs=9.5, fontweight='bold')
    for j, (at, ik, lp, mu, cap) in enumerate(items):
        molekul(ax, at, ik, lp=lp, muatan=mu, ox=9 + j * 7, oy=y + 0.5, s=1.7, fs=12); T(ax, 9 + j * 7, y - 2.4, cap, fs=7.6, c='#444444')
simpan(f, 'muatan')

# 8. baji dan garis putus-putus
f, ax = kanv(7.0, 2.4, (0, 24), (0, 8))
molekul(ax, {'C': (0, 0, 'C'), 'a': (0, 1.2, 'H'), 'b': (-1.05, -0.6, 'H'), 'c': (1.05, -0.45, 'H'), 'd': (0.3, -1.15, 'H')},
        [('C', 'a', 1), ('C', 'b', 1), ('C', 'c', 'w'), ('C', 'd', 'h')], ox=4, oy=4.4, s=1.7)
T(ax, 4, 0.9, 'metana', fs=9)
molekul(ax, {'C': (0, 0, 'C'), 'a': (0, 1.2, 'Br'), 'b': (-1.05, -0.6, 'H'), 'c': (1.05, -0.45, 'Cl'), 'd': (0.3, -1.15, 'F')},
        [('C', 'a', 1), ('C', 'b', 1), ('C', 'c', 'w'), ('C', 'd', 'h')], ox=12, oy=4.4, s=1.7)
T(ax, 12, 0.9, 'bromoklorofluorometana', fs=9)
for y, t, sty in [(6.4, 'garis biasa: di bidang kertas', 1), (4.4, 'baji: mendekati pembaca', 'w'), (2.4, 'garis putus-putus: menjauhi pembaca', 'h')]:
    molekul(ax, {'a': (0, 0, ''), 'b': (1.4, 0, '')}, [('a', 'b', sty)], ox=17.0, oy=y, s=1.0); T(ax, 18.8, y, t, fs=8.3, ha='left')
simpan(f, 'baji')

# 9. VSEPR
f, ax = kanv(7.4, 2.8, (0, 27), (0, 10))
def pb_lobe(ax, x, y, ang, s=1.0):
    u = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    ax.add_patch(Ellipse((x + u[0] * 0.75 * s, y + u[1] * 0.75 * s), 1.1 * s, 0.6 * s, angle=ang, fc=JG, ec=JT, lw=0.8, alpha=0.5))
    for f_ in (-0.12, 0.12): ax.add_patch(Circle((x + u[0] * 0.8 * s - u[1] * f_ * s, y + u[1] * 0.8 * s + u[0] * f_ * s), 0.05 * s, color=TUA, zorder=5))
dat = [('C', 'metana', 0, '109,5°'), ('N', 'amonia', 1, '107°'), ('O', 'air', 2, '104,5°')]
for i, (el, nm, npb, ang) in enumerate(dat):
    cx = 4.5 + i * 9.0; cy = 5.2; at = {'X': (0, 0, el)}; ik = []
    pos = [(0, 1.3), (-1.15, -0.5), (1.0, -0.25), (0.45, -1.05)]
    sty = [1, 1, 'w', 'h']
    for k in range(4 - npb):
        idx = [3, 2, 1, 0][k] if npb else k; at[f'h{k}'] = (pos[idx][0], pos[idx][1], 'H'); ik.append(('X', f'h{k}', sty[idx]))
    molekul(ax, at, ik, ox=cx, oy=cy, s=1.6)
    for k in range(npb):
        p = pos[[0, 1][k]]; pb_lobe(ax, cx, cy, np.degrees(np.arctan2(p[1], p[0])), s=1.4)
    T(ax, cx, 1.4, f'{nm}\n{4 - npb} ikatan, {npb} pasangan bebas', fs=8.3); T(ax, cx + 2.2, 7.6, ang, fs=9, c=BIRU, fontweight='bold')
simpan(f, 'vsepr')

# 10. ikatan sigma dan pi
f, ax = kanv(7.4, 2.6, (0, 30), (0, 10))
def sorb(ax, x, y, r=0.75, c=MUDA): ax.add_patch(Circle((x, y), r, fc=c, ec=TUA, lw=0.8, alpha=0.65))
def hyb(ax, x, y, ang, c=BIRU, L=1.6):
    u = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    ax.add_patch(Ellipse((x + u[0] * L * 0.45, y + u[1] * L * 0.45), L, 0.75, angle=ang, fc=c, ec=TUA, lw=0.8, alpha=0.6))
    ax.add_patch(Ellipse((x - u[0] * 0.25, y - u[1] * 0.25), 0.4, 0.3, angle=ang, fc=c, ec=TUA, lw=0.6, alpha=0.4))
sorb(ax, 2.2, 5.5); sorb(ax, 3.4, 5.5); T(ax, 2.8, 2.6, 's + s\n(H–H)', fs=8.5)
hyb(ax, 8.0, 5.5, 0); sorb(ax, 10.0, 5.5, 0.65); T(ax, 9.0, 2.6, 'sp³ + s\n(C–H)', fs=8.5)
hyb(ax, 14.2, 5.5, 0); hyb(ax, 17.0, 5.5, 180); T(ax, 15.6, 2.6, 'sp³ + sp³\n(C–C)', fs=8.5)
for x in (23.0, 25.4):
    for sg in (1, -1): ax.add_patch(Ellipse((x, 5.5 + sg * 1.0), 0.8, 1.7, fc=JG, ec=JT, lw=0.8, alpha=0.6))
    ax.plot(x, 5.5, 'o', color=TUA, ms=3)
ax.plot([23.0, 25.4], [5.5, 5.5], color=TUA, lw=1.2)
for sg in (1, -1): ax.add_patch(Ellipse((24.2, 5.5 + sg * 1.05), 3.4, 1.0, fc='none', ec=JT, lw=1.0, ls='--'))
T(ax, 24.2, 2.6, 'p + p sisi ke sisi\n(ikatan π)', fs=8.5)
T(ax, 9.3, 9.0, 'ikatan σ: tumpang tindih ujung ke ujung', fs=8.8, c=BIRU, fontweight='bold')
T(ax, 24.2, 9.0, 'ikatan π: sisi ke sisi', fs=8.8, c=JT, fontweight='bold')
ax.plot([20.3, 20.3], [1.5, 9.5], color='#cccccc', lw=0.8)
simpan(f, 'sigmapi')

# 11. rotasi ikatan rangkap
f, ax = kanv(7.0, 2.6, (0, 26), (0, 10))
def pp(ax, x, y, ang_deg, c=JG):
    if ang_deg == 0:
        for sg in (1, -1): ax.add_patch(Ellipse((x, y + sg * 1.0), 0.8, 1.7, fc=c, ec=JT, lw=0.8, alpha=0.6))
    else:
        for sg in (1, -1): ax.add_patch(Ellipse((x + sg * 0.55, y + sg * 0.25), 1.3, 0.55, fc=c, ec=JT, lw=0.8, alpha=0.6))
for x0, tw, t in [(4.5, False, 'kedua orbital p sejajar:\ntumpang tindih, ikatan π ada'), (17.5, True, 'satu karbon diputar 90°:\ntumpang tindih nol, ikatan π putus')]:
    ax.plot([x0, x0 + 3.0], [5.6, 5.6], color=TUA, lw=1.6); ax.plot(x0, 5.6, 'o', color=TUA, ms=4); ax.plot(x0 + 3, 5.6, 'o', color=TUA, ms=4)
    for dx, dy in [(-1.1, 0.8), (-1.1, -0.8)]: ax.plot([x0, x0 + dx], [5.6, 5.6 + dy], color=TUA, lw=1.2)
    if not tw:
        for dx, dy in [(1.1, 0.8), (1.1, -0.8)]: ax.plot([x0 + 3, x0 + 3 + dx], [5.6, 5.6 + dy], color=TUA, lw=1.2)
    else:
        ax.plot([x0 + 3, x0 + 4.1], [5.6, 5.6], color=TUA, lw=1.2); ax.plot([x0 + 3, x0 + 2.6], [5.6, 4.9], color=TUA, lw=1.2)
    pp(ax, x0, 5.6, 0); pp(ax, x0 + 3, 5.6, 90 if tw else 0)
    T(ax, x0 + 1.5, 1.6, t, fs=8.5)
panah(ax, (11.0, 5.6), (14.6, 5.6)); T(ax, 12.8, 6.6, '≈ 260 kJ mol$^{-1}$', fs=8.8, c=MERAH)
simpan(f, 'rotasi')

# 12. momen dipol
f, ax = kanv(7.4, 2.8, (0, 30), (0, 10.5))
def vek(ax, a, b, c=MERAH):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=10, color=c, lw=1.6, zorder=6))
    d = np.array(b) - np.array(a); u = d / np.hypot(*d); n = np.array([-u[1], u[0]]); p = np.array(a) + u * 0.25
    ax.plot([p[0] - n[0] * 0.18, p[0] + n[0] * 0.18], [p[1] - n[1] * 0.18, p[1] + n[1] * 0.18], color=c, lw=1.6, zorder=6)
molekul(ax, {'C': (0, 0, 'C'), 'a': (-1.2, 0, 'O'), 'b': (1.2, 0, 'O')}, [('C', 'a', 2), ('C', 'b', 2)], lp={'a': [135, 225], 'b': [45, -45]}, ox=3.5, oy=6.0, s=1.3)
vek(ax, (3.3, 7.0), (1.9, 7.0)); vek(ax, (3.7, 7.0), (5.1, 7.0)); T(ax, 3.5, 2.4, 'CO₂\nμ = 0 D', fs=9)
molekul(ax, {'O': (0, 0, 'O'), 'a': (-0.8, -0.65, 'H'), 'b': (0.8, -0.65, 'H')}, [('O', 'a', 1), ('O', 'b', 1)], lp={'O': [60, 120]}, ox=10.5, oy=6.4, s=1.5)
vek(ax, (10.5, 4.6), (10.5, 3.6 + 2.0 + 0.0)) if False else vek(ax, (10.5, 4.3), (10.5, 5.6)); T(ax, 10.5, 2.4, 'H₂O\nμ = 1,85 D', fs=9)
molekul(ax, {'C': (0, 0, 'C'), 'Cl': (0, 1.2, 'Cl'), 'a': (-1.05, -0.6, 'H'), 'b': (1.05, -0.45, 'H'), 'c': (0.3, -1.15, 'H')},
        [('C', 'Cl', 1), ('C', 'a', 1), ('C', 'b', 'w'), ('C', 'c', 'h')], ox=17.5, oy=5.6, s=1.4)
vek(ax, (18.6, 5.2), (18.6, 7.4)); T(ax, 17.5, 2.4, 'CH₃Cl\nμ = 1,87 D', fs=9)
molekul(ax, {'C': (0, 0, 'C'), 'a': (0, 1.2, 'Cl'), 'b': (-1.05, -0.6, 'Cl'), 'c': (1.05, -0.45, 'Cl'), 'd': (0.3, -1.15, 'Cl')},
        [('C', 'a', 1), ('C', 'b', 1), ('C', 'c', 'w'), ('C', 'd', 'h')], ox=25.5, oy=5.6, s=1.4)
T(ax, 25.5, 2.4, 'CCl₄\nμ = 0 D (vektor saling meniadakan)', fs=9)
T(ax, 15, 10.0, 'panah ┼→ menunjuk dari ujung δ+ ke ujung δ−', fs=8.5, c=MERAH)
simpan(f, 'dipol')

# 13. lima pola resonansi
f, ax = kanv(7.4, 10.5, (0, 30), (-5, 38))
S2 = 1.9
def baris(y, nomor, judul): T(ax, 0.3, y + 3.0, f'{nomor}. {judul}', fs=9.5, ha='left', fontweight='bold', c=BIRU)
def at_(d): return d
# pola 1: enolat
y = 31.0; baris(y, 1, 'pasangan bebas di samping ikatan π')
A = molekul(ax, {'a': (0, 0, ''), 'b': (1.3, 0.75, ''), 'O': (2.6, 0, 'O')}, [('a', 'b', 2), ('b', 'O', 1)], lp={'O': [-40, -140, 90]}, muatan={'O': ('-', 15)}, ox=2.5, oy=y, s=S2)
lengkung(ax, A['O'] + np.array([-0.15, 0.75]), (A['b'] + A['O']) / 2 + np.array([0.0, 0.45]), rad=0.6)
lengkung(ax, (A['a'] + A['b']) / 2 + np.array([0.1, 0.35]), A['a'] + np.array([-0.3, 0.6]), rad=0.5)
resonansi(ax, 13.0, y + 0.7, w=1.8)
molekul(ax, {'a': (0, 0, ''), 'b': (1.3, 0.75, ''), 'O': (2.6, 0, 'O')}, [('a', 'b', 1), ('b', 'O', 2)], lp={'O': [-40, -140], 'a': [200]}, muatan={'a': ('-', 140)}, ox=16.0, oy=y, s=S2)
T(ax, 27.0, y + 0.7, 'ion enolat', fs=9, c='#555555')
# pola 2
y = 23.5; baris(y, 2, 'pasangan bebas di samping muatan positif')
A = molekul(ax, {'m': (0, 0, 'CH₃'), 'O': (1.5, 0, 'O'), 'c': (3.0, 0, 'CH₂')}, [('m', 'O', 1), ('O', 'c', 1)], lp={'O': [90, 270]}, muatan={'c': ('+', 50)}, ox=2.0, oy=y, s=S2)
lengkung(ax, A['O'] + np.array([0.1, 0.65]), (A['O'] + A['c']) / 2 + np.array([0.15, 0.15]), rad=-0.7)
resonansi(ax, 13.0, y, w=1.8)
molekul(ax, {'m': (0, 0, 'CH₃'), 'O': (1.5, 0, 'O'), 'c': (3.0, 0, 'CH₂')}, [('m', 'O', 1), ('O', 'c', 2)], lp={'O': [270]}, muatan={'O': ('+', 90)}, ox=15.5, oy=y, s=S2)
T(ax, 27.0, y, 'oktet lengkap\ndi semua atom', fs=9, c='#555555')
# pola 3
y = 15.5; baris(y, 3, 'ikatan π di samping muatan positif')
A = molekul(ax, {'a': (0, 0, ''), 'b': (1.3, 0.75, ''), 'c': (2.6, 0, '')}, [('a', 'b', 2), ('b', 'c', 1)], muatan={'c': ('+', -20)}, ox=2.5, oy=y, s=S2)
lengkung(ax, (A['a'] + A['b']) / 2 + np.array([0, 0.4]), (A['b'] + A['c']) / 2 + np.array([0.15, 0.4]), rad=-0.7)
resonansi(ax, 13.0, y + 0.7, w=1.8)
molekul(ax, {'a': (0, 0, ''), 'b': (1.3, 0.75, ''), 'c': (2.6, 0, '')}, [('a', 'b', 1), ('b', 'c', 2)], muatan={'a': ('+', 200)}, ox=16.0, oy=y, s=S2)
T(ax, 27.0, y + 0.7, 'kation alil', fs=9, c='#555555')
# pola 4
y = 7.5; baris(y, 4, 'ikatan π antara atom berbeda keelektronegatifan')
A = molekul(ax, {'C': (0, 0, 'C'), 'O': (1.5, 0, 'O'), 'a': (-0.9, 0.8, 'H'), 'b': (-0.9, -0.8, 'H')}, [('C', 'O', 2), ('C', 'a', 1), ('C', 'b', 1)], lp={'O': [50, -50]}, ox=4.0, oy=y, s=S2)
lengkung(ax, (A['C'] + A['O']) / 2 + np.array([0, 0.25]), A['O'] + np.array([-0.1, 0.65]), rad=-0.6)
resonansi(ax, 13.0, y, w=1.8)
molekul(ax, {'C': (0, 0, 'C'), 'O': (1.5, 0, 'O'), 'a': (-0.9, 0.8, 'H'), 'b': (-0.9, -0.8, 'H')}, [('C', 'O', 1), ('C', 'a', 1), ('C', 'b', 1)], lp={'O': [70, -70, 0]}, muatan={'C': ('+', 75), 'O': ('-', 120)}, ox=17.5, oy=y, s=S2)
T(ax, 27.0, y, 'karbon δ+:\nsasaran nukleofil', fs=9, c='#555555')
# pola 5
y = -1.5; baris(y, 5, 'ikatan π terkonjugasi dalam cincin')
def heks(ox, oy, r=1.5, dbl=(0, 2, 4)):
    at = {f'v{i}': (r * np.cos(np.radians(90 + 60 * i)), r * np.sin(np.radians(90 + 60 * i)), '') for i in range(6)}
    ik = [(f'v{i}', f'v{(i + 1) % 6}', 2 if i in dbl else 1) for i in range(6)]
    return molekul(ax, at, ik, ox=ox, oy=oy, s=1.0, lw=1.8)
A = heks(6.0, y)
for i in (0, 2, 4):
    p = (A[f'v{i}'] + A[f'v{(i + 1) % 6}']) / 2; q = (A[f'v{(i + 1) % 6}'] + A[f'v{(i + 2) % 6}']) / 2; c0 = np.array([6.0, y])
    lengkung(ax, c0 + (p - c0) * 0.72, c0 + (q - c0) * 0.72, rad=-0.45, ms=8)
resonansi(ax, 13.0, y, w=1.8)
heks(19.5, y, dbl=(1, 3, 5))
T(ax, 27.0, y, 'benzena', fs=9, c='#555555')
simpan(f, 'pola')

# 14. titik didih alkana dan alkohol
f, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
n = np.arange(1, 9)
alk = [-161.5, -88.6, -42.1, -0.5, 36.1, 68.7, 98.4, 125.6]
ol = [64.7, 78.4, 97.2, 117.7, 138.0, 157.0, 176.0, 195.0]
ax.plot(n, ol, 'o-', color=JT, lw=1.8, label='alkan-1-ol (C$_n$H$_{2n+1}$OH)'); ax.plot(n, alk, 's-', color=BIRU, lw=1.8, label='alkana (C$_n$H$_{2n+2}$)')
ax.axhline(0, color='#cccccc', lw=0.7); ax.set_xlabel('jumlah atom karbon'); ax.set_ylabel('titik didih (°C)')
ax.yaxis.set_major_formatter(fmt); ax.legend(frameon=False, fontsize=8.5)
ax.annotate('ikatan hidrogen\nmenaikkan titik didih', (2, 78.4), (3.2, -110), fontsize=8.2, color=TUA, arrowprops=dict(arrowstyle='-|>', color=TUA, lw=0.8))
plt.tight_layout(); simpan(f, 'didih')

# 15. ikatan hidrogen etanol vs dimetil eter
f, ax = kanv(7.4, 3.2, (0, 30), (-0.8, 12))
def etanol(ox, oy, ang=0):
    return molekul(ax, {'R': (0, 0, 'CH₃CH₂'), 'O': (3.2, 0, 'O'), 'H': (4.0, -0.7, 'H')}, [('R', 'O', 1), ('O', 'H', 1)], lp={'O': [80, 140]}, ox=ox, oy=oy, s=1.3, gap=0.24)
P1 = etanol(1.6, 9.0); P2 = etanol(6.0, 5.6); P3 = etanol(1.6, 2.4)
for a, b in [(P1['H'], P2['O']), (P2['H'], P3['O'] + np.array([0.1, 0.3]))]:
    ax.plot([a[0] + 0.1, b[0] - 0.05], [a[1] - 0.15, b[1] + 0.3], color=BIRU, lw=1.6, ls=(0, (2, 2)))
T(ax, 7.0, 10.6, 'etanol: donor dan akseptor ikatan hidrogen', fs=8.8, c=BIRU, fontweight='bold'); T(ax, 7.0, -0.1, 'titik didih 78 °C', fs=8.8)
ax.plot([15, 15], [0.5, 11.5], color='#cccccc', lw=0.8)
def eter(ox, oy):
    return molekul(ax, {'a': (0, 0, 'CH₃'), 'O': (1.6, 0.6, 'O'), 'b': (3.2, 0, 'CH₃')}, [('a', 'O', 1), ('O', 'b', 1)], lp={'O': [60, 120]}, ox=ox, oy=oy, s=1.3)
eter(17.5, 8.0); eter(22.5, 5.0); eter(17.5, 2.0)
T(ax, 22.0, 10.6, 'dimetil eter: tidak ada H pada O', fs=8.8, c=JT, fontweight='bold'); T(ax, 22.0, -0.1, 'titik didih −24 °C', fs=8.8)
simpan(f, 'ikatanH')

# 16. kelarutan alkohol dalam air
f, ax = plt.subplots(figsize=(6.0, 2.9), dpi=220)
nm = ['metanol', 'etanol', 'propan-1-ol', 'butan-1-ol', 'pentan-1-ol', 'heksan-1-ol', 'heptan-1-ol', 'oktan-1-ol']
v = [None, None, None, 7.7, 2.2, 0.59, 0.17, 0.054]
x = np.arange(8)
for i, val in enumerate(v):
    if val is None: ax.bar(i, 12, color=MUDA); ax.text(i, 12.3, 'campur\nsempurna', ha='center', fontsize=7, color=TUA)
    else: ax.bar(i, val, color=BIRU); ax.text(i, val + 0.3, koma(val), ha='center', fontsize=7.5, color=TUA)
ax.set_xticks(x); ax.set_xticklabels(nm, rotation=30, ha='right', fontsize=8); ax.set_ylabel('kelarutan (g per 100 mL air)'); ax.set_ylim(0, 15)
ax.yaxis.set_major_formatter(fmt)
plt.tight_layout(); simpan(f, 'larut')
print('ok tambahan')
