# Gambar tambahan Bab 7: neraca energi sel bahan bakar, ΔG°(T) amonia, grafit-intan terhadap tekanan
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R0 = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R0}/bab07/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)

# 1. neraca energi H2 + 1/2 O2 -> H2O(l): -ΔH = kerja maksimum + kalor wajib
f, ax = plt.subplots(figsize=(5.8, 2.6))
ax.barh([1], [285.83], color=TUA, height=0.5); ax.text(142, 1, '$-\\Delta_\\mathrm{r}H^\\circ$ = 285,83 kJ', color='white', ha='center', va='center', fontsize=9)
ax.barh([0], [237.13], color=BIRU, height=0.5); ax.barh([0], [48.70], left=237.13, color=JT, height=0.5)
ax.text(118, 0, 'kerja listrik maksimum\n$-\\Delta_\\mathrm{r}G^\\circ$ = 237,13 kJ (83%)', color='white', ha='center', va='center', fontsize=8.6)
ax.annotate('kalor wajib\n$-T\\Delta_\\mathrm{r}S^\\circ$ = 48,7 kJ', xy=(261, -0.2), xytext=(250, -0.85), fontsize=8.4, color=JT, ha='center', arrowprops=dict(arrowstyle='->', color=JT, lw=0.8))
ax.set_yticks([]); ax.set_xlim(0, 300); ax.set_ylim(-1.15, 1.4); ax.set_xlabel('kJ per mol H$_2$'); ax.spines['left'].set_visible(False); ax.xaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'neraca')

# 2. ΔrG° sintesis amonia terhadap suhu
f, ax = plt.subplots(figsize=(6.0, 3.0)); T = np.linspace(200, 900, 200); dH, dS = -92.22, -0.1988
ax.plot(T, dH - T * dS, color=BIRU, lw=2.2, label='$\\Delta_\\mathrm{r}G^\\circ = \\Delta_\\mathrm{r}H^\\circ - T\\Delta_\\mathrm{r}S^\\circ$')
ax.axhline(0, color='#999999', lw=0.8); ax.axhline(dH, color=JT, lw=1.2, ls='--', label='$\\Delta_\\mathrm{r}H^\\circ$ = −92,22 kJ mol$^{-1}$')
T0 = dH / dS; ax.plot(T0, 0, 'o', color=JT, ms=5); ax.annotate(f'{T0:.0f} K'.replace('.', ','), xy=(T0, 0), xytext=(T0 - 75, 18), fontsize=8.5, color=JT, arrowprops=dict(arrowstyle='->', color=JT, lw=0.8))
for t in [298.15, 500]: ax.plot(t, dH - t * dS, 's', color=TUA, ms=4.5)
ax.text(310, -47, '298 K: −32,9', fontsize=8.3, color=TUA); ax.text(512, -10, '500 K: +7,2', fontsize=8.3, color=TUA)
ax.text(250, -75, '$\\Delta_\\mathrm{r}G^\\circ < 0$:\npembentukan NH$_3$ disukai', fontsize=8.3, color='#666666'); ax.text(620, 62, '$\\Delta_\\mathrm{r}G^\\circ > 0$:\npenguraian NH$_3$ disukai', fontsize=8.3, color='#666666')
ax.set_xlabel('$T$ (K)'); ax.set_ylabel('kJ mol$^{-1}$'); ax.set_xlim(200, 900); ax.set_ylim(-100, 100); ax.legend(frameon=False, fontsize=8.3, loc='lower right', bbox_to_anchor=(1, 0.0))
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'GTamonia')

# 3. G grafit dan intan terhadap tekanan pada 298 K
f, ax = plt.subplots(figsize=(6.0, 3.0)); p = np.linspace(0, 25, 200)  # kbar
Gg = 5.298e-6 * p * 1e8 / 1000; Gi = 2.90 + 3.419e-6 * p * 1e8 / 1000
ax.plot(p, Gg, color=TUA, lw=2.2, label='grafit ($V_\\mathrm{m}$ = 5,30 cm$^3$ mol$^{-1}$)'); ax.plot(p, Gi, color=BIRU, lw=2.2, label='intan ($V_\\mathrm{m}$ = 3,42 cm$^3$ mol$^{-1}$)')
px = 2.90e3 / 1.879e-6 / 1e8; ax.plot(px, 5.298e-6 * px * 1e8 / 1000, 'o', color=JT, ms=5); ax.axvline(px, color=JT, lw=0.8, ls=':')
ax.text(px + 0.4, 1.5, f'{px:.1f} kbar'.replace('.', ','), fontsize=8.5, color=JT)
ax.text(6, 1.0, 'grafit stabil', fontsize=8.5, color=TUA); ax.text(18.5, 5.5, 'intan stabil', fontsize=8.5, color=BIRU)
ax.set_xlabel('$p$ (kbar)'); ax.set_ylabel('$G_\\mathrm{m} - G_\\mathrm{m}^\\circ$(grafit) (kJ mol$^{-1}$)'); ax.set_xlim(0, 25); ax.legend(frameon=False, fontsize=8.3, loc='upper left')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'intan')
print('ok bab07c', T0, px)
