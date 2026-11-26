#!/usr/bin/env python3
# Ilustrasi pembuka bab Kimia Anorganik 1 (gaya terang, sesuai isi bab).
# python3 edisi/pembuka2.py -> _kerja/pembuka/bNN.png, bNN.txt
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
TUA, UT, MU, EM, AB = '#4a2511', '#c2611f', '#f6c79b', '#e9b949', '#8a9a90'
WARNA = {'C': '#3b4048', 'H': '#f5f6f7', 'O': '#d2553b', 'N': '#3b6fb6'}
JARI = {'C': 0.30, 'H': 0.19, 'O': 0.30, 'N': 0.30}
W, H = 8.27, 5.0
def kanvas():
    f = plt.figure(figsize=(W, H), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect('equal'); return f, ax
def simpan(n, f, cap):
    f.savefig(f'{K}/b{n:02d}.png', transparent=True); plt.close(f); open(f'{K}/b{n:02d}.txt', 'w').write(cap)
def molekul(ax, atom, ikatan, dx, dy, s=1.0):
    P = {k: (dx + s * x, dy + s * y) for k, (e, x, y) in atom.items()}
    for a, b in ikatan: ax.plot(*zip(P[a], P[b]), color=AB, lw=5 * s, solid_capstyle='round', zorder=1)
    for k, (e, x, y) in sorted(atom.items(), key=lambda t: t[1][0] == 'H'):
        r = JARI[e] * s; X, Y = P[k]
        ax.add_patch(Circle((X, Y), r, fc=WARNA[e], ec=TUA, lw=1.0, zorder=3))
        ax.add_patch(Circle((X - 0.3 * r, Y + 0.3 * r), 0.35 * r, fc='white', ec='none', alpha=0.35, zorder=4))
    return P

# Bab 1: energi ionisasi pertama H–Kr (NIST), gigi gergaji periodik
IE = [13.598, 24.587, 5.392, 9.323, 8.298, 11.260, 14.534, 13.618, 17.423, 21.565, 5.139, 7.646, 5.986, 8.152, 10.487,
      10.360, 12.968, 15.760, 4.341, 6.113, 6.561, 6.828, 6.746, 6.767, 7.434, 7.902, 7.881, 7.640, 7.726, 9.394,
      5.999, 7.899, 9.789, 9.752, 11.814, 14.000]
SIM = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr'.split()
f, ax = kanvas()
x0, x1, y0, y1 = 0.7, 7.9, 0.75, 4.2
X = [x0 + (x1 - x0) * i / 35 for i in range(36)]; Y = [y0 + (y1 - y0) * v / 25 for v in IE]
for xa, xb, c in [(X[2] - .1, X[9] + .1, '#fcefe3'), (X[18] - .1, X[35] + .1, '#fcefe3')]:
    ax.add_patch(plt.Rectangle((xa, y0 - .05), xb - xa, y1 - y0 + .1, fc=c, ec='none', zorder=0))
ax.plot(X, Y, color=UT, lw=2.2, zorder=2)
for i, (x, y) in enumerate(zip(X, Y)):
    gas = SIM[i] in ('He', 'Ne', 'Ar', 'Kr'); alk = SIM[i] in ('Li', 'Na', 'K')
    ax.scatter(x, y, s=46 if (gas or alk) else 18, color=EM if gas else (TUA if alk else UT), zorder=3, edgecolor='white', lw=.6)
    if gas or alk: ax.text(x, y + (.17 if gas else -.25), SIM[i], ha='center', fontsize=10, fontweight='bold', color=TUA, family='Liberation Sans')
ax.plot([x0, x0], [y0, y1], color=TUA, lw=1); ax.plot([x0, x1], [y0, y0], color=TUA, lw=1)
for v in (5, 10, 15, 20, 25):
    yy = y0 + (y1 - y0) * v / 25; ax.text(x0 - .1, yy, f'{v}', ha='right', va='center', fontsize=9, color=TUA, family='Liberation Sans')
ax.text(x0 - .5, (y0 + y1) / 2, 'energi ionisasi pertama (eV)', rotation=90, ha='center', va='center', fontsize=9.5, color=TUA, family='Liberation Sans')
for z in (1, 10, 18, 36):
    ax.text(X[z - 1], y0 - .22, str(z), ha='center', fontsize=9, color=TUA, family='Liberation Sans')
ax.text((x0 + x1) / 2, y0 - .5, 'nomor atom Z', ha='center', fontsize=9.5, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'pola yang berulang', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(1, f, 'Energi ionisasi pertama unsur hidrogen sampai kripton: puncak di gas mulia, lembah di logam alkali, berulang setiap periode.')
print('ok1')

# Bab 2: CH4 tetrahedron lawan XeF4 segi empat datar (empat ikatan, bentuk berbeda)
from matplotlib.patches import Ellipse
def proj(v, th=np.deg2rad(28), ph=np.deg2rad(18)):
    x, y, z = v; X = x*np.cos(th) - y*np.sin(th); Y = (x*np.sin(th) + y*np.cos(th))*np.sin(ph) + z*np.cos(ph)
    d = (x*np.sin(th) + y*np.cos(th))*np.cos(ph) - z*np.sin(ph); return X, Y, d
def gambar(ax, cx, cy, arah, pb, warna_pusat, warna_ujung, label_pusat, s=1.15):
    items = sorted([(proj(v)[2], i, proj(v)) for i, v in enumerate(arah)], reverse=True)
    for d, i, (X, Y, _) in items:
        if i in pb:
            ang = np.degrees(np.arctan2(Y, X))
            ax.add_patch(Ellipse((cx + .55*s*X, cy + .55*s*Y), .8*s, .45*s, angle=ang, fc=MU, ec=UT, lw=1.2, alpha=.85, zorder=2 if d > 0 else 4))
        else:
            ax.plot([cx, cx + s*X], [cy, cy + s*Y], color=AB, lw=5, zorder=2 if d > 0 else 4, solid_capstyle='round')
            ax.add_patch(Circle((cx + s*X, cy + s*Y), .24*s, fc=warna_ujung, ec=TUA, lw=1, zorder=3 if d > 0 else 5))
    ax.add_patch(Circle((cx, cy), .36*s, fc=warna_pusat, ec=TUA, lw=1.2, zorder=4.5))
    ax.text(cx, cy, label_pusat, ha='center', va='center', fontsize=12, fontweight='bold', color='white', zorder=6, family='Liberation Sans')
f, ax = kanvas()
TET = [(0, 0, 1), (.943, 0, -.333), (-.471, .816, -.333), (-.471, -.816, -.333)]
OKT = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
gambar(ax, 2.2, 2.35, TET, (), '#3b4048', '#f4f6f6', 'C')
gambar(ax, 6.1, 2.35, OKT, (0, 1), UT, EM, 'Xe')
ax.text(2.2, .6, 'CH₄: empat pasangan → tetrahedron', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(6.1, .6, 'XeF₄: enam pasangan → segi empat datar', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'empat ikatan, dua bentuk', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(2, f, 'Metana dan xenon tetrafluorida sama-sama mempunyai empat ikatan, tetapi xenon juga mempunyai dua pasangan elektron bebas (elips) yang ikut menentukan bentuk.')
print('ok2')

# Bab 3: cis- dan trans-[PtCl2(NH3)2] dengan pita IR Pt–Cl (dua lawan satu)
f, ax = kanvas()
def platin(cx, cy, cl, s=.95):
    arah = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for k, (ux, uy) in enumerate(arah):
        X, Y = cx + s * ux, cy + s * uy
        ax.plot([cx, X], [cy, Y], color=AB, lw=5, solid_capstyle='round', zorder=1)
        if k in cl:
            ax.add_patch(Circle((X, Y), .3, fc='#3f9a6b', ec=TUA, lw=1, zorder=3))
            ax.text(X, Y, 'Cl', ha='center', va='center', fontsize=10, fontweight='bold', color='white', zorder=4, family='Liberation Sans')
        else:
            ax.add_patch(Circle((X, Y), .27, fc=WARNA['N'], ec=TUA, lw=1, zorder=3))
            ax.text(X, Y, 'NH₃', ha='center', va='center', fontsize=7.5, fontweight='bold', color='white', zorder=4, family='Liberation Sans')
    ax.add_patch(Circle((cx, cy), .36, fc=UT, ec=TUA, lw=1.2, zorder=4.5))
    ax.text(cx, cy, 'Pt', ha='center', va='center', fontsize=12, fontweight='bold', color='white', zorder=6, family='Liberation Sans')
def pita(cx, y0, pus):
    x = np.linspace(-1.3, 1.3, 400); T = np.ones_like(x)
    for p in pus: T -= .8 * np.exp(-((x - p) / .07) ** 2)
    ax.plot(cx + x, y0 + .7 * T, color=UT, lw=2)
    ax.plot([cx - 1.3, cx + 1.3], [y0 - .05, y0 - .05], color=TUA, lw=.8)
platin(2.2, 2.85, (0, 1)); platin(6.1, 2.85, (0, 2))
pita(2.2, .75, (-.22, .22)); pita(6.1, .75, (0,))
ax.text(2.2, .35, 'cis: dua pita Pt–Cl', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(6.1, .35, 'trans: satu pita Pt–Cl', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'rumus sama, simetri berbeda', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(3, f, 'Cisplatin (kiri) dan transplatin (kanan) mempunyai rumus yang sama. Simetrinya yang berbeda meramalkan dua pita regangan Pt–Cl di inframerah untuk isomer cis dan hanya satu untuk isomer trans.')
print('ok3')

# Bab 4: oksigen cair menempel di antara kutub magnet + dua elektron π* sejajar
from matplotlib.patches import Rectangle, FancyBboxPatch
f, ax = kanvas()
for x0, c, t in [(1.0, '#c9503c', 'U'), (3.3, '#3b6fb6', 'S')]:
    ax.add_patch(FancyBboxPatch((x0, 1.0), 1.2, 2.6, boxstyle='round,pad=0.02,rounding_size=0.12', fc=c, ec=TUA, lw=1.2))
    ax.text(x0 + .6, 3.2, t, ha='center', va='center', fontsize=16, fontweight='bold', color='white', family='Liberation Sans')
# jembatan oksigen cair (biru pucat) di celah
xs = np.linspace(2.2, 3.3, 50); top = 2.35 + .06 * np.sin(np.linspace(0, 3 * np.pi, 50)); bot = 1.85 - .05 * np.cos(np.linspace(0, 2 * np.pi, 50))
ax.fill_between(xs, bot, top, color='#a9cdf0', ec='#6a9fd0', lw=1, zorder=3)
for k in range(5): ax.add_patch(Circle((2.35 + .22 * k, 1.75 - .25 * (k % 2) - .15), .05, fc='#a9cdf0', ec='#6a9fd0', zorder=3))
ax.text(2.75, .55, 'O₂ cair tertahan magnet', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
# diagram pi*
for xc in (5.9, 7.0):
    ax.plot([xc - .35, xc + .35], [3.0, 3.0], color=TUA, lw=2.5)
    ax.annotate('', (xc, 3.45), (xc, 2.65), arrowprops=dict(arrowstyle='-|>', color=UT, lw=2, mutation_scale=16))
for xc in (5.9, 7.0):
    ax.plot([xc - .35, xc + .35], [1.6, 1.6], color=TUA, lw=2.5)
    for d, (a, b) in zip((-.09, .09), ((1.25, 2.0), (1.95, 1.2))):
        ax.annotate('', (xc + d, b), (xc + d, a), arrowprops=dict(arrowstyle='-|>', color=AB, lw=1.6, mutation_scale=12))
ax.text(7.55, 3.0, 'π*', va='center', fontsize=14, color=TUA, family='Liberation Sans')
ax.text(7.55, 1.6, 'π', va='center', fontsize=14, color=TUA, family='Liberation Sans')
ax.text(6.45, .55, 'dua elektron sejajar', ha='center', fontsize=11, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'elektron yang tidak berpasangan', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(4, f, 'Oksigen cair menggantung di antara kutub magnet karena dua elektron terakhirnya menempati dua orbital π* yang setara dengan spin sejajar, sesuatu yang tidak dapat ditunjukkan struktur Lewis.')
print('ok4')

# Bab 5: dua cara menumpuk bola (tampak samping lapisan A, B, C)
f, ax = kanvas()
def tumpuk(x0, urut, judul):
    off = {'A': 0, 'B': .5, 'C': 1.0}; warna = {'A': '#f6c79b', 'B': UT, 'C': EM}
    for k, L in enumerate(urut):
        y = 1.45 + k * .52
        for i in range(4):
            x = x0 + i * .6 + off[L] * .6 / 1.5
            ax.add_patch(Circle((x, y), .29, fc=warna[L], ec=TUA, lw=1, zorder=2 + k))
            ax.add_patch(Circle((x - .09, y + .09), .09, fc='white', ec='none', alpha=.4, zorder=2.1 + k))
        ax.text(x0 - .55, y, L, ha='center', va='center', fontsize=13, fontweight='bold', color=TUA, family='Liberation Sans')
    ax.text(x0 + 1.1, .7, judul, ha='center', fontsize=11, color=TUA, family='Liberation Sans')
tumpuk(1.3, 'ABAB', 'hcp: ABAB…'); tumpuk(5.2, 'ABCA', 'ccp: ABCABC…')
ax.text(W / 2, 4.65, 'menumpuk bola serapat mungkin', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(5, f, 'Dua cara menumpuk lapisan bola serapat mungkin. Pada hcp lapisan ketiga kembali ke posisi A; pada ccp lapisan ketiga menempati posisi baru C. Keduanya mengisi 74 % ruang.')
print('ok5')

# Bab 6: tangga energi Mg -> MgCl, MgCl2, MgCl3 (Kapustinskii)
f, ax = kanvas()
nama = ['MgCl', 'MgCl₂', 'MgCl₃']; dH = [-88, -581, 4257]
y0 = 2.5; sk = 1 / 560
ax.plot([.8, 7.6], [y0, y0], color=AB, lw=1, ls='--'); ax.text(.85, y0 + .08, 'unsur: Mg + Cl₂', fontsize=10, color=TUA, family='Liberation Sans')
for i, (nm, v) in enumerate(zip(nama, dH)):
    x = 1.9 + 2.2 * i; h = max(min(v * sk, 1.6), -1.6)
    c = MU if v > 0 else (UT if v < -300 else '#f6c79b')
    ax.add_patch(plt.Rectangle((x - .45, y0), .9, h, fc=c, ec=TUA, lw=1.2))
    ax.text(x, y0 + h + (.12 if v > 0 else -.32), f'{v:+d} kJ/mol'.replace('-', '−'), ha='center', fontsize=10, color=TUA, family='Liberation Sans')
    ax.text(x, .75, nm, ha='center', fontsize=13, fontweight='bold', color=TUA, family='Liberation Sans')
ax.text(6.3, 3.3, '(batang\nterpotong)', ha='center', fontsize=8.5, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'mengapa MgCl₂?', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(6, f, 'Entalpi pembentukan hasil perhitungan untuk tiga klorida magnesium. Kenaikan energi kisi membayar energi ionisasi kedua, tetapi tidak dapat membayar energi ionisasi ketiga.')
print('ok6')

# Bab 7: tembaga, silikon, intan sebagai pita
f, ax = kanvas()
dat = [('Cu', 'logam', 10**5.78, (0.6, 3.7), (0.6, 2.4)), ('Si', 'semikonduktor', 3e-6, None, None), ('intan', 'isolator', 1e-14, None, None)]
for i, (nm, kel, s, _, _) in enumerate(dat):
    x = 1.0 + 2.4 * i
    if nm == 'Cu':
        ax.add_patch(plt.Rectangle((x, .9), 1.3, 3.0, fc='white', ec=TUA, lw=1.4)); ax.add_patch(plt.Rectangle((x, .9), 1.3, 1.7, fc=UT, ec=TUA, lw=1.4))
    else:
        gap = .7 if nm == 'Si' else 1.9; top = .9 + (3.0 - gap) / 2
        ax.add_patch(plt.Rectangle((x, .9), 1.3, top - .9, fc=UT, ec=TUA, lw=1.4)); ax.add_patch(plt.Rectangle((x, top + gap), 1.3, 3.9 - top - gap, fc='white', ec=TUA, lw=1.4))
        ax.annotate('', (x + 1.45, top + gap), (x + 1.45, top), arrowprops=dict(arrowstyle='<->', color=EM, lw=1.4))
        ax.text(x + 1.52, top + gap / 2, '1,1 eV' if nm == 'Si' else '5,5 eV', fontsize=9, color=TUA, va='center', family='Liberation Sans')
    ax.text(x + .65, .55, f'{nm}: {kel}', ha='center', fontsize=11, fontweight='bold', color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'satu teori, tiga perilaku', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(7, f, 'Tembaga, silikon, dan intan berbeda konduktivitas sampai 10²⁰ kali karena letak tingkat Fermi terhadap pita-pita energinya: di dalam pita, di dalam celah kecil, atau di dalam celah besar.')
print('ok7')

# Bab 8: tangga kekuatan asam (H0 / pKa)
f, ax = kanvas()
skala = [('HF–SbF₅', -21), ('HSO₃F–SbF₅', -19), ('HSO₃F', -15.1), ('H₂SO₄ 100 %', -12), ('H$_3$O$^+$', -1.7), ('HF', 3.2), ('CH₃COOH', 4.8), ('NH$_4^+$', 9.3), ('H₂O', 15.7)]
x0, x1 = .9, 7.5
def X(v): return x0 + (v + 23) / (17 + 23) * (x1 - x0)
ax.add_patch(plt.Rectangle((X(-1.7), 1.55), X(15.7) - X(-1.7), .5, fc='#f6c79b', ec=TUA)); ax.text((X(-1.7) + X(15.7)) / 2, 1.8, 'jendela air', ha='center', va='center', fontsize=10, color=TUA, family='Liberation Sans')
ax.add_patch(plt.Rectangle((X(-23), 1.55), X(-12) - X(-23), .5, fc=UT, ec=TUA)); ax.text((X(-23) + X(-12)) / 2, 1.8, 'superasam', ha='center', va='center', fontsize=10, color='white', family='Liberation Sans')
ax.plot([x0, x1], [1.3, 1.3], color=TUA, lw=1.5)
for k, (nm, v) in enumerate(skala):
    ax.plot([X(v), X(v)], [1.22, 1.38], color=TUA, lw=1.2)
    ax.text(X(v), 2.35 + .38 * (k % 3), nm, ha='center', fontsize=9, color=TUA, family='Liberation Sans', rotation=0)
    ax.plot([X(v), X(v)], [2.1, 2.3 + .38 * (k % 3)], color=AB, lw=.6)
for v in (-20, -10, 0, 10):
    ax.text(X(v), .95, f'{v}'.replace('-', '−'), ha='center', fontsize=9, color=TUA, family='Liberation Sans')
ax.text((x0 + x1) / 2, .55, '← lebih asam          H₀ atau pKa          lebih basa →', ha='center', fontsize=10, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'tangga keasaman', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(8, f, 'Keasaman beberapa zat dalam satu skala. Air hanya dapat memperlihatkan keasaman di dalam jendelanya; superasam jauh lebih kuat daripada asam sulfat murni.')
print('ok8')

# Bab 9: besi galvanis lawan kaleng timah dengan goresan
f, ax = kanvas()
for x0, lap, cl, teks, rus in [(.6, 'Zn', '#b0b8c0', 'seng berkorban: besi aman', False), (4.5, 'Sn', '#d8dde2', 'besi di goresan berkarat', True)]:
    ax.add_patch(plt.Rectangle((x0, 1.2), 3.2, 1.0, fc='#6b6f75', ec=TUA, lw=1.2)); ax.text(x0 + 1.6, 1.6, 'besi', ha='center', va='center', color='white', fontsize=11, family='Liberation Sans')
    ax.add_patch(plt.Rectangle((x0, 2.2), 1.35, .35, fc=cl, ec=TUA)); ax.add_patch(plt.Rectangle((x0 + 1.85, 2.2), 1.35, .35, fc=cl, ec=TUA))
    ax.text(x0 + .67, 2.37, lap, ha='center', va='center', fontsize=10, color=TUA, family='Liberation Sans'); ax.text(x0 + 2.52, 2.37, lap, ha='center', va='center', fontsize=10, color=TUA, family='Liberation Sans')
    ax.add_patch(plt.Rectangle((x0, 2.55), 3.2, .6, fc='#cfe6f7', ec='none', alpha=.8)); ax.text(x0 + 3.1, 2.95, 'air + O₂', ha='right', fontsize=8.5, color=TUA, family='Liberation Sans')
    if rus:
        ax.add_patch(plt.Polygon([[x0 + 1.35, 2.2], [x0 + 1.85, 2.2], [x0 + 1.75, 1.85], [x0 + 1.45, 1.85]], fc=UT, ec=TUA)); ax.annotate('', (x0 + 1.6, 2.9), (x0 + 1.6, 2.25), arrowprops=dict(arrowstyle='-|>', color=UT))
    else:
        for xx in (x0 + .9, x0 + 2.3): ax.annotate('', (xx, 2.9), (xx, 2.58), arrowprops=dict(arrowstyle='-|>', color=EM))
    ax.text(x0 + 1.6, .75, teks, ha='center', fontsize=10.5, color=TUA, family='Liberation Sans')
ax.text(2.2, 3.55, 'besi galvanis', ha='center', fontsize=12, fontweight='bold', color=TUA, family='Liberation Sans'); ax.text(6.1, 3.55, 'kaleng timah', ha='center', fontsize=12, fontweight='bold', color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'siapa yang teroksidasi?', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(9, f, 'Goresan pada lapisan pelindung. Seng, yang lebih mudah teroksidasi, melindungi besi; timah, yang lebih sukar teroksidasi, justru membuat besi di goresan berkarat lebih cepat.')
print('ok9')

# Bab 10: natrium dalam air lawan dalam amonia cair
f, ax = kanvas()
for x0, isi, wl, teks, judul in [(1.0, '#cfe6f7', False, 'Na + H₂O → NaOH + ½H₂', 'air'), (5.0, '#1d3f9a', True, 'Na → Na⁺ + e⁻(am)', 'amonia cair, −33 °C')]:
    ax.add_patch(plt.Polygon([[x0, 3.6], [x0 + .25, 1.0], [x0 + 2.75, 1.0], [x0 + 3.0, 3.6]], fc='none', ec=TUA, lw=1.6))
    ax.add_patch(plt.Polygon([[x0 + .05, 3.0], [x0 + .25, 1.0], [x0 + 2.75, 1.0], [x0 + 2.95, 3.0]], fc=isi, ec='none', alpha=.85))
    ax.text(x0 + 1.5, 4.0, judul, ha='center', fontsize=12, fontweight='bold', color=TUA, family='Liberation Sans')
    ax.text(x0 + 1.5, .55, teks, ha='center', fontsize=10.5, color=TUA, family='Liberation Sans')
    if not wl:
        ax.add_patch(plt.Circle((x0 + 1.5, 3.02), .16, fc='#c8c8c8', ec=TUA))
        for k in range(9):
            ax.add_patch(plt.Circle((x0 + .8 + .18 * k, 3.25 + .25 * np.sin(k * 1.7) ** 2), .05 + .02 * (k % 3), fc='white', ec=AB, lw=.8))
        ax.text(x0 + 2.4, 3.3, 'H₂', fontsize=10, color=UT, family='Liberation Sans')
    else:
        for k in range(14):
            xx, yy = x0 + .6 + 1.8 * ((k * .37) % 1), 1.3 + 1.5 * ((k * .61) % 1)
            ax.add_patch(plt.Circle((xx, yy), .13, fc='none', ec='#9fc4ff', lw=1, ls='--')); ax.text(xx, yy, 'e⁻', ha='center', va='center', fontsize=6.5, color='white', family='Liberation Sans')
ax.text(W / 2, 4.65, 'pelarut menentukan kimianya', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(10, f, 'Natrium bereaksi hebat dengan air, tetapi larut dengan tenang dalam amonia cair menghasilkan larutan biru berisi elektron tersolvasi.')
print('ok10')

# Bab 11: oktahedron Werner dan empat warna kompleks kobalt
f, ax = kanvas()
th, ph = np.radians(30), np.radians(25)
def pj(v):
    x, y, z = v; x1 = x * np.cos(th) - y * np.sin(th); y1 = x * np.sin(th) + y * np.cos(th); return (x1, z * np.cos(ph) - y1 * np.sin(ph)), y1 * np.cos(ph) + z * np.sin(ph)
cx, cy, s = 2.4, 2.45, 1.35
L = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
it = sorted([(pj(v)[1], pj(v)[0], k) for k, v in enumerate(L)])
for d, (x, y), k in it: ax.plot([cx, cx + s * x], [cy, cy + s * y], color=AB, lw=3, zorder=2 + d)
ax.add_patch(plt.Circle((cx, cy), .32, fc=UT, ec=TUA, lw=1.5, zorder=5)); ax.text(cx, cy, 'Co', ha='center', va='center', color='white', fontsize=12, fontweight='bold', zorder=6, family='Liberation Sans')
for d, (x, y), k in it:
    c = '#3fae5a' if k in (4, 5) else '#9fc4ff'; t = 'Cl' if k in (4, 5) else 'NH₃'
    ax.add_patch(plt.Circle((cx + s * x, cy + s * y), .27, fc=c, ec=TUA, zorder=5 + 2 * d)); ax.text(cx + s * x, cy + s * y, t, ha='center', va='center', fontsize=8, zorder=5.1 + 2 * d, color=TUA, family='Liberation Sans')
for i, (w, nm) in enumerate([('#e9a21b', 'kuning'), ('#8b2c6e', 'ungu merah'), ('#2e8b3a', 'hijau'), ('#6a3f9e', 'ungu')]):
    x0 = 4.9 + (i % 2) * 1.55; y0 = 2.75 - (i // 2) * 1.55
    ax.add_patch(plt.Rectangle((x0, y0), 1.25, 1.2, fc=w, ec=TUA, lw=1.2)); ax.text(x0 + .62, y0 - .2, nm, ha='center', fontsize=9, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'satu logam, banyak warna', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(11, f, 'Ion kompleks oktahedral trans-[Co(NH₃)₄Cl₂]⁺ dan warna empat senyawa kobalt(III)–amonia yang dijelaskan oleh teori Werner.')
print('ok11')

# Bab 12: hidrogen di dalam kisi paladium dan kristal XeF2
f, ax = kanvas()
for i in range(5):
    for j in range(4):
        x, y = 1.0 + i * .75, .9 + j * .75
        ax.add_patch(plt.Circle((x, y), .27, fc='#c9cdd2', ec=TUA, lw=1.1))
        if i < 4 and j < 3 and (i + j) % 2 == 0: ax.add_patch(plt.Circle((x + .375, y + .375), .1, fc='white', ec=UT, lw=1.3, zorder=3))
ax.text(2.5, .25, 'H di rongga kisi paladium', ha='center', fontsize=10.5, color=TUA, family='Liberation Sans')
cx, cy = 6.4, 2.2
ax.plot([cx, cx], [cy - 1.2, cy + 1.2], color=AB, lw=4)
for dy in (-1.2, 1.2): ax.add_patch(plt.Circle((cx, cy + dy), .3, fc='#9fd8a8', ec=TUA, lw=1.2, zorder=4)); ax.text(cx, cy + dy, 'F', ha='center', va='center', fontsize=11, family='Liberation Sans', zorder=5)
for a in (0, 120, 240):
    r = np.radians(a); ax.add_patch(matplotlib.patches.Ellipse((cx + .55 * np.cos(r), cy + .25 * np.sin(r)), .6, .3, angle=a if a == 0 else a, fc=EM, alpha=.45, ec='none'))
ax.add_patch(plt.Circle((cx, cy), .36, fc='#5b86e5', ec=TUA, lw=1.4, zorder=5)); ax.text(cx, cy, 'Xe', ha='center', va='center', color='white', fontsize=12, fontweight='bold', zorder=6, family='Liberation Sans')
ax.text(cx, .25, 'XeF₂: gas mulia yang bereaksi', ha='center', fontsize=10.5, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'unsur pertama dan golongan terakhir', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(12, f, 'Kiri: atom hidrogen menempati rongga di antara atom paladium. Kanan: XeF₂ yang linear dengan tiga pasangan bebas di sekitar xenon.')
print('ok12')

# Bab 13: inti yang memancarkan partikel alfa, dan kurva energi ikat
f, ax = kanvas()
rng = np.random.default_rng(7); cx, cy = 2.2, 2.3
pts = []
while len(pts) < 46:
    p = rng.normal(0, .48, 2)
    if np.hypot(*p) < .95 and all(np.hypot(*(p - q)) > .17 for q in pts): pts.append(p)
for i, p in enumerate(sorted(pts, key=lambda q: q[1])):
    ax.add_patch(plt.Circle((cx + p[0], cy + p[1]), .12, fc=UT if i % 2 else '#9fb3c8', ec=TUA, lw=.7))
ax_ = 4.0; ay = 3.2
for k, (dx, dy) in enumerate([(-.09, -.09), (.09, .09), (-.09, .09), (.09, -.09)]): ax.add_patch(plt.Circle((ax_ + dx, ay + dy), .1, fc=UT if k < 2 else '#9fb3c8', ec=TUA, lw=.7))
ax.annotate('', (ax_ - .25, ay - .15), (cx + .9, cy + .5), arrowprops=dict(arrowstyle='<-', color=EM, lw=2))
ax.text(ax_ + .25, ay + .1, 'α', fontsize=14, color=TUA, family='Liberation Sans')
A = np.linspace(4, 240, 200); Z0 = (A / 2) / (1 + 0.0077 * A ** (2 / 3)); B = (15.75 * A - 17.8 * A ** (2 / 3) - 0.711 * Z0 * (Z0 - 1) / A ** (1 / 3) - 23.7 * (A - 2 * Z0) ** 2 / A) / A
X = 5.0 + A / 240 * 2.9; Y = 1.0 + (B - 5) / 4 * 2.4; ax.plot(X, Y, color=UT, lw=2.5)
ax.plot([5.0, 5.0, 7.95], [3.6, 1.0, 1.0], color=AB, lw=1); ax.text(6.45, .62, 'nomor massa', ha='center', fontsize=9, color=TUA, family='Liberation Sans'); ax.text(4.85, 2.3, 'B/A', rotation=90, ha='center', fontsize=9, color=TUA, family='Liberation Sans')
ax.text(5.0 + 56 / 240 * 2.9, 3.5, 'Fe', ha='center', fontsize=10, color=TUA, family='Liberation Sans')
ax.text(W / 2, 4.65, 'energi dari dalam inti', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(13, f, 'Kiri: inti berat memancarkan partikel alfa. Kanan: energi ikat per nukleon, yang mencapai puncak di sekitar besi.')
print('ok13')
