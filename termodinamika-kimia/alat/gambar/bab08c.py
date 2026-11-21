# Gambar tambahan Bab 8: μ es dan air terhadap tekanan pada −1 °C; rapatan air dan uap menuju titik kritis
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R0 = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R0}/bab08/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
# 1. μ(es) dan μ(air) pada −1 °C terhadap tekanan
f, ax = plt.subplots(figsize=(6.0, 3.0)); p = np.linspace(0, 250, 200)  # bar
dm = 22.0 - 1.63e-6 * (p - 1) * 1e5
ax.plot(p, dm, color=BIRU, lw=2.4); ax.axhline(0, color='#999999', lw=0.8)
ax.fill_between(p, dm, 0, where=dm > 0, color=MUDA, alpha=0.3, lw=0); ax.fill_between(p, dm, 0, where=dm < 0, color=BIRU, alpha=0.15, lw=0)
px = 1 + 22.0 / (1.63e-6 * 1e5); ax.plot(px, 0, 'o', color=JT, ms=5)
ax.text(px + 4, 2, f'{px:.0f} bar'.replace('.', ','), fontsize=8.5, color=JT); ax.text(15, 6, 'es stabil\n(μ air > μ es)', fontsize=8.5, color=TUA); ax.text(196, -5, 'air stabil', fontsize=8.5, color=BIRU)
ax.text(120, 15, 'kemiringan = $V_\\mathrm{m}$(air) − $V_\\mathrm{m}$(es)\n= −1,63 cm$^3$ mol$^{-1}$', fontsize=8.3, color=TUA)
ax.set_xlabel('$p$ (bar)'); ax.set_ylabel('$\\mu$(air) − $\\mu$(es) (J mol$^{-1}$)'); ax.set_title('−1 °C', fontsize=9)
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom); f.tight_layout(); simpan(f, 'mup')
# 2. rapatan cairan dan uap air jenuh (data IAPWS, dibulatkan)
T = np.array([25, 100, 150, 200, 250, 300, 350]); rl = np.array([997.0, 958.4, 917.0, 864.7, 799.1, 712.1, 574.7]); rv = np.array([0.023, 0.598, 2.55, 7.86, 19.97, 46.2, 113.6])
Tc, rc = 373.95, 322.0
f, ax = plt.subplots(figsize=(6.0, 3.1))
ax.plot(T, rl, 'o-', color=BIRU, lw=2, ms=5, label='cairan jenuh'); ax.plot(T, rv, 's-', color=JT, lw=2, ms=4.5, label='uap jenuh')
tt = np.linspace(350, Tc, 50); d = (rl[-1] - rv[-1]) / 2 * ((Tc - tt) / (Tc - 350)) ** 0.33; m = rc + (tt - Tc) * ((rl[-1] + rv[-1]) / 2 - rc) / (350 - Tc)
ax.plot(tt, m + d, color=BIRU, lw=2, ls='--'); ax.plot(tt, m - d, color=JT, lw=2, ls='--')
ax.plot(Tc, rc, '*', color=TUA, ms=12); ax.annotate('titik kritis\n374 °C; 322 kg m$^{-3}$', xy=(Tc, rc), xytext=(250, 420), fontsize=8.5, color=TUA, arrowprops=dict(arrowstyle='->', color=TUA, lw=0.8))
ax.set_xlabel('$t$ (°C)'); ax.set_ylabel('rapatan (kg m$^{-3}$)'); ax.set_xlim(0, 400); ax.set_ylim(0, 1050); ax.legend(frameon=False, fontsize=8.5, loc='center left')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom); f.tight_layout(); simpan(f, 'kritis')
print('ok bab08c', px)
