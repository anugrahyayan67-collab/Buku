#!/usr/bin/env python3
# Gambar Bab 11 Kimia Anorganik 1: senyawa koordinasi -> bab11/fig/*.png
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.ticker import FuncFormatter
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab11', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'mathtext.fontset': 'dejavusans'})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
def koma(ax, sb='xy'):
    fm = FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−'))
    if 'x' in sb: ax.xaxis.set_major_formatter(fm)
    if 'y' in sb: ax.yaxis.set_major_formatter(fm)
def proj(v, th=np.radians(30), ph=np.radians(28)):
    x, y, z = v; x1 = x * np.cos(th) - y * np.sin(th); y1 = x * np.sin(th) + y * np.cos(th)
    return np.array([x1, z * np.cos(ph) - y1 * np.sin(ph)]), y1 * np.cos(ph) + z * np.sin(ph)
def bola(ax, pusat, lig, warna, label=None, cx=0, cy=0, s=1.0, ikatan=None, lw=2):
    # lig: list (vec, warna, teks); gambar dari belakang ke depan
    items = [(proj(np.array(v) * s)[1], np.array(v) * s, c, t) for v, c, t in lig]
    items.sort(key=lambda a: a[0])
    p0, _ = proj((0, 0, 0))
    for dep, v, c, t in items:
        p, _ = proj(v); ax.plot([cx, cx + p[0]], [cy, cy + p[1]], color=ABU, lw=lw, zorder=2 + dep)
    ax.add_patch(Circle((cx, cy), .2 * s, fc=pusat, ec=TUA, zorder=5)); 
    if label: ax.text(cx, cy, label, ha='center', va='center', fontsize=7, color='white', zorder=6)
    for dep, v, c, t in items:
        p, _ = proj(v); z = 5 + dep * 2
        ax.add_patch(Circle((cx + p[0], cy + p[1]), .14 * s, fc=c, ec=TUA, zorder=z))
        if t: ax.text(cx + p[0], cy + p[1], t, ha='center', va='center', fontsize=6.5, zorder=z + .1, color=TUA if c in ('white', '#f5f6f7', MUDA, JG, '#9fd8a8') else 'white')
OKT = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
# 1. Werner: empat kompleks kobalt
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.9), gridspec_kw={'width_ratios': [1, 1.2]})
nm = ['CoCl$_3$·\n6NH$_3$\n(kuning)', 'CoCl$_3$·\n5NH$_3$\n(ungu-merah)', 'CoCl$_3$·\n4NH$_3$\n(hijau)', 'CoCl$_3$·\n4NH$_3$\n(ungu)']; wr = ['#e9a21b', '#8b2c6e', '#2e8b3a', '#6a3f9e']
for i, (n_, w) in enumerate(zip(nm, wr)):
    a1.add_patch(plt.Rectangle((i * 1.1, 0), .9, .9, fc=w, ec=TUA)); a1.text(i * 1.1 + .45, -.15, n_, ha='center', va='top', fontsize=7.3)
a1.set_xlim(-.1, 4.4); a1.set_ylim(-1.1, 1.0); a1.axis('off'); a1.set_title('warna yang berbeda', fontsize=9.5, color=TUA)
cmp = ['[Co(NH$_3$)$_6$]Cl$_3$', '[Co(NH$_3$)$_5$Cl]Cl$_2$', '[Co(NH$_3$)$_4$Cl$_2$]Cl', '[Co(NH$_3$)$_3$Cl$_3$]']; ag = [3, 2, 1, 0]; ion = [4, 3, 2, 0]
x = np.arange(4); a2.bar(x - .2, ag, .4, color=BIRU, label='mol AgCl mengendap'); a2.bar(x + .2, ion, .4, color=JGT, label='jumlah ion (konduktivitas)')
a2.set_xticks(x); a2.set_xticklabels(cmp, fontsize=7, rotation=18); a2.set_ylim(0, 5); a2.legend(fontsize=7.5, loc='upper right'); a2.set_title('Cl$^-$ bebas dan ion per rumus', fontsize=9.5, color=TUA)
simpan(f, 'a_werner')
# 2. geometri bilangan koordinasi
geo = [('KB 2: linear', [(1, 0, 0), (-1, 0, 0)]), ('KB 3: segitiga datar', [(np.cos(a), np.sin(a), 0) for a in np.radians([90, 210, 330])]),
       ('KB 4: tetrahedral', [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]), ('KB 4: bujur sangkar', [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]),
       ('KB 5: bipiramida trigonal', [(0, 0, 1), (0, 0, -1)] + [(np.cos(a), np.sin(a), 0) for a in np.radians([0, 120, 240])]), ('KB 5: piramida bujur sangkar', [(0, 0, 1), (1, 0, -.2), (-1, 0, -.2), (0, 1, -.2), (0, -1, -.2)]),
       ('KB 6: oktahedral', OKT), ('KB 6: prisma trigonal', [(np.cos(a), np.sin(a), s_) for s_ in (.8, -.8) for a in np.radians([90, 210, 330])])]
f, axs = plt.subplots(2, 4, figsize=(7.6, 4.0))
for ax, (t, L) in zip(axs.flat, geo):
    L = [np.array(v) / np.linalg.norm(v) for v in L]
    bola(ax, JGT, [(v, MUDA, '') for v in L], JGT)
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(t, fontsize=8.5, color=TUA)
simpan(f, 'a_geometri')
# 3. isomer
f, axs = plt.subplots(1, 4, figsize=(7.8, 2.4))
A, B = (MUDA, ''), ('#9fd8a8', '')
def okt(ax, warna, t):
    bola(ax, JGT, [(v, c, '') for v, c in zip(OKT, warna)], JGT); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.35, 1.3); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(t, fontsize=8.5, color=TUA)
g = '#3fae5a'; m = MUDA
okt(axs[0], [m, m, g, g if False else m, g, m], 'cis-MA$_4$B$_2$')
okt(axs[1], [m, m, m, m, g, g], 'trans-MA$_4$B$_2$')
okt(axs[2], [g, m, g, m, g, m], 'fac-MA$_3$B$_3$')
okt(axs[3], [g, g, m, m, g, m], 'mer-MA$_3$B$_3$')
simpan(f, 'b_isomer')
# 4. enantiomer M(AA)3: tampak sepanjang sumbu C3 (dua segitiga + kelat)
f, axs = plt.subplots(1, 2, figsize=(5.6, 2.8))
for ax, sgn, t in [(axs[0], -1, 'Δ (putar kanan)'), (axs[1], 1, 'Λ (putar kiri)')]:
    up = [np.radians(90 + 120 * k) for k in range(3)]; dn = [a + np.radians(60) for a in up]
    P = lambda a, r=1: (r * np.cos(a), r * np.sin(a))
    ax.add_patch(plt.Polygon([P(a) for a in dn], fc='none', ec=ABU, ls=':')); ax.add_patch(plt.Polygon([P(a) for a in up], fc='none', ec=ABU))
    for k in range(3):
        a0 = up[k]; a1 = up[k] + sgn * np.radians(60)
        x0, y0 = P(a0); x1, y1 = P(a1)
        ax.annotate('', (x1, y1), (x0, y0), arrowprops=dict(arrowstyle='-', color=JGT, lw=4, connectionstyle=f'arc3,rad={-.35 * sgn}'))
        ax.add_patch(Circle((x0, y0), .13, fc=MUDA, ec=TUA, zorder=4)); ax.add_patch(Circle((x1, y1), .13, fc=MUDA, ec=TUA, zorder=3, alpha=.7))
    ax.add_patch(Circle((0, 0), .17, fc=JGT, ec=TUA, zorder=5)); ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.3, 1.4); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(t, fontsize=9.5, color=TUA)
simpan(f, 'b_kiral')
# 5. orbital d dan ligan oktahedral (penampang bidang xy)
f, axs = plt.subplots(1, 2, figsize=(6.4, 3.1))
xx, yy = np.meshgrid(np.linspace(-2, 2, 300), np.linspace(-2, 2, 300)); r = np.hypot(xx, yy) + 1e-9
for ax, fn, t in [(axs[0], (xx ** 2 - yy ** 2) / r ** 2 * r ** 2 * np.exp(-r * 2.5), r'$d_{x^2-y^2}$ (e$_g$): menunjuk ke ligan'), (axs[1], (xx * yy) / r ** 2 * r ** 2 * np.exp(-r * 2.5), r'$d_{xy}$ (t$_{2g}$): di antara ligan')]:
    v = np.abs(fn).max(); ax.contourf(xx, yy, fn, levels=[-v, -.3 * v], colors=[MUDA]); ax.contourf(xx, yy, fn, levels=[.3 * v, v], colors=[JG])
    for p in [(1.6, 0), (-1.6, 0), (0, 1.6), (0, -1.6)]: ax.add_patch(Circle(p, .17, fc='#d2553b', ec=TUA)); ax.text(p[0], p[1], 'L', ha='center', va='center', color='white', fontsize=8)
    ax.axhline(0, color=ABU, lw=.6, ls=':'); ax.axvline(0, color=ABU, lw=.6, ls=':'); ax.text(1.85, .1, 'x', fontsize=9); ax.text(.08, 1.85, 'y', fontsize=9)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(t, fontsize=9, color=TUA)
simpan(f, 'c_orbital')
# 6. diagram pemisahan
f, ax = plt.subplots(figsize=(7.0, 3.6))
def lev(x, y, n, c=TUA, w=.32):
    for k in range(n): ax.plot([x + k * (w + .06), x + k * (w + .06) + w], [y, y], color=c, lw=2.2)
lev(.1, 0, 5, ABU, .2); ax.text(.7, -.35, 'ion bebas\n(bola)', ha='center', fontsize=8)
# oktahedral
lev(2.1, -.4, 3, BIRU); lev(2.29, .6, 2, JGT); ax.text(3.4, -.4, 't$_{2g}$', va='center'); ax.text(3.2, .6, 'e$_g$', va='center')
ax.annotate('', (2.0, .6), (2.0, -.4), arrowprops=dict(arrowstyle='<->')); ax.text(1.65, .1, 'Δ$_o$', fontsize=11)
ax.text(1.9, .15 - .02, '', fontsize=7); ax.text(2.7, -1.0, 'oktahedral', ha='center', fontsize=9, color=TUA)
ax.text(3.85, .6, '+0,6Δ$_o$', fontsize=7.5, va='center', color=JGT); ax.text(3.85, -.4, '−0,4Δ$_o$', fontsize=7.5, va='center', color=BIRU)
# tetrahedral
lev(5.0, -.18, 2, BIRU); lev(4.8, .26, 3, JGT); ax.text(5.9, -.18, 'e', va='center'); ax.text(6.05, .26, 't$_2$', va='center')
ax.annotate('', (4.65, .26), (4.65, -.18), arrowprops=dict(arrowstyle='<->')); ax.text(3.75, .0, 'Δ$_t$ ≈ $\\frac{4}{9}$Δ$_o$', fontsize=9)
ax.text(5.4, -1.0, 'tetrahedral', ha='center', fontsize=9, color=TUA)
# bujur sangkar
yl = [(-.75, 'd$_{xz}$, d$_{yz}$', 2), (-.45, 'd$_{z^2}$', 1), (-.05, 'd$_{xy}$', 1), (1.1, 'd$_{x^2-y^2}$', 1)]
for y_, t, n_ in yl: lev(7.4 + (0 if n_ == 2 else .19), y_, n_, JGT if y_ > 1 else BIRU); ax.text(8.35, y_, t, va='center', fontsize=8.5)
ax.text(7.9, -1.25, 'bujur sangkar', ha='center', fontsize=9, color=TUA)
for x0 in (1.05, 3.95 + .6, 6.7): pass
ax.set_xlim(0, 9.3); ax.set_ylim(-1.45, 1.4); ax.axis('off'); ax.set_ylabel('energi')
ax.annotate('', (-.05, 1.3), (-.05, -1.3), arrowprops=dict(arrowstyle='->', color=ABU)); ax.text(-.15, 0, 'energi', rotation=90, va='center', ha='right', color=ABU, fontsize=8.5)
simpan(f, 'c_pisah')
# 7. spektrum Ti3+ dan deret spektrokimia Cr(III)
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 2.9), gridspec_kw={'width_ratios': [1.1, 1]})
nu = np.linspace(10000, 32000, 400); A_ = np.exp(-((nu - 20300) / 3000) ** 2) + .25 * np.exp(-((nu - 17400) / 2000) ** 2)
lam = 1e7 / nu; a1.plot(lam, A_ / A_.max(), color=BIRU)
for lo, hi, c in [(380, 450, '#7a4fbf'), (450, 495, '#3b6fd6'), (495, 570, '#3fae5a'), (570, 590, '#e6d23a'), (590, 620, '#f0a030'), (620, 750, '#d9433b')]: a1.axvspan(lo, hi, color=c, alpha=.18, lw=0)
a1.axvline(493, color=TUA, ls='--', lw=.8); a1.text(500, .95, '493 nm\n20 300 cm$^{-1}$', fontsize=7.5)
a1.set_xlim(350, 800); a1.set_yticks([]); a1.set_xlabel('panjang gelombang (nm)'); a1.set_ylabel('serapan'); a1.set_title('[Ti(H$_2$O)$_6$]$^{3+}$: menyerap hijau, tampak ungu', fontsize=8.8, color=TUA); koma(a1, 'x')
L = ['Cl$^-$', 'F$^-$', 'H$_2$O', 'NH$_3$', 'en', 'CN$^-$']; v = [13600, 15200, 17400, 21550, 21900, 26600]
a2.barh(range(6), v, color=[JG, JG, BIRU, BIRU, BIRU, JGT], edgecolor=TUA); a2.set_yticks(range(6)); a2.set_yticklabels(L)
for i, vv in enumerate(v): a2.text(vv + 300, i, f'{vv:,}'.replace(',', ' '), va='center', fontsize=7.5)
a2.set_xlim(0, 31000); a2.set_xlabel('Δ$_o$ untuk [CrL$_6$] (cm$^{-1}$)'); a2.set_title('deret spektrokimia, Cr(III)', fontsize=8.8, color=TUA)
a2.xaxis.set_major_formatter(FuncFormatter(lambda v_, p: f'{v_:,.0f}'.replace(',', ' ')))
simpan(f, 'c_spektrum')
# 8. CFSE dan jari-jari ion M2+
dn = np.arange(11); hs = [0, -.4, -.8, -1.2, -.6, 0, -.4, -.8, -1.2, -.6, 0]; ls_ = [0, -.4, -.8, -1.2, -1.6, -2.0, -2.4, -1.8, -1.2, -.6, 0]; tt = [0, -.27, -.53, -.36, -.18, 0, -.27, -.53, -.36, -.18, 0]
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.0))
a1.plot(dn, hs, 'o-', color=JGT, label='oktahedral, spin tinggi'); a1.plot(dn, ls_, 's--', color=BIRU, label='oktahedral, spin rendah'); a1.plot(dn, tt, '^:', color=HIJ, label='tetrahedral ($\\frac{4}{9}$Δ$_o$)')
a1.set_xlabel('jumlah elektron d'); a1.set_ylabel('EPMK (satuan Δ$_o$)'); a1.legend(fontsize=7); a1.set_xticks(dn); koma(a1, 'y')
ion = ['Ca', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']; rr = [100, 86, 79, 80, 83, 78, 74.5, 69, 73, 74]; d_ = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2.plot(d_, rr, 'o-', color=JGT); [a2.text(x_, y_ + (-3.2 if t_ in ('Ni','Cu') else 1.2), t_ + '$^{2+}$', ha='center', fontsize=7) for x_, y_, t_ in zip(d_, rr, ion)]
a2.plot([0, 5, 10], [100, 83, 74], ':', color=ABU); a2.set_xlabel('jumlah elektron d'); a2.set_ylabel('jari-jari ion M$^{2+}$, KB 6 (pm)'); a2.set_ylim(64, 106); a2.set_xticks(range(11)); koma(a2, 'y')
a2.set_title('spin tinggi: dua lembah', fontsize=8.8, color=TUA)
simpan(f, 'c_epmk')
# 9. Irving-Williams dan efek kelat
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.0))
m_ = ['Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']; lk = [2.73, 4.28, 5.89, 7.51, 10.55, 5.71]
a1.plot(range(6), lk, 'o-', color=BIRU); a1.set_xticks(range(6)); a1.set_xticklabels([x_ + '$^{2+}$' for x_ in m_]); a1.set_ylabel('log $K_1$ (etilenadiamina)'); koma(a1, 'y')
a1.set_title('deret Irving–Williams', fontsize=8.8, color=TUA)
lab = ['[Cd(NH$_2$Me)$_4$]$^{2+}$', '[Cd(en)$_2$]$^{2+}$']; dH = [-57.3, -56.5]; mTS = [20.1, -4.2]; dG = [-37.2, -60.7]
x = np.arange(2); a2.bar(x - .25, dH, .25, color=BIRU, label='Δ$H$°'); a2.bar(x, mTS, .25, color=JG, label='−$T$Δ$S$°'); a2.bar(x + .25, dG, .25, color=JGT, label='Δ$G$°')
a2.axhline(0, color=TUA, lw=.8); a2.set_xticks(x); a2.set_xticklabels(lab, fontsize=8); a2.set_ylabel('kJ mol$^{-1}$'); a2.legend(fontsize=7.5, loc='upper right'); a2.set_ylim(-70, 45); koma(a2, 'y')
a2.set_title('efek kelat: empat N donor', fontsize=8.8, color=TUA)
simpan(f, 'd_kelat')
