# Gambar tambahan Bab 13: diagram Pourbaix besi (aktivitas ion terlarut 1e-6)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
s = 0.05916; c = 1e-6
E2 = -0.447 + s / 2 * np.log10(c); E3 = 0.771
pH3 = 14 + np.log10((2.79e-39 / c) ** (1 / 3)); pH2 = 14 + np.log10((4.87e-17 / c) ** 0.5)
E4 = lambda pH: E3 - 3 * s * (pH - pH3)
E5 = lambda pH: E2 - s * (pH - pH2)
E6 = lambda pH: E4(pH2) - s * (pH - pH2)
f, ax = plt.subplots(figsize=(6.4, 4.2)); pH = np.linspace(0, 14, 100)
ax.plot([0, pH2], [E2, E2], color=TUA, lw=2); ax.plot([0, pH3], [E3, E3], color=TUA, lw=2); ax.plot([pH3, pH3], [E3, 1.6], color=TUA, lw=2)
p = np.linspace(pH3, pH2, 50); ax.plot(p, E4(p), color=TUA, lw=2); ax.plot([pH2, pH2], [E2, E4(pH2)], color=TUA, lw=2)
p = np.linspace(pH2, 14, 50); ax.plot(p, E5(p), color=TUA, lw=2); ax.plot(p, E6(p), color=TUA, lw=2)
ax.plot(pH, 1.229 - s * pH, color=BIRU, lw=1.3, ls='--'); ax.plot(pH, -s * pH, color=BIRU, lw=1.3, ls='--')
ax.text(13.9, 1.229 - s * 13.9 + 0.05, 'O$_2$/H$_2$O', color=BIRU, fontsize=8.5, ha='right'); ax.text(5.0, -s * 5.0 + 0.05, 'H$_2$O/H$_2$', color=BIRU, fontsize=8.5, ha='center')
ax.fill_between([0, pH2], [-1.2, -1.2], [E2, E2], color=MUDA, alpha=0.25)
p = np.linspace(pH2, 14, 50); ax.fill_between(p, -1.2, E5(p), color=MUDA, alpha=0.25)
ax.text(5, -0.95, 'Fe (kebal, tidak berkarat)', fontsize=9.5, color=BIRU, ha='center')
ax.text(1.4, 0.1, 'Fe$^{2+}$\n(korosi)', fontsize=10, color=JT, ha='center'); ax.text(1.5, 1.32, 'Fe$^{3+}$\n(korosi)', fontsize=10, color=JT, ha='center')
ax.text(10.0, 0.12, 'Fe(OH)$_3$ / Fe$_2$O$_3$\n(pasif: lapisan oksida)', fontsize=9.5, color=HJ, ha='center'); ax.text(12.2, -0.62, 'Fe(OH)$_2$', fontsize=9, color=HJ, ha='center')
ax.axvline(7, color='#bbbbbb', lw=0.8, ls=':'); ax.plot(7, 1.229 - s * 7, 'o', color=BIRU, ms=5)
ax.set_xlim(0, 14); ax.set_ylim(-1.2, 1.6); ax.set_xlabel('pH'); ax.set_ylabel('$E$ (V terhadap SHE)'); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); f.savefig(f'{R}/bab13/fig/pourbaix.png', dpi=220, bbox_inches='tight'); plt.close(f)
print('E2', E2, 'pH3', pH3, 'pH2', pH2, 'E4(pH2)', E4(pH2))
