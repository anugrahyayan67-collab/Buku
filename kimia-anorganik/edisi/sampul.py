#!/usr/bin/env python3
# Sampul depan & belakang Kimia Anorganik 1 Edisi 1 + gambar: kisi garam batu NaCl bercahaya.
import os, re, glob, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
E = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(E); K = f'{E}/_kerja'; os.makedirs(K, exist_ok=True)
JUDUL = [re.match(r'# Bab (\d+) (.*)', open(sorted(glob.glob(f'{d}/[a-z]-*.md'))[0]).readline()).groups() for d in sorted(glob.glob(f'{R}/bab[0-9][0-9]'))]
CM = LinearSegmentedColormap.from_list('g', [(0, (0.08, 0.05, 0.2, 0)), (0.35, (0.36, 0.25, 0.75, 0.5)), (0.7, (0.36, 0.88, 0.9, 0.85)), (1, (1, 1, 1, 1))])
def latar(nama, cx, cy, sk, redup=1.0, w=8.27, h=11.69):
    X, Y = np.meshgrid(np.linspace(0, w, int(w * 130)), np.linspace(h, 0, int(h * 130)))
    u, v = (X - cx) / sk, (Y - cy) / sk; psi = 0
    for k in range(3):
        a = 2 * np.pi * k / 3 + 0.2; psi = psi + np.exp(1j * 4.0 * (u * np.cos(a) + v * np.sin(a)))
    I = abs(psi) ** 2 / 9; env = np.exp(-(u ** 2 + v ** 2) / 9.0)
    d = (I ** 1.6) * env
    f = plt.figure(figsize=(w, h), dpi=200); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off')
    ax.imshow(CM(np.clip(d / d.max(), 0, 1) ** 0.6) * [1, 1, 1, redup], extent=[0, w, 0, h], interpolation='bicubic')
    t = np.linspace(0, 2 * np.pi, 7) + np.pi / 6
    for rr, al in [(2.2, .35), (3.4, .18)]:
        for k2, a2 in [(6, .05), (2.5, .2), (1, 1)]: ax.plot(cx + rr * np.cos(t), cy + rr * np.sin(t), color='#e9b949', lw=0.8 * k2, alpha=al * a2 * redup)
    ax.set_xlim(0, w); ax.set_ylim(0, h); f.savefig(f'{K}/{nama}', transparent=True); plt.close(f)
# Ilustrasi panel: kisi garam batu NaCl bercahaya (Na+ biru kobalt kecil, Cl- tembaga besar) dalam proyeksi miring,
# dengan sel satuan yang disorot dan butir cahaya di latar.
f = plt.figure(figsize=(6.7, 6.2), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off')
ax.set_xlim(-4.8, 4.8); ax.set_ylim(-4.45, 4.45); ax.set_aspect('equal')
th, ph = np.deg2rad(32), np.deg2rad(22)
def proj(x, y, z):
    X = x * np.cos(th) - y * np.sin(th); Y = (x * np.sin(th) + y * np.cos(th)) * np.sin(ph) + z * np.cos(ph)
    D = (x * np.sin(th) + y * np.cos(th)) * np.cos(ph) - z * np.sin(ph)
    return 1.25 * X, 1.25 * Y - 0.2, D
N = 3; T = []
for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            T.append((i - N / 2, j - N / 2, k - N / 2, (i + j + k) % 2))
# ikatan (garis kisi) di belakang dulu
for (x, y, z, s) in T:
    for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
        if (x + dx) <= N / 2 and (y + dy) <= N / 2 and (z + dz) <= N / 2:
            p1, p2 = proj(x, y, z), proj(x + dx, y + dy, z + dz)
            for k2, a2 in [(4, .05), (1.6, .14), (.7, .45)]:
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#f6c79b', lw=k2, alpha=a2, zorder=1)
# sel satuan disorot (kubus tengah)
c0 = -0.5
for (u, v) in [((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (0, 1, 0)), ((0, 0, 0), (0, 0, 1)), ((1, 1, 0), (1, 0, 0)), ((1, 1, 0), (0, 1, 0)), ((1, 1, 0), (1, 1, 1)),
               ((1, 0, 1), (1, 0, 0)), ((1, 0, 1), (0, 0, 1)), ((1, 0, 1), (1, 1, 1)), ((0, 1, 1), (0, 1, 0)), ((0, 1, 1), (0, 0, 1)), ((0, 1, 1), (1, 1, 1))]:
    p1 = proj(*(c0 + q for q in u)); p2 = proj(*(c0 + q for q in v))
    for k2, a2 in [(7, .06), (3, .16), (1.2, .9)]:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#e9b949', lw=k2, alpha=a2, zorder=2, solid_capstyle='round')
# ion, urut dari belakang ke depan
for (x, y, z, s) in sorted(T, key=lambda t: -proj(t[0], t[1], t[2])[2]):
    X, Y, D = proj(x, y, z); dep = 0.75 + 0.25 * (1 - (D + 3) / 6)
    if s == 0: r, c, g = 0.42, '#c2611f', '#f6c79b'   # Cl- besar
    else: r, c, g = 0.22, '#5b86e5', '#a9c1f5'        # Na+ kecil (biru kobalt)
    for k2, a2 in [(3.2, .05), (2.0, .10), (1.35, .18)]:
        ax.add_patch(plt.Circle((X, Y), r * k2 * dep, color=g, alpha=a2, lw=0, zorder=3))
    ax.add_patch(plt.Circle((X, Y), r * dep, color=c, zorder=4, ec=g, lw=0.8))
    ax.add_patch(plt.Circle((X - 0.32 * r * dep, Y + 0.32 * r * dep), 0.33 * r * dep, color='white', alpha=0.45, lw=0, zorder=5))
rng = np.random.default_rng(7)
for _ in range(50):
    x, y = rng.uniform(-4.6, 4.6), rng.uniform(-4.3, 4.3); r = rng.uniform(4, 14)
    if abs(x) < 3.6 and abs(y) < 3.4: continue
    for k, a2 in [(8, .03), (3, .1), (1, .5)]: ax.scatter(x, y, s=r * k, color='#fbe7d6', alpha=a2, lw=0)
f.savefig(f'{K}/sampul-latar.png', transparent=True); plt.close(f)
daftar = ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in JUDUL)
open(f'{K}/sampul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} body{{margin:0;font-family:Inter,sans-serif}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;color:#4a2511;background:#fffaf5}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:9mm;background:#4a2511}}
.ed{{position:absolute;top:24mm;left:22mm;font-size:9pt;letter-spacing:6px;font-weight:800;color:#b9801a}}
.pen{{position:absolute;top:24mm;right:18mm;font-size:9pt;font-weight:800;letter-spacing:6px;color:#4a2511}}
.jd{{position:absolute;top:36mm;left:20mm;font-size:54pt;font-weight:900;line-height:.88;letter-spacing:-1px;color:#4a2511}}
.jd span{{color:#c2611f}}
.sb{{position:absolute;top:77mm;left:22mm;width:130mm;font-size:13pt;line-height:1.45;color:#6b4a35;border-top:.6mm solid #d79a2b;padding-top:4mm}}
.panel{{position:absolute;left:22mm;right:18mm;top:98mm;bottom:22mm;background:radial-gradient(ellipse at 50% 60%,#7a3d17 0%,#5c2d10 55%,#3a1c0a 100%)}}
.panel img{{position:absolute;left:4%;top:5%;width:92%;height:90%;object-fit:contain}}
.ln{{position:absolute;bottom:22mm;left:22mm;width:40mm;height:.7mm;background:#d79a2b}}
.pers{{position:absolute;right:6mm;bottom:4mm;font-family:Caladea,serif;font-style:italic;font-size:13pt;color:rgba(250,222,210,.85)}}
.blk .isi{{position:absolute;top:24mm;left:22mm;right:20mm}}
.blk h2{{font-size:18pt;font-weight:900;margin:0 0 6mm 0;text-transform:uppercase;letter-spacing:1.5px;line-height:1.2;color:#4a2511}} .blk h2 span{{color:#c2611f}}
.blk p{{font-size:10.5pt;line-height:1.6;color:#3a2a1f;margin:0 0 3.5mm 0;font-family:Caladea,serif}}
.blk ul{{list-style:none;padding:0;margin:8mm 0 0 0;columns:2;column-gap:10mm;font-size:9.2pt;border-top:.5mm solid #4a2511;padding-top:5mm;color:#3a2a1f}}
.blk li{{margin:0 0 2.2mm 0;padding-left:8mm;text-indent:-8mm;break-inside:avoid}} .blk li b{{display:inline-block;width:8mm;text-indent:0;color:#b9801a}}
.tp{{position:absolute;left:22mm;right:20mm;bottom:22mm;background:#fcefe3;padding:5mm 6mm;font-family:Caladea,serif;font-size:10pt;line-height:1.55;color:#3a2a1f}}
.tp b{{font-family:Inter,sans-serif;font-size:8.5pt;letter-spacing:2px;color:#c2611f;display:block;margin-bottom:1.5mm}}
</style></head><body>
<div class="pg"><div class="bar"></div><div class="ed">EDISI PERTAMA</div><div class="pen">SEPTIAN ANUGRAH DWI PUTRA</div>
<div class="jd">KIMIA<br><span>ANORGANIK 1</span></div>
<div class="sb">Teori Dasar · dari struktur atom sampai kimia inti</div>
<div class="panel"><img src="sampul-latar.png"></div></div>
<div class="pg blk"><div class="bar"></div><div class="isi"><h2>Mengapa unsur <span>berperilaku seperti itu?</span></h2>
<p>Buku ini membahas teori dasar kimia anorganik: bagaimana inti memegang elektron, bagaimana sifat unsur berulang dalam tabel periodik, bagaimana elektron dibagi dalam ikatan, dan bagaimana ion-ion tersusun dalam kristal.</p>
<p>Setiap tren dibuka dengan data nyata, lalu dijelaskan dengan model yang paling sederhana, dan setiap model ditunjukkan juga kapan gagal. Contoh diambil dari mineral, industri, material, lingkungan, dan tubuh manusia.</p>
<p>Setiap bab ditutup dengan ringkasan, pertanyaan konsep, soal beserta jawabannya, pembahasan soal terpilih, dan bacaan lanjut. Buku ini adalah lanjutan dari <i>Kimia Kuantum</i> dan <i>Termodinamika Kimia</i>.</p>
<ul>{daftar}</ul></div>
<div class="tp"><b>TENTANG PENYUSUN</b><b style="color:#4a2511;letter-spacing:.5px;font-size:11pt">Septian Anugrah Dwi Putra</b>Mahasiswa S1 Kimia, Universitas Negeri Surabaya. Penyusun <i>Fisika Umum</i>, <i>Kimia Kuantum</i>, <i>Kimia Fisika 1</i>, dan <i>Kimia Organik 1</i>; buku ini disusun untuk mata kuliah Teori Dasar Anorganik.</div></div>
</body></html>''')
