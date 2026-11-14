#!/usr/bin/env python3
# Sampul depan & belakang Edisi 3 (HTML 2 halaman) + gambar latar: awan elektron orbital 3d_z2 hidrogen.
import sys, os, re, glob, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
R = os.path.expanduser('~/fisika-umum'); K = f'{R}/edisi2/_kerja'
JUDUL = [re.match(r'# Bab (\d+) (.*)', open(sorted(glob.glob(f'{d}/[a-z]-*.md'))[0]).readline()).groups() for d in sorted(glob.glob(f'{R}/bab[0-9][0-9]'))]

def awan(nama, w_in, h_in, cx, cy, skala, ntitik, sudut=0.0, redup=1.0):
    nx, ny = int(w_in * 120), int(h_in * 120)
    X, Y = np.meshgrid(np.linspace(0, w_in, nx), np.linspace(h_in, 0, ny))
    u, v = (X - cx) / skala, (Y - cy) / skala
    c, s = np.cos(sudut), np.sin(sudut); x, z = c * u - s * v, s * u + c * v
    r = np.sqrt(x * x + z * z) + 1e-9
    psi = r ** 2 * np.exp(-r / 3) * (3 * (z / r) ** 2 - 1)            # 3d_z2, bidang xz
    rho = psi ** 2; rho /= rho.max()
    cm = LinearSegmentedColormap.from_list('g', [(0, (0.04, 0.10, 0.19, 0)), (0.25, (0.11, 0.46, 0.74, 0.55)), (0.6, (0.50, 0.75, 0.94, 0.85)), (1, (1, 1, 1, 1))])
    f = plt.figure(figsize=(w_in, h_in), dpi=200); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off')
    ax.imshow(cm(rho ** 0.6) * [1, 1, 1, redup], extent=[0, w_in, 0, h_in], interpolation='bicubic')
    rng = np.random.default_rng(7); p = (rho / rho.sum()).ravel()
    k = rng.choice(p.size, ntitik, p=p); iy, ix = np.unravel_index(k, rho.shape)
    px = X[0, ix] + rng.normal(0, w_in / nx * .6, ntitik); py = Y[iy, 0] + rng.normal(0, h_in / ny * .6, ntitik)
    ax.scatter(px, py, s=0.5, c='white', alpha=0.55 * redup, lw=0)
    for rr in [1.3, 2.4, 3.6]:                                         # lintasan Bohr tipis sebagai gema sejarah
        t = np.linspace(0, 2 * np.pi, 400); ax.plot(cx + rr * np.cos(t), cy + rr * np.sin(t) * 0.999, color='#f0a060', lw=0.5, alpha=0.30 * redup)
    ax.set_xlim(0, w_in); ax.set_ylim(0, h_in)
    f.savefig(f'{K}/{nama}', transparent=True); plt.close(f)

awan('sampul-latar.png', 8.27, 11.69, 4.6, 3.9, 0.21, 90000, sudut=0.35)
awan('sampul-latar2.png', 8.27, 11.69, 6.9, 1.6, 0.15, 30000, sudut=-0.5, redup=0.5)

daftar = ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in JUDUL)
open(f'{K}/sampul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} body{{margin:0;font-family:Inter,sans-serif}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;color:#fff;
 background:radial-gradient(ellipse at 56% 67%,#163e6e 0%,#0e2748 38%,#081a31 75%,#06142a 100%)}}
.art{{position:absolute;inset:0;background:url(sampul-latar.png) center/cover no-repeat}}
.art2{{position:absolute;inset:0;background:url(sampul-latar2.png) center/cover no-repeat}}
.ed{{position:absolute;top:24mm;left:20mm;font-size:9pt;letter-spacing:6px;font-weight:800;color:#f0a060}}
.jd{{position:absolute;top:33mm;left:17mm;font-size:96pt;font-weight:900;line-height:.86;letter-spacing:-1px}}
.jd span{{color:#7fc0f0}}
.sb{{position:absolute;top:95mm;left:20mm;width:115mm;font-size:13.5pt;line-height:1.45;color:#cfe3f5;font-weight:400;border-top:.6mm solid #f0a060;padding-top:4mm}}
.pen{{position:absolute;top:24mm;right:20mm;text-align:right;font-size:9pt;font-weight:800;letter-spacing:6px;color:#fff}}
.tp{{position:absolute;left:20mm;right:22mm;bottom:22mm;border-top:.4mm solid rgba(127,192,240,.35);padding-top:5mm;font-family:Caladea,serif;font-size:10pt;line-height:1.55;color:#dbe9f6}}
.tp b{{font-family:Inter,sans-serif;font-size:8.5pt;letter-spacing:2px;color:#7fc0f0;display:block;margin-bottom:2mm}}
.pers{{position:absolute;right:20mm;bottom:18mm;font-family:Caladea,serif;font-style:italic;font-size:13pt;color:rgba(207,227,245,.75);letter-spacing:.5px}}
.blk .isi{{position:absolute;top:26mm;left:20mm;right:22mm}}
.blk h2{{font-size:24pt;font-weight:900;margin:0 0 7mm 0;letter-spacing:-.4px}}
.blk h2 span{{color:#7fc0f0}}
.blk p{{font-size:10.5pt;line-height:1.62;color:#dbe9f6;margin:0 0 4mm 0;font-family:Caladea,serif;max-width:150mm}}
.blk ul{{list-style:none;padding:0;margin:10mm 0 0 0;columns:2;column-gap:10mm;font-size:9.2pt;border-top:.4mm solid rgba(127,192,240,.35);padding-top:6mm}}
.blk li{{margin:0 0 2.4mm 0;color:#fff}} .blk li b{{display:inline-block;width:8mm;color:#f0a060}}
</style></head><body>
<div class="pg"><div class="art"></div><div class="ed">EDISI KEEMPAT</div>
<div class="jd">FISIKA<br><span>UMUM</span></div>
<div class="sb">untuk mahasiswa kimia dan ilmu-ilmu sains</div>
<div class="pen">SEPTIAN ANUGRAH DWI PUTRA</div>
<div class="pers">Ĥψ = Eψ</div></div>
<div class="pg blk"><div class="art2"></div><div class="isi"><h2>Fisika sebagai <span>dasar kimia</span></h2>
<p>Buku ini membawa pembaca dari pengukuran dan vektor sampai orbital atom, ikatan kimia, dan inti atom, dalam lima belas bab yang masing-masing utuh: semua yang diperlukan untuk memahami sebuah bab diajarkan di bab itu.</p>
<p>Setiap gagasan tidak hanya dirumuskan, tetapi juga dijelaskan asal-usulnya: mengapa gaya sebenarnya adalah laju perubahan momentum, mengapa air naik dalam pipa kapiler, mengapa garam larut dalam air, mengapa wortel berwarna jingga. Setiap gagasan diikuti contoh soal yang diselesaikan langkah demi langkah dan diperiksa kewajarannya.</p>
<p>Hampir setiap bab memuat kaitan langsung dengan kimia: kurva energi ikatan, getaran molekul dan spektrum inframerah, sentrifugasi, persamaan Arrhenius, energi bebas Gibbs dan kesetimbangan fasa, larutan elektrolit, elektrokimia, spektrum NMR, dan struktur atom. Setiap bab ditutup dengan ringkasan, pertanyaan konsep, soal latihan, jawaban semua soal, dan pembahasan soal terpilih.</p>
<ul>{daftar}</ul></div>
<div class="tp"><b>TENTANG PENYUSUN</b><b style="color:#fff;letter-spacing:.5px;font-size:11pt">Septian Anugrah Dwi Putra</b>Mahasiswa S1 Kimia, Universitas Negeri Surabaya. Buku ini disusun sebagai bekal memahami fisika yang menjadi dasar ilmu kimia, dari mekanika sampai struktur atom.</div></div>
</body></html>''')
