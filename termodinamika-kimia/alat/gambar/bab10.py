# Gambar Bab 10: python3 alat/gambar/bab10.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab10', 'fig')
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
# 10.1 hukum Raoult benzena–toluena 25 °C
x = np.linspace(0, 1, 100); pB, pT = 12.7, 3.79
f, ax = plt.subplots(figsize=(5.2, 3.6), dpi=220)
ax.plot(x, x * pB + (1 - x) * pT, color=TUA, lw=2.6); ax.plot(x, x * pB, color=BIRU, lw=2, ls='--'); ax.plot(x, (1 - x) * pT, color=JT, lw=2, ls='--')
ax.text(0.55, 9.6, 'tekanan total', color=TUA, fontsize=9.5, rotation=27); ax.text(0.62, 6.6, 'benzena', color=BIRU, fontsize=9.5); ax.text(0.12, 3.75, 'toluena', color=JT, fontsize=9.5)
ax.set_xlim(0, 1); ax.set_ylim(0, 13.5); ax.set_xlabel('fraksi mol benzena dalam cairan'); ax.set_ylabel('tekanan uap (kPa)')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); f.savefig(f'{D}/raoult.png'); plt.close(f)
# 10.2 Raoult dan Henry pada larutan nyata (model Margules, skematis)
A, ps = 1.3, 10.0
xb = np.linspace(0.0005, 1, 300); p = xb * ps * np.exp(A * (1 - xb) ** 2)
f, ax = plt.subplots(figsize=(5.2, 3.6), dpi=220)
ax.plot(xb, p, color=TUA, lw=2.6)
ax.plot([0, 1], [0, ps], color=BIRU, lw=1.6, ls='--'); ax.plot([0, 0.55], [0, 0.55 * ps * np.exp(A)], color=JT, lw=1.6, ls='--')
ax.fill_between([0, 0.12], 0, 20, color=JG, alpha=0.15, lw=0); ax.fill_between([0.85, 1], 0, 20, color=MUDA, alpha=0.25, lw=0)
ax.text(0.55, 1.6, 'hukum Raoult\n' + r'$p_\mathrm{B} = x_\mathrm{B}p^*_\mathrm{B}$', color=BIRU, fontsize=9)
ax.text(0.25, 15.6, 'hukum Henry\n' + r'$p_\mathrm{B} = x_\mathrm{B}K_\mathrm{B}$', color=JT, fontsize=9)
ax.text(0.01, 18.8, 'larutan encer:\nHenry berlaku', fontsize=8, color=JT); ax.text(0.86, 18.8, 'hampir murni:\nRaoult berlaku', fontsize=8, color=BIRU)
ax.plot([1], [ps], 'o', color=BIRU, ms=5); ax.text(0.97, ps + 0.7, r'$p^*_\mathrm{B}$', color=BIRU, ha='right')
ax.set_xlim(0, 1); ax.set_ylim(0, 21); ax.set_xlabel(r'fraksi mol B, $x_\mathrm{B}$'); ax.set_ylabel(r'tekanan uap B, $p_\mathrm{B}$')
ax.set_yticks([]); ax.xaxis.set_major_formatter(kom)
f.tight_layout(); f.savefig(f'{D}/henry.png'); plt.close(f)
# 10.3 potensial kimia pelarut terhadap suhu: padat, cair murni, larutan, gas
T = np.linspace(0, 10, 200)
f, ax = plt.subplots(figsize=(5.2, 3.6), dpi=220)
s = lambda T: 1.0 - 0.25 * T; l = lambda T: 2.0 - 0.45 * T; g = lambda T: 5.6 - 0.9 * T; dl = 0.45
ax.plot(T, s(T), color=TUA, lw=2.4); ax.plot(T, l(T), color=BIRU, lw=2.4); ax.plot(T, l(T) - dl, color=BIRU, lw=2.4, ls='--'); ax.plot(T, g(T), color=JT, lw=2.4)
Tf, Tf2 = 1 / 0.2, (1 - dl) / 0.2 * -1
Tf = (2.0 - 1.0) / 0.2; Tf2 = (2.0 - dl - 1.0) / 0.2; Tb = (5.6 - 2.0) / 0.45; Tb2 = (5.6 - 2.0 + dl) / 0.45
for t, c in [(Tf, '#888'), (Tf2, '#888'), (Tb, '#888'), (Tb2, '#888')]: ax.axvline(t, color=c, lw=0.8, ls=':')
ax.annotate('', xy=(Tf2, -3.2), xytext=(Tf, -3.2), arrowprops=dict(arrowstyle='->', color=HJ, lw=1.6)); ax.text((Tf + Tf2) / 2, -3.05, r'$\Delta T_\mathrm{f}$', color=HJ, ha='center', fontsize=9)
ax.annotate('', xy=(Tb2, -3.2), xytext=(Tb, -3.2), arrowprops=dict(arrowstyle='->', color=HJ, lw=1.6)); ax.text((Tb + Tb2) / 2, -3.05, r'$\Delta T_\mathrm{b}$', color=HJ, ha='center', fontsize=9)
ax.text(8.3, -0.85, 'padat', color=TUA, fontsize=9.5); ax.text(0.3, 2.15, 'cair murni', color=BIRU, fontsize=9.5); ax.text(5.9, -1.85, 'larutan', color=BIRU, fontsize=9.5); ax.text(4.3, 2.0, 'gas', color=JT, fontsize=9.5)
ax.set_xlim(0, 10); ax.set_ylim(-3.6, 3.2); ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel('suhu, T'); ax.set_ylabel(r'potensial kimia pelarut, $\mu_\mathrm{A}$')
f.tight_layout(); f.savefig(f'{D}/muT.png'); plt.close(f)
