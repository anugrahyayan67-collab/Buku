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
    o.bondLineWidth = 2; o.fixedFontSize = 30; o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74)})
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
    return molekul(ax, {'R': (0, 0, 'C₂H₅'), 'O': (2.6, 0, 'O'), 'H': (3.4, -0.7, 'H')}, [('R', 'O', 1), ('O', 'H', 1)], lp={'O': [80, 140]}, ox=ox, oy=oy, s=1.3, gap=0.24)
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

# ================= versi ilustrasi 3D (menggantikan versi garis) =================
from ilustrasi import ax3d, sumbu, orbital_s, orbital_p, orbital_hibrid, tetes, molekul3d, bola, batang, EMAS, JINGGA, BIRU3, MERAH3
from rdkit.Chem import AllChem
def koord(smi, seed=7):
    m = Chem.AddHs(Chem.MolFromSmiles(smi)); AllChem.EmbedMolecule(m, randomSeed=seed); AllChem.MMFFOptimizeMolecule(m)
    P = m.GetConformer().GetPositions(); P = P - P[[a.GetIdx() for a in m.GetAtoms() if a.GetSymbol() != 'H'][0]]
    return m, P
def pasang(m, P):
    atom = [(a.GetSymbol(), P[a.GetIdx()]) for a in m.GetAtoms()]; ik = [(b.GetBeginAtomIdx(), b.GetEndAtomIdx()) for b in m.GetBonds()]; return atom, ik
def layar(az):
    a = np.radians(az); return np.array([-np.sin(a), np.cos(a), 0.0])
def rz(P, u, v):
    u = np.array(u, float); u[2] = 0; a = np.arctan2(v[1], v[0]) - np.arctan2(u[1], u[0]); c, s_ = np.cos(a), np.sin(a)
    return P @ np.array([[c, -s_, 0], [s_, c, 0], [0, 0, 1]]).T
def putar(P, u, v):
    """putar sehingga vektor u menjadi v"""
    from ilustrasi import _rot
    R1 = _rot(u).T; R2 = _rot(v); return P @ R1.T @ R2.T

# orbital: diagram energi (garis tipis) + bentuk orbital berbayang
f = plt.figure(figsize=(7.4, 2.0), dpi=220)
a = f.add_axes([0.0, 0.08, 0.24, 0.84]); a.set_xlim(0, 6); a.set_ylim(0, 10); a.axis('off')
for y, lab, n_ in [(1.0, '1s', 1), (4.0, '2s', 1), (7.0, '2p', 3)]:
    for i in range(n_): a.plot([1.4 + i * 1.5, 2.5 + i * 1.5], [y, y], color=TUA, lw=1.2)
    a.text(0.9, y, lab, fontsize=9, color=TUA, va='center', ha='right')
for x, y, s in [(1.95, 1.0, 'ud'), (1.95, 4.0, 'ud'), (1.95, 7.0, 'u'), (3.45, 7.0, 'u')]:
    if 'u' in s: a.annotate('', (x - 0.15, y + 1.1), (x - 0.15, y + 0.05), arrowprops=dict(arrowstyle='-|>', color=BIRU, lw=1.0, mutation_scale=8))
    if 'd' in s: a.annotate('', (x + 0.15, y + 0.05), (x + 0.15, y + 1.1), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.0, mutation_scale=8))
a.text(3.0, 9.6, 'karbon: 1s² 2s² 2p²', fontsize=9, color=TUA, ha='center', fontweight='bold')
for k, (nm, d) in enumerate([('s', None), ('$p_x$', (1, 0, 0)), ('$p_y$', (0, 1, 0)), ('$p_z$', (0, 0, 1))]):
    ax = ax3d(f, [0.25 + k * 0.19, 0.1, 0.19, 0.95], lim=0.95); sumbu(ax, L=0.95, fs=8)
    if d is None: orbital_s(ax, 0.5)
    else: orbital_p(ax, d, 1.0)
    f.text(0.25 + k * 0.19 + 0.095, 0.04, nm, ha='center', fontsize=10, color=TUA)
f.savefig(f'{F}/orbital.png', bbox_inches='tight'); plt.close(f)

# hibridisasi
f = plt.figure(figsize=(7.4, 2.5), dpi=220)
t4 = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
ax = ax3d(f, [0.0, 0.1, 0.33, 0.9], lim=1.15, elev=12, azim=-52)
for d in t4: orbital_hibrid(ax, d, 0.25, 1.05)
f.text(0.165, 0.04, 'sp³: empat cuping ke sudut tetrahedron\n(109,5°)', ha='center', fontsize=8.6, color=TUA)
ax = ax3d(f, [0.335, 0.1, 0.33, 0.9], lim=1.15, elev=22, azim=-60)
for g in (90, 210, 330): orbital_hibrid(ax, (np.cos(np.radians(g)), np.sin(np.radians(g)), 0), 1 / 3, 1.05)
orbital_p(ax, (0, 0, 1), 0.85, w1='#8dbbe8', w2='#8dbbe8')
f.text(0.5, 0.04, 'sp² + p: tiga cuping dalam satu bidang\n(120°); orbital p tegak lurus', ha='center', fontsize=8.6, color=TUA)
ax = ax3d(f, [0.67, 0.1, 0.33, 0.9], lim=1.15, elev=22, azim=-60)
for d in [(1, 0, 0), (-1, 0, 0)]: orbital_hibrid(ax, d, 0.5, 1.05)
orbital_p(ax, (0, 1, 0), 0.75, w1='#8dbbe8', w2='#8dbbe8'); orbital_p(ax, (0, 0, 1), 0.75, w1='#a9cdf0', w2='#a9cdf0')
f.text(0.835, 0.04, 'sp + 2p: dua cuping segaris (180°);\ndua orbital p tegak lurus', ha='center', fontsize=8.6, color=TUA)
f.savefig(f'{F}/hibrid.png', bbox_inches='tight'); plt.close(f)

# sigma dan pi
f = plt.figure(figsize=(7.4, 2.3), dpi=220)
pan = [('s + s (H–H)', 'ss'), ('sp³ + s (C–H)', 'hs'), ('sp³ + sp³ (C–C)', 'hh'), ('p + p sisi ke sisi (π)', 'pp')]
for k, (t, j) in enumerate(pan):
    ax = ax3d(f, [k * 0.25, 0.12, 0.25, 0.88], lim=1.25, elev=14, azim=-80)
    if j == 'ss': orbital_s(ax, 0.55, (-0.42, 0, 0)); orbital_s(ax, 0.55, (0.42, 0, 0), w='#7fb0e6')
    if j == 'hs': orbital_hibrid(ax, (1, 0, 0), 0.25, 1.0, (-0.75, 0, 0)); orbital_s(ax, 0.42, (0.62, 0, 0), w='#8dc0ee')
    if j == 'hh': orbital_hibrid(ax, (1, 0, 0), 0.25, 0.9, (-0.85, 0, 0)); orbital_hibrid(ax, (-1, 0, 0), 0.25, 0.9, (0.85, 0, 0), w='#f3c86a')
    if j == 'pp':
        for x in (-0.45, 0.45): orbital_p(ax, (0, 0, 1), 0.85, (x, 0, 0), w1=JG, w2=JG)
        ax.plot([-0.45, 0.45], [0, 0], [0, 0], color=TUA, lw=1.2)
    f.text(k * 0.25 + 0.125, 0.05, t, ha='center', fontsize=8.8, color=TUA)
f.text(0.375, 0.95, 'ikatan σ: tumpang tindih ujung ke ujung, di sepanjang sumbu antarinti', ha='center', fontsize=8.8, color=BIRU, fontweight='bold')
f.text(0.875, 0.95, 'ikatan π: di atas dan di bawah sumbu', ha='center', fontsize=8.8, color=JT, fontweight='bold')
f.savefig(f'{F}/sigmapi.png', bbox_inches='tight'); plt.close(f)

# dipol: bola-batang (penggambar 2D berurutan kedalaman) dengan panah tipis
from ilustrasi import bolabatang, hadap
def kanvas2d(f, rect, lim=1.6):
    a = f.add_axes(rect); a.set_xlim(-lim, lim); a.set_ylim(-lim, lim); a.set_aspect('equal'); a.axis('off'); return a
def pdipol(a, p, q, c=MERAH):
    p, q = np.array(p, float), np.array(q, float); a.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=9, color=c, lw=1.3, zorder=200))
    d = (q - p) / np.hypot(*(q - p)); n = np.array([-d[1], d[0]]) * 0.11; c0 = p + d * 0.12; a.plot([c0[0] - n[0], c0[0] + n[0]], [c0[1] - n[1], c0[1] + n[1]], color=c, lw=1.3, zorder=200)
f = plt.figure(figsize=(7.4, 2.5), dpi=220)
EL, AZ = 12, -70
for k, (smi, nm, mu) in enumerate([('O=C=O', 'CO₂', 'μ = 0 D'), ('O', 'H₂O', 'μ = 1,85 D'), ('CCl', 'CH₃Cl', 'μ = 1,87 D'), ('C(Cl)(Cl)(Cl)Cl', 'CCl₄', 'μ = 0 D')]):
    m, P = koord(smi)
    hs = [a.GetIdx() for a in m.GetAtoms() if a.GetSymbol() == 'H']
    if smi == 'O=C=O': P = hadap(P - P[1], kanan=P[0] - P[1], atas=(0, 0, 1), elev=EL, azim=AZ)
    if smi == 'O': P = hadap(P, kanan=P[hs[0]] - P[hs[1]], atas=-(P[hs[0]] + P[hs[1]]), elev=EL, azim=AZ)
    if smi == 'CCl': ax_ = P[1] - P[0]; h_ = P[hs[0]] - np.dot(P[hs[0]], ax_) / np.dot(ax_, ax_) * ax_; P = hadap(P, atas=ax_, kanan=h_ * 0.5 + np.cross(ax_, h_) * 0.3, elev=EL, azim=AZ)
    if smi.startswith('C(Cl)'): ax_ = P[1] - P[0]; h_ = P[2] - np.dot(P[2], ax_) / np.dot(ax_, ax_) * ax_; P = hadap(P, atas=ax_, kanan=h_ * 0.5 + np.cross(ax_, h_) * 0.3, elev=EL, azim=AZ)
    a = kanvas2d(f, [k * 0.25, 0.17, 0.25, 0.76], lim=2.5)
    atom, ik = pasang(m, P); bolabatang(a, atom, ik, elev=EL, azim=AZ, skala=1.0)
    if smi == 'O=C=O': pdipol(a, (-0.2, 0.65), (-1.15, 0.65)); pdipol(a, (0.2, 0.65), (1.15, 0.65))
    if smi == 'O': pdipol(a, (0, -1.4), (0, -0.45))
    if smi == 'CCl': pdipol(a, (1.15, -0.4), (1.15, 1.7))
    f.text(k * 0.25 + 0.125, 0.03, f'{nm}\n{mu}', ha='center', fontsize=9, color=TUA)
f.text(0.5, 0.97, 'panah dipol menunjuk dari ujung δ+ ke ujung δ−; pada CO₂ dan CCl₄ vektor saling meniadakan', ha='center', fontsize=8.6, color=MERAH)
f.savefig(f'{F}/dipol.png', bbox_inches='tight'); plt.close(f)

# VSEPR: bola-batang dengan pasangan bebas sebagai cuping
f = plt.figure(figsize=(7.4, 2.3), dpi=220)
for k, (smi, nm, sud, npb) in enumerate([('C', 'metana', '109,5°', 0), ('N', 'amonia', '107°', 1), ('O', 'air', '104,5°', 2)]):
    m, P = koord(smi); hs = [a.GetIdx() for a in m.GetAtoms() if a.GetSymbol() == 'H']
    sH = sum(P[h] / np.linalg.norm(P[h]) for h in hs)
    if npb == 0: P = hadap(P, atas=P[hs[0]], kanan=np.cross(P[hs[0]], P[hs[1]]), elev=14, azim=-55)
    if npb == 1: P = hadap(P, atas=-sH, kanan=np.cross(-sH, P[hs[0]]) + P[hs[0]] * 0.0, elev=14, azim=-55)
    if npb == 2:
        H1, H2 = P[hs[0]], P[hs[1]]; P = hadap(P, atas=-(H1 + H2), kanan=(H1 - H2) * 0.6 + np.cross(H1, H2) * 0.8, elev=14, azim=-55)
    cup = []
    if npb == 1: cup = [(0, (0, 0, 1), '#f3c86a')]
    if npb == 2:
        H1, H2 = [P[h] / np.linalg.norm(P[h]) for h in hs]; bis = -(H1 + H2); bis /= np.linalg.norm(bis); n = np.cross(H1, H2); n /= np.linalg.norm(n)
        cup = [(0, bis * 0.58 + n * 0.81 * sg, '#f3c86a') for sg in (1, -1)]
    a = kanvas2d(f, [k * 0.333, 0.2, 0.333, 0.78], lim=1.45)
    atom, ik = pasang(m, P); bolabatang(a, atom, ik, elev=14, azim=-55, skala=1.0, cuping=cup)
    f.text(k * 0.333 + 0.166, 0.03, f'{nm} ({sud})\n{4 - npb} ikatan, {npb} pasangan bebas', ha='center', fontsize=8.8, color=TUA)
f.savefig(f'{F}/vsepr.png', bbox_inches='tight'); plt.close(f)
print('ok ilustrasi')

# ================= versi render WebGL (three.js) =================
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3d'))
from r3d import render, spek_molekul, tampil, tetra, hx, kamera_terbaik
TMP = os.path.join(F, '_r3d'); os.makedirs(TMP, exist_ok=True)
BIRU_O, MERAH_O, EMAS_O, JG_O, PUC = 0x4f86d9, 0xe0707a, 0xf4b942, 0xf0a060, 0x9cc4ee
def sumbu3(L=1.25):
    return [{'p': [-L, 0, 0], 'q': [L, 0, 0]}, {'p': [0, -L, 0], 'q': [0, L, 0]}, {'p': [0, 0, -L], 'q': [0, 0, L]}]
def lob(d, L=1.0, w=0.36, c=EMAS_O, o=(0, 0, 0), a=1.0, k=0.7): return {'d': list(map(float, d)), 'L': L, 'w': w, 'c': c, 'o': list(o), 'a': a, 'k': k}
def porb(d, L=0.95, c1=BIRU_O, c2=MERAH_O, o=(0, 0, 0)): return [lob(d, L, 0.36, c1, o), lob(-np.array(d, float), L, 0.36, c2, o)]
def horb(d, c=EMAS_O, o=(0, 0, 0), s=1.0): return [lob(d, 1.1 * s, 0.42 * s, c, o, k=0.75), lob(-np.array(d, float), 0.3 * s, 0.16 * s, 0xe8893a, o, k=0.6)]
CAM = [1.0, -1.35, 0.55]
jobs = []
# orbital s, p
for nm, d in [('s', None), ('px', (1, 0, 0)), ('py', (0, 1, 0)), ('pz', (0, 0, 1))]:
    sp = {'w': 520, 'h': 520, 'zoom': 1.45, 'camdir': CAM, 'axes': sumbu3(1.3), 'labels': [[1.45, 0, 0], [0, 1.45, 0], [0, 0, 1.45]]}
    if d is None: sp['spheres'] = [{'p': [0, 0, 0], 'r': 0.55, 'c': BIRU_O}]
    else: sp['lobes'] = porb(d)
    jobs.append((sp, f'{TMP}/o_{nm}.png'))
# hibrid
jobs.append(({'w': 600, 'h': 560, 'zoom': 1.35, 'camdir': [1.0, -1.6, 0.35], 'lobes': sum([horb(v) for v in tetra()], [])}, f'{TMP}/h_sp3.png'))
jobs.append(({'w': 600, 'h': 560, 'zoom': 1.35, 'camdir': [0.7, -1.4, 0.6], 'lobes': sum([horb((np.cos(a), np.sin(a), 0)) for a in np.radians([90, 210, 330])], []) + porb((0, 0, 1), 0.85, PUC, PUC)}, f'{TMP}/h_sp2.png'))
jobs.append(({'w': 600, 'h': 560, 'zoom': 1.35, 'camdir': [0.7, -1.4, 0.6], 'lobes': horb((1, 0, 0)) + horb((-1, 0, 0)) + porb((0, 1, 0), 0.8, PUC, PUC) + porb((0, 0, 1), 0.8, 0xb9d7f3, 0xb9d7f3)}, f'{TMP}/h_sp.png'))
# sigma pi
SC = [0.15, -1, 0.25]
jobs.append(({'w': 600, 'h': 380, 'zoom': 0.95, 'camdir': SC, 'spheres': [{'p': [-0.42, 0, 0], 'r': 0.55, 'c': BIRU_O}, {'p': [0.42, 0, 0], 'r': 0.55, 'c': PUC}]}, f'{TMP}/s_ss.png'))
jobs.append(({'w': 600, 'h': 380, 'zoom': 0.95, 'camdir': SC, 'lobes': horb((1, 0, 0), o=(-0.75, 0, 0)), 'spheres': [{'p': [0.62, 0, 0], 'r': 0.42, 'c': PUC}]}, f'{TMP}/s_hs.png'))
jobs.append(({'w': 600, 'h': 380, 'zoom': 0.95, 'camdir': SC, 'lobes': horb((1, 0, 0), o=(-0.85, 0, 0), s=0.9) + horb((-1, 0, 0), c=0xf6d27a, o=(0.85, 0, 0), s=0.9)}, f'{TMP}/s_hh.png'))
jobs.append(({'w': 600, 'h': 380, 'zoom': 0.95, 'camdir': SC, 'lobes': porb((0, 0, 1), 0.85, JG_O, JG_O, (-0.45, 0, 0)) + porb((0, 0, 1), 0.85, JG_O, JG_O, (0.45, 0, 0)),
              'bonds': [{'p': [-0.45, 0, 0], 'q': [0.45, 0, 0], 'r': 0.03, 'c': 0x3b4049}]}, f'{TMP}/s_pp.png'))
# molekul: geometri ideal
def mol(at, ik): return at, ik
dCO, dOH, dCH, dCCl, dNH = 1.16, 0.96, 1.09, 1.78, 1.01
t = tetra()
M = {}
M['co2'] = ([('C', (0, 0, 0)), ('O', (dCO, 0, 0)), ('O', (-dCO, 0, 0))], [(0, 1, 2), (0, 2, 2)])
a = np.radians(104.5 / 2); M['h2o'] = ([('O', (0, 0, 0)), ('H', (dOH * np.sin(a), 0, -dOH * np.cos(a))), ('H', (-dOH * np.sin(a), 0, -dOH * np.cos(a)))], [(0, 1), (0, 2)])
M['ch3cl'] = ([('C', (0, 0, 0)), ('Cl', tuple(t[0] * dCCl))] + [('H', tuple(v * dCH)) for v in t[1:]], [(0, 1), (0, 2), (0, 3), (0, 4)])
M['ccl4'] = ([('C', (0, 0, 0))] + [('Cl', tuple(v * dCCl)) for v in t], [(0, 1), (0, 2), (0, 3), (0, 4)])
M['ch4'] = ([('C', (0, 0, 0))] + [('H', tuple(v * dCH)) for v in t], [(0, 1), (0, 2), (0, 3), (0, 4)])
M['nh3'] = ([('N', (0, 0, 0))] + [('H', tuple(v * dNH)) for v in t[1:]], [(0, 1), (0, 2), (0, 3)])
M['h2o_v'] = ([('O', (0, 0, 0)), ('H', (0.76, 0, -0.59)), ('H', (-0.76, 0, -0.59))], [(0, 1), (0, 2)])
MC = [0.35, -1, 0.18]
lab_dipol = {'co2': [[-0.25, 0, 0.6], [-1.1, 0, 0.6], [0.25, 0, 0.6], [1.1, 0, 0.6]], 'h2o': [[0, 0, -1.25], [0, 0, -0.35]], 'ch3cl': [[0, 0, 0], list(t[0] * dCCl)], 'ccl4': [[0, 0, 0]]}
for k in ['co2', 'h2o', 'ch3cl', 'ccl4']:
    sp = spek_molekul(*M[k], ganda=[0, 0, 1]); sp.update({'w': 520, 'h': 560, 'zoom': 2.45, 'target': [0, 0, 0.25], 'camdir': MC if k not in ('ch3cl', 'ccl4') else kamera_terbaik([p for _, p in M[k][0]], (5, 15)), 'labels': lab_dipol[k]}); jobs.append((sp, f'{TMP}/d_{k}.png'))
for k, npb in [('ch4', 0), ('nh3', 1), ('h2o_v', 2)]:
    pts = [p for _, p in M[k][0]] + ([tuple(t[0] * 0.9)] if npb == 1 else []) + ([(0, 0.62, 0.45), (0, -0.62, 0.45)] if npb == 2 else [])
    sp = spek_molekul(*M[k]); sp.update({'w': 520, 'h': 520, 'zoom': 1.55, 'camdir': kamera_terbaik(pts, (10, 30))})
    r0 = 0.30  # sedikit di bawah jari-jari atom pusat agar ujung cuping menempel rapat
    if npb == 1: sp['lobes'] = [lob(t[0], 0.95, 0.34, 0xf3c86a, o=tuple(t[0] * r0))]
    if npb == 2: sp['lobes'] = [lob((0, sg * 0.81, 0.58), 0.95, 0.34, 0xf3c86a, o=(0, sg * 0.81 * r0, 0.58 * r0)) for sg in (1, -1)]
    jobs.append((sp, f'{TMP}/v_{k}.png'))
META = render(jobs)

def bingkai(f, rect): a = f.add_axes(rect); a.axis('off'); return a
# susun gambar orbital
f = plt.figure(figsize=(7.4, 2.0), dpi=220)
a = f.add_axes([0.0, 0.08, 0.24, 0.84]); a.set_xlim(0, 6); a.set_ylim(0, 10); a.axis('off')
for y, lab, n_ in [(1.0, '1s', 1), (4.0, '2s', 1), (7.0, '2p', 3)]:
    for i in range(n_): a.plot([1.4 + i * 1.5, 2.5 + i * 1.5], [y, y], color=TUA, lw=1.1)
    a.text(0.9, y, lab, fontsize=9, color=TUA, va='center', ha='right')
for x, y, s_ in [(1.95, 1.0, 'ud'), (1.95, 4.0, 'ud'), (1.95, 7.0, 'u'), (3.45, 7.0, 'u')]:
    if 'u' in s_: a.annotate('', (x - 0.15, y + 1.1), (x - 0.15, y + 0.05), arrowprops=dict(arrowstyle='-|>', color=BIRU, lw=1.0, mutation_scale=8))
    if 'd' in s_: a.annotate('', (x + 0.15, y + 0.05), (x + 0.15, y + 1.1), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.0, mutation_scale=8))
a.text(3.0, 9.6, 'karbon: 1s² 2s² 2p²', fontsize=9, color=TUA, ha='center', fontweight='bold')
for k, (nm, t_) in enumerate([('s', 's'), ('px', '$p_x$'), ('py', '$p_y$'), ('pz', '$p_z$')]):
    a = bingkai(f, [0.25 + k * 0.19, 0.12, 0.19, 0.86]); fn = f'{TMP}/o_{nm}.png'
    tampil(a, fn, [('x', 0), ('y', 0), ('z', 0)], META[fn], fs=8, c='#55606b', style='italic')
    f.text(0.25 + k * 0.19 + 0.095, 0.04, t_, ha='center', fontsize=10, color=TUA)
f.savefig(f'{F}/orbital.png', bbox_inches='tight'); plt.close(f)
# hibrid
f = plt.figure(figsize=(7.4, 2.5), dpi=220)
for k, (nm, t_) in enumerate([('sp3', 'sp³: empat cuping ke sudut tetrahedron\n(109,5°)'), ('sp2', 'sp² + p: tiga cuping dalam satu bidang\n(120°); orbital p tegak lurus'), ('sp', 'sp + 2p: dua cuping segaris (180°);\ndua orbital p tegak lurus')]):
    a = bingkai(f, [k * 0.333, 0.2, 0.333, 0.8]); tampil(a, f'{TMP}/h_{nm}.png'); f.text(k * 0.333 + 0.166, 0.03, t_, ha='center', fontsize=8.6, color=TUA)
f.savefig(f'{F}/hibrid.png', bbox_inches='tight'); plt.close(f)
# sigma pi
f = plt.figure(figsize=(7.4, 1.9), dpi=220)
for k, (nm, t_) in enumerate([('ss', 's + s (H–H)'), ('hs', 'sp³ + s (C–H)'), ('hh', 'sp³ + sp³ (C–C)'), ('pp', 'p + p sisi ke sisi (π)')]):
    a = bingkai(f, [k * 0.25, 0.16, 0.25, 0.68]); tampil(a, f'{TMP}/s_{nm}.png'); f.text(k * 0.25 + 0.125, 0.04, t_, ha='center', fontsize=8.8, color=TUA)
f.text(0.375, 0.95, 'ikatan σ: tumpang tindih ujung ke ujung, di sepanjang sumbu antarinti', ha='center', fontsize=8.8, color=BIRU, fontweight='bold')
f.text(0.875, 0.95, 'ikatan π: di atas dan di bawah sumbu', ha='center', fontsize=8.8, color=JT, fontweight='bold')
f.savefig(f'{F}/sigmapi.png', bbox_inches='tight'); plt.close(f)
# dipol
def pd2(a, p, q, c=MERAH):
    p, q = np.array(p, float), np.array(q, float); a.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=10, color=c, lw=1.4, zorder=5))
    d = (q - p) / np.hypot(*(q - p)); n = np.array([-d[1], d[0]]) * 9; c0 = p + d * 14; a.plot([c0[0] - n[0], c0[0] + n[0]], [c0[1] - n[1], c0[1] + n[1]], color=c, lw=1.4, zorder=5)
f = plt.figure(figsize=(7.4, 2.3), dpi=220)
for k, (nm, t_, mu) in enumerate([('co2', 'CO₂', 'μ = 0 D'), ('h2o', 'H₂O', 'μ = 1,85 D'), ('ch3cl', 'CH₃Cl', 'μ = 1,87 D'), ('ccl4', 'CCl₄', 'μ = 0 D')]):
    a = bingkai(f, [k * 0.25, 0.18, 0.25, 0.74]); fn = f'{TMP}/d_{nm}.png'; tampil(a, fn); pr = META[fn]
    if nm == 'co2': pd2(a, pr[0], pr[1]); pd2(a, pr[2], pr[3])
    if nm == 'h2o': pd2(a, pr[0], pr[1])
    if nm == 'ch3cl': o_ = np.array([150, 0]); v_ = np.array(pr[1]) - np.array(pr[0]); pd2(a, np.array(pr[0]) + o_ - v_ * 0.35, np.array(pr[1]) + o_ + v_ * 0.1)
    f.text(k * 0.25 + 0.125, 0.03, f'{t_}\n{mu}', ha='center', fontsize=9, color=TUA)
f.text(0.5, 0.97, 'panah dipol menunjuk dari ujung δ+ ke ujung δ−; pada CO₂ dan CCl₄ vektor saling meniadakan', ha='center', fontsize=8.6, color=MERAH)
f.savefig(f'{F}/dipol.png', bbox_inches='tight'); plt.close(f)
# VSEPR
f = plt.figure(figsize=(7.4, 2.3), dpi=220)
for k, (nm, t_, sud, npb) in enumerate([('ch4', 'metana', '109,5°', 0), ('nh3', 'amonia', '107°', 1), ('h2o_v', 'air', '104,5°', 2)]):
    a = bingkai(f, [k * 0.333, 0.2, 0.333, 0.78]); tampil(a, f'{TMP}/v_{nm}.png')
    f.text(k * 0.333 + 0.166, 0.03, f'{t_} ({sud})\n{4 - npb} ikatan, {npb} pasangan bebas', ha='center', fontsize=8.8, color=TUA)
f.savefig(f'{F}/vsepr.png', bbox_inches='tight'); plt.close(f)
print('ok webgl')

# rotasi ikatan rangkap: render 3D
dCC = 1.34; hx_, hz_ = 1.09 * np.cos(np.radians(60)), 1.09 * np.sin(np.radians(60))
def etena(putar90=False):
    a = [('C', (-dCC / 2, 0, 0)), ('C', (dCC / 2, 0, 0)), ('H', (-dCC / 2 - hx_, hz_, 0)), ('H', (-dCC / 2 - hx_, -hz_, 0))]
    if putar90: a += [('H', (dCC / 2 + hx_, 0, hz_)), ('H', (dCC / 2 + hx_, 0, -hz_))]
    else: a += [('H', (dCC / 2 + hx_, hz_, 0)), ('H', (dCC / 2 + hx_, -hz_, 0))]
    return a, [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)]
J = []
for k, tw in [('rata', False), ('putar', True)]:
    at, ik = etena(tw); sp = spek_molekul(at, ik); sp.update({'w': 640, 'h': 520, 'zoom': 1.5, 'camdir': [0.55, -1, 0.5]})
    sp['lobes'] = porb((0, 0, 1), 0.8, JG_O, JG_O, (-dCC / 2, 0, 0)) + (porb((0, 1, 0), 0.8, JG_O, JG_O, (dCC / 2, 0, 0)) if tw else porb((0, 0, 1), 0.8, JG_O, JG_O, (dCC / 2, 0, 0)))
    for l_ in sp['lobes']: l_['w'] = 0.27; l_['a'] = 0.78
    J.append((sp, f'{TMP}/r_{k}.png'))
render(J)
f = plt.figure(figsize=(7.0, 2.4), dpi=220)
a = bingkai(f, [0.0, 0.2, 0.42, 0.8]); tampil(a, f'{TMP}/r_rata.png'); f.text(0.21, 0.04, 'kedua orbital p sejajar:\ntumpang tindih, ikatan π ada', ha='center', fontsize=8.8, color=TUA)
a = bingkai(f, [0.58, 0.2, 0.42, 0.8]); tampil(a, f'{TMP}/r_putar.png'); f.text(0.79, 0.04, 'satu karbon diputar 90°:\ntumpang tindih nol, ikatan π putus', ha='center', fontsize=8.8, color=TUA)
f.add_artist(FancyArrowPatch((0.44, 0.55), (0.56, 0.55), transform=f.transFigure, arrowstyle='-|>', mutation_scale=12, color=TUA, lw=1.3)); f.text(0.5, 0.65, '≈ 260 kJ mol$^{-1}$', ha='center', fontsize=8.8, color=MERAH)
f.savefig(f'{F}/rotasi.png', bbox_inches='tight'); plt.close(f)
print('ok rotasi')

print('ok ikatanH')
