#!/usr/bin/env python3
# Ilustrasi pembuka bab Termodinamika Kimia (gaya terang, sesuai isi bab).
# python3 edisi/pembuka2.py -> _kerja/pembuka/bNN.png, bNN.txt
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
NI, UN, SI, EM, AB = '#3d1418', '#b4442b', '#f4a261', '#d9a22b', '#9c8580'
W, H = 8.27, 5.0
def kanvas():
    f = plt.figure(figsize=(W, H), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, W); ax.set_ylim(0, H); return f, ax
def bola(ax, x, y, r, c, z=3):
    ax.add_patch(Circle((x, y), r, color=c, zorder=z, ec=NI, lw=0.5))
    for k in range(5): ax.add_patch(Circle((x - r * 0.3 * (k + 1) / 5, y + r * 0.3 * (k + 1) / 5), r * (1 - (k + 1) / 6), color='white', alpha=0.08, zorder=z, lw=0))
def simpan(n, f, cap):
    f.savefig(f'{K}/b{n:02d}.png', transparent=True); plt.close(f); open(f'{K}/b{n:02d}.txt', 'w').write(cap)

# 1 molekul gas di dalam wadah dan sebaran Maxwell–Boltzmann
f, ax = kanvas(); rng = np.random.default_rng(7)
ax.add_patch(FancyBboxPatch((0.45, 0.45), 3.6, 4.1, boxstyle='round,pad=0,rounding_size=0.12', fc='white', ec=NI, lw=2.2, alpha=0.9, zorder=1))
ax.add_patch(Rectangle((0.45, 4.55), 3.6, 0.18, color=AB, zorder=2))
for _ in range(34):
    x, y = rng.uniform(0.75, 3.75), rng.uniform(0.75, 4.25); th = rng.uniform(0, 2 * np.pi); v = rng.rayleigh(0.32)
    c = [SI, UN, NI][min(2, int(v / 0.3))]
    ex, ey = x + v * np.cos(th), y + v * np.sin(th)
    if not (0.6 < ex < 3.9 and 0.6 < ey < 4.4): th += np.pi
    ax.annotate('', xy=(x + v * np.cos(th), y + v * np.sin(th)), xytext=(x, y), arrowprops=dict(arrowstyle='-|>', color=AB, lw=1.0, mutation_scale=7), zorder=3)
    bola(ax, x, y, 0.1, c, z=4)
v = np.linspace(0, 4, 400)
for T, c in [(1.0, NI), (2.2, UN), (4.0, SI)]:
    fv = v ** 2 * np.exp(-v ** 2 / T) / T ** 1.5; ax.plot(4.7 + v * 0.85, 0.7 + 3.5 * fv / 0.37, color=c, lw=2.6)
ax.plot([4.7, 8.1], [0.7, 0.7], color=AB, lw=1.2); ax.plot([4.7, 4.7], [0.7, 4.4], color=AB, lw=1.2)
simpan(1, f, 'Molekul gas bergerak acak dengan kelajuan yang beragam; sebaran kelajuannya melebar ketika gas dipanaskan.')
