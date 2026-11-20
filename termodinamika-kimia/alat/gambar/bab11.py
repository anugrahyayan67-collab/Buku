# Gambar Bab 11: python3 alat/gambar/bab11.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab11', 'fig')
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
R = 8.314; P = 101.325
ant = lambda A, B, C: (lambda t: 10 ** (A - B / (t + C)) * 0.133322)
bz, tl = ant(6.90565, 1211.033, 220.790), ant(6.95464, 1344.8, 219.482)
et, wa = ant(8.20417, 1642.89, 230.300), ant(8.07131, 1730.63, 233.426)
def solve(f, a, b):
    for _ in range(80):
        c = (a + b) / 2
        if f(a) * f(c) <= 0: b = c
        else: a = c
    return c
def simpan(f, n): f.tight_layout(); f.savefig(f'{D}/{n}.png'); plt.close(f)
def sumbu(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
# 11.1 diagram p-x-y benzena-toluena 25 °C
pB, pT = 12.7, 3.79; x = np.linspace(0, 1, 200)
f, ax = plt.subplots(figsize=(5.2, 3.7), dpi=220)
ax.plot(x, pT + (pB - pT) * x, color=BIRU, lw=2.4); ax.plot(x, pB * pT / (pB - (pB - pT) * x), color=JT, lw=2.4)
xl, yv, p0 = 0.248, 0.525, 6.0
ax.plot([xl, yv], [p0, p0], color=TUA, lw=1.4); ax.plot([0.4], [p0], 'o', color=TUA, ms=5)
for xx in (xl, yv): ax.plot([xx], [p0], 's', color=HJ, ms=5)
ax.text(0.41, p0 + 0.25, 'a', fontsize=9.5); ax.text(xl - 0.05, p0 - 0.6, r'$x_\mathrm{B}$', color=HJ); ax.text(yv + 0.01, p0 - 0.6, r'$y_\mathrm{B}$', color=HJ)
ax.text(0.15, 10.6, 'cair', fontsize=11, color=BIRU, fontweight='bold'); ax.text(0.72, 4.6, 'uap', fontsize=11, color=JT, fontweight='bold')
ax.text(0.55, 9.0, 'garis cair', color=BIRU, fontsize=9, rotation=31); ax.text(0.62, 6.3, 'garis uap', color=JT, fontsize=9, rotation=28)
ax.set_xlim(0, 1); ax.set_ylim(3, 13.5); ax.set_xlabel('fraksi mol benzena, z'); ax.set_ylabel('p (kPa)'); sumbu(ax); simpan(f, 'pxy')
# 11.2 diagram T-x-y benzena-toluena 1 atm dengan tangga distilasi
xs = np.linspace(0, 1, 120); Tb = np.array([solve(lambda t: xx * bz(t) + (1 - xx) * tl(t) - P, 70, 120) for xx in xs]); ys = xs * bz(Tb) / P
f, ax = plt.subplots(figsize=(5.2, 3.9), dpi=220)
ax.plot(xs, Tb, color=BIRU, lw=2.4); ax.plot(ys, Tb, color=JT, lw=2.4)
x = 0.2
for i in range(5):
    T = solve(lambda t: x * bz(t) + (1 - x) * tl(t) - P, 70, 120); y = x * bz(T) / P
    ax.plot([x, y], [T, T], color=TUA, lw=1.3); T2 = solve(lambda t: y * bz(t) + (1 - y) * tl(t) - P, 70, 120)
    ax.plot([y, y], [T, T2], color=TUA, lw=1.3, ls=':'); ax.text((x + y) / 2, T + 0.5, str(i + 1), fontsize=8, color=TUA, ha='center'); x = y
ax.text(0.08, 86, 'cair', fontsize=11, color=BIRU, fontweight='bold'); ax.text(0.65, 106, 'uap', fontsize=11, color=JT, fontweight='bold')
ax.text(0.45, 104, 'garis titik embun', color=JT, fontsize=9); ax.text(0.03, 81.5, 'garis titik gelembung', color=BIRU, fontsize=9)
ax.set_xlim(0, 1); ax.set_ylim(78, 112); ax.set_xlabel('fraksi mol benzena'); ax.set_ylabel('T (°C)'); sumbu(ax); simpan(f, 'txy')
# 11.3 azeotrop etanol-air (model van Laar)
A12, A21 = 1.6798, 0.9227
def gam(x1):
    x2 = 1 - x1; d = A12 * x1 + A21 * x2
    return np.exp(A12 * (A21 * x2 / d) ** 2), np.exp(A21 * (A12 * x1 / d) ** 2)
xs = np.linspace(0.001, 0.999, 300); T = []; Y = []
for x1 in xs:
    g1, g2 = gam(x1); t = solve(lambda t: x1 * g1 * et(t) + (1 - x1) * g2 * wa(t) - P, 60, 110); T.append(t); Y.append(x1 * g1 * et(t) / P)
T = np.array(T); Y = np.array(Y)
f, ax = plt.subplots(figsize=(5.2, 3.9), dpi=220)
ax.plot(xs, T, color=BIRU, lw=2.4); ax.plot(Y, T, color=JT, lw=2.4)
i = np.argmin(T); ax.plot([xs[i]], [T[i]], 'o', color=HJ, ms=6, zorder=5); ax.annotate('azeotrop', (xs[i], T[i]), (0.62, 81.5), color=HJ, fontsize=9, arrowprops=dict(arrowstyle='->', color=HJ))
ax.text(0.1, 83, 'cair', fontsize=11, color=BIRU, fontweight='bold'); ax.text(0.3, 95, 'uap', fontsize=11, color=JT, fontweight='bold')
ax.set_xlim(0, 1); ax.set_ylim(76, 101); ax.set_xlabel('fraksi mol etanol'); ax.set_ylabel('T (°C)'); sumbu(ax); simpan(f, 'azeotrop')
# 11.4 kurva kelarutan larutan reguler
def binodal(beta): return solve(lambda x: np.log(x / (1 - x)) - beta * (2 * x - 1), 1e-12, 0.49999)
betas = np.linspace(2.0001, 6, 300); xb = np.array([binodal(b) for b in betas]); Tr = 2 / betas
f, ax = plt.subplots(figsize=(5.2, 3.7), dpi=220)
ax.plot(np.r_[xb, (1 - xb)[::-1]], np.r_[Tr, Tr[::-1]], color=TUA, lw=2.4)
ax.fill(np.r_[xb, (1 - xb)[::-1]], np.r_[Tr, Tr[::-1]], color=JG, alpha=0.18, lw=0)
b = 2.5; x1 = binodal(b); ax.plot([x1, 1 - x1], [2 / b] * 2, color=HJ, lw=1.4); ax.plot([0.35], [2 / b], 'o', color=HJ, ms=5)
ax.plot([0.5], [1], 'o', color=JT, ms=6); ax.text(0.53, 1.01, r'$T_\mathrm{c}$', color=JT)
ax.text(0.5, 1.07, 'satu fasa cair', ha='center', fontsize=10, color=BIRU); ax.text(0.5, 0.55, 'dua fasa cair', ha='center', fontsize=10, color=JT)
ax.set_xlim(0, 1); ax.set_ylim(0.3, 1.15); ax.set_xlabel(r'fraksi mol B, $x_\mathrm{B}$'); ax.set_ylabel(r'$T/T_\mathrm{c}$'); sumbu(ax); simpan(f, 'larut')
# 11.5 eutektik benzena-naftalena (larutan ideal)
Ta, Ha, Tn, Hn = 278.7, 9870, 353.4, 19010
xa = lambda T: np.exp(-Ha / R * (1 / T - 1 / Ta)); xn = lambda T: np.exp(-Hn / R * (1 / T - 1 / Tn))
Te = solve(lambda T: xa(T) + xn(T) - 1, 200, 278); xe = xn(Te)
f, ax = plt.subplots(figsize=(5.2, 3.9), dpi=220)
T1 = np.linspace(Te, Ta, 100); ax.plot(1 - xa(T1), T1 - 273.15, color=BIRU, lw=2.4)
T2 = np.linspace(Te, Tn, 100); ax.plot(xn(T2), T2 - 273.15, color=JT, lw=2.4)
ax.plot([0, 1], [Te - 273.15] * 2, color=TUA, lw=1.6); ax.plot([xe], [Te - 273.15], 'o', color=HJ, ms=6, zorder=5)
ax.text(0.45, 55, 'larutan cair', fontsize=10, color=TUA, ha='center'); ax.text(0.03, -20, 'benzena padat\n+ naftalena padat', fontsize=9, color=TUA)
ax.text(0.55, 15, 'naftalena padat\n+ larutan', fontsize=9, color=JT); ax.annotate('benzena padat + larutan', (0.03, 0.5), (0.12, 14), fontsize=8, color=BIRU, arrowprops=dict(arrowstyle='->', color=BIRU))
ax.annotate('eutektik', (xe, Te - 273.15), (0.25, -10), color=HJ, fontsize=9, arrowprops=dict(arrowstyle='->', color=HJ))
ax.set_xlim(0, 1); ax.set_ylim(-30, 85); ax.set_xlabel('fraksi mol naftalena'); ax.set_ylabel('T (°C)'); sumbu(ax); simpan(f, 'eutektik')
# 11.6 diagram segitiga (skematis)
h = np.sqrt(3) / 2
def tri(a, b, c):  # fraksi A (kiri bawah), B (kanan bawah), C (puncak)
    return b + c / 2, c * h
f, ax = plt.subplots(figsize=(5.0, 4.4), dpi=220); ax.axis('off')
ax.plot([0, 1, 0.5, 0], [0, 0, h, 0], color=TUA, lw=1.8)
for k in np.arange(0.1, 1, 0.1):
    for p, q in [(tri(1 - k, 0, k), tri(0, 1 - k, k)), (tri(k, 1 - k, 0), tri(k, 0, 1 - k)), (tri(1 - k, k, 0), tri(0, k, 1 - k))]:
        ax.plot([p[0], q[0]], [p[1], q[1]], color='#ddd', lw=0.6, zorder=0)
xa_ = np.linspace(0.04, 0.96, 200); c = 1.6 * xa_ * (1 - xa_) ** 1.3
px = [tri(1 - a - cc, a, cc) for a, cc in zip(xa_, c)]
ax.plot([p[0] for p in px], [p[1] for p in px], color=BIRU, lw=2.2)
ax.fill([p[0] for p in px], [p[1] for p in px], color=MUDA, alpha=0.3, lw=0)
for a1, a2 in [(0.07, 0.88), (0.12, 0.78), (0.2, 0.66)]:
    c1 = 1.6 * a1 * (1 - a1) ** 1.3; c2 = 1.6 * a2 * (1 - a2) ** 1.3
    p1, p2 = tri(1 - a1 - c1, a1, c1), tri(1 - a2 - c2, a2, c2); ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=JT, lw=1.2)
pt = tri(0.2, 0.3, 0.5); ax.plot(*pt, 'o', color=HJ, ms=6); ax.text(pt[0] + 0.02, pt[1], 'P', color=HJ, fontsize=10)
ax.text(-0.04, -0.06, 'air', ha='center', fontsize=10, color=TUA); ax.text(1.04, -0.06, 'kloroform', ha='center', fontsize=10, color=TUA); ax.text(0.5, h + 0.03, 'asam asetat', ha='center', fontsize=10, color=TUA)
ax.text(0.55, 0.08, 'dua fasa', ha='center', fontsize=9, color=BIRU); ax.text(0.5, 0.55, 'satu fasa', ha='center', fontsize=9, color=TUA)
ax.set_xlim(-0.1, 1.1); ax.set_ylim(-0.1, h + 0.08); ax.set_aspect('equal'); simpan(f, 'segitiga')
