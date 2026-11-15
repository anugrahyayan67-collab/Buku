#!/usr/bin/env python3
# Gambar pembuka tiap bab Kimia Kuantum: ilustrasi bercahaya sesuai topik bab.
# Pakai: python3 edisi/pembuka.py -> edisi/_kerja/pembuka/bNN.png dan bNN.txt (keterangan)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from math import comb, factorial
from numpy.polynomial import legendre as Lg, hermite as Hm
from matplotlib.colors import LinearSegmentedColormap
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
SI, UN, EM, PU = '#5ce1e6', '#9d8cf0', '#f2c25b', '#ffffff'      # sian, ungu, emas, putih
W, H = 8.5, 6.4
CM = LinearSegmentedColormap.from_list('g', [(0, (0.08, 0.05, 0.2, 0)), (0.3, (0.36, 0.25, 0.75, 0.55)), (0.65, (0.36, 0.88, 0.9, 0.85)), (1, (1, 1, 1, 1))])
def kanvas(xl=(-1, 1), yl=(-0.75, 0.75)):
    f = plt.figure(figsize=(W, H), dpi=200); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(*xl); ax.set_ylim(*yl); return f, ax
def cahaya(ax, x, y, c=SI, lw=2.0):
    for k, a in [(9, .05), (5, .1), (2.5, .25), (1, 1)]: ax.plot(x, y, color=c, lw=lw * k, alpha=a, solid_capstyle='round')
def titik(ax, x, y, c=PU, s=40):
    for k, a in [(12, .05), (5, .15), (1, 1)]: ax.scatter(x, y, s=s * k, color=c, alpha=a, lw=0)
def awan(ax, d, ext):
    d = d / d.max(); ax.imshow(CM(d ** 0.55), extent=ext, interpolation='bicubic', origin='lower')
def simpan(n, f, cap):
    f.savefig(f'{K}/b{n:02d}.png', transparent=True); plt.close(f); open(f'{K}/b{n:02d}.txt', 'w').write(cap)
def lag(k, a, x): return sum((-1) ** i * comb(k + a, k - i) * x ** i / factorial(i) for i in range(k + 1))
def plm(l, m, x):
    c = np.zeros(l + 1); c[l] = 1; d = Lg.legder(c, m) if m else c
    return (1 - x * x) ** (m / 2) * Lg.legval(x, d)
def orbital(n, l, m, X, Z):
    r = np.hypot(X, Z) + 1e-9; rho = 2 * r / n
    return rho ** l * np.exp(-rho / 2) * lag(n - l - 1, 2 * l + 1, rho) * plm(l, m, Z / r) * (np.sign(X) if m else 1)

# 1 Lahirnya mekanika kuantum: kurva Planck
f, ax = kanvas((0, 3.2), (-0.15, 1.25)); lam = np.linspace(0.05, 3.2, 600)
for T, c in [(3500, UN), (4500, SI), (5800, PU)]:
    B = 1 / lam ** 5 / (np.exp(1.4388e4 / (lam * 1000 * T / 1000) / 1) - 1); B = B / (1 / 0.5 ** 5 / (np.exp(1.4388e4 / (500 * 5.8)) - 1))
    cahaya(ax, lam, B * 0.95, c)
simpan(1, f, 'Latar: radiasi benda hitam pada tiga suhu, teka-teki yang melahirkan kuantum Planck')
# 2 Matematika: e^{iθ}, akar satuan, spiral
f, ax = kanvas((-1.6, 1.6), (-1.2, 1.2)); t = np.linspace(0, 2 * np.pi, 400)
cahaya(ax, np.cos(t), np.sin(t), UN, 1.5)
for k in range(6): titik(ax, np.cos(2 * np.pi * k / 6), np.sin(2 * np.pi * k / 6), EM, 30)
tt = np.linspace(0, 6 * np.pi, 900); cahaya(ax, np.exp(-tt / 14) * np.cos(tt) * 1.45, np.exp(-tt / 14) * np.sin(tt) * 1.45, SI, 1.2)
simpan(2, f, 'Latar: bidang kompleks, lingkaran satuan, dan akar keenam dari satu')
# 3 Partikel dalam kotak
f, ax = kanvas((-0.25, 1.25), (-0.2, 5.6)); x = np.linspace(0, 1, 400)
cahaya(ax, [0, 0], [0, 5.5], PU, 2); cahaya(ax, [1, 1], [0, 5.5], PU, 2)
for n in range(1, 6): cahaya(ax, x, n - 0.3 + 0.38 * np.sin(n * np.pi * x), [UN, SI, EM, SI, UN][n - 1], 1.6)
simpan(3, f, 'Latar: lima keadaan terendah partikel dalam kotak')
# 4 Operator dan postulat: paket gelombang sebagai superposisi
f, ax = kanvas((-6, 6), (-2.4, 2.4)); x = np.linspace(-6, 6, 1200)
for i, k in enumerate(np.linspace(2.5, 4.5, 5)): cahaya(ax, x, 1.4 + 0.18 * np.cos(k * x) + i * 0.0, UN, 0.6) if False else None
wp = sum(np.exp(-((k - 3.5) / 0.6) ** 2) * np.cos(k * x) for k in np.linspace(2, 5, 30)); wp /= abs(wp).max()
for i, k in enumerate([2.6, 3.2, 3.8, 4.4]): cahaya(ax, x, 1.7 - i * 0.28 + 0.1 * np.cos(k * x), UN, 0.7)
cahaya(ax, x, -0.9 + 1.2 * wp, SI, 1.6); cahaya(ax, x, -0.9 + 1.2 * np.exp(-(x / 1.7) ** 2), EM, 0.9)
simpan(4, f, 'Latar: paket gelombang sebagai superposisi fungsi eigen momentum')
# 5 Osilator harmonik
f, ax = kanvas((-4.2, 4.2), (-0.3, 6.2)); x = np.linspace(-4.2, 4.2, 800)
cahaya(ax, x, 0.5 * x ** 2, PU, 1.3)
for n in range(6):
    c = np.zeros(n + 1); c[n] = 1; psi = Hm.hermval(x, c) * np.exp(-x ** 2 / 2); psi /= abs(psi).max()
    cahaya(ax, x, n + 0.5 + 0.4 * psi ** 2 * (1 if n % 2 == 0 else 1), [SI, UN, EM][n % 3], 1.3)
simpan(5, f, 'Latar: rapat peluang enam keadaan osilator harmonik dalam sumur parabola')
# 6 Momentum sudut: harmonik bola (penampang kutub)
f, ax = kanvas((-3.4, 3.4), (-2.6, 2.6)); th = np.linspace(0, 2 * np.pi, 600)
for (l, m, cx, cy, c) in [(1, 0, -2.2, 1.1, SI), (2, 0, 0, 1.1, UN), (3, 0, 2.2, 1.1, EM), (2, 1, -1.1, -1.2, UN), (3, 1, 1.1, -1.2, SI)]:
    rr = abs(plm(l, m, np.cos(th))); rr = 0.9 * rr / rr.max(); cahaya(ax, cx + rr * np.sin(th), cy + rr * np.cos(th), c, 1.2)
simpan(6, f, 'Latar: penampang harmonik bola |Y_ℓm| untuk ℓ = 1, 2, 3')
# 7 Atom hidrogen: awan orbital 4f
f, ax = kanvas((-1, 1), (-0.75, 0.75)); X, Z = np.meshgrid(np.linspace(-30, 30, 700), np.linspace(-22.5, 22.5, 525))
awan(ax, orbital(4, 3, 0, X, Z) ** 2, (-1, 1, -0.75, 0.75))
simpan(7, f, 'Latar: awan elektron orbital 4f atom hidrogen')
# 8 Metode pendekatan: kurva variasi helium di atas energi tepat
f, ax = kanvas((0.9, 2.6), (-3.05, -1.75)); z = np.linspace(0.9, 2.6, 400)
cahaya(ax, z, z ** 2 - 2 * 1.6875 * z, SI, 1.6); cahaya(ax, [0.9, 2.6], [-2.9037, -2.9037], EM, 1.0)
cahaya(ax, z, z ** 2 - 2 * 1.6875 * z + 0.25 * (z - 1.6875) ** 2 + 0.03, UN, 0.9); titik(ax, 1.6875, -1.6875 ** 2, PU, 50)
simpan(8, f, 'Latar: energi variasi atom helium sebagai fungsi muatan efektif, selalu di atas energi tepat')
# 9 Spin dan atom berelektron banyak: diagram Aufbau
f, ax = kanvas((-0.5, 7.5), (-0.5, 5.6))
lev = [(0, 0.3, 1, '1s'), (0, 1.3, 1, '2s'), (2, 1.8, 3, '2p'), (0, 2.8, 1, '3s'), (2, 3.2, 3, '3p'), (0, 4.0, 1, '4s'), (5, 4.4, 5, '3d')]
for x0, y, k, nm in lev:
    for j in range(k):
        xx = x0 + j * 0.85; cahaya(ax, [xx, xx + 0.6], [y, y], UN, 1.3)
        ax.annotate('', xy=(xx + 0.22, y + 0.38), xytext=(xx + 0.22, y + 0.04), arrowprops=dict(arrowstyle='-|>', color=SI, lw=2.4, mutation_scale=22))
        if y < 3.5: ax.annotate('', xy=(xx + 0.4, y + 0.04), xytext=(xx + 0.4, y + 0.38), arrowprops=dict(arrowstyle='-|>', color=EM, lw=2.4, mutation_scale=22))
simpan(9, f, 'Latar: pengisian orbital menurut asas Pauli dan aturan Hund')
# 10 Simetri: heksagon dengan bidang cermin dan sumbu C6
f, ax = kanvas((-1.6, 1.6), (-1.2, 1.2)); a = np.linspace(0, 2 * np.pi, 7)
for k in range(6): cahaya(ax, [-1.25 * np.cos(np.pi * k / 6), 1.25 * np.cos(np.pi * k / 6)], [-1.25 * np.sin(np.pi * k / 6), 1.25 * np.sin(np.pi * k / 6)], UN, 0.6)
cahaya(ax, 0.8 * np.cos(a + np.pi / 6), 0.8 * np.sin(a + np.pi / 6), SI, 1.8); titik(ax, 0.8 * np.cos(a[:6] + np.pi / 6), 0.8 * np.sin(a[:6] + np.pi / 6), PU, 40)
t = np.linspace(0.2, 1.7, 100); cahaya(ax, 1.05 * np.cos(t), 1.05 * np.sin(t), EM, 1.2)
simpan(10, f, 'Latar: heksagon benzena dengan enam bidang cermin dan sumbu putar C₆')
# 11 Molekul diatom: orbital ikatan dan antiikatan H2+
f, ax = kanvas((-1, 1), (-0.75, 0.75)); X, Y = np.meshgrid(np.linspace(-6, 6, 700), np.linspace(-4.5, 4.5, 525))
pa = np.exp(-np.hypot(X + 1.0, Y - 1.9)); pb = np.exp(-np.hypot(X - 1.0, Y - 1.9)); qa = np.exp(-np.hypot(X + 1.0, Y + 1.9)); qb = np.exp(-np.hypot(X - 1.0, Y + 1.9))
awan(ax, (pa + pb) ** 2 + 0.9 * (qa - qb) ** 2, (-1, 1, -0.75, 0.75))
simpan(11, f, 'Latar: orbital ikatan (atas) dan antiikatan (bawah) ion H₂⁺')
# 12 Hibridisasi: empat lobus sp3 (tiga miring, satu ke arah pembaca)
f, ax = kanvas((-1, 1), (-0.75, 0.75)); X, Y = np.meshgrid(np.linspace(-6, 6, 700), np.linspace(-4.5, 4.5, 525)); D = 0 * X
for ang in [90, 210, 330]:
    u = np.radians(ang); px = X * np.cos(u) + Y * np.sin(u); py = -X * np.sin(u) + Y * np.cos(u)
    D += np.exp(-((px - 2.0) / 1.25) ** 2 - (py / 0.85) ** 2) + 0.18 * np.exp(-((px + 0.7) / 0.5) ** 2 - (py / 0.45) ** 2)
D += 0.8 * np.exp(-(X ** 2 + Y ** 2) / 0.9)
awan(ax, D, (-1, 1, -0.75, 0.75))
simpan(12, f, 'Latar: lobus empat orbital hibrida sp³ karbon; lobus keempat mengarah ke pembaca')
# 13 Sistem pi: lingkaran Frost benzena
f, ax = kanvas((-2.2, 2.2), (-1.65, 1.65)); t = np.linspace(0, 2 * np.pi, 400)
cahaya(ax, 1.25 * np.cos(t), 1.25 * np.sin(t), UN, 1.0); a = np.pi / 2 + np.arange(6) * np.pi / 3 + np.pi
for k in range(6):
    y = 1.25 * np.sin(a[k]); x = 1.25 * np.cos(a[k]); cahaya(ax, [x - 0.35, x + 0.35], [y, y], SI, 1.6)
    if y < 0: titik(ax, [x - 0.1, x + 0.1], [y + 0.12, y + 0.12], EM, 18)
simpan(13, f, 'Latar: lingkaran Frost untuk tingkat energi orbital π benzena')
# 14 Senyawa koordinasi: pemecahan orbital d
f, ax = kanvas((-0.5, 8.5), (-0.5, 5.5))
for j in range(5): cahaya(ax, [0.3 + j * 0.62, 0.8 + j * 0.62], [2.5, 2.5], UN, 1.3)
for j in range(2): cahaya(ax, [5.2 + j * 0.9, 5.9 + j * 0.9], [4.0, 4.0], EM, 1.6)
for j in range(3): cahaya(ax, [4.75 + j * 0.9, 5.45 + j * 0.9], [1.4, 1.4], SI, 1.6)
for y1 in [4.0, 1.4]: cahaya(ax, [3.5, 4.6], [2.5, y1], PU, 0.4)
th = np.linspace(0, 2 * np.pi, 300); rr = abs(np.cos(2 * th)); cahaya(ax, 1.6 + 0.9 * rr * np.cos(th), 4.3 + 0.9 * rr * np.sin(th), SI, 0.8)
simpan(14, f, 'Latar: pemecahan lima orbital d dalam medan ligan oktahedral menjadi t₂g dan e_g')
# 15 Spektroskopi: kurva Morse dan transisi Franck–Condon
f, ax = kanvas((0.4, 3.6), (-0.3, 6.0)); r = np.linspace(0.55, 3.6, 500)
V0 = 4 * (1 - np.exp(-1.6 * (r - 1.2))) ** 2; V1 = 2.2 + 3 * (1 - np.exp(-1.3 * (r - 1.5))) ** 2
cahaya(ax, r, np.minimum(V0, 6.5), UN, 1.4); cahaya(ax, r, np.minimum(V1, 6.5), SI, 1.4)
for v in range(4):
    e = 0.45 + v * 0.8; rs = r[V0 <= e]; cahaya(ax, [rs.min(), rs.max()], [e, e], UN, 0.5)
    e1 = 2.2 + 0.35 + v * 0.6; rs = r[V1 <= e1]; cahaya(ax, [rs.min(), rs.max()], [e1, e1], SI, 0.5)
ax.annotate('', xy=(1.2, 3.55), xytext=(1.2, 0.45), arrowprops=dict(arrowstyle='-|>', color=EM, lw=2.5))
simpan(15, f, 'Latar: dua kurva energi potensial dan transisi vertikal Franck–Condon')
# 16 Resonansi magnetik: spektrum NMR etil
f, ax = kanvas((0.5, 4.6), (-0.1, 1.15)); x = np.linspace(0.5, 4.6, 3000)
def lor(x0, a, w=0.012): return a * w ** 2 / ((x - x0) ** 2 + w ** 2)
J = 0.06; y = sum(lor(1.25 + (k - 1) * J, a) for k, a in enumerate([1, 2, 1])) * 0.45 + sum(lor(4.1 + (k - 1.5) * J, a) for k, a in enumerate([1, 3, 3, 1])) * 0.3 + lor(2.05, 1) * 0.9
cahaya(ax, x[::-1], y, SI, 1.1)
simpan(16, f, 'Latar: spektrum ¹H NMR dengan triplet, singlet, dan kuartet')
# 17 Kimia komputasi: kontur rapat elektron molekul air
f, ax = kanvas((-1, 1), (-0.75, 0.75)); X, Y = np.meshgrid(np.linspace(-4, 4, 700), np.linspace(-3, 3, 525))
at = [(0, 0.4, 8, 0.5), (-1.45, -0.7, 1, 0.75), (1.45, -0.7, 1, 0.75)]
rho = sum(q * np.exp(-((X - a) ** 2 + (Y - b) ** 2) / (2 * s ** 2)) for a, b, q, s in at)
awan(ax, rho ** 0.5, (-1, 1, -0.75, 0.75))
ax.contour(np.linspace(-1, 1, 700), np.linspace(-0.75, 0.75, 525), np.log(rho + 1e-6), levels=12, colors=[SI], linewidths=0.6, alpha=0.6)
simpan(17, f, 'Latar: kontur rapat elektron molekul air hasil perhitungan SCF')
print('ok')
