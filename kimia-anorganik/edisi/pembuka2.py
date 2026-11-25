#!/usr/bin/env python3
# Ilustrasi pembuka bab Kimia Anorganik 1 (gaya terang, sesuai isi bab).
# python3 edisi/pembuka2.py -> _kerja/pembuka/bNN.png, bNN.txt
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
TUA, UT, MU, EM, AB = '#0f3b40', '#1f8a8a', '#a8dede', '#e9a86b', '#8a9a9a'
WARNA = {'C': '#3b4a4b', 'H': '#f4f6f6', 'O': '#d2553b', 'N': '#3b6fb6'}
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
for xa, xb, c in [(X[2] - .1, X[9] + .1, '#e3f3f3'), (X[18] - .1, X[35] + .1, '#e3f3f3')]:
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
