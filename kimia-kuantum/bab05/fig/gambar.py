#!/usr/bin/env python3
# Gambar Bab 5 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib, math
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from math import pi
from scipy.special import eval_hermite
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
def psi(v, x): return eval_hermite(v, x) * np.exp(-x * x / 2) / np.sqrt(np.sqrt(pi) * 2 ** v * math.factorial(v))
cols = [B, H, J2, TUA, B, H]

# 1. potensial, tingkat, fungsi gelombang
f, axs = plt.subplots(1, 2, figsize=(6.8, 3.6), sharey=True); x = np.linspace(-4.2, 4.2, 600)
for ax, kind in [(axs[0], 'psi'), (axs[1], 'p')]:
    ax.plot(x, 0.5 * x * x, color=TUA, lw=1.6)
    for v in range(5):
        E = v + 0.5; xt = np.sqrt(2 * v + 1); ax.plot([-xt, xt], [E, E], color='#bbb', lw=.7, ls='--')
        y = psi(v, x)
        if kind == 'psi': ax.plot(x, E + 0.55 * y, color=cols[v], lw=1.5)
        else: ax.fill_between(x, E, E + 0.9 * y * y, color=cols[v], alpha=.4); ax.plot(x, E + 0.9 * y * y, color=cols[v], lw=1)
        if kind == 'p': ax.text(4.3, E, f'$v = {v}$', va='center', fontsize=8)
    ax.set_ylim(0, 5.6); ax.set_xlim(-4.2, 4.2); ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_xlabel('$\\xi = \\sqrt{\\alpha}\\,x$'); koma(ax)
    ax.set_title('$\\psi_v$' if kind == 'psi' else '$|\\psi_v|^2$', fontsize=10)
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
axs[0].set_ylabel('$E/\\hbar\\omega$'); sv(f, 'c_osilator.png')

# 2. korespondensi v = 0, 1, 10
f, axs = plt.subplots(1, 3, figsize=(6.8, 2.2))
for ax, v in zip(axs, [0, 1, 10]):
    sp(ax); xt = np.sqrt(2 * v + 1); x = np.linspace(-xt - 1.8, xt + 1.8, 800)
    ax.fill_between(x, 0, psi(v, x) ** 2, color=MUDA, alpha=.6); ax.plot(x, psi(v, x) ** 2, color=B, lw=1)
    xc = np.linspace(-xt * 0.999, xt * 0.999, 400); ax.plot(xc, 1 / (pi * np.sqrt(xt * xt - xc * xc)), color=J2, lw=1.4, ls='--')
    ax.axvline(-xt, color='#999', lw=.6, ls=':'); ax.axvline(xt, color='#999', lw=.6, ls=':')
    ax.set_title(f'$v = {v}$', fontsize=9); ax.set_yticks([]); ax.set_ylim(0, max(psi(v, x) ** 2) * 1.35); koma(ax, y=False)
axs[2].text(0, 0.2, 'klasik', color=J2, fontsize=8, ha='center'); sv(f, 'c_korespondensi.png')

# 3. Morse H2 dan tingkat
f, ax = plt.subplots(figsize=(5.6, 3.3)); sp(ax)
De, a, re, we, wexe = 4.7472, 1.9444, 0.7414, 4401.21, 121.34
r = np.linspace(0.35, 3.2, 600); V = De * (1 - np.exp(-a * (r - re))) ** 2
ax.plot(r, V, color=TUA, lw=1.8, label='Morse'); ax.plot(r, De * a * a * (r - re) ** 2, color=B, lw=1.2, ls='--', label='harmonik')
lam = 17.4
for v in range(17):
    Ev = (we * (v + .5) - we ** 2 / (4 * De / 1.23984e-4) * (v + .5) ** 2) * 1.23984e-4
    if Ev > De: break
    y = 1 - np.sqrt(Ev / De); rl = re - np.log(1 + np.sqrt(Ev / De)) / a; rr = re - np.log(1 - np.sqrt(Ev / De)) / a
    ax.plot([rl, rr], [Ev, Ev], color=J2, lw=.8)
ax.axhline(De, color='#999', lw=.7, ls=':'); ax.text(2.6, De + 0.1, '$D_e$', fontsize=9)
ax.annotate('', xy=(2.3, 0.27), xytext=(2.3, De), arrowprops=dict(arrowstyle='<->', color=H, lw=1)); ax.text(2.35, 2.5, '$D_0$', color=H, fontsize=9)
ax.set_ylim(0, 5.5); ax.set_xlim(0.3, 3.2); ax.set_xlabel('$r$ (Å)'); ax.set_ylabel('$V$ (eV)'); ax.legend(frameon=False, fontsize=8, loc='lower right'); koma(ax)
ax.set_title('H$_2$', fontsize=9); sv(f, 'c_morse.png')

# 4. spektrum IR HCl (cabang P dan R) dengan doblet isotop
f, ax = plt.subplots(figsize=(6.4, 2.6)); sp(ax)
nu0, B0, B1 = 2885.98, 10.44, 10.14; kT = 207.2
nu = np.linspace(2600, 3150, 6000); I = np.zeros_like(nu)
for iso, w, sh in [(35, 0.758, 0.0), (37, 0.242, -2.1)]:
    for J in range(0, 16):
        pop = (2 * J + 1) * np.exp(-B0 * J * (J + 1) / kT)
        R = nu0 + sh + 2 * B1 + (3 * B1 - B0) * J + (B1 - B0) * J * J
        if J >= 1:
            Pb = nu0 + sh - (B1 + B0) * J + (B1 - B0) * J * J; I += w * pop * np.exp(-0.5 * ((nu - Pb) / 0.5) ** 2)
        I += w * pop * np.exp(-0.5 * ((nu - R) / 0.5) ** 2)
ax.plot(nu, I / I.max(), color=B, lw=.8); ax.invert_xaxis(); ax.set_yticks([])
ax.set_xlabel('bilangan gelombang (cm$^{-1}$)'); ax.text(3000, 0.95, 'cabang R', fontsize=8); ax.text(2760, 0.95, 'cabang P', fontsize=8)
ax.text(2886, 0.05, 'pusat pita\n(tanpa garis)', fontsize=7.5, ha='center')
ax.set_title('serapan IR gas HCl: setiap garis kembar (H$^{35}$Cl dan H$^{37}$Cl)', fontsize=8.5); sv(f, 'c_irhcl.png')

# 5. mode normal CO2 dan H2O
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.6))
ax = axs[0]; ax.axis('off'); ax.set_xlim(-2.2, 2.2); ax.set_ylim(-3.6, 0.8)
mods = [('ulur simetris, 1333 cm$^{-1}$ (Raman)', [(-1, 0, -.4, 0), (0, 0, 0, 0), (1, 0, .4, 0)]),
        ('tekuk, 667 cm$^{-1}$ (×2, IR)', [(-1, 0, 0, -.35), (0, 0, 0, .5), (1, 0, 0, -.35)]),
        ('ulur asimetris, 2349 cm$^{-1}$ (IR)', [(-1, 0, .35, 0), (0, 0, -.6, 0), (1, 0, .35, 0)])]
for i, (t, at) in enumerate(mods):
    y0 = -i * 1.3; ax.plot([-1, 1], [y0, y0], color='#999', lw=1.5)
    for k, (x0, _, dx, dy) in enumerate(at):
        ax.plot(x0, y0, 'o', color=J2 if k != 1 else TUA, ms=12 if k != 1 else 10)
        if dx or dy: ax.annotate('', xy=(x0 + dx, y0 + dy), xytext=(x0, y0), arrowprops=dict(arrowstyle='->', color=B, lw=1.4))
    ax.text(0, y0 - 0.55, t, ha='center', fontsize=7.8)
ax.set_title('CO$_2$', fontsize=9)
ax = axs[1]; ax.axis('off'); ax.set_xlim(-3.6, 3.6); ax.set_ylim(-1.5, 1.3)
th = np.radians(52.25); Hp = [(-np.sin(th), -np.cos(th)), (np.sin(th), -np.cos(th))]
for j, (t, vec) in enumerate([('simetris\n3657', [(-.25, -.2), (.25, -.2)]), ('tekuk\n1595', [(.3, -.15), (-.3, -.15)]), ('asimetris\n3756', [(-.25, -.2), (-.25, .2)])]):
    x0 = (j - 1) * 2.3
    for (hx, hy), (dx, dy) in zip(Hp, vec):
        ax.plot([x0, x0 + hx], [0.3, 0.3 + hy], color='#999', lw=1.5); ax.plot(x0 + hx, 0.3 + hy, 'o', color='#ddd', mec=TUA, ms=8)
        ax.annotate('', xy=(x0 + hx + dx, 0.3 + hy + dy), xytext=(x0 + hx, 0.3 + hy), arrowprops=dict(arrowstyle='->', color=B, lw=1.3))
    ax.plot(x0, 0.3, 'o', color=J2, ms=12); ax.text(x0, -1.3, t + ' cm$^{-1}$', ha='center', fontsize=7.8)
ax.set_title('H$_2$O (ketiganya aktif IR)', fontsize=9)
sv(f, 'c_mode.png')

# 6. metode Numerov: tembakan
f, ax = plt.subplots(figsize=(5.2, 2.6)); sp(ax)
def numerov(E, x):
    h = x[1] - x[0]; k2 = 2 * E - x * x; y = np.zeros_like(x); y[0] = 0; y[1] = 1e-6
    for i in range(1, len(x) - 1):
        y[i + 1] = (2 * (1 - 5 * h * h * k2[i] / 12) * y[i] - (1 + h * h * k2[i - 1] / 12) * y[i - 1]) / (1 + h * h * k2[i + 1] / 12)
    return y
x = np.linspace(-6, 4.0, 2000)
for E, col, lb in [(0.45, J2, '$E = 0{,}45$'), (0.50, B, '$E = 0{,}50$ (tepat)'), (0.55, H, '$E = 0{,}55$')]:
    y = numerov(E, x); y /= np.max(np.abs(y[x < 1.5])); ax.plot(x, y, color=col, lw=1.5, label=lb)
ax.set_ylim(-1.5, 1.8); ax.axhline(0, color='#999', lw=.6); ax.set_xlabel('$\\xi$'); ax.set_ylabel('$\\psi$ (tak dinormalkan)')
ax.legend(frameon=False, fontsize=7.5, loc='upper left'); koma(ax); sv(f, 'c_numerov.png')
print('gambar selesai')
