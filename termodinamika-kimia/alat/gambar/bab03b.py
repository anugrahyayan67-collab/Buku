# Gambar tambahan Bab 3 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch, Circle
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab03/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def panah(ax, a, b, c=TUA, lw=1.6, ms=13): ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw))
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)

# 1. piston: kerja melawan tekanan luar
f, ax = plt.subplots(figsize=(6.6, 3.0)); ax.set_xlim(0, 20); ax.set_ylim(0, 9); ax.set_aspect('equal'); ax.axis('off')
for x0, h, t in [(1.0, 3.2, 'keadaan awal'), (11.0, 5.2, 'setelah memuai')]:
    ax.plot([x0, x0, x0 + 6, x0 + 6], [7.8, 0.6, 0.6, 7.8], color=TUA, lw=2)
    ax.add_patch(Rectangle((x0 + 0.05, 0.65), 5.9, h - 0.65, fc='#eaf3fb', ec='none'))
    rng = np.random.default_rng(int(h * 10))
    for _ in range(int(14 * h / 3.2)):
        ax.add_patch(Circle((x0 + 0.5 + rng.random() * 5.0, 1.0 + rng.random() * (h - 1.5)), 0.13, color=BIRU))
    ax.add_patch(Rectangle((x0 + 0.05, h), 5.9, 0.45, fc='#9aa3ad', ec=TUA, lw=1))
    for xx in (x0 + 1.5, x0 + 3, x0 + 4.5): panah(ax, (xx, h + 1.9), (xx, h + 0.55), JT, lw=1.3, ms=10)
    ax.text(x0 + 3, h + 2.15, '$p_\\mathrm{luar}$', ha='center', fontsize=9.5, color=JT)
    ax.text(x0 + 3, 0.0, t, ha='center', fontsize=9, color=TUA)
ax.annotate('', (17.6, 5.2), (17.6, 3.2), arrowprops=dict(arrowstyle='<->', color=HJ, lw=1.2)); ax.text(17.85, 4.2, '$\\Delta h$', color=HJ, va='center')
ax.text(9.0, 4.4, '$\\Delta V = A\\,\\Delta h$\n\n$w = -p_\\mathrm{luar}\\Delta V$', ha='center', va='center', fontsize=9, color=TUA); ax.plot([11.1, 17.4], [3.2, 3.2], color=HJ, lw=0.9, ls=':')
simpan(f, 'piston')

# 2. konvensi tanda q dan w (IUPAC)
f, ax = plt.subplots(figsize=(6.8, 3.0)); ax.set_xlim(-2, 22); ax.set_ylim(0, 9.4); ax.axis('off')
ax.add_patch(FancyBboxPatch((6.5, 2.5), 7, 4.2, boxstyle='round,pad=0.2', fc='#eaf3fb', ec=BIRU, lw=1.6)); ax.text(10, 4.6, 'sistem\n$\\Delta U = q + w$', ha='center', va='center', fontsize=11, color=TUA)
ax.text(10, 8.6, 'lingkungan', ha='center', fontsize=10, color='#666666')
panah(ax, (-0.5, 5.6), (6.3, 5.6), HJ, lw=2.2); ax.text(2.9, 6.1, '$q > 0$ (kalor masuk)', ha='center', fontsize=9, color=HJ)
panah(ax, (6.3, 3.6), (-0.5, 3.6), JT, lw=2.2); ax.text(2.9, 2.9, '$q < 0$ (kalor keluar)', ha='center', fontsize=9, color=JT)
panah(ax, (20.5, 5.6), (13.7, 5.6), HJ, lw=2.2); ax.text(17.1, 6.1, '$w > 0$ (kerja pada sistem,\npemampatan)', ha='center', fontsize=9, color=HJ)
panah(ax, (13.7, 3.6), (20.5, 3.6), JT, lw=2.2); ax.text(17.1, 2.3, '$w < 0$ (sistem melakukan\nkerja, pemuaian)', ha='center', fontsize=9, color=JT)
ax.text(10, 0.8, 'energi yang masuk ke sistem bertanda positif', ha='center', fontsize=9, color=TUA)
simpan(f, 'tanda')

# 3. dua jalur, satu ΔU (gas ideal 1 mol, 300 K)
f, ax = plt.subplots(figsize=(5.8, 3.4))
Rg = 8.314; V1, V2, p1 = 10, 20, 2.4942; p2 = p1 / 2
ax.plot([V1, V1, V2], [p1, p2, p2], color=JT, lw=2.2, marker='o', ms=4, label='jalur A: dinginkan, lalu muai')
ax.plot([V1, V2, V2], [p1, p1, p2], color=BIRU, lw=2.2, marker='o', ms=4, label='jalur B: muai, lalu dinginkan')
V = np.linspace(V1, V2, 100); ax.plot(V, p1 * V1 / V, color=HJ, lw=2, ls='--', label='jalur C: isotermal')
ax.fill_between([V1, V2], [p2, p2], color=JT, alpha=0.12); ax.text(15, 0.55, '$|w_A|$', color=JT, ha='center')
ax.text(V1 - 0.4, p1, '1', ha='right', va='center', fontsize=11, fontweight='bold'); ax.text(V2 + 0.3, p2, '2', ha='left', va='center', fontsize=11, fontweight='bold')
ax.set_xlabel('$V$ (L)'); ax.set_ylabel('$p$ (bar)'); ax.set_xlim(8, 22); ax.set_ylim(0, 3.9); ax.legend(frameon=False, fontsize=8.5, loc='upper right', ncol=1); koma(ax)
f.tight_layout(); simpan(f, 'jalur')

# 4. C_V,m hidrogen terhadap suhu (bertangga): translasi, rotasi, getaran
f, ax = plt.subplots(figsize=(6.2, 3.1))
T = np.logspace(1, 4, 600); Trot, Tvib = 87.6, 6332
def ein(x): x = np.minimum(x, 600); return x ** 2 * np.exp(-x) / (1 - np.exp(-x)) ** 2
cv = 1.5 + 1.0 / (1 + np.exp(-(np.log(T) - np.log(1.6 * Trot)) * 3.2)) + ein(Tvib / T)
ax.semilogx(T, cv, color=BIRU, lw=2.4)
for y, t in [(1.5, 'translasi: $\\frac{3}{2} R$'), (2.5, '+ rotasi: $\\frac{5}{2} R$'), (3.5, '+ getaran: $\\frac{7}{2} R$')]:
    ax.axhline(y, color='#bbbbbb', lw=0.8, ls=':'); ax.text(11, y + 0.07, t, fontsize=8.5, color='#555555')
ax.axvline(298, color=JT, lw=0.8, ls='--'); ax.text(310, 1.15, '298 K', color=JT, fontsize=8.5)
ax.set_xlabel('$T$ (K, skala log)'); ax.set_ylabel('$C_{V,\\mathrm{m}}/R$'); ax.set_ylim(1, 4); ax.set_xlim(10, 10000); ax.yaxis.set_major_formatter(kom)
ax.text(3000, 1.4, 'hidrogen (H$_2$), skematis', fontsize=8.5, color=TUA, ha='center')
f.tight_layout(); simpan(f, 'cv')
print('ok bab03b')
