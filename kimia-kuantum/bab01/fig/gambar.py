#!/usr/bin/env python3
# Gambar Bab 1 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle
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
def panah(ax, a, b, c=TUA, lw=1.4, ms=11, ls='-'):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw, ls=ls, shrinkA=0, shrinkB=0))
h = 6.62607015e-34; c = 2.99792458e8; kB = 1.380649e-23; me = 9.1093837015e-31; e = 1.602176634e-19
hb = h / 2 / pi; eps0 = 8.8541878128e-12; a0 = 5.29177210903e-11

# ---------- 1. skala energi gejala kimia (subbab 1.1)
f, ax = plt.subplots(figsize=(6.8, 3.1)); sp(ax); ax.spines['left'].set_visible(False)
bar = [('resonansi magnet inti (NMR)', 4e-8, 4e-6, MUDA), ('resonansi spin elektron (ESR)', 1e-5, 2e-4, MUDA),
       ('rotasi molekul', 5e-5, 5e-3, B), ('getaran molekul', 5e-3, 0.5, B), ('ikatan hidrogen', 0.05, 0.4, H),
       ('energi ikatan kovalen', 1.5, 10, H), ('transisi elektron valensi (UV–tampak)', 1.5, 8, J2),
       ('ionisasi elektron valensi', 4, 25, J2), ('elektron kulit dalam (sinar-X)', 1e2, 1e5, TUA)]
for i, (t, a, b, col) in enumerate(bar):
    y = len(bar) - i
    ax.barh(y, np.log10(b) - np.log10(a), left=np.log10(a), height=.62, color=col, alpha=.9)
    ax.text(np.log10(a) - 0.12 if np.log10(b) > 0.5 else np.log10(b) + .12, y, t, va='center',
            ha='right' if np.log10(b) > 0.5 else 'left', fontsize=8)
kt = np.log10(0.02569)
ax.axvline(kt, color=H, lw=1, ls='--'); ax.text(kt + .08, len(bar) + .35, '$kT$ pada 298 K', color=H, fontsize=8)
ax.set_yticks([]); ax.set_xlim(-8, 5.3); ax.set_ylim(0.4, len(bar) + .8)
ax.set_xticks(range(-8, 6)); ax.set_xticklabels([f'$10^{{{k}}}$' for k in range(-8, 6)])
ax.set_xlabel('energi (eV)')
ax2 = ax.twiny(); ax2.set_xlim(ax.get_xlim()); off = np.log10(8065.54)
tk = range(-4, 10, 2); ax2.set_xticks([k - off for k in tk]); ax2.set_xticklabels([f'$10^{{{k}}}$' for k in tk])
ax2.set_xlabel('bilangan gelombang (cm$^{-1}$)'); ax2.spines['right'].set_visible(False); ax2.spines['left'].set_visible(False)
sv(f, 'c_skala.png')

# ---------- 2. spektrum benda hitam (subbab 1.3)
f, ax = plt.subplots(figsize=(6.0, 3.3)); sp(ax)
lam = np.linspace(60e-9, 3000e-9, 1500)
def M(lam, T): return 2 * pi * h * c ** 2 / lam ** 5 / np.expm1(h * c / (lam * kB * T)) / 1e12   # MW m^-2 per mikrometer
ax.axvspan(400, 700, color=MUDA, alpha=.25, lw=0); ax.text(550, 112, 'cahaya\ntampak', ha='center', fontsize=8, color=B)
for T, col in [(6000, TUA), (5000, B), (4000, H), (3000, J2)]:
    ax.plot(lam * 1e9, M(lam, T), color=col, lw=1.8); lm = 2.897772e-3 / T
    ax.plot(lm * 1e9, M(lm, T), 'o', color=col, ms=3.5); ax.text(lm * 1e9 + 40, M(lm, T) + 2, f'{T} K', color=col, fontsize=8.5)
TT = np.linspace(2900, 6600, 50); ax.plot(2.897772e-3 / TT * 1e9, M(2.897772e-3 / TT, TT), color='#888', lw=.8, ls=':')
rj = 2 * pi * c * kB * 5000 / lam ** 4 / 1e12
ax.plot(lam * 1e9, rj, color=B, lw=1.3, ls='--'); ax.text(1380, 52, 'Rayleigh–Jeans (5000 K)', color=B, fontsize=8)
ax.set_ylim(0, 125); ax.set_xlim(0, 3000); ax.set_xlabel('panjang gelombang $\\lambda$ (nm)')
ax.set_ylabel('$M_\\lambda$ (MW m$^{-2}$ µm$^{-1}$)'); sv(f, 'c_bendahitam.png')

# ---------- 3. penghitungan mode (subbab 1.3)
f, axs = plt.subplots(1, 2, figsize=(6.8, 3.0), gridspec_kw={'width_ratios': [1, 1.15]})
ax = axs[0]; ax.axis('off'); x = np.linspace(0, 1, 300)
for i, n in enumerate([1, 2, 3, 5]):
    y0 = 3.3 - i * 1.05; ax.plot(x, y0 + .38 * np.sin(n * pi * x), color=[B, H, J2, TUA][i], lw=1.6)
    ax.plot([0, 1], [y0, y0], color='#bbb', lw=.5); ax.text(1.05, y0, f'$n = {n}$', va='center', fontsize=8.5)
ax.plot([0, 0], [-0.5, 3.8], color=TUA, lw=3); ax.plot([1, 1], [-0.5, 3.8], color=TUA, lw=3)
ax.text(.5, -0.85, 'dinding logam: $E = 0$ di $x = 0$ dan $x = L$', ha='center', fontsize=8)
ax.set_xlim(-.1, 1.35); ax.set_ylim(-1, 3.9)
ax = axs[1]; sp(ax); N = 11
for i in range(1, N):
    for j in range(1, N):
        ax.plot(i, j, 'o', color=B if i * i + j * j <= 64 else '#c9d6e3', ms=2.6)
th = np.linspace(0, pi / 2, 100); ax.plot(8 * np.cos(th), 8 * np.sin(th), color=H, lw=1.4)
th = np.linspace(0, pi / 2, 100); ax.plot(8.9 * np.cos(th), 8.9 * np.sin(th), color=H, lw=1, ls='--')
ax.annotate('$n$', xy=(5.66, 5.66), xytext=(1.6, 2.0), fontsize=9, color=H, arrowprops=dict(arrowstyle='-', color=H, lw=.8))
ax.text(7.0, 9.6, 'kulit $n$ sampai $n + dn$', color=H, fontsize=8)
ax.set_xlim(0, 10.5); ax.set_ylim(0, 10.5); ax.set_aspect('equal'); ax.set_xlabel('$n_x$'); ax.set_ylabel('$n_y$')
ax.set_xticks([0, 2, 4, 6, 8, 10]); ax.set_yticks([0, 2, 4, 6, 8, 10]); sv(f, 'c_mode.png')

# ---------- 4. energi rata-rata osilator dan kapasitas kalor Einstein (subbab 1.3)
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
ax = axs[0]; sp(ax); x = np.linspace(1e-3, 6, 400)
ax.plot(x, np.ones_like(x), color=H, lw=1.6, ls='--', label='klasik: $kT$')
ax.plot(x, x / np.expm1(x), color=B, lw=2, label='Planck: $h\\nu/(e^{h\\nu/kT} - 1)$')
ax.set_xlabel('$h\\nu/kT$'); ax.set_ylabel('$\\langle E\\rangle / kT$'); ax.set_ylim(0, 1.4); ax.set_xlim(0, 6)
ax.legend(frameon=False, fontsize=7.6, loc='upper right'); koma(ax)
ax.text(3.2, .45, 'mode "membeku":\nkuantum $h\\nu$ jauh\nlebih besar dari $kT$', fontsize=7.6, color=TUA)
ax = axs[1]; sp(ax); t = np.linspace(0.02, 1.6, 400); xx = 1 / t
ax.plot(t, xx ** 2 * np.exp(xx) / np.expm1(xx) ** 2, color=B, lw=2)
ax.axhline(1, color=H, ls='--', lw=1.2); ax.text(1.05, 1.03, 'Dulong–Petit $3R$', color=H, fontsize=8)
td = 298.15 / 1320; yd = (1 / td) ** 2 * np.exp(1 / td) / np.expm1(1 / td) ** 2
ax.plot(td, yd, 'o', color=J2, ms=5); ax.annotate('intan, 298 K', xy=(td, yd), xytext=(0.35, 0.12), fontsize=8, arrowprops=dict(arrowstyle='->', color=J2, lw=.8))
ax.set_xlabel('$T/\\theta_E$'); ax.set_ylabel('$C_{V,m}/3R$'); ax.set_ylim(0, 1.15); ax.set_xlim(0, 1.6); koma(ax)
plt.tight_layout(); sv(f, 'c_osilator.png')

# ---------- 5. efek fotolistrik dan PES N2 (subbab 1.4)
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9), gridspec_kw={'width_ratios': [1.1, 1]})
ax = axs[0]; sp(ax); nu = np.linspace(0, 16, 200)
for nm, phi, col in [('Cs', 2.14, B), ('Na', 2.75, H), ('Zn', 4.33, J2)]:
    n0 = phi * e / h / 1e14; nn = np.linspace(n0, 16, 50)
    ax.plot(nn, h * nn * 1e14 / e - phi, color=col, lw=1.8); ax.plot([0, n0], [-phi, 0], color=col, lw=.8, ls=':')
    ax.text(15.3, h * 15.3e14 / e - phi + .25, nm, color=col, fontsize=9, ha='right')
ax.axhline(0, color='#888', lw=.6); ax.set_xlim(0, 16); ax.set_ylim(-4.6, 4.6)
ax.set_xlabel('frekuensi $\\nu$ ($10^{14}$ Hz)'); ax.set_ylabel('$K_{\\mathrm{maks}}$ (eV)'); koma(ax)
ax.text(1.0, 3.4, 'kemiringan = $h$\n(sama untuk semua logam)', fontsize=7.8, color=TUA)
ax.text(.5, -3.9, 'perpotongan = $-\\phi$', fontsize=7.8, color='#555')
ax = axs[1]; sp(ax); K = np.linspace(1.5, 7, 1200); I = np.zeros_like(K)
def pita(I, k0, ampl, wid=.035):
    return I + ampl * np.exp(-0.5 * ((K - k0) / wid) ** 2)
I = pita(I, 5.64, 1.0); I = pita(I, 5.64 - 0.27, .08)
for v, a_ in enumerate([.55, .9, .7, .4, .2]): I = pita(I, 4.53 - 0.225 * v, a_ * .55)
I = pita(I, 2.47, .45); I = pita(I, 2.47 - 0.29, .12)
ax.plot(K, I, color=B, lw=1.3); ax.fill_between(K, 0, I, color=MUDA, alpha=.4)
for k0, t in [(5.64, '15,58 eV'), (4.53, '16,69 eV'), (2.47, '18,75 eV')]:
    ax.text(k0, max(I[np.abs(K - k0) < .3]) + .07, t, ha='center', fontsize=7.6, color=TUA)
ax.set_xlim(7, 1.5); ax.set_ylim(0, 1.25); ax.set_yticks([]); koma(ax, y=False)
ax.set_xlabel('energi kinetik fotoelektron (eV)'); ax.set_title('N$_2$ disinari He I (21,22 eV)', fontsize=8.5)
ax.text(4.2, 1.1, 'label: energi ionisasi', fontsize=7.4, color='#555')
plt.tight_layout(); sv(f, 'c_fotolistrik.png')

# ---------- 6. efek Compton (subbab 1.5)
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8), gridspec_kw={'width_ratios': [1, 1.15]})
ax = axs[0]; ax.axis('off'); ax.set_xlim(-3.2, 3.2); ax.set_ylim(-2.2, 2.2); ax.set_aspect('equal')
xs = np.linspace(-3, -0.35, 300); ax.plot(xs, .18 * np.sin(9 * xs), color=B, lw=1.3); panah(ax, (-0.5, 0), (-0.15, 0), B)
ax.text(-2.4, .38, '$\\lambda$', color=B, fontsize=11)
ax.add_patch(Circle((0, 0), .14, color=H))
tt = np.radians(40); s_ = np.linspace(.35, 2.9, 300); xx, yy = s_ * np.cos(tt), s_ * np.sin(tt)
ax.plot(xx - .16 * np.sin(5.5 * s_) * np.sin(tt), yy + .16 * np.sin(5.5 * s_) * np.cos(tt), color=J2, lw=1.3)
panah(ax, (2.6 * np.cos(tt), 2.6 * np.sin(tt)), (3.0 * np.cos(tt), 3.0 * np.sin(tt)), J2)
ax.text(1.0, 1.6, "$\\lambda'$", color=J2, fontsize=11)
pp = np.radians(-35); panah(ax, (.2 * np.cos(pp), .2 * np.sin(pp)), (2.3 * np.cos(pp), 2.3 * np.sin(pp)), H, 1.6)
ax.text(1.5, -1.65, 'elektron\nterpental', color=H, fontsize=8.5)
ax.plot([0, 2.8], [0, 0], color='#999', lw=.7, ls='--')
from matplotlib.patches import Arc
ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=0, theta2=40, color=TUA, lw=.8)); ax.text(.95, .25, '$\\theta$', fontsize=10)
ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=-35, theta2=0, color=TUA, lw=.8)); ax.text(.7, -.32, '$\\varphi$', fontsize=10)
ax = axs[1]; sp(ax); lc = 2.42631; l0 = 71.07; L = np.linspace(70, 77.5, 900)
for i, th in enumerate([0, 45, 90, 135]):
    l1 = l0 + lc * (1 - np.cos(np.radians(th))); y0 = 3 - i
    I = .55 * np.exp(-0.5 * ((L - l0) / .12) ** 2) + (.7 if th else 0) * np.exp(-0.5 * ((L - l1) / .35) ** 2)
    ax.plot(L, y0 + I, color=[TUA, B, H, J2][i], lw=1.3); ax.text(77.6, y0 + .15, f'$\\theta$ = {th}°', fontsize=8, va='bottom', ha='right')
ax.axvline(l0, color='#aaa', lw=.6, ls=':')
ax.set_yticks([]); ax.set_xlabel('panjang gelombang terhambur (pm)'); ax.set_xlim(70, 77.7); koma(ax, y=False)
ax.set_title('sinar-X Mo K$\\alpha$ dihamburkan grafit', fontsize=8.5)
plt.tight_layout(); sv(f, 'c_compton.png')

# ---------- 7. tingkat energi hidrogen dan deret spektrum (subbab 1.6)
f = plt.figure(figsize=(6.8, 3.6)); ax = f.add_axes([0.08, 0.27, 0.9, 0.7]); sp(ax); ax.spines['bottom'].set_visible(False)
En = lambda n: -13.598 / n ** 2
for n in range(1, 8):
    ax.plot([0, 10], [En(n), En(n)], color=TUA if n < 7 else '#999', lw=1)
    if n <= 3: ax.text(10.15, En(n), f'$n = {n}$', va='center', fontsize=8)
ax.plot([0, 10], [0, 0], color=TUA, lw=1, ls='--'); ax.text(10.15, 0.25, '$n = \\infty$', fontsize=8, va='center')
def deret(x0, nl, col, nama):
    for i, nu in enumerate(range(nl + 1, nl + 6)):
        panah(ax, (x0 + .32 * i, En(nu)), (x0 + .32 * i, En(nl)), col, 1.1, 8)
    ax.text(x0 + 1.75 if nl == 1 else x0 + .6, En(nl) + .45 if nl == 1 else En(nl) - .9, nama, color=col, fontsize=8.5, ha='left' if nl == 1 else 'center')
deret(0.7, 1, B, 'Lyman (UV)'); deret(4.0, 2, H, 'Balmer (tampak)'); deret(7.3, 3, J2, 'Paschen (IR)')
ax.set_xlim(0, 11.3); ax.set_ylim(-14.8, 1); ax.set_xticks([]); ax.set_ylabel('energi (eV)'); koma(ax)
ax.set_yticks([-13.6, -10, -5, -3.4, -1.51, 0]); ax.yaxis.set_major_formatter(KOMA)
ax3 = f.add_axes([0.08, 0.05, 0.9, 0.12]); ax3.set_facecolor('#06142a')
from matplotlib.colors import hsv_to_rgb
def warna(l):
    if l < 440: return (0.55, 0.3, 1)
    if l < 490: return (0.1, 0.5, 1)
    if l < 580: return (0.2, 0.9, 0.4)
    return (1, 0.15, 0.1)
for n2 in range(3, 12):
    l = 1 / (1.0967758e7 * (1 / 4 - 1 / n2 ** 2)) * 1e9
    ax3.axvline(l, color=warna(l), lw=1.6 if n2 < 7 else .8)
    if n2 < 7: ax3.text(l, 1.08, ['H$\\alpha$', 'H$\\beta$', 'H$\\gamma$', 'H$\\delta$'][n2 - 3], ha='center', fontsize=7.5, transform=ax3.get_xaxis_transform())
ax3.axvline(364.7, color='#aaa', lw=.7, ls=':'); ax3.set_xlim(350, 700); ax3.set_yticks([])
ax3.set_xlabel('deret Balmer: panjang gelombang (nm)', fontsize=8.5); ax3.tick_params(labelsize=8)
sv(f, 'c_hidrogen.png')

# ---------- 8. Moseley (subbab 1.6)
f, ax = plt.subplots(figsize=(5.4, 2.9)); sp(ax)
Z = np.arange(13, 51); nu = 0.75 * 3.2898419603e15 * (Z - 1) ** 2
ax.plot(Z, np.sqrt(nu) / 1e8, color=B, lw=1.2)
dik = [z for z in Z if z not in (43,)]
ax.plot(dik, np.sqrt(0.75 * 3.2898419603e15 * (np.array(dik) - 1) ** 2) / 1e8, 'o', color=B, ms=3)
ax.plot(43, np.sqrt(0.75 * 3.2898419603e15 * 42 ** 2) / 1e8, 'o', mfc='white', mec=J2, ms=6, mew=1.5)
ax.annotate('$Z = 43$: belum dikenal (1913),\nkelak teknesium (1937)', xy=(43, np.sqrt(0.75 * 3.2898419603e15 * 42 ** 2) / 1e8), xytext=(26, 21.5), fontsize=8, color=J2,
            arrowprops=dict(arrowstyle='->', color=J2, lw=.8))
for zz, s in [(20, 'Ca'), (26, 'Fe'), (29, 'Cu'), (42, 'Mo')]:
    ax.text(zz + .6, np.sqrt(0.75 * 3.2898419603e15 * (zz - 1) ** 2) / 1e8 - 1.1, s, fontsize=8, color=TUA)
ax.set_xlabel('nomor atom $Z$'); ax.set_ylabel('$\\sqrt{\\nu}$ ($10^{8}$ Hz$^{1/2}$)'); koma(ax); sv(f, 'c_moseley.png')

# ---------- 9. gelombang de Broglie pada lingkaran (subbab 1.7)
f, axs = plt.subplots(1, 2, figsize=(6.0, 2.9))
for ax, nn, ttl in [(axs[0], 4, '$2\\pi r = 4\\lambda$: gelombang berdiri'), (axs[1], 4.4, '$2\\pi r = 4{,}4\\lambda$: gelombang saling meniadakan')]:
    ax.axis('off'); ax.set_aspect('equal'); t = np.linspace(0, 2 * pi, 600)
    ax.plot(np.cos(t), np.sin(t), color='#bbb', lw=.8, ls='--'); ax.add_patch(Circle((0, 0), .07, color=H))
    if nn == 4:
        r = 1 + .18 * np.sin(nn * t); ax.plot(r * np.cos(t), r * np.sin(t), color=B, lw=1.8)
    else:
        for k, col in zip(range(3), [B, MUDA, J1]):
            tt = np.linspace(0, 2 * pi, 600) + 2 * pi * k; r = 1 + .18 * np.sin(nn * tt)
            ax.plot(r * np.cos(tt), r * np.sin(tt), color=col, lw=1.3)
    ax.set_title(ttl, fontsize=8.5); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3)
sv(f, 'c_debroglie.png')

# ---------- 10. celah ganda: penumpukan titik (subbab 1.8)
f = plt.figure(figsize=(6.8, 3.2)); rng = np.random.default_rng(7)
xg = np.linspace(-1, 1, 2000); I = np.cos(9 * pi * xg / 2) ** 2 * np.sinc(1.6 * xg) ** 2
p = I / I.sum()
for k, N in enumerate([30, 400, 6000]):
    ax = f.add_axes([0.02 + k * 0.33, 0.33, 0.30, 0.62]); ax.set_facecolor('#06142a'); ax.set_xticks([]); ax.set_yticks([])
    x = rng.choice(xg, N, p=p) + rng.normal(0, .004, N); y = rng.uniform(0, 1, N)
    ax.scatter(x, y, s=1.6 if N < 1000 else .5, c='white', lw=0); ax.set_xlim(-1, 1); ax.set_ylim(0, 1)
    ax.set_title(f'{N} elektron', fontsize=8.5)
ax = f.add_axes([0.02, 0.05, 0.96, 0.22]); sp(ax); ax.spines['left'].set_visible(False)
xx = np.linspace(-1, 1, 1000); ax.plot(xx, np.cos(9 * pi * xx / 2) ** 2 * np.sinc(1.6 * xx) ** 2, color=B, lw=1.4, label='kedua celah terbuka')
ax.plot(xx, .5 * np.sinc(1.6 * xx) ** 2, color=H, lw=1.2, ls='--', label='jumlah pola satu celah ($P_1 + P_2$)')
ax.set_yticks([]); ax.set_xticks([]); ax.legend(frameon=False, fontsize=7.5, loc='upper right', ncol=2); ax.set_ylim(0, 1.25)
ax.set_xlabel('posisi pada layar', fontsize=8.5); sv(f, 'c_celah.png')

# ---------- 11. paket gelombang (subbab 1.9)
f, axs = plt.subplots(2, 2, figsize=(6.6, 3.6), gridspec_kw={'width_ratios': [1.6, 1]})
x = np.linspace(-6, 6, 1500); k0 = 8; kk = np.linspace(0, 16, 600)
for i, s in enumerate([0.5, 1.6]):
    ax = axs[i, 0]; sp(ax); env = np.exp(-x ** 2 / (4 * s ** 2))
    ax.plot(x, env * np.cos(k0 * x), color=B, lw=1); ax.plot(x, env, color=H, lw=1, ls='--'); ax.plot(x, -env, color=H, lw=1, ls='--')
    ax.set_yticks([]); ax.set_xlim(-6, 6); ax.set_ylabel('Re $\\psi$', fontsize=8)
    ax.text(3.0, .65, f'$\\Delta x$ = {s}'.replace('.', ','), fontsize=8.5, color=TUA)
    ax = axs[i, 1]; sp(ax); sk = 1 / (2 * s); ax.fill_between(kk, 0, np.exp(-(kk - k0) ** 2 / (2 * sk ** 2)), color=MUDA, alpha=.6)
    ax.plot(kk, np.exp(-(kk - k0) ** 2 / (2 * sk ** 2)), color=B, lw=1.2); ax.set_yticks([]); ax.set_xlim(0, 16)
    ax.text(10.5, .75, f'$\\Delta k$ = {sk:.2g}'.replace('.', ','), fontsize=8.5, color=TUA); ax.set_ylabel('$|\\phi(k)|^2$', fontsize=8)
axs[1, 0].set_xlabel('$x$'); axs[1, 1].set_xlabel('$k$'); axs[0, 0].set_xticks([]); axs[0, 1].set_xticks([])
plt.tight_layout(); sv(f, 'c_paket.png')

# ---------- 12. ukuran atom dari asas ketidakpastian (subbab 1.9)
f, ax = plt.subplots(figsize=(5.2, 3.0)); sp(ax)
r = np.linspace(.2, 4, 500) * a0; Kr = hb ** 2 / (2 * me * r ** 2) / e; V = -e ** 2 / (4 * pi * eps0 * r) / e
ax.plot(r / a0, Kr, color=H, lw=1.4, ls='--', label='kinetik $\\hbar^2/2m_er^2$')
ax.plot(r / a0, V, color=B, lw=1.4, ls='--', label='potensial $-e^2/4\\pi\\varepsilon_0 r$')
ax.plot(r / a0, Kr + V, color=TUA, lw=2, label='jumlah $E(r)$')
ax.plot(1, -13.6057, 'o', color=J2, ms=6); ax.annotate('minimum: $r = a_0$,\n$E = -13{,}6$ eV', xy=(1, -13.6), xytext=(1.7, -24), fontsize=8,
                                                       arrowprops=dict(arrowstyle='->', color=J2, lw=.8))
ax.axhline(0, color='#999', lw=.6); ax.set_ylim(-40, 40); ax.set_xlim(0.2, 4); ax.set_xlabel('$r/a_0$'); ax.set_ylabel('energi (eV)')
ax.legend(frameon=False, fontsize=7.8, loc='upper right'); koma(ax); sv(f, 'c_atomstabil.png')
print('gambar selesai')
