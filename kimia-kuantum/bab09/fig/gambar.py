#!/usr/bin/env python3
# Gambar Bab 9 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
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

# 0. Stern-Gerlach
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.6), gridspec_kw={'width_ratios': [1.7, 1]})
ax = axs[0]; ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(-2.2, 2.2)
ax.add_patch(Rectangle((0.1, -0.6), 1.2, 1.2, color=J1, alpha=.8)); ax.text(0.7, -0.95, 'tungku', ha='center', fontsize=8)
ax.plot([1.3, 4.0], [0, 0], color=B, lw=1.5)
for x0 in (2.0, 2.6): ax.plot([x0, x0], [0.12, 0.8], color=TUA, lw=2); ax.plot([x0, x0], [-0.8, -0.12], color=TUA, lw=2)
ax.text(2.3, 1.0, 'celah', ha='center', fontsize=8)
ax.add_patch(Polygon([[4.0, 0.35], [6.6, 0.35], [6.6, 1.5], [4.0, 1.5]], color=TUA))
ax.add_patch(Polygon([[4.0, 0.95], [5.3, 0.25], [6.6, 0.95]], color='white'))
ax.add_patch(Rectangle((4.0, -1.5), 2.6, 1.15, color='#5a6b85'))
ax.text(5.3, 1.75, 'N', color=TUA, ha='center', fontsize=9, weight='bold'); ax.text(5.3, -1.95, 'S', color=TUA, ha='center', fontsize=9, weight='bold')
xs = np.linspace(4.0, 8.9, 60)
for sgn in (1, -1):
    y = np.where(xs < 6.6, sgn * 0.12 * ((xs - 4.0) / 2.6) ** 2, sgn * (0.12 + 0.24 * (xs - 6.6)))
    ax.plot(xs, y, color=B, lw=1.5)
ax.plot([9.0, 9.0], [-1.6, 1.6], color='#888', lw=3); ax.text(9.0, -2.0, 'pelat', ha='center', fontsize=8)
ax.text(7.7, 1.1, r'$\partial B_z/\partial z$', fontsize=8.5)
ax = axs[1]; sp(ax); z = np.linspace(-1.5, 1.5, 400)
ax.plot(z, np.where(np.abs(z) < 1, 0.45, 0), color=J2, lw=1.3, ls='--', label='klasik')
ax.plot(z, np.exp(-((z - 0.8) / 0.12) ** 2) + np.exp(-((z + 0.8) / 0.12) ** 2), color=B, lw=1.8, label='teramati')
ax.set_xlabel('$z$ di pelat (relatif)'); ax.set_yticks([]); ax.legend(frameon=False, fontsize=8, loc='upper center'); ax.set_ylim(0, 1.4); koma(ax)
sv(f, 'c_sterngerlach.png')

# 1. dua partikel dalam kotak
x = np.linspace(0, 1, 300); X1, X2 = np.meshgrid(x, x)
p = lambda n, x: np.sqrt(2) * np.sin(n * pi * x)
D = (p(1, X1) * p(2, X2)) ** 2
S = ((p(1, X1) * p(2, X2) + p(2, X1) * p(1, X2)) / np.sqrt(2)) ** 2
A = ((p(1, X1) * p(2, X2) - p(2, X1) * p(1, X2)) / np.sqrt(2)) ** 2
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('b', ['#ffffff', MUDA, B, TUA])
f, axs = plt.subplots(1, 3, figsize=(6.8, 2.4))
for ax, Z, t in zip(axs, [D, S, A], ['dapat dibedakan', 'boson (simetris)', 'fermion (antisimetris)']):
    ax.imshow(Z, origin='lower', extent=[0, 1, 0, 1], cmap=cmap, vmin=0, vmax=max(D.max(), S.max(), A.max()))
    ax.plot([0, 1], [0, 1], color=J2, lw=1, ls='--'); ax.set_title(t, fontsize=8.5)
    ax.set_xlabel('$x_1/L$'); ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1]); koma(ax)
axs[0].set_ylabel('$x_2/L$'); sv(f, 'c_identik.png')

# 2. penetrasi: distribusi radial hidrogen n = 3
r = np.linspace(0, 25, 800)
R30 = 2 / np.sqrt(27) * (1 - 2 * r / 3 + 2 * r * r / 27) * np.exp(-r / 3)
R31 = 8 / (27 * np.sqrt(6)) * r * (1 - r / 6) * np.exp(-r / 3)
R32 = 4 / (81 * np.sqrt(30)) * r * r * np.exp(-r / 3)
f, ax = plt.subplots(figsize=(5.2, 2.9)); sp(ax)
ax.axvspan(0, 2.0, color=J1, alpha=.18, lw=0); ax.text(1.0, 0.115, 'kulit\ndalam', ha='center', fontsize=7.5, color=J2)
for R, cl, t in [(R30, B, '3s'), (R31, H, '3p'), (R32, J2, '3d')]: ax.plot(r, r * r * R * R, color=cl, lw=1.6, label=t)
ax.set_xlabel('$r$ ($a_0$)'); ax.set_ylabel('$r^2R^2$'); ax.legend(frameon=False, fontsize=8); ax.set_xlim(0, 25); ax.set_ylim(0, 0.13); koma(ax)
ins = ax.inset_axes([0.55, 0.32, 0.28, 0.4])
for R, cl in [(R30, B), (R31, H), (R32, J2)]: ins.plot(r, r * r * R * R, color=cl, lw=1.2)
ins.set_xlim(0, 4); ins.set_ylim(0, 0.03); ins.tick_params(labelsize=6); koma(ins); ins.set_title('dekat inti', fontsize=6.5)
sv(f, 'c_penetrasi.png')

# 3. energi ionisasi Z = 1..36
IE = [13.598, 24.587, 5.392, 9.323, 8.298, 11.260, 14.534, 13.618, 17.423, 21.565, 5.139, 7.646, 5.986, 8.152, 10.487, 10.360,
      12.968, 15.760, 4.341, 6.113, 6.561, 6.828, 6.746, 6.767, 7.434, 7.902, 7.881, 7.640, 7.726, 9.394, 5.999, 7.900, 9.789,
      9.752, 11.814, 13.999]
sym = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr'.split()
Z = np.arange(1, 37)
f, ax = plt.subplots(figsize=(6.6, 2.9)); sp(ax)
ax.plot(Z, IE, color=B, lw=1.2, marker='o', ms=3)
for z_ in (2, 10, 18, 36): ax.text(z_, IE[z_ - 1] + 0.8, sym[z_ - 1], ha='center', fontsize=8, color=TUA)
for z_ in (3, 11, 19): ax.text(z_, IE[z_ - 1] - 2.2, sym[z_ - 1], ha='center', fontsize=8, color=J2)
for z_ in (5, 8, 13, 16, 31): ax.text(z_ + 0.2, IE[z_ - 1] - 1.6, sym[z_ - 1], ha='center', fontsize=7, color=H)
for z_ in (2.5, 10.5, 18.5): ax.axvline(z_, color='#ccc', lw=.6, ls=':')
ax.axvspan(20.5, 30.5, color=MUDA, alpha=.2, lw=0); ax.text(25.5, 16, 'logam transisi 3d', ha='center', fontsize=7.5, color=B)
ax.set_xlabel('nomor atom $Z$'); ax.set_ylabel('energi ionisasi (eV)'); ax.set_xlim(0, 37); ax.set_ylim(0, 27); koma(ax)
sv(f, 'c_ionisasi.png')

# 4. energi korelasi
nm = ['He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']; Ne_ = np.arange(2, 11)
ec = [42.04, 45.33, 94.33, 124.85, 156.38, 188.27, 257.90, 324.55, 390.50]
f, ax = plt.subplots(figsize=(5.0, 2.9)); sp(ax)
ax.bar(Ne_, ec, color=[B if n_ < 8 else J2 for n_ in Ne_], width=0.6)
for n_, e_, t in zip(Ne_, ec, nm): ax.text(n_, e_ + 6, t, ha='center', fontsize=8)
ax.set_xlabel('jumlah elektron'); ax.set_ylabel('$-E_\\mathrm{kor}$ (m$E_h$)'); ax.set_ylim(0, 430); koma(ax)
ax.text(2.0, 380, 'jingga: elektron 2p mulai berpasangan', color=J2, fontsize=7.5, ha='left')
sv(f, 'c_korelasi.png')

# 5. karbon 2p2
f, axs = plt.subplots(1, 2, figsize=(5.8, 3.2), gridspec_kw={'width_ratios': [2.2, 1]})
ax = axs[0]; ax.axis('off'); ax.set_xlim(0, 4.2); ax.set_ylim(-1500, 27000)
F2 = 1694.0; ramal = {'$^3$P': 0, '$^1$D': 6 * F2, '$^1$S': 15 * F2}; ukur = {'$^3$P': 29.6, '$^1$D': 10192.6, '$^1$S': 21648.0}
for k, cl in zip(ramal, [B, H, J2]):
    ax.plot([0.3, 1.3], [ramal[k]] * 2, color=cl, lw=2); ax.plot([2.4, 3.4], [ukur[k]] * 2, color=cl, lw=2)
    ax.plot([1.3, 2.4], [ramal[k], ukur[k]], color='#bbb', lw=.6)
    ax.text(3.5, ukur[k], k, va='center', fontsize=9)
    ax.text(0.2, ramal[k], f'{ramal[k]:.0f}'.replace('.', ','), ha='right', va='center', fontsize=7)
    ax.text(2.3, ukur[k] + 700, f'{ukur[k]:.0f}' + (' (pusat berat)' if ukur[k] < 100 else ''), ha='right', va='center', fontsize=7)
ax.text(0.8, 26500, 'satu konfigurasi', ha='center', fontsize=8); ax.text(2.9, 26500, 'terukur', ha='center', fontsize=8)
ax.text(0.8, -1300, '(cm$^{-1}$)', ha='center', fontsize=7)
ax = axs[1]; ax.axis('off'); ax.set_xlim(0, 2); ax.set_ylim(-5, 50)
for J_, e_ in [(0, 0), (1, 16.4), (2, 43.4)]:
    ax.plot([0.2, 1.0], [e_, e_], color=B, lw=2); ax.text(1.1, e_, f'$^3P_{J_}$  ' + f'{e_:g}'.replace('.', ','), va='center', fontsize=8)
ax.text(0.6, 48, '$^3$P (cm$^{-1}$)', ha='center', fontsize=8)
sv(f, 'c_karbon.png')

# 6. spin-orbit terhadap Z
f, ax = plt.subplots(figsize=(5.0, 3.0)); sp(ax)
alk = [(3, 0.3354, 'Li'), (11, 17.196, 'Na'), (19, 57.71, 'K'), (37, 237.60, 'Rb'), (55, 554.04, 'Cs')]
hal = [(9, 404.1, 'F'), (17, 882.35, 'Cl'), (35, 3685.24, 'Br'), (53, 7603.15, 'I')]
for data, cl, lab in [(alk, B, 'alkali, $np$ tereksitasi'), (hal, J2, 'halogen, $^2$P dasar')]:
    zz = [d[0] for d in data]; vv = [d[1] for d in data]
    ax.loglog(zz, vv, 'o-', color=cl, lw=1.2, ms=4, label=lab)
    for z_, v_, t in data: ax.text(z_ * 1.06, v_ * 0.7, t, fontsize=7.5, color=cl)
zg = np.array([5, 60]); ax.loglog(zg, 0.25 * zg ** 2, color='#aaa', lw=.8, ls=':'); ax.text(40, 0.25 * 40 ** 2 * 1.3, '$\\propto Z^2$', fontsize=8, color='#888')
ax.set_xlabel('nomor atom $Z$'); ax.set_ylabel('pemecahan (cm$^{-1}$)'); ax.legend(frameon=False, fontsize=7.5, loc='lower right')
from matplotlib.ticker import NullFormatter, FixedLocator
ax.xaxis.set_major_locator(FixedLocator([3, 5, 10, 20, 50])); ax.xaxis.set_minor_formatter(NullFormatter())
for axis in (ax.xaxis, ax.yaxis): axis.set_major_formatter(FuncFormatter(lambda x, p: ('%g' % x).replace('.', ',')))
sv(f, 'c_spinorbit.png')
print('selesai')
