# Gambar Bab 6: diagram energi, Hammond, karbokation, kendali kinetik/termodinamik
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from scipy.interpolate import CubicSpline
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab06/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
def kurva(ax, x, y, c=BIRU):
    xx = np.linspace(x[0], x[-1], 500); ax.plot(xx, CubicSpline(x, y, bc_type='clamped')(xx), color=c, lw=2)
def gaya(ax):
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('koordinat reaksi'); ax.set_ylabel('energi')

# 1. diagram energi
f, ax = plt.subplots(1, 2, figsize=(7.2, 2.9), dpi=220)
kurva(ax[0], [0, 1, 2, 3, 4], [2, 2.3, 6, 1.5, 0.8]); gaya(ax[0])
ax[0].text(2, 6.3, '‡', ha='center', fontsize=13, color=JT); ax[0].text(0, 2.3, 'pereaksi', fontsize=8.5, color=TUA); ax[0].text(3.2, 0.3, 'produk', fontsize=8.5, color=TUA)
ax[0].annotate('', (1.0, 6.0), (1.0, 2.05), arrowprops=dict(arrowstyle='<->', color=JT)); ax[0].text(0.55, 4.0, '$E_a$', color=JT, fontsize=10)
ax[0].annotate('', (3.9, 0.85), (3.9, 2.0), arrowprops=dict(arrowstyle='<->', color=HJ)); ax[0].plot([0, 3.9], [2, 2], color='#c9d2db', lw=0.8, ls=':'); ax[0].text(3.95, 1.3, 'ΔG°', color=HJ, fontsize=9)
ax[0].set_ylim(0, 7.2); ax[0].set_title('satu langkah', fontsize=9.5, color=TUA)
kurva(ax[1], [0, 1, 2, 3, 4, 5, 6], [2, 2.2, 6.2, 4.0, 5.2, 1.0, 0.8]); gaya(ax[1])
ax[1].text(2, 6.5, '‡₁', ha='center', fontsize=12, color=JT); ax[1].text(4, 5.6, '‡₂', ha='center', fontsize=12, color=JT)
ax[1].text(3, 3.4, 'I', ha='center', fontsize=11, color=BIRU, fontweight='bold'); ax[1].text(0, 2.3, 'pereaksi', fontsize=8.5, color=TUA); ax[1].text(5.1, 0.3, 'produk', fontsize=8.5, color=TUA)
ax[1].set_ylim(0, 7.2); ax[1].set_title('dua langkah, dengan intermediet', fontsize=9.5, color=TUA)
plt.tight_layout(); f.savefig(f'{F}/energi.png', bbox_inches='tight'); plt.close(f)

# 2. Hammond
f, ax = plt.subplots(1, 2, figsize=(6.8, 2.8), dpi=220)
kurva(ax[0], [0, 1.2, 2.6, 3.2, 4], [1, 1.4, 5.6, 5.0, 4.8], JT); gaya(ax[0]); ax[0].set_ylim(0, 6.6)
ax[0].text(2.6, 5.9, '‡ mirip produk', ha='center', fontsize=8.5, color=JT); ax[0].text(0, 0.4, 'pereaksi', fontsize=8.5); ax[0].text(3.3, 4.2, 'produk', fontsize=8.5)
ax[0].set_title('endoterm: keadaan transisi lambat', fontsize=9, color=TUA)
kurva(ax[1], [0, 0.8, 1.4, 2.8, 4], [4.8, 5.0, 5.6, 1.4, 1.0], HJ); gaya(ax[1]); ax[1].set_ylim(0, 6.6)
ax[1].text(1.4, 5.9, '‡ mirip pereaksi', ha='center', fontsize=8.5, color=HJ); ax[1].text(0, 4.2, 'pereaksi', fontsize=8.5); ax[1].text(3.3, 0.4, 'produk', fontsize=8.5)
ax[1].set_title('eksoterm: keadaan transisi awal', fontsize=9, color=TUA)
plt.tight_layout(); f.savefig(f'{F}/hammond.png', bbox_inches='tight'); plt.close(f)

# 3. karbokation: hiperkonjugasi + urutan
f, ax = plt.subplots(1, 2, figsize=(7.2, 2.9), dpi=220, gridspec_kw={'width_ratios': [1, 1.25]})
a = ax[0]; a.set_xlim(-2.2, 2.4); a.set_ylim(-1.8, 1.9); a.set_aspect('equal'); a.axis('off')
for s in (1, -1): a.add_patch(Ellipse((0.8, 0.62 * s), 0.55, 1.15, fc='white', ec=TUA, lw=1.2))
a.text(0.8, 0.62, 'kosong', ha='center', va='center', fontsize=7, color=TUA)
a.plot(0.8, 0, 'o', color=TUA, ms=6); a.text(1.05, -0.12, 'C$^+$', fontsize=10, color=JT)
a.plot([0.8, -0.4], [0, 0], color=TUA, lw=2); a.plot(-0.4, 0, 'o', color=TUA, ms=6)
a.plot([-0.4, -0.4], [0, 1.0], color=BIRU, lw=2.2); a.text(-0.55, 1.15, 'H', fontsize=10, color=BIRU)
a.add_patch(Ellipse((-0.25, 0.75), 0.4, 0.95, angle=-20, fc=MUDA, ec=BIRU, lw=1, alpha=0.6))
a.annotate('', (0.55, 0.75), (-0.05, 0.85), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.3, connectionstyle='arc3,rad=-0.3'))
a.plot([-0.4, -1.2], [0, -0.6], color=TUA, lw=1.5); a.plot([-0.4, -1.0], [0, -1.0], color=TUA, lw=1.5)
a.set_title('hiperkonjugasi: σ(C–H) → p kosong', fontsize=8.8, color=TUA, y=-0.08)
b = ax[1]; lab = ['CH$_3^+$', 'RCH$_2^+$\n(1°)', 'R$_2$CH$^+$\n(2°)', 'R$_3$C$^+$\n(3°)', 'alilik /\nbenzilik']; val = [1, 2, 3, 4, 4.3]
b.bar(range(5), val, color=[MUDA, BIRU, BIRU, TUA, HJ], width=0.65)
b.set_xticks(range(5)); b.set_xticklabels(lab, fontsize=8); b.set_yticks([]); b.set_ylabel('kestabilan (kualitatif)')
b.set_title('kestabilan karbokation', fontsize=9, color=TUA)
plt.tight_layout(); f.savefig(f'{F}/kation.png', bbox_inches='tight'); plt.close(f)

# 4. kendali kinetik vs termodinamik
f, ax = plt.subplots(figsize=(5.6, 3.0), dpi=220)
X = [-2, -1, 0, 1, 2]; Y = [2.6, 6.2, 5.0, 7.0, 1.2]; xx = np.linspace(-2, 2, 600); yy = CubicSpline(X, Y, bc_type='clamped')(xx)
ax.plot(xx[xx <= 0], yy[xx <= 0], color=JT, lw=2); ax.plot(xx[xx >= 0], yy[xx >= 0], color=HJ, lw=2)
ax.text(0, 4.5, 'intermediet', ha='center', fontsize=8.5, color=TUA)
ax.text(-2, 1.6, 'produk K\n(kinetik)', ha='center', fontsize=8.5, color=JT); ax.text(2, 0.2, 'produk T\n(termodinamik)', ha='center', fontsize=8.5, color=HJ)
ax.text(-1, 6.45, 'penghalang\nrendah', ha='center', fontsize=7.8, color=JT); ax.text(1, 7.3, 'penghalang tinggi', ha='center', fontsize=7.8, color=HJ)
gaya(ax); ax.set_ylim(-0.6, 8.2); ax.set_xlim(-2.6, 2.6)
f.savefig(f'{F}/kendali.png', bbox_inches='tight'); plt.close(f)
print('ok')
