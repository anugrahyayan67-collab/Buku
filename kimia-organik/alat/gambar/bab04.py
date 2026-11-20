# Gambar Bab 4: Newman, energi putaran, tegangan cincin, kursi, pembalikan kursi
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab04/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))

# 1. Newman etana
def newman(ax, depan, belakang, lab_d, lab_b, judul):
    ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.9, 1.9); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0, 0), 0.7, fc='white', ec=TUA, lw=1.6, zorder=2))
    for a, t in zip(belakang, lab_b):
        r = np.radians(a); ax.plot([0.7 * np.cos(r), 1.35 * np.cos(r)], [0.7 * np.sin(r), 1.35 * np.sin(r)], color=JT, lw=1.6, zorder=1)
        ax.text(1.6 * np.cos(r), 1.6 * np.sin(r), t, ha='center', va='center', color=JT, fontsize=10)
    for a, t in zip(depan, lab_d):
        r = np.radians(a); ax.plot([0, 1.25 * np.cos(r)], [0, 1.25 * np.sin(r)], color=TUA, lw=1.8, zorder=3)
        ax.text(1.5 * np.cos(r), 1.5 * np.sin(r), t, ha='center', va='center', color=TUA, fontsize=10)
    ax.plot(0, 0, 'o', color=TUA, ms=4, zorder=4); ax.set_title(judul, color=TUA, fontsize=10, y=-0.08)
f, ax = plt.subplots(1, 2, figsize=(5.6, 2.9), dpi=220)
newman(ax[0], [90, 210, 330], [30, 150, 270], 'HHH', 'HHH', 'goyang (60°)')
newman(ax[1], [90, 210, 330], [100, 220, 340], 'HHH', 'HHH', 'tindih (0°)')
plt.tight_layout(); f.savefig(f'{F}/newman.png', bbox_inches='tight'); plt.close(f)

# 2. energi putaran etana dan butana
phi = np.linspace(0, 360, 721)
Eet = 6 * (1 + np.cos(np.radians(3 * phi)))
# butana: titik kunci (sudut CH3-C-C-CH3): 0:19, 60:3.8, 120:16, 180:0, 240:16, 300:3.8, 360:19
from scipy.interpolate import CubicSpline
xs = np.array([0, 60, 120, 180, 240, 300, 360]); ys = np.array([19, 3.8, 16, 0, 16, 3.8, 19])
cs = CubicSpline(xs, ys, bc_type='periodic'); Ebu = cs(phi)
f, ax = plt.subplots(2, 1, figsize=(5.6, 4.6), dpi=220, sharex=True)
ax[0].plot(phi, Eet, color=BIRU, lw=2); ax[0].set_ylabel('E (kJ mol$^{-1}$)'); ax[0].set_ylim(-1, 14); ax[0].text(5, 12.6, 'etana', color=TUA, fontsize=10)
ax[1].plot(phi, Ebu, color=JT, lw=2); ax[1].set_ylabel('E (kJ mol$^{-1}$)'); ax[1].set_ylim(-2, 27); ax[1].set_xlim(-15, 375)
for x, y, t in [(0, 19, '19\ntindih\nCH₃/CH₃'), (60, 3.8, 'gauche\n3,8'), (120, 16, 'tindih H/CH₃\n16'), (180, 0, 'anti 0'), (300, 3.8, 'gauche\n3,8')]:
    ax[1].annotate(t, (x, y), textcoords='offset points', xytext=(14 if x == 0 else 0, 8 if (y > 10 or x == 180) else -26), ha='center', fontsize=7.6, color=TUA)
ax[1].text(330, 20.5, 'butana', color=TUA, fontsize=10)
ax[1].set_xlabel('sudut torsi (°)'); ax[1].set_xticks(range(0, 361, 60))
for a in ax: a.yaxis.set_major_formatter(kom)
plt.tight_layout(); f.savefig(f'{F}/putar.png', bbox_inches='tight'); plt.close(f)

# 3. tegangan cincin
n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]; s = [115, 110, 27, 0, 27, 40, 54, 50, 46, 17, 0]
f, ax = plt.subplots(figsize=(5.0, 2.9), dpi=220)
ax.bar(n, s, color=[JT if v > 60 else (HJ if v < 5 else BIRU) for v in s], width=0.7)
for x, v in zip(n, s): ax.text(x, v + 2, str(v), ha='center', fontsize=7.8, color=TUA)
ax.set_xlabel('jumlah karbon cincin'); ax.set_ylabel('tegangan cincin (kJ mol$^{-1}$)'); ax.set_xticks(n)
f.savefig(f'{F}/tegangan.png', bbox_inches='tight'); plt.close(f)

# 4. kursi aksial/ekuatorial (gambar kursi baku: sisi sejajar)
P = np.array([(0, 0), (0.85, 0.75), (2.15, 0.5), (3.0, 0.85), (2.15, 0.1), (0.85, 0.35)]) - np.array([1.5, 0.4])
naik = [False, True, False, True, False, True]
def kursi(ax, aks=True, eq=True, c_ring=TUA, ca=BIRU, ce=JT, lw=2, L=0.6):
    for i in range(6): ax.plot(*zip(P[i], P[(i + 1) % 6]), color=c_ring, lw=lw, zorder=2)
    cen = P.mean(0)
    for i in range(6):
        if aks: ax.plot([P[i][0], P[i][0]], [P[i][1], P[i][1] + (L if naik[i] else -L)], color=ca, lw=lw * 0.9, zorder=1)
        if eq:
            d = P[(i + 2) % 6] - P[(i + 1) % 6]; d = d / np.linalg.norm(d)
            if np.dot(d, P[i] - cen) < 0: d = -d
            ax.plot([P[i][0], P[i][0] + L * d[0]], [P[i][1], P[i][1] + L * d[1]], color=ce, lw=lw * 0.9, zorder=1)
f, ax = plt.subplots(1, 2, figsize=(7.0, 2.8), dpi=220)
for a, (A, Eq, t) in zip(ax, [(True, False, 'aksial'), (False, True, 'ekuatorial')]):
    a.set_xlim(-2.2, 2.2); a.set_ylim(-1.0, 1.1); a.set_aspect('equal'); a.axis('off'); kursi(a, A, Eq)
    a.set_title(t, color=BIRU if A else JT, fontsize=10.5, y=-0.1)
plt.tight_layout(); f.savefig(f'{F}/kursi.png', bbox_inches='tight'); plt.close(f)

# 5. pembalikan kursi
f, ax = plt.subplots(figsize=(6.2, 3.0), dpi=220)
x = [0, 1, 2, 3, 4, 5, 6]; y = [0, 45, 23, 29, 23, 45, 0]; lab = ['kursi', 'setengah-\nkursi', 'putar-\nperahu', 'perahu', 'putar-\nperahu', 'setengah-\nkursi', 'kursi']
xx = np.linspace(0, 6, 600); yy = CubicSpline(x, y, bc_type='clamped')(xx)
ax.plot(xx, yy, color=BIRU, lw=2)
for a, b, t in zip(x, y, lab):
    ax.plot(a, b, 'o', color=JT, ms=4); ax.text(a, b + 3, f'{b}', ha='center', fontsize=8, color=TUA); ax.text(a, -9, t, ha='center', va='top', fontsize=7.6, color=TUA)
ax.set_ylim(-20, 55); ax.set_xlim(-0.5, 6.5); ax.set_yticks(range(0, 51, 10)); ax.set_xticks([]); ax.set_ylabel('E (kJ mol$^{-1}$)'); ax.spines['bottom'].set_visible(False)
f.savefig(f'{F}/balik.png', bbox_inches='tight'); plt.close(f)
print('ok')
