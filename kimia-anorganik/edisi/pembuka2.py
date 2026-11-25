#!/usr/bin/env python3
# Ilustrasi pembuka bab Kimia Anorganik 1 (gaya terang, sesuai isi bab).
# python3 edisi/pembuka2.py -> _kerja/pembuka/bNN.png, bNN.txt
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
TUA, UT, MU, EM, AB = '#4a2511', '#c2611f', '#f6c79b', '#e9b949', '#8a9a90'
WARNA = {'C': '#3b4048', 'H': '#f5f6f7', 'O': '#d2553b', 'N': '#3b6fb6'}
JARI = {'C': 0.30, 'H': 0.19, 'O': 0.30, 'N': 0.30}
W, H = 8.27, 5.0
def kanvas():
    f = plt.figure(figsize=(W, H), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect('equal'); return f, ax
def simpan(n, f, cap):
    f.savefig(f'{K}/b{n:02d}.png', transparent=True); plt.close(f); open(f'{K}/b{n:02d}.txt', 'w').write(cap)
def molekul(ax, atom, ikatan, dx, dy, s=1.0):
    P = {k: (dx + s * x, dy + s * y) for k, (e, x, y) in atom.items()}
    for a, b in ikatan: ax.plot(*zip(P[a], P[b]), color=AB, lw=5 * s, solid_capstyle='round', zorder=1)
    for k, (e, x, y) in sorted(atom.items(), key=lambda t: t[1][0] == 'H'):
        r = JARI[e] * s; X, Y = P[k]
        ax.add_patch(Circle((X, Y), r, fc=WARNA[e], ec=TUA, lw=1.0, zorder=3))
        ax.add_patch(Circle((X - 0.3 * r, Y + 0.3 * r), 0.35 * r, fc='white', ec='none', alpha=0.35, zorder=4))
    return P

# Bab 1: energi ionisasi pertama H–Kr (NIST), gigi gergaji periodik
IE = [13.598, 24.587, 5.392, 9.323, 8.298, 11.260, 14.534, 13.618, 17.423, 21.565, 5.139, 7.646, 5.986, 8.152, 10.487,
      10.360, 12.968, 15.760, 4.341, 6.113, 6.561, 6.828, 6.746, 6.767, 7.434, 7.902, 7.881, 7.640, 7.726, 9.394,
      5.999, 7.899, 9.789, 9.752, 11.814, 14.000]
SIM = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr'.split()
f, ax = kanvas()
x0, x1, y0, y1 = 0.7, 7.9, 0.75, 4.2
X = [x0 + (x1 - x0) * i / 35 for i in range(36)]; Y = [y0 + (y1 - y0) * v / 25 for v in IE]
for xa, xb, c in [(X[2] - .1, X[9] + .1, '#fcefe3'), (X[18] - .1, X[35] + .1, '#fcefe3')]:
    ax.add_patch(plt.Rectangle((xa, y0 - .05), xb - xa, y1 - y0 + .1, fc=c, ec='none', zorder=0))
ax.plot(X, Y, color=UT, lw=2.2, zorder=2)
for i, (x, y) in enumerate(zip(X, Y)):
    gas = SIM[i] in ('He', 'Ne', 'Ar', 'Kr'); alk = SIM[i] in ('Li', 'Na', 'K')
    ax.scatter(x, y, s=46 if (gas or alk) else 18, color=EM if gas else (TUA if alk else UT), zorder=3, edgecolor='white', lw=.6)
    if gas or alk: ax.text(x, y + (.17 if gas else -.25), SIM[i], ha='center', fontsize=10, fontweight='bold', color=TUA, family='Liberation Sans')
ax.plot([x0, x0], [y0, y1], color=TUA, lw=1); ax.plot([x0, x1], [y0, y0], color=TUA, lw=1)
for v in (5, 10, 15, 20, 25):
    yy = y0 + (y1 - y0) * v / 25; ax.text(x0 - .1, yy, f'{v}', ha='right', va='center', fontsize=9, color=TUA, family='Liberation Sans')
ax.text(x0 - .5, (y0 + y1) / 2, 'energi ionisasi pertama (eV)', rotation=90, ha='center', va='center', fontsize=9.5, color=TUA, family='Liberation Sans')
for z in (1, 10, 18, 36):
    ax.text(X[z - 1], y0 - .22, str(z), ha='center', fontsize=9, color=TUA, family='Liberation Sans')
ax.text((x0 + x1) / 2, y0 - .5, 'nomor atom Z', ha='center', fontsize=9.5, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'pola yang berulang', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(1, f, 'Energi ionisasi pertama unsur hidrogen sampai kripton: puncak di gas mulia, lembah di logam alkali, berulang setiap periode.')
print('ok1')

# Bab 2: CH4 tetrahedron lawan XeF4 segi empat datar (empat ikatan, bentuk berbeda)
from matplotlib.patches import Ellipse
def proj(v, th=np.deg2rad(28), ph=np.deg2rad(18)):
    x, y, z = v; X = x*np.cos(th) - y*np.sin(th); Y = (x*np.sin(th) + y*np.cos(th))*np.sin(ph) + z*np.cos(ph)
    d = (x*np.sin(th) + y*np.cos(th))*np.cos(ph) - z*np.sin(ph); return X, Y, d
def gambar(ax, cx, cy, arah, pb, warna_pusat, warna_ujung, label_pusat, s=1.15):
    items = sorted([(proj(v)[2], i, proj(v)) for i, v in enumerate(arah)], reverse=True)
    for d, i, (X, Y, _) in items:
        if i in pb:
            ang = np.degrees(np.arctan2(Y, X))
            ax.add_patch(Ellipse((cx + .55*s*X, cy + .55*s*Y), .8*s, .45*s, angle=ang, fc=MU, ec=UT, lw=1.2, alpha=.85, zorder=2 if d > 0 else 4))
        else:
            ax.plot([cx, cx + s*X], [cy, cy + s*Y], color=AB, lw=5, zorder=2 if d > 0 else 4, solid_capstyle='round')
            ax.add_patch(Circle((cx + s*X, cy + s*Y), .24*s, fc=warna_ujung, ec=TUA, lw=1, zorder=3 if d > 0 else 5))
    ax.add_patch(Circle((cx, cy), .36*s, fc=warna_pusat, ec=TUA, lw=1.2, zorder=4.5))
    ax.text(cx, cy, label_pusat, ha='center', va='center', fontsize=12, fontweight='bold', color='white', zorder=6, family='Liberation Sans')
f, ax = kanvas()
TET = [(0, 0, 1), (.943, 0, -.333), (-.471, .816, -.333), (-.471, -.816, -.333)]
OKT = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
gambar(ax, 2.2, 2.35, TET, (), '#3b4048', '#f4f6f6', 'C')
gambar(ax, 6.1, 2.35, OKT, (0, 1), UT, EM, 'Xe')
ax.text(2.2, .6, 'CH₄: empat pasangan → tetrahedron', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(6.1, .6, 'XeF₄: enam pasangan → segi empat datar', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'empat ikatan, dua bentuk', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(2, f, 'Metana dan xenon tetrafluorida sama-sama mempunyai empat ikatan, tetapi xenon juga mempunyai dua pasangan elektron bebas (elips) yang ikut menentukan bentuk.')
print('ok2')

# Bab 3: cis- dan trans-[PtCl2(NH3)2] dengan pita IR Pt–Cl (dua lawan satu)
f, ax = kanvas()
def platin(cx, cy, cl, s=.95):
    arah = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for k, (ux, uy) in enumerate(arah):
        X, Y = cx + s * ux, cy + s * uy
        ax.plot([cx, X], [cy, Y], color=AB, lw=5, solid_capstyle='round', zorder=1)
        if k in cl:
            ax.add_patch(Circle((X, Y), .3, fc='#3f9a6b', ec=TUA, lw=1, zorder=3))
            ax.text(X, Y, 'Cl', ha='center', va='center', fontsize=10, fontweight='bold', color='white', zorder=4, family='Liberation Sans')
        else:
            ax.add_patch(Circle((X, Y), .27, fc=WARNA['N'], ec=TUA, lw=1, zorder=3))
            ax.text(X, Y, 'NH₃', ha='center', va='center', fontsize=7.5, fontweight='bold', color='white', zorder=4, family='Liberation Sans')
    ax.add_patch(Circle((cx, cy), .36, fc=UT, ec=TUA, lw=1.2, zorder=4.5))
    ax.text(cx, cy, 'Pt', ha='center', va='center', fontsize=12, fontweight='bold', color='white', zorder=6, family='Liberation Sans')
def pita(cx, y0, pus):
    x = np.linspace(-1.3, 1.3, 400); T = np.ones_like(x)
    for p in pus: T -= .8 * np.exp(-((x - p) / .07) ** 2)
    ax.plot(cx + x, y0 + .7 * T, color=UT, lw=2)
    ax.plot([cx - 1.3, cx + 1.3], [y0 - .05, y0 - .05], color=TUA, lw=.8)
platin(2.2, 2.85, (0, 1)); platin(6.1, 2.85, (0, 2))
pita(2.2, .75, (-.22, .22)); pita(6.1, .75, (0,))
ax.text(2.2, .35, 'cis: dua pita Pt–Cl', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(6.1, .35, 'trans: satu pita Pt–Cl', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'rumus sama, simetri berbeda', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(3, f, 'Cisplatin (kiri) dan transplatin (kanan) mempunyai rumus yang sama. Simetrinya yang berbeda meramalkan dua pita regangan Pt–Cl di inframerah untuk isomer cis dan hanya satu untuk isomer trans.')
print('ok3')

# Bab 4: oksigen cair menempel di antara kutub magnet + dua elektron π* sejajar
from matplotlib.patches import Rectangle, FancyBboxPatch
f, ax = kanvas()
for x0, c, t in [(1.0, '#c9503c', 'U'), (3.3, '#3b6fb6', 'S')]:
    ax.add_patch(FancyBboxPatch((x0, 1.0), 1.2, 2.6, boxstyle='round,pad=0.02,rounding_size=0.12', fc=c, ec=TUA, lw=1.2))
    ax.text(x0 + .6, 3.2, t, ha='center', va='center', fontsize=16, fontweight='bold', color='white', family='Liberation Sans')
# jembatan oksigen cair (biru pucat) di celah
xs = np.linspace(2.2, 3.3, 50); top = 2.35 + .06 * np.sin(np.linspace(0, 3 * np.pi, 50)); bot = 1.85 - .05 * np.cos(np.linspace(0, 2 * np.pi, 50))
ax.fill_between(xs, bot, top, color='#a9cdf0', ec='#6a9fd0', lw=1, zorder=3)
for k in range(5): ax.add_patch(Circle((2.35 + .22 * k, 1.75 - .25 * (k % 2) - .15), .05, fc='#a9cdf0', ec='#6a9fd0', zorder=3))
ax.text(2.75, .55, 'O₂ cair tertahan magnet', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
# diagram pi*
for xc in (5.9, 7.0):
    ax.plot([xc - .35, xc + .35], [3.0, 3.0], color=TUA, lw=2.5)
    ax.annotate('', (xc, 3.45), (xc, 2.65), arrowprops=dict(arrowstyle='-|>', color=UT, lw=2, mutation_scale=16))
for xc in (5.9, 7.0):
    ax.plot([xc - .35, xc + .35], [1.6, 1.6], color=TUA, lw=2.5)
    for d, (a, b) in zip((-.09, .09), ((1.25, 2.0), (1.95, 1.2))):
        ax.annotate('', (xc + d, b), (xc + d, a), arrowprops=dict(arrowstyle='-|>', color=AB, lw=1.6, mutation_scale=12))
ax.text(7.55, 3.0, 'π*', va='center', fontsize=14, color=TUA, family='Liberation Sans')
ax.text(7.55, 1.6, 'π', va='center', fontsize=14, color=TUA, family='Liberation Sans')
ax.text(6.45, .55, 'dua elektron sejajar', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'elektron yang tidak berpasangan', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(4, f, 'Oksigen cair menggantung di antara kutub magnet karena dua elektron terakhirnya menempati dua orbital π* yang setara dengan spin sejajar, sesuatu yang tidak dapat ditunjukkan struktur Lewis.')
print('ok4')
