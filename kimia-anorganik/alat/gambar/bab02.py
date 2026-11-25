#!/usr/bin/env python3
# Gambar Bab 2 Kimia Anorganik 1: ikatan kovalen dan bentuk molekul. -> bab02/fig/*.png
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Ellipse, FancyArrowPatch
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab02', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.edgecolor': '#0e2748', 'axes.labelcolor': '#0e2748',
                     'xtick.color': '#0e2748', 'ytick.color': '#0e2748', 'axes.spines.top': False, 'axes.spines.right': False})
TUA, BIRU, MUDA, JG, JGT, HIJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
koma = FuncFormatter(lambda v, p: (f'{v:g}').replace('.', ','))
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)

# proyeksi 3D sederhana
TH, PH = np.deg2rad(28), np.deg2rad(18)
def P(v):
    x, y, z = v
    X = x * np.cos(TH) - y * np.sin(TH)
    Y = (x * np.sin(TH) + y * np.cos(TH)) * np.sin(PH) + z * np.cos(PH)
    d = (x * np.sin(TH) + y * np.cos(TH)) * np.cos(PH) - z * np.sin(PH)
    return X, Y, d
GEO = {
    2: [(0, 0, 1), (0, 0, -1)],
    3: [(0, 0, 1), (.866, 0, -.5), (-.866, 0, -.5)],
    4: [(0, 0, 1), (.943, 0, -.333), (-.471, .816, -.333), (-.471, -.816, -.333)],
    5: [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-.5, .866, 0), (-.5, -.866, 0)],
    6: [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)],
}
def molekul(ax, n, pb=(), cx=0, cy=0, s=1.0, pusat='A'):
    """n domain; pb = indeks domain yang berupa pasangan bebas."""
    items = []
    for i, v in enumerate(GEO[n]):
        X, Y, d = P(v); items.append((d, i, X, Y))
    for d, i, X, Y in sorted(items, reverse=True):
        if i in pb:
            ang = np.degrees(np.arctan2(Y, X))
            ax.add_patch(Ellipse((cx + .55 * s * X, cy + .55 * s * Y), .75 * s, .42 * s, angle=ang, fc=MUDA, ec=BIRU, lw=1, alpha=.8, zorder=2 if d > 0 else 4))
            for k in (-1, 1):
                ax.plot(cx + .62 * s * X + k * .07 * s * np.sin(np.radians(ang)), cy + .62 * s * Y - k * .07 * s * np.cos(np.radians(ang)), 'o', ms=2.5, color=TUA, zorder=5)
        else:
            ax.plot([cx, cx + s * X], [cy, cy + s * Y], color='#8a9aa8', lw=3 * s, zorder=2 if d > 0 else 4, solid_capstyle='round')
            ax.add_patch(plt.Circle((cx + s * X, cy + s * Y), .2 * s, fc=JG, ec=JGT, lw=1, zorder=3 if d > 0 else 5))
    ax.add_patch(plt.Circle((cx, cy), .27 * s, fc=BIRU, ec=TUA, lw=1, zorder=4.5))

# 1. Galeri geometri dasar VSEPR
f, ax = plt.subplots(figsize=(7.6, 2.3)); ax.axis('off'); ax.set_aspect('equal')
nama = ['2: linear\n180°', '3: segitiga datar\n120°', '4: tetrahedron\n109,5°', '5: bipiramida segitiga\n90°, 120°', '6: oktahedron\n90°']
for k, n in enumerate([2, 3, 4, 5, 6]):
    molekul(ax, n, cx=3 * k, cy=0, s=1.0); ax.text(3 * k, -1.75, nama[k], ha='center', va='top', fontsize=9, color=TUA)
ax.set_xlim(-1.4, 13.4); ax.set_ylim(-2.7, 1.4)
simpan(f, 'a_vsepr')

# 2. Bentuk dengan pasangan bebas
f, ax = plt.subplots(figsize=(7.6, 4.4)); ax.axis('off'); ax.set_aspect('equal')
kasus = [(4, (0,), 'AX₃E\npiramida segitiga\nNH₃'), (4, (0, 3), 'AX₂E₂\nbengkok\nH₂O'), (5, (2,), 'AX₄E\njungkat-jungkit\nSF₄'),
         (5, (3, 4), 'AX₃E₂\nbentuk T\nClF₃'), (5, (2, 3, 4), 'AX₂E₃\nlinear\nXeF₂'), (6, (1,), 'AX₅E\npiramida alas persegi\nBrF₅'),
         (6, (0, 1), 'AX₄E₂\nsegi empat datar\nXeF₄')]
for k, (n, pb, lab) in enumerate(kasus):
    cx, cy = 3 * (k % 4), -3.9 * (k // 4)
    molekul(ax, n, pb, cx=cx, cy=cy, s=1.0); ax.text(cx, cy - 1.5, lab, ha='center', va='top', fontsize=8.6, color=TUA)
ax.set_xlim(-1.5, 10.5); ax.set_ylim(-7.9, 1.4)
simpan(f, 'b_pasbebas')

# 3. Sudut ikatan hidrida golongan 15 dan 16
f, ax = plt.subplots(figsize=(6.4, 3.0))
g15 = [('NH₃', 106.7), ('PH₃', 93.3), ('AsH₃', 92.1), ('SbH₃', 91.6)]
g16 = [('H₂O', 104.5), ('H₂S', 92.1), ('H₂Se', 90.6), ('H₂Te', 90.3)]
x = np.arange(4)
ax.bar(x - .2, [v for _, v in g15], .38, color=BIRU, label='golongan 15 (EH₃)')
ax.bar(x + .2, [v for _, v in g16], .38, color=JG, label='golongan 16 (H₂E)')
for i in range(4):
    ax.text(i - .2, g15[i][1] + .6, g15[i][0], ha='center', fontsize=8.5, color=TUA)
    ax.text(i + .2, g16[i][1] + .6, g16[i][0], ha='center', fontsize=8.5, color=TUA)
ax.axhline(109.47, color=HIJ, ls='--', lw=1); ax.text(-.45, 110.2, 'tetrahedron 109,5°', ha='left', fontsize=8.5, color=HIJ)
ax.axhline(90, color='#8a9aa8', ls=':', lw=1.2, label='orbital p murni 90°')
ax.set_xticks(x); ax.set_xticklabels(['periode 2', 'periode 3', 'periode 4', 'periode 5'])
ax.set_ylabel('sudut H–E–H (°)'); ax.set_ylim(85, 114); ax.legend(frameon=False, fontsize=8.5, loc='upper right', bbox_to_anchor=(1, .78))
ax.yaxis.set_major_formatter(koma)
simpan(f, 'b_sudut')

# 4. Orbital hibrida sp, sp2, sp3 (penampang sudut |a + b cos t|)
f, axs = plt.subplots(1, 3, figsize=(7.2, 2.4), subplot_kw={'projection': 'polar'})
for ax, (nm, s) in zip(axs, [('sp (50 % s)', .5), ('sp² (33 % s)', 1 / 3), ('sp³ (25 % s)', .25)]):
    t = np.linspace(0, 2 * np.pi, 600); a, b = np.sqrt(s), np.sqrt(1 - s) * np.sqrt(3)
    psi = a + b * np.cos(t); r = psi**2
    ax.fill(t[psi > 0], r[psi > 0], color=JG, alpha=.75); ax.fill(t[psi < 0], r[psi < 0], color=MUDA, alpha=.9)
    ax.plot(t, r, color=TUA, lw=.8); ax.set_yticklabels([]); ax.set_xticklabels([]); ax.grid(alpha=.25)
    ax.set_title(nm, fontsize=10, color=TUA, pad=6); ax.spines['polar'].set_visible(False)
simpan(f, 'b_hibrida')

# 5. Momen dipol: penjumlahan vektor ikatan
f, ax = plt.subplots(figsize=(7.4, 2.6)); ax.axis('off'); ax.set_aspect('equal')
def atom(x, y, t, c=JG, r=.28): ax.add_patch(plt.Circle((x, y), r, fc=c, ec=TUA, lw=1, zorder=3)); ax.text(x, y, t, ha='center', va='center', fontsize=9, fontweight='bold', color=TUA, zorder=4)
def panah(x0, y0, x1, y1, c=JGT, lw=2): ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=12, color=c, lw=lw, zorder=5))
# CO2
atom(0, 0, 'C', '#c9d3dc'); atom(-1.1, 0, 'O'); atom(1.1, 0, 'O')
panah(-.3, .45, -.95, .45); panah(.3, .45, .95, .45); ax.text(0, -.85, 'CO₂\nμ = 0', ha='center', va='top', fontsize=9, color=TUA)
# H2O
ox, oy = 3.6, .2; a = np.radians(104.5 / 2)
atom(ox, oy, 'O'); hx = [ox - np.sin(a), ox + np.sin(a)]; hy = oy - np.cos(a)
for x in hx: ax.plot([ox, x], [oy, hy], color='#8a9aa8', lw=2.5, zorder=2); atom(x, hy, 'H', '#f4f6f4', .22)
panah(ox, oy - 1.2, ox, oy - .35, BIRU, 2.6); ax.text(ox + .25, oy - 1.05, 'μ', fontsize=10, color=BIRU)
ax.text(ox, -1.2, 'H₂O\nμ = 1,85 D', ha='center', va='top', fontsize=9, color=TUA)
# NH3 dan NF3
for k, (nm, sub, mu, arah) in enumerate([('NH₃', 'H', '1,47 D', 1), ('NF₃', 'F', '0,23 D', -1)]):
    cx = 7.0 + 2.6 * k; atom(cx, .35, 'N', '#7fc0f0')
    for dx in (-.7, 0, .7):
        ax.plot([cx, cx + dx], [.35, -.45], color='#8a9aa8', lw=2.5, zorder=2); atom(cx + dx, -.45, sub, '#f4f6f4' if sub == 'H' else JG, .22)
    ax.add_patch(Ellipse((cx, .95), .4, .55, fc=MUDA, ec=BIRU, lw=1, alpha=.8))
    ax.text(cx, -1.2, f'{nm}\nμ = {mu}', ha='center', va='top', fontsize=9, color=TUA)
ax.set_xlim(-1.6, 10.9); ax.set_ylim(-2.1, 1.4)
simpan(f, 'c_dipol')

# 6. Energi dan panjang ikatan terhadap orde ikatan
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0))
DAT = {'C–C': ([347, 614, 839], [154, 134, 120], BIRU), 'N–N': ([160, 418, 945], [145, 125, 110], JG), 'O–O': ([146, 498], [148, 121], HIJ)}
for nm, (E, L, c) in DAT.items():
    o = list(range(1, len(E) + 1))
    a1.plot(o, E, 'o-', color=c, lw=1.8, label=nm); a2.plot(o, L, 'o-', color=c, lw=1.8, label=nm)
a1.set_xlabel('orde ikatan'); a1.set_ylabel('energi ikatan (kJ mol$^{-1}$)'); a1.set_xticks([1, 2, 3]); a1.legend(frameon=False, fontsize=8.5)
a2.set_xlabel('orde ikatan'); a2.set_ylabel('panjang ikatan (pm)'); a2.set_xticks([1, 2, 3]); a2.set_ylim(100, 160)
simpan(f, 'c_ikatan')

# 7. Titik didih hidrida golongan 14-17
BP = {'14': ([-161.5, -111.9, -88.5, -51.8], ['CH₄', 'SiH₄', 'GeH₄', 'SnH₄'], '#8a9aa8'),
      '15': ([-33.3, -87.7, -62.5, -17.0], ['NH₃', 'PH₃', 'AsH₃', 'SbH₃'], BIRU),
      '16': ([100.0, -60.3, -41.3, -2.2], ['H₂O', 'H₂S', 'H₂Se', 'H₂Te'], JGT),
      '17': ([19.5, -85.1, -66.8, -35.4], ['HF', 'HCl', 'HBr', 'HI'], HIJ)}
f, ax = plt.subplots(figsize=(6.4, 3.6))
for g, (v, lab, c) in BP.items():
    ax.plot([2, 3, 4, 5], v, 'o-', color=c, lw=1.8, label=f'golongan {g}')
    ax.text(1.85, v[0], lab[0], ha='right', va='center', fontsize=9, color=c, fontweight='bold')
    ax.plot([2, 3], [v[1] + (v[1] - v[2]), v[1]], ':', color=c, lw=1)
ax.set_xticks([2, 3, 4, 5]); ax.set_xticklabels(['periode 2', '3', '4', '5']); ax.set_xlim(1.3, 5.3)
ax.set_ylabel('titik didih (°C)'); ax.legend(frameon=False, fontsize=8.5, loc='upper left', bbox_to_anchor=(1.0, 1.0)); ax.yaxis.set_major_formatter(koma)
simpan(f, 'c_hidrida')

# 8. Gaya dispersi: titik didih gas mulia terhadap polarisabilitas
GM = [('He', .205, 4.2), ('Ne', .396, 27.1), ('Ar', 1.64, 87.3), ('Kr', 2.48, 119.8), ('Xe', 4.04, 165.0), ('Rn', 5.3, 211.5)]
f, ax = plt.subplots(figsize=(5.6, 3.0))
ax.plot([a for _, a, _ in GM], [t for _, _, t in GM], 'o-', color=BIRU, lw=1.8)
for n, a, t in GM: ax.text(a + .12, t - 6, n, fontsize=9.5, color=TUA, fontweight='bold')
ax.set_xlabel('polarisabilitas α (10$^{-30}$ m$^3$)'); ax.set_ylabel('titik didih (K)'); ax.xaxis.set_major_formatter(koma)
simpan(f, 'c_dispersi')
