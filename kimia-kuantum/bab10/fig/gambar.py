#!/usr/bin/env python3
# Gambar Bab 10 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, FancyArrowPatch
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
def atom(ax, x, y, r, c, t='', fs=8, tc='white', z=5):
    ax.add_patch(Circle((x, y), r, fc=c, ec=TUA, lw=0.8, zorder=z))
    if t: ax.text(x, y, t, ha='center', va='center', fontsize=fs, color=tc, zorder=z + 1, fontweight='bold')

# ---------------------------------------------------------------- 1. unsur simetri H2O dan NH3
f = plt.figure(figsize=(6.8, 3.0))
ax = f.add_axes([0.0, 0.0, 0.5, 1.0], projection='3d'); ax.axis('off')
th = np.radians(104.5) / 2; r = 1.0
O = np.array([0, 0, 0.25]); H1 = O + np.array([0, r * np.sin(th), -r * np.cos(th)]); H2 = O + np.array([0, -r * np.sin(th), -r * np.cos(th)])
# bidang yz (bidang molekul) dan xz
yy, zz = np.meshgrid([-1.1, 1.1], [-0.8, 1.0])
ax.plot_surface(0 * yy, yy, zz, color=MUDA, alpha=0.25, shade=False)
xx, zz2 = np.meshgrid([-1.0, 1.0], [-0.8, 1.0])
ax.plot_surface(xx, 0 * xx, zz2, color=J1, alpha=0.22, shade=False)
ax.plot([0, 0], [0, 0], [-1.0, 1.25], color=TUA, lw=1.4)
ax.text(0.15, 0, 1.18, '$C_2$ ($z$)', fontsize=8.5, ha='left')
for P in (H1, H2): ax.plot(*zip(O, P), color=TUA, lw=2.5)
ax.scatter(*O, s=260, color=J2, edgecolor=TUA, depthshade=False); ax.scatter(*zip(H1, H2), s=110, color='white', edgecolor=TUA, depthshade=False)
ax.text(0, 1.05, -0.75, "$\\sigma_v'(yz)$", fontsize=8, color=B); ax.text(0.95, 0, 0.95, '$\\sigma_v(xz)$', fontsize=8, color=J2)
ax.text(0, 0, 0.42, 'O', fontsize=8); ax.view_init(elev=14, azim=28); ax.set_box_aspect((1, 1, 1))
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-0.9, 1.1); ax.set_title('H₂O ($C_{2v}$)', fontsize=9, y=1.0)
ax = f.add_axes([0.53, 0.05, 0.45, 0.88]); ax.set_aspect('equal'); ax.axis('off')
angs = [90, 210, 330]
for k, a in enumerate(angs):
    c, s = np.cos(np.radians(a)), np.sin(np.radians(a))
    ax.plot([-1.25 * c, 1.25 * c], [-1.25 * s, 1.25 * s], ls='--', color=J2, lw=1)
    ax.text(1.38 * c, 1.38 * s, f'$\\sigma_{k + 1}$', ha='center', va='center', fontsize=9, color=J2)
    ax.plot([0, c], [0, s], color=TUA, lw=2.2, zorder=3); atom(ax, c, s, 0.13, 'white', f'H{k + 1}'.replace('H', 'H'), fs=6.5, tc=TUA)
atom(ax, 0, 0, 0.17, B, 'N', fs=8)
ax.annotate('', xy=(0.42 * np.cos(np.radians(150)), 0.42 * np.sin(np.radians(150))), xytext=(0.42 * np.cos(np.radians(40)), 0.42 * np.sin(np.radians(40))),
            arrowprops=dict(arrowstyle='->', color=H, lw=1.3, connectionstyle='arc3,rad=0.45'))
ax.text(0.05, 0.55, '$C_3$', color=H, fontsize=9); ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.5, 1.6)
ax.set_title('NH₃ ($C_{3v}$), dilihat dari atas', fontsize=9)
sv(f, 'c_unsur.png')

# ---------------------------------------------------------------- 2. diagram alir
f, ax = plt.subplots(figsize=(6.8, 5.6)); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 10)
def kotak(x, y, t, w=2.6, h=0.62, c=MUDA, fs=7.6, tc=TUA):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.04,rounding_size=0.15', fc=c, ec=TUA, lw=0.8))
    ax.text(x, y, t, ha='center', va='center', fontsize=fs, color=tc)
def hasil(x, y, t, w=1.15): kotak(x, y, t, w=w, h=0.5, c=TUA, fs=8.2, tc='white')
def panah(x1, y1, x2, y2, t='', dx=0.1, dy=0.0):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='->', color=TUA, lw=0.8))
    if t: ax.text((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, t, fontsize=7, color=J2, ha='left', va='center')
kotak(2.0, 9.4, 'Linear?')
panah(3.3, 9.4, 4.3, 9.4, 'ya', -0.2, 0.18); kotak(5.6, 9.4, 'Pusat inversi?', w=2.4)
panah(6.8, 9.4, 7.6, 9.4, 'ya', -0.2, 0.18); hasil(8.25, 9.4, '$D_{\\infty h}$')
panah(6.6, 9.09, 7.75, 8.62, 'tidak', 0.05, 0.12); hasil(8.25, 8.4, '$C_{\\infty v}$')
panah(2.0, 9.09, 2.0, 8.2, 'tidak')
kotak(2.0, 7.9, 'Dua atau lebih $C_n$, $n \\geq 3$?', w=3.2)
panah(3.6, 7.9, 4.5, 7.9, 'ya', -0.2, 0.18); kotak(6.0, 7.9, 'Ada $C_5$? → $I_h$\nAda $C_4$? → $O_h$\nlainnya → $T_d$', w=2.8, h=0.95)
panah(2.0, 7.59, 2.0, 6.85, 'tidak')
kotak(2.0, 6.55, 'Ada sumbu $C_n$?', w=2.6)
panah(3.3, 6.55, 4.3, 6.55, 'tidak', -0.25, 0.18); kotak(6.0, 6.55, 'Ada $\\sigma$? → $C_s$\nAda $i$? → $C_i$\nlainnya → $C_1$', w=2.8, h=0.95)
panah(2.0, 6.24, 2.0, 5.5, 'ya')
kotak(2.0, 5.2, 'Pilih sumbu utama $C_n$.\nAda $n$ sumbu $C_2 \\perp C_n$?', w=3.4, h=0.85)
panah(3.7, 5.2, 5.35, 5.2, 'ya', -0.2, 0.18)
kotak(6.4, 5.2, 'Ada $\\sigma_h$?', w=2.0)
panah(7.4, 5.2, 8.0, 5.2, 'ya', -0.2, 0.18); hasil(8.6, 5.2, '$D_{nh}$', w=1.0)
panah(6.4, 4.89, 6.4, 4.35, 'tidak'); kotak(6.4, 4.05, 'Ada $n$ $\\sigma_d$?', w=2.0)
panah(7.4, 4.05, 8.0, 4.05, 'ya', -0.2, 0.18); hasil(8.6, 4.05, '$D_{nd}$', w=1.0)
panah(6.4, 3.74, 6.4, 3.2, 'tidak'); hasil(6.4, 2.95, '$D_n$', w=1.0)
panah(2.0, 4.77, 2.0, 3.95, 'tidak')
kotak(2.0, 3.65, 'Ada $\\sigma_h$?', w=2.0)
panah(3.0, 3.65, 3.8, 3.65, 'ya', -0.2, 0.18); hasil(4.4, 3.65, '$C_{nh}$', w=1.0)
panah(2.0, 3.34, 2.0, 2.75, 'tidak'); kotak(2.0, 2.45, 'Ada $n$ $\\sigma_v$?', w=2.0)
panah(3.0, 2.45, 3.8, 2.45, 'ya', -0.2, 0.18); hasil(4.4, 2.45, '$C_{nv}$', w=1.0)
panah(2.0, 2.14, 2.0, 1.55, 'tidak'); kotak(2.0, 1.25, 'Ada $S_{2n}$ berimpit $C_n$?', w=3.0)
panah(3.5, 1.25, 4.3, 1.25, 'ya', -0.2, 0.18); hasil(4.9, 1.25, '$S_{2n}$', w=1.0)
panah(2.0, 0.94, 2.0, 0.45, 'tidak'); hasil(2.0, 0.2, '$C_n$', w=1.0)
sv(f, 'c_alir.png')

# ---------------------------------------------------------------- 3. C3v tidak komutatif
f, axs = plt.subplots(2, 4, figsize=(6.8, 3.6))
def nh3(ax, isi, judul, bidang=None):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.2, 1.4)
    for k, a in enumerate(angs):
        c, s = np.cos(np.radians(a)), np.sin(np.radians(a))
        ax.plot([0, c], [0, s], color='#999', lw=1.2, zorder=1)
        warna = {'a': B, 'b': J1, 'c': H}[isi[k]]
        atom(ax, c, s, 0.2, warna, isi[k], fs=8)
        ax.text(1.42 * c, 1.42 * s - 0.02, str(k + 1), fontsize=6.5, color='#888', ha='center', va='center')
    atom(ax, 0, 0, 0.12, TUA)
    if bidang is not None:
        c, s = np.cos(np.radians(angs[bidang])), np.sin(np.radians(angs[bidang]))
        ax.plot([-1.2 * c, 1.2 * c], [-1.2 * s, 1.2 * s], ls='--', color=J2, lw=1)
    ax.set_title(judul, fontsize=8)
nh3(axs[0, 0], 'abc', 'awal'); nh3(axs[0, 1], 'acb', 'setelah $\\sigma_1$', 0); nh3(axs[0, 2], 'bac', 'lalu $C_3$')
nh3(axs[0, 3], 'bac', '= $\\sigma_3$ dari awal', 2)
nh3(axs[1, 0], 'abc', 'awal'); nh3(axs[1, 1], 'cab', 'setelah $C_3$'); nh3(axs[1, 2], 'cba', 'lalu $\\sigma_1$', 0)
nh3(axs[1, 3], 'cba', '= $\\sigma_2$ dari awal', 1)
f.text(0.01, 0.73, '$C_3\\sigma_1$', fontsize=9, rotation=90, va='center'); f.text(0.01, 0.27, '$\\sigma_1C_3$', fontsize=9, rotation=90, va='center')
f.subplots_adjust(wspace=0.05, hspace=0.25, left=0.04); sv(f, 'c_c3v.png')

# ---------------------------------------------------------------- 4. SALC
f, axs = plt.subplots(1, 7, figsize=(6.9, 1.9))
def salc(ax, pos, coef, judul, bawah, pusat=True):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.45, 1.45)
    for (x, y), c in zip(pos, coef):
        ax.plot([0, x], [0, y], color='#bbb', lw=1, zorder=1)
        if abs(c) > 1e-9:
            ax.add_patch(Circle((x, y), 0.55 * np.sqrt(abs(c)), fc=B if c > 0 else J1, ec=TUA, lw=0.6, alpha=0.9, zorder=3))
        else:
            ax.add_patch(Circle((x, y), 0.08, fc='white', ec=TUA, lw=0.6, zorder=3))
    if pusat: atom(ax, 0, 0, 0.1, TUA)
    ax.set_title(judul, fontsize=8); ax.text(0, -1.55, bawah, ha='center', fontsize=7.5, color=TUA)
t2 = np.radians(52.25)
pw = [(np.sin(t2), -np.cos(t2)), (-np.sin(t2), -np.cos(t2))]
salc(axs[0], pw, [0.5, 0.5], 'H₂O $a_1$', '$2s$, $2p_z$')
salc(axs[1], pw, [0.5, -0.5], 'H₂O $b_2$', '$2p_y$')
pn = [(np.cos(np.radians(a)), np.sin(np.radians(a))) for a in angs]
salc(axs[2], pn, [1 / 3, 1 / 3, 1 / 3], 'NH₃ $a_1$', '$2s$, $2p_z$')
salc(axs[3], pn, [4 / 6, -1 / 6, -1 / 6], 'NH₃ $e$ (a)', '$2p_y$')
salc(axs[4], pn, [0, 0.5, -0.5], 'NH₃ $e$ (b)', '$-2p_x$')
pc = [(0.75, 0.75), (-0.75, -0.75), (0.75, -0.75), (-0.75, 0.75)]   # proyeksi H1..H4 ke bidang xy
salc(axs[5], pc, [0.25] * 4, 'CH₄ $a_1$', '$2s$')
salc(axs[6], pc, [0.25, -0.25, 0.25, -0.25], 'CH₄ $t_2$ ($x$)', '$2p_x$')
f.subplots_adjust(wspace=0.08); sv(f, 'c_salc.png')

# ---------------------------------------------------------------- 5. diagram OM H2O
f, ax = plt.subplots(figsize=(6.4, 4.6)); sp(ax)
def lv(x, E, w=0.7, c=TUA, lw=1.8): ax.plot([x - w / 2, x + w / 2], [E, E], color=c, lw=lw, solid_capstyle='round')
def el(x, E, n=2):
    if n == 2: ax.text(x, E + 0.15, '↑↓', ha='center', va='bottom', fontsize=8, color=J2, fontweight='bold')
# orbital atom O (kiri) dan SALC H (kanan)
EO2s, EO2p, EH = -32.4, -15.9, -13.6
lv(0.6, EO2s); ax.text(0.15, EO2s, 'O 2s ($a_1$)', ha='right', va='center', fontsize=7.5)
for dx in (-0.45, 0, 0.45): lv(0.6 + dx, EO2p, w=0.36)
ax.text(0.6, EO2p - 1.4, '$2p_x$ $b_1$   $2p_y$ $b_2$   $2p_z$ $a_1$', ha='center', fontsize=7, va='top')
ax.text(0.6, EO2p + 0.6, 'O 2p', ha='center', fontsize=7.5)
for dx in (-0.22, 0.22): lv(5.2 + dx, EH, w=0.36)
ax.text(5.2, EH + 0.6, 'H 1s (SALC)', ha='center', fontsize=7.5); ax.text(5.2, EH - 1.4, '$a_1$      $b_2$', ha='center', fontsize=7, va='top')
MO = [('$2a_1$', -32.2, 2), ('$1b_2$', -18.5, 2), ('$3a_1$', -14.7, 2), ('$1b_1$', -12.6, 2), ('$4a_1$', -2.0, 0), ('$2b_2$', 0.0, 0)]
for nm, E, n in MO:
    c = TUA if n else '#888'
    lv(2.9, E, w=0.8, c=c); el(2.9, E, n); ax.text(3.45, E, nm, va='center', fontsize=8, color=c)
    if n: ax.text(2.35, E, f'{-E:.1f} eV'.replace('.', ','), ha='right', va='center', fontsize=6.8, color=B)
def gar(x1, E1, x2, E2): ax.plot([x1, x2], [E1, E2], color='#9ab', lw=0.6, ls=':')
for E in (-32.2, -14.7, -2.0): gar(0.95, EO2s if E == -32.2 else EO2p, 2.5, E)
gar(0.95, EO2p, 2.5, -18.5); gar(0.95, EO2p, 2.5, -12.6); gar(0.95, EO2p, 2.5, 0.0)
for E in (-32.2, -18.5, -14.7, -2.0, 0.0): gar(4.84, EH, 3.3, E)
ax.set_xlim(-1.5, 6.2); ax.set_ylim(-35, 3); ax.set_xticks([]); ax.set_ylabel('energi (eV)'); koma(ax, x=False)
ax.spines['bottom'].set_visible(False)
ax.text(2.9, 2.0, 'H₂O', ha='center', fontsize=9, fontweight='bold')
ax.text(2.9, -6.5, 'kosong (kualitatif)', ha='center', fontsize=7, color='#888')
sv(f, 'c_mo_h2o.png')

# ---------------------------------------------------------------- 6. benzena
f = plt.figure(figsize=(6.8, 3.0))
ax = f.add_axes([0.02, 0.1, 0.27, 0.82]); sp(ax)
lev = [(2, [0]), (1, [-1, 1]), (-1, [-2, 2]), (-2, [3])]
nam = {2: '$a_{2u}$', 1: '$e_{1g}$', -1: '$e_{2u}$', -2: '$b_{2g}$'}
for x_, ks in lev:
    E = -x_
    xs = [0.5] if len(ks) == 1 else [0.25, 0.75]
    for xx in xs:
        ax.plot([xx - 0.18, xx + 0.18], [E, E], color=TUA, lw=1.8)
        if x_ > 0: ax.text(xx, E + 0.08, '↑↓', ha='center', va='bottom', fontsize=8, color=J2, fontweight='bold')
    ax.text(1.02, E, nam[x_], va='center', fontsize=8)
ax.set_yticks([-2, -1, 0, 1, 2]); ax.set_yticklabels(['$\\alpha+2\\beta$', '$\\alpha+\\beta$', '$\\alpha$', '$\\alpha-\\beta$', '$\\alpha-2\\beta$'], fontsize=7.5)
ax.set_xticks([]); ax.set_xlim(0, 1.3); ax.set_ylim(-2.6, 2.6); ax.axhline(0, color='#ddd', lw=0.6, zorder=0)
pos = [(np.cos(np.radians(90 - 60 * j)), np.sin(np.radians(90 - 60 * j))) for j in range(6)]
orb = [('$k = 0$', [1] * 6), ('$k = \\pm1$ (cos)', [np.cos(pi * j / 3) for j in range(6)]), ('$k = \\pm1$ (sin)', [np.sin(pi * j / 3) for j in range(6)]),
       ('$k = \\pm2$ (cos)', [np.cos(2 * pi * j / 3) for j in range(6)]), ('$k = \\pm2$ (sin)', [np.sin(2 * pi * j / 3) for j in range(6)]), ('$k = 3$', [(-1) ** j for j in range(6)])]
for i, (t, c) in enumerate(orb):
    ax = f.add_axes([0.32 + (i % 3) * 0.225, 0.52 - (i // 3) * 0.47, 0.21, 0.44]); ax.set_aspect('equal'); ax.axis('off')
    c = np.array(c); c = c / np.sqrt((c ** 2).sum())
    xs, ys = zip(*pos); ax.add_patch(Polygon(pos, closed=True, fill=False, ec='#999', lw=1))
    for (x, y), cc in zip(pos, c):
        if abs(cc) > 1e-9: ax.add_patch(Circle((x, y), 0.62 * abs(cc), fc=B if cc > 0 else J1, ec=TUA, lw=0.5, alpha=0.9))
        else: ax.plot(x, y, 'o', ms=2.5, color=TUA)
    ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.45, 1.45); ax.set_title(t, fontsize=7.5, pad=1)
sv(f, 'c_benzena.png')

# ---------------------------------------------------------------- 7. mode normal H2O (medan gaya valensi)
mO, mH = 15.995, 1.008; r0 = 0.9572; th0 = np.radians(104.52)
X0 = np.array([0, 0, 0.0, 0, r0 * np.sin(th0 / 2), -r0 * np.cos(th0 / 2), 0, -r0 * np.sin(th0 / 2), -r0 * np.cos(th0 / 2)])
def intern(X):
    O, A, C = X[0:3], X[3:6], X[6:9]
    a, c = A - O, C - O; r1, r2 = np.linalg.norm(a), np.linalg.norm(c)
    return np.array([r1, r2, np.arccos(a @ c / r1 / r2)])
Bm = np.zeros((3, 9)); hh = 1e-6
for k in range(9):
    d = np.zeros(9); d[k] = hh; Bm[:, k] = (intern(X0 + d) - intern(X0 - d)) / (2 * hh)
F = np.array([[8.45, -0.10, 0.25], [-0.10, 8.45, 0.25], [0.25, 0.25, 0.76]])   # mdyn/Å, mdyn/rad
Hc = Bm.T @ F @ Bm; Mv = np.repeat([mO, mH, mH], 3)
Hm = Hc / np.sqrt(np.outer(Mv, Mv)); w, v = np.linalg.eigh(Hm)
nu = np.sqrt(np.clip(w, 0, None) * 1e2 / 1.66054e-27) / (2 * pi * 2.99792458e10)
idx = np.argsort(w)[-3:]
modes = [(i, nu[i]) for i in idx]
print('frekuensi model (cm^-1):', sorted([round(n) for _, n in modes]))
f, axs = plt.subplots(1, 3, figsize=(6.6, 2.4))
nmode = sorted(modes, key=lambda t: t[1])
judul = {0: 'tekuk ($A_1$), 1595 cm$^{-1}$', 1: 'ulur simetris ($A_1$), 3657 cm$^{-1}$', 2: 'ulur asimetris ($B_2$), 3756 cm$^{-1}$'}
urut = [1, 0, 2]
for ax, ii in zip(axs, urut):
    i, n_ = nmode[ii]; d = v[:, i] / np.sqrt(Mv); d = d / np.abs(d).max() * 0.45
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.3, 0.75)
    P = X0.reshape(3, 3)[:, 1:]; D = d.reshape(3, 3)[:, 1:]
    if D[0, 1] > 0 and ii == 1: D = -D
    for p_ in P[1:]: ax.plot([P[0, 0], p_[0]], [P[0, 1], p_[1]], color='#999', lw=2.5, zorder=1)
    atom(ax, *P[0], 0.17, J2, 'O', fs=8); atom(ax, *P[1], 0.11, 'white', 'H', fs=6.5, tc=TUA); atom(ax, *P[2], 0.11, 'white', 'H', fs=6.5, tc=TUA)
    for p_, dd in zip(P[1:], D[1:]):
        if np.hypot(*dd) > 0.02: ax.annotate('', xy=(p_[0] + dd[0], p_[1] + dd[1]), xytext=(p_[0], p_[1]), arrowprops=dict(arrowstyle='->', color=B, lw=1.6), zorder=8)
    ax.set_title(judul[ii], fontsize=8)
sv(f, 'c_mode_h2o.png')

# ---------------------------------------------------------------- 8. spektrum SF6 skematis
f, axs = plt.subplots(2, 1, figsize=(6.0, 3.2), sharex=True)
ir = [(948, 1.0, '$\\nu_3$ $T_{1u}$'), (615, 0.55, '$\\nu_4$ $T_{1u}$')]
ra = [(775, 1.0, '$\\nu_1$ $A_{1g}$'), (643, 0.35, '$\\nu_2$ $E_g$'), (525, 0.45, '$\\nu_5$ $T_{2g}$')]
for ax, data, t, c in [(axs[0], ir, 'IR', B), (axs[1], ra, 'Raman', H)]:
    sp(ax)
    for x, y, lab in data:
        ax.plot([x, x], [0, y], color=c, lw=2.2); ax.text(x, y + 0.06, lab, ha='center', fontsize=7.5)
    ax.axvline(348, color='#999', ls='--', lw=0.8); ax.set_ylim(0, 1.35); ax.set_yticks([])
    ax.text(0.01, 0.85, t, transform=ax.transAxes, fontsize=9, fontweight='bold', color=c)
axs[0].text(352, 1.05, '$\\nu_6$ $T_{2u}$ (bisu)', fontsize=7, color='#777')
axs[1].set_xlim(1050, 300); axs[1].set_xlabel('bilangan gelombang (cm$^{-1}$)'); koma(axs[1], y=False)
f.subplots_adjust(hspace=0.12); sv(f, 'c_sf6.png')

# ---------------------------------------------------------------- 9. CD skematis
lam = np.linspace(185, 250, 400)
def g(l0, s, a): return a * np.exp(-((lam - l0) / s) ** 2)
heliks = g(192, 6.5, 7.5) + g(208, 5.5, -3.6) + g(222, 8, -3.6)
beta = g(196, 6.5, 3.2) + g(217, 8, -1.9)
acak = g(198, 6, -4.2) + g(220, 6, 0.3)
f, ax = plt.subplots(figsize=(5.2, 3.0)); sp(ax)
ax.plot(lam, heliks, color=B, lw=1.8, label='heliks α'); ax.plot(lam, beta, color=H, lw=1.8, label='lembaran β'); ax.plot(lam, acak, color=J1, lw=1.8, label='acak')
ax.axhline(0, color='#999', lw=0.6); ax.set_xlabel('panjang gelombang (nm)'); ax.set_ylabel('$\\Delta\\varepsilon$ (satuan relatif)')
for l0 in (192, 208, 222): ax.axvline(l0, color=B, lw=0.5, ls=':')
ax.legend(frameon=False, fontsize=8); koma(ax); ax.set_xlim(185, 250)
sv(f, 'c_cd.png')
print('selesai')
