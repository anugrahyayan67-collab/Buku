#!/usr/bin/env python3
# Gambar Bab 3 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from math import pi
from scipy.optimize import brentq
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
hb = 1.054571817e-34; me = 9.1093837015e-31; e = 1.602176634e-19

# 1. mode tali
f, ax = plt.subplots(figsize=(5.6, 2.4)); ax.axis('off'); x = np.linspace(0, 1, 300)
for i, n in enumerate([1, 2, 3]):
    y0 = -i * 1.2
    for t, al in [(0, 1), (0.35, .45), (0.7, .25)]:
        ax.plot(x, y0 + .45 * np.cos(pi * t) * np.sin(n * pi * x), color=[B, H, J2][i], lw=1.5, alpha=al)
        ax.plot(x, y0 - .45 * np.cos(pi * t) * np.sin(n * pi * x), color=[B, H, J2][i], lw=1.5, alpha=al * .6)
    ax.text(1.05, y0, f'$n = {n}$:  $\\nu_{n} = {n}v/2L$', va='center', fontsize=9)
    ax.plot([0, 1], [y0, y0], 'ko', ms=3)
ax.set_xlim(-.05, 1.55); sv(f, 'c_tali.png')

# 2. partikel dalam kotak: tingkat, psi, psi^2
f, axs = plt.subplots(1, 2, figsize=(6.8, 3.6), sharey=True)
x = np.linspace(0, 1, 400)
for ax, kind in [(axs[0], 'psi'), (axs[1], 'psi2')]:
    ax.plot([0, 0], [0, 18], color=TUA, lw=2.5); ax.plot([1, 1], [0, 18], color=TUA, lw=2.5); ax.plot([0, 1], [0, 0], color=TUA, lw=1)
    for n, col in zip(range(1, 5), [B, H, J2, TUA]):
        E = n * n; ax.plot([0, 1], [E, E], color='#bbb', lw=.7, ls='--')
        y = np.sqrt(2) * np.sin(n * pi * x)
        if kind == 'psi': ax.plot(x, E + 0.9 * y, color=col, lw=1.6)
        else: ax.fill_between(x, E, E + 0.55 * y * y, color=col, alpha=.45); ax.plot(x, E + 0.55 * y * y, color=col, lw=1.2)
        if kind == 'psi2': ax.text(1.05, E, f'$n = {n}$,  $E = {n*n}E_1$', va='center', fontsize=8.5)
    ax.set_xticks([0, 1]); ax.set_xticklabels(['0', '$L$']); ax.set_xlim(-.05, 1.05 if kind == 'psi' else 1.55)
    ax.set_title('$\\psi_n(x)$' if kind == 'psi' else '$|\\psi_n(x)|^2$', fontsize=10)
    for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
    ax.set_yticks([])
sv(f, 'c_kotak.png')

# 3. korespondensi
f, axs = plt.subplots(1, 3, figsize=(6.8, 2.2), sharey=True)
for ax, n in zip(axs, [1, 3, 20]):
    sp(ax); ax.fill_between(x, 0, 2 * np.sin(n * pi * x) ** 2, color=MUDA, alpha=.6); ax.plot(x, 2 * np.sin(n * pi * x) ** 2, color=B, lw=1)
    ax.axhline(1, color=J2, lw=1.3, ls='--'); ax.set_title(f'$n = {n}$', fontsize=9); ax.set_xticks([0, 1]); ax.set_xticklabels(['0', '$L$'])
axs[0].set_ylabel('$L\\,|\\psi_n|^2$'); koma(axs[0], x=False); axs[2].text(.62, 1.08, 'klasik', color=J2, fontsize=8)
sv(f, 'c_korespondensi.png')

# 4. model elektron bebas: sianin
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9), gridspec_kw={'width_ratios': [1, 1.25]})
ax = axs[0]; ax.axis('off')
for n in range(1, 7):
    E = n * n; ax.plot([0, 1], [E, E], color=TUA, lw=1.6)
    if n <= 4:
        for s in (-.07, .07): ax.annotate('', xy=(0.5 + s, E + (1.2 if s < 0 else -1.2)), xytext=(0.5 + s, E + (-1.2 if s < 0 else 1.2)), arrowprops=dict(arrowstyle='-|>', color=J2, lw=1, mutation_scale=7))
    ax.text(1.08, E, f'$n = {n}$', va='center', fontsize=8)
ax.annotate('', xy=(0.25, 25), xytext=(0.25, 16), arrowprops=dict(arrowstyle='-|>', color=B, lw=1.5))
ax.text(-0.02, 20, '$h\\nu$', color=B, fontsize=10, ha='right'); ax.text(0.5, 31, '8 elektron π: HOMO $n = 4$, LUMO $n = 5$', ha='center', fontsize=8)
ax.set_xlim(-0.3, 1.4); ax.set_ylim(-1, 38)
ax = axs[1]; sp(ax); k = np.array([1, 2, 3, 4, 5]); obs = np.array([312.5, 416, 519, 625, 734])
L = (2 * k + 4) * 1.39e-10; N = 2 * k + 4; lam = 8 * me * 2.99792458e8 * L ** 2 / (6.62607015e-34 * (N + 1)) * 1e9
ax.plot(k, lam, 'o-', color=B, lw=1.5, label='model elektron bebas'); ax.plot(k, obs, 's--', color=J2, lw=1.2, label='teramati')
ax.set_xlabel('banyak gugus vinilena $k$'); ax.set_ylabel('$\\lambda_{\\mathrm{maks}}$ (nm)'); ax.legend(frameon=False, fontsize=8); ax.set_xticks(k)
ax.set_title('Me$_2$N–(CH=CH)$_k$–CH=NMe$_2^+$', fontsize=9)
plt.tight_layout(); sv(f, 'c_sianin.png')

# 5. sumur terhingga: penyelesaian grafis dan fungsi gelombang
z0 = 5.7279
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9))
ax = axs[0]; sp(ax); z = np.linspace(0.01, z0, 2000)
t = np.tan(z); t[np.abs(t) > 12] = np.nan; ct = -1 / np.tan(z); ct[np.abs(ct) > 12] = np.nan
ax.plot(z, t, color=B, lw=1.3, label='$\\tan z$ (genap)'); ax.plot(z, ct, color=H, lw=1.3, label='$-\\cot z$ (ganjil)')
ax.plot(z, np.sqrt(z0 ** 2 - z ** 2) / z, color=J2, lw=1.8, label='$\\sqrt{z_0^2 - z^2}/z$')
ax.set_ylim(0, 8); ax.set_xlim(0, 6); ax.set_xlabel('$z = ka$'); ax.legend(frameon=False, fontsize=7.5); koma(ax)
ax = axs[1]; sp(ax); a = 0.5e-9; V0 = 5.0
xs = np.linspace(-1.2e-9, 1.2e-9, 1200)
ax.plot([-1.2, -0.5, -0.5, 0.5, 0.5, 1.2], [V0, V0, 0, 0, V0, V0], color=TUA, lw=1.8)
for En, par, col in [(0.2718, 0, B), (1.0774, 1, H), (2.3792, 0, J2), (4.0593, 1, TUA)]:
    kk = np.sqrt(2 * me * En * e) / hb; kp = np.sqrt(2 * me * (V0 - En) * e) / hb
    inside = np.cos(kk * xs) if par == 0 else np.sin(kk * xs)
    edge = np.cos(kk * a) if par == 0 else np.sin(kk * a)
    out = edge * np.exp(-kp * (np.abs(xs) - a)) * (np.sign(xs) if par else 1)
    y = np.where(np.abs(xs) <= a, inside, out); y = y / np.max(np.abs(y))
    ax.plot(xs * 1e9, En + 0.42 * y, color=col, lw=1.4); ax.axhline(En, color='#ccc', lw=.5, ls=':')
ax.set_xlabel('$x$ (nm)'); ax.set_ylabel('energi (eV)'); ax.set_ylim(-0.6, 5.6); koma(ax)
plt.tight_layout(); sv(f, 'c_sumur.png')

# 6. tangga potensial: R dan T
f, ax = plt.subplots(figsize=(4.8, 2.7)); sp(ax); r = np.linspace(0.01, 5, 600)
R = np.where(r > 1, ((np.sqrt(r) - np.sqrt(np.clip(r - 1, 0, None))) / (np.sqrt(r) + np.sqrt(np.clip(r - 1, 0, None)))) ** 2, 1)
ax.plot(r, R, color=J2, lw=1.8, label='pantulan $R$'); ax.plot(r, 1 - R, color=B, lw=1.8, label='transmisi $T$')
ax.axvline(1, color='#999', lw=.7, ls=':'); ax.set_xlabel('$E/V_0$'); ax.set_ylabel('peluang'); ax.legend(frameon=False, fontsize=8); koma(ax)
ax.text(1.1, 0.5, 'klasik: $R = 0$\nuntuk $E > V_0$', fontsize=8); sv(f, 'c_tangga.png')

# 7. penerobosan: fungsi gelombang dan T terhadap lebar
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
ax = axs[0]; ax.axis('off'); xx = np.linspace(-3, 6, 1500); k_ = 4.0; kap = 1.2; a = 1.4; y0 = 0.75; y1 = y0 * np.exp(-kap * a)
fn = lambda u, yy: yy * np.cos(k_ * u) - (kap * yy / k_) * np.sin(k_ * u)
y = np.where(xx < 0, fn(xx, y0), np.where(xx < a, y0 * np.exp(-kap * xx), fn(xx - a, y1)))
ax.add_patch(plt.Rectangle((0, -1.4), a, 2.9, color=MUDA, alpha=.5)); ax.text(a / 2, 1.65, 'penghalang\n$V_0 > E$', ha='center', fontsize=8.5)
ax.plot(xx, y, color=B, lw=1.6); ax.axhline(0, color='#999', lw=.6); ax.text(a / 2, -1.75, '$a$', ha='center')
ax.set_xlim(-3, 6); ax.set_ylim(-2.1, 2.3)
ax = axs[1]; sp(ax); w = np.linspace(0.005, 0.12, 300) * 1e-9
def T(E, V, a, m):
    kp = np.sqrt(2 * m * (V - E) * e) / hb; return 1 / (1 + V ** 2 * np.sinh(kp * a) ** 2 / (4 * E * (V - E)))
u = 1.66053906660e-27
for m, nm, col in [(me, 'elektron', B), (1.00783 * u, 'H', J2), (2.01410 * u, 'D', H)]:
    ax.semilogy(w * 1e9, T(0.2, 0.5, w, m), color=col, lw=1.8, label=nm)
ax.set_ylim(1e-14, 2); ax.set_xlabel('lebar penghalang $a$ (nm)'); ax.set_ylabel('$T$'); ax.legend(frameon=False, fontsize=8); koma(ax, y=False)
ax.set_title('$E = 0{,}2$ eV, $V_0 = 0{,}5$ eV', fontsize=8.5)
plt.tight_layout(); sv(f, 'c_terobos.png')

# 8. paket gelombang menyebar
f, ax = plt.subplots(figsize=(5.4, 2.5)); sp(ax); x = np.linspace(-6, 30, 1500)
for t, col in [(0, TUA), (1, B), (2, J2), (4, H)]:
    s0 = 1.0; st = s0 * np.sqrt(1 + (t / (2 * s0 ** 2)) ** 2); xc = 5 * t
    ax.plot(x, np.exp(-(x - xc) ** 2 / (2 * st ** 2)) / (st * np.sqrt(2 * pi)), color=col, lw=1.6, label=f'$t = {t}$')
ax.set_xlabel('$x$'); ax.set_ylabel('$|\\Psi|^2$'); ax.legend(frameon=False, fontsize=8); koma(ax)
ax.set_title('paket Gauss bergerak dan melebar ($\\hbar = m = 1$, $\\sigma_0 = 1$)', fontsize=8.5); sv(f, 'c_paket.png')

# 9. amonia: sumur ganda
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8), gridspec_kw={'width_ratios': [1.3, 1]})
ax = axs[0]; sp(ax); q = np.linspace(-1.6, 1.6, 400); V = 2023 * ((q / 0.38) ** 2 - 1) ** 2
V = 2023 * (1 - (q / 0.38) ** 2) ** 2 * (np.abs(q) < 10)
ax.plot(q * 100, V, color=TUA, lw=1.8); ax.set_ylim(0, 3200); ax.set_xlim(-60, 60)
for E0, d in [(470, 8), (950, 36)]:
    ax.plot([-48, 48], [E0 - d, E0 - d], color=B, lw=1.2); ax.plot([-48, 48], [E0 + d, E0 + d], color=J2, lw=1.2)
ax.text(0, 2120, 'penghalang 2023 cm$^{-1}$', ha='center', fontsize=8); ax.text(30, 300, 'pemisahan 0,79 cm$^{-1}$\n(diperbesar)', fontsize=7.5)
ax.set_xlabel('koordinat inversi (pm)'); ax.set_ylabel('$V$ (cm$^{-1}$)'); koma(ax)
ax = axs[1]; ax.axis('off')
for xc, s in [(-0.55, 1), (0.55, -1)]:
    ax.plot([xc, xc - .35], [0, .5 * s], color=TUA, lw=1.5); ax.plot([xc, xc + .35], [0, .5 * s], color=TUA, lw=1.5); ax.plot([xc, xc], [0, .6 * s], color=TUA, lw=1.5)
    ax.plot(xc, 0, 'o', color=B, ms=11); ax.text(xc, -0.03, 'N', color='white', ha='center', va='center', fontsize=7, fontweight='bold')
    for dx in (-.35, .35, 0): ax.plot(xc + dx, (.5 if dx else .6) * s, 'o', color='#ddd', mec=TUA, ms=6)
ax.annotate('', xy=(0.3, 0), xytext=(-0.3, 0), arrowprops=dict(arrowstyle='<->', color=J2, lw=1.4)); ax.text(0, 0.12, 'menerobos', ha='center', fontsize=8, color=J2)
ax.set_xlim(-1.2, 1.2); ax.set_ylim(-0.9, 0.9)
plt.tight_layout(); sv(f, 'c_amonia.png')

# 10. STM
f, ax = plt.subplots(figsize=(4.4, 2.6)); sp(ax); d = np.linspace(0.3, 1.0, 200); kap = 1.0868
ax.semilogy(d, np.exp(-2 * kap * (d - 0.3) * 10), color=B, lw=1.8)
ax.set_xlabel('jarak ujung–permukaan (nm)'); ax.set_ylabel('arus relatif'); koma(ax, y=False)
ax.text(0.55, 0.05, 'tiap 0,1 nm: arus turun 8,8 kali\n($\\phi = 4{,}5$ eV)', fontsize=8); sv(f, 'c_stm.png')
print('gambar selesai')

# 11. evolusi superposisi psi1 + psi2
f, axs = plt.subplots(1, 4, figsize=(6.8, 1.9), sharey=True); x = np.linspace(0, 1, 300)
p1 = np.sqrt(2) * np.sin(pi * x); p2 = np.sqrt(2) * np.sin(2 * pi * x)
for ax, (fr, lab) in zip(axs, [(0, '$t = 0$'), (0.25, '$t = T/4$'), (0.5, '$t = T/2$'), (0.75, '$t = 3T/4$')]):
    sp(ax); P = 0.5 * (p1 ** 2 + p2 ** 2 + 2 * p1 * p2 * np.cos(2 * pi * fr))
    ax.fill_between(x, 0, P, color=MUDA, alpha=.6); ax.plot(x, P, color=B, lw=1.3)
    xm = np.trapezoid(x * P, x) / np.trapezoid(P, x); ax.axvline(xm, color=J2, lw=1, ls='--')
    ax.set_title(lab, fontsize=9); ax.set_xticks([0, 1]); ax.set_xticklabels(['0', '$L$'])
axs[0].set_ylabel('$L|\\Psi|^2$'); koma(axs[0], x=False)
sv(f, 'c_superposisi.png')
print('ok 11')
