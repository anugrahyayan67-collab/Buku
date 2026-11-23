#!/usr/bin/env python3
# Ilustrasi pembuka bab Fisika Umum (gaya terang, sesuai isi bab). -> edisi2/_kerja/pembuka/fNN.png, fNN.txt
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Polygon, Wedge, Ellipse, FancyArrowPatch, Arc
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
T, B, L, J, H, AB = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#8a97a8'
W, Hh = 8.27, 5.0
def kanvas():
    f = plt.figure(figsize=(W, Hh), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, 8.27); ax.set_ylim(0, 5.0); return f, ax
def panah(ax, a, b, c=T, lw=2.4, ms=18): ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw, shrinkA=0, shrinkB=0))
def bola(ax, x, y, r, c, z=3):
    ax.add_patch(Circle((x, y), r, color=c, zorder=z, ec='#22324a', lw=0.6))
    for k in range(6): ax.add_patch(Circle((x - r * .3 * (k + 1) / 6, y + r * .3 * (k + 1) / 6), r * (1 - (k + 1) / 7), color='white', alpha=.08, zorder=z, lw=0))
def simpan(n, f, cap): f.savefig(f'{K}/f{n:02d}.png', transparent=True); plt.close(f); open(f'{K}/f{n:02d}.txt', 'w').write(cap)
# 1 penggaris, jangka sorong, vektor
f, ax = kanvas(); ax.add_patch(Rectangle((0.6, 0.6), 7.0, 0.7, fc='#f3e3c6', ec='#b08a50', lw=1.2))
for i in range(71): x = 0.7 + i * 0.097; ax.plot([x, x], [1.3, 1.3 - (0.32 if i % 10 == 0 else 0.18 if i % 5 == 0 else 0.1)], color='#6a5330', lw=0.8)
panah(ax, (1.2, 2.0), (4.2, 4.2), B, 3); panah(ax, (4.2, 4.2), (6.8, 2.6), J, 3); panah(ax, (1.2, 2.0), (6.8, 2.6), T, 3.2)
simpan(1, f, 'Setiap besaran fisika adalah angka beserta satuannya; vektor dijumlahkan dengan aturan ujung ke pangkal.')
# 2 lintasan proyektil dengan foto stroboskop
f, ax = kanvas(); t = np.linspace(0, 1, 13); x = 0.8 + 6.6 * t; y = 0.7 + 4.0 * t * (1 - t) * 3.4 / 3.4 * 1.0 + 0
y = 0.7 + 13.0 * t * (1 - t) * 0.3
ax.plot(0.8 + 6.6 * np.linspace(0, 1, 200), 0.7 + 3.9 * np.linspace(0, 1, 200) * (1 - np.linspace(0, 1, 200)) * 1.0 * 4 / 4 * 1, color=AB, lw=1, ls='--')
for xi, yi in zip(x, 0.7 + 3.9 * t * (1 - t)): bola(ax, xi, yi, 0.16, H)
panah(ax, (0.8, 0.7), (1.8, 2.0), B); ax.plot([0.4, 7.9], [0.55, 0.55], color=AB, lw=1.2)
simpan(2, f, 'Bola yang dilempar menempuh lintasan parabola: gerak mendatar tetap, gerak tegak dipercepat gravitasi.')
# 3 balok di bidang miring dengan diagram gaya
f, ax = kanvas(); ax.add_patch(Polygon([(0.6, 0.6), (7.4, 0.6), (7.4, 4.0)], closed=True, fc='#e6eef7', ec=AB, lw=1.4))
th = np.arctan(3.4 / 6.8); sx = 4.0; sy = 0.6 + (sx - 0.6) * np.tan(th); hb = 0.45
cx, cy = sx - hb * np.sin(th), sy + hb * np.cos(th)
from matplotlib.transforms import Affine2D
bx = Rectangle((-0.55, -hb), 1.1, 2 * hb, fc=B, ec=T, lw=1.2, transform=Affine2D().rotate(th).translate(cx, cy) + ax.transData); ax.add_patch(bx)
panah(ax, (cx, cy), (cx, cy - 1.6), H); panah(ax, (cx, cy), (cx - 1.3 * np.sin(th), cy + 1.3 * np.cos(th)), T); panah(ax, (cx, cy), (cx - 1.1 * np.cos(th), cy - 1.1 * np.sin(th)), J)
simpan(3, f, 'Balok di bidang miring: berat, gaya normal, dan gesekan menentukan percepatannya menurut hukum Newton.')
# 4 lintasan roller coaster dan energi
f, ax = kanvas(); x = np.linspace(0.4, 7.9, 400); y = 1.0 + 2.6 * np.exp(-((x - 1.4) / 0.9) ** 2) + 1.2 * np.exp(-((x - 5.2) / 1.0) ** 2)
ax.plot(x, y, color=T, lw=3); ax.fill_between(x, 0.4, y, color='#e6eef7')
bola(ax, 1.4, 3.85, 0.22, H); bola(ax, 3.4, 1.25, 0.22, H)
for (xb, U, Kk) in [(6.5, 2.4, 0.4)]: ax.add_patch(Rectangle((xb, 3.0), 0.35, U * 0.6, color=B)); ax.add_patch(Rectangle((xb + 0.45, 3.0), 0.35, Kk * 0.6, color=J))
simpan(4, f, 'Di lintasan tanpa gesekan, energi potensial dan energi kinetik saling bertukar, jumlahnya tetap.')
# 5 bola biliar bertumbukan
f, ax = kanvas(); bola(ax, 2.0, 2.5, 0.42, '#f4f4f6'); panah(ax, (0.6, 2.5), (1.5, 2.5), AB)
for (x, y, c) in [(4.6, 2.5, '#d93a2b'), (5.35, 2.95, '#2b6bd9'), (5.35, 2.05, '#f2c12e'), (6.1, 3.4, '#2e9e4f'), (6.1, 2.5, '#222'), (6.1, 1.6, '#e07b2c')]: bola(ax, x, y, 0.42, c)
simpan(5, f, 'Tumbukan bola biliar: momentum total sebelum dan sesudah tumbukan selalu sama.')
# 6 gunung es / bejana tekanan
f, ax = kanvas(); ax.add_patch(Rectangle((0.4, 0.4), 7.5, 2.8, color='#cfe3f5')); ax.plot([0.4, 7.9], [3.2, 3.2], color=B, lw=2)
ax.add_patch(Polygon([(3.0, 3.2), (3.6, 4.4), (4.3, 3.9), (4.9, 3.2)], closed=True, fc='white', ec=AB, lw=1.2))
ax.add_patch(Polygon([(2.4, 3.2), (5.6, 3.2), (6.0, 1.6), (4.6, 0.7), (3.0, 0.9), (2.0, 1.8)], closed=True, fc='#eef6fc', ec=AB, lw=1.2, alpha=0.95))
for y in (2.4, 1.4): panah(ax, (6.8, y), (6.8, y + 0.6), T, 2)
simpan(6, f, 'Sembilan persepuluh gunung es tenggelam: gaya apung sama dengan berat air yang dipindahkannya.')
# 7 garis arus melewati sayap
f, ax = kanvas()
for k, y0 in enumerate(np.linspace(0.7, 4.3, 11)):
    x = np.linspace(0.3, 7.9, 300); bump = 0.55 * np.exp(-((x - 4.2) / 1.3) ** 2) * (1 if y0 > 2.5 else -0.35) * np.exp(-abs(y0 - 2.5) / 1.6)
    ax.plot(x, y0 + bump, color=B if y0 > 2.5 else L, lw=1.3)
t = np.linspace(0, np.pi, 100); ax.fill(np.r_[2.8 + 2.8 * (1 - np.cos(t)) / 2, (2.8 + 2.8 * (1 - np.cos(t)) / 2)[::-1]], np.r_[2.5 + 0.45 * np.sin(t) ** 1.2, 2.5 - 0.1 * np.sin(t)[::-1]], color=T)
simpan(7, f, 'Udara mengalir lebih cepat di atas sayap; menurut Bernoulli tekanannya lebih kecil, sehingga sayap terangkat.')
# 8 pegas dan bandul, grafik sinus
f, ax = kanvas(); ax.plot([0.5, 2.3], [4.6, 4.6], color=T, lw=3)
y = np.linspace(4.6, 2.4, 300); ax.plot(1.4 + 0.25 * np.sin(2 * np.pi * 9 * (4.6 - y) / 2.2), y, color=AB, lw=2); ax.add_patch(Rectangle((1.0, 1.6), 0.8, 0.8, color=B))
x = np.linspace(2.9, 7.9, 400); ax.plot(x, 2.5 + 1.4 * np.cos(2 * np.pi * (x - 2.9) / 2.0) * np.exp(-(x - 2.9) / 9), color=J, lw=2.5); ax.plot([2.9, 7.9], [2.5, 2.5], color=AB, lw=0.8)
simpan(8, f, 'Benda pada pegas bergetar harmonik; simpangannya terhadap waktu berbentuk gelombang kosinus.')
# 9 gelombang air / garpu tala
f, ax = kanvas(); x = np.linspace(0.4, 7.9, 600); ax.plot(x, 2.5 + 0.9 * np.sin(2 * np.pi * x / 1.5), color=B, lw=3); ax.plot(x, 2.5 - 0.9 * np.sin(2 * np.pi * x / 1.5), color=L, lw=2, ls='--')
for k in range(1, 6): ax.plot([0.4 + k * 1.5 - 0.0] * 2, [2.3, 2.7], color=T, lw=2)
simpan(9, f, 'Gelombang berdiri pada senar: simpul dan perut berjarak setengah panjang gelombang.')
# 10 termometer dan molekul gas
f, ax = kanvas(); ax.add_patch(FancyBboxPatch((0.9, 0.9), 0.5, 3.6, boxstyle='round,pad=0,rounding_size=0.25', fc='white', ec=AB, lw=1.4)); ax.add_patch(Circle((1.15, 0.9), 0.45, color=H)); ax.add_patch(Rectangle((1.03, 0.9), 0.24, 2.4, color=H))
ax.add_patch(Rectangle((2.6, 0.7), 5.0, 3.8, fc='#f2f7fc', ec=T, lw=2)); rng = np.random.default_rng(3)
for i in range(22):
    x, y = 3.0 + rng.random() * 4.2, 1.1 + rng.random() * 3.0; bola(ax, x, y, 0.13, B); a = rng.random() * 2 * np.pi; ax.plot([x, x + 0.5 * np.cos(a)], [y, y + 0.5 * np.sin(a)], color=AB, lw=1)
simpan(10, f, 'Suhu adalah ukuran energi kinetik rata-rata molekul yang bergerak acak di dalam gas.')
# 11 mesin panas: silinder dan piston, siklus pV
f, ax = kanvas(); ax.add_patch(Rectangle((0.8, 0.8), 1.6, 3.4, fc='#fde9d9', ec=T, lw=2)); ax.add_patch(Rectangle((0.8, 2.8), 1.6, 0.35, color=AB)); ax.plot([1.6, 1.6], [3.15, 4.6], color=T, lw=4)
V = np.linspace(1, 3, 100); ax.plot(3.4 + V * 1.3, 0.8 + 3.2 / V, color=H, lw=2.5); ax.plot(3.4 + V * 1.3, 0.8 + 1.6 / V, color=B, lw=2.5)
ax.plot([4.7, 4.7], [0.8 + 1.6, 0.8 + 3.2], color=T, lw=2); ax.plot([7.3, 7.3], [0.8 + 1.6 / 3, 0.8 + 3.2 / 3], color=T, lw=2)
simpan(11, f, 'Mesin kalor mengubah sebagian kalor menjadi kerja; luas siklus pada diagram p–V adalah kerjanya.')
# 12 garis medan dua muatan
f, ax = kanvas(); Y, X = np.mgrid[0:5:200j, 0:8.27:300j]
def E(q, x0, y0): r3 = ((X - x0) ** 2 + (Y - y0) ** 2 + 0.02) ** 1.5; return q * (X - x0) / r3, q * (Y - y0) / r3
e1 = E(1, 2.8, 2.5); e2 = E(-1, 5.5, 2.5); ax.streamplot(X, Y, e1[0] + e2[0], e1[1] + e2[1], color=L, density=1.3, linewidth=1, arrowsize=0.8)
bola(ax, 2.8, 2.5, 0.32, H); bola(ax, 5.5, 2.5, 0.32, B)
simpan(12, f, 'Garis medan listrik keluar dari muatan positif dan masuk ke muatan negatif.')
# 13 rangkaian listrik dengan lampu dan baterai
f, ax = kanvas(); ax.plot([1, 7.2, 7.2, 1, 1], [4.2, 4.2, 0.9, 0.9, 4.2], color=T, lw=2.5)
ax.add_patch(Rectangle((0.7, 2.1), 0.6, 0.9, fc=B, ec=T)); ax.add_patch(Circle((4.1, 4.2), 0.55, fc='#fff2b8', ec=T, lw=2))
for k, a2 in [(1.3, .15), (1.0, .25)]: ax.add_patch(Circle((4.1, 4.2), 0.55 * k + 0.2, color='#ffd34d', alpha=a2, lw=0))
x = np.linspace(3.2, 5.0, 200); ax.plot(x, 0.9 + 0.25 * np.sign(np.sin(2 * np.pi * (x - 3.2) * 3)) * (abs(np.sin(2 * np.pi * (x - 3.2) * 3)) > .02), color=T, lw=2)
for x in (2.2, 6.0): panah(ax, (x, 4.45), (x + 0.6, 4.45), J, 2)
simpan(13, f, 'Rangkaian listrik sederhana: baterai mendorong arus melalui hambatan dan menyalakan lampu.')
# 14 magnet batang dan serbuk besi
f, ax = kanvas(); ax.add_patch(Rectangle((2.8, 2.15), 1.35, 0.7, color='#c43a3a')); ax.add_patch(Rectangle((4.15, 2.15), 1.35, 0.7, color=B))
for k in np.linspace(0.3, 2.2, 8):
    t = np.linspace(0, np.pi, 100)
    for s in (1, -1): ax.plot(4.15 + 1.5 * (1 + k / 1.4) * np.cos(t) * 1.25, 2.5 + s * k * np.sin(t) * 1.15, color=AB, lw=1)
simpan(14, f, 'Serbuk besi di sekitar magnet batang membentuk garis-garis medan magnet dari kutub utara ke kutub selatan.')
# 15 atom Bohr dan foton
f, ax = kanvas(); bola(ax, 2.4, 2.5, 0.3, H)
for r, c in [(0.8, B), (1.4, B), (2.0, L)]: ax.add_patch(Circle((2.4, 2.5), r, fill=False, ec=c, lw=1.6))
bola(ax, 2.4 + 2.0 * np.cos(.6), 2.5 + 2.0 * np.sin(.6), 0.12, T); x = np.linspace(4.6, 7.9, 300); ax.plot(x, 2.5 + 0.35 * np.sin(2 * np.pi * (x - 4.6) / 0.45) * np.exp(-((x - 6.2) / 1.2) ** 2), color=J, lw=2.5)
panah(ax, (7.6, 2.5), (8.1, 2.5), J, 2)
simpan(15, f, 'Elektron yang turun ke orbit lebih dalam memancarkan satu foton: gagasan kuantum Bohr.')
print('ok')
