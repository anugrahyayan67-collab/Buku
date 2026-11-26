#!/usr/bin/env python3
# Gambar Bab 13 Kimia Anorganik 1: kimia inti -> bab13/fig/*.png
import os, math, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab13', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
def koma(ax, sb='xy'):
    fm = FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−'))
    if 'x' in sb: ax.xaxis.set_major_formatter(fm)
    if 'y' in sb: ax.yaxis.set_major_formatter(fm)
# nuklida stabil (pilihan: isotop terbanyak tiap unsur)
st = [(1,1),(1,2),(2,3),(2,4),(3,6),(3,7),(4,9),(5,10),(5,11),(6,12),(6,13),(7,14),(7,15),(8,16),(8,17),(8,18),(9,19),(10,20),(11,23),(12,24),(13,27),(14,28),(15,31),(16,32),(17,35),(17,37),(18,40),(19,39),(20,40),(21,45),(22,48),(23,51),(24,52),(25,55),(26,56),(27,59),(28,58),(29,63),(30,64),(31,69),(32,74),(33,75),(34,80),(35,79),(36,84),(37,85),(38,88),(39,89),(40,90),(41,93),(42,98),(44,102),(45,103),(46,106),(47,107),(48,114),(50,120),(51,121),(52,128),(53,127),(54,132),(55,133),(56,138),(57,139),(58,140),(59,141),(60,142),(62,152),(63,153),(64,158),(65,159),(66,164),(67,165),(68,166),(69,169),(70,174),(71,175),(72,180),(73,181),(74,184),(75,185),(76,192),(77,193),(78,195),(79,197),(80,202),(81,205),(82,208),(83,209)]
def semf(Z, A):
    aV, aS, aC, aA, aP = 15.75, 17.8, 0.711, 23.7, 11.18; N = A - Z
    d = aP / A ** .5 if (Z % 2 == 0 and N % 2 == 0) else (-aP / A ** .5 if (Z % 2 == 1 and N % 2 == 1) else 0)
    return aV * A - aS * A ** (2 / 3) - aC * Z * (Z - 1) / A ** (1 / 3) - aA * (A - 2 * Z) ** 2 / A + d
# 1. pita kestabilan
f, ax = plt.subplots(figsize=(5.6, 4.4))
Zs = [z for z, a in st]; Ns = [a - z for z, a in st]
ax.plot([0, 90], [0, 90], ':', color=ABU); ax.text(70, 66, 'N = Z', color=ABU, fontsize=8.5, rotation=40)
A_ = np.arange(2, 260); Z0 = (A_ / 2) / (1 + 0.0077 * A_ ** (2 / 3)); ax.plot(Z0, A_ - Z0, color=JG, lw=6, alpha=.35, label='lembah kestabilan (rumus massa)')
ax.scatter(Zs, Ns, s=10, color=BIRU, zorder=3, label='nuklida stabil (contoh)')
ax.annotate('kelebihan neutron:\npeluruhan β$^-$', (40, 75), (12, 95), fontsize=8, arrowprops=dict(arrowstyle='->', color=JGT), color=JGT)
ax.annotate('kelebihan proton:\nβ$^+$ / penangkapan elektron', (60, 62), (62, 30), fontsize=8, arrowprops=dict(arrowstyle='->', color=HIJ), color=HIJ)
ax.annotate('terlalu berat:\npeluruhan α', (92, 146), (55, 140), fontsize=8, arrowprops=dict(arrowstyle='->', color=TUA))
ax.set_xlim(0, 100); ax.set_ylim(0, 160); ax.set_xlabel('jumlah proton Z'); ax.set_ylabel('jumlah neutron N'); ax.legend(fontsize=7.5, loc='upper left')
simpan(f, 'a_pita')
# 2. energi ikat per nukleon
dat = {'$^2$H': (2, 1.112), '$^4$He': (4, 7.074), '$^6$Li': (6, 5.332), '$^{12}$C': (12, 7.680), '$^{16}$O': (16, 7.976), '$^{56}$Fe': (56, 8.790), '$^{62}$Ni': (62, 8.795), '$^{90}$Zr': (90, 8.710), '$^{120}$Sn': (120, 8.504), '$^{197}$Au': (197, 7.916), '$^{208}$Pb': (208, 7.867), '$^{235}$U': (235, 7.591), '$^{238}$U': (238, 7.570)}
f, ax = plt.subplots(figsize=(6.2, 3.4))
A = np.arange(10, 250); Zb = np.round((A / 2) / (1 + 0.0077 * A ** (2 / 3))).astype(int); Z0f = (A / 2) / (1 + 0.0077 * A ** (2 / 3)); B = (15.75 * A - 17.8 * A ** (2 / 3) - 0.711 * Z0f * (Z0f - 1) / A ** (1 / 3) - 23.7 * (A - 2 * Z0f) ** 2 / A) / A
ax.plot(A, B, color=ABU, lw=1.2, label='rumus massa semiempiris')
for k, (a, b) in dat.items():
    ax.plot(a, b, 'o', color=JGT if k in ('$^{56}$Fe', '$^{62}$Ni') else BIRU); dy = -.45 if k in ('$^6$Li', '$^2$H', '$^{62}$Ni', '$^{208}$Pb', '$^{238}$U') else .18
    dx = -14 if k == '$^{235}$U' else 4
    ax.text(a + dx, b + dy, k, fontsize=7.5)
ax.annotate('', (40, 8.55), (8, 6.6), arrowprops=dict(arrowstyle='->', color=HIJ)); ax.text(30, 6.9, 'fusi', color=HIJ, fontsize=9)
ax.annotate('fisi', (150, 8.4), (210, 8.5), arrowprops=dict(arrowstyle='->', color=JGT), color=JGT, fontsize=9, va='center')
ax.set_xlabel('nomor massa A'); ax.set_ylabel('energi ikat per nukleon (MeV)'); ax.set_ylim(.8, 9.4); ax.set_xlim(0, 250); ax.legend(fontsize=7.5, loc='lower right'); koma(ax)
simpan(f, 'a_energi')
# 3. deret uranium-238 pada peta N-Z
ch = [('U', 92, 238, 'a'), ('Th', 90, 234, 'b'), ('Pa', 91, 234, 'b'), ('U', 92, 234, 'a'), ('Th', 90, 230, 'a'), ('Ra', 88, 226, 'a'), ('Rn', 86, 222, 'a'), ('Po', 84, 218, 'a'), ('Pb', 82, 214, 'b'), ('Bi', 83, 214, 'b'), ('Po', 84, 214, 'a'), ('Pb', 82, 210, 'b'), ('Bi', 83, 210, 'b'), ('Po', 84, 210, 'a'), ('Pb', 82, 206, '')]
th = {238: '4,47 × 10$^9$ th', 226: '1600 th', 222: '3,8 hari', 206: 'stabil'}
f, ax = plt.subplots(figsize=(4.4, 7.4))
for i, (s, z, a, m) in enumerate(ch):
    n = a - z; c = '#f6d3b0' if a != 206 else '#9fd8a8'
    ax.add_patch(plt.Rectangle((z - .47, n - .47), .94, .94, fc=c, ec=TUA, lw=.8)); ax.text(z, n, f'$^{{{a}}}${s}', ha='center', va='center', fontsize=6.6)
    if a in th and not (s == 'U' and a == 234): ax.text(z + .6, n, th[a], ha='left', va='center', fontsize=6.5, color=JGT)
    if i + 1 < len(ch):
        s2, z2, a2, _ = ch[i + 1]; n2 = a2 - z2
        ax.annotate('', (z2, n2), (z, n), arrowprops=dict(arrowstyle='->', color=BIRU if m == 'a' else JGT, lw=1.3, shrinkA=13 if m == 'a' else 4, shrinkB=13 if m == 'a' else 4))
ax.set_xlim(80.8, 96.5); ax.set_ylim(122.5, 147); ax.set_xlabel('Z'); ax.set_ylabel('N'); ax.set_xticks(range(81, 94)); ax.set_aspect('equal')
ax.plot([], [], color=BIRU, label='α: Z − 2, N − 2'); ax.plot([], [], color=JGT, label='β$^-$: Z + 1, N − 1'); ax.legend(fontsize=7.5, loc='upper left')
simpan(f, 'b_deret')
# 4. kinetika peluruhan
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 2.9))
t = np.linspace(0, 5, 300); a1.plot(t, 100 * 0.5 ** t, color=BIRU)
for k in range(1, 5): a1.plot([k, k], [0, 100 * 0.5 ** k], ':', color=ABU); a1.text(k + .05, 100 * 0.5 ** k + 3, f'{100 * 0.5 ** k:g} %'.replace('.', ','), fontsize=7.5)
a1.set_xlabel('waktu (dalam waktu paruh)'); a1.set_ylabel('inti tersisa (%)'); koma(a1)
ty = np.linspace(0, 40000, 300); a2.plot(ty, 100 * 0.5 ** (ty / 5730), color=JGT)
a2.plot([5300], [100 * 0.5 ** (5300 / 5730)], 'o', color=TUA); a2.text(6300, 55, 'Ötzi ≈ 5300 tahun:\n53 % $^{14}$C tersisa', fontsize=7.5)
a2.set_xlabel('umur (tahun)'); a2.set_ylabel('$^{14}$C tersisa (%)'); a2.set_title('penanggalan radiokarbon (t$_{1/2}$ = 5730 th)', fontsize=8.8, color=TUA)
a2.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:,.0f}'.replace(',', ' '))); koma(a2, 'y')
simpan(f, 'b_kinetika')
# 5. hasil fisi (skematis)
A = np.arange(70, 166); y = 6.5 * np.exp(-((A - 95) / 6.5) ** 2) + 6.5 * np.exp(-((A - 139) / 6.5) ** 2) + .01
f, ax = plt.subplots(figsize=(5.6, 2.9)); ax.semilogy(A, y, color=BIRU)
ax.text(95, 8, '$^{90}$Sr, $^{92}$Kr, $^{99}$Mo', ha='center', fontsize=7.5); ax.text(139, 8, '$^{131}$I, $^{137}$Cs, $^{141}$Ba', ha='center', fontsize=7.5)
ax.set_ylim(.005, 20); ax.set_xlabel('nomor massa produk fisi A'); ax.set_ylabel('hasil per fisi (%)'); ax.set_title('fisi $^{235}$U oleh neutron termal (skematis)', fontsize=8.8, color=TUA)
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',')))
simpan(f, 'c_fisi')
# 6. dosis
lab = ['makan satu pisang', 'foto rontgen gigi', 'penerbangan 7 jam', 'foto rontgen dada', 'latar alam per tahun (rata-rata dunia)', 'CT perut', 'batas pekerja radiasi per tahun', 'gejala radiasi akut', 'fatal bagi ≈ 50 % tanpa perawatan']
mSv = [0.0001, 0.005, 0.03, 0.1, 2.4, 8, 20, 1000, 4500]
f, ax = plt.subplots(figsize=(6.4, 3.4)); ax.barh(range(len(lab)), mSv, color=[HIJ] * 4 + [BIRU] * 3 + [JGT] * 2, edgecolor=TUA); ax.set_xscale('log')
ax.set_yticks(range(len(lab))); ax.set_yticklabels(lab, fontsize=8); ax.set_xlabel('dosis efektif (mSv, skala log)'); ax.set_xlim(5e-5, 2e4)
for i, v in enumerate(mSv): ax.text(v * 1.3, i, f'{v:g}'.replace('.', ','), va='center', fontsize=7)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',')))
simpan(f, 'd_dosis')
