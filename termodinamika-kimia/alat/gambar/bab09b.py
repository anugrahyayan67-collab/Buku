# Gambar tambahan Bab 9 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab09/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
Rg = 8.314

# 1. μ_A - μ_A* terhadap x_A dalam campuran ideal
f, ax = plt.subplots(figsize=(6.0, 3.1)); x = np.linspace(0.001, 1, 400)
for T, c in [(298.15, BIRU), (400, JT)]: ax.plot(x, Rg * T * np.log(x) / 1000, color=c, lw=2.2, label=f'{T:g} K'.replace('.', ','))
ax.axhline(0, color='#999999', lw=0.8); ax.set_ylim(-12, 1); ax.set_xlim(0, 1)
ax.annotate('turun tanpa batas\nbila A sangat encer', (0.02, -9.7), (0.15, -10.5), fontsize=8.5, color=TUA, arrowprops=dict(arrowstyle='->', color=TUA, lw=0.8))
ax.annotate('zat murni: μ = μ*', (1, 0), (0.62, 0.45), fontsize=8.5, color='#555555', arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8))
ax.set_xlabel('fraksi mol $x_\\mathrm{A}$'); ax.set_ylabel('$\\mu_\\mathrm{A} - \\mu_\\mathrm{A}^*$ (kJ mol$^{-1}$)'); ax.legend(frameon=False, fontsize=8.5, loc='lower right'); koma(ax)
f.tight_layout(); simpan(f, 'mux')

# 2. μ gas nyata (van der Waals, CO2 300 K) dan ideal terhadap p; selisih = RT ln φ
a, b, T = 3.640, 0.04267, 300.0; Rl = 0.08314
p = np.linspace(0.5, 60, 300)
def Vm(pp):
    r = np.roots([pp, -(pp * b + Rl * T), a, -a * b]); r = r[np.isreal(r)].real; return r.max()
lnphi = []
for pp in p:
    V = Vm(pp); Z = pp * V / (Rl * T); lnphi.append(Z - 1 - np.log(Z * (1 - b / V)) - a / (Rl * T * V))
lnphi = np.array(lnphi)
f, ax = plt.subplots(figsize=(6.0, 3.1))
ax.plot(p, Rg * T * np.log(p) / 1000, color=BIRU, lw=2, ls='--', label='gas ideal: $RT\\ln(p/p^\\circ)$')
ax.plot(p, Rg * T * (np.log(p) + lnphi) / 1000, color=JT, lw=2.2, label='CO$_2$ nyata: $RT\\ln(f/p^\\circ)$')
i = np.argmin(abs(p - 45)); ax.annotate('', (45, Rg * T * (np.log(45) + lnphi[i]) / 1000), (45, Rg * T * np.log(45) / 1000), arrowprops=dict(arrowstyle='<->', color=HJ, lw=1.2))
ax.annotate('$RT\\ln\\varphi$ < 0: tarikan\nmenurunkan μ', (45.3, Rg * T * (np.log(45) + lnphi[i] / 2) / 1000), (36, 6.3), color=HJ, fontsize=8.5, arrowprops=dict(arrowstyle='->', color=HJ, lw=0.8))
ax.set_xlabel('$p$ (bar)'); ax.set_ylabel('$\\mu - \\mu^\\circ$ (kJ mol$^{-1}$)'); ax.set_xlim(0, 60); ax.legend(frameon=False, fontsize=8.5, loc='lower right'); koma(ax)
f.tight_layout(); simpan(f, 'mufug')
print('ok bab09b', np.exp(lnphi[i]))
