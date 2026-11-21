#!/usr/bin/env python3
# Sampul depan & belakang Kimia Fisika 1: Termodinamika Kimia Edisi 1 + gambar: isoterm bercahaya dan siklus Carnot.
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
f = plt.figure(figsize=(6.7, 6.2), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0.45, 2.75); ax.set_ylim(0.15, 6.1)
def neon(x, y, c, lw=1.0, al=1.0):
    for k, a2 in [(9, .04), (5, .09), (2.4, .25), (1, 1)]: ax.plot(x, y, color=c, lw=lw * k, alpha=a2 * al, solid_capstyle='round')
kp = 0.95; p = lambda x, T: kp * T / x
V = np.linspace(0.5, 2.7, 400)
warna = ['#7a2a22', '#a8382a', '#c9502f', '#e2733a', '#f4a261', '#f7c27a', '#fbe0a8']
for i, c in enumerate(warna):
    T = 1.0 + 0.4 * i; m = p(V, T) < 6.0; neon(V[m], p(V[m], T), c, 0.6, 0.45 + 0.07 * i)
# siklus Carnot gas monoatomik (gamma = 5/3): dua isoterm emas, dua adiabat putih
g = 5 / 3; Th, Tc = 2.6, 1.6; VA, VB = 0.62, 1.12
VC = VB * (Th / Tc) ** (1 / (g - 1)); VD = VA * (Th / Tc) ** (1 / (g - 1))
x1 = np.linspace(VA, VB, 100); x2 = np.linspace(VB, VC, 100); x3 = np.linspace(VC, VD, 100); x4 = np.linspace(VD, VA, 100)
ax.fill(np.r_[x1, x2, x3, x4], np.r_[p(x1, Th), p(VB, Th) * (VB / x2) ** g, p(x3, Tc), p(VD, Tc) * (VD / x4) ** g], color='#e9b949', alpha=0.10, lw=0)
neon(x1, p(x1, Th), '#e9b949', 1.6); neon(x3, p(x3, Tc), '#e9b949', 1.6)
neon(x2, p(VB, Th) * (VB / x2) ** g, '#fff3d6', 1.4); neon(x4, p(VD, Tc) * (VD / x4) ** g, '#fff3d6', 1.4)
for (x, y) in [(VA, p(VA, Th)), (VB, p(VB, Th)), (VC, p(VC, Tc)), (VD, p(VD, Tc))]:
    for k, a2 in [(10, .05), (4, .15), (1, 1)]: ax.scatter(x, y, s=30 * k, color='#e9b949', alpha=a2, lw=0, zorder=5)
rng = np.random.default_rng(4)
for _ in range(40):
    x, y = rng.uniform(0.5, 2.7), rng.uniform(0.3, 5.9); r = rng.uniform(4, 14)
    for k, a2 in [(8, .03), (3, .1), (1, .5)]: ax.scatter(x, y, s=r * k, color='#fbe0a8', alpha=a2, lw=0)
f.savefig(f'{K}/sampul-latar.png', transparent=True); plt.close(f)
daftar = ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in JUDUL)
open(f'{K}/sampul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} body{{margin:0;font-family:Inter,sans-serif}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;color:#3d1418;background:#fefaf8}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:9mm;background:#3d1418}}
.ed{{position:absolute;top:24mm;left:22mm;font-size:9pt;letter-spacing:6px;font-weight:800;color:#b9801a}}
.pen{{position:absolute;top:24mm;right:18mm;font-size:9pt;font-weight:800;letter-spacing:6px;color:#3d1418}}
.jd{{position:absolute;top:36mm;left:20mm;font-size:54pt;font-weight:900;line-height:.88;letter-spacing:-1px;color:#3d1418}}
.jd span{{color:#b4442b}}
.sb{{position:absolute;top:77mm;left:22mm;width:130mm;font-size:13pt;line-height:1.45;color:#5e4440;border-top:.6mm solid #d79a2b;padding-top:4mm}}
.panel{{position:absolute;left:22mm;right:18mm;top:98mm;bottom:22mm;background:radial-gradient(ellipse at 50% 60%,#7a2a22 0%,#4d1a17 55%,#2e0e10 100%)}}
.panel img{{position:absolute;left:4%;top:5%;width:92%;height:90%;object-fit:contain}}
.ln{{position:absolute;bottom:22mm;left:22mm;width:40mm;height:.7mm;background:#d79a2b}}
.pers{{position:absolute;right:6mm;bottom:4mm;font-family:Caladea,serif;font-style:italic;font-size:13pt;color:rgba(250,222,210,.85)}}
.blk .isi{{position:absolute;top:24mm;left:22mm;right:20mm}}
.blk h2{{font-size:18pt;font-weight:900;margin:0 0 6mm 0;text-transform:uppercase;letter-spacing:1.5px;line-height:1.2;color:#3d1418}} .blk h2 span{{color:#b4442b}}
.blk p{{font-size:10.5pt;line-height:1.6;color:#3a2522;margin:0 0 3.5mm 0;font-family:Caladea,serif}}
.blk ul{{list-style:none;padding:0;margin:8mm 0 0 0;columns:2;column-gap:10mm;font-size:9.2pt;border-top:.5mm solid #3d1418;padding-top:5mm;color:#3a2522}}
.blk li{{margin:0 0 2.2mm 0;padding-left:8mm;text-indent:-8mm;break-inside:avoid}} .blk li b{{display:inline-block;width:8mm;text-indent:0;color:#b9801a}}
.tp{{position:absolute;left:22mm;right:20mm;bottom:22mm;background:#fbece6;padding:5mm 6mm;font-family:Caladea,serif;font-size:10pt;line-height:1.55;color:#3a2522}}
.tp b{{font-family:Inter,sans-serif;font-size:8.5pt;letter-spacing:2px;color:#b4442b;display:block;margin-bottom:1.5mm}}
</style></head><body>
<div class="pg"><div class="bar"></div><div class="ed">EDISI PERTAMA</div><div class="pen">SEPTIAN ANUGRAH DWI PUTRA</div>
<div class="jd">KIMIA<br><span>FISIKA 1</span></div>
<div class="sb">Termodinamika Kimia · dari gas ideal sampai sel elektrokimia</div>
<div class="panel"><img src="sampul-latar.png"></div></div>
<div class="pg blk"><div class="bar"></div><div class="isi"><h2>Mengapa reaksi kimia <span>berjalan ke satu arah?</span></h2>
<p>Buku ini menjawab pertanyaan-pertanyaan pokok kimia fisika dengan termodinamika: mengapa gas memuai bila dipanaskan, dari mana datangnya kalor reaksi, mengapa es mencair tetapi tidak membeku kembali dengan sendirinya pada suhu kamar, sampai di mana sebuah reaksi berhenti, dan berapa tegangan yang dapat diberikan sebuah baterai.</p>
<p>Setiap besaran diberi gambaran molekulnya lebih dulu, lalu dihubungkan dengan pengukuran di laboratorium. Setiap gagasan diikuti contoh soal yang diselesaikan lengkap dan diperiksa kewajarannya, dengan data zat nyata dan sesekali perhitungan dengan Python.</p>
<p>Setiap bab ditutup dengan ringkasan, pertanyaan konsep, soal bertingkat beserta jawabannya, pembahasan soal terpilih, dan bacaan lanjut. Buku ini adalah lanjutan dari <i>Fisika Umum</i> dan <i>Kimia Kuantum</i>.</p>
<ul>{daftar}</ul></div>
<div class="tp"><b>TENTANG PENYUSUN</b><b style="color:#3d1418;letter-spacing:.5px;font-size:11pt">Septian Anugrah Dwi Putra</b>Mahasiswa S1 Kimia, Universitas Negeri Surabaya. Penyusun <i>Fisika Umum</i> dan <i>Kimia Kuantum</i>; buku ini disusun untuk mata kuliah Termodinamika Kimia, dari gas ideal sampai sel elektrokimia.</div></div>
</body></html>''')
