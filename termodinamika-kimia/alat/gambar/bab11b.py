# Gambar tambahan Bab 11 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab11/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
Rg = 8.314; T1, H1, T2, H2 = 1357.8, 13.26e3, 1728.3, 17.48e3
T = np.linspace(T1 + 0.01, T2 - 0.01, 300)
K1 = np.exp(-H1 / Rg * (1 / T - 1 / T1)); K2 = np.exp(-H2 / Rg * (1 / T - 1 / T2)); xs = (1 - K2) / (K1 - K2); xl = K1 * xs
f, ax = plt.subplots(figsize=(5.8, 3.6))
ax.plot(1 - xl, T, color=JT, lw=2.2, label='likuidus'); ax.plot(1 - xs, T, color=BIRU, lw=2.2, label='solidus')
ax.fill_betweenx(T, 1 - xl, 1 - xs, color=JG, alpha=0.18)
Tq = 1500; i = np.argmin(abs(T - Tq)); ax.plot([1 - xl[i], 1 - xs[i]], [Tq, Tq], color=TUA, lw=1, marker='o', ms=4); ax.text(1 - xs[i] + 0.02, Tq - 8, f'1500 K', fontsize=8.5, va='top')
ax.text(0.35, 1700, 'cair', fontsize=10, color=JT); ax.text(0.75, 1420, 'larutan padat', fontsize=10, color=BIRU); ax.annotate('cair + padat', (0.62, 1592), (0.66, 1490), fontsize=8.5, color='#8a5a2a', arrowprops=dict(arrowstyle='->', color='#8a5a2a', lw=0.8))
ax.set_xlabel('fraksi mol Ni'); ax.set_ylabel('$T$ (K)'); ax.set_xlim(0, 1); ax.set_ylim(1330, 1760); ax.legend(frameon=False, fontsize=8.5, loc='upper left'); koma(ax)
ax.text(0.01, 1335, 'Cu 1358 K', fontsize=8, va='bottom'); ax.text(0.99, 1335, 'Ni 1728 K', fontsize=8, va='bottom', ha='right')
f.tight_layout(); simpan(f, 'lensa')
f, ax = plt.subplots(figsize=(6.0, 3.0)); x = np.linspace(0, 8, 300)
for k, c in [(0.01, TUA), (0.1, BIRU), (0.5, JT)]: ax.plot(x, 1 - (1 - k) * np.exp(-k * x), color=c, lw=2, label=f'$k$ = {k:g}'.replace('.', ','))
ax.axhline(1, color='#999999', lw=0.8, ls=':'); ax.text(7.9, 1.03, 'kadar awal', ha='right', fontsize=8.5, color='#666666')
ax.set_xlabel('jarak dari ujung awal batang, $x/L$ (dalam panjang zona)'); ax.set_ylabel('$C/C_0$ setelah satu lintasan'); ax.set_ylim(0, 1.15); ax.set_xlim(0, 8); ax.legend(frameon=False, fontsize=8.5, loc='center right', bbox_to_anchor=(1, 0.62)); koma(ax)
f.tight_layout(); simpan(f, 'zona')
print('ok bab11b')
