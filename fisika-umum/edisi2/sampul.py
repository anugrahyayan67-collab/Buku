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
f = plt.figure(figsize=(6.7, 6.2), dpi=240); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(-5.4, 5.4); ax.set_ylim(-5.0, 5.0)
def neon(x, y, c, lw=1.0):
    for k, a2 in [(8, .04), (4.5, .09), (2.2, .25), (1, 1)]: ax.plot(x, y, color=c, lw=lw * k, alpha=a2, solid_capstyle='round')
def bintik(x, y, c, s):
    for k in np.geomspace(16, 1.6, 22): ax.scatter(x, y, s=s * k, color=c, alpha=0.035, lw=0, zorder=5)
    ax.scatter(x, y, s=s, color=c, alpha=1, lw=0, zorder=6)
Y, X = np.mgrid[-5:5:400j, -5.4:5.4:430j]; Ex = 0 * X; Ey = 0 * X
Q = [(-1.9, 1), (1.9, -1)]
for x0, q in Q:
    r3 = ((X - x0) ** 2 + Y ** 2 + 0.03) ** 1.5; Ex += q * (X - x0) / r3; Ey += q * Y / r3
ang = np.linspace(0, 2 * np.pi, 22, endpoint=False); seeds = np.c_[-1.9 + 0.35 * np.cos(ang), 0.35 * np.sin(ang)]
for lw, al in [(4.0, .06), (2.0, .16), (0.9, 1)]:
    ax.streamplot(X, Y, Ex, Ey, color=matplotlib.colors.to_rgba('#7fc0f0', al), linewidth=lw, start_points=seeds, arrowsize=0, broken_streamlines=False, integration_direction='forward')
    ax.streamplot(X, Y, Ex, Ey, color=matplotlib.colors.to_rgba('#7fc0f0', al), linewidth=lw, start_points=seeds * [-1, 1], arrowsize=0, broken_streamlines=False, integration_direction='backward')
bintik(-1.9, 0, '#f0a060', 90); bintik(1.9, 0, '#9fd2ff', 90)
f.savefig(f'{K}/sampul-latar.png', transparent=True); plt.close(f)
daftar = ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in JUDUL)
open(f'{K}/sampul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} body{{margin:0;font-family:Inter,sans-serif}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;color:#0e2748;background:#f8fbfe}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:9mm;background:#0e2748}}
.ed{{position:absolute;top:24mm;left:22mm;font-size:9pt;letter-spacing:6px;font-weight:800;color:#c0601f}}
.pen{{position:absolute;top:24mm;right:18mm;font-size:9pt;font-weight:800;letter-spacing:6px;color:#0e2748}}
.jd{{position:absolute;top:36mm;left:20mm;font-size:54pt;font-weight:900;line-height:.88;letter-spacing:-1px;color:#0e2748}}
.jd span{{color:#1b75bc}}
.sb{{position:absolute;top:77mm;left:22mm;width:130mm;font-size:13pt;line-height:1.45;color:#4a5668;border-top:.6mm solid #f0a060;padding-top:4mm}}
.panel{{position:absolute;left:22mm;right:18mm;top:98mm;bottom:22mm;background:radial-gradient(ellipse at 50% 60%,#163e6e 0%,#0e2748 45%,#081a31 80%,#06142a 100%)}}
.panel img{{position:absolute;left:4%;top:5%;width:92%;height:90%;object-fit:contain}}
.ln{{position:absolute;bottom:22mm;left:22mm;width:40mm;height:.7mm;background:#f0a060}}
.pers{{position:absolute;right:6mm;bottom:4mm;font-family:Caladea,serif;font-style:italic;font-size:13pt;color:rgba(221,214,250,.85)}}
.blk .isi{{position:absolute;top:24mm;left:22mm;right:20mm}}
.blk h2{{font-size:18pt;font-weight:900;margin:0 0 6mm 0;text-transform:uppercase;letter-spacing:1.5px;line-height:1.2;color:#0e2748}} .blk h2 span{{color:#1b75bc}}
.blk p{{font-size:10.5pt;line-height:1.6;color:#1f2a38;margin:0 0 3.5mm 0;font-family:Caladea,serif}}
.blk ul{{list-style:none;padding:0;margin:8mm 0 0 0;columns:2;column-gap:10mm;font-size:9.2pt;border-top:.5mm solid #0e2748;padding-top:5mm;color:#1f2a38}}
.blk li{{margin:0 0 2.2mm 0;padding-left:8mm;text-indent:-8mm;break-inside:avoid}} .blk li b{{display:inline-block;width:8mm;text-indent:0;color:#c0601f}}
.tp{{position:absolute;left:22mm;right:20mm;bottom:22mm;background:#e8f1fa;padding:5mm 6mm;font-family:Caladea,serif;font-size:10pt;line-height:1.55;color:#1f2a38}}
.tp b{{font-family:Inter,sans-serif;font-size:8.5pt;letter-spacing:2px;color:#1b75bc;display:block;margin-bottom:1.5mm}}
</style></head><body>
<div class="pg"><div class="bar"></div><div class="ed">EDISI PERTAMA</div><div class="pen">SEPTIAN ANUGRAH DWI PUTRA</div>
<div class="jd">FISIKA<br><span>UMUM</span></div>
<div class="sb">untuk mahasiswa kimia dan ilmu-ilmu sains</div>
<div class="panel"><img src="sampul-latar.png"></div></div>
<div class="pg blk"><div class="bar"></div><div class="isi"><h2>Fisika sebagai <span>dasar kimia</span></h2>
<p>Buku ini membawa pembaca dari pengukuran dan vektor sampai atom, foton, dan inti, dalam lima belas bab yang masing-masing utuh: semua yang diperlukan untuk memahami sebuah bab diajarkan di bab itu.</p>
<p>Setiap gagasan tidak hanya dirumuskan, tetapi juga dijelaskan asal-usulnya: mengapa gaya sebenarnya adalah laju perubahan momentum, mengapa air naik dalam pipa kapiler, mengapa garam larut dalam air. Setiap gagasan diikuti contoh soal yang diselesaikan langkah demi langkah dan diperiksa kewajarannya.</p>
<p>Hampir setiap bab memuat kaitan langsung dengan kimia: kurva energi ikatan, getaran molekul, persamaan Arrhenius, energi bebas Gibbs, elektrokimia, spektrum NMR, dan struktur atom. Setiap bab ditutup dengan ringkasan, pertanyaan konsep, soal, jawaban, dan pembahasan.</p>
<ul>{daftar}</ul></div>
<div class="tp"><b>TENTANG PENYUSUN</b><b style="color:#0e2748;letter-spacing:.5px;font-size:11pt">Septian Anugrah Dwi Putra</b>Mahasiswa S1 Kimia, Universitas Negeri Surabaya. Buku ini disusun sebagai bekal memahami fisika yang menjadi dasar ilmu kimia, dari mekanika sampai struktur atom.</div></div>
</body></html>''')
