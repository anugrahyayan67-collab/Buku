#!/usr/bin/env python3
# Sampul depan & belakang Kimia Organik 1 Edisi 1 + gambar: rumus kerangka parasetamol bercahaya dan panah lengkung mekanisme.
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
# Ilustrasi panel: rumus kerangka parasetamol bercahaya + panah lengkung (Nu menyerang C=O),
# dengan kerangka molekul samar di latar (sikloheksana, rantai zig-zag, cincin aromatik).
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch
f = plt.figure(figsize=(6.7, 6.2), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off')
ax.set_xlim(-4.8, 4.8); ax.set_ylim(-4.45, 4.45); ax.set_aspect('equal')
def neon(x, y, c, lw=1.0, al=1.0, glow='#9fd8a8'):
    for k, a2, cc in [(9, .05, glow), (5, .10, glow), (2.4, .28, glow), (1, 1, c)]:
        ax.plot(x, y, color=cc, lw=lw * k, alpha=a2 * al, solid_capstyle='round', solid_joinstyle='round')
def ikatan(p1, p2, c='#e8f7ee', lw=1.5, al=1.0, pendek=(0, 0)):
    (x1, y1), (x2, y2) = p1, p2; dx, dy = x2 - x1, y2 - y1; d = np.hypot(dx, dy)
    a1, a2 = pendek[0] / d, pendek[1] / d
    neon([x1 + a1 * dx, x2 - a2 * dx], [y1 + a1 * dy, y2 - a2 * dy], c, lw, al)
def ganda_dalam(p1, p2, pusat, lw=1.3, al=1.0):
    # garis kedua ikatan rangkap di sisi dalam cincin, sedikit lebih pendek
    (x1, y1), (x2, y2) = p1, p2; mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    vx, vy = pusat[0] - mx, pusat[1] - my; n = np.hypot(vx, vy); vx, vy = vx / n * 0.26, vy / n * 0.26
    t = 0.18; ikatan((x1 + (x2 - x1) * t + vx, y1 + (y2 - y1) * t + vy), (x2 - (x2 - x1) * t + vx, y2 - (y2 - y1) * t + vy), lw=lw, al=al)
def label(x, y, teks, c='#f6d27a', fs=27):
    ax.text(x, y, teks, color=c, fontsize=fs, fontweight='bold', family='Liberation Sans', ha='center', va='center', zorder=6,
            path_effects=[pe.withStroke(linewidth=9, foreground=(0.91, 0.73, 0.29, 0.10)), pe.withStroke(linewidth=4, foreground=(0.91, 0.73, 0.29, 0.25))])

# --- latar: kerangka molekul samar
def bentuk(titik, cx, cy, sk, rot, tutup=False, al=0.24):
    t = np.array(titik, float); r = np.deg2rad(rot); R2 = np.array([[np.cos(r), -np.sin(r)], [np.sin(r), np.cos(r)]])
    t = t @ R2.T * sk + [cx, cy]
    if tutup: t = np.vstack([t, t[:1]])
    neon(t[:, 0], t[:, 1], '#9fd8a8', 0.7, al)
heks = [(np.cos(np.pi / 3 * k), np.sin(np.pi / 3 * k)) for k in range(6)]
kursi = [(0, 0), (0.87, 0.5), (1.87, 0.35), (2.6, 0.9), (1.73, 0.4), (0.73, 0.55)]
zig = [(0.87 * k, 0.5 * (k % 2)) for k in range(6)]
for (cx, cy, sk, rot, jenis) in [(-3.6, 3.3, 0.55, 15, 'h'), (3.5, 3.6, 0.5, 0, 'k'), (-3.9, -3.5, 0.6, 20, 'z'),
                                 (3.6, -3.3, 0.55, -10, 'h'), (-4.2, 0.6, 0.45, 80, 'z'), (0.6, 3.9, 0.45, -5, 'z'),
                                 (0.2, -3.9, 0.5, 30, 'k'), (4.2, -1.9, 0.42, 90, 'h')]:
    if jenis == 'h': bentuk(heks, cx, cy, sk, rot, True)
    elif jenis == 'k': bentuk(kursi, cx - 0.7, cy, sk, rot, True)
    else: bentuk(zig, cx - 1.2, cy, sk, rot)

# --- molekul utama: parasetamol, HO-C6H4-NH-C(=O)-CH3, panjang ikatan L
L = 1.45; ox, oy = -0.8, -1.0
P = lambda x, y: (ox + L * x, oy + L * y)
V = [P(np.cos(np.pi / 3 * k), np.sin(np.pi / 3 * k)) for k in range(6)]
pusat = P(0, 0)
for k in range(6): ikatan(V[k], V[(k + 1) % 6])
for k in (0, 2, 4): ganda_dalam(V[k], V[(k + 1) % 6], pusat)
O1 = P(-2, 0); N = P(2, 0); Ck = P(2.5, 0.866); Ok = P(2.5, 1.866); Me = P(3.5, 0.866)
ikatan(V[3], O1, pendek=(0, 0.42)); label(O1[0] - 0.25, O1[1], 'HO')
ikatan(V[0], N, pendek=(0, 0.36)); label(*N, 'N'); label(N[0], N[1] - 0.68, 'H', fs=21)
ikatan(N, Ck, pendek=(0.36, 0)); ikatan(Ck, Me)
ikatan(Ck, Ok, pendek=(0, 0.36))
dx = 0.24
ikatan((Ck[0] + dx, Ck[1] + 0.14), (Ok[0] + dx, Ok[1]), pendek=(0, 0.4))
label(*Ok, 'O')
# pasangan elektron bebas pada O karbonil
for sx in (-0.17, 0.17):
    for k2, a2 in [(6, .08), (1, .9)]: ax.scatter(Ok[0] + sx * 1.2, Ok[1] + 0.46, s=9 * k2, color='#f6d27a', alpha=a2, lw=0, zorder=6)

# --- panah lengkung: Nu⁻ menyerang C karbonil, elektron π pindah ke O
Nu = (Ck[0] + 0.75, Ck[1] + 2.0); label(Nu[0] + 0.3, Nu[1] + 0.15, 'Nu', c='#f4a261', fs=24)
neon([Nu[0] + 0.8, Nu[0] + 1.04], [Nu[1] + 0.47, Nu[1] + 0.47], '#f4a261', 1.6, glow='#f4a261')  # muatan negatif
def panah(a, b, rad, c='#f4a261'):
    for k, a2 in [(5, .07), (2.5, .2), (1, 1)]:
        ax.add_patch(FancyArrowPatch(a, b, connectionstyle=f'arc3,rad={rad}', arrowstyle='-|>,head_length=6,head_width=3.2',
                                     mutation_scale=1.6 if k == 1 else 1.6, lw=1.5 * k, color=c, alpha=a2, zorder=7))
panah((Nu[0] + 0.45, Nu[1] - 0.3), (Ck[0] + 0.16, Ck[1] + 0.14), -0.5)
panah(((Ck[0] + Ok[0]) / 2 - 0.1, (Ck[1] + Ok[1]) / 2), (Ok[0] - 0.5, Ok[1] + 0.1), -1.0)

# --- butir cahaya
rng = np.random.default_rng(4)
for _ in range(45):
    x, y = rng.uniform(-4.6, 4.6), rng.uniform(-4.3, 4.3); r = rng.uniform(4, 14)
    if abs(x - 0.3) < 3.4 and abs(y - 0.3) < 2.8: continue
    for k, a2 in [(8, .03), (3, .1), (1, .5)]: ax.scatter(x, y, s=r * k, color='#d8f3df', alpha=a2, lw=0)
f.savefig(f'{K}/sampul-latar.png', transparent=True); plt.close(f)
daftar = ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in JUDUL)
open(f'{K}/sampul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} body{{margin:0;font-family:Inter,sans-serif}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;color:#143d2a;background:#f8fcf9}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:9mm;background:#143d2a}}
.ed{{position:absolute;top:24mm;left:22mm;font-size:9pt;letter-spacing:6px;font-weight:800;color:#b9801a}}
.pen{{position:absolute;top:24mm;right:18mm;font-size:9pt;font-weight:800;letter-spacing:6px;color:#143d2a}}
.jd{{position:absolute;top:36mm;left:20mm;font-size:54pt;font-weight:900;line-height:.88;letter-spacing:-1px;color:#143d2a}}
.jd span{{color:#2e8b57}}
.sb{{position:absolute;top:77mm;left:22mm;width:130mm;font-size:13pt;line-height:1.45;color:#3f5a48;border-top:.6mm solid #d79a2b;padding-top:4mm}}
.panel{{position:absolute;left:22mm;right:18mm;top:98mm;bottom:22mm;background:radial-gradient(ellipse at 50% 60%,#24603f 0%,#18432c 55%,#0e2a1b 100%)}}
.panel img{{position:absolute;left:4%;top:5%;width:92%;height:90%;object-fit:contain}}
.ln{{position:absolute;bottom:22mm;left:22mm;width:40mm;height:.7mm;background:#d79a2b}}
.pers{{position:absolute;right:6mm;bottom:4mm;font-family:Caladea,serif;font-style:italic;font-size:13pt;color:rgba(250,222,210,.85)}}
.blk .isi{{position:absolute;top:24mm;left:22mm;right:20mm}}
.blk h2{{font-size:18pt;font-weight:900;margin:0 0 6mm 0;text-transform:uppercase;letter-spacing:1.5px;line-height:1.2;color:#143d2a}} .blk h2 span{{color:#2e8b57}}
.blk p{{font-size:10.5pt;line-height:1.6;color:#233a2b;margin:0 0 3.5mm 0;font-family:Caladea,serif}}
.blk ul{{list-style:none;padding:0;margin:8mm 0 0 0;columns:2;column-gap:10mm;font-size:9.2pt;border-top:.5mm solid #143d2a;padding-top:5mm;color:#233a2b}}
.blk li{{margin:0 0 2.2mm 0;padding-left:8mm;text-indent:-8mm;break-inside:avoid}} .blk li b{{display:inline-block;width:8mm;text-indent:0;color:#b9801a}}
.tp{{position:absolute;left:22mm;right:20mm;bottom:22mm;background:#e6f4ea;padding:5mm 6mm;font-family:Caladea,serif;font-size:10pt;line-height:1.55;color:#233a2b}}
.tp b{{font-family:Inter,sans-serif;font-size:8.5pt;letter-spacing:2px;color:#2e8b57;display:block;margin-bottom:1.5mm}}
</style></head><body>
<div class="pg"><div class="bar"></div><div class="ed">EDISI PERTAMA</div><div class="pen">SEPTIAN ANUGRAH DWI PUTRA</div>
<div class="jd">KIMIA<br><span>ORGANIK 1</span></div>
<div class="sb">Senyawa Monofungsi · dari struktur dan ikatan sampai amina</div>
<div class="panel"><img src="sampul-latar.png"></div></div>
<div class="pg blk"><div class="bar"></div><div class="isi"><h2>Mengapa molekul <span>bereaksi seperti itu?</span></h2>
<p>Buku ini membahas senyawa organik monofungsi: bagaimana atom karbon tersambung, bagaimana bentuk tiga dimensi dan sebaran elektron menentukan sifat sebuah molekul, dan bagaimana setiap gugus fungsi bereaksi.</p>
<p>Setiap reaksi dijelaskan dari aliran elektronnya, langkah demi langkah dengan panah lengkung, sehingga pembaca memahami mengapa sebuah reaksi terjadi, bukan sekadar menghafal hasilnya. Contoh diambil dari obat, bahan alam, industri, dan laboratorium.</p>
<p>Setiap bab ditutup dengan ringkasan, pertanyaan konsep, soal beserta jawabannya, pembahasan soal terpilih, dan bacaan lanjut. Buku ini adalah lanjutan dari <i>Kimia Kuantum</i> dan <i>Termodinamika Kimia</i>.</p>
<ul>{daftar}</ul></div>
<div class="tp"><b>TENTANG PENYUSUN</b><b style="color:#143d2a;letter-spacing:.5px;font-size:11pt">Septian Anugrah Dwi Putra</b>Mahasiswa S1 Kimia, Universitas Negeri Surabaya. Penyusun <i>Fisika Umum</i>, <i>Kimia Kuantum</i>, dan <i>Kimia Fisika 1</i>; buku ini disusun untuk mata kuliah Senyawa Organik Monofungsi.</div></div>
</body></html>''')
