# Gambar tambahan Bab 6: entropi gas ideal terhadap suhu dan volume
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R0 = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
R = 8.314
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0)); T = np.linspace(298.15, 1000, 200)
a1.plot(T, 1.5 * R * np.log(T / 298.15), color=BIRU, lw=2.2, label='gas monoatomik, $V$ tetap ($\\frac{3}{2}R$)')
a1.plot(T, 2.5 * R * np.log(T / 298.15), color=JT, lw=2.2, label='gas monoatomik, $p$ tetap ($\\frac{5}{2}R$)')
a1.plot(T, 3.5 * R * np.log(T / 298.15), color=HJ, lw=2.0, ls='--', label='gas diatomik, $p$ tetap ($\\frac{7}{2}R$)')
a1.set_xlabel('$T_2$ (K), dari 298 K'); a1.set_ylabel('$\\Delta S_\\mathrm{m}$ (J K$^{-1}$ mol$^{-1}$)'); a1.legend(frameon=False, fontsize=7.6, loc='upper left'); a1.set_ylim(0, 42)
r = np.logspace(-1, 2, 200); a2.semilogx(r, R * np.log(r), color=BIRU, lw=2.2); a2.axhline(0, color='#999999', lw=0.8)
for rr in [2, 10]: a2.plot(rr, R * np.log(rr), 'o', color=JT, ms=5); a2.text(rr * 1.15, R * np.log(rr) - 3, f'{R*np.log(rr):.2f}'.replace('.', ','), fontsize=8.3, color=JT)
a2.text(0.12, 30, 'isotermal: $\\Delta S_\\mathrm{m} = R\\ln(V_2/V_1)$', fontsize=8.3, color=TUA)
a2.set_xlabel('$V_2/V_1$'); a2.set_ylabel('$\\Delta S_\\mathrm{m}$ (J K$^{-1}$ mol$^{-1}$)')
for ax in (a1, a2): ax.yaxis.set_major_formatter(kom)
a1.xaxis.set_major_formatter(kom); a2.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',')))
f.tight_layout(); f.savefig(f'{R0}/bab06/fig/STV.png', dpi=220, bbox_inches='tight'); plt.close(f)
print('ok bab06c')
