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
latar('sampul-latar.png', 4.3, 3.9, 0.55)
latar('sampul-latar2.png', 7.0, 1.4, 0.4, 0.45)
daftar = ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in JUDUL)
open(f'{K}/sampul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} body{{margin:0;font-family:Inter,sans-serif}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;color:#fff;
 background:radial-gradient(ellipse at 52% 68%,#3a2a85 0%,#221860 38%,#150f3d 75%,#0e0a2c 100%)}}
.art{{position:absolute;inset:0;background:url(sampul-latar.png) center/cover no-repeat}}
.art2{{position:absolute;inset:0;background:url(sampul-latar2.png) center/cover no-repeat}}
.ed{{position:absolute;top:24mm;left:20mm;font-size:9pt;letter-spacing:6px;font-weight:800;color:#f2c25b}}
.pen{{position:absolute;top:24mm;right:20mm;font-size:9pt;font-weight:800;letter-spacing:6px;color:#fff}}
.jd{{position:absolute;top:33mm;left:17mm;font-size:92pt;font-weight:900;line-height:.86;letter-spacing:-1px}}
.jd span{{color:#5ce1e6}}
.sb{{position:absolute;top:95mm;left:20mm;width:125mm;font-size:13.5pt;line-height:1.45;color:#ddd6fa;border-top:.6mm solid #f2c25b;padding-top:4mm}}
.pers{{position:absolute;right:20mm;bottom:18mm;font-family:Caladea,serif;font-style:italic;font-size:13pt;color:rgba(221,214,250,.75)}}
.blk .isi{{position:absolute;top:26mm;left:20mm;right:22mm}}
.blk h2{{font-size:19pt;font-weight:900;margin:0 0 7mm 0;text-transform:uppercase;letter-spacing:1.5px;line-height:1.2}} .blk h2 span{{color:#5ce1e6}}
.blk p{{font-size:10.5pt;line-height:1.62;color:#e4defb;margin:0 0 4mm 0;font-family:Caladea,serif;max-width:150mm}}
.blk ul{{list-style:none;padding:0;margin:9mm 0 0 0;columns:2;column-gap:10mm;font-size:9.2pt;border-top:.4mm solid rgba(92,225,230,.35);padding-top:6mm}}
.blk li{{margin:0 0 2.3mm 0}} .blk li b{{display:inline-block;width:8mm;color:#f2c25b}}
.tp{{position:absolute;left:20mm;right:22mm;bottom:22mm;border-top:.4mm solid rgba(92,225,230,.35);padding-top:5mm;font-family:Caladea,serif;font-size:10pt;line-height:1.55;color:#e4defb}}
.tp b{{font-family:Inter,sans-serif;font-size:8.5pt;letter-spacing:2px;color:#5ce1e6;display:block;margin-bottom:2mm}}
</style></head><body>
<div class="pg"><div class="art"></div><div class="ed">EDISI PERTAMA</div><div class="pen">SEPTIAN ANUGRAH DWI PUTRA</div>
<div class="jd">KIMIA<br><span>KUANTUM</span></div>
<div class="sb">dari persamaan Schrödinger sampai kimia komputasi</div>
<div class="pers">ψ = Σ c<sub>i</sub> φ<sub>i</sub></div></div>
<div class="pg blk"><div class="art2"></div><div class="isi"><h2>Mengapa atom <span>membentuk molekul?</span></h2>
<p>Buku ini menjawab pertanyaan-pertanyaan terdalam kimia dengan mekanika kuantum: mengapa metana tetrahedral, mengapa O₂ paramagnetik, mengapa benzena luar biasa mantap, mengapa larutan kompleks berwarna, dan bagaimana komputer meramalkan struktur molekul.</p>
<p>Setiap hasil diturunkan langkah demi langkah dan langsung dikaitkan dengan kimia: spektroskopi, ikatan, reaktivitas, sifat periodik. Setiap gagasan diikuti contoh soal yang diselesaikan dan diperiksa kewajarannya, dan sejak bab-bab awal pembaca diajak menghitung sendiri dengan Python.</p>
<p>Setiap bab ditutup dengan ringkasan, pertanyaan konsep, soal bertingkat beserta jawabannya, pembahasan soal terpilih, dan bacaan lanjut. Buku ini adalah lanjutan dari <i>Fisika Umum</i>.</p>
<ul>{daftar}</ul></div>
<div class="tp"><b>TENTANG PENYUSUN</b><b style="color:#fff;letter-spacing:.5px;font-size:11pt">Septian Anugrah Dwi Putra</b>Mahasiswa S1 Kimia, Universitas Negeri Surabaya. Penyusun <i>Fisika Umum</i>; buku ini disusun sebagai lanjutannya, dari dasar-dasar mekanika kuantum sampai kimia komputasi.</div></div>
</body></html>''')
