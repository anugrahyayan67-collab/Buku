#!/usr/bin/env python3
# Ilustrasi pembuka bab (gaya terang, sesuai isi bab). python3 edisi/pembuka2.py -> _kerja/pembuka/bNN.png, bNN.txt
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Polygon, Wedge, Ellipse
from numpy.polynomial import hermite as Hm
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
NI, UN, SI, EM, AB = '#1e1548', '#4a3ab0', '#1fa9b0', '#d79a2b', '#8b86a8'
CPK = {'C': '#444a55', 'H': '#f4f4f6', 'O': '#d93a2b', 'N': '#3a5bd9', 'Cl': '#3fbf4a', 'Co': '#d08aa8', 'He': '#7fd3e0'}
W, H = 8.27, 5.0
def kanvas(xl=(0, 8.27), yl=(0, 5.0)):
    f = plt.figure(figsize=(W, H), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal' if False else 'auto'); return f, ax
def bola(ax, x, y, r, c, z=3):
    ax.add_patch(Circle((x, y), r, color=c, zorder=z, ec='#2b2440', lw=0.6))
    for k in range(6):
        ax.add_patch(Circle((x - r * 0.3 * (k + 1) / 6, y + r * 0.3 * (k + 1) / 6), r * (1 - (k + 1) / 7), color='white', alpha=0.07, zorder=z, lw=0))
def ikatan(ax, p, q, z=2, lw=5, c='#9a95ad'):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=c, lw=lw, zorder=z, solid_capstyle='round')
def tabung(ax, x, y, w, h, c, z=3):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=%g' % (w / 2), fc='white', ec='#6d6890', lw=1.2, zorder=z, alpha=0.9))
    ax.add_patch(FancyBboxPatch((x + 0.04, y + 0.04), w - 0.08, h * 0.62, boxstyle='round,pad=0,rounding_size=%g' % (w / 2 - 0.04), fc=c, ec='none', zorder=z + 1, alpha=0.9))
    ax.add_patch(Rectangle((x + w * 0.18, y + 0.15), w * 0.12, h * 0.5, color='white', alpha=0.35, zorder=z + 2, lw=0))
def simpan(n, f, cap):
    f.savefig(f'{K}/b{n:02d}.png', transparent=True); plt.close(f); open(f'{K}/b{n:02d}.txt', 'w').write(cap)

# 1 benda panas dan kurva Planck
f, ax = kanvas(); lam = np.linspace(0.15, 3.0, 500)
for (T, c, x, h, lc) in [(3000, '#d9431e', 1.4, 0.45, '#d9431e'), (4500, '#f39c34', 2.9, 0.62, '#e8861f'), (6000, '#ffe9a8', 4.4, 0.8, EM), (9000, '#cfe3ff', 5.9, 1.0, UN)]:
    for k, a2 in [(1.0, .18), (0.75, .35), (0.55, 1)]: ax.add_patch(Circle((x, 4.15), 0.5 * k, color=c, alpha=a2, lw=0))
    B = 1 / lam ** 5 / (np.exp(14388 / (lam * T)) - 1); ax.plot(0.6 + lam * 2.45, 0.35 + 2.9 * h * B / B.max(), color=lc, lw=2.6)
ax.plot([0.6, 7.9], [0.35, 0.35], color=AB, lw=1)
simpan(1, f, 'Benda yang dipanaskan berubah warna dari merah ke putih kebiruan; kurva Planck menjelaskan mengapa.')
# 2 lingkaran satuan dan gelombang
f, ax = kanvas(); t = np.linspace(0, 2 * np.pi, 300); cx, cy, R = 1.9, 2.5, 1.5
ax.plot(cx + R * np.cos(t), cy + R * np.sin(t), color=UN, lw=2); ax.plot([cx - 1.8, cx + 1.8], [cy, cy], color=AB, lw=1); ax.plot([cx, cx], [cy - 1.8, cy + 1.8], color=AB, lw=1)
th = 0.9; ax.annotate('', xy=(cx + R * np.cos(th), cy + R * np.sin(th)), xytext=(cx, cy), arrowprops=dict(arrowstyle='-|>', color=NI, lw=2.5, mutation_scale=20))
ax.plot([cx + R * np.cos(th)] * 2, [cy, cy + R * np.sin(th)], color=EM, lw=2, ls='--'); ax.plot([cx, cx + R * np.cos(th)], [cy, cy], color=SI, lw=3)
x = np.linspace(4.0, 8.0, 400); ax.plot(x, cy + 1.0 * np.sin(2.2 * (x - 4) + 0), color=EM, lw=2.5); ax.plot(x, cy + 1.0 * np.cos(2.2 * (x - 4)), color=SI, lw=2.5)
for k in range(6): ax.add_patch(Circle((cx + R * np.cos(2 * np.pi * k / 6), cy + R * np.sin(2 * np.pi * k / 6)), 0.07, color=UN, zorder=4))
simpan(2, f, 'Rumus Euler menghubungkan lingkaran satuan dengan gelombang sinus dan kosinus.')
# 3 zat warna sianin dan partikel dalam kotak
f, ax = kanvas()
for i, c in enumerate(['#f2d43a', '#e8602c', '#c02a5e', '#3b59c9']): tabung(ax, 0.6 + i * 0.75, 0.5, 0.5, 3.6, c)
xs = np.linspace(4.0, 7.8, 9); ys = 2.4 + 0.35 * (-1) ** np.arange(9)
for i in range(8): ikatan(ax, (xs[i], ys[i]), (xs[i + 1], ys[i + 1]), lw=5)
for i in range(9): bola(ax, xs[i], ys[i], 0.17, CPK['N'] if i in (0, 8) else CPK['C'])
xx = np.linspace(4.0, 7.8, 300)
for n, c in [(1, UN), (3, SI)]: ax.plot(xx, 3.6 + 0.3 * n / 2 + 0.35 * np.sin(n * np.pi * (xx - 4) / 3.8), color=c, lw=2)
ax.plot([4.0, 4.0], [3.3, 4.6], color=NI, lw=3); ax.plot([7.8, 7.8], [3.3, 4.6], color=NI, lw=3)
simpan(3, f, 'Makin panjang rantai terkonjugasi zat warna, makin panjang gelombang yang diserap: elektron dalam kotak.')
# 4 percobaan celah ganda
f, ax = kanvas()
ax.add_patch(Rectangle((3.0, 0.4), 0.15, 4.2, color=NI)); ax.add_patch(Rectangle((3.0, 2.1), 0.15, 0.2, color='white')); ax.add_patch(Rectangle((3.0, 2.7), 0.15, 0.2, color='white'))
for r in np.arange(0.4, 4.6, 0.38):
    for yc in (2.2, 2.8):
        a = np.linspace(-1.1, 1.1, 100); ax.plot(3.15 + r * np.cos(a), yc + r * np.sin(a), color=SI, lw=0.8, alpha=0.5)
for r in np.arange(0.3, 2.6, 0.38): ax.plot(3.0 - r * np.ones(2), [1.4, 3.6], color=UN, lw=1, alpha=0.6)
y = np.linspace(0.4, 4.6, 400); I = np.cos(9 * (y - 2.5)) ** 2 * np.exp(-((y - 2.5) / 1.4) ** 2)
ax.add_patch(Rectangle((7.3, 0.4), 0.12, 4.2, color='#d9d4ef')); ax.fill_betweenx(y, 7.42, 7.42 + 0.7 * I, color=UN, alpha=0.85)
simpan(4, f, 'Pola interferensi celah ganda: elektron tunggal pun berperilaku sebagai gelombang yang hanya diramalkan peluangnya.')
# 5 HCl berpegas dan spektrum IR
f, ax = kanvas(); xs = np.linspace(1.3, 3.6, 300); ax.plot(xs, 3.4 + 0.18 * np.sin(2 * np.pi * 7 * (xs - 1.3) / 2.3), color=AB, lw=2.5)
bola(ax, 1.0, 3.4, 0.42, CPK['H']); bola(ax, 4.1, 3.4, 0.62, CPK['Cl'])
nu = np.linspace(2600, 3100, 800); y = np.zeros_like(nu)
for J in range(1, 9):
    for s in (+1, -1): y += np.exp(-J * (J + 1) / 30) * J * np.exp(-((nu - (2886 + s * 21 * J)) / 2.5) ** 2)
ax.plot(5.0 + (nu - 2600) / 500 * 3.0, 0.6 + 2.6 * (1 - 0.4 * y / y.max()) - 1.0, color=UN, lw=1.4)
simpan(5, f, 'Molekul HCl bergetar seperti dua bola berpegas; spektrum inframerahnya membuka tingkat energi getaran.')
# 6 rotor CO dan spektrum gelombang mikro
f, ax = kanvas(); ikatan(ax, (1.4, 2.7), (2.6, 3.3), lw=8); bola(ax, 1.4, 2.7, 0.45, CPK['C']); bola(ax, 2.6, 3.3, 0.42, CPK['O'])
t = np.linspace(0.3, 5.6, 200); ax.plot(2.0 + 1.7 * np.cos(t), 3.0 + 0.6 * np.sin(t), color=SI, lw=2)
ax.annotate('', xy=(2.0 + 1.7 * np.cos(5.75), 3.0 + 0.6 * np.sin(5.75)), xytext=(2.0 + 1.7 * np.cos(5.55), 3.0 + 0.6 * np.sin(5.55)), arrowprops=dict(arrowstyle='-|>', color=SI, lw=2, mutation_scale=18))
for J in range(1, 12):
    x = 4.6 + J * 0.28; h = 3.2 * (2 * J + 1) * np.exp(-J * (J + 1) / 40) / 8; ax.plot([x, x], [0.6, 0.6 + h], color=UN, lw=3)
ax.plot([4.6, 8.0], [0.6, 0.6], color=AB, lw=1)
simpan(6, f, 'Molekul CO berputar; garis-garis spektrum rotasinya berjarak sama, sidik jari bagi teleskop radio.')
# 7 spektrum garis hidrogen
f, ax = kanvas(); ax.add_patch(FancyBboxPatch((0.6, 3.5), 3.0, 0.5, boxstyle='round,pad=0,rounding_size=0.25', fc='#f6c6e8', ec='#b96aa6', lw=1.5))
for k, a in [(1, .15), (0.6, .3)]: ax.add_patch(FancyBboxPatch((0.6 - k * 0.2, 3.5 - k * 0.2), 3.0 + k * 0.4, 0.5 + k * 0.4, boxstyle='round,pad=0,rounding_size=0.4', fc='#e874c8', ec='none', alpha=a * 0.5))
ax.add_patch(Rectangle((0.6, 1.0), 7.1, 1.2, color=NI))
for lam, c in [(656.3, '#ff2a1a'), (486.1, '#28c7e8'), (434.0, '#5a3dff'), (410.2, '#8b2bd6')]:
    x = 0.6 + (lam - 380) / (700 - 380) * 7.1; ax.plot([x, x], [1.0, 2.2], color=c, lw=4)
simpan(7, f, 'Cahaya tabung lucutan hidrogen terurai menjadi empat garis Balmer, jejak tingkat energi atom hidrogen.')
# 8 pendekatan bertahap menuju energi tepat
f, ax = kanvas(); E0 = 1.0; vals = [3.9, 2.6, 1.9, 1.5, 1.3, 1.17, 1.1, 1.06]
ax.plot([0.6, 7.8], [E0, E0], color=EM, lw=2.5, ls='--')
for i, v in enumerate(vals):
    x = 1.0 + i * 0.9; ax.plot([x - 0.3, x + 0.3], [v, v], color=UN, lw=3)
    if i: ax.annotate('', xy=(x - 0.32, v), xytext=(x - 0.6, vals[i - 1]), arrowprops=dict(arrowstyle='-|>', color=SI, lw=1.4))
simpan(8, f, 'Setiap perbaikan fungsi uji menurunkan energi, tetapi tidak pernah melewati energi tepat: asas variasi.')
# 9 tabel periodik blok s, p, d, f
f, ax = kanvas(); s = 0.4; x0, y0 = 0.5, 4.3
col = {'s': '#7d6be0', 'p': SI, 'd': EM, 'f': '#e07d9d'}
def kotak(c, r, b): ax.add_patch(Rectangle((x0 + c * s, y0 - r * s), s * 0.92, s * 0.92, color=col[b], ec='white'))
kotak(0, 0, 's'); kotak(17, 0, 'p')
for r in range(1, 7):
    for c in range(2): kotak(c, r, 's')
    for c in range(12, 18):
        if r >= 1: kotak(c, r, 'p')
    if r >= 3:
        for c in range(2, 12): kotak(c, r, 'd')
for r in (8, 9):
    for c in range(3, 17): kotak(c, r - 0.5, 'f')
simpan(9, f, 'Blok s, p, d, dan f tabel periodik: susunan yang lahir dari spin elektron dan asas Pauli.')
# 10 benzena dengan unsur simetri
f, ax = kanvas(); cx, cy = 4.1, 2.5; a = np.pi / 2 + np.arange(6) * np.pi / 3
for k in range(6): ax.plot([cx - 2.2 * np.cos(k * np.pi / 6), cx + 2.2 * np.cos(k * np.pi / 6)], [cy - 2.2 * np.sin(k * np.pi / 6), cy + 2.2 * np.sin(k * np.pi / 6)], color=AB, lw=1, ls='--')
C = [(cx + 1.1 * np.cos(t), cy + 1.1 * np.sin(t)) for t in a]; Hh = [(cx + 1.85 * np.cos(t), cy + 1.85 * np.sin(t)) for t in a]
for i in range(6): ikatan(ax, C[i], C[(i + 1) % 6], lw=6); ikatan(ax, C[i], Hh[i], lw=4)
for p in Hh: bola(ax, *p, 0.22, CPK['H'])
for p in C: bola(ax, *p, 0.3, CPK['C'])
t = np.linspace(0.2, 1.4, 60); ax.annotate('', xy=(cx + 2.4 * np.cos(1.45), cy + 2.4 * np.sin(1.45)), xytext=(cx + 2.4 * np.cos(1.35), cy + 2.4 * np.sin(1.35)), arrowprops=dict(arrowstyle='-|>', color=EM, lw=2)); ax.plot(cx + 2.4 * np.cos(t), cy + 2.4 * np.sin(t), color=EM, lw=2)
simpan(10, f, 'Benzena: enam bidang cermin dan sumbu putar lipat enam menentukan grup titiknya, D₆h.')
# 11 O2 dan magnet
f, ax = kanvas(); cx = 4.1
ax.add_patch(Wedge((cx, 2.6), 2.0, 180, 360, width=0.75, color='#c43a3a')); ax.add_patch(Rectangle((cx - 2.0, 2.6), 0.75, 1.7, color='#c43a3a')); ax.add_patch(Rectangle((cx + 1.25, 2.6), 0.75, 1.7, color='#c43a3a'))
ax.add_patch(Rectangle((cx - 2.0, 4.0), 0.75, 0.35, color='#c9c9d2')); ax.add_patch(Rectangle((cx + 1.25, 4.0), 0.75, 0.35, color='#c9c9d2'))
for (x, y) in [(cx - 0.55, 3.9), (cx + 0.45, 3.4), (cx - 0.3, 2.85), (cx + 0.6, 4.35)]:
    ikatan(ax, (x - 0.22, y), (x + 0.22, y), lw=7); bola(ax, x - 0.22, y, 0.24, CPK['O']); bola(ax, x + 0.22, y, 0.24, CPK['O'])
simpan(11, f, 'Oksigen tertarik magnet: dua elektron tak berpasangan di orbital antiikatan, ramalan teori orbital molekul.')
# 12 metana, air, etilena
f, ax = kanvas()
def metana(cx, cy, s=1.0):
    pts = [(0, 1.0), (-0.95, -0.35), (0.95, -0.35), (0.25, -0.6)]
    for p in pts: ikatan(ax, (cx, cy), (cx + p[0] * s, cy + p[1] * s), lw=5)
    for p in pts[:3]: bola(ax, cx + p[0] * s, cy + p[1] * s, 0.24 * s, CPK['H'])
    bola(ax, cx, cy, 0.36 * s, CPK['C']); bola(ax, cx + pts[3][0] * s, cy + pts[3][1] * s, 0.24 * s, CPK['H'], z=4)
metana(1.6, 2.6, 1.2)
ikatan(ax, (4.2, 2.6), (3.7, 2.0), lw=5); ikatan(ax, (4.2, 2.6), (4.7, 2.0), lw=5); bola(ax, 4.2, 2.6, 0.38, CPK['O']); bola(ax, 3.7, 2.0, 0.24, CPK['H']); bola(ax, 4.7, 2.0, 0.24, CPK['H'])
ikatan(ax, (6.1, 2.6), (7.0, 2.6), lw=9)
for (x, y) in [(5.6, 3.1), (5.6, 2.1), (7.5, 3.1), (7.5, 2.1)]: ikatan(ax, (6.1 if x < 6.5 else 7.0, 2.6), (x, y), lw=5); bola(ax, x, y, 0.22, CPK['H'])
bola(ax, 6.1, 2.6, 0.33, CPK['C']); bola(ax, 7.0, 2.6, 0.33, CPK['C'])
simpan(12, f, 'Metana (sp³), air (sudut 104,5°), dan etilena (sp²): bentuk molekul dijelaskan oleh hibridisasi.')
# 13 benzena, naftalena, grafena
f, ax = kanvas()
def hexa(cx, cy, r, c=NI, lw=3):
    t = np.pi / 6 + np.arange(7) * np.pi / 3; ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), color=c, lw=lw)
hexa(1.5, 2.5, 0.9); ax.add_patch(Circle((1.5, 2.5), 0.55, fill=False, ec=SI, lw=3))
hexa(3.4, 2.5, 0.8); hexa(3.4 + 1.386, 2.5, 0.8); ax.add_patch(Circle((3.4, 2.5), 0.48, fill=False, ec=SI, lw=2.5)); ax.add_patch(Circle((3.4 + 1.386, 2.5), 0.48, fill=False, ec=SI, lw=2.5))
for i in range(6):
    for j in range(6):
        hexa(6.0 + i * 0.52 + (j % 2) * 0.26, 0.9 + j * 0.45, 0.3, c=UN, lw=1.2) if 6.0 + i * 0.52 < 8.0 else None
simpan(13, f, 'Benzena, naftalena, dan grafena: elektron π yang terdelokalisasi, dari cincin aromatik sampai lembaran karbon.')
# 14 larutan kompleks berwarna dan oktahedron
f, ax = kanvas()
for i, c in enumerate(['#2f7fd9', '#f19ab8', '#1f4fa8', '#3fae5a', '#7d4fb5', '#e3a32a']): tabung(ax, 0.5 + i * 0.68, 0.4, 0.46, 3.8, c)
cx, cy = 6.4, 2.5; L = [(1.2, 0), (-1.2, 0), (0, 1.3), (0, -1.3), (0.55, 0.5), (-0.55, -0.5)]
for p in L: ikatan(ax, (cx, cy), (cx + p[0], cy + p[1]), lw=5)
for p in L[5:]: bola(ax, cx + p[0], cy + p[1], 0.26, CPK['O'], z=2)
bola(ax, cx, cy, 0.42, CPK['Co'])
for p in L[:5]: bola(ax, cx + p[0], cy + p[1], 0.26, CPK['O'], z=4)
simpan(14, f, 'Larutan kompleks logam transisi beraneka warna; ion pusatnya dikelilingi enam ligan dalam bentuk oktahedron.')
# 15 prisma dan spektrum
f, ax = kanvas(); ax.add_patch(Polygon([(2.4, 0.9), (4.4, 0.9), (3.4, 4.2)], closed=True, fc='#e6e2f7', ec=UN, lw=2))
ax.plot([0.3, 3.0], [2.2, 2.6], color='#888', lw=4)
cols = ['#ff2a1a', '#ff8c1a', '#ffe01a', '#3fcf4a', '#28a8e8', '#3a3dff', '#8b2bd6']
for i, c in enumerate(cols): ax.plot([3.8, 7.9], [2.5, 3.6 - i * 0.32], color=c, lw=3)
simpan(15, f, 'Prisma menguraikan cahaya putih menjadi spektrum; spektroskopi membaca warna yang diserap atau dipancarkan molekul.')
# 16 magnet NMR dan spektrum
f, ax = kanvas(); ax.add_patch(FancyBboxPatch((0.7, 0.6), 2.2, 3.6, boxstyle='round,pad=0,rounding_size=0.3', fc='#e3e0ee', ec='#6d6890', lw=1.5))
ax.add_patch(Ellipse((1.8, 4.2), 2.2, 0.5, fc='#f2f0f8', ec='#6d6890', lw=1.5)); ax.add_patch(Rectangle((1.7, 4.2), 0.2, 0.5, color='#9a95ad'))
x = np.linspace(3.6, 7.9, 2000)
def lor(x0, a, w=0.012): return a * w ** 2 / ((x - x0) ** 2 + w ** 2)
J = 0.06; y = sum(lor(7.2 + (k - 1) * J, a) for k, a in enumerate([1, 2, 1])) * 0.9 + sum(lor(4.4 + (k - 1.5) * J, a) for k, a in enumerate([1, 3, 3, 1])) * 0.6 + lor(5.9, 1) * 1.8
ax.plot(x, 0.7 + 1.6 * y, color=UN, lw=1.4); ax.plot([3.6, 7.9], [0.7, 0.7], color=AB, lw=1)
simpan(16, f, 'Magnet superkonduktor spektrometer NMR dan spektrum ¹H dengan pola pemecahan spin–spin.')
# 17 komputer dan molekul hasil perhitungan
f, ax = kanvas(); ax.add_patch(FancyBboxPatch((1.4, 1.2), 5.4, 3.4, boxstyle='round,pad=0,rounding_size=0.15', fc=NI, ec='#3a3360', lw=2))
ax.add_patch(Rectangle((3.6, 0.6), 1.0, 0.6, color='#b9b5cc')); ax.add_patch(Rectangle((2.8, 0.45), 2.6, 0.15, color='#b9b5cc'))
X, Y = np.meshgrid(np.linspace(1.6, 6.6, 300), np.linspace(1.4, 4.4, 200))
rho = sum(q * np.exp(-((X - a) ** 2 + (Y - b) ** 2) / (2 * s ** 2)) for a, b, q, s in [(4.1, 3.2, 8, .35), (3.3, 2.5, 1, .45), (4.9, 2.5, 1, .45)])
ax.contour(X, Y, np.log(rho + 1e-6), levels=10, colors=[SI], linewidths=0.8)
ikatan(ax, (4.1, 3.2), (3.3, 2.5), lw=4); ikatan(ax, (4.1, 3.2), (4.9, 2.5), lw=4); bola(ax, 4.1, 3.2, 0.3, CPK['O'], z=5); bola(ax, 3.3, 2.5, 0.2, CPK['H'], z=5); bola(ax, 4.9, 2.5, 0.2, CPK['H'], z=5)
simpan(17, f, 'Program kimia kuantum menghitung rapat elektron dan struktur molekul air langsung dari persamaan Schrödinger.')
print('ok')
