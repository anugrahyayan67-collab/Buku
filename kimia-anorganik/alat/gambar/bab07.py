#!/usr/bin/env python3
# Gambar Bab 7 Kimia Anorganik 1: logam, semikonduktor, dan teori pita. -> bab07/fig/*.png
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab07', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
from matplotlib.ticker import FuncFormatter
def koma(ax, sb='xy'):
    fm = FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−'))
    if 'x' in sb: ax.xaxis.set_major_formatter(fm)
    if 'y' in sb: ax.yaxis.set_major_formatter(fm)
# 1. titik leleh periode 6
el = ['Cs', 'Ba', 'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg']; tl = [28.4, 727, 920, 2233, 3017, 3422, 3186, 3033, 2446, 1768, 1064, -38.8]
f, ax = plt.subplots(figsize=(6.4, 3.0)); ax.plot(range(12), tl, 'o-', color=JGT); ax.set_xticks(range(12)); ax.set_xticklabels(el)
ax.set_ylabel('titik leleh (°C)'); koma(ax, 'y'); ax.axvspan(4.5, 5.5, color=JG, alpha=.15); ax.text(5, 3550, 'pita d setengah penuh', ha='center', fontsize=8.5, color=JGT); ax.set_ylim(-300, 3900)
simpan(f, 'a_leleh')
# 2. dari orbital ke pita: rantai Hückel
f, ax = plt.subplots(figsize=(6.6, 3.4))
Ns = [1, 2, 3, 4, 6, 10, 30]
for i, N in enumerate(Ns):
    E = [0.0] if N == 1 else 2 * np.cos(np.arange(1, N + 1) * np.pi / (N + 1))
    for e_ in E: ax.plot([i - .3, i + .3], [-e_, -e_], color=TUA, lw=1.4 if N < 30 else .8)
    ax.text(i, -2.45, f'{N}', ha='center', fontsize=9)
i = len(Ns); ax.add_patch(Rectangle((i - .3, -2), .6, 4, fc=MUDA, ec=BIRU)); ax.text(i, -2.45, '$N \\to \\infty$', ha='center', fontsize=9)
ax.text(i + .4, -1.7, 'ikatan', fontsize=8.5, color=BIRU); ax.text(i + .4, 1.6, 'antiikatan', fontsize=8.5, color=BIRU)
ax.annotate('', (i + .55, 2), (i + .55, -2), arrowprops=dict(arrowstyle='<->', color=JGT)); ax.text(i + .62, 0, 'lebar\npita 4|β|', fontsize=8, color=JGT, va='center')
ax.set_xlim(-.6, i + 1.4); ax.set_ylim(-2.7, 2.4); ax.set_xticks([]); ax.set_ylabel('energi (dalam |β|, nol = α)'); koma(ax, 'y')
ax.text((len(Ns)) / 2, 2.25, 'jumlah atom dalam rantai', ha='center', fontsize=9, color=TUA)
for s in ('top', 'right', 'bottom'): ax.spines[s].set_visible(False)
simpan(f, 'b_pita')
# 3. kerapatan keadaan dan Fermi-Dirac
kB = 8.617e-5; EF = 7.0
E = np.linspace(0, 10, 800); g = np.sqrt(E)
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.0))
a1.plot(g, E, color=TUA); a1.fill_betweenx(E, 0, g * (E <= EF), color=JG, alpha=.6); a1.axhline(EF, color=JGT, ls='--', lw=1); a1.text(.2, EF + .2, '$E_F$ ≈ 7 eV (Cu)', color=JGT, fontsize=9)
a1.set_xlabel(r'kerapatan keadaan $g(E) \propto \sqrt{E}$'); a1.set_ylabel('energi (eV)'); a1.set_xticks([]); koma(a1, 'y'); a1.set_title('pita terisi sampai tingkat Fermi', fontsize=9.5, color=TUA)
d = np.linspace(-0.6, 0.6, 500)
for T, c in [(300, BIRU), (1000, HIJ), (5000, JGT)]: a2.plot(d, 1 / (np.exp(d / (kB * T)) + 1), color=c, label=f'{T} K')
a2.plot(d, (d < 0).astype(float), color=TUA, lw=1, ls=':', label='0 K'); a2.set_xlabel('$E - E_F$ (eV)'); a2.set_ylabel('peluang terisi $f(E)$'); a2.legend(fontsize=8); koma(a2)
a2.set_title('fungsi Fermi–Dirac', fontsize=9.5, color=TUA)
simpan(f, 'b_dos')
# 4. kelas: logam, semilogam, semikonduktor, isolator
f, axs = plt.subplots(1, 4, figsize=(7.8, 3.0), sharey=True)
def pita(ax, y0, y1, isi, c_isi=JG):
    ax.add_patch(Rectangle((0, y0), 1, y1 - y0, fc='white', ec=TUA, lw=1)); ax.add_patch(Rectangle((0, y0), 1, isi - y0, fc=c_isi, ec=TUA, lw=1))
cfg = [('logam', [(0, 3, 1.8)], 1.8), ('semilogam', [(0, 1.6, 1.6), (1.4, 3, 1.4)], 1.5), ('semikonduktor\n(celah ≈ 1 eV)', [(0, 1.3, 1.3), (1.9, 3, 1.9)], 1.6), ('isolator\n(celah > 4 eV)', [(0, .8, .8), (2.4, 3, 2.4)], 1.6)]
for ax, (nm, bs, ef) in zip(axs, cfg):
    if nm == 'semilogam':
        ax.add_patch(Rectangle((0, 0), .5, 1.6, fc='white', ec=TUA)); ax.add_patch(Rectangle((0, 0), .5, ef, fc=JG, ec=TUA))
        ax.add_patch(Rectangle((.5, 1.4), .5, 1.6, fc='white', ec=TUA)); ax.add_patch(Rectangle((.5, 1.4), .5, ef - 1.4, fc=JG, ec=TUA))
    else:
        for a, b, i_ in bs: pita(ax, a, b, i_)
    ax.axhline(ef, color=JGT, ls='--', lw=1); ax.set_xlim(-.2, 1.2); ax.set_ylim(-.1, 3.2); ax.set_xticks([]); ax.set_title(nm, fontsize=9, color=TUA)
axs[0].set_ylabel('energi'); axs[0].set_yticks([]); axs[0].text(1.05, 1.85, '$E_F$', color=JGT, fontsize=9)
simpan(f, 'b_kelas')
# 5. doping: diagram pita n dan p + pembawa intrinsik vs suhu
f, (a1, a2, a3) = plt.subplots(1, 3, figsize=(8.0, 2.9), gridspec_kw={'width_ratios': [1, 1, 1.4]})
for ax, jenis in [(a1, 'n'), (a2, 'p')]:
    ax.add_patch(Rectangle((0, 0), 1, 1, fc=JG, ec=TUA)); ax.add_patch(Rectangle((0, 2.12), 1, 1, fc='white', ec=TUA))
    ax.text(.5, .5, 'pita valensi', ha='center', va='center', fontsize=8); ax.text(.5, 2.6, 'pita konduksi', ha='center', va='center', fontsize=8)
    if jenis == 'n':
        for x in np.linspace(.1, .9, 6): ax.plot([x - .04, x + .04], [2.0, 2.0], color=HIJ, lw=2)
        ax.text(.5, 1.8, 'tingkat donor (P)', ha='center', fontsize=7.5, color=HIJ)
        for x in (.25, .6): ax.add_patch(Circle((x, 2.3), .04, color=BIRU))
        ax.set_title('tipe n (Si:P)', fontsize=9.5, color=TUA)
    else:
        for x in np.linspace(.1, .9, 6): ax.plot([x - .04, x + .04], [1.1, 1.1], color=JGT, lw=2)
        ax.text(.5, 1.25, 'tingkat akseptor (B)', ha='center', fontsize=7.5, color=JGT)
        for x in (.3, .7): ax.add_patch(Circle((x, .85), .045, fc='white', ec=TUA))
        ax.set_title('tipe p (Si:B)', fontsize=9.5, color=TUA)
    ax.set_xlim(-.05, 1.05); ax.set_ylim(-.1, 3.2); ax.axis('off')
T = np.linspace(250, 600, 200)
for nm, Eg, Nc, Nv, c in [('Ge', .66, 1.04e19, 6.0e18, HIJ), ('Si', 1.12, 2.8e19, 1.04e19, BIRU), ('GaAs', 1.42, 4.7e17, 7.0e18, JGT)]:
    ni = np.sqrt(Nc * Nv) * (T / 300)**1.5 * np.exp(-Eg / (2 * kB * T)); a3.semilogy(T, ni, color=c, label=nm)
a3.set_ylim(1e3, 1e19); a3.axhline(5e16, color=ABU, ls='--', lw=1); a3.text(255, 1e17, 'doping 1 ppm P dalam Si', fontsize=7.5, color=ABU)
a3.set_xlabel('suhu (K)'); a3.set_ylabel('$n_i$ (cm$^{-3}$)'); a3.legend(fontsize=8, loc='lower right'); a3.set_title('pembawa intrinsik', fontsize=9.5, color=TUA)
simpan(f, 'c_doping')
# 6. sambungan p-n
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 2.9))
x = np.linspace(-1, 1, 300); step = 0.6 / (1 + np.exp(-x / .12))
for ax, judul, sh in [(a1, 'tanpa tegangan: pita melengkung', 1.0), (a2, 'tegangan maju: penghalang turun', .45)]:
    s = sh * step
    ax.plot(x, 2.0 - s, color=TUA); ax.plot(x, 1.0 - s, color=TUA); ax.fill_between(x, 0.4 - s, 1.0 - s, color=JG, alpha=.6)
    ax.axvline(0, color=ABU, ls=':', lw=1); ax.text(-.75, 2.15, 'p', fontsize=12, fontweight='bold'); ax.text(.65, 2.15 - .6 * sh, 'n', fontsize=12, fontweight='bold')
    ax.set_title(judul, fontsize=9.3, color=TUA); ax.axis('off'); ax.set_ylim(0, 2.5)
    ax.text(-.95, 1.95, 'pita konduksi', fontsize=7.5); ax.text(-.95, .55, 'pita valensi', fontsize=7.5)
a2.annotate('', (.35, 1.1 - .27), (.6, 1.5), arrowprops=dict(arrowstyle='-|>', color=BIRU)); a2.text(.15, 1.25, 'e$^-$ + lubang\n→ foton (LED)', fontsize=7.5, color=BIRU)
simpan(f, 'c_pn')
# 7. celah pita dan warna
f, ax = plt.subplots(figsize=(7.2, 2.6))
lam = np.linspace(380, 750, 400)
def wl2rgb(l):
    if l < 440: r, g, b = -(l - 440) / 60, 0, 1
    elif l < 490: r, g, b = 0, (l - 440) / 50, 1
    elif l < 510: r, g, b = 0, 1, -(l - 510) / 20
    elif l < 580: r, g, b = (l - 510) / 70, 1, 0
    elif l < 645: r, g, b = 1, -(l - 645) / 65, 0
    else: r, g, b = 1, 0, 0
    return (r, g, b)
for l in lam: ax.add_patch(Rectangle((1239.84 / l, 0), 0.008, 1, color=wl2rgb(l)))
mat = [('ZnS putih', 3.68), ('TiO₂ putih', 3.0), ('CdS kuning', 2.42), ('HgS merah', 2.0), ('CdSe hitam-merah', 1.74), ('GaAs hitam', 1.42), ('Si hitam', 1.12)]
for k, (nm, Eg) in enumerate(mat):
    ax.plot([Eg, Eg], [0, 1.25 + .0], color=TUA, lw=1); ax.text(Eg, 1.3 + .28 * (k % 2), nm, ha='center', fontsize=7.8, color=TUA)
ax.set_xlim(4.0, 1.0); ax.set_ylim(0, 1.95); ax.set_yticks([]); ax.set_xlabel('celah pita (eV); daerah berwarna = cahaya tampak 380–750 nm'); koma(ax, 'x')
for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
simpan(f, 'c_warna')
# 8. superkonduktor
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 2.9), gridspec_kw={'width_ratios': [1, 1.3]})
T = np.linspace(0, 10, 300); a1.plot(T, .2 + .02 * T**2, color=ABU, label='logam biasa'); a1.plot(T, np.where(T < 4.15, 0, .2 + .02 * T**2), color=JGT, lw=2, label='Hg (superkonduktor)')
a1.axvline(4.15, color=JGT, ls=':', lw=1); a1.text(4.3, 1.5, '$T_c$ = 4,15 K', color=JGT, fontsize=8.5); a1.set_xlabel('suhu (K)'); a1.set_ylabel('hambatan (sembarang)'); a1.set_yticks([]); a1.legend(fontsize=7.8, loc='upper left'); koma(a1, 'x')
nm = ['Hg\n1911', 'Nb\n1930', 'Nb₃Sn\n1954', 'Nb₃Ge\n1973', 'YBCO\n1987', 'Hg-1223\n1993', 'MgB₂\n2001']; Tc = [4.15, 9.25, 18.3, 23.2, 93, 133, 39]
a2.bar(range(7), Tc, color=[MUDA] * 4 + [JG, JG, MUDA], edgecolor=TUA); a2.axhline(77, color=BIRU, ls='--', lw=1); a2.text(-.4, 80, 'N₂ cair 77 K', color=BIRU, fontsize=8)
a2.set_xticks(range(7)); a2.set_xticklabels(nm, fontsize=6.8); a2.set_ylabel('$T_c$ (K)'); koma(a2, 'y')
simpan(f, 'c_super')
