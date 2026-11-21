# Gambar tambahan Bab 10 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Circle
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab10/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
A = 0.509
# 1. γ± NaCl: data, hukum pembatas, diperluas, Davies
b = np.array([0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]); g = np.array([0.965, 0.927, 0.902, 0.819, 0.778, 0.681, 0.657])
s = np.linspace(0, 1.0, 300); I = s ** 2
f, ax = plt.subplots(figsize=(6.2, 3.3))
ax.plot(s, 10 ** (-A * s), color=BIRU, lw=1.8, ls='--', label='hukum pembatas')
ax.plot(s, 10 ** (-A * s / (1 + s)), color=HJ, lw=1.8, label='Debye–Hückel diperluas')
ax.plot(s, 10 ** (-A * (s / (1 + s) - 0.3 * I)), color=JT, lw=1.8, ls='-.', label='Davies')
ax.plot(np.sqrt(b), g, 'o', color=TUA, ms=6, label='NaCl terukur (25 °C)')
ax.set_xlabel('$\\sqrt{I}$ ($I$ dalam mol kg$^{-1}$)'); ax.set_ylabel('$\\gamma_\\pm$'); ax.set_xlim(0, 1.0); ax.set_ylim(0.3, 1.02); ax.legend(frameon=False, fontsize=8.5, loc='lower left'); koma(ax)
f.tight_layout(); simpan(f, 'gamma')
# 2. atmosfer ion (skematis)
f, ax = plt.subplots(figsize=(4.6, 3.4)); ax.set_xlim(-5, 5); ax.set_ylim(-3.8, 3.8); ax.set_aspect('equal'); ax.axis('off')
rng = np.random.default_rng(4)
ax.add_patch(Circle((0, 0), 2.6, fc='#fbe3d4', ec=JT, lw=1, ls='--', alpha=0.6))
pts = []
while len(pts) < 46:
    r = np.sqrt(rng.uniform(0.9 ** 2, 4.7 ** 2)); t = rng.uniform(0, 2 * np.pi); x, y = r * np.cos(t), r * np.sin(t)
    if abs(y) > 3.1 or (abs(y) < 0.45 and 0.5 < x < 2.8): continue
    if any((x - u) ** 2 + (y - v) ** 2 < 0.62 ** 2 for u, v, _ in pts): continue
    neg = rng.random() < (0.85 if r < 2.6 else 0.5); pts.append((x, y, neg))
for x, y, neg in pts:
    ax.add_patch(Circle((x, y), 0.24, color=BIRU if neg else JT, alpha=0.9)); ax.text(x, y - 0.02, '−' if neg else '+', ha='center', va='center', fontsize=7, color='white', fontweight='bold')
ax.add_patch(Circle((0, 0), 0.45, color=JT)); ax.text(0, -0.02, '+', ha='center', va='center', fontsize=12, color='white', fontweight='bold')
ax.annotate('', (2.6, 0), (0, 0), arrowprops=dict(arrowstyle='<->', color=TUA, lw=1)); ax.text(1.5, 0.22, '$\\kappa^{-1}$', ha='center', fontsize=10, color=TUA)
ax.text(0, -3.75, 'kation pusat dikelilingi "atmosfer" bermuatan negatif', ha='center', fontsize=8.5, color=TUA)
simpan(f, 'atmosfer')
print('ok bab10b')
