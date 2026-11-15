#!/usr/bin/env python3
# Gambar Bab 16 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
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
def lor(x, x0, w): return (w / 2) ** 2 / ((x - x0) ** 2 + (w / 2) ** 2)

# ---- simulasi spin (sama dengan Contoh 16.c27)
sx = np.array([[0, 1], [1, 0]]) / 2; sy = np.array([[0, -1j], [1j, 0]]) / 2; sz = np.array([[1, 0], [0, -1]]) / 2
def op(s, k, n):
    m = np.array([[1.0]])
    for i in range(n): m = np.kron(m, s if i == k else np.eye(2))
    return m
def spektrum(nu, J, nu0=1e4):
    n = len(nu); X, Y, Z = ([op(s, k, n) for k in range(n)] for s in (sx, sy, sz))
    Hm = sum(-(nu0 + nu[k]) * Z[k] for k in range(n))
    for i in range(n):
        for j in range(i + 1, n): Hm = Hm + J[i][j] * (X[i] @ X[j] + Y[i] @ Y[j] + Z[i] @ Z[j])
    E, V = np.linalg.eigh(Hm); F = V.conj().T @ sum(X) @ V; g = {}
    for a in range(2 ** n):
        for b in range(a + 1, 2 ** n):
            if abs(F[a, b]) ** 2 > 1e-6:
                f = round(E[b] - E[a] - nu0, 3); g[f] = g.get(f, 0) + abs(F[a, b]) ** 2
    return g

# 1. Zeeman
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
Bm = np.linspace(0, 15, 50)
ax = axs[0]; sp(ax)
for g, c, nm in [(26.7522, B, '¹H'), (6.7283, H, '¹³C')]:
    nu = g / (2 * np.pi) * 10 * Bm  # MHz
    ax.plot(Bm, nu / 2, color=c, lw=1.6); ax.plot(Bm, -nu / 2, color=c, lw=1.6)
    ax.text(15.3, nu[-1] / 2, f'{nm} β', color=c, va='center', fontsize=8); ax.text(15.3, -nu[-1] / 2, f'{nm} α', color=c, va='center', fontsize=8)
ax.annotate('', xy=(14.09, 300), xytext=(14.09, -300), arrowprops=dict(arrowstyle='<->', color=J2, lw=1.1))
ax.text(13.7, -170, '600 MHz', color=J2, fontsize=8, ha='right')
ax.set_xlabel('$B_0$ (T)'); ax.set_ylabel('$E/h$ (MHz)'); ax.set_title('spin ½', fontsize=9.5); koma(ax); ax.set_xlim(0, 17.5)
ax = axs[1]; sp(ax)
nu = 4.1066 / (2 * np.pi) * 10 * Bm
for m, c in [(1, B), (0, H), (-1, J2)]:
    ax.plot(Bm, -m * nu, color=c, lw=1.6); ax.text(15.3, -m * nu[-1], f'$m_I = {m:+d}$'.replace('+0', '0'), color=c, va='center', fontsize=8)
ax.annotate('', xy=(10, 0), xytext=(10, -4.1066 / (2 * np.pi) * 100), arrowprops=dict(arrowstyle='<->', color=TUA, lw=.9))
ax.annotate('', xy=(11, 4.1066 / (2 * np.pi) * 110), xytext=(11, 0), arrowprops=dict(arrowstyle='<->', color=TUA, lw=.9))
ax.text(9.6, -38, '$h\\nu_0$', fontsize=8.5, ha='right'); ax.text(11.4, 35, '$h\\nu_0$', fontsize=8.5)
ax.set_xlabel('$B_0$ (T)'); ax.set_title('spin 1 (²H)', fontsize=9.5); koma(ax); ax.set_xlim(0, 18.5)
f.tight_layout(); sv(f, 'c_zeeman.png')

# 2. Geseran kimia
f, axs = plt.subplots(2, 1, figsize=(6.8, 4.6), gridspec_kw={'height_ratios': [1.1, 1]})
ax = axs[0]
g1 = [('alkil C–H', 0.8, 1.8), ('alilik, α-karbonil', 1.8, 2.7), ('alkuna ≡C–H', 1.8, 3.1), ('H–C–N, H–C–halogen', 2.2, 4.2),
      ('H–C–O', 3.3, 4.6), ('alkena', 4.5, 6.5), ('aromatik', 6.5, 8.5), ('aldehida', 9.3, 10.5), ('asam karboksilat', 10.0, 13.0)]
for i, (nm, a, b) in enumerate(g1):
    ax.barh(i, b - a, left=a, color=B if i % 2 == 0 else MUDA, height=.62)
    ax.text(b + 0.2 if b < 11 else a - 0.2, i, nm, va='center', ha='right' if b < 11 else 'left', fontsize=7.5)
ax.set_xlim(13.5, -0.5); ax.set_yticks([]); ax.set_xlabel('δ ¹H (ppm)'); koma(ax, y=False); ax.invert_yaxis()
for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
ax = axs[1]
g2 = [('alkil', 0, 50), ('C–N', 30, 65), ('C–O', 50, 90), ('alkuna', 65, 90), ('alkena', 100, 150), ('aromatik', 110, 160),
      ('ester, amida, asam', 160, 185), ('aldehida, keton', 190, 220)]
for i, (nm, a, b) in enumerate(g2):
    ax.barh(i, b - a, left=a, color=H if i % 2 == 0 else '#8fcfba', height=.62)
    ax.text(b + 3 if b < 190 else a - 3, i, nm, va='center', ha='right' if b < 190 else 'left', fontsize=7.5)
ax.set_xlim(230, -10); ax.set_yticks([]); ax.set_xlabel('δ ¹³C (ppm)'); koma(ax, y=False); ax.invert_yaxis()
for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
f.tight_layout(); sv(f, 'c_geseran.png')

# 3. Etil asetat
from math import comb
f = plt.figure(figsize=(6.8, 4.4)); ax = f.add_axes([0.06, 0.55, 0.9, 0.4]); sp(ax)
x = np.linspace(0.8, 4.5, 40000); J = 7.1 / 400; w = 0.8 / 400
def eas(x):
    y = np.zeros_like(x)
    for d, n, nH in [(4.12, 3, 2), (1.26, 2, 3), (2.05, 0, 3)]:
        for k in range(n + 1): y += nH * comb(n, k) / 2 ** n * lor(x, d + (k - n / 2) * J, w)
    return y
y = eas(x); ax.plot(x, y, color=TUA, lw=.8); ax.set_xlim(4.5, 0.8); ax.set_yticks([]); ax.spines['left'].set_visible(False)
ax.set_xlabel('δ (ppm)'); koma(ax, y=False); ax.set_ylim(0, max(y) * 1.3)
ax.text(4.12, 1.2, 'OCH₂', ha='center', fontsize=8, color=B); ax.text(2.05, max(y) * 1.05, 'CH₃CO', ha='center', fontsize=8, color=B)
ax.text(1.26, 1.8, 'CH₃', ha='center', fontsize=8, color=B)
for k, (d, nm) in enumerate([(4.12, 'kuartet OCH₂'), (1.26, 'triplet CH₃')]):
    a2 = f.add_axes([0.06 + k * 0.33, 0.08, 0.27, 0.32]); sp(a2); xx = np.linspace(d - 0.05, d + 0.05, 4000)
    a2.plot((xx - d) * 400, eas(xx), color=B, lw=1); a2.set_xlim(20, -20); a2.set_yticks([]); a2.spines['left'].set_visible(False)
    a2.set_xlabel('ν − ν(pusat) (Hz)', fontsize=8); a2.set_title(nm, fontsize=8.5); koma(a2, y=False)
ia = f.add_axes([0.73, 0.06, 0.24, 0.38]); ia.axis('off')
lv = [[0], [-.5, .5], [-1, 0, 1], [-1.5, -.5, .5, 1.5]]
for r in range(3):
    for xx in lv[r]:
        for dd in [-.5, .5]: ia.plot([xx, xx + dd], [3 - r, 2 - r], color=B, lw=.8)
for xx, I in zip(lv[3], [1, 3, 3, 1]): ia.plot([xx, xx], [0, -I * 0.3], color=J2, lw=2.2)
for xx, I in zip(lv[3], [1, 3, 3, 1]): ia.text(xx, -I * 0.3 - 0.35, str(I), ha='center', fontsize=7.5)
ia.text(0, 3.2, 'OCH₂ + 3 proton CH₃', ha='center', fontsize=7.5); ia.set_xlim(-2, 2); ia.set_ylim(-1.6, 3.5)
ia.annotate('', xy=(-1.5, 1.75), xytext=(-0.5, 1.75), arrowprops=dict(arrowstyle='<->', color=TUA, lw=.6)); ia.text(-1.0, 1.85, '$J$', fontsize=7.5, ha='center')
sv(f, 'c_etilasetat.png')

# 4. Karplus
f, ax = plt.subplots(figsize=(4.8, 2.9)); sp(ax)
ph = np.linspace(0, 180, 300); c = np.cos(np.radians(ph))
ax.plot(ph, 7.76 * c * c - 1.10 * c + 1.40, color=B, lw=1.8)
for p, nm in [(60, 'aks–ekuat\nekuat–ekuat'), (180, 'aks–aks')]:
    cc = np.cos(np.radians(p)); v = 7.76 * cc * cc - 1.10 * cc + 1.40
    ax.plot(p, v, 'o', color=J2, ms=6); ax.text(p - 4 if p == 180 else p + 6, v + 0.6, nm, fontsize=8, ha='right' if p == 180 else 'left')
ax.set_xlabel('sudut dihedral φ (°)'); ax.set_ylabel('³J (Hz)'); ax.set_xticks([0, 30, 60, 90, 120, 150, 180]); ax.set_ylim(0, 12); koma(ax)
sv(f, 'c_karplus.png')

# 5. AB
f, ax = plt.subplots(figsize=(5.2, 4.4)); sp(ax)
x = np.linspace(-80, 80, 6000)
for i, r in enumerate([10, 3, 1, 0.3, 0]):
    g = spektrum([5 * r, -5 * r], [[0, 10], [10, 0]]); y = sum(I * lor(x, fr, 0.8) for fr, I in g.items())
    off = -i * 1.15; ax.plot(x, off + y / 1.0, color=[B, H, J2, TUA, B][i], lw=1)
    ax.text(62, off + 0.25, f'Δν/J = {r:g}'.replace('.', ','), fontsize=8)
ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.set_xlabel('ν − ν̄ (Hz)'); ax.set_xlim(-80, 80); koma(ax, y=False)
sv(f, 'c_ab.png')

# 6. pertukaran dua tapak
f, ax = plt.subplots(figsize=(5.2, 4.4)); sp(ax)
dn = 30.0; x = np.linspace(-45, 45, 3000); R2 = 1 / 0.5
def garis(k):
    W = 2 * np.pi * np.array([dn / 2, -dn / 2]); out = []
    for nu in x:
        A = np.array([[1j * (2 * np.pi * nu - W[0]) + R2 + k, -k], [-k, 1j * (2 * np.pi * nu - W[1]) + R2 + k]])
        out.append(np.real(np.ones(2) @ np.linalg.solve(A, np.array([.5, .5]))))
    return np.array(out)
ks = [2, 20, 50, 66.6, 150, 1000]
for i, k in enumerate(ks):
    y = garis(k); y = y / y.max(); off = -i * 1.2
    ax.plot(x, off + y, color=[B, H, J2, TUA, H, B][i], lw=1.1)
    ax.text(47, off + 0.25, f'$k$ = {k:g} s$^{{-1}}$'.replace('.', ',') + (' (koalesensi)' if k == 66.6 else ''), fontsize=8)
ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.set_xlabel('ν (Hz)'); koma(ax, y=False); ax.set_xlim(-45, 45)
sv(f, 'c_tukar.png')

# 7. model vektor, FID, spektrum
f = plt.figure(figsize=(6.8, 4.9))
def bola(ax):
    ax.set_box_aspect((1, 1, 1)); ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1); ax.set_axis_off()
    for v, nm in [((1.15, 0, 0), "x′"), ((0, 1.15, 0), "y′"), ((0, 0, 1.15), 'z')]:
        ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color='#999', lw=.7); ax.text(*[1.08 * t for t in v], nm, fontsize=8)
    u = np.linspace(0, 2 * np.pi, 60); ax.plot(np.cos(u), np.sin(u), 0 * u, color='#ccc', lw=.6)
ax = f.add_subplot(2, 2, 1, projection='3d'); bola(ax); ax.view_init(18, 35)
th = np.linspace(0, np.pi / 2, 40); ax.plot(0 * th, -np.sin(th), np.cos(th), color=J2, lw=1.6)
ax.quiver(0, 0, 0, 0, 0, 1, color=B, lw=1.6, arrow_length_ratio=.12); ax.quiver(0, 0, 0, 0, -1, 0, color=TUA, lw=1.8, arrow_length_ratio=.12)
ax.quiver(0, 0, 0, 0.9, 0, 0, color=H, lw=1.6, arrow_length_ratio=.15); ax.text(0.7, 0.05, -0.25, '$B_1$', color=H, fontsize=9)
ax.text(0, 0.1, 1.0, '$M_0$', color=B, fontsize=9); ax.set_title('(a) pulsa 90°', fontsize=9)
ax = f.add_subplot(2, 2, 2, projection='3d'); bola(ax); ax.view_init(25, 35)
t = np.linspace(0, 0.3, 800); Om = 2 * np.pi * 20; T2, T1 = 0.08, 0.2
mx = np.sin(Om * t) * np.exp(-t / T2); my = -np.cos(Om * t) * np.exp(-t / T2); mz = 1 - np.exp(-t / T1)
ax.plot(mx, my, mz, color=B, lw=1); ax.quiver(0, 0, 0, 0, -1, 0, color=TUA, lw=1.5, arrow_length_ratio=.12); ax.set_title('(b) presesi dan relaksasi', fontsize=9)
ax = f.add_subplot(2, 2, 3); sp(ax)
SW, N, T2 = 1000.0, 4096, 0.2; tt = np.arange(N) / SW
fid = (np.exp(2j * np.pi * 120 * tt) + 0.5 * np.exp(-2j * np.pi * 250 * tt)) * np.exp(-tt / T2)
ax.plot(tt, fid.real, color=B, lw=.5); ax.set_xlim(0, 0.6); ax.set_xlabel('$t$ (s)'); ax.set_yticks([]); ax.set_title('(c) FID (bagian riil)', fontsize=9); koma(ax, y=False)
ax = f.add_subplot(2, 2, 4); sp(ax)
sp_ = np.fft.fftshift(np.fft.fft(fid)).real; fr = np.fft.fftshift(np.fft.fftfreq(N, 1 / SW))
ax.plot(fr, sp_ / sp_.max(), color=J2, lw=1); ax.set_xlim(400, -400); ax.set_xlabel('ν (Hz)'); ax.set_yticks([]); ax.set_title('(d) spektrum', fontsize=9); koma(ax, y=False)
f.tight_layout(); sv(f, 'c_vektor.png')

# 8. relaksasi
f, axs = plt.subplots(1, 3, figsize=(6.8, 2.4))
ax = axs[0]; sp(ax); tau = np.linspace(0, 5, 300)
ax.plot(tau, 1 - 2 * np.exp(-tau), color=B, lw=1.6); ax.axhline(0, color='#999', lw=.6); ax.axvline(np.log(2), color=J2, lw=.8, ls='--')
ax.text(np.log(2) + 0.15, -0.7, '$T_1\\ln 2$', color=J2, fontsize=8); ax.set_xlabel('$\\tau/T_1$'); ax.set_ylabel('$M_z/M_0$'); ax.set_title('(a)', fontsize=9); koma(ax)
ax = axs[1]; sp(ax); t = np.linspace(0, 4, 300)
ax.plot(t, np.exp(-t), color=B, lw=1.6, label='$T_2$'); ax.plot(t, np.exp(-t * 3), color=J2, lw=1.4, ls='--', label='$T_2^*$')
ax.legend(frameon=False, fontsize=8); ax.set_xlabel('$t/T_2$'); ax.set_ylabel('$M_\\perp/M_0$'); ax.set_title('(b)', fontsize=9); koma(ax)
ax = axs[2]; sp(ax)
hb = 1.054571817e-34; gH = 26.7522128e7; r = 1.52e-10; w0 = 2 * np.pi * 400e6; K = 0.3 * 1e-14 * gH ** 4 * hb ** 2 / r ** 6
tc = np.logspace(-12, -7, 300); Jw = lambda w: tc / (1 + (w * tc) ** 2)
R1 = K * (Jw(w0) + 4 * Jw(2 * w0)); R2 = K / 2 * (3 * tc + 5 * Jw(w0) + 2 * Jw(2 * w0))
ax.loglog(tc, 1 / R1, color=B, lw=1.6, label='$T_1$'); ax.loglog(tc, 1 / R2, color=J2, lw=1.4, ls='--', label='$T_2$')
ax.axvline(0.6158 / w0, color='#999', lw=.6, ls=':'); ax.legend(frameon=False, fontsize=8); ax.set_xlabel('$\\tau_c$ (s)'); ax.set_ylabel('waktu (s)'); ax.set_title('(c)', fontsize=9)
f.tight_layout(); sv(f, 'c_relaksasi.png')

# 9. COSY 1-propanol
f, ax = plt.subplots(figsize=(4.6, 4.6))
d = {'CH₃': 0.94, 'CH₂': 1.57, 'OCH₂': 3.58}; X, Y = np.meshgrid(np.linspace(0.5, 4.0, 400), np.linspace(0.5, 4.0, 400))
Z = np.zeros_like(X); s = 0.05
pk = [(v, v) for v in d.values()] + [(0.94, 1.57), (1.57, 0.94), (1.57, 3.58), (3.58, 1.57)]
for a, b in pk: Z += np.exp(-((X - a) ** 2 + (Y - b) ** 2) / (2 * s * s))
ax.contour(X, Y, Z, levels=[0.15, 0.35, 0.6, 0.85], colors=[MUDA, B, B, TUA], linewidths=.9)
ax.plot([0.5, 4], [0.5, 4], color='#bbb', lw=.6, ls=':')
for nm, v in d.items(): ax.text(v, 0.45, nm, ha='center', va='bottom', fontsize=8, color=TUA)
ax.annotate('', xy=(1.57, 0.94), xytext=(0.94, 0.94), arrowprops=dict(arrowstyle='->', color=J2, lw=.9))
ax.annotate('', xy=(3.58, 1.57), xytext=(1.57, 1.57), arrowprops=dict(arrowstyle='->', color=J2, lw=.9))
ax.set_xlim(4.0, 0.5); ax.set_ylim(4.0, 0.5); ax.set_xlabel('δ $F_2$ (ppm)'); ax.set_ylabel('δ $F_1$ (ppm)'); koma(ax)
sv(f, 'c_cosy.png')

# 10. ESR turunan
from math import comb
f, axs = plt.subplots(3, 1, figsize=(5.6, 5.2))
def dlor(x, x0, w): return -(x - x0) / ((x - x0) ** 2 + (w / 2) ** 2) ** 2
for ax, (nm, a, ints, w, rng) in zip(axs, [('(a) ·CH₃', 2.30, [comb(3, k) for k in range(4)], 0.08, 5.5),
                                         ('(b) C$_6$H$_6^{-}$·', 0.375, [comb(6, k) for k in range(7)], 0.03, 1.6),
                                         ('(c) nitroksida', 1.6, [1, 1, 1], 0.08, 2.6)]):
    sp(ax); x = np.linspace(-rng, rng, 4000); n = len(ints); y = sum(I * dlor(x, (k - (n - 1) / 2) * a, w) for k, I in enumerate(ints))
    ax.plot(x, y / abs(y).max(), color=B, lw=.9); ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.text(-rng, 0.7, nm, fontsize=8.5)
    koma(ax, y=False); ax.set_xlim(-rng, rng)
axs[2].set_xlabel('$B - B_0$ (mT)'); f.tight_layout(); sv(f, 'c_esr.png')

# 11. MRI
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
ax = axs[0]; sp(ax); x = np.linspace(-10, 10, 800)
prof = np.where(np.abs(x + 4) < 2, np.sqrt(np.clip(4 - (x + 4) ** 2, 0, None)), 0) + 0.6 * np.where(np.abs(x - 4.5) < 1.2, np.sqrt(np.clip(1.44 - (x - 4.5) ** 2, 0, None)), 0) * 1.6
ax.fill_between(x, 0, prof, color=MUDA); ax.plot(x, prof, color=B, lw=1.2)
ax2 = ax.twiny(); ax2.set_xlim(-10 * 4.258, 10 * 4.258); ax2.set_xlabel('ν − ν₀ (kHz), $G_x$ = 10 mT/m', fontsize=8); ax2.xaxis.set_major_formatter(KOMA)
ax.set_xlabel('$x$ (cm)'); ax.set_yticks([]); ax.set_xlim(-10, 10); koma(ax, y=False); ax.set_title('(a)', fontsize=9, loc='left')
ax = axs[1]; sp(ax)
tis = [('materi\nputih', 600, 80, .70), ('materi\nabu-abu', 950, 100, .80), ('CSS', 4000, 2000, 1.0)]
xx = np.arange(3); wdt = 0.36
s1 = [r * (1 - np.exp(-500 / T1)) * np.exp(-15 / T2) for _, T1, T2, r in tis]; s2 = [r * (1 - np.exp(-4000 / T1)) * np.exp(-100 / T2) for _, T1, T2, r in tis]
ax.bar(xx - wdt / 2, s1, wdt, color=B, label='berbobot $T_1$'); ax.bar(xx + wdt / 2, s2, wdt, color=J1, label='berbobot $T_2$')
ax.set_xticks(xx); ax.set_xticklabels([t[0] for t in tis], fontsize=8); ax.set_ylabel('sinyal relatif'); ax.legend(frameon=False, fontsize=8); koma(ax, x=False)
ax.set_title('(b)', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_mri.png')
print('ok')
