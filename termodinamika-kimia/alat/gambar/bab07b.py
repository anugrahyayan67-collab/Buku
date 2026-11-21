# Gambar tambahan Bab 7 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab07/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)

# 1. peta tanda ΔH dan ΔS
f, ax = plt.subplots(figsize=(6.0, 4.0)); ax.set_xlim(-1, 1); ax.set_ylim(-1, 1)
ax.axhline(0, color=TUA, lw=1.2); ax.axvline(0, color=TUA, lw=1.2)
for sp in ax.spines.values(): sp.set_visible(False)
ax.set_xticks([]); ax.set_yticks([])
ax.fill([0, 1, 1, 0], [0, 0, -1, -1], color='#e6f2e9'); ax.fill([-1, 0, 0, -1], [0, 0, 1, 1], color='#fbe3d4')
Q = [(0.5, -0.5, 'Δ$H$ < 0, Δ$S$ > 0\nspontan pada semua suhu\n(pembakaran)', HJ), (-0.5, 0.5, 'Δ$H$ > 0, Δ$S$ < 0\ntidak spontan pada suhu berapa pun\n(N$_2$ + 2O$_2$ → 2NO$_2$)', JT),
     (0.5, 0.5, 'Δ$H$ > 0, Δ$S$ > 0\nspontan pada suhu tinggi\n$T > \\Delta H/\\Delta S$\n(es mencair, CaCO$_3$ terurai)', BIRU), (-0.5, -0.5, 'Δ$H$ < 0, Δ$S$ < 0\nspontan pada suhu rendah\n$T < \\Delta H/\\Delta S$\n(air membeku, sintesis NH$_3$)', BIRU)]
for x, y, t, c in Q: ax.text(x, y, t, ha='center', va='center', fontsize=8.8, color=c)
ax.text(1.0, 0.04, 'Δ$S$ →', ha='right', va='bottom', fontsize=10); ax.text(0.03, 1.0, 'Δ$H$ ↑', ha='left', va='top', fontsize=10)
ax.text(0, -1.08, 'Δ$G$ = Δ$H$ − $T$Δ$S$', ha='center', fontsize=10, color=TUA)
simpan(f, 'kuadran')

# 2. G_m terhadap tekanan: gas ideal dan cairan (air, 298 K), relatif terhadap 1 bar
f, ax = plt.subplots(figsize=(6.0, 3.1)); p = np.linspace(0.05, 10, 400); Rg = 8.314; T = 298.15
ax.plot(p, Rg * T * np.log(p) / 1000, color=BIRU, lw=2.2, label='gas ideal: $RT\\ln(p/p^\\circ)$')
ax.plot(p, 18.07e-6 * (p - 1) * 1e5 / 1000, color=JT, lw=2.2, label='air cair: $V_\\mathrm{m}(p - p^\\circ)$')
ax.axhline(0, color='#999999', lw=0.8); ax.axvline(1, color='#999999', lw=0.8, ls=':')
ax.set_xlabel('$p$ (bar)'); ax.set_ylabel('$G_\\mathrm{m}(p) - G_\\mathrm{m}(1\\ \\mathrm{bar})$ (kJ mol$^{-1}$)'); ax.set_xlim(0, 10); ax.set_ylim(-7, 7); ax.legend(frameon=False, fontsize=8.5, loc='lower right'); koma(ax)
f.tight_layout(); simpan(f, 'Gp')

# 3. diagram Ellingham sederhana (ΔH°, ΔS° 298 K dianggap tetap), per mol O2
f, ax = plt.subplots(figsize=(6.4, 3.6)); T = np.linspace(300, 2000, 50)
L = [('2C + O$_2$ → 2CO', -221.06, 178.7, HJ), ('C + O$_2$ → CO$_2$', -393.51, 2.86, TUA), ('2Fe + O$_2$ → 2FeO', -544.0, -138.2, JT), ('$\\frac{4}{3}$Al + O$_2$ → $\\frac{2}{3}$Al$_2$O$_3$', -1117.1, -209.0, BIRU)]
for t, H, S, c in L:
    G = H - T * S / 1000; ax.plot(T, G, color=c, lw=2.2); ax.text(2010, G[-1], t, fontsize=8.3, color=c, va='center')
Tx = (-221.06 + 544.0) / (178.7 - 138.2) * 1000 / 1000
Tx = (-544.0 + 221.06) / (-(178.7) / 1000 - (-138.2) / 1000) if False else (544.0 - 221.06) / ((178.7 + 138.2) / 1000)
ax.plot(Tx, -221.06 - Tx * 0.1787, 'o', color=JT, ms=6); ax.annotate(f'≈ {Tx:.0f} K: di atas suhu ini\nC mereduksi FeO'.replace('.', ','), (Tx, -221.06 - Tx * 0.1787), (430, -760), fontsize=8.3, color=JT, arrowprops=dict(arrowstyle='->', color=JT, lw=0.8))
ax.set_xlabel('$T$ (K)'); ax.set_ylabel('Δ$G$° (kJ per mol O$_2$)'); ax.set_xlim(300, 2000); ax.set_ylim(-1100, -200); koma(ax)
f.tight_layout(); simpan(f, 'ellingham')
print('ok bab07b', Tx)
