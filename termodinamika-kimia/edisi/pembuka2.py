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

# 5 mesin kalor: sumber panas, mesin, penampung dingin; dan molekul yang menyebar
f, ax = kanvas()
ax.add_patch(FancyBboxPatch((0.5, 3.6), 3.0, 0.9, boxstyle='round,pad=0,rounding_size=0.12', fc=UN, ec=NI, lw=1.6, alpha=0.9))
ax.add_patch(FancyBboxPatch((0.5, 0.4), 3.0, 0.9, boxstyle='round,pad=0,rounding_size=0.12', fc='#bfe0f2', ec=NI, lw=1.6))
ax.add_patch(Circle((2.0, 2.45), 0.55, fc='white', ec=NI, lw=2.2))
for a in np.linspace(0, 2 * np.pi, 7)[:-1]: ax.plot([2.0, 2.0 + 0.45 * np.cos(a)], [2.45, 2.45 + 0.45 * np.sin(a)], color=NI, lw=1.6)
ax.annotate('', xy=(2.0, 3.02), xytext=(2.0, 3.58), arrowprops=dict(arrowstyle='-|>', color=UN, lw=4, mutation_scale=18))
ax.annotate('', xy=(2.0, 1.32), xytext=(2.0, 1.88), arrowprops=dict(arrowstyle='-|>', color=SI, lw=2.6, mutation_scale=16))
ax.annotate('', xy=(3.5, 2.45), xytext=(2.6, 2.45), arrowprops=dict(arrowstyle='-|>', color=EM, lw=3.2, mutation_scale=18))
rng = np.random.default_rng(5)
ax.add_patch(Rectangle((4.6, 0.8), 3.3, 3.4, fc='white', ec=NI, lw=2, alpha=0.9)); ax.plot([6.25, 6.25], [0.8, 4.2], color=AB, lw=1.2, ls='--')
for _ in range(26):
    x, y = rng.uniform(4.8, 7.7), rng.uniform(1.0, 4.0); bola(ax, x, y, 0.09, UN if x < 6.25 else SI, z=4)
simpan(5, f, 'Mesin kalor selalu membuang sebagian kalornya; molekul selalu menyebar. Keduanya diatur oleh hukum yang sama: entropi semesta bertambah.')

# 6 kristal sempurna pada 0 K, cairan, gas, dan tangga entropi
f, ax = kanvas(); rng = np.random.default_rng(9)
for i in range(5):
    for j in range(5): bola(ax, 0.55 + i * 0.3, 1.0 + j * 0.3, 0.12, NI, z=3)
for _ in range(14): bola(ax, rng.uniform(2.35, 3.25), rng.uniform(0.95, 2.1), 0.12, UN, z=3)
for _ in range(7): bola(ax, rng.uniform(3.7, 4.6), rng.uniform(0.9, 3.0), 0.12, SI, z=3)
T = np.linspace(0.02, 1, 100); x0 = 5.0
ax.plot(x0 + T * 0.9, 0.7 + 1.0 * T ** 2, color=NI, lw=2.8); ax.plot([x0 + 0.9] * 2, [1.7, 2.2], color=EM, lw=2, ls='--')
ax.plot([x0 + 0.9, x0 + 1.2], [2.2, 2.3], color=UN, lw=2.8); ax.plot([x0 + 1.2] * 2, [2.3, 3.6], color=EM, lw=2, ls='--')
T2 = np.linspace(0, 1, 50); ax.plot(x0 + 1.2 + T2 * 1.8, 3.6 + 0.6 * np.log1p(2 * T2), color=SI, lw=2.8)
ax.plot([x0 - 0.1, 8.1], [0.7, 0.7], color=AB, lw=1.2); ax.plot([x0 - 0.1, x0 - 0.1], [0.7, 4.6], color=AB, lw=1.2)
simpan(6, f, 'Kristal sempurna pada nol mutlak mempunyai entropi nol; entropi naik perlahan saat dipanaskan dan melompat pada peleburan dan penguapan.')

# 7 sel bahan bakar dan jaringan hubungan U, H, A, G
f, ax = kanvas()
ax.add_patch(FancyBboxPatch((0.5, 0.8), 3.4, 3.2, boxstyle='round,pad=0,rounding_size=0.15', fc='white', ec=NI, lw=2.2, alpha=0.9))
ax.add_patch(Rectangle((1.1, 1.0), 0.35, 2.6, color=AB)); ax.add_patch(Rectangle((2.95, 1.0), 0.35, 2.6, color=AB))
ax.add_patch(Rectangle((1.45, 1.0), 1.5, 2.6, color='#bfe0f2', alpha=0.6))
for y in np.linspace(1.3, 3.3, 5): bola(ax, 0.8, y, 0.09, '#f4f4f6', z=4); bola(ax, 3.6, y, 0.1, UN, z=4)
ax.plot([1.27, 1.27, 3.12, 3.12], [3.6, 4.5, 4.5, 3.6], color=NI, lw=2)
ax.add_patch(Circle((2.2, 4.5), 0.25, fc=EM, ec=NI, lw=1.5, zorder=5))
pos = {'U': (5.2, 3.8), 'H': (7.4, 3.8), 'A': (5.2, 1.3), 'G': (7.4, 1.3)}
for k, (x, y) in pos.items():
    ax.add_patch(Circle((x, y), 0.45, fc=SI if k == 'G' else 'white', ec=NI, lw=2.2, zorder=3))
    ax.text(x, y, k, ha='center', va='center', fontsize=22, color=NI, fontweight='bold', zorder=4)
for a, b in [('U', 'H'), ('U', 'A'), ('H', 'G'), ('A', 'G')]:
    (x1, y1), (x2, y2) = pos[a], pos[b]; ax.plot([x1 + 0.5 * np.sign(x2 - x1), x2 - 0.5 * np.sign(x2 - x1)], [y1 + 0.5 * np.sign(y2 - y1), y2 - 0.5 * np.sign(y2 - y1)], color=UN, lw=2.4)
simpan(7, f, 'Sel bahan bakar mengubah energi Gibbs langsung menjadi kerja listrik; U, H, A, dan G terhubung oleh jaringan persamaan fundamental.')

# 8 gunung dan panci, serta diagram fasa dengan titik tripel dan titik kritis
f, ax = kanvas(); rng = np.random.default_rng(8)
ax.fill([0.3, 1.6, 2.2, 2.9, 4.2], [0.6, 3.6, 3.0, 4.3, 0.6], color=AB, alpha=0.35, lw=0)
ax.fill([2.55, 2.9, 3.25], [3.8, 4.3, 3.8], color='white', alpha=0.9, lw=0)
ax.add_patch(Rectangle((1.0, 0.65), 1.6, 0.95, fc=NI, ec=NI, lw=1.5, zorder=3)); ax.add_patch(Rectangle((0.9, 1.6), 1.8, 0.12, color=UN, zorder=3))
for _ in range(9):
    x = rng.uniform(1.2, 2.4); t = np.linspace(0, 1, 30); ax.plot(x + 0.08 * np.sin(t * 9 + x * 5), 1.85 + 0.9 * t, color=SI, lw=1.8, alpha=0.8)
for _ in range(6): bola(ax, rng.uniform(1.15, 2.45), rng.uniform(0.8, 1.45), 0.07, SI, z=4)
x0, y0 = 4.9, 0.7; ax.plot([x0, 8.1], [y0, y0], color=AB, lw=1.2); ax.plot([x0, x0], [y0, 4.6], color=AB, lw=1.2)
tt, pt, tc, pc = x0 + 1.1, y0 + 1.1, x0 + 2.9, y0 + 3.2
t = np.linspace(0, 1, 100)
ax.plot(tt + (tc - tt) * t, pt + (pc - pt) * t ** 1.6, color=UN, lw=3)
ax.plot(x0 + 0.1 + (tt - x0 - 0.1) * t, y0 + 0.05 + (pt - y0 - 0.05) * t ** 2, color=NI, lw=3)
ax.plot(tt - 0.25 * t, pt + 3.0 * t, color=NI, lw=3)
ax.fill_between(tt + (tc - tt) * t, pt + (pc - pt) * t ** 1.6, 4.6, color=SI, alpha=0.18, lw=0)
for (x, y), c in [((tt, pt), EM), ((tc, pc), UN)]: ax.add_patch(Circle((x, y), 0.13, fc=c, ec=NI, lw=1.5, zorder=5))
ax.add_patch(Circle((tc, pc), 0.32, fc=EM, alpha=0.25, lw=0, zorder=4))
simpan(8, f, 'Titik didih air turun di puncak gunung; diagram fasa memetakan di mana padat, cair, dan gas stabil, dari titik tripel sampai titik kritis.')

# 9 dua gelas ukur yang dicampur dan lereng potensial kimia
f, ax = kanvas(); rng = np.random.default_rng(9)
def gelas(x, w, h, isi, c):
    ax.add_patch(Rectangle((x, 0.6), w, h, fc='white', ec=NI, lw=2, alpha=0.9, zorder=2))
    ax.add_patch(Rectangle((x + 0.04, 0.64), w - 0.08, isi, color=c, alpha=0.45, zorder=3, lw=0))
    for k in range(1, 6): ax.plot([x, x + 0.15], [0.6 + k * h / 6] * 2, color=NI, lw=1, zorder=4)
gelas(0.4, 0.75, 2.6, 1.3, SI); gelas(1.45, 0.75, 2.6, 1.3, UN); gelas(2.7, 0.95, 3.4, 2.5, EM)
ax.plot([0.4, 3.65], [0.64 + 2.6, 0.64 + 2.6], color=UN, lw=1.4, ls='--', zorder=5)
ax.annotate('', xy=(2.65, 2.4), xytext=(2.25, 2.4), arrowprops=dict(arrowstyle='-|>', color=NI, lw=2, mutation_scale=14))
for _ in range(16): bola(ax, rng.uniform(2.85, 3.5), rng.uniform(0.8, 3.0), 0.07, SI if rng.random() < .5 else UN, z=5)
x = np.linspace(4.6, 8.0, 200); y = 1.0 + 2.8 / (1 + np.exp(4 * (x - 6.3)))
ax.plot(x, y, color=NI, lw=3); ax.fill_between(x, 0.7, y, color=SI, alpha=0.18, lw=0)
for xx, c in [(5.0, UN), (5.9, UN), (6.7, SI), (7.5, SI)]:
    yy = 1.0 + 2.8 / (1 + np.exp(4 * (xx - 6.3))); bola(ax, xx, yy + 0.2, 0.17, c, z=5)
ax.annotate('', xy=(7.2, 1.6), xytext=(5.6, 3.7), arrowprops=dict(arrowstyle='-|>', color=UN, lw=2.2, mutation_scale=16))
simpan(9, f, 'Dua volume yang dicampur tidak selalu menjumlah; setiap zat bergerak menuruni lereng potensial kimianya sendiri.')

# 10 tabung-U osmosis dan sel darah merah
f, ax = kanvas(); rng = np.random.default_rng(10)
xl, xr, w = 1.0, 2.9, 0.75
for x, h in [(xl, 2.3), (xr, 3.4)]:
    ax.add_patch(Rectangle((x, 0.9), w, 3.2, fc='white', ec=NI, lw=2, alpha=0.9, zorder=2))
    ax.add_patch(Rectangle((x + 0.04, 0.94), w - 0.08, h - 0.94, color='#bfe0f2' if x == xl else SI, alpha=0.55, zorder=3, lw=0))
ax.add_patch(Rectangle((xl, 0.55), xr + w - xl, 0.4, fc='white', ec=NI, lw=2, zorder=2)); ax.add_patch(Rectangle((xl + 0.04, 0.59), xr + w - xl - 0.08, 0.36, color='#bfe0f2', alpha=0.55, zorder=3, lw=0))
ax.plot([2.3, 2.3], [0.57, 0.93], color=UN, lw=3, ls=(0, (2, 1.5)), zorder=5)
for _ in range(10): bola(ax, rng.uniform(xr + 0.12, xr + w - 0.12), rng.uniform(1.1, 3.2), 0.07, UN, z=5)
ax.annotate('', xy=(xr - 0.05, 2.0), xytext=(xl + w + 0.1, 1.5), arrowprops=dict(arrowstyle='-|>', color=NI, lw=2, connectionstyle='arc3,rad=-0.3', mutation_scale=14))
ax.plot([xr, xr + w], [3.4, 3.4], color=NI, lw=1); ax.annotate('', xy=(xr + w + 0.2, 3.4), xytext=(xr + w + 0.2, 2.3), arrowprops=dict(arrowstyle='<->', color=EM, lw=1.8))
for (x, y, r, c) in [(5.6, 3.3, 0.55, UN), (7.2, 3.3, 0.72, UN), (5.6, 1.5, 0.48, '#d97b5f'), (7.2, 1.45, 0.62, UN)]:
    ax.add_patch(Circle((x, y), r, fc=c, ec=NI, lw=1.5, alpha=0.85, zorder=3)); ax.add_patch(Circle((x, y), r * 0.45, fc='white', alpha=0.25, zorder=4, lw=0))
ax.annotate('', xy=(6.45, 3.3), xytext=(6.2, 3.3), arrowprops=dict(arrowstyle='-|>', color=AB, lw=1.6))
simpan(10, f, 'Pelarut mengalir melewati membran ke larutan yang lebih pekat; sel darah merah menggembung atau mengerut mengikuti tekanan osmotik.')

# 11 kolom distilasi dan diagram suhu-komposisi
f, ax = kanvas(); rng = np.random.default_rng(11)
ax.add_patch(FancyBboxPatch((1.4, 0.5), 1.1, 4.1, boxstyle='round,pad=0,rounding_size=0.25', fc='white', ec=NI, lw=2.2, alpha=0.9, zorder=2))
for k, y in enumerate(np.linspace(0.95, 4.1, 8)):
    ax.plot([1.45, 2.45], [y, y], color=NI, lw=1.5, zorder=3)
    c = [UN, UN, '#c9603f', SI, SI, EM, EM, EM][k]
    ax.add_patch(Rectangle((1.47, y), 0.96, 0.1, color=c, alpha=0.6, zorder=3, lw=0))
    for _ in range(3): bola(ax, rng.uniform(1.6, 2.3), y + rng.uniform(0.18, 0.3), 0.045, c, z=4)
ax.plot([2.5, 3.3, 3.3], [4.3, 4.3, 3.6], color=NI, lw=2); ax.add_patch(Rectangle((3.15, 3.0), 0.3, 0.6, fc=EM, ec=NI, lw=1.5, alpha=0.8))
ax.add_patch(Circle((1.95, 0.55), 0.0, color=NI))
x0, y0 = 4.6, 0.7; ax.plot([x0, 8.0], [y0, y0], color=AB, lw=1.2); ax.plot([x0, x0], [y0, 4.6], color=AB, lw=1.2); ax.plot([8.0, 8.0], [y0, 4.6], color=AB, lw=1.2)
t = np.linspace(0, 1, 100); X = x0 + 3.4 * t
lo = 4.2 - 3.0 * t - 0.45 * np.sin(np.pi * t); hi = 4.2 - 3.0 * t + 0.45 * np.sin(np.pi * t)
ax.plot(X, lo, color=UN, lw=3); ax.plot(X, hi, color=SI, lw=3); ax.fill_between(X, lo, hi, color=SI, alpha=0.15, lw=0)
xx = 0.15
for i in range(4):
    yl = 4.2 - 3.0 * xx - 0.45 * np.sin(np.pi * xx)
    xv = solve_x = None
    tt = np.linspace(xx, 1, 400); hh = 4.2 - 3.0 * tt + 0.45 * np.sin(np.pi * tt); j = np.argmin(abs(hh - yl)); xv = tt[j]
    ax.plot([x0 + 3.4 * xx, x0 + 3.4 * xv], [yl, yl], color=NI, lw=1.6); yl2 = 4.2 - 3.0 * xv - 0.45 * np.sin(np.pi * xv)
    ax.plot([x0 + 3.4 * xv] * 2, [yl, yl2], color=NI, lw=1.6); xx = xv
simpan(11, f, 'Kolom distilasi melakukan langkah-langkah penguapan dan pengembunan berulang; setiap langkah adalah satu anak tangga pada diagram suhu–komposisi.')

# 12 lembah energi Gibbs dan labu N2O4/NO2
f, ax = kanvas(); rng = np.random.default_rng(12)
for k, (x0, a) in enumerate([(0.6, 0.25), (2.2, 0.6), (3.8, 0.95)]):
    ax.add_patch(Circle((x0 + 0.55, 1.6), 0.55, fc='white', ec=NI, lw=2, alpha=0.9, zorder=2))
    ax.add_patch(Rectangle((x0 + 0.45, 2.1), 0.2, 0.5, fc='white', ec=NI, lw=2, zorder=2))
    ax.add_patch(Circle((x0 + 0.55, 1.6), 0.5, color='#a0522d', alpha=a * 0.6, zorder=3, lw=0))
    for _ in range(6): bola(ax, x0 + 0.55 + rng.uniform(-0.3, 0.3), 1.6 + rng.uniform(-0.3, 0.3), 0.05, UN if rng.random() < a else SI, z=4)
xi = np.linspace(0.005, 0.995, 300); G = 1.0 * xi + 0.9 * (xi * np.log(xi) + (1 - xi) * np.log(1 - xi))
X = 4.9 + 3.0 * xi; Y = 2.6 + 2.2 * G
ax.plot(X, Y, color=NI, lw=3); ax.fill_between(X, 0.7, Y, color=SI, alpha=0.15, lw=0)
i = np.argmin(G); bola(ax, X[i], Y[i] + 0.16, 0.16, EM, z=5)
ax.plot([4.9, 7.9], [0.7, 0.7], color=AB, lw=1.2)
simpan(12, f, 'Campuran N₂O₄ dan NO₂ makin cokelat ketika dipanaskan; kesetimbangan terletak di dasar lembah energi Gibbs.')

# 13 sel Daniell dan baterai
f, ax = kanvas(); rng = np.random.default_rng(13)
for x0, c, cl in [(0.5, '#9aa3ab', '#bfe0f2'), (2.7, UN, '#8cc0e8')]:
    ax.add_patch(Rectangle((x0, 0.6), 1.6, 2.2, fc='white', ec=NI, lw=2, alpha=0.9, zorder=2))
    ax.add_patch(Rectangle((x0 + 0.04, 0.64), 1.52, 1.6, color=cl, alpha=0.6, zorder=3, lw=0))
    ax.add_patch(Rectangle((x0 + 0.6, 1.0), 0.4, 2.6, color=c, ec=NI, lw=1.4, zorder=4))
ax.plot([1.85, 1.85, 3.35, 3.35], [1.6, 3.2, 3.2, 1.6], color='#dcc9a0', lw=9, zorder=1, solid_capstyle='butt')
ax.plot([1.3, 1.3, 3.5, 3.5], [3.6, 4.4, 4.4, 3.6], color=NI, lw=2)
ax.add_patch(Circle((2.4, 4.4), 0.32, fc=EM, ec=NI, lw=1.8, zorder=5))
for k in range(5): bola(ax, 1.5 + k * 0.45, 4.62, 0.06, SI, z=6)
for i, (x, h) in enumerate([(5.0, 2.6), (6.1, 3.2), (7.2, 3.8)]):
    ax.add_patch(FancyBboxPatch((x, 0.7), 0.8, h, boxstyle='round,pad=0,rounding_size=0.08', fc=[SI, UN, NI][i], ec=NI, lw=1.6, alpha=0.85))
    ax.add_patch(Rectangle((x + 0.25, 0.7 + h), 0.3, 0.15, color=NI))
    for j in range(int(h / 0.45)): ax.add_patch(Rectangle((x + 0.15, 0.9 + j * 0.45), 0.5, 0.22, color='white', alpha=0.35, lw=0))
simpan(13, f, 'Sel Daniell mengubah energi Gibbs reaksi seng–tembaga menjadi listrik; baterai modern mengemas prinsip yang sama dengan energi spesifik makin besar.')

# 14 tangga tingkat energi dengan populasi Boltzmann pada tiga suhu
f, ax = kanvas(); rng = np.random.default_rng(14)
for k, (x0, b) in enumerate([(0.5, 1.6), (2.9, 0.75), (5.3, 0.3)]):
    p = np.exp(-b * np.arange(8)); p = p / p.sum(); n = np.round(p * 26).astype(int)
    for j in range(8):
        y = 0.7 + j * 0.5
        ax.plot([x0, x0 + 2.0], [y, y], color=NI, lw=1.8, zorder=2)
        for m in range(min(n[j], 10)): bola(ax, x0 + 0.15 + m * 0.19, y + 0.11, 0.085, [NI, UN, SI][k], z=4)
    ax.plot(x0 + 2.1 + 0.6 * p / p.max() * np.exp(0), 0.7 + np.arange(8) * 0.5, color=EM, lw=0)
yy = np.linspace(0, 3.5, 200)
for k, (x0, b) in enumerate([(0.5, 1.6), (2.9, 0.75), (5.3, 0.3)]):
    ax.plot(x0 + 1.95 * np.exp(-b * yy / 0.5) + 0.05, 0.7 + yy, color=EM, lw=2.2, alpha=0.8, zorder=3)
ax.add_patch(Rectangle((0.5, 0.35), 6.8, 0.08, color=AB, lw=0))
simpan(14, f, 'Molekul tersebar di antara tingkat-tingkat energi menurut faktor Boltzmann; ketika suhu naik, populasi merambat ke tingkat yang lebih tinggi.')
