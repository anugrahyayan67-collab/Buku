#!/usr/bin/env python3
# Gambar Bab 2 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import FancyArrowPatch, Arc, Polygon
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
def panah(ax, a, b, c=TUA, lw=1.4, ms=11):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw, shrinkA=0, shrinkB=0))

# 1. bidang kompleks dan akar satuan
f, axs = plt.subplots(1, 2, figsize=(6.6, 3.0))
ax = axs[0]; ax.set_aspect('equal'); ax.axis('off')
panah(ax, (-0.3, 0), (4.4, 0), '#777', 1); panah(ax, (0, -0.3), (0, 4.4), '#777', 1)
ax.text(4.45, -0.1, 'Re', fontsize=9); ax.text(0.1, 4.45, 'Im', fontsize=9)
panah(ax, (0, 0), (3, 3.6), B, 1.8); ax.plot(3, 3.6, 'o', color=B, ms=5)
ax.plot([3, 3], [0, 3.6], color='#aaa', ls=':', lw=1); ax.plot([0, 3], [3.6, 3.6], color='#aaa', ls=':', lw=1)
ax.text(3.15, 3.7, '$z = x + iy = re^{i\\theta}$', fontsize=9, color=B); ax.text(2.9, -0.4, '$x$', fontsize=9); ax.text(-0.35, 3.5, '$y$', fontsize=9)
ax.text(1.0, 1.9, '$r = |z|$', fontsize=9, rotation=50, color=B)
ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=0, theta2=50.2, color=J2, lw=1.2)); ax.text(0.9, 0.3, '$\\theta$', color=J2, fontsize=10)
ax.plot(3, -3.6 + 0.0, 'o', color=J2, ms=0)
ax.set_xlim(-0.5, 5.2); ax.set_ylim(-0.6, 4.7)
ax = axs[1]; ax.set_aspect('equal'); ax.axis('off'); t = np.linspace(0, 2 * pi, 300)
ax.plot(np.cos(t), np.sin(t), color='#bbb', lw=.8, ls='--'); ax.plot([-1.4, 1.4], [0, 0], color='#999', lw=.6); ax.plot([0, 0], [-1.4, 1.4], color='#999', lw=.6)
for k in range(6):
    z = np.exp(2j * pi * k / 6); ax.plot(z.real, z.imag, 'o', color=B, ms=6)
    ax.text(1.22 * z.real, 1.22 * z.imag, f'$k = {k}$', ha='center', va='center', fontsize=8)
ax.add_patch(Polygon([(np.cos(2 * pi * k / 6), np.sin(2 * pi * k / 6)) for k in range(6)], closed=True, fill=False, ec=MUDA, lw=1))
ax.set_title('akar keenam dari satu: $e^{2\\pi ik/6}$', fontsize=9); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
sv(f, 'c_kompleks.png')

# 2. fungsi Gauss, fungsi genap dan ganjil
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.6))
ax = axs[0]; sp(ax); x = np.linspace(-3, 3, 400)
for a, col in [(0.5, J2), (1, B), (3, TUA)]:
    ax.plot(x, np.exp(-a * x * x), color=col, lw=1.8, label=f'$a = {a}$'.replace('.', ','))
ax.legend(frameon=False, fontsize=8); ax.set_xlabel('$x$'); ax.set_ylabel('$e^{-ax^2}$'); koma(ax)
ax.set_title('luas $= \\sqrt{\\pi/a}$', fontsize=9)
ax = axs[1]; sp(ax); y = x * np.exp(-x * x)
ax.fill_between(x, 0, y, where=y > 0, color=MUDA, alpha=.7); ax.fill_between(x, 0, y, where=y < 0, color=J1, alpha=.7)
ax.plot(x, y, color=B, lw=1.6); ax.axhline(0, color='#999', lw=.6); ax.set_xlabel('$x$'); ax.set_ylabel('$xe^{-x^2}$'); koma(ax)
ax.set_title('fungsi ganjil: luas kiri dan kanan saling meniadakan', fontsize=8.5)
plt.tight_layout(); sv(f, 'c_gauss.png')

# 3. penyelesaian PD orde dua dan syarat batas
f, axs = plt.subplots(1, 3, figsize=(6.9, 2.4))
ax = axs[0]; sp(ax); x = np.linspace(0, 2 * pi, 300)
ax.plot(x, np.sin(x), color=B, lw=1.6, label='$\\sin kx$'); ax.plot(x, np.cos(x), color=J2, lw=1.6, label='$\\cos kx$')
ax.set_title("$y'' = -k^2y$", fontsize=9); ax.legend(frameon=False, fontsize=7.5, loc='lower left'); ax.set_xticks([]); koma(ax)
ax = axs[1]; sp(ax); x = np.linspace(-2, 2, 300)
ax.plot(x, np.exp(x), color=B, lw=1.6, label='$e^{\\kappa x}$'); ax.plot(x, np.exp(-x), color=J2, lw=1.6, label='$e^{-\\kappa x}$')
ax.set_title("$y'' = +\\kappa^2y$", fontsize=9); ax.legend(frameon=False, fontsize=7.5); ax.set_ylim(0, 6); ax.set_xticks([]); koma(ax)
ax = axs[2]; sp(ax); x = np.linspace(0, 1, 300)
for n, col in [(1, B), (2, H), (3, J2)]: ax.plot(x, np.sin(n * pi * x), color=col, lw=1.5, label=f'$n = {n}$')
ax.plot(0, 0, 'ko', ms=4); ax.plot(1, 0, 'ko', ms=4); ax.axhline(0, color='#999', lw=.6)
ax.set_title('$y(0) = y(L) = 0$', fontsize=9); ax.legend(frameon=False, fontsize=7, loc='lower left'); ax.set_xticks([0, 1]); ax.set_xticklabels(['0', '$L$']); koma(ax, x=False)
plt.tight_layout(); sv(f, 'c_pd.png')

# 4. koordinat bola dan distribusi radial 1s
f = plt.figure(figsize=(6.8, 3.0))
ax = f.add_subplot(1, 2, 1, projection='3d'); ax.set_axis_off()
L = 1.2
for v, t in [((L, 0, 0), '$x$'), ((0, L, 0), '$y$'), ((0, 0, L), '$z$')]:
    ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color='#777', lw=1); ax.text(v[0] * 1.08, v[1] * 1.08, v[2] * 1.08, t, fontsize=10)
th, ph, r = 0.85, 0.9, 1.0; P = (r * np.sin(th) * np.cos(ph), r * np.sin(th) * np.sin(ph), r * np.cos(th))
ax.plot([0, P[0]], [0, P[1]], [0, P[2]], color=B, lw=2); ax.scatter(*P, color=B, s=18)
ax.plot([P[0], P[0]], [P[1], P[1]], [0, P[2]], color='#aaa', ls=':', lw=1); ax.plot([0, P[0]], [0, P[1]], [0, 0], color='#aaa', ls=':', lw=1)
tt = np.linspace(0, th, 30); ax.plot(0.35 * np.sin(tt) * np.cos(ph), 0.35 * np.sin(tt) * np.sin(ph), 0.35 * np.cos(tt), color=J2, lw=1.2)
pp = np.linspace(0, ph, 30); ax.plot(0.4 * np.cos(pp), 0.4 * np.sin(pp), 0 * pp, color=H, lw=1.2)
ax.text(0.12, 0.08, 0.42, '$\\theta$', color=J2, fontsize=10); ax.text(0.42, 0.25, -0.02, '$\\varphi$', color=H, fontsize=10)
ax.text(P[0] * 0.55, P[1] * 0.55 + 0.05, P[2] * 0.55 + 0.1, '$r$', color=B, fontsize=10)
ax.view_init(elev=20, azim=25); ax.set_box_aspect((1, 1, 1))
ax = f.add_subplot(1, 2, 2); sp(ax); r = np.linspace(0, 6, 400); Pr = 4 * r ** 2 * np.exp(-2 * r)
ax.plot(r, Pr, color=B, lw=1.8); ax.fill_between(r, 0, Pr, where=r <= 1, color=MUDA, alpha=.7)
ax.text(0.15, 0.12, '32,3%', fontsize=8.5, color=TUA); ax.axvline(1, color=J2, lw=.8, ls='--'); ax.axvline(1.5, color=H, lw=.8, ls=':')
ax.text(1.05, 0.58, 'puncak: $r = a_0$', fontsize=8, color=J2); ax.text(1.55, 0.45, '$\\langle r\\rangle = 1{,}5\\,a_0$', fontsize=8, color=H)
ax.set_xlabel('$r/a_0$'); ax.set_ylabel('$4\\pi r^2|\\psi_{1s}|^2$ (satuan $a_0^{-1}$)'); koma(ax); ax.set_ylim(0, 0.65)
plt.tight_layout(); sv(f, 'c_bola.png')

# 5. tingkat energi Huckel
f, ax = plt.subplots(figsize=(6.4, 2.9)); sp(ax); ax.spines['bottom'].set_visible(False)
sist = [('etilena', [1, -1], 2), ('alil', [1.414, 0, -1.414], 3), ('butadiena', [1.618, 0.618, -0.618, -1.618], 4), ('benzena', [2, 1, 1, -1, -1, -2], 6)]
for i, (nm, xs, ne) in enumerate(sist):
    x0 = i * 2.2; xs = sorted(-q for q in xs); used = {}
    for e_ in xs:
        k = used.get(round(e_, 3), 0); used[round(e_, 3)] = k + 1
        deg = sum(1 for q in xs if abs(q - e_) < 1e-3)
        off = 0 if deg == 1 else (-0.38 if k == 0 else 0.38)
        ax.plot([x0 + off - 0.3, x0 + off + 0.3], [e_, e_], color=TUA, lw=1.8)
    # isi elektron dari bawah
    rem = ne; seen = {}
    for e_ in sorted(xs):
        k = seen.get(round(e_, 3), 0); seen[round(e_, 3)] = k + 1
        deg = sum(1 for q in xs if abs(q - e_) < 1e-3); off = 0 if deg == 1 else (-0.38 if k == 0 else 0.38)
        for s_ in (-0.08, 0.08):
            if rem > 0: ax.annotate('', xy=(x0 + off + s_, e_ + (0.18 if s_ < 0 else -0.18)), xytext=(x0 + off + s_, e_ + (-0.18 if s_ < 0 else 0.18)), arrowprops=dict(arrowstyle='-|>', color=J2, lw=1, mutation_scale=7)); rem -= 1
    ax.text(x0, 2.35, nm, ha='center', fontsize=8.5)
ax.axhline(0, color='#bbb', lw=.6, ls='--'); ax.set_ylim(-2.4, 2.7); ax.set_xlim(-1, 7.6); ax.set_xticks([])
ax.set_ylabel('$(E - \\alpha)/|\\beta|$'); koma(ax)
sv(f, 'c_huckel.png')

# 6. deret Taylor potensial Morse dan deret Fourier
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.7))
ax = axs[0]; sp(ax); De, a, re = 4.618, 1.869, 1.275; r = np.linspace(0.8, 3.0, 400); x = r - re
V = De * (1 - np.exp(-a * x)) ** 2
ax.plot(r, V, color=TUA, lw=2, label='Morse'); ax.plot(r, De * a * a * x * x, color=B, lw=1.4, ls='--', label='orde 2 (harmonik)')
ax.plot(r, De * (a * a * x * x - a ** 3 * x ** 3), color=J2, lw=1.4, ls=':', label='orde 3')
ax.set_ylim(0, 6); ax.set_xlabel('$r$ (Å)'); ax.set_ylabel('$V$ (eV)'); ax.legend(frameon=False, fontsize=7.5, loc='upper right'); koma(ax)
ax.set_title('HCl', fontsize=9)
ax = axs[1]; sp(ax); x = np.linspace(-pi, pi, 800)
for N, col in [(1, MUDA), (3, B), (15, TUA)]:
    s = sum(4 / pi / (2 * m + 1) * np.sin((2 * m + 1) * x) for m in range(N)); ax.plot(x, s, color=col, lw=1.3, label=f'{N} suku')
ax.plot(x, np.sign(x), color=J2, lw=1, ls='--'); ax.legend(frameon=False, fontsize=7.5, loc='lower right'); ax.set_xticks([-pi, 0, pi]); ax.set_xticklabels(['$-\\pi$', '0', '$\\pi$'])
ax.set_title('gelombang persegi dari sinus', fontsize=9); koma(ax, x=False)
plt.tight_layout(); sv(f, 'c_deret.png')

# 7. FID dan spektrum
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.5))
ax = axs[0]; sp(ax); t = np.linspace(0, 3, 1500); T2 = 0.5
ax.plot(t, np.exp(-t / T2) * np.cos(2 * pi * 8 * t) + 0.6 * np.exp(-t / T2) * np.cos(2 * pi * 13 * t), color=B, lw=.9)
ax.set_xlabel('waktu $t$ (s)'); ax.set_yticks([]); ax.set_title('sinyal terhadap waktu (FID)', fontsize=9); koma(ax, y=False)
ax = axs[1]; sp(ax); nu = np.linspace(0, 20, 1000); g = 1 / (pi * T2)
Lz = lambda n0: (g / 2) ** 2 / ((nu - n0) ** 2 + (g / 2) ** 2)
ax.plot(nu, Lz(8) + 0.6 * Lz(13), color=TUA, lw=1.5); ax.set_xlabel('frekuensi $\\nu$ (Hz)'); ax.set_yticks([])
ax.set_title('spektrum (transformasi Fourier)', fontsize=9); ax.annotate('lebar $1/\\pi T_2$', xy=(8.4, .5), xytext=(10, .8), fontsize=8, arrowprops=dict(arrowstyle='->', lw=.7))
plt.tight_layout(); sv(f, 'c_fid.png')

# 8. sebaran peluang
f, axs = plt.subplots(1, 3, figsize=(6.9, 2.3))
ax = axs[0]; sp(ax); x = np.linspace(0, 1, 300)
ax.plot(x, 2 * np.sin(pi * x) ** 2, color=B, lw=1.8, label='kotak, $n = 1$'); ax.plot(x, np.ones_like(x), color=J2, lw=1.3, ls='--', label='seragam')
ax.axvline(.5, color='#999', lw=.6, ls=':'); ax.set_xlabel('$x/L$'); ax.set_ylabel('$P(x)\\,L$'); ax.legend(frameon=False, fontsize=7); koma(ax)
ax = axs[1]; sp(ax); x = np.linspace(-4, 4, 400); ax.plot(x, np.exp(-x * x / 2) / np.sqrt(2 * pi), color=B, lw=1.8)
ax.fill_between(x, 0, np.exp(-x * x / 2) / np.sqrt(2 * pi), where=abs(x) <= 1, color=MUDA, alpha=.7); ax.text(-0.45, 0.12, '68,3%', fontsize=8)
ax.set_xlabel('$(x - \\langle x\\rangle)/\\sigma$'); ax.set_title('Gauss', fontsize=9); koma(ax)
ax = axs[2]; sp(ax); m = 28.014 * 1.66054e-27; kT = 1.380649e-23 * 298.15; v = np.linspace(0, 1500, 400)
Fv = 4 * pi * (m / (2 * pi * kT)) ** 1.5 * v ** 2 * np.exp(-m * v * v / (2 * kT))
ax.plot(v, Fv * 1e3, color=B, lw=1.8);
for vv, nm, col in [(420.7, '$v_p$', J2), (474.7, '$\\langle v\\rangle$', H), (515.2, '$v_{\\mathrm{rms}}$', TUA)]:
    ax.axvline(vv, color=col, lw=.8, ls='--', label=nm)
ax.legend(frameon=False, fontsize=7, loc='upper right')
ax.set_xlabel('$v$ (m/s)'); ax.set_ylabel('$f(v)$ ($10^{-3}$ s/m)'); ax.set_title('N$_2$, 298 K', fontsize=9); koma(ax)
plt.tight_layout(); sv(f, 'c_peluang.png')
print('gambar selesai')
