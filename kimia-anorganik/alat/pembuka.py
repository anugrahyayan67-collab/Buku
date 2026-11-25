#!/usr/bin/env python3
# Gambar latar halaman pembuka bab Kimia Kuantum: awan elektron orbital hidrogen (n, l, m) di bidang xz.
# Pakai: python3 alat/pembuka.py  -> _kerja/pembuka/orbNN.png dan orbNN.txt untuk 20 bab.
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from math import comb, factorial
from numpy.polynomial import legendre as Lg
from matplotlib.colors import LinearSegmentedColormap
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
K = os.path.join(R, '_kerja', 'pembuka'); os.makedirs(K, exist_ok=True)
ORB = [(1,0,0),(2,0,0),(2,1,0),(3,0,0),(3,1,0),(3,2,0),(3,2,1),(4,0,0),(4,1,0),(4,2,0),
       (4,2,1),(4,3,0),(4,3,1),(5,0,0),(5,1,0),(5,2,0),(5,2,1),(5,3,0),(5,3,1),(5,4,0)]
HUR = 'spdfg'
def lag(k, a, x): return sum((-1) ** i * comb(k + a, k - i) * x ** i / factorial(i) for i in range(k + 1))
def plm(l, m, x):
    c = np.zeros(l + 1); c[l] = 1; d = Lg.legder(c, m) if m else c
    return (1 - x * x) ** (m / 2) * Lg.legval(x, d)
def nama(n, l, m):
    sub = {(1,0):'z',(2,0):'z²',(2,1):'xz',(3,0):'z³',(3,1):'xz²',(4,0):'z⁴'}.get((l, m), '')
    return f'{n}{HUR[l]}', sub
cm = LinearSegmentedColormap.from_list('g', [(0, (0.04, 0.10, 0.19, 0)), (0.25, (0.11, 0.46, 0.74, 0.55)), (0.6, (0.50, 0.75, 0.94, 0.85)), (1, (1, 1, 1, 1))])
W, H = 8.27, 6.6
import sys
pilih = [int(a) for a in sys.argv[1:]] or range(1, len(ORB) + 1)
for i in pilih:
    n, l, m = ORB[i - 1]
    ext = 2.4 * n * n + 4
    nx, ny = int(W * 110), int(H * 110)
    X, Z = np.meshgrid(np.linspace(-1, 1, nx) * ext * W / H * 0.62, np.linspace(1, -1, ny) * ext * 0.62)
    rot = 0.3 if i % 2 else -0.3
    x, z = np.cos(rot) * X - np.sin(rot) * Z, np.sin(rot) * X + np.cos(rot) * Z
    r = np.hypot(x, z) + 1e-9; ct = z / r; rho = 2 * r / n
    psi = rho ** l * np.exp(-rho / 2) * lag(n - l - 1, 2 * l + 1, rho) * plm(l, m, ct) * (np.sign(x) if m else 1)
    d = psi ** 2 * r ** (0.0 if n == 1 else 1.2 if l == 0 else 0.5); d /= d.max()
    f = plt.figure(figsize=(W, H), dpi=200); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off')
    ax.imshow(cm(d ** 0.6), extent=[0, W, 0, H], interpolation='bicubic')
    rng = np.random.default_rng(i); p = (d / d.sum()).ravel(); N = 60000
    k = rng.choice(p.size, N, p=p); iy, ix = np.unravel_index(k, d.shape)
    px = ix / nx * W + rng.normal(0, W / nx * .6, N); py = H - iy / ny * H + rng.normal(0, H / ny * .6, N)
    ax.scatter(px, py, s=0.45, c='white', alpha=0.5, lw=0); ax.set_xlim(0, W); ax.set_ylim(0, H)
    f.savefig(f'{K}/orb{i:02d}.png', transparent=True); plt.close(f)
    s, sub = nama(n, l, m); open(f'{K}/orb{i:02d}.txt', 'w').write(f'{s}|{sub}')
print('ok', list(pilih))
