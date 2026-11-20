# Gambar Bab 9: python3 alat/gambar/bab09.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab09', 'fig')
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
VE0, VW0 = 58.68, 18.07; A0, A1, A2 = -4.0, -0.2, 0.1
VE = lambda x: x * (1 - x) * (A0 + A1 * (2 * x - 1) + A2 * (2 * x - 1) ** 2)
def part(x, h=1e-6):
    d = (VE(x + h) - VE(x - h)) / (2 * h); return VE0 + VE(x) + (1 - x) * d, VW0 + VE(x) - x * d
# 9.1 volume pencampuran dan metode titik potong
x = np.linspace(0, 1, 300); x0 = 0.3; d = (VE(x0 + 1e-6) - VE(x0 - 1e-6)) / 2e-6
f, ax = plt.subplots(figsize=(5.2, 3.6), dpi=220)
ax.axhline(0, color='#888', lw=0.8)
ax.plot(x, VE(x), color=BIRU, lw=2.4)
xt = np.linspace(0, 1, 2); ax.plot(xt, VE(x0) + d * (xt - x0), color=JT, lw=1.6, ls='--')
ax.plot([x0], [VE(x0)], 'o', color=JT, ms=6, zorder=5)
ax.plot([0, 1], [VE(x0) - d * x0, VE(x0) + d * (1 - x0)], 's', color=HJ, ms=6, zorder=5, clip_on=False)
ax.annotate(r'$V_\mathrm{air} - V^*_\mathrm{m,air}$', (0, VE(x0) - d * x0), (0.06, -1.55), fontsize=9, color=HJ, arrowprops=dict(arrowstyle='->', color=HJ))
ax.annotate(r'$V_\mathrm{etanol} - V^*_\mathrm{m,etanol}$', (1, VE(x0) + d * (1 - x0)), (0.52, -1.75), fontsize=9, color=HJ, arrowprops=dict(arrowstyle='->', color=HJ))
ax.set_xlim(0, 1); ax.set_ylim(-2.2, 0.3)
ax.set_xlabel('fraksi mol etanol'); ax.set_ylabel(r'$\Delta_\mathrm{mix}V_\mathrm{m}$ (cm$^3$ mol$^{-1}$)')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); f.savefig(f'{D}/vmix.png'); plt.close(f)
# 9.2 volume molar parsial
x = np.linspace(0.001, 0.999, 300); P = np.array([part(t) for t in x])
f, ax = plt.subplots(figsize=(5.2, 3.6), dpi=220); ax2 = ax.twinx(); ax2.spines['right'].set_visible(True); ax2.spines['top'].set_visible(False)
ax.plot(x, P[:, 0], color=BIRU, lw=2.4); ax2.plot(x, P[:, 1], color=JT, lw=2.4)
ax.set_xlabel('fraksi mol etanol'); ax.set_ylabel(r'$V_\mathrm{etanol}$ (cm$^3$ mol$^{-1}$)', color=BIRU); ax2.set_ylabel(r'$V_\mathrm{air}$ (cm$^3$ mol$^{-1}$)', color=JT)
ax.set_ylim(54.5, 59); ax2.set_ylim(13.5, 18.5)
for a in (ax, ax2): a.yaxis.set_major_formatter(kom)
ax.xaxis.set_major_formatter(kom)
ax.text(0.2, 56.6, 'etanol', color=BIRU, fontsize=10, ha='right'); ax2.text(0.84, 15.9, 'air', color=JT, fontsize=10)
f.tight_layout(); f.savefig(f'{D}/vparsial.png'); plt.close(f)
# 9.3 koefisien fugasitas van der Waals
def phi(a, b, p, T=298.15):
    Rl = 0.08314; Ap = a * p / (Rl * T) ** 2; Bp = b * p / (Rl * T)
    r = np.roots([1, -(1 + Bp), Ap, -Ap * Bp]); Z = max(t.real for t in r if abs(t.imag) < 1e-9)
    return np.exp(Z - 1 - np.log(Z - Bp) - Ap / Z)
p = np.linspace(0.5, 600, 300)
f, ax = plt.subplots(figsize=(5.2, 3.6), dpi=220)
for g, a, b, c in [('H₂', 0.2476, 0.02661, HJ), ('N₂', 1.370, 0.0387, BIRU), ('CH₄', 2.283, 0.04278, JT)]:
    y = [phi(a, b, t) for t in p]; ax.plot(p, y, color=c, lw=2.4); ax.text(605, y[-1], g, color=c, fontsize=10, va='center')
ax.axhline(1, color='#888', lw=0.8, ls=':'); ax.text(250, 1.012, 'gas ideal', fontsize=8.5, color='#666')
ax.set_xlim(0, 650); ax.set_xlabel('p (bar)'); ax.set_ylabel('koefisien fugasitas φ')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); f.savefig(f'{D}/phi.png'); plt.close(f)
