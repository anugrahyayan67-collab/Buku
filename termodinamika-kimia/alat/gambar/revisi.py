# Gambar tambahan revisi 1.1: python3 alat/gambar/revisi.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Polygon
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, bab, n): f.tight_layout(); f.savefig(f'{R}/bab{bab:02d}/fig/{n}.png'); plt.close(f)
def panah(ax, a, b, c=TUA, lw=1.6, ms=12): ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw))

# Bab 1: satu molekul memantul di dinding kanan
f, ax = plt.subplots(figsize=(5.4, 3.0), dpi=220); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 5.4); ax.set_aspect('equal')
ax.add_patch(Rectangle((0.6, 0.4), 6.2, 4.4, fill=False, ec=TUA, lw=1.8))
ax.add_patch(Rectangle((6.8, 0.4), 0.25, 4.4, color=JG, alpha=0.7))
ax.text(6.95, 4.95, 'dinding (luas $L^2$)', ha='center', fontsize=8.5, color=JT)
x0, y0 = 3.2, 2.0; ax.add_patch(Circle((x0, y0), 0.17, color=BIRU)); panah(ax, (x0 + 0.2, y0 + 0.1), (6.55, 3.1), BIRU)
ax.add_patch(Circle((6.62, 3.15), 0.17, color=BIRU, alpha=0.5)); panah(ax, (6.45, 3.3), (4.2, 4.3), BIRU)
panah(ax, (3.45, 1.35), (5.0, 1.35), JT); ax.text(4.2, 0.95, '$+v_x$', color=JT, ha='center')
panah(ax, (5.0, 4.0), (3.45, 4.0), JT); ax.text(4.2, 3.6, '$-v_x$', color=JT, ha='center')
ax.annotate('', (0.6, 0.15), (6.8, 0.15), arrowprops=dict(arrowstyle='<->', color=TUA, lw=1)); ax.text(3.7, -0.15, '$L$', ha='center', va='top')
ax.text(7.4, 3.0, 'perubahan momentum\nper pantulan: $2mv_x$\n\nselang antarpantulan\npada dinding yang sama:\n$2L/v_x$', fontsize=8.5, color=TUA, va='center')
simpan(f, 1, 'dinding')

# Bab 3: ekspansi reversibel dengan butir pasir
f, ax = plt.subplots(figsize=(5.6, 2.8), dpi=220); ax.axis('off'); ax.set_xlim(0, 11); ax.set_ylim(0, 5.2)
rng = np.random.default_rng(3)
for k, (x0, nb, h) in enumerate([(0.5, 40, 1.6), (4.0, 24, 2.3), (7.5, 8, 3.0)]):
    ax.add_patch(Rectangle((x0, 0.4), 2.6, 3.9, fill=False, ec=TUA, lw=1.6))
    ax.add_patch(Rectangle((x0 + 0.05, 0.45), 2.5, h - 0.45, color=MUDA, alpha=0.5, lw=0))
    ax.add_patch(Rectangle((x0 + 0.05, h), 2.5, 0.22, color=TUA))
    for i in range(nb):
        r = i // 8; c = i % 8; ax.add_patch(Circle((x0 + 0.35 + c * 0.27 + (r % 2) * 0.13, h + 0.36 + r * 0.2), 0.1, color=JG, ec=JT, lw=0.4))
    ax.text(x0 + 1.3, 0.05, ['awal', 'di tengah jalan', 'akhir'][k], ha='center', fontsize=9, color=TUA)
for x in (3.3, 6.8): panah(ax, (x, 2.4), (x + 0.5, 2.4), JT)

simpan(f, 3, 'pasir')

# Bab 4: bom kalorimeter (skema)
f, ax = plt.subplots(figsize=(4.6, 3.6), dpi=220); ax.axis('off'); ax.set_xlim(0, 8); ax.set_ylim(0, 6.6)
ax.add_patch(Rectangle((0.6, 0.4), 5.4, 5.0, fill=False, ec=TUA, lw=2.2)); ax.text(3.3, 5.6, 'wadah berisolasi', ha='center', fontsize=8.5, color=TUA)
ax.add_patch(Rectangle((0.9, 0.7), 4.8, 3.9, color=MUDA, alpha=0.45, lw=0)); ax.text(1.1, 4.25, 'air', fontsize=9, color=BIRU)
ax.add_patch(Rectangle((2.2, 1.0), 2.0, 2.4, fc='#d9dde2', ec=TUA, lw=1.8)); ax.text(3.2, 2.75, 'bom baja\n(V tetap)', ha='center', fontsize=7.5, color=TUA)
ax.add_patch(Rectangle((2.9, 2.0), 0.6, 0.3, color=JT)); ax.text(3.2, 1.65, 'sampel + O₂', ha='center', fontsize=7, color=JT)
ax.plot([2.6, 2.6, 3.0], [3.4, 2.6, 2.2], color=TUA, lw=1); ax.plot([3.8, 3.8, 3.4], [3.4, 2.6, 2.2], color=TUA, lw=1)
ax.plot([4.9, 4.9], [1.2, 6.2], color=TUA, lw=2); ax.add_patch(Circle((4.9, 1.2), 0.13, color='#c0392b')); ax.text(5.1, 6.0, 'termometer', fontsize=8, color=TUA)
ax.plot([1.6, 1.6], [1.2, 6.0], color=TUA, lw=1.5); ax.plot([1.2, 2.0], [1.2, 1.2], color=TUA, lw=2.5); ax.text(1.0, 6.05, 'pengaduk', fontsize=8, color=TUA)
ax.text(6.3, 2.6, 'q = C·ΔT\nΔU = q$_V$', fontsize=9.5, color=HJ)
simpan(f, 4, 'bom')

# Bab 5: siklus sembarang dipetak menjadi siklus Carnot kecil
f, ax = plt.subplots(figsize=(4.8, 3.6), dpi=220)
t = np.linspace(0, 2 * np.pi, 400); X = 2.0 + 0.9 * np.cos(t); Y = 2.0 + 1.1 * np.sin(t) + 0.15 * np.sin(2 * t)
for c in np.linspace(1.6, 5.2, 13): xx = np.linspace(0.8, 3.3, 100); ax.plot(xx, c / xx, color=JG, lw=0.7, alpha=0.8)
for c in np.linspace(1.8, 9.5, 13): xx = np.linspace(0.8, 3.3, 100); ax.plot(xx, c / xx ** (5 / 3), color=MUDA, lw=0.7)
ax.plot(X, Y, color=TUA, lw=2.4)
g = 5 / 3; c1, c2, a1, a2 = 3.6, 4.0, 5.3, 6.0
Vx = lambda c, a: (a / c) ** (1 / (g - 1))
VA, VB, VC, VD = Vx(c2, a1), Vx(c2, a2), Vx(c1, a2), Vx(c1, a1)
v1 = np.linspace(VA, VB, 30); v2 = np.linspace(VB, VC, 30); v3 = np.linspace(VC, VD, 30); v4 = np.linspace(VD, VA, 30)
ax.fill(np.r_[v1, v2, v3, v4], np.r_[c2 / v1, a2 / v2 ** g, c1 / v3, a1 / v4 ** g], color=JT, alpha=0.55, lw=0)
ax.annotate('satu siklus Carnot kecil', (VB, c2 / VB), (2.45, 3.3), fontsize=8.5, color=JT, arrowprops=dict(arrowstyle='->', color=JT))
ax.text(3.0, 1.6, 'isoterm', color=JT, fontsize=8.5); ax.text(0.85, 0.55, 'adiabat', color=BIRU, fontsize=8.5)
ax.set_xlim(0.8, 3.4); ax.set_ylim(0.4, 3.6); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('V'); ax.set_ylabel('p')
simpan(f, 5, 'clausius')

# Bab 6: entropi pencampuran per mol terhadap fraksi mol
x = np.linspace(1e-4, 1 - 1e-4, 300); Sm = -8.314 * (x * np.log(x) + (1 - x) * np.log(1 - x))
f, ax = plt.subplots(figsize=(4.8, 3.2), dpi=220)
ax.plot(x, Sm, color=BIRU, lw=2.4); ax.plot([0.5], [8.314 * np.log(2)], 'o', color=JT); ax.text(0.53, 5.95, r'$R\ln 2 = 5{,}76$', color=JT, fontsize=9)
ax.set_xlim(0, 1); ax.set_ylim(0, 6.6); ax.set_xlabel('fraksi mol B'); ax.set_ylabel(r'$\Delta_\mathrm{mix}S_\mathrm{m}$ (J K$^{-1}$ mol$^{-1}$)')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom); simpan(f, 6, 'campurS')

# Bab 7: kotak termodinamika
f, ax = plt.subplots(figsize=(3.6, 3.6), dpi=220); ax.axis('off'); ax.set_xlim(-0.6, 3.6); ax.set_ylim(-0.6, 3.6); ax.set_aspect('equal')
ax.add_patch(Rectangle((0, 0), 3, 3, fill=False, ec=TUA, lw=1.8))
for (x, y, t) in [(0, 3, 'V'), (3, 3, 'T'), (3, 0, 'p'), (0, 0, 'S')]:
    ax.add_patch(Circle((x, y), 0.32, fc='white', ec=TUA, lw=1.5, zorder=3)); ax.text(x, y, t, ha='center', va='center', fontsize=14, style='italic', zorder=4)
for (x, y, t) in [(1.5, 3, 'A'), (3, 1.5, 'G'), (1.5, 0, 'H'), (0, 1.5, 'U')]:
    ax.add_patch(Rectangle((x - 0.3, y - 0.27), 0.6, 0.54, fc=MUDA, ec=BIRU, lw=1.2, zorder=3)); ax.text(x, y, t, ha='center', va='center', fontsize=14, color=TUA, fontweight='bold', zorder=4)
panah(ax, (0.3, 0.3), (2.68, 2.68), JT, 1.8, 14); panah(ax, (2.7, 0.3), (0.32, 2.68), JT, 1.8, 14)
f.savefig(f'{R}/bab07/fig/kotak.png'); plt.close(f)
print('ok')
