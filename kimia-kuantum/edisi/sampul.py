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
f = plt.figure(figsize=(6.7, 6.2), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(-5.4, 5.4); ax.set_ylim(-5.0, 5.0)
def neon(x, y, c, lw=1.0, al=1.0):
    for k, a2 in [(9, .04), (5, .09), (2.4, .25), (1, 1)]: ax.plot(x, y, color=c, lw=lw * k, alpha=a2 * al, solid_capstyle='round')
def hexa(cx, cy, r): t = np.arange(7) * np.pi / 3; return cx + r * np.cos(t), cy + r * np.sin(t)
for i in range(-7, 8):
    for j in range(-6, 7):
        cx = i * 1.5; cy = j * np.sqrt(3) + (i % 2) * np.sqrt(3) / 2; d = np.hypot(cx, cy)
        if d > 7: continue
        w = max(0.0, 1 - d / 7.2)
        c = '#5ce1e6' if d < 0.5 else ('#9d8cf0' if d < 3.6 else '#6b5fd0')
        x, y = hexa(cx, cy, 1.0); neon(x, y, c, 0.55 + 0.9 * w, 0.25 + 0.75 * w)
for t in np.arange(6) * np.pi / 3:
    x, y = np.cos(t), np.sin(t)
    for k, a2 in [(10, .05), (4, .15), (1, 1)]: ax.scatter(x, y, s=22 * k, color='#f2c25b', alpha=a2, lw=0)
tt = np.linspace(0, 2 * np.pi, 200); neon(0.55 * np.cos(tt), 0.55 * np.sin(tt), '#f2c25b', 0.9)
f.savefig(f'{K}/sampul-latar.png', transparent=True); plt.close(f)
daftar = ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in JUDUL)
open(f'{K}/sampul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} body{{margin:0;font-family:Inter,sans-serif}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;color:#1e1548;background:#faf9fe}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:9mm;background:#1e1548}}
.ed{{position:absolute;top:24mm;left:22mm;font-size:9pt;letter-spacing:6px;font-weight:800;color:#b9801a}}
.pen{{position:absolute;top:24mm;right:18mm;font-size:9pt;font-weight:800;letter-spacing:6px;color:#1e1548}}
.jd{{position:absolute;top:34mm;left:20mm;font-size:84pt;font-weight:900;line-height:.88;letter-spacing:-1px;color:#1e1548}}
.jd span{{color:#4a3ab0}}
.sb{{position:absolute;top:92mm;left:22mm;width:130mm;font-size:13pt;line-height:1.45;color:#4b4566;border-top:.6mm solid #d79a2b;padding-top:4mm}}
.panel{{position:absolute;left:22mm;right:18mm;top:118mm;bottom:22mm;background:radial-gradient(ellipse at 50% 60%,#3a2a85 0%,#221860 55%,#150f3d 100%)}}
.panel img{{position:absolute;left:4%;top:5%;width:92%;height:90%;object-fit:contain}}
.ln{{position:absolute;bottom:22mm;left:22mm;width:40mm;height:.7mm;background:#d79a2b}}
.pers{{position:absolute;right:6mm;bottom:4mm;font-family:Caladea,serif;font-style:italic;font-size:13pt;color:rgba(221,214,250,.85)}}
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
<div class="panel"><img src="sampul-latar.png"></div></div>
<div class="pg blk"><div class="bar"></div><div class="isi"><h2>Mengapa atom <span>membentuk molekul?</span></h2>
<p>Buku ini menjawab pertanyaan-pertanyaan terdalam kimia dengan mekanika kuantum: mengapa metana tetrahedral, mengapa O₂ paramagnetik, mengapa benzena luar biasa mantap, mengapa larutan kompleks berwarna, dan bagaimana komputer meramalkan struktur molekul.</p>
<p>Setiap hasil diturunkan langkah demi langkah dan langsung dikaitkan dengan kimia: spektroskopi, ikatan, reaktivitas, sifat periodik. Setiap gagasan diikuti contoh soal yang diselesaikan dan diperiksa kewajarannya, dan sejak bab-bab awal pembaca diajak menghitung sendiri dengan Python.</p>
<p>Setiap bab ditutup dengan ringkasan, pertanyaan konsep, soal bertingkat beserta jawabannya, pembahasan soal terpilih, dan bacaan lanjut. Buku ini adalah lanjutan dari <i>Fisika Umum</i>.</p>
<ul>{daftar}</ul></div>
<div class="tp"><b>TENTANG PENYUSUN</b><b style="color:#1e1548;letter-spacing:.5px;font-size:11pt">Septian Anugrah Dwi Putra</b>Mahasiswa S1 Kimia, Universitas Negeri Surabaya. Penyusun <i>Fisika Umum</i>; buku ini disusun sebagai lanjutannya, dari dasar-dasar mekanika kuantum sampai kimia komputasi.</div></div>
</body></html>''')
