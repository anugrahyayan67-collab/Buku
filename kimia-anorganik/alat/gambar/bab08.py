#!/usr/bin/env python3
# Gambar Bab 8 Kimia Anorganik 1: asam dan basa. -> bab08/fig/*.png
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab08', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
from matplotlib.ticker import FuncFormatter
def koma(ax, sb='xy'):
    fm = FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−'))
    if 'x' in sb: ax.xaxis.set_major_formatter(fm)
    if 'y' in sb: ax.yaxis.set_major_formatter(fm)
def sub(s):
    import re; return re.sub(r'(\d+)', r'$_{\1}$', s)
# 1. Delta G terhadap T untuk NH3 + HCl -> NH4Cl
T = np.linspace(250, 800, 100); dG = -176.2 + T * 0.2851
f, ax = plt.subplots(figsize=(5.6, 2.9)); ax.plot(T, dG, color=BIRU, lw=2); ax.axhline(0, color=TUA, lw=.8)
ax.plot([618], [0], 'o', color=JGT); ax.annotate('618 K (345 °C)', (618, 0), (450, 40), fontsize=9, arrowprops=dict(arrowstyle='->', color=ABU))
ax.text(280, -95, 'NH$_4$Cl terbentuk spontan', fontsize=8.5, color=BIRU); ax.text(640, 25, 'NH$_4$Cl terurai', fontsize=8.5, color=JGT)
ax.set_xlabel('suhu (K)'); ax.set_ylabel('Δ$_r$$G$° (kJ mol$^{-1}$)'); koma(ax)
simpan(f, 'a_dg')
# 2. aturan Pauling
ok = [('HOCl', 0, 7.53), ('HClO$_2$', 1, 1.96), ('HClO$_3$', 2, -1.0), ('HClO$_4$', 3, -10), ('H$_3$PO$_4$', 1, 2.15), ('H$_2$SO$_4$', 2, -3), ('H$_2$SO$_3$', 1, 1.86), ('HNO$_3$', 2, -1.4),
      ('HNO$_2$', 1, 3.25), ('B(OH)$_3$', 0, 9.24), ('Si(OH)$_4$', 0, 9.8), ('HOI', 0, 10.6), ('HOBr', 0, 8.65), ('H$_5$IO$_6$', 1, 3.29), ('H$_3$AsO$_4$', 1, 2.26)]
f, ax = plt.subplots(figsize=(6.0, 3.6)); from collections import defaultdict
cnt = defaultdict(int); tot = defaultdict(int)
for o in ok: tot[o[1]] += 1
p = []
for o in ok: p.append(o[1] + (cnt[o[1]] - (tot[o[1]] - 1) / 2) * .16); cnt[o[1]] += 1
p = np.array(p); pk = [o[2] for o in ok]
ax.scatter(p, pk, color=JGT, zorder=3); ax.plot([-.3, 3.3], [8 + 1.5, 8 - 5 * 3.3], color=BIRU, lw=1.5, label='aturan Pauling: p$K_a$ ≈ 8 − 5$p$')
for k, ((nm, _, y), x) in enumerate(zip(ok, p)): ax.text(x, y + (.45 if k % 2 else -.95), nm, fontsize=6.3, color=TUA, ha='center')
ax.set_xlabel('$p$ = jumlah O yang tidak terikat H'); ax.set_ylabel('p$K_{a1}$ terukur'); ax.set_xticks([0, 1, 2, 3]); ax.legend(fontsize=8.5); koma(ax)
simpan(f, 'b_pauling')
# 3. asam aqua
aq = [('Na$^+$', .98, 14.8), ('Ca$^{2+}$', 4.0, 12.8), ('Mg$^{2+}$', 5.56, 11.4), ('Zn$^{2+}$', 5.41, 9.0), ('Fe$^{2+}$', 5.13, 9.5), ('Cu$^{2+}$', 5.48, 7.5), ('Al$^{3+}$', 16.8, 5.0),
      ('Cr$^{3+}$', 14.6, 4.0), ('Fe$^{3+}$', 13.95, 2.2), ('Sc$^{3+}$', 12.1, 4.3), ('Be$^{2+}$', 8.9, 5.7), ('Hg$^{2+}$', 3.92, 3.4)]
f, ax = plt.subplots(figsize=(5.8, 3.3))
for nm, x, y in aq:
    c = JGT if nm.startswith(('Hg', 'Cu', 'Fe$^{3', 'Cr')) else BIRU
    ax.scatter(x, y, color=c, zorder=3); ax.text(x + .25, y + .2, nm, fontsize=8, color=TUA)
ax.set_xlabel('$z^2/r$ (× 100 pm$^{-1}$)'); ax.set_ylabel('p$K_a$ ion aqua'); koma(ax); ax.set_xlim(0, 19)
ax.text(10.5, 13, 'biru: ion bergaris lurus\njingga: ion d dengan karakter\nkovalen (lebih asam)', fontsize=7.8, color=TUA)
simpan(f, 'b_aqua')
# 4. sifat oksida golongan utama
el = [['Li', 'Be', 'B', 'C', 'N', '', ''], ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl'], ['K', 'Ca', 'Ga', 'Ge', 'As', 'Se', 'Br'], ['Rb', 'Sr', 'In', 'Sn', 'Sb', 'Te', 'I'], ['Cs', 'Ba', 'Tl', 'Pb', 'Bi', 'Po', '']]
sif = [['b', 'a', 'x', 'x', 'x', '', ''], ['b', 'b', 'a', 'x', 'x', 'x', 'x'], ['b', 'b', 'a', 'a', 'x', 'x', 'x'], ['b', 'b', 'a', 'a', 'a', 'a', 'x'], ['b', 'b', 'b', 'a', 'b', 'a', '']]
col = {'b': BIRU, 'a': HIJ, 'x': JGT}
f, ax = plt.subplots(figsize=(5.8, 3.3))
for i, row in enumerate(el):
    for j, e in enumerate(row):
        if not e: continue
        ax.add_patch(Rectangle((j, -i), .92, .92, fc=col[sif[i][j]], ec='white', alpha=.85)); ax.text(j + .46, -i + .46, e, ha='center', va='center', color='white', fontsize=10, fontweight='bold')
for k, (t, c) in enumerate([('oksida basa', BIRU), ('amfoter', HIJ), ('oksida asam', JGT)]):
    ax.add_patch(Rectangle((7.3, -k * .7 - .3), .4, .4, fc=c)); ax.text(7.8, -k * .7 - .1, t, va='center', fontsize=9)
ax.set_xlim(-.1, 9.6); ax.set_ylim(-4.2, 1.1); ax.axis('off'); ax.set_aspect('equal')
ax.text(3.5, 1.0, 'golongan 1, 2, 13–17 (oksida yang paling umum)', ha='center', fontsize=8.5, color=TUA)
simpan(f, 'b_oksida')
# 5. jendela pelarut (leveling)
f, ax = plt.subplots(figsize=(6.6, 2.6))
win = [('air', -1.7, 15.7, BIRU), ('asam asetat', -6, 7, JGT), ('amonia cair', 9, 32, HIJ), ('DMSO', 1, 35, ABU)]
for k, (nm, a, b, c) in enumerate(win):
    ax.add_patch(Rectangle((a, k), b - a, .6, fc=c, alpha=.6, ec=TUA)); ax.text(a - .6, k + .3, nm, ha='right', va='center', fontsize=9)
ax.set_xlim(-22, 40); ax.set_ylim(-.3, 4.2); ax.set_yticks([]); ax.set_xlabel('p$K_a$ (skala air), asam lebih kuat di kiri'); koma(ax, 'x')
for x, l in [(-10, 'HClO$_4$'), (-3, 'H$_2$SO$_4$'), (3.2, 'HF'), (9.2, 'NH$_4^+$'), (15.7, 'H$_2$O'), (35, 'NH$_3$')]:
    ax.plot([x, x], [-.3, 4.0], color=ABU, lw=.6, ls=':'); ax.text(x, 4.0, l, ha='center', fontsize=7.5, color=TUA)
for s_ in ('top', 'right', 'left'): ax.spines[s_].set_visible(False)
simpan(f, 'b_pelarut')
# 6. kekerasan absolut
cat = [('Al$^{3+}$', 45.8), ('Li$^+$', 35.1), ('Mg$^{2+}$', 32.6), ('Na$^+$', 21.1), ('Ca$^{2+}$', 19.5), ('K$^+$', 13.6), ('Fe$^{3+}$', 12.1), ('Zn$^{2+}$', 10.9), ('Pb$^{2+}$', 8.5), ('Hg$^{2+}$', 7.7), ('Ag$^+$', 7.0), ('Cu$^+$', 6.3), ('Au$^+$', 5.5)]
an = [('F$^-$', 7.0), ('H$^-$', 6.4), ('OH$^-$', 5.6), ('CN$^-$', 5.1), ('Cl$^-$', 4.7), ('Br$^-$', 4.2), ('SH$^-$', 4.0), ('I$^-$', 3.7)]
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.0), gridspec_kw={'width_ratios': [1.6, 1]})
a1.bar(range(len(cat)), [v for _, v in cat], color=[BIRU if v > 11 else JGT for _, v in cat], edgecolor=TUA); a1.set_xticks(range(len(cat))); a1.set_xticklabels([n for n, _ in cat], fontsize=7.5, rotation=0)
a1.set_ylabel('η (eV)'); a1.set_title('kation (asam)', fontsize=9.5, color=TUA); koma(a1, 'y')
a2.bar(range(len(an)), [v for _, v in an], color=[BIRU if v > 5.5 else JGT for _, v in an], edgecolor=TUA); a2.set_xticks(range(len(an))); a2.set_xticklabels([n for n, _ in an], fontsize=7.5)
a2.set_title('anion (basa)', fontsize=9.5, color=TUA); koma(a2, 'y')
simpan(f, 'c_keras')
# 7. Drago–Wayland: urutan basa bergantung asam
basa = ['Et$_2$O', 'DMSO', 'NH$_3$', 'piridina', 'Me$_3$N']; EB = [.963, 1.34, 1.36, 1.17, .808]; CB = [3.25, 2.85, 3.46, 6.40, 11.54]
f, ax = plt.subplots(figsize=(6.0, 3.0)); x = np.arange(5)
for k, (nm, EA, CA, c) in enumerate([('I$_2$ (lunak: $C_A$ besar)', 1.0, 1.0, JGT), ('fenol (keras: $E_A$ besar)', 4.33, .442, BIRU)]):
    v = [(EA * e + CA * cc) * 4.184 for e, cc in zip(EB, CB)]; ax.bar(x + (k - .5) * .38, v, .38, color=c, alpha=.85, label=nm, edgecolor=TUA)
ax.set_xticks(x); ax.set_xticklabels(basa); ax.set_ylabel('−Δ$H$ ramalan (kJ mol$^{-1}$)'); ax.legend(fontsize=8); koma(ax, 'y')
simpan(f, 'c_drago')
# 8. situs asam zeolit
f, ax = plt.subplots(figsize=(6.2, 2.6)); ax.set_aspect('equal'); ax.axis('off')
xs = [0, 2, 4, 6]; lab = ['Si', 'Si', 'Al', 'Si']
for x, l in zip(xs, lab):
    ax.add_patch(Circle((x, 0), .32, fc=MUDA if l == 'Si' else JG, ec=TUA)); ax.text(x, 0, l, ha='center', va='center', fontsize=10, fontweight='bold')
    for dy in (1, -1): ax.plot([x, x], [dy * .32, dy * .85], color=ABU, lw=2); ax.add_patch(Circle((x, dy * 1.05), .2, fc='#d2553b', ec=TUA)); ax.text(x + .28, dy * 1.05, 'O', fontsize=8, va='center')
for a, b in zip(xs[:-1], xs[1:]):
    m = (a + b) / 2; ax.plot([a + .32, m - .2], [0, 0], color=ABU, lw=2); ax.plot([m + .2, b - .32], [0, 0], color=ABU, lw=2); ax.add_patch(Circle((m, 0), .2, fc='#d2553b', ec=TUA))
ax.plot([3, 3], [.2, .62], color=ABU, lw=2); ax.add_patch(Circle((3, .78), .16, fc='white', ec=TUA)); ax.text(3, .78, 'H', ha='center', va='center', fontsize=8, fontweight='bold')
ax.text(3, 1.35, 'situs asam Brønsted Si–O(H)–Al', ha='center', fontsize=9, color=JGT); ax.text(4, -1.6, 'Al menggantikan Si: kerangka bermuatan −1, diimbangi H$^+$', ha='center', fontsize=8.5, color=TUA)
ax.set_xlim(-.8, 6.8); ax.set_ylim(-1.9, 1.6)
simpan(f, 'c_zeolit')
