#!/usr/bin/env python3
# Gambar Bab 7 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from math import pi, factorial
from scipy.special import genlaguerre, sph_harm_y
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
def R(n, l, r):
    rho = 2 * r / n; N = np.sqrt((2 / n) ** 3 * factorial(n - l - 1) / (2 * n * factorial(n + l)))
    return N * np.exp(-rho / 2) * rho ** l * genlaguerre(n - l - 1, 2 * l + 1)(rho)

# 1. potensial efektif
f, ax = plt.subplots(figsize=(5.6, 3.0)); sp(ax); r = np.linspace(0.05, 25, 800)
for l, col in [(0, B), (1, H), (2, J2)]:
    ax.plot(r, -1 / r + l * (l + 1) / (2 * r * r), color=col, lw=1.6, label=f'$\\ell = {l}$')
for n in [1, 2, 3]: ax.axhline(-0.5 / n ** 2, color='#999', lw=.7, ls='--'); ax.text(25.3, -0.5 / n ** 2, f'$n = {n}$', va='center', fontsize=8)
ax.set_ylim(-0.6, 0.15); ax.set_xlim(0, 25); ax.set_xlabel('$r$ ($a_0$)'); ax.set_ylabel('$V_\\mathrm{ef}$ ($E_h$)')
ax.legend(frameon=False, fontsize=8, loc='lower right'); koma(ax); sv(f, 'c_veff.png')

# 2. fungsi radial dan distribusi radial
f, axs = plt.subplots(2, 3, figsize=(6.8, 4.0), sharex='col')
r = np.linspace(0, 30, 1200)
for j, n in enumerate([1, 2, 3]):
    for l, col in [(0, B), (1, H), (2, J2)]:
        if l >= n: continue
        lab = f'{n}{"spd"[l]}'
        axs[0, j].plot(r, R(n, l, r), color=col, lw=1.4, label=lab)
        axs[1, j].plot(r, r * r * R(n, l, r) ** 2, color=col, lw=1.4, label=lab)
        axs[1, j].axvline(0.5 * (3 * n * n - l * (l + 1)), color=col, lw=.7, ls=':')
    xm = [5, 15, 25][j]
    for i in range(2):
        sp(axs[i, j]); axs[i, j].set_xlim(0, xm); koma(axs[i, j]); axs[i, j].legend(frameon=False, fontsize=7.5)
    axs[0, j].axhline(0, color='#999', lw=.6); axs[1, j].set_xlabel('$r$ ($a_0$)')
axs[0, 0].set_ylabel('$R_{n\\ell}(r)$'); axs[1, 0].set_ylabel('$r^2R_{n\\ell}^2$')
f.tight_layout(); sv(f, 'c_radial.png')

# 3. penampang orbital (bidang xz) dan permukaan batas
f, axs = plt.subplots(2, 3, figsize=(6.8, 4.6))
lst = [(2, 0, 0, '2s', 12), (2, 1, 0, '2p$_z$', 14), (3, 1, 0, '3p$_z$', 26), (3, 2, 0, '3d$_{z^2}$', 26), (3, 2, 1, '3d$_{xz}$', 26), (4, 3, 0, '4f$_{z^3}$', 40)]
for ax, (n, l, m, t, L) in zip(axs.flat, lst):
    x = np.linspace(-L, L, 400); X, Z = np.meshgrid(x, x); rr = np.sqrt(X ** 2 + Z ** 2) + 1e-9; th = np.arccos(Z / rr)
    if m == 0: Y = np.real(sph_harm_y(l, 0, th, 0 * th))
    else: Y = np.sqrt(2) * (-1) ** m * np.real(sph_harm_y(l, m, th, np.where(X >= 0, 0, pi)))
    psi = R(n, l, rr) * Y; vmax = np.abs(psi).max() * 0.6
    ax.contourf(X, Z, psi, levels=np.linspace(-vmax, vmax, 21), cmap=matplotlib.colors.LinearSegmentedColormap.from_list('bj', [J2, J1, '#ffffff', MUDA, B]), extend='both')
    ax.contour(X, Z, psi, levels=[0], colors=TUA, linewidths=.6, linestyles='--')
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(t, fontsize=9)
    for s in ax.spines.values(): s.set_color('#ccc')
f.tight_layout(); sv(f, 'c_orbital.png')

# 4. diagram tingkat dan deret spektrum
f, ax = plt.subplots(figsize=(6.2, 3.6)); sp(ax); ax.spines['bottom'].set_visible(False)
for n in range(1, 8):
    E = -13.606 / n ** 2; ax.plot([0, 10], [E, E], color=TUA if n < 7 else '#999', lw=1.1)
    if n <= 5: ax.text(10.15, E, f'$n = {n}$', va='center', fontsize=7.5)
ax.plot([0, 10], [0, 0], color='#999', lw=.8, ls='--'); ax.text(10.15, 0.2, 'ionisasi', fontsize=7.5)
for i, nu in enumerate(range(2, 7)): x = 0.6 + 0.35 * i; ax.annotate('', xy=(x, -13.606), xytext=(x, -13.606 / nu ** 2), arrowprops=dict(arrowstyle='->', color=B, lw=1))
for i, nu in enumerate(range(3, 8)): x = 3.6 + 0.35 * i; ax.annotate('', xy=(x, -3.4015), xytext=(x, -13.606 / nu ** 2), arrowprops=dict(arrowstyle='->', color=J2, lw=1))
for i, nu in enumerate(range(4, 8)): x = 6.6 + 0.35 * i; ax.annotate('', xy=(x, -1.5118), xytext=(x, -13.606 / nu ** 2), arrowprops=dict(arrowstyle='->', color=H, lw=1))
ax.text(1.2, -12.2, 'Lyman\n(UV)', color=B, fontsize=8); ax.text(4.2, -5.3, 'Balmer\n(tampak)', color=J2, fontsize=8); ax.text(7.0, -2.6, 'Paschen\n(IR)', color=H, fontsize=8)
ax.set_xticks([]); ax.set_ylabel('$E$ (eV)'); ax.set_ylim(-14.3, 0.8); koma(ax); sv(f, 'c_spektrum.png')

# 5. Zeeman normal
f, axs = plt.subplots(1, 2, figsize=(6.4, 2.8), gridspec_kw={'width_ratios': [1.4, 1]})
ax = axs[0]; ax.axis('off')
ax.plot([0, 1], [3, 3], color=TUA, lw=1.4); ax.text(-0.05, 3, '2p', ha='right', va='center')
for m in [-1, 0, 1]: ax.plot([1.6, 2.6], [3 + 0.35 * m, 3 + 0.35 * m], color=TUA, lw=1.4); ax.text(2.7, 3 + 0.35 * m, f'$m = {m:+d}$'.replace('+0', '0').replace('-', '−'), va='center', fontsize=8)
for m in [-1, 0, 1]: ax.plot([1.0, 1.6], [3, 3 + 0.35 * m], color='#bbb', lw=.7)
ax.plot([0, 1], [0, 0], color=TUA, lw=1.4); ax.plot([1.6, 2.6], [0, 0], color=TUA, lw=1.4); ax.text(-0.05, 0, '1s', ha='right', va='center'); ax.text(2.7, 0, '$m = 0$', va='center', fontsize=8)
for k, (m, col) in enumerate([(1, B), (0, H), (-1, J2)]): ax.annotate('', xy=(1.9 + 0.25 * k, 0), xytext=(1.9 + 0.25 * k, 3 + 0.35 * m), arrowprops=dict(arrowstyle='->', color=col, lw=1.2))
ax.text(0.5, 3.6, '$B = 0$', ha='center', fontsize=8); ax.text(2.1, 3.75, '$B > 0$', ha='center', fontsize=8); ax.set_xlim(-0.4, 3.3); ax.set_ylim(-0.4, 4)
ax = axs[1]; sp(ax); ax.vlines([-1, 0, 1], 0, [1, 1, 1], colors=[J2, H, B], lw=2.5)
ax.set_xlim(-2, 2); ax.set_ylim(0, 1.3); ax.set_yticks([]); ax.set_xticks([-1, 0, 1]); ax.set_xticklabels(['$-\\mu_BB$', '0', '$+\\mu_BB$'])
ax.set_xlabel('pergeseran energi foton'); ax.set_title('triplet Zeeman normal', fontsize=8.5)
sv(f, 'c_zeeman.png')

# 6. metode tembak radial
f, ax = plt.subplots(figsize=(5.2, 2.6)); sp(ax)
def nr(E, r, l):
    h = r[1] - r[0]; g = 2 * (-1 / r - E) + l * (l + 1) / r ** 2; ff = 1 - h * h / 12 * g; u = np.zeros_like(r); u[0], u[1] = r[0], r[1]
    for i in range(1, len(r) - 1): u[i + 1] = ((12 - 10 * ff[i]) * u[i] - ff[i - 1] * u[i - 1]) / ff[i + 1]
    return u
r = np.arange(1, 6001) * 0.002
for E, col, lb in [(-0.47, J2, '$E = -0{,}47$'), (-0.50, B, '$E = -0{,}50$ (tepat)'), (-0.53, H, '$E = -0{,}53$')]:
    u = nr(E, r, 0); u /= np.max(np.abs(u[r < 2])); ax.plot(r, u, color=col, lw=1.4, label=lb)
ax.set_xlim(0, 12); ax.set_ylim(-1.5, 1.8); ax.axhline(0, color='#999', lw=.6); ax.set_xlabel('$r$ ($a_0$)'); ax.set_ylabel('$u(r)$ (tak dinormalkan)')
ax.legend(frameon=False, fontsize=7.5); koma(ax); sv(f, 'c_tembak.png')
print('gambar selesai')
