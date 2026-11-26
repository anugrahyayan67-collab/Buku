#!/usr/bin/env python3
# Gambar Bab 12 Kimia Anorganik 1: hidrogen dan gas mulia -> bab12/fig/*.png
import os, math, random, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.ticker import FuncFormatter
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab12', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
def koma(ax, sb='xy'):
    fm = FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−'))
    if 'x' in sb: ax.xaxis.set_major_formatter(fm)
    if 'y' in sb: ax.yaxis.set_major_formatter(fm)
cm = 0.0119626
# 1. kurva potensial H2/D2 dan orto/para
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.0))
De = 458.0; re = 74.1; we = 4401.2
a = (we * cm * 1e-3) / 1  # tidak dipakai
k = (2 * math.pi * 2.998e10 * we) ** 2 * (1.008 / 2 * 1.6605e-27)  # N/m
beta = math.sqrt(k / (2 * De * 1000 / 6.022e23)) * 1e-12  # per pm
r = np.linspace(45, 300, 400); V = De * (1 - np.exp(-beta * (r - re))) ** 2 - De
a1.plot(r, V, color=TUA)
for nm, w, c in [('H$_2$', 4401.2, JGT), ('D$_2$', 3115.5, BIRU)]:
    E0 = -De + .5 * w * cm; x1 = re - math.log(1 + math.sqrt((E0 + De) / De)) / beta; x2 = re - math.log(1 - math.sqrt((E0 + De) / De)) / beta
    a1.plot([x1, x2], [E0, E0], color=c, lw=2); a1.text(x2 + 4, E0 + (4 if nm[0] == 'H' else -16), f'{nm}: ZPE {0.5 * w * cm:.1f} kJ mol$^{{-1}}$'.replace('.', ','), fontsize=7.5, color=c)
a1.axhline(0, color=ABU, ls=':', lw=.8); a1.set_xlim(40, 300); a1.set_ylim(-480, 60); a1.set_xlabel('jarak H–H (pm)'); a1.set_ylabel('energi (kJ mol$^{-1}$)'); koma(a1)
a1.set_title('tingkat titik nol: D$_2$ lebih rendah', fontsize=8.8, color=TUA)
B = 60.853
def fp(T):
    pa = sum((2 * J + 1) * math.exp(-B * J * (J + 1) * 1.4388 / T) for J in range(0, 30, 2)); o = 3 * sum((2 * J + 1) * math.exp(-B * J * (J + 1) * 1.4388 / T) for J in range(1, 30, 2)); return pa / (pa + o)
T = np.linspace(10, 350, 300); a2.plot(T, [100 * fp(t) for t in T], color=BIRU); a2.axhline(25, color=ABU, ls=':', lw=.8)
a2.axvline(20.3, color=JGT, ls='--', lw=.8); a2.text(24, 85, 'titik didih\n20,3 K', fontsize=7.5, color=JGT); a2.text(250, 28, '25 %', fontsize=8, color=ABU)
a2.set_xlabel('suhu (K)'); a2.set_ylabel('para-H$_2$ setimbang (%)'); a2.set_ylim(0, 105); koma(a2); a2.set_title('orto- dan para-hidrogen', fontsize=8.8, color=TUA)
simpan(f, 'a_isotop')
# 2. jenis hidrida pada tabel periodik
ele = {'H': (1, 1), 'Li': (2, 1), 'Be': (2, 2), 'B': (2, 13), 'C': (2, 14), 'N': (2, 15), 'O': (2, 16), 'F': (2, 17), 'Na': (3, 1), 'Mg': (3, 2), 'Al': (3, 13), 'Si': (3, 14), 'P': (3, 15), 'S': (3, 16), 'Cl': (3, 17),
       'K': (4, 1), 'Ca': (4, 2), 'Ga': (4, 13), 'Ge': (4, 14), 'As': (4, 15), 'Se': (4, 16), 'Br': (4, 17), 'Rb': (5, 1), 'Sr': (5, 2), 'In': (5, 13), 'Sn': (5, 14), 'Sb': (5, 15), 'Te': (5, 16), 'I': (5, 17), 'Cs': (6, 1), 'Ba': (6, 2), 'Tl': (6, 13), 'Pb': (6, 14), 'Bi': (6, 15)}
tm = ['Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'La', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg']
for i, e in enumerate(tm): ele[e] = (4 + i // 10, 3 + i % 10)
ion = {'Li', 'Na', 'K', 'Rb', 'Cs', 'Ca', 'Sr', 'Ba'}; per = {'Be', 'Mg'}; log_ = {'Sc', 'Ti', 'V', 'Cr', 'Y', 'Zr', 'Nb', 'La', 'Hf', 'Ta', 'Pd', 'Ni'}
f, ax = plt.subplots(figsize=(7.6, 3.4))
for e, (p, g) in ele.items():
    if e == 'H': c = '#ffffff'
    elif e in ion: c = JG
    elif e in per: c = '#f6d3b0'
    elif e in log_: c = '#9fd8a8'
    elif g >= 13 or e in ('Zn', 'Cd', 'Hg', 'Cu', 'Ag', 'Au'): c = MUDA if g >= 13 else '#e3e6ea'
    else: c = '#e3e6ea'
    ax.add_patch(plt.Rectangle((g, -p), .94, .94, fc=c, ec=TUA, lw=.6)); ax.text(g + .47, -p + .47, e, ha='center', va='center', fontsize=7.5)
for i, (c, t) in enumerate([(JG, 'ionik (salin)'), ('#f6d3b0', 'peralihan (polimer)'), ('#9fd8a8', 'logam / interstisi'), (MUDA, 'kovalen molekular'), ('#e3e6ea', 'tidak ada hidrida biner stabil / tidak jelas')]):
    xx = 1 + (i % 3) * 5.4; yy = -6.75 - (i // 3) * .6; ax.add_patch(plt.Rectangle((xx, yy), .5, .4, fc=c, ec=TUA, lw=.6)); ax.text(xx + .65, yy + .2, t, va='center', fontsize=7.5)
ax.set_xlim(.9, 18.1); ax.set_ylim(-7.5, 0); ax.axis('off')
simpan(f, 'b_jenis')
# 3. entalpi pembentukan hidrida blok p
g_ = ['14', '15', '16', '17']; Hf = [[-74.6, -45.9, -241.8, -273.3], [34.3, 5.4, -20.6, -92.3], [90.8, 66.4, 29.7, -36.3], [162.8, 145.1, 99.6, 26.5]]
nm = [['CH$_4$', 'NH$_3$', 'H$_2$O', 'HF'], ['SiH$_4$', 'PH$_3$', 'H$_2$S', 'HCl'], ['GeH$_4$', 'AsH$_3$', 'H$_2$Se', 'HBr'], ['SnH$_4$', 'SbH$_3$', 'H$_2$Te', 'HI']]
f, ax = plt.subplots(figsize=(5.4, 3.3)); A = np.array(Hf)
im = ax.imshow(A, cmap='RdBu_r', vmin=-280, vmax=280)
for i in range(4):
    for j in range(4): ax.text(j, i, nm[i][j] + '\n' + f'{A[i, j]:+.1f}'.replace('.', ',').replace('-', '−'), ha='center', va='center', fontsize=8, color='white' if abs(A[i, j]) > 170 else TUA)
ax.set_xticks(range(4)); ax.set_xticklabels(g_); ax.set_xlabel('golongan'); ax.set_yticks(range(4)); ax.set_yticklabels(['periode 2', 'periode 3', 'periode 4', 'periode 5'])
cb = f.colorbar(im, ax=ax, shrink=.85); cb.set_label('Δ$_f$H° (kJ mol$^{-1}$, gas)'); cb.ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('-', '−')))
simpan(f, 'b_entalpi')
# 4. kerapatan energi
lab = ['H$_2$ 700 bar', 'H$_2$ cair', 'LaNi$_5$H$_6$', 'metanol', 'bensin', 'baterai Li-ion']; mj_kg = [120.0, 120.0, 1.65, 19.9, 44.4, 0.9]; mj_l = [4.8, 8.5, 13.9, 15.8, 33.1, 2.5]
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 2.8))
a1.barh(range(6), mj_kg, color=[BIRU, BIRU, HIJ, JG, JGT, ABU], edgecolor=TUA); a1.set_yticks(range(6)); a1.set_yticklabels(lab); a1.set_xlabel('MJ per kg'); a1.set_xscale('log'); a1.set_title('per massa (bahan bakar saja)', fontsize=8.8, color=TUA)
a2.barh(range(6), mj_l, color=[BIRU, BIRU, HIJ, JG, JGT, ABU], edgecolor=TUA); a2.set_yticks([]); a2.set_xlabel('MJ per liter'); a2.set_title('per volume', fontsize=8.8, color=TUA)
for ax, v in [(a1, mj_kg), (a2, mj_l)]:
    for i, x in enumerate(v): ax.text(x * (1.08 if ax is a1 else 1) + (0 if ax is a1 else .5), i, f'{x:g}'.replace('.', ','), va='center', fontsize=7.5)
a2.set_xlim(0, 40); a1.set_xlim(.5, 600)
a1.xaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',')))
simpan(f, 'b_energi')
# 5. lapisan es Ih (proyeksi heksagonal) dengan aturan es
random.seed(3)
a_ = 1.0; pts = {}; edges = []
for i in range(-3, 4):
    for j in range(-3, 4):
        x0 = i * 1.5 * a_ * 2 / 2 * 1; 
for i in range(-6, 7):
    for j in range(-6, 7):
        bx, by = i * 1.5, i * math.sqrt(3) / 2 + j * math.sqrt(3)
        pts[(round(bx, 3), round(by, 3))] = 1; pts[(round(bx + 1, 3), round(by, 3))] = 1
P = [p for p in pts if abs(p[0]) < 4.6 and abs(p[1]) < 3.3]; S = set(P)
for p in P:
    for q in P:
        if p < q and abs(math.dist(p, q) - 1) < 1e-2: edges.append((p, q))
# arah ikatan: setiap O memberi 1 atau 2 H dalam bidang (ikatan ke-4 keluar bidang)
for trial in range(5000):
    dirs = {e: random.random() < .5 for e in edges}; cnt = {p: 0 for p in P}; deg = {p: 0 for p in P}
    for (p, q), d in dirs.items(): cnt[p if d else q] += 1; deg[p] += 1; deg[q] += 1
    if all((1 <= cnt[p] <= 2) if deg[p] == 3 else cnt[p] <= 2 for p in P): break
f, ax = plt.subplots(figsize=(5.6, 4.0))
for (p, q), d in dirs.items():
    don, acc = (p, q) if d else (q, p); ax.plot([p[0], q[0]], [p[1], q[1]], color=ABU, ls=':', lw=1)
    hx, hy = don[0] + .32 * (acc[0] - don[0]), don[1] + .32 * (acc[1] - don[1]); ax.plot([don[0], hx], [don[1], hy], color=TUA, lw=1.6); ax.add_patch(Circle((hx, hy), .09, fc='white', ec=TUA, lw=.8, zorder=4))
for p in P: ax.add_patch(Circle(p, .16, fc='#d2553b', ec=TUA, zorder=5))
ax.set_xlim(-4.8, 4.8); ax.set_ylim(-3.4, 3.4); ax.set_aspect('equal'); ax.axis('off')
simpan(f, 'c_es')
# 6. massa jenis air
T = [-10, -5, 0, 2, 4, 6, 8, 10, 15, 20, 30, 40, 60, 80, 100]; rho = [0.99815, 0.99930, 0.99984, 0.99994, 0.99997, 0.99994, 0.99985, 0.99970, 0.99910, 0.99820, 0.99565, 0.99222, 0.98320, 0.97179, 0.95835]
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 2.9))
a1.plot(T, rho, 'o-', color=BIRU, ms=3); a1.axhline(0.9167, color=JGT, ls='--'); a1.text(40, .9195, 'es Ih pada 0 °C: 0,917', color=JGT, fontsize=8)
a1.set_xlabel('suhu (°C)'); a1.set_ylabel('massa jenis (g cm$^{-3}$)'); a1.set_ylim(.905, 1.005); koma(a1)
a2.plot(T[:9], rho[:9], 'o-', color=BIRU, ms=4); a2.axvline(3.98, color=HIJ, ls=':'); a2.text(4.3, .9983, 'maksimum\n3,98 °C', color=HIJ, fontsize=8)
a2.axvspan(-10, 0, color=MUDA, alpha=.25); a2.text(-9.5, .99995, 'lewat dingin', fontsize=7.5, color=BIRU)
a2.set_xlabel('suhu (°C)'); a2.set_ylabel('massa jenis (g cm$^{-3}$)'); koma(a2); a2.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:.4f}'.replace('.', ',')))
simpan(f, 'c_air')
# 7. gas mulia: energi ionisasi dan titik didih
g = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']; IE = [2372, 2081, 1521, 1351, 1170, 1037]; bp = [4.22, 27.1, 87.3, 119.9, 165.1, 211]
f, a1 = plt.subplots(figsize=(5.8, 3.0)); a1.plot(range(6), IE, 'o-', color=BIRU); a1.set_ylabel('energi ionisasi pertama (kJ mol$^{-1}$)', color=BIRU); a1.set_xticks(range(6)); a1.set_xticklabels(g)
a1.axhline(1165, color=HIJ, ls='--', lw=1); a1.text(2.3, 1185, 'O$_2$ → O$_2^+$: 1165', color=HIJ, fontsize=8)
a2 = a1.twinx(); a2.plot(range(6), bp, 's--', color=JGT); a2.set_ylabel('titik didih (K)', color=JGT); koma(a1, 'y'); koma(a2, 'y')
simpan(f, 'd_gasmulia')
# 8. bentuk senyawa xenon
def proj(v, th=np.radians(30), ph=np.radians(22)):
    x, y, z = v; x1 = x * np.cos(th) - y * np.sin(th); y1 = x * np.sin(th) + y * np.cos(th); return np.array([x1, z * np.cos(ph) - y1 * np.sin(ph)]), y1 * np.cos(ph) + z * np.sin(ph)
def mol(ax, lig, lp, t):
    items = sorted([(proj(v)[1], v, c, s) for v, c, s in lig], key=lambda a: a[0])
    for d, v, c, s in items:
        p, _ = proj(v); ax.plot([0, p[0]], [0, p[1]], color=ABU, lw=2.2, zorder=2 + d)
    for v in lp:
        p, d = proj(np.array(v) * .75); ax.add_patch(matplotlib.patches.Ellipse((p[0] * .8, p[1] * .8), .55, .3, angle=np.degrees(np.arctan2(p[1], p[0])), fc='#e9b949', ec='none', alpha=.45, zorder=1))
    ax.add_patch(Circle((0, 0), .24, fc='#5b86e5', ec=TUA, zorder=5)); ax.text(0, 0, 'Xe', ha='center', va='center', fontsize=7.5, color='white', zorder=6)
    for d, v, c, s in items:
        p, _ = proj(v); ax.add_patch(Circle(p, .16, fc=c, ec=TUA, zorder=6 + d)); ax.text(p[0], p[1], s, ha='center', va='center', fontsize=6.5, zorder=6.1 + d)
    ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.35, 1.35); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(t, fontsize=8.5, color=TUA)
F_, O_ = '#9fd8a8', '#e8806b'
ex = [(1, 0, 0), (-.5, .866, 0), (-.5, -.866, 0)]
f, axs = plt.subplots(1, 5, figsize=(8.2, 2.0))
mol(axs[0], [((0, 0, 1), F_, 'F'), ((0, 0, -1), F_, 'F')], ex, 'XeF$_2$: linear')
mol(axs[1], [((1, 0, 0), F_, 'F'), ((-1, 0, 0), F_, 'F'), ((0, 1, 0), F_, 'F'), ((0, -1, 0), F_, 'F')], [(0, 0, 1), (0, 0, -1)], 'XeF$_4$: bujur sangkar')
mol(axs[2], [((0, 0, 1), O_, 'O'), ((1, 0, 0), F_, 'F'), ((-1, 0, 0), F_, 'F'), ((0, 1, 0), F_, 'F'), ((0, -1, 0), F_, 'F')], [(0, 0, -1)], 'XeOF$_4$: piramida\nbujur sangkar')
tp = [(0.94 * np.cos(a), 0.94 * np.sin(a), -.33) for a in np.radians([90, 210, 330])]
mol(axs[3], [(v, O_, 'O') for v in tp], [(0, 0, 1)], 'XeO$_3$: piramida\nsegitiga')
td = [np.array(v) / math.sqrt(3) for v in [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]]
mol(axs[4], [(v, O_, 'O') for v in td], [], 'XeO$_4$: tetrahedral')
simpan(f, 'd_xenon')
