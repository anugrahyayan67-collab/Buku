#!/usr/bin/env python3
# Gambar Bab 6 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib, math
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from math import pi
from scipy.special import sph_harm_y
def sph_harm(m, l, ph, th): return sph_harm_y(l, m, th, ph)
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

# 1. partikel pada cincin: fungsi gelombang riil dan tingkat energi (benzena)
f = plt.figure(figsize=(6.8, 2.8))
ph = np.linspace(0, 2 * pi, 400)
for i, (mm, t) in enumerate([(0, '$m = 0$'), (1, '$\\cos\\phi$  ($|m| = 1$)'), (2, '$\\cos 2\\phi$  ($|m| = 2$)'), (3, '$\\cos 3\\phi$  ($|m| = 3$)')]):
    ax = f.add_axes([0.0 + i * 0.17, 0.12, 0.16, 0.76]); ax.set_aspect('equal'); ax.axis('off')
    ax.plot(np.cos(ph), np.sin(ph), color='#bbb', lw=1)
    y = np.cos(mm * ph) * 0.35; r = 1 + y
    ax.plot(r * np.cos(ph), r * np.sin(ph), color=B, lw=1.5)
    ax.fill_between(np.cos(ph) * 0, 0, 0)
    for k in range(2 * mm):
        a = (k + 0.5) * pi / mm; ax.plot(np.cos(a), np.sin(a), 'o', color=J2, ms=3.5)
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_title(t, fontsize=8.5)
ax = f.add_axes([0.73, 0.12, 0.26, 0.78]); sp(ax)
for mm in range(0, 4):
    E = mm * mm
    for s in ([0] if mm == 0 else [-1, 1]):
        x0 = 0.5 + s * 0.35; ax.plot([x0 - 0.25, x0 + 0.25], [E, E], color=TUA, lw=1.6)
        lab = '$m = 0$' if mm == 0 else f'$m = {"+" if s > 0 else "−"}{mm}$'
        ax.text(x0, E + 0.45, lab, ha='center', fontsize=6.8)
        if mm <= 1: ax.text(x0, E - 0.05, '↑↓', ha='center', va='center', fontsize=10, color=J2, fontweight='bold')
ax.set_xticks([]); ax.set_ylabel('$E/(\\hbar^2/2I)$'); ax.set_ylim(-0.5, 10.5); ax.set_xlim(-0.2, 1.2); koma(ax)
ax.set_title('benzena: 6 elektron π', fontsize=8.5)
sv(f, 'c_cincin.png')

# 2. harmonik bola riil (permukaan |Y|)
f = plt.figure(figsize=(6.8, 4.2))
th, ph = np.meshgrid(np.linspace(0, pi, 90), np.linspace(0, 2 * pi, 120))
def real_Y(l, mm):
    if mm == 0: return np.real(sph_harm(0, l, ph, th))
    Yp = sph_harm(abs(mm), l, ph, th)
    return np.sqrt(2) * (-1) ** mm * (np.real(Yp) if mm > 0 else np.imag(Yp))
lst = [(0, 0, 's'), (1, 0, 'p$_z$'), (1, 1, 'p$_x$'), (1, -1, 'p$_y$'), (2, 0, 'd$_{z^2}$'), (2, 1, 'd$_{xz}$'), (2, 2, 'd$_{x^2-y^2}$'), (2, -2, 'd$_{xy}$')]
for i, (l, mm, t) in enumerate(lst):
    ax = f.add_subplot(2, 4, i + 1, projection='3d'); Y = real_Y(l, mm); R = np.abs(Y)
    X = R * np.sin(th) * np.cos(ph); Yc = R * np.sin(th) * np.sin(ph); Z = R * np.cos(th)
    col = np.where(Y >= 0, 1.0, 0.0); from matplotlib.colors import ListedColormap
    cm = ListedColormap([J1, B])
    ax.plot_surface(X, Yc, Z, facecolors=cm(col), rstride=2, cstride=2, linewidth=0, antialiased=True, shade=True)
    lim = R.max() * 0.85; ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1)); ax.axis('off'); ax.set_title(f'{t}  ($\\ell = {l}$)', fontsize=9, pad=-2)
    ax.view_init(elev=18, azim=30)
f.subplots_adjust(wspace=0, hspace=0.05); sv(f, 'c_harmonik.png')

# 3. model vektor l = 2
f, axs = plt.subplots(1, 2, figsize=(6.6, 3.0), gridspec_kw={'width_ratios': [1, 1.25]})
ax = axs[0]; ax.set_aspect('equal'); sp(ax); L = np.sqrt(6)
t = np.linspace(-pi / 2, pi / 2, 200); ax.plot(L * np.cos(t), L * np.sin(t), color='#bbb', lw=1, ls='--')
for mm in range(-2, 3):
    x = np.sqrt(L * L - mm * mm); ax.annotate('', xy=(x, mm), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=B, lw=1.5))
    ax.axhline(mm, color='#ddd', lw=.6, zorder=0); ax.text(-0.35, mm, f'$m = {mm}$'.replace('-', '−'), ha='right', va='center', fontsize=7.5)
ax.set_xlim(-1.5, 2.8); ax.set_ylim(-2.8, 2.8); ax.set_xticks([]); ax.set_yticks([-2, -1, 0, 1, 2]); koma(ax)
ax.set_ylabel('$L_z/\\hbar$'); ax.text(1.2, 2.55, '$|L| = \\sqrt{6}\\,\\hbar$', fontsize=8)
ax = axs[1]; ax.axis('off'); ax = f.add_subplot(1, 2, 2, projection='3d'); ax.axis('off')
for mm, col in [(2, B), (1, H), (0, J2)]:
    r = np.sqrt(6 - mm * mm); phi = np.linspace(0, 2 * pi, 100)
    ax.plot(r * np.cos(phi), r * np.sin(phi), mm * np.ones_like(phi), color=col, lw=1)
    for p0 in np.linspace(0, 2 * pi, 7)[:-1]:
        ax.plot([0, r * np.cos(p0)], [0, r * np.sin(p0)], [0, mm], color=col, lw=.5, alpha=.6)
    ax.plot([0, r], [0, 0], [0, mm], color=col, lw=1.8)
ax.plot([0, 0], [0, 0], [-0.5, 3], color=TUA, lw=1); ax.text(0, 0, 3.15, '$z$', fontsize=9)
ax.set_box_aspect((1, 1, 0.9)); ax.view_init(elev=14, azim=-60); ax.set_title('kerucut untuk $m = 2$, 1, 0', fontsize=8.5)
sv(f, 'c_vektor.png')

# 4. tingkat rotor dan spektrum gelombang mikro CO
f, axs = plt.subplots(1, 2, figsize=(6.8, 3.0), gridspec_kw={'width_ratios': [1, 1.6]})
ax = axs[0]; sp(ax); Bc = 1.9225
for J in range(6):
    E = Bc * J * (J + 1); ax.plot([0, 1], [E, E], color=TUA, lw=1.4); ax.text(1.05, E, f'$J = {J}$', va='center', fontsize=7.5)
    if J < 5:
        x = 0.15 + 0.15 * J; ax.annotate('', xy=(x, Bc * (J + 1) * (J + 2)), xytext=(x, E), arrowprops=dict(arrowstyle='->', color=B, lw=1.1))
ax.set_xticks([]); ax.set_xlim(0, 1.4); ax.set_ylabel('$E$ (cm$^{-1}$)'); koma(ax); ax.set_title('$E_J = BJ(J+1)$', fontsize=8.5)
ax = axs[1]; sp(ax); kT = 207.22
Js = np.arange(0, 30); nu = 2 * Bc * (Js + 1) - 4 * 6.12e-6 * (Js + 1) ** 3
I = (Js + 1) * np.exp(-Bc * Js * (Js + 1) * 1.4388 / 298.15) * (1 - np.exp(-1.4388 * nu / 298.15)) * nu
ax.vlines(nu, 0, I / I.max(), color=B, lw=1.4); ax.set_xlabel('bilangan gelombang (cm$^{-1}$)'); ax.set_yticks([]); koma(ax)
ax.set_title('serapan rotasi CO pada 298 K (dihitung)', fontsize=8.5); ax.set_xlim(0, 120)
sv(f, 'c_rotor.png')

# 5. populasi rotasi
f, ax = plt.subplots(figsize=(5.6, 2.8)); sp(ax)
for nm, Bv, col in [('HCl', 10.44, B), ('CO', 1.9225, J2), ('I$_2$', 0.0374, H)]:
    Js = np.arange(0, 160 if nm == 'I$_2$' else 40); p = (2 * Js + 1) * np.exp(-Bv * Js * (Js + 1) * 1.4388 / 298.15); p /= p.sum()
    ax.plot(Js, p, 'o-', color=col, ms=2.5, lw=1, label=nm)
ax.set_xlim(0, 120); ax.set_xlabel('$J$'); ax.set_ylabel('fraksi molekul'); ax.legend(frameon=False, fontsize=8); koma(ax)
ax.set_title('sebaran populasi rotasi pada 298 K', fontsize=8.5); sv(f, 'c_populasi.png')

# 6. distorsi sentrifugal HCl: selisih garis berturutan
f, ax = plt.subplots(figsize=(5.0, 2.6)); sp(ax)
Bv, Dv = 10.4398, 5.32e-4; Js = np.arange(0, 14)
nu_r = 2 * Bv * (Js + 1); nu_d = 2 * Bv * (Js + 1) - 4 * Dv * (Js + 1) ** 3
ax.plot(Js, nu_r - nu_d, 'o-', color=J2, ms=3)
ax.set_xlabel('$J$ (transisi $J+1 \\leftarrow J$)'); ax.set_ylabel('$\\tilde\\nu_\\mathrm{tegar} - \\tilde\\nu$ (cm$^{-1}$)'); koma(ax)
ax.set_title('HCl: garis bergeser makin jauh dari ramalan rotor tegar', fontsize=8.5); sv(f, 'c_sentrifugal.png')
print('gambar selesai')
