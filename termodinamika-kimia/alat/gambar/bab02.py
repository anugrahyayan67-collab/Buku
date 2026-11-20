# Gambar 2.3 (revisi 1.1): isoterm van der Waals tereduksi dengan konstruksi Maxwell
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.optimize import brentq
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
pr = lambda V, T: 8 * T / (3 * V - 1) - 3 / V ** 2

def maxwell(T):
    def akar(p):
        r = np.roots([3 * p, -(p + 8 * T), 9, -3]); r = np.sort(r[abs(r.imag) < 1e-9].real); return r[0], r[-1]
    def selisih(p):
        Vl, Vg = akar(p)
        Vv = np.linspace(Vl, Vg, 4001); return np.trapezoid(pr(Vv, T) - p, Vv)
    V = np.linspace(0.45, 5, 4000); P = pr(V, T); d = np.diff(P)
    i1 = np.where((d[:-1] < 0) & (d[1:] > 0))[0][0]; i2 = np.where((d[:-1] > 0) & (d[1:] < 0))[0][0]
    p = brentq(selisih, max(P[i1], 1e-4) + 1e-6, P[i2] - 1e-6); return p, akar(p)

f, ax = plt.subplots(figsize=(5.0, 3.4), dpi=220)
V = np.linspace(0.42, 5, 1500)
warna = {0.85: TUA, 0.9: BIRU, 0.95: MUDA, 1.0: JT, 1.1: JG, 1.25: HJ}
for T, c in warna.items():
    ax.plot(V, pr(V, T), color=c, lw=2.4 if T == 1 else 1.6, label=f'{T:g}'.replace('.', ','))
T = 0.85; p, (Vl, Vg) = maxwell(T)
Vv = np.linspace(Vl, Vg, 800); P = pr(Vv, T)
ax.fill_between(Vv, P, p, where=P < p, color=MUDA, alpha=0.45, lw=0)
ax.fill_between(Vv, P, p, where=P > p, color=JG, alpha=0.45, lw=0)
ax.plot([Vl, Vg], [p, p], color=TUA, lw=1.4, ls='--')
ax.plot([Vl, Vg], [p, p], 'o', color=TUA, ms=4)
ax.text(Vl - 0.05, p + 0.08, 'cair', ha='right', fontsize=8.5, color=TUA)
ax.text(Vg + 0.08, p + 0.06, 'gas', fontsize=8.5, color=TUA)
ax.annotate('kedua luas berarsir\nsama besar', (0.75, 0.3), (1.3, 0.12), fontsize=8, color=TUA, arrowprops=dict(arrowstyle='-', color=TUA, lw=0.7)); ax.annotate('', (2.0, 0.56), (1.75, 0.26), arrowprops=dict(arrowstyle='-', color=TUA, lw=0.7))
ax.plot(1, 1, 'o', color=JT); ax.text(1.08, 1.06, 'titik kritis', color=JT, fontsize=8.5)
ax.set_xlim(0.4, 5); ax.set_ylim(0, 2.2)
ax.set_xlabel('$V_m/V_c$'); ax.set_ylabel('$p/p_c$')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
ax.legend(title='$T/T_c$', frameon=False, fontsize=8.5, title_fontsize=9)
f.tight_layout(); f.savefig(f'{R}/bab02/fig/isoterm.png'); plt.close(f)
print('p_uap tereduksi', p, 'V_cair', Vl, 'V_gas', Vg)
