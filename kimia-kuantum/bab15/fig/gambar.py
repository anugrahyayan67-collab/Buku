#!/usr/bin/env python3
# Gambar Bab 15 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.special import voigt_profile, eval_hermite, factorial
from scipy.linalg import eigh_tridiagonal
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'mathtext.fontset': 'dejavusans',
                     'text.color': '#0e2748', 'axes.edgecolor': '#0e2748', 'axes.labelcolor': '#0e2748',
                     'xtick.color': '#0e2748', 'ytick.color': '#0e2748'})
TUA, B_, MUDA, J1, J2, H = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
def fmt(x, p=None): return ('%g' % x).replace('.', ',').replace('-', '−')
KOMA = FuncFormatter(fmt)
def ribu_f(v, p=None):
    s = '%d' % round(abs(v)); s = s if abs(v) < 10000 else s[:-3] + ' ' + s[-3:]
    return ('−' if v < 0 else '') + s
RIBU = FuncFormatter(ribu_f)
def sv(f, n): f.savefig(n, dpi=220, bbox_inches='tight'); plt.close(f)
def sp(ax):
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
def koma(ax, x=True, y=True):
    if x: ax.xaxis.set_major_formatter(KOMA)
    if y: ax.yaxis.set_major_formatter(KOMA)
c = 2.99792458e10; h = 6.62607015e-34; u = 1.66053906660e-27; hb = h / 2 / np.pi

# 1. profil garis
x = np.linspace(-4, 4, 2001); G = np.exp(-4 * np.log(2) * x ** 2); L = 1 / (1 + 4 * x ** 2)
V = voigt_profile(x, 1 / (2 * np.sqrt(2 * np.log(2))), 0.5); V /= V.max()
f, axs = plt.subplots(1, 2, figsize=(7.0, 2.8))
for ax, lg in zip(axs, [False, True]):
    sp(ax); ax.plot(x, G, color=B_, lw=1.6, label='Gauss'); ax.plot(x, L, color=J2, lw=1.6, label='Lorentz'); ax.plot(x, V, color=H, lw=1.4, ls='--', label='Voigt')
    ax.set_xlabel(r'$(\nu - \nu_0)/\Delta\nu$'); koma(ax)
    if lg: ax.set_yscale('log'); ax.set_ylim(1e-6, 1.5); ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: '$10^{%d}$' % round(np.log10(v))))
axs[0].set_ylabel('intensitas relatif'); axs[0].legend(frameon=False, fontsize=8); axs[0].set_title('(a)', loc='left', fontsize=9); axs[1].set_title('(b)', loc='left', fontsize=9)
f.tight_layout(); sv(f, 'c_garis.png')

# 2. Raman rotasi N2
Bn = 1.98957; kT = 0.6950348 * 298.15; xs = np.linspace(-125, 125, 5001); y = np.zeros_like(xs)
def gs(x0, a, w=0.9): return a * np.exp(-4 * np.log(2) * ((xs - x0) / w) ** 2)
for J in range(0, 30):
    g = 6 if J % 2 == 0 else 3; pop = g * (2 * J + 1) * np.exp(-Bn * J * (J + 1) / kT)
    bS = 3 * (J + 1) * (J + 2) / (2 * (2 * J + 1) * (2 * J + 3)); y += gs(4 * Bn * (J + 1.5), pop * bS)
    if J >= 2:
        bO = 3 * J * (J - 1) / (2 * (2 * J + 1) * (2 * J - 1)); y += gs(-Bn * (4 * J - 2), pop * bO)
f, ax = plt.subplots(figsize=(6.6, 2.8)); sp(ax)
ax.plot(xs, y / y.max(), color=B_, lw=1.0); ax.axvline(0, color=J2, lw=2); ax.text(2, 1.02, 'Rayleigh\n(dipotong)', fontsize=7.5, color=J2)
ax.text(62, 1.1, 'cabang S (Stokes)', fontsize=8); ax.text(-118, 1.1, 'cabang O (anti-Stokes)', fontsize=8)
ax.set_xlabel(r'geseran Raman (cm$^{-1}$)'); ax.set_ylabel('intensitas relatif'); ax.set_ylim(0, 1.2); koma(ax)
sv(f, 'c_ramanrot.png')

# 3. kontur pita CO2
def pita(nu0, Bl, Bu, jenis, xr):
    xs = np.linspace(*xr, 6001); y = np.zeros_like(xs); kT = 207.2
    for J in range(0, 120, 2):
        w = (2 * J + 1) * np.exp(-Bl * J * (J + 1) / kT) / (2 * J + 1)
        E0 = Bl * J * (J + 1)
        if jenis == 'sejajar':
            lines = [(nu0 + Bu * (J + 1) * (J + 2) - E0, J + 1)] + ([(nu0 + Bu * (J - 1) * J - E0, J)] if J > 0 else [])
        else:
            lines = [(nu0 + Bu * (J + 1) * (J + 2) - E0, (J + 2) / 2), (nu0 + Bu * J * (J + 1) - E0, (2 * J + 1) / 2)] + ([(nu0 + Bu * (J - 1) * J - E0, (J - 1) / 2)] if J > 1 else [])
        for x0, s in lines: y += w * s * np.exp(-4 * np.log(2) * ((xs - x0) / 0.6) ** 2)
    return xs, y / y.max()
f, axs = plt.subplots(1, 2, figsize=(7.0, 2.8))
for ax, (nu0, Bl, Bu, j, xr, t) in zip(axs, [(2349.1, 0.39022, 0.38714, 'sejajar', (2300, 2400), r'(a) $\nu_3$, pita sejajar'), (667.4, 0.39022, 0.39064, 'tegak', (617, 717), r'(b) $\nu_2$, pita tegak lurus')]):
    sp(ax); xx, yy = pita(nu0, Bl, Bu, j, xr); ax.plot(xx, yy, color=B_, lw=.8); ax.set_title(t, loc='left', fontsize=9)
    ax.set_xlabel(r'$\tilde\nu$ (cm$^{-1}$)'); ax.xaxis.set_major_formatter(RIBU); koma(ax, x=False); ax.set_ylim(0, 1.08)
    ax.text(nu0 - 32, 0.55, 'P', fontsize=10); ax.text(nu0 + 28, 0.55, 'R', fontsize=10)
axs[1].text(667.4 + 2, 0.95, 'Q', fontsize=10); axs[0].set_ylabel('serapan relatif')
f.tight_layout(); sv(f, 'c_pita.png')

# 4. Raman: diagram dan CCl4
f, axs = plt.subplots(1, 2, figsize=(7.2, 3.0), gridspec_kw={'width_ratios': [1, 1.5]})
ax = axs[0]; ax.axis('off')
for yv in (0, 1): ax.plot([0, 10], [yv, yv], color=TUA, lw=1.5)
ax.text(10.2, 0, '$v = 0$', va='center', fontsize=8); ax.text(10.2, 1, '$v = 1$', va='center', fontsize=8)
for x0 in (3.0, 5.5, 8.0): ax.plot([x0 - 0.8, x0 + 0.8], [6, 6], color='#888', ls='--', lw=1)
ax.annotate('', xy=(0.8, 1), xytext=(0.8, 0), arrowprops=dict(arrowstyle='->', color=H, lw=1.3)); ax.text(0.2, 1.4, 'IR', fontsize=8, color=H)
ax.annotate('', xy=(2.7, 6), xytext=(2.7, 0), arrowprops=dict(arrowstyle='->', color=B_, lw=1.3)); ax.annotate('', xy=(3.3, 0), xytext=(3.3, 6), arrowprops=dict(arrowstyle='->', color=B_, lw=1.3))
ax.text(3.0, 6.4, 'Rayleigh', ha='center', fontsize=7.5)
ax.annotate('', xy=(5.2, 6), xytext=(5.2, 0), arrowprops=dict(arrowstyle='->', color=B_, lw=1.3)); ax.annotate('', xy=(5.8, 1), xytext=(5.8, 6), arrowprops=dict(arrowstyle='->', color=J2, lw=1.3))
ax.text(5.5, 6.4, 'Stokes', ha='center', fontsize=7.5)
ax.annotate('', xy=(7.7, 6), xytext=(7.7, 1), arrowprops=dict(arrowstyle='->', color=B_, lw=1.3)); ax.annotate('', xy=(8.3, 0), xytext=(8.3, 6), arrowprops=dict(arrowstyle='->', color=MUDA, lw=1.3))
ax.text(8.0, 6.4, 'anti-Stokes', ha='center', fontsize=7.5); ax.text(0.1, 5.8, 'keadaan\nmaya', fontsize=7, color='#666')
ax.set_xlim(0, 11.5); ax.set_ylim(-0.5, 7); ax.set_title('(a)', loc='left', fontsize=9)
ax = axs[1]; sp(ax); xs = np.linspace(-900, 900, 9001); y = np.zeros_like(xs); nu0 = 1e7 / 532
for v, I in [(218, 0.55), (314, 0.45), (459, 1.0), (762, 0.15), (790, 0.18)]:
    ra = ((nu0 + v) / (nu0 - v)) ** 4 * np.exp(-1.438777 * v / 298.15)
    for s, a in [(v, I), (-v, I * ra)]: y += a / (1 + 4 * ((xs - s) / 6) ** 2)
ax.plot(xs, y, color=B_, lw=1); ax.axvline(0, color=J2, lw=1.5); ax.text(15, 0.95, 'Rayleigh', fontsize=7.5, color=J2)
ax.text(450, 1.03, '459', ha='center', fontsize=7.5); ax.text(-459, 0.17, '−459', ha='center', fontsize=7.5)
ax.set_xlabel('geseran Raman (cm$^{-1}$)'); ax.set_ylabel('intensitas relatif'); ax.set_ylim(0, 1.15); koma(ax); ax.set_title('(b) CCl$_4$, 532 nm', loc='left', fontsize=9)
ax.text(-850, 0.6, 'anti-Stokes', fontsize=8); ax.text(550, 0.6, 'Stokes', fontsize=8)
f.tight_layout(); sv(f, 'c_raman.png')

# 5. Franck-Condon I2
def kin(mu): return h / (8 * np.pi ** 2 * c * mu * u) * 1e20
def morse_lv(mu, we, wx, re, r, n=60):
    De = we ** 2 / (4 * wx); a = np.sqrt(8 * np.pi ** 2 * c * mu * u * wx / h) * 1e-10; dr = r[1] - r[0]; T = kin(mu)
    Vp = De * (1 - np.exp(-a * (r - re))) ** 2
    E, p = eigh_tridiagonal(2 * T / dr ** 2 + Vp, -T / dr ** 2 * np.ones(len(r) - 1), select='i', select_range=(0, n))
    return E, p / np.sqrt(dr), Vp, De
r = np.linspace(2.2, 5.5, 6000); mu = 63.452
EX, pX, VX, DX = morse_lv(mu, 214.50, 0.614, 2.666, r); EB, pB, VB, DB = morse_lv(mu, 125.69, 0.764, 3.024, r)
FCm = (pB.T @ pX[:, 0] * (r[1] - r[0])) ** 2
def psiho(v, x, mu, w):
    a = mu * u * w / hb; xi = np.sqrt(a) * x; N = (a / np.pi) ** 0.25 / np.sqrt(2.0 ** v * factorial(v)); return N * eval_hermite(v, xi) * np.exp(-xi ** 2 / 2)
xg = np.linspace(-0.8e-10, 1.4e-10, 40001); p0 = psiho(0, xg, mu, 2 * np.pi * c * 214.50)
FCh = np.array([np.trapezoid(p0 * psiho(v, xg - 0.358e-10, mu, 2 * np.pi * c * 125.69), xg) ** 2 for v in range(61)])
f, axs = plt.subplots(1, 2, figsize=(7.2, 3.2), gridspec_kw={'width_ratios': [1.1, 1]})
ax = axs[0]; sp(ax); Te = 15769.0
ax.plot(r, VX, color=B_, lw=1.5); ax.plot(r, VB + Te, color=J2, lw=1.5)
m0 = np.abs(pX[:, 0]) > 1e-3 * np.abs(pX[:, 0]).max(); ax.plot(r[m0], EX[0] + 1800 * pX[m0, 0] / pX[:, 0].max(), color=B_, lw=.8)
for v in (0, 10, 20, 32, 45):
    m = (VB + Te) < EB[v] + Te; ax.plot(r[m], 0 * r[m] + EB[v] + Te, color='#aaa', lw=.6)
v = 32; m1 = np.abs(pB[:, v]) > 2e-3 * np.abs(pB[:, v]).max(); ax.plot(r[m1], EB[v] + Te + 1500 * pB[m1, v] / np.abs(pB[:, v]).max(), color=J2, lw=.7)
ax.annotate('', xy=(2.666, EB[32] + Te), xytext=(2.666, EX[0]), arrowprops=dict(arrowstyle='->', color=TUA, lw=1.2))
ax.text(4.3, 3000, 'X', fontsize=10); ax.text(4.3, 21400, 'B', fontsize=10); ax.text(2.7, 9000, 'transisi\ntegak', fontsize=7.5)
ax.set_xlim(2.3, 5.0); ax.set_ylim(-500, 24000); ax.set_xlabel('$r$ (Å)'); ax.set_ylabel('energi (cm$^{-1}$)'); ax.yaxis.set_major_formatter(RIBU); koma(ax, y=False); ax.set_title('(a)', loc='left', fontsize=9)
ax = axs[1]; sp(ax); vv = np.arange(61)
ax.bar(vv - 0.2, FCm[:61], width=0.4, color=B_, label='Morse'); ax.bar(vv + 0.2, FCh, width=0.4, color=J1, label='harmonik')
ax.set_xlabel("$v'$"); ax.set_ylabel('faktor Franck–Condon'); ax.legend(frameon=False, fontsize=8); koma(ax); ax.set_title('(b)', loc='left', fontsize=9)
f.tight_layout(); sv(f, 'c_franck.png')

# 6. Jablonski
f, ax = plt.subplots(figsize=(6.4, 4.2)); ax.axis('off')
def tingkat(x0, y0, lab, w=1.6):
    ax.plot([x0, x0 + w], [y0, y0], color=TUA, lw=2)
    for k in range(1, 4): ax.plot([x0, x0 + w], [y0 + 0.18 * k, y0 + 0.18 * k], color='#999', lw=.6)
    ax.text(x0 - 0.15, y0, lab, ha='right', va='center', fontsize=10)
tingkat(0.5, 0, '$S_0$', 4.6); tingkat(0.5, 4.0, '$S_1$'); tingkat(0.5, 6.0, '$S_2$'); tingkat(3.5, 3.0, '$T_1$')
def panah(x, y1, y2, col, lab=None, gel=False):
    if gel:
        yy = np.linspace(y1, y2, 200); ax.plot(x + 0.06 * np.sin(np.linspace(0, 14 * np.pi, 200)), yy, color=col, lw=1)
        ax.annotate('', xy=(x, y2), xytext=(x, y2 + (0.15 if y2 < y1 else -0.15)), arrowprops=dict(arrowstyle='->', color=col, lw=1))
    else: ax.annotate('', xy=(x, y2), xytext=(x, y1), arrowprops=dict(arrowstyle='->', color=col, lw=1.6))
    if lab: ax.text(x, (y1 + y2) / 2, lab, ha='center', va='center', fontsize=8, bbox=dict(fc='white', ec='none', pad=0.6), color=col)
panah(0.7, 0, 6.5, B_, 'A'); panah(1.0, 0, 4.5, B_, 'A')
panah(1.3, 6.5, 6.0, J2, None, True); panah(1.3, 6.0, 4.5, J2, None, True); panah(1.5, 4.54, 4.0, J2, None, True)
ax.text(1.75, 6.3, 'RG', fontsize=7.5, color=J2); ax.text(1.55, 5.2, 'KI', fontsize=7.5, color=J2)
panah(1.85, 4.0, 0.3, H, 'F')
ax.annotate('', xy=(3.5, 3.4), xytext=(2.1, 4.0), arrowprops=dict(arrowstyle='->', color=J2, lw=1, ls='--')); ax.text(2.55, 3.95, 'LAS', fontsize=7.5, color=J2)
panah(4.3, 3.0, 0.3, '#7a3fa0', 'P'); panah(4.8, 3.0, 0.54, J2, None, True); ax.text(5.0, 1.6, 'LAS', fontsize=7.5, color=J2)
for y, t in [(6.6, 'serapan  10$^{-15}$ s'), (6.1, 'relaksasi getaran  10$^{-12}$ s'), (5.6, 'fluoresensi  10$^{-9}$ s'), (5.1, 'lintas antarsistem  10$^{-11}$–10$^{-6}$ s'), (4.6, 'fosforesensi  10$^{-3}$–10$^{2}$ s')]:
    ax.text(5.8, y, t, fontsize=7.8)
ax.set_xlim(-0.3, 9.0); ax.set_ylim(-0.4, 7.0); sv(f, 'c_jablonski.png')

# 7. citra cermin
x = np.linspace(17000, 33000, 3000); S = 1.0; w = 1400; E00 = 25000
ab = sum(np.exp(-S) * S ** v / factorial(v) * np.exp(-4 * np.log(2) * ((x - E00 - v * w) / 650) ** 2) for v in range(8))
em = sum(np.exp(-S) * S ** v / factorial(v) * np.exp(-4 * np.log(2) * ((x - E00 + v * w) / 650) ** 2) for v in range(8))
f, ax = plt.subplots(figsize=(6.2, 2.8)); sp(ax)
ax.plot(x, ab / ab.max(), color=B_, lw=1.6, label='serapan'); ax.plot(x, em / em.max(), color=J2, lw=1.6, label='fluoresensi')
ax.axvline(E00, color='#999', ls=':', lw=.8); ax.text(E00 + 150, 1.02, '0–0', fontsize=8)
ax.set_xlabel(r'$\tilde\nu$ (cm$^{-1}$)'); ax.set_ylabel('intensitas relatif'); ax.xaxis.set_major_formatter(RIBU); koma(ax, x=False); ax.legend(frameon=False, fontsize=8); ax.set_ylim(0, 1.12)
sv(f, 'c_cermin.png')

# 8. laser
f, axs = plt.subplots(1, 3, figsize=(7.4, 2.8), gridspec_kw={'width_ratios': [1, 1, 1.4]})
for ax, lv, judul in [(axs[0], [(0, '1'), (3.0, '3'), (2.4, '2')], '(a) tiga tingkat'), (axs[1], [(0, '0'), (3.0, '3'), (2.4, '2'), (0.6, '1')], '(b) empat tingkat')]:
    ax.axis('off')
    for y, n in lv:
        ax.plot([0, 2], [y, y], color=TUA, lw=1.8); ax.text(2.1, y, n, va='center', fontsize=8)
    ax.annotate('', xy=(0.4, 3.0), xytext=(0.4, 0), arrowprops=dict(arrowstyle='->', color=B_, lw=2.2)); ax.text(0.05, 1.5, 'pompa', rotation=90, va='center', fontsize=7.5, color=B_)
    yy = np.linspace(3.0, 2.45, 50); ax.plot(1.0 + 0.05 * np.sin(np.linspace(0, 10 * np.pi, 50)), yy, color=J2, lw=1)
    lo = 0 if len(lv) == 3 else 0.6
    ax.annotate('', xy=(1.5, lo), xytext=(1.5, 2.4), arrowprops=dict(arrowstyle='->', color='#c0392b', lw=2)); ax.text(1.62, 1.4, 'laser', fontsize=7.5, color='#c0392b')
    if len(lv) == 4:
        yy = np.linspace(0.6, 0.05, 30); ax.plot(1.0 + 0.05 * np.sin(np.linspace(0, 6 * np.pi, 30)), yy, color=J2, lw=1)
    ax.set_xlim(-0.2, 2.6); ax.set_ylim(-0.3, 3.4); ax.set_title(judul, fontsize=9, loc='left')
ax = axs[2]; sp(ax); nu = np.linspace(-2.0, 2.0, 1000); gain = np.exp(-4 * np.log(2) * (nu / 1.51) ** 2)
ax.plot(nu, gain, color=B_, lw=1.5); ax.axhline(0.45, color=J2, ls='--', lw=1); ax.text(1.25, 0.49, 'kerugian', fontsize=7.5, color=J2)
for m in np.arange(-4, 5) * 0.5:
    gm = np.exp(-4 * np.log(2) * (m / 1.51) ** 2); ax.plot([m, m], [0, gm], color=('#c0392b' if gm > 0.45 else '#bbb'), lw=1.5)
ax.set_xlabel(r'$\nu - \nu_0$ (GHz)'); ax.set_ylabel('penguatan'); koma(ax); ax.set_title('(c) mode rongga 30 cm', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_laser.png')

# 9. PES N2
mu = 7.00154; xg = np.linspace(-0.5e-10, 0.6e-10, 20001); p0 = psiho(0, xg, mu, 2 * np.pi * c * 2358.6)
E = np.linspace(15.2, 19.6, 4000); y = np.zeros_like(E)
for IE, we, wx, re, amp, lab in [(15.581, 2207.0, 16.10, 1.1164, 1.0, '$X\\,^2\\Sigma_g^+$'), (16.693, 1903.7, 15.02, 1.1749, 1.9, '$A\\,^2\\Pi_u$'), (18.751, 2419.8, 23.18, 1.0742, 0.55, '$B\\,^2\\Sigma_u^+$')]:
    dr = (re - 1.0977) * 1e-10
    for v in range(8):
        F = np.trapezoid(p0 * psiho(v, xg - dr, mu, 2 * np.pi * c * we), xg) ** 2
        Ev = IE + (we * v - wx * (v * v + v)) / 8065.544
        y += amp * F * np.exp(-4 * np.log(2) * ((E - Ev) / 0.025) ** 2)
    labs = (IE, lab)
f, ax = plt.subplots(figsize=(6.6, 2.9)); sp(ax); ax.plot(E, y / y.max(), color=B_, lw=1)
for IE, lab, yy in [(15.53, '$X\\,^2\\Sigma_g^+$ ($3\\sigma_g^{-1}$)', 0.85), (17.0, '$A\\,^2\\Pi_u$ ($1\\pi_u^{-1}$)', 0.9), (18.70, '$B\\,^2\\Sigma_u^+$ ($2\\sigma_u^{-1}$)', 0.62)]:
    ax.text(IE, yy, lab, fontsize=8, ha='left')
ax.invert_xaxis(); ax.set_xlabel('energi ionisasi (eV)'); ax.set_ylabel('cacah elektron (relatif)'); koma(ax); ax.set_ylim(0, 1.1)
sec = ax.secondary_xaxis('top', functions=(lambda e: 21.218 - e, lambda k: 21.218 - k)); sec.set_xlabel('energi kinetik dengan He I (eV)'); sec.xaxis.set_major_formatter(KOMA)
sv(f, 'c_pes.png')

# 10. paket gelombang I2 B
we, wx = 125.69, 0.764; v = np.arange(31); Ev = we * (v + 0.5) - wx * (v + 0.5) ** 2
wv = np.exp(-(v - 10) ** 2 / (2 * 3 ** 2)); wv /= wv.sum()
f, axs = plt.subplots(2, 1, figsize=(6.6, 4.4))
for ax, tm, n, sat in [(axs[0], 3e-12, 6001, 'fs'), (axs[1], 100e-12, 200001, 'ps')]:
    t = np.linspace(0, tm, n); A = np.abs((wv[:, None] * np.exp(-2j * np.pi * c * Ev[:, None] * t)).sum(0)) ** 2
    sp(ax); ax.plot(t * (1e15 if sat == 'fs' else 1e12), A, color=B_, lw=.6 if sat == 'ps' else 1.2)
    ax.set_xlabel('$t$ (%s)' % sat); ax.set_ylabel(r'$|\langle\Psi(0)|\Psi(t)\rangle|^2$'); koma(ax); ax.set_ylim(0, 1.05)
axs[0].set_title('(a)', loc='left', fontsize=9); axs[1].set_title('(b)', loc='left', fontsize=9)
axs[1].text(21.8, 1.0, '≈ 22 ps', fontsize=8, ha='center'); axs[1].text(43.7, 0.97, '≈ 44 ps', fontsize=8, ha='center')
f.tight_layout(); sv(f, 'c_paket.png')
print('selesai')
