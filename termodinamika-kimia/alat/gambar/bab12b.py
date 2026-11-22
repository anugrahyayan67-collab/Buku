# Gambar tambahan Bab 12 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
f, ax = plt.subplots(figsize=(6.0, 3.1)); t = np.linspace(0, 100, 200); T = t + 273.15
pKw = 13.997 + 55840 / 8.314 * (1 / T - 1 / 298.15) / np.log(10)
ax.plot(t, pKw, color=BIRU, lw=2.2, label='van \'t Hoff, Δ$_r$H° = 55,8 kJ mol$^{-1}$ tetap')
td = [0, 25, 50, 100]; pd = [14.94, 14.00, 13.26, 12.26]; ax.plot(td, pd, 'o', color=JT, ms=6, label='terukur')
ax.plot(t, pKw / 2, color=HJ, lw=1.6, ls='--', label='pH netral = p$K_w$/2')
ax.set_xlabel('suhu (°C)'); ax.set_ylabel('p$K_w$ atau pH'); ax.set_xlim(0, 100); ax.set_ylim(5.5, 15.5); ax.legend(frameon=False, fontsize=8.5, loc='center right'); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); f.savefig(f'{R}/bab12/fig/kw.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok')
