# Gambar tambahan Bab 4 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab04/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def k(x, d=1): return f'{x:+.{d}f}'.replace('.', ',').replace('-', '−')
def tingkat(ax, x0, x1, y, t, c=TUA, kiri=False, fs=8.8):
    ax.plot([x0, x1], [y, y], color=c, lw=2.2); ax.text((x0 + x1) / 2, y + 12, t, ha='center', va='bottom', fontsize=fs, color=c)
def ar(ax, x, y0, y1, t, c, dx=0.15, fs=8.6):
    ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle='-|>', mutation_scale=11, color=c, lw=1.5)); ax.text(x + dx, (y0 + y1) / 2, t, fontsize=fs, color=c, va='center')

# 1. siklus Born–Haber NaCl (tangga bergeser ke kanan)
f, ax = plt.subplots(figsize=(9.0, 4.8)); ax.axis('off'); W = 2.6
L = [(0, 0.0, 'Na(s) + ½Cl$_2$(g)'), (1, 107.3, 'Na(g) + ½Cl$_2$(g)'), (2, 603.1, 'Na$^+$(g) + e$^-$ + ½Cl$_2$(g)'), (3, 724.8, 'Na$^+$(g) + e$^-$ + Cl(g)'), (4, 376.2, 'Na$^+$(g) + Cl$^-$(g)')]
for i, y, t in L: tingkat(ax, i * W, (i + 1) * W, y, t, fs=8.2)
lab = ['sublimasi\n+107,3', 'ionisasi\n+495,8', 'atomisasi\n+121,7', 'afinitas elektron\n−348,6']
for i in range(4):
    c = HJ if L[i + 1][1] < L[i][1] else BIRU; ar(ax, (i + 1) * W, L[i][1], L[i + 1][1], lab[i], c, dx=0.1, fs=8.2)
tingkat(ax, 0, W, -411.2, 'NaCl(s)', c=JT, fs=8.2)
ar(ax, 0.85 * W, 0, -411.2, 'pembentukan\n−411,2', HJ, dx=0.1, fs=8.2)
xl = 5 * W + 0.5; ax.add_patch(FancyArrowPatch((xl, -411.2), (xl, 376.2), arrowstyle='-|>', mutation_scale=12, color=JT, lw=2))
ax.plot([W, xl + 0.1], [-411.2, -411.2], color=JT, lw=0.8, ls=':'); ax.plot([5 * W, xl + 0.1], [376.2, 376.2], color=JT, lw=0.8, ls=':')
ax.text(xl + 0.15, -20, 'entalpi kisi\n+787,4', fontsize=9, color=JT, va='center', fontweight='bold')
ax.set_xlim(-0.1, xl + 1.8); ax.set_ylim(-470, 800); ax.text(0, 780, 'kJ mol$^{-1}$, relatif terhadap unsur', fontsize=8.5, color='#666666')
simpan(f, 'bornhaber')

# 2. tangga entalpi pembentukan: pembakaran etanol
f, ax = plt.subplots(figsize=(6.4, 3.6)); ax.axis('off'); ax.set_xlim(0, 10)
yr = -277.69; yp = 2 * -393.51 + 3 * -285.83
tingkat(ax, 0.5, 9.5, 0, 'unsur dalam keadaan acuan: 2C(grafit) + 3H$_2$(g) + 3½O$_2$(g)   (Δ$_f$H° = 0)', c='#666666')
ax.plot([0.8, 3.8], [yr, yr], color=TUA, lw=2.2); ax.text(2.3, yr - 25, 'C$_2$H$_5$OH(l) + 3O$_2$(g)', ha='center', va='top', fontsize=8.8, color=TUA)
ax.plot([6.2, 9.2], [yp, yp], color=TUA, lw=2.2); ax.text(7.7, yp - 25, '2CO$_2$(g) + 3H$_2$O(l)', ha='center', va='top', fontsize=8.8, color=TUA)
ar(ax, 1.2, 0, yr, 'Δ$_f$H°(etanol) −277,7', BIRU, dx=0.12); ar(ax, 7.7, 0, yp, '2(−393,5) + 3(−285,8)\n= −1644,5', BIRU)
ax.add_patch(FancyArrowPatch((3.8, yr), (6.2, yp), arrowstyle='-|>', mutation_scale=12, color=JT, lw=2))
ax.text(0.6, (yr + yp) / 2 - 150, 'Δ$_r$H° = −1644,5 − (−277,7)\n= −1366,8 kJ mol$^{-1}$', fontsize=9, color=JT, fontweight='bold')
ax.set_ylim(-1820, 120)
simpan(f, 'formasi')

# 3. entalpi ikatan: pembakaran metana (fase gas)
f, ax = plt.subplots(figsize=(6.4, 3.6)); ax.axis('off'); ax.set_xlim(0, 10)
brk = 4 * 412 + 2 * 498; frm = 2 * 799 + 4 * 463
tingkat(ax, 0.6, 3.6, 0, 'CH$_4$(g) + 2O$_2$(g)'); tingkat(ax, 3.4, 6.6, brk, 'C(g) + 4H(g) + 4O(g)'); tingkat(ax, 6.4, 9.4, brk - frm, 'CO$_2$(g) + 2H$_2$O(g)', c=JT)
ar(ax, 3.5, 0, brk, 'putus 4 C–H + 2 O=O\n+2644', BIRU); ar(ax, 6.5, brk, brk - frm, 'bentuk 2 C=O + 4 O–H\n−3450', HJ)
ax.add_patch(FancyArrowPatch((2.1, 0), (2.1, brk - frm), arrowstyle='-|>', mutation_scale=12, color=JT, lw=2)); ax.plot([2.1, 6.4], [brk - frm, brk - frm], color=JT, lw=0.8, ls=':')
ax.text(0.2, (brk - frm) / 2, 'Δ$_r$H ≈ −806\n(terukur −802)', fontsize=9, color=JT, fontweight='bold', va='center')
ax.set_ylim(-950, 2900); ax.text(0.0, -900, 'kJ mol$^{-1}$; entalpi ikatan rata-rata Tabel 4.2', fontsize=8.5, color='#666666', ha='left')
simpan(f, 'ikatan')

# 4. Kirchhoff: entalpi penguapan air terhadap suhu
f, ax = plt.subplots(figsize=(6.0, 3.1))
td = np.array([0, 25, 50, 75, 100]); Hd = np.array([45.05, 43.99, 42.91, 41.81, 40.66])
t = np.linspace(0, 100, 50); dCp = (75.3 - 33.6) / 1000; ax.plot(t, 40.66 + dCp * (100 - t), color=BIRU, lw=2, label='Kirchhoff: $\\Delta C_p$ = −41,7 J K$^{-1}$ mol$^{-1}$ tetap')
ax.plot(td, Hd, 'o', color=JT, ms=6, label='data terukur')
ax.set_xlabel('suhu (°C)'); ax.set_ylabel('Δ$_\\mathrm{vap}$H (kJ mol$^{-1}$)'); ax.legend(frameon=False, fontsize=8.5); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'kirchhoff')
print('ok bab04b')
