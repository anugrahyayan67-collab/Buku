# Gambar Bab 12: python3 alat/gambar/bab12.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab12', 'fig')
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
R = 8.314; T = 298.15; RT = R * T
def simpan(f, n): f.tight_layout(); f.savefig(f'{D}/{n}.png'); plt.close(f)
def sumbu(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
# 12.1 G terhadap kemajuan reaksi N2O4 -> 2NO2 pada 298 K, 1 bar; G relatif terhadap N2O4 murni
GfN, GfD = 97.89e3, 51.31e3
xi = np.linspace(1e-6, 1 - 1e-6, 400); nD, nN = 2 * xi, 1 - xi; nt = nD + nN
G = nN * (GfN + RT * np.log(nN / nt)) + nD * (GfD + RT * np.log(nD / nt))
Gl = nN * GfN + nD * GfD
f, ax = plt.subplots(figsize=(5.2, 3.7), dpi=220)
ax.plot(xi, (G - GfN) / 1000, color=BIRU, lw=2.6); ax.plot(xi, (Gl - GfN) / 1000, color=JT, lw=1.6, ls='--')
i = np.argmin(G); ax.plot([xi[i]], [(G[i] - GfN) / 1000], 'o', color=HJ, ms=6, zorder=5)
ax.annotate('kesetimbangan', (xi[i], (G[i] - GfN) / 1000), (0.3, 1.6), color=HJ, fontsize=9, arrowprops=dict(arrowstyle='->', color=HJ))
ax.text(0.55, 3.3, 'tanpa pencampuran', color=JT, fontsize=9, rotation=17); ax.text(0.62, -0.6, 'dengan pencampuran', color=BIRU, fontsize=9)
ax.set_xlim(0, 1); ax.set_xlabel(r'kemajuan reaksi $\xi$ (mol)'); ax.set_ylabel(r'$G - G(\mathrm{N_2O_4})$ (kJ)'); sumbu(ax); simpan(f, 'gxi')
# 12.2 plot van 't Hoff
Ti = np.linspace(280, 800, 100)
dCp = -45.47; lnK1 = 32900 / RT; dH = -92220
lnKa = lambda TT: lnK1 - (dH - dCp * T) / R * (1 / TT - 1 / T) + dCp / R * np.log(TT / T)
lnKn = lambda TT: -4730 / RT - 57200 / R * (1 / TT - 1 / T)
f, ax = plt.subplots(figsize=(5.2, 3.7), dpi=220)
ax.plot(1000 / Ti, lnKa(Ti), color=BIRU, lw=2.4); Tn = np.linspace(280, 450, 50); ax.plot(1000 / Tn, lnKn(Tn), color=JT, lw=2.4)
ax.text(2.0, -6, r'$\mathrm{N_2 + 3H_2 \rightarrow 2NH_3}$' + '\n(eksoterm)', color=BIRU, fontsize=9); ax.text(2.45, 8.0, r'$\mathrm{N_2O_4 \rightarrow 2NO_2}$' + '\n(endoterm)', color=JT, fontsize=9)
ax.axhline(0, color='#888', lw=0.8, ls=':')
ax.set_xlabel(r'1000/T ($\mathrm{K^{-1}}$)'); ax.set_ylabel('ln K'); sumbu(ax); simpan(f, 'vanthoff')
# 12.3 fraksi mol NH3 pada kesetimbangan
def solve(fn, a, b):
    for _ in range(80):
        c = (a + b) / 2
        if fn(a) * fn(c) <= 0: b = c
        else: a = c
    return c
def xNH3(TT, p):
    K = np.exp(lnKa(TT)); fn = lambda e: (2 * e) ** 2 * (4 - 2 * e) ** 2 / ((1 - e) * (3 - 3 * e) ** 3) / p ** 2 - K
    e = solve(fn, 1e-12, 1 - 1e-12); return 2 * e / (4 - 2 * e)
Tt = np.linspace(573, 873, 80)
f, ax = plt.subplots(figsize=(5.2, 3.7), dpi=220)
for p, c in [(10, MUDA), (100, BIRU), (300, TUA), (1000, JT)]:
    y = [xNH3(t, p) for t in Tt]; ax.plot(Tt - 273.15, y, color=c, lw=2.4); ax.text(Tt[3] - 273.15 + 2, y[3] + 0.01, f'{p} bar', color=c, fontsize=9)
ax.axvspan(400, 500, color=JG, alpha=0.15, lw=0); ax.text(405, 0.86, 'rentang\nindustri', fontsize=8.5, color=JT)
ax.set_xlim(300, 600); ax.set_ylim(0, 0.95); ax.set_xlabel('T (°C)'); ax.set_ylabel(r'fraksi mol $\mathrm{NH_3}$ pada kesetimbangan'); sumbu(ax); simpan(f, 'haber')
