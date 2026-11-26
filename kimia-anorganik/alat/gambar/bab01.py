#!/usr/bin/env python3
# Gambar Bab 1 Kimia Anorganik 1: struktur atom dan sifat periodik. -> bab01/fig/*.png
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.ticker import FuncFormatter
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab01', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.edgecolor': '#0e2748', 'axes.labelcolor': '#0e2748',
                     'xtick.color': '#0e2748', 'ytick.color': '#0e2748', 'axes.spines.top': False, 'axes.spines.right': False})
TUA, BIRU, MUDA, JG, JGT, HIJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
koma = FuncFormatter(lambda v, p: (f'{v:g}').replace('.', ','))
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
SIM = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr'.split()
IE = [13.598, 24.587, 5.392, 9.323, 8.298, 11.260, 14.534, 13.618, 17.423, 21.565, 5.139, 7.646, 5.986, 8.152, 10.487,
      10.360, 12.968, 15.760, 4.341, 6.113, 6.561, 6.828, 6.746, 6.767, 7.434, 7.902, 7.881, 7.640, 7.726, 9.394,
      5.999, 7.899, 9.789, 9.752, 11.814, 14.000]
Z = np.arange(1, 37)

# 1. Fungsi sebaran radial hidrogenik: penetrasi 2s dan 2p
r = np.linspace(0, 16, 800)
P1s = 4 * r**2 * np.exp(-2 * r)
P2s = r**2 * (2 - r)**2 * np.exp(-r) / 8
P2p = r**4 * np.exp(-r) / 24
f, ax = plt.subplots(figsize=(6.4, 3.4))
ax.plot(r, P1s, color=TUA, lw=1.6, label='1s')
ax.plot(r, P2s, color=BIRU, lw=2.2, label='2s')
ax.plot(r, P2p, color=JG, lw=2.2, label='2p')
ax.fill_between(r[r < 2], P2s[r < 2], color=MUDA, alpha=.6)
ax.annotate('puncak kecil 2s\ndi dekat inti\n(penetrasi)', xy=(0.6, 0.06), xytext=(2.6, 0.35), color=TUA, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=TUA))
ax.set_xlabel('jarak dari inti, r / a₀'); ax.set_ylabel('peluang radial P(r)'); ax.legend(frameon=False)
ax.xaxis.set_major_formatter(koma); ax.yaxis.set_major_formatter(koma); ax.set_xlim(0, 16); ax.set_ylim(0, 0.6)
simpan(f, 'a_penetrasi')

# 2. Zeff Slater elektron terluar dan Zeff dari energi ionisasi, Z = 1-18
def zs(Zn):
    if Zn == 1: return 1.0
    if Zn == 2: return 2 - 0.30
    if Zn <= 10: return Zn - (1.70 + (Zn - 3) * 0.35)
    return Zn - (2 + 6.8 + (Zn - 11) * 0.35)
zsl = [zs(z) for z in range(1, 19)]
nn = [1, 1] + [2] * 8 + [3] * 8
zie = [n * np.sqrt(IE[i] / 13.606) for i, n in enumerate(nn)]
f, ax = plt.subplots(figsize=(6.4, 3.4))
ax.plot(range(1, 19), zsl, 'o-', color=BIRU, lw=1.8, ms=5, label='aturan Slater')
ax.plot(range(1, 19), zie, 's--', color=JGT, lw=1.4, ms=4.5, label='dari energi ionisasi, $n\\sqrt{I/R}$')
for i in range(18): ax.text(i + 1 + (.38 if SIM[i] == 'Na' else 0), max(zsl[i], zie[i]) + (.05 if SIM[i] == 'Na' else .25), SIM[i], ha='center', fontsize=8, color=TUA)
ax.axvspan(2.5, 10.5, color='#edf5fc', zorder=0); ax.axvspan(10.5, 18.5, color='#fdf3ea', zorder=0)
ax.set_xlabel('nomor atom Z'); ax.set_ylabel('muatan inti efektif $Z_{ef}$'); ax.legend(frameon=False, loc='upper left')
ax.yaxis.set_major_formatter(koma); ax.set_xlim(0.5, 18.5); ax.set_ylim(0, 7.6)
simpan(f, 'a_zeff')

# 3. Urutan pengisian (aturan n + l, diagonal)
f, ax = plt.subplots(figsize=(5.2, 4.2)); ax.axis('off')
lab = 'spdf'
for n in range(1, 8):
    for l in range(0, min(n, 4)):
        ax.add_patch(FancyBboxPatch((l - .28, -n - .22), .56, .44, boxstyle='round,pad=.04', fc=['#edf5fc', '#fdf3ea', '#e8f6f0', '#f2effc'][l], ec='none', zorder=1))
        ax.text(l, -n, f'{n}{lab[l]}', ha='center', va='center', fontsize=12, color=TUA, fontweight='bold', zorder=3)
for s in range(1, 9):
    xs, ys = [], []
    for l in range(0, 4):
        n = s - l
        if n >= l + 1 and 1 <= n <= 7: xs.append(l); ys.append(-n)
    if len(xs) > 1:
        ax.annotate('', xy=(xs[-1] + .25, ys[-1] + .25), xytext=(xs[0] - .2, ys[0] - .2),
                    arrowprops=dict(arrowstyle='<-', color=JG, lw=1.4, alpha=.75), zorder=2)
ax.text(1.5, -8.2, 'ikuti panah dari atas ke bawah:\n1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d …', ha='center', fontsize=9, color=TUA)
ax.set_xlim(-0.8, 3.8); ax.set_ylim(-8.8, -0.4)
simpan(f, 'b_aufbau')

# 4. Tabel periodik dengan blok
blok = {}
pos = {}
def taruh(sym, per, gol): pos[sym] = (gol, per)
ELM = ('H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr '
       'Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu '
       'Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr '
       'Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og').split()
z = 0
def isi(per, gols, bl):
    global z
    for g in gols:
        s = ELM[z]; z += 1; pos[s] = (g, per, bl)
isi(1, [1], 's'); isi(1, [18], 's')
for per in (2, 3): isi(per, [1, 2], 's'); isi(per, range(13, 19), 'p')
for per in (4, 5): isi(per, [1, 2], 's'); isi(per, range(3, 13), 'd'); isi(per, range(13, 19), 'p')
for per in (6, 7):
    isi(per, [1, 2], 's'); isi(per, [3], 'd')
    for k in range(14):
        s = ELM[z]; z += 1; pos[s] = (4 + k, per + 2.6, 'f')
    isi(per, range(4, 13), 'd'); isi(per, range(13, 19), 'p')
WB = {'s': '#7fc0f0', 'p': '#f0a060', 'd': '#9fd8bf', 'f': '#c9b8f2'}
f, ax = plt.subplots(figsize=(7.4, 4.6)); ax.axis('off')
for s, (g, per, bl) in pos.items():
    ax.add_patch(plt.Rectangle((g - .45, -per - .45), .9, .9, fc=WB[bl], ec='white', lw=.8))
    ax.text(g, -per, s, ha='center', va='center', fontsize=6.6, color=TUA, fontweight='bold')
for bl, (x, y) in {'blok s': (1.5, .3), 'blok d': (7.5, -3.0), 'blok p': (15.5, -0.3), 'blok f': (10.5, -10.6)}.items():
    ax.text(x, y, bl, ha='center', fontsize=10, fontweight='bold', color=TUA)
for g in range(1, 19): ax.text(g, -0.4 if g in (1, 18) else (-1.4 if g in (2, 13, 14, 15, 16, 17) else -3.4), str(g), ha='center', fontsize=6.5, color='#5d6b7d')
ax.set_xlim(0.3, 18.7); ax.set_ylim(-10.9, 0.7); ax.set_aspect('equal')
simpan(f, 'b_tabel')

# 5. Jari-jari kovalen (Cordero 2008) dan deret isoelektronik
RC = [31, 28, 128, 96, 84, 76, 71, 66, 57, 58, 166, 141, 121, 111, 107, 105, 102, 106, 203, 176, 170, 160, 153, 139,
      139, 132, 126, 124, 132, 122, 122, 120, 119, 120, 120, 116]
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.3), gridspec_kw={'width_ratios': [1.6, 1]})
a1.plot(Z, RC, '-', color=BIRU, lw=1.6); a1.scatter(Z, RC, s=14, color=BIRU, zorder=3)
for i in (2, 10, 18):
    a1.scatter(Z[i], RC[i], s=40, color=JGT, zorder=4); a1.text(Z[i], RC[i] + 9, SIM[i], ha='center', fontsize=9, color=TUA)
a1.axvspan(20.5, 30.5, color='#e8f6f0', zorder=0); a1.text(25.5, 214, 'logam transisi', ha='center', fontsize=8.5, color=HIJ)
a1.set_xlabel('nomor atom Z'); a1.set_ylabel('jari-jari kovalen (pm)'); a1.set_ylim(0, 230)
ion = ['O$^{2-}$', 'F$^{-}$', 'Na$^{+}$', 'Mg$^{2+}$', 'Al$^{3+}$']; rr = [140, 133, 102, 72, 53.5]
a2.bar(range(5), rr, color=[JG, JG, BIRU, BIRU, BIRU], width=.6)
for i, v in enumerate(rr): a2.text(i, v + 4, f'{v:g}'.replace('.', ','), ha='center', fontsize=9, color=TUA)
a2.set_xticks(range(5)); a2.set_xticklabels(ion); a2.set_ylabel('jari-jari ion (pm)'); a2.set_ylim(0, 165)
a2.set_title('semua 10 elektron', fontsize=9.5, color=TUA)
simpan(f, 'b_jari')

# 6. Energi ionisasi pertama H-Kr dengan lekukan
f, ax = plt.subplots(figsize=(7.2, 3.6))
ax.plot(Z, IE, '-', color=BIRU, lw=1.6); ax.scatter(Z, IE, s=16, color=BIRU, zorder=3)
for s in ('He', 'Ne', 'Ar', 'Kr', 'Li', 'Na', 'K', 'B', 'O', 'Al', 'S', 'Zn', 'Ga'):
    i = SIM.index(s); up = s in ('He', 'Ne', 'Ar', 'Kr', 'Zn', 'O', 'S')
    ax.text(Z[i], IE[i] + (0.8 if up else -1.7), s, ha='center', fontsize=8.5, color=JGT if s in ('B', 'O', 'Al', 'S', 'Ga') else TUA,
            fontweight='bold')
ax.set_xlabel('nomor atom Z'); ax.set_ylabel('energi ionisasi pertama (eV)'); ax.set_ylim(0, 27)
ax.yaxis.set_major_formatter(koma)
simpan(f, 'c_ie')

# 7. Energi ionisasi berurutan Na, Mg, Al (skala log)
DAT = {'Na': [5.139, 47.286, 71.620], 'Mg': [7.646, 15.035, 80.144, 109.265], 'Al': [5.986, 18.829, 28.448, 119.99, 153.83]}
VAL = {'Na': 1, 'Mg': 2, 'Al': 3}
f, axs = plt.subplots(1, 3, figsize=(7.4, 3.0), sharey=True)
for ax, (e, v) in zip(axs, DAT.items()):
    c = [BIRU if k < VAL[e] else JG for k in range(len(v))]
    ax.bar(range(1, len(v) + 1), v, color=c, width=.6); ax.set_yscale('log'); ax.set_title(e, color=TUA, fontsize=11, fontweight='bold')
    for k, x in enumerate(v): ax.text(k + 1, x * 1.15, f'{x:.0f}' if x > 20 else f'{x:.1f}'.replace('.', ','), ha='center', fontsize=7.5, color=TUA)
    ax.set_xticks(range(1, len(v) + 1)); ax.set_xlabel('ionisasi ke-')
axs[0].set_ylabel('energi ionisasi (eV)'); axs[0].set_ylim(3, 400)
axs[0].yaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'))
simpan(f, 'c_iesuksesif')

# 8. Afinitas elektron H-Kr
EA = {'H': .754, 'Li': .618, 'B': .277, 'C': 1.262, 'O': 1.461, 'F': 3.401, 'Na': .548, 'Al': .433, 'Si': 1.390, 'P': .747,
      'S': 2.077, 'Cl': 3.613, 'K': .501, 'Ca': .025, 'Sc': .188, 'Ti': .079, 'V': .525, 'Cr': .666, 'Fe': .151, 'Co': .662,
      'Ni': 1.156, 'Cu': 1.235, 'Ga': .43, 'Ge': 1.233, 'As': .804, 'Se': 2.021, 'Br': 3.364}
f, ax = plt.subplots(figsize=(7.2, 3.4))
for i, s in enumerate(SIM):
    if s in EA: ax.bar(i + 1, EA[s], color=JG if s in ('F', 'Cl', 'Br', 'O', 'S', 'Se') else BIRU, width=.7)
    else: ax.scatter(i + 1, 0, marker='x', color=JGT, s=26, zorder=3)
for s in ('F', 'Cl', 'Br', 'C', 'Si', 'N', 'Be', 'Mg', 'He', 'Ne', 'Ar', 'Zn'):
    i = SIM.index(s); ax.text(i + 1, EA.get(s, 0) + .12, s, ha='center', fontsize=8.5, color=TUA, fontweight='bold')
ax.text(30.5, 2.9, '× = anion tidak stabil\n(afinitas negatif)', fontsize=8.5, color=JGT, ha='center')
ax.set_xlabel('nomor atom Z'); ax.set_ylabel('afinitas elektron (eV)'); ax.set_ylim(-0.2, 4); ax.yaxis.set_major_formatter(koma)
simpan(f, 'c_ea')

# 9. Tiga skala keelektronegatifan
EL = ['C', 'N', 'O', 'F', 'Si', 'Cl']
pa = [2.55, 3.04, 3.44, 3.98, 1.90, 3.16]
mu = [2.51, 2.87, 2.99, 4.06, 1.95, 3.27]
ar = [2.50, 3.01, 3.57, 4.10, 1.74, 2.85]
x = np.arange(len(EL)); w = .26
f, ax = plt.subplots(figsize=(6.4, 3.2))
ax.bar(x - w, pa, w, color=BIRU, label='Pauling (energi ikatan)')
ax.bar(x, [m if m else 0 for m in mu], w, color=JG, label='Mulliken (I + A), diskalakan')
ax.bar(x + w, ar, w, color=HIJ, label='Allred–Rochow ($Z_{ef}/r^2$)')
ax.set_xticks(x); ax.set_xticklabels(EL, fontsize=11); ax.set_ylabel('keelektronegatifan'); ax.set_ylim(0, 4.8)
ax.legend(frameon=False, fontsize=8.5, ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.13)); ax.yaxis.set_major_formatter(koma)
simpan(f, 'c_en')

# 10. Efek pasangan inert: I2 + I3 golongan 13
G13 = ['B', 'Al', 'Ga', 'In', 'Tl']; S23 = [25.155 + 37.931, 18.829 + 28.448, 20.515 + 30.726, 18.870 + 28.044, 20.428 + 29.852]
f, ax = plt.subplots(figsize=(5.4, 3.0))
ax.plot(range(5), S23, 'o-', color=BIRU, lw=1.8, ms=7)
for i, v in enumerate(S23): ax.text(i, v + 1.2, f'{v:.1f}'.replace('.', ','), ha='center', fontsize=9, color=TUA)
ax.set_xticks(range(5)); ax.set_xticklabels(G13, fontsize=11); ax.set_ylabel('$I_2 + I_3$ (eV)'); ax.set_ylim(40, 70)
ax.annotate('naik lagi di Ga dan Tl', xy=(4, S23[4]), xytext=(2.6, 60), fontsize=9, color=JGT, arrowprops=dict(arrowstyle='->', color=JGT))
simpan(f, 'c_inert')
