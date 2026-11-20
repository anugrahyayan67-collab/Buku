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

# 2 pencairan gas di bawah piston dan isoterm gas nyata dengan kubah dua fasa
f, ax = kanvas(); rng = np.random.default_rng(3)
ax.add_patch(Rectangle((0.55, 0.45), 2.9, 3.6, fc='white', ec=NI, lw=2.2, zorder=1, alpha=0.9))
ax.add_patch(Rectangle((0.6, 3.25), 2.8, 0.32, color=AB, zorder=3)); ax.add_patch(Rectangle((1.85, 3.57), 0.3, 1.1, color=AB, zorder=3))
ax.add_patch(Rectangle((0.6, 0.5), 2.8, 1.05, color=SI, alpha=0.35, zorder=1, lw=0))
for _ in range(9):
    x, y = rng.uniform(0.85, 3.15), rng.uniform(1.85, 3.0); bola(ax, x, y, 0.1, UN, z=4)
for i in range(13):
    for j in range(4):
        bola(ax, 0.78 + i * 0.205 + (j % 2) * 0.1, 0.66 + j * 0.2 + rng.uniform(-0.02, 0.02), 0.095, NI if (i + j) % 3 else UN, z=4)
def brentq(f, a, b):
    fa = f(a)
    for _ in range(80):
        c = (a + b) / 2; fc = f(c)
        if fa * fc <= 0: b = c
        else: a, fa = c, fc
    return (a + b) / 2
def maxwell(Tr):
    P = lambda v: 8 * Tr / (3 * v - 1) - 3 / v ** 2
    def akar(p):
        r = np.roots([3 * p, -(p + 8 * Tr), 9, -3]); r = sorted(x.real for x in r if abs(x.imag) < 1e-9 and x.real > 1 / 3); return r[0], r[-1]
    def selisih(p):
        vl, vg = akar(p); vv = np.linspace(vl, vg, 2000); return np.trapezoid(P(vv) - p, vv)
    ps = np.linspace(0.02, 0.999, 400); ok = [p for p in ps if len([x for x in np.roots([3 * p, -(p + 8 * Tr), 9, -3]) if abs(x.imag) < 1e-9 and x.real > 1 / 3]) == 3]
    p = brentq(selisih, min(ok) + 1e-6, max(ok) - 1e-6); return (p,) + akar(p)
V = np.linspace(0.4, 3.2, 600); x0 = 4.75; sx, sy = 1.1, 1.75
X = lambda v: x0 + (v - 0.4) * sx; Y = lambda p: 0.6 + p * sy
kub = []
for Tr in np.linspace(0.86, 0.99, 25): kub.append(maxwell(Tr))
kub = np.array(kub); ax.plot(X(np.r_[kub[:, 1], kub[::-1, 2]]), Y(np.r_[kub[:, 0], kub[::-1, 0]]), color=AB, lw=1.2, ls='--')
for Tr, c in [(0.85, NI), (0.93, UN), (1.0, EM), (1.15, SI)]:
    pr = 8 * Tr / (3 * V - 1) - 3 / V ** 2
    if Tr < 1:
        pv, vl, vg = maxwell(Tr); m1 = (V <= vl) & (pr < 2.0); m2 = V >= vg
        ax.plot(X(V[m1]), Y(pr[m1]), color=c, lw=2.4); ax.plot(X(V[m2]), Y(pr[m2]), color=c, lw=2.4); ax.plot([X(vl), X(vg)], [Y(pv)] * 2, color=c, lw=2.4)
    else:
        m = pr < 2.0; ax.plot(X(V[m]), Y(pr[m]), color=c, lw=2.8 if Tr == 1 else 2.4)
ax.plot([x0, 8.1], [0.6, 0.6], color=AB, lw=1.2); ax.plot([x0, x0], [0.6, 4.4], color=AB, lw=1.2)
simpan(2, f, 'Gas yang ditekan di bawah suhu kritisnya mencair; isotermnya mendatar selama gas dan cairan hidup berdampingan.')

# 3 kalor masuk dari bawah, kerja keluar lewat piston; isoterm dan adiabat
f, ax = kanvas(); rng = np.random.default_rng(11)
ax.add_patch(Rectangle((0.7, 1.1), 2.6, 3.0, fc='white', ec=NI, lw=2.2, zorder=1, alpha=0.9))
ax.add_patch(Rectangle((0.75, 3.0), 2.5, 0.3, color=AB, zorder=3)); ax.add_patch(Rectangle((1.85, 3.3), 0.3, 1.2, color=AB, zorder=3))
ax.annotate('', xy=(2.0, 4.85), xytext=(2.0, 4.5), arrowprops=dict(arrowstyle='-|>', color=UN, lw=3, mutation_scale=18))
for _ in range(16):
    x, y = rng.uniform(0.95, 3.05), rng.uniform(1.3, 2.8); bola(ax, x, y, 0.09, UN if rng.random() < .5 else SI, z=4)
for k, x in enumerate(np.linspace(1.0, 3.0, 6)):
    t = np.linspace(0, 1, 50); ax.plot(x + 0.08 * np.sin(t * 14), 0.3 + 0.65 * t, color=EM if k % 2 else UN, lw=2.2)
x = np.linspace(4.6, 8.0, 300); V = (x - 4.3) / 0.85
ax.plot(x, 0.7 + 3.2 / V, color=UN, lw=2.6); ax.plot(x, 0.7 + 3.2 / V ** (5 / 3), color=EM, lw=2.6)
ax.fill_between(x, 0.7, 0.7 + 3.2 / V, color=SI, alpha=0.18, lw=0)
ax.plot([4.5, 8.1], [0.7, 0.7], color=AB, lw=1.2); ax.plot([4.5, 4.5], [0.7, 4.5], color=AB, lw=1.2)
simpan(3, f, 'Energi dalam gas berubah lewat dua pintu: kalor yang masuk dari bawah dan kerja yang keluar mendorong piston.')

# 4 bom kalorimeter dan tangga entalpi
f, ax = kanvas()
ax.add_patch(FancyBboxPatch((0.5, 0.5), 3.2, 3.3, boxstyle='round,pad=0,rounding_size=0.15', fc='white', ec=NI, lw=2.2, alpha=0.9, zorder=1))
ax.add_patch(Rectangle((0.62, 0.62), 2.96, 2.6, color='#bfe0f2', alpha=0.6, zorder=1, lw=0))
ax.add_patch(FancyBboxPatch((1.45, 0.95), 1.3, 1.75, boxstyle='round,pad=0,rounding_size=0.12', fc=AB, ec=NI, lw=1.6, zorder=3))
for k, a2 in [(0.55, .25), (0.38, .5), (0.22, 1)]: ax.add_patch(Circle((2.1, 1.65), k, color=SI if k > 0.3 else EM, alpha=a2, zorder=4, lw=0))
ax.add_patch(Rectangle((3.05, 2.2), 0.12, 2.3, color='white', ec=NI, lw=1.2, zorder=5)); ax.add_patch(Rectangle((3.07, 2.25), 0.08, 1.4, color=UN, zorder=6))
ax.add_patch(Circle((3.11, 2.2), 0.13, color=UN, zorder=6))
lv = [(4.2, 'C + O₂'), (3.2, 'CO + ½O₂'), (1.0, 'CO₂')]
for y, t in lv: ax.plot([4.6 if y != 3.2 else 6.2, 6.0 if y != 3.2 else 7.9], [y, y], color=NI, lw=3)
ax.plot([6.2, 7.9], [1.0, 1.0], color=NI, lw=3)
for (x, y0, y1, c) in [(5.0, 4.2, 1.05, UN), (6.6, 4.2, 3.25, SI), (7.4, 3.2, 1.05, EM)]:
    ax.annotate('', xy=(x, y1), xytext=(x, y0), arrowprops=dict(arrowstyle='-|>', color=c, lw=3, mutation_scale=18))
ax.plot([6.0, 6.6], [4.2, 4.2], color=NI, lw=3)
simpan(4, f, 'Bom kalorimeter mengukur kalor pembakaran; karena entalpi fungsi keadaan, langkah-langkah reaksi dapat dijumlahkan.')
