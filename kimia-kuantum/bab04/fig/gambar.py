#!/usr/bin/env python3
# Gambar Bab 4 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib, itertools
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from math import pi
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'mathtext.fontset': 'dejavusans',
                     'text.color': '#0e2748', 'axes.edgecolor': '#0e2748', 'axes.labelcolor': '#0e2748',
                     'xtick.color': '#0e2748', 'ytick.color': '#0e2748'})
TUA, B, MUDA, J1, J2, H = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
KOMA = FuncFormatter(lambda x, p: ('%g' % x).replace('.', ',').replace('-', '−'))
def sv(f, n): f.savefig(n, dpi=220, bbox_inches='tight'); plt.close(f)
def sp(ax):
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
def koma(ax, x=True, y=True):
    if x: ax.xaxis.set_major_formatter(KOMA)
    if y: ax.yaxis.set_major_formatter(KOMA)

# 1. tingkat kotak kubus dan kotak sedikit memanjang
f, ax = plt.subplots(figsize=(5.6, 3.4)); ax.axis('off')
lv = {}
for n in itertools.product(range(1, 5), repeat=3):
    lv.setdefault(sum(k * k for k in n), []).append(n)
for s in sorted(lv)[:8]:
    g = len(lv[s]); ax.plot([0, 1], [s, s], color=TUA, lw=1.6); ax.text(-0.08, s, f'{s}', ha='right', va='center', fontsize=8)
    ax.text(1.08, s, f'$g = {g}$', va='center', fontsize=8, color=B)
    # kotak memanjang: c = 1.1 L pada sumbu z
    for n in lv[s]:
        e2 = n[0] ** 2 + n[1] ** 2 + n[2] ** 2 / 1.21
        ax.plot([2.0, 3.0], [e2, e2], color=J2, lw=1.3); ax.plot([1.0, 2.0], [s, e2], color='#ccc', lw=.5, ls=':')
ax.text(0.5, 21.2, 'kubus', ha='center', fontsize=9); ax.text(2.5, 21.2, '$c = 1{,}1\\,L$', ha='center', fontsize=9)
ax.text(-0.35, 12, '$E/(h^2/8mL^2)$', rotation=90, va='center', fontsize=9)
ax.set_xlim(-0.6, 3.3); ax.set_ylim(1.5, 22); sv(f, 'c_kubus.png')

# 2. kotak dua dimensi
f, axs = plt.subplots(1, 4, figsize=(6.8, 1.9))
x = np.linspace(0, 1, 120); X, Y = np.meshgrid(x, x)
for ax, (nx, ny) in zip(axs, [(1, 1), (2, 1), (1, 2), (2, 2)]):
    Z = np.sin(nx * pi * X) * np.sin(ny * pi * Y)
    ax.contourf(X, Y, Z, levels=np.linspace(-1, 1, 21), cmap='RdBu_r'); ax.contour(X, Y, Z, levels=[0], colors=TUA, linewidths=.8)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(f'$({nx}, {ny})$', fontsize=9)
sv(f, 'c_kotak2d.png')

# 3. ekspansi fungsi segitiga
f, axs = plt.subplots(1, 2, figsize=(6.6, 2.6), gridspec_kw={'width_ratios': [1.5, 1]})
ax = axs[0]; sp(ax); x = np.linspace(0, 1, 400); tri = np.sqrt(12) * np.where(x < .5, x, 1 - x)
c = {n: 4 * np.sqrt(6) / (n * pi) ** 2 * np.sin(n * pi / 2) for n in range(1, 40)}
ax.plot(x, tri, color=TUA, lw=2, label='$f(x)$')
for N, col in [(1, J2), (3, B)]:
    s = sum(c[n] * np.sqrt(2) * np.sin(n * pi * x) for n in range(1, N + 1)); ax.plot(x, s, color=col, lw=1.3, ls='--', label=f'sampai $n = {N}$')
ax.legend(frameon=False, fontsize=8); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '$L/2$', '$L$']); ax.set_ylabel('$\\sqrt{L}\\,f$'); koma(ax, x=False)
ax = axs[1]; sp(ax); ns = np.arange(1, 8); cc = np.array([c[n] ** 2 for n in ns])
ax.bar(ns, cc, color=B); ax.set_yscale('log'); ax.set_ylim(1e-4, 2); ax.set_xlabel('$n$'); ax.set_ylabel('$|c_n|^2$'); ax.set_xticks(ns)
for n, v in zip(ns, cc):
    if v > 1e-6: ax.text(n, v * 1.4, f'{v:.4f}'.replace('.', ','), ha='center', fontsize=7)
plt.tight_layout(); sv(f, 'c_ekspansi.png')

# 4. paritas
f, axs = plt.subplots(1, 4, figsize=(6.8, 1.9), sharey=True); x = np.linspace(-3.5, 3.5, 400)
Hs = [np.ones_like(x), 2 * x, 4 * x * x - 2, 8 * x ** 3 - 12 * x]; nm = ['genap', 'ganjil', 'genap', 'ganjil']
for i, ax in enumerate(axs):
    y = Hs[i] * np.exp(-x * x / 2); y /= np.max(np.abs(y))
    ax.axhline(0, color='#aaa', lw=.6); ax.axvline(0, color='#aaa', lw=.6, ls=':')
    ax.plot(x, y, color=[B, J2][i % 2], lw=1.8); ax.set_title(f'$\\psi_{i}$: {nm[i]}', fontsize=9); ax.set_xticks([]); ax.set_yticks([])
    for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
sv(f, 'c_paritas.png')

# 5. kotak dalam medan listrik (diagonalisasi)
hb = 1.054571817e-34; me = 9.1093837015e-31; e = 1.602176634e-19; h = 6.62607015e-34; L = 1e-9; Nb = 12
E0 = h ** 2 / (8 * me * L ** 2)
def Hm(F):
    M = np.zeros((Nb, Nb))
    for m in range(1, Nb + 1):
        M[m - 1, m - 1] = m * m * E0 + e * F * L / 2
        for n in range(1, Nb + 1):
            if (m + n) % 2: M[m - 1, n - 1] = e * F * (-8 * L * m * n / (pi ** 2 * (m * m - n * n) ** 2))
    return M
Fs = np.linspace(0, 1.5e9, 60); EE = np.array([np.linalg.eigvalsh(Hm(F))[:3] / e for F in Fs])
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.7))
ax = axs[0]; sp(ax)
for k, col in zip(range(3), [B, H, J2]): ax.plot(Fs / 1e9, EE[:, k] - Fs * L / 2, color=col, lw=1.8, label=f'keadaan {k + 1}')
ax.set_xlabel('medan $F$ ($10^9$ V/m)'); ax.set_ylabel('$E - eFL/2$ (eV)'); ax.legend(frameon=False, fontsize=7.5); koma(ax)
ax = axs[1]; sp(ax); x = np.linspace(0, 1, 300)
w, v = np.linalg.eigh(Hm(1.5e9)); psi = sum(v[n - 1, 0] * np.sqrt(2) * np.sin(n * pi * x) for n in range(1, Nb + 1))
ax.plot(x, 2 * np.sin(pi * x) ** 2, color='#999', lw=1.2, ls='--', label='$F = 0$'); ax.plot(x, psi ** 2, color=B, lw=1.8, label='$F = 1{,}5 \\times 10^9$ V/m')
ax.set_xticks([0, 1]); ax.set_xticklabels(['0', '$L$']); ax.set_ylabel('$L|\\psi_1|^2$'); ax.legend(frameon=False, fontsize=7.5); koma(ax, x=False)
ax.annotate('', xy=(0.15, 2.3), xytext=(0.85, 2.3), arrowprops=dict(arrowstyle='->', color=J2)); ax.text(0.5, 2.38, 'gaya pada elektron', ha='center', fontsize=7.5, color=J2)
plt.tight_layout(); sv(f, 'c_stark.png')
print('gambar selesai')
