#!/usr/bin/env python3
# Sampul depan & belakang Kimia Kuantum Edisi 1 + gambar latar: interferensi tiga gelombang (pola heksagonal, seperti benzena/grafena).
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
        for k2, a2 in [(6, .05), (2.5, .2), (1, 1)]: ax.plot(cx + rr * np.cos(t), cy + rr * np.sin(t), color='#f2c25b', lw=0.8 * k2, alpha=al * a2 * redup)
    ax.set_xlim(0, w); ax.set_ylim(0, h); f.savefig(f'{K}/{nama}', transparent=True); plt.close(f)
from matplotlib.patches import Polygon
f = plt.figure(figsize=(7.4, 7.0), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, 10.6); ax.set_ylim(0, 10)
for k, a2 in [(26, .04), (14, .08), (7, .18), (3, .6), (1.4, 1)]: ax.plot([0, 3.95], [3.1, 4.55], color='#ffffff' if k < 4 else '#d9d4ee', lw=k, alpha=a2, solid_capstyle='round')
ax.plot([0, 3.95], [3.1, 4.55], color='#a9a4c4', lw=0.8)
ax.add_patch(Polygon([(2.6, 1.6), (6.4, 1.6), (4.5, 7.6)], closed=True, fc='#eceaf7', ec='none', alpha=0.95))
ax.add_patch(Polygon([(4.5, 7.6), (6.4, 1.6), (5.2, 1.6)], closed=True, fc='#dcd8f0', ec='none', alpha=0.9))
ax.add_patch(Polygon([(2.6, 1.6), (6.4, 1.6), (4.5, 7.6)], closed=True, fc='none', ec='#8f89b0', lw=1.4))
ax.plot([3.1, 4.3], [2.2, 6.4], color='white', lw=3, alpha=0.7)
cols = ['#e8321e', '#f2781e', '#f5c71e', '#46c24f', '#1fa7d9', '#3b4ae0', '#7b2fc9']
x0, y0, x1 = 5.05, 4.55, 9.0
for i, c in enumerate(cols):
    yt = 7.4 - i * 0.62; ax.fill([x0, x1, x1, x0], [y0 + 0.06, yt, yt - 0.62, y0 - 0.06], color=c, alpha=0.62, lw=0)
import numpy as np
yy = np.linspace(7.4 - 7 * 0.62, 7.4, 400)
from matplotlib.colors import LinearSegmentedColormap
cmv = LinearSegmentedColormap.from_list('v', cols[::-1])
ax.imshow(cmv(np.linspace(0, 1, 400))[:, None, :].repeat(20, 1), extent=[9.0, 9.7, yy[0], yy[-1]], origin='lower', aspect='auto', zorder=3)
for yl in [7.4 - 0.62 * 0.7, 7.4 - 0.62 * 2.6, 7.4 - 0.62 * 4.2, 7.4 - 0.62 * 5.1, 7.4 - 0.62 * 6.4]: ax.plot([9.0, 9.7], [yl, yl], color='#1e1548', lw=2.2, zorder=4)
f.savefig(f'{K}/sampul-latar.png', transparent=True); plt.close(f)
daftar = ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in JUDUL)
open(f'{K}/sampul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} body{{margin:0;font-family:Inter,sans-serif}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;color:#1e1548;background:#ffffff}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:9mm;background:#1e1548}}
.ed{{position:absolute;top:24mm;left:22mm;font-size:9pt;letter-spacing:6px;font-weight:800;color:#b9801a}}
.pen{{position:absolute;top:24mm;right:18mm;font-size:9pt;font-weight:800;letter-spacing:6px;color:#1e1548}}
.jd{{position:absolute;top:34mm;left:20mm;font-size:84pt;font-weight:900;line-height:.88;letter-spacing:-1px;color:#1e1548}}
.jd span{{color:#4a3ab0}}
.sb{{position:absolute;top:92mm;left:22mm;width:130mm;font-size:13pt;line-height:1.45;color:#4b4566;border-top:.6mm solid #d79a2b;padding-top:4mm}}
.panel{{position:absolute;left:12mm;right:0;top:108mm;bottom:30mm}}
.panel img{{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}}
.ln{{position:absolute;bottom:22mm;left:22mm;width:40mm;height:.7mm;background:#d79a2b}}
.pers{{position:absolute;right:22mm;bottom:26mm;font-family:Caladea,serif;font-style:italic;font-size:13pt;color:rgba(221,214,250,.85)}}
.blk .isi{{position:absolute;top:24mm;left:22mm;right:20mm}}
.blk h2{{font-size:18pt;font-weight:900;margin:0 0 6mm 0;text-transform:uppercase;letter-spacing:1.5px;line-height:1.2;color:#1e1548}} .blk h2 span{{color:#4a3ab0}}
.blk p{{font-size:10.5pt;line-height:1.6;color:#2b2545;margin:0 0 3.5mm 0;font-family:Caladea,serif}}
.blk ul{{list-style:none;padding:0;margin:8mm 0 0 0;columns:2;column-gap:10mm;font-size:9.2pt;border-top:.5mm solid #1e1548;padding-top:5mm;color:#2b2545}}
.blk li{{margin:0 0 2.2mm 0;padding-left:8mm;text-indent:-8mm;break-inside:avoid}} .blk li b{{display:inline-block;width:8mm;text-indent:0;color:#b9801a}}
.tp{{position:absolute;left:22mm;right:20mm;bottom:22mm;background:#efecfc;padding:5mm 6mm;font-family:Caladea,serif;font-size:10pt;line-height:1.55;color:#2b2545}}
.tp b{{font-family:Inter,sans-serif;font-size:8.5pt;letter-spacing:2px;color:#4a3ab0;display:block;margin-bottom:1.5mm}}
</style></head><body>
<div class="pg"><div class="bar"></div><div class="ed">EDISI PERTAMA</div><div class="pen">SEPTIAN ANUGRAH DWI PUTRA</div>
<div class="jd">KIMIA<br><span>KUANTUM</span></div>
<div class="sb">dari persamaan Schrödinger sampai kimia komputasi</div>
<div class="panel"><img src="sampul-latar.png"></div><div class="ln"></div></div>
<div class="pg blk"><div class="bar"></div><div class="isi"><h2>Mengapa atom <span>membentuk molekul?</span></h2>
<p>Buku ini menjawab pertanyaan-pertanyaan terdalam kimia dengan mekanika kuantum: mengapa metana tetrahedral, mengapa O₂ paramagnetik, mengapa benzena luar biasa mantap, mengapa larutan kompleks berwarna, dan bagaimana komputer meramalkan struktur molekul.</p>
<p>Setiap hasil diturunkan langkah demi langkah dan langsung dikaitkan dengan kimia: spektroskopi, ikatan, reaktivitas, sifat periodik. Setiap gagasan diikuti contoh soal yang diselesaikan dan diperiksa kewajarannya, dan sejak bab-bab awal pembaca diajak menghitung sendiri dengan Python.</p>
<p>Setiap bab ditutup dengan ringkasan, pertanyaan konsep, soal bertingkat beserta jawabannya, pembahasan soal terpilih, dan bacaan lanjut. Buku ini adalah lanjutan dari <i>Fisika Umum</i>.</p>
<ul>{daftar}</ul></div>
<div class="tp"><b>TENTANG PENYUSUN</b><b style="color:#1e1548;letter-spacing:.5px;font-size:11pt">Septian Anugrah Dwi Putra</b>Mahasiswa S1 Kimia, Universitas Negeri Surabaya. Penyusun <i>Fisika Umum</i>; buku ini disusun sebagai lanjutannya, dari dasar-dasar mekanika kuantum sampai kimia komputasi.</div></div>
</body></html>''')
