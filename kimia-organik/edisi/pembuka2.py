#!/usr/bin/env python3
# Ilustrasi pembuka bab Kimia Organik 1 (gaya terang, sesuai isi bab).
# python3 edisi/pembuka2.py -> _kerja/pembuka/bNN.png, bNN.txt
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
TUA, UT, MU, EM, AB = '#143d2a', '#2e8b57', '#9fd8a8', '#e9b949', '#8a9a90'
WARNA = {'C': '#3b4a42', 'H': '#f4f6f4', 'O': '#d2553b', 'N': '#3b6fb6'}
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

# Bab 1: dua molekul C2H6O, etanol (ikatan hidrogen) dan dimetil eter
f, ax = kanvas()
et = {'C1': ('C', 0, 0), 'C2': ('C', 0.95, 0.45), 'O': ('O', 1.9, 0), 'Ho': ('H', 2.6, 0.35),
      'h1': ('H', -0.55, 0.55), 'h2': ('H', -0.5, -0.5), 'h3': ('H', 0.1, -0.75), 'h4': ('H', 0.85, 1.2), 'h5': ('H', 1.15, -0.25 + 0.95)}
et['h5'] = ('H', 1.45, 1.05)
ik = [('C1', 'C2'), ('C2', 'O'), ('O', 'Ho'), ('C1', 'h1'), ('C1', 'h2'), ('C1', 'h3'), ('C2', 'h4'), ('C2', 'h5')]
P1 = molekul(ax, et, ik, 0.9, 2.6, 0.95)
P2 = molekul(ax, et, ik, 3.6, 0.9, 0.95)
ax.plot([P1['Ho'][0] + 0.15, P2['O'][0] - 0.05], [P1['Ho'][1] - 0.15, P2['O'][1] + 0.25], color=UT, lw=2.2, ls=(0, (2, 2)), zorder=0)
ax.text(3.45, 2.75, 'ikatan hidrogen', color=UT, fontsize=10, rotation=-40, family='Liberation Sans')
eter = {'Ca': ('C', 0, 0), 'O': ('O', 0.85, 0.5), 'Cb': ('C', 1.7, 0),
        'a1': ('H', -0.6, 0.5), 'a2': ('H', -0.45, -0.55), 'a3': ('H', 0.1, -0.7), 'b1': ('H', 2.3, 0.5), 'b2': ('H', 2.15, -0.55), 'b3': ('H', 1.6, -0.7)}
ike = [('Ca', 'O'), ('O', 'Cb'), ('Ca', 'a1'), ('Ca', 'a2'), ('Ca', 'a3'), ('Cb', 'b1'), ('Cb', 'b2'), ('Cb', 'b3')]
molekul(ax, eter, ike, 5.55, 3.2, 0.95)
ax.text(1.9, 4.55, 'etanol · td 78 °C', color=TUA, fontsize=12, fontweight='bold', family='Liberation Sans')
ax.text(5.2, 4.55, 'dimetil eter · td −24 °C', color=TUA, fontsize=12, fontweight='bold', family='Liberation Sans')
ax.text(6.3, 0.75, 'C₂H₆O', color=EM, fontsize=22, fontweight='bold', family='Liberation Sans')
simpan(1, f, 'Etanol dan dimetil eter mempunyai rumus molekul yang sama, C₂H₆O. Hanya etanol yang mempunyai ikatan O–H, sehingga molekul-molekulnya saling terkait oleh ikatan hidrogen dan mendidih 102 derajat lebih tinggi.')
print('ok')
