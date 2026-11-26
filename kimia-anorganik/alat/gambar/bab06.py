#!/usr/bin/env python3
# Gambar Bab 6 Kimia Anorganik 1: energetika padatan ionik. -> bab06/fig/*.png
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab06', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
from matplotlib.ticker import FuncFormatter
def koma(ax, sb='xy'):
    fm = FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−'))
    if 'x' in sb: ax.xaxis.set_major_formatter(fm)
    if 'y' in sb: ax.yaxis.set_major_formatter(fm)
K = 138935.5; A = 1.74756; n = 8; r0 = 282.0
# 1. energi terhadap jarak untuk NaCl
r = np.linspace(180, 700, 400); tarik = -K * A / r; B = K * A * r0**(n - 1) / n; tolak = B / r**n
f, ax = plt.subplots(figsize=(6.0, 3.6))
ax.plot(r, tarik, color=BIRU, lw=1.6, ls='--', label=r'tarikan Coulomb $\propto -1/r$'); ax.plot(r, tolak, color=JGT, lw=1.6, ls='--', label=r'tolakan $\propto 1/r^n$')
ax.plot(r, tarik + tolak, color=TUA, lw=2.2, label='total'); ax.axhline(0, color=ABU, lw=.7)
U0 = -K * A / r0 * (1 - 1 / n); ax.plot([r0], [U0], 'o', color=TUA); ax.annotate(f'$r_0$ = 282 pm\n$U$ = −753 kJ mol$^{{-1}}$', (r0, U0), (370, -1150), fontsize=8.5, arrowprops=dict(arrowstyle='->', color=ABU))
ax.set_ylim(-1400, 900); ax.set_xlabel('jarak Na–Cl, $r$ (pm)'); ax.set_ylabel('energi (kJ mol$^{-1}$)'); ax.legend(fontsize=8.3, loc='upper right'); koma(ax)
simpan(f, 'a_energi')
# 2. konvergensi tetapan Madelung: kulit demi kulit lawan kubus Evjen
def evjen(N):
    rr = np.arange(-N, N + 1); X, Y, Z = np.meshgrid(rr, rr, rr, indexing='ij'); q = (-1.0) ** (np.abs(X) + np.abs(Y) + np.abs(Z)); w = np.ones_like(X, float)
    for Q in (X, Y, Z): w *= np.where(np.abs(Q) == N, .5, 1.)
    d = np.sqrt(X**2 + Y**2 + Z**2); m = d > 0; return -(q[m] * w[m] / d[m]).sum()
N = 8; rr = np.arange(-N, N + 1); X, Y, Z = np.meshgrid(rr, rr, rr, indexing='ij'); d2 = (X**2 + Y**2 + Z**2).ravel(); q = ((-1.0) ** (np.abs(X) + np.abs(Y) + np.abs(Z))).ravel()
kul = sorted(set(d2[d2 > 0]))[:25]; s = 0; ps = []
for k in kul: s += -(q[d2 == k] / np.sqrt(k)).sum(); ps.append(s)
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.0))
a1.plot(range(1, len(ps) + 1), ps, 'o-', color=JGT, ms=4); a1.axhline(1.74756, color=TUA, ls='--', lw=1); a1.set_xlabel('jumlah kulit tetangga'); a1.set_ylabel('jumlah parsial'); a1.set_title('kulit demi kulit: berayun liar', fontsize=9.5, color=TUA); koma(a1, 'y')
Ns = range(1, 11); a2.plot(Ns, [evjen(k) for k in Ns], 'o-', color=BIRU, ms=4); a2.axhline(1.74756, color=TUA, ls='--', lw=1); a2.text(5, 1.70, '1,74756', color=TUA, fontsize=9)
a2.set_xlabel('ukuran kubus Evjen, $N$'); a2.set_title('kubus netral (Evjen): cepat konvergen', fontsize=9.5, color=TUA); a2.set_ylim(1.4, 1.8); koma(a2, 'y')
simpan(f, 'a_madelung')
# 3. siklus Born-Haber NaCl
f, ax = plt.subplots(figsize=(6.4, 4.6))
lv = [('Na(s) + ½Cl$_2$(g)', 0, 0), ('Na(g) + ½Cl$_2$(g)', 107.5, 0), ('Na(g) + Cl(g)', 229.2, 0), ('Na$^+$(g) + e$^-$ + Cl(g)', 725.0, 0),
      ('Na$^+$(g) + Cl$^-$(g)', 376.4, 1), ('NaCl(s)', -411.2, 1)]
X = {0: 0, 1: 2.2}
for nm, y, c in lv:
    ax.plot([X[c], X[c] + 1.6], [y, y], color=TUA, lw=2); ax.text(X[c] + .8, y + 14, nm, ha='center', fontsize=8.5, color=TUA)
def pan(x, y1, y2, t, c=BIRU, kanan=True):
    ax.annotate('', (x, y2), (x, y1), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.5)); ax.text(x + (.06 if kanan else -.06), (y1 + y2) / 2, t, fontsize=8.2, color=c, va='center', ha='left' if kanan else 'right')
pan(-.15, 0, 107.5, 'sublimasi Na +107,5', kanan=False); pan(-.15, 107.5, 229.2, '½ D(Cl–Cl) +121,7', kanan=False); pan(.3, 229.2, 725.0, 'energi ionisasi Na\n+495,8')
pan(2.5, 725.0, 376.4, 'afinitas elektron Cl\n−348,6', JGT); pan(3.5, 376.4, -411.2, 'kisi terbentuk\n−787,6', JGT)
pan(1.55, 0, -411.2, 'Δ$_f$$H$°\n−411,2', HIJ, kanan=False)
ax.set_xlim(-2.0, 4.6); ax.set_ylim(-470, 800); ax.set_ylabel('entalpi (kJ mol$^{-1}$)'); ax.set_xticks([]); koma(ax, 'y')
for s_ in ('top', 'right', 'bottom'): ax.spines[s_].set_visible(False)
simpan(f, 'b_bornhaber')
# 4. hitung lawan siklus
nm = ['LiF', 'NaF', 'NaCl', 'NaI', 'KCl', 'CsCl', 'CsI', 'AgF', 'AgCl', 'AgBr', 'AgI']
bl = [1005, 898, 753, 671, 686, 620, 567, 871, 783, 758, 735]; cy = [1049, 930, 787, 705, 717, 659, 604, 974, 918, 905, 892]
f, ax = plt.subplots(figsize=(6.6, 3.2)); x = np.arange(len(nm))
ax.bar(x - .2, bl, .4, color=MUDA, edgecolor=BIRU, label='Born–Landé (model ionik)'); ax.bar(x + .2, cy, .4, color=JG, edgecolor=JGT, label='siklus Born–Haber')
for i in range(len(nm)): ax.text(x[i], cy[i] + 15, f'{100*(cy[i]-bl[i])/cy[i]:.0f} %', ha='center', fontsize=7.5, color=TUA)
ax.set_xticks(x); ax.set_xticklabels(nm, fontsize=8.5); ax.set_ylabel('entalpi kisi (kJ mol$^{-1}$)'); ax.set_ylim(0, 1150); ax.legend(fontsize=8, ncol=2, loc='lower center', bbox_to_anchor=(.5, 1.0), frameon=False); koma(ax, 'y')
simpan(f, 'b_banding')
# 5. senyawa hipotetis magnesium klorida
f, ax = plt.subplots(figsize=(5.6, 3.2))
sp = ['MgCl', 'MgCl$_2$', 'MgCl$_3$']; val = [-88, -581, 4257]
ax.bar(range(3), val, color=[MUDA, HIJ, JGT], edgecolor=TUA, width=.55); ax.axhline(0, color=TUA, lw=.8)
for i, v in enumerate(val): ax.text(i, v + 120 if v > 0 else 150, f'{v:+d}'.replace('-', '−'), ha='center', fontsize=9, color=TUA)
ax.set_xticks(range(3)); ax.set_xticklabels(sp); ax.set_ylabel('Δ$_f$$H$° hitung (kJ mol$^{-1}$)'); ax.set_ylim(-1000, 4900); koma(ax, 'y')
simpan(f, 'c_hipotetis')
# 6. kelarutan: dua bilangan besar yang hampir saling meniadakan
f, ax = plt.subplots(figsize=(6.2, 3.1))
garam = ['LiF', 'NaCl', 'KCl', 'CsF', 'AgCl']; Ukis = [1049, 787, 717, 744, 918]; hidr = [-1023, -765, -682, -775, -825]; ukur = [4.9, 3.9, 17.2, -36.9, 65.5]
x = np.arange(len(garam)); ax.bar(x - .2, Ukis, .4, color=JG, edgecolor=JGT, label='entalpi kisi (diputus)'); ax.bar(x + .2, hidr, .4, color=MUDA, edgecolor=BIRU, label='entalpi hidrasi ion')
for i in range(len(garam)): ax.text(x[i], 1110, f'Δ$_{{lar}}H$ = {ukur[i]:+.1f}'.replace('.', ',').replace('-', '−'), ha='center', fontsize=7.8, color=TUA)
ax.axhline(0, color=TUA, lw=.8); ax.set_xticks(x); ax.set_xticklabels(garam); ax.set_ylabel('kJ mol$^{-1}$'); ax.set_ylim(-1200, 1250); ax.legend(fontsize=7.8, ncol=2, loc='lower center', bbox_to_anchor=(.5, 1.0), frameon=False); koma(ax, 'y')
simpan(f, 'c_larut')
# 7. karbonat
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.0))
rM = [72, 100, 118, 135]; T = [302, 836, 1098, 1292]; lab = ['Mg', 'Ca', 'Sr', 'Ba']; dU = [482, 401, 359, 325]
a1.plot(rM, T, 'o-', color=JGT); [a1.text(r_ + 3, t_ - 20, l, fontsize=9) for r_, t_, l in zip(rM, T, lab)]
a1.set_xlim(65, 150); a1.set_xlabel('jari-jari M$^{2+}$ (pm)'); a1.set_ylabel('suhu urai (°C, $p$(CO$_2$) = 1 bar)'); koma(a1)
a2.plot(rM, dU, 'o-', color=BIRU); [a2.text(r_ + 3, u_ + 3, l, fontsize=9) for r_, u_, l in zip(rM, dU, lab)]
a2.set_xlim(65, 150); a2.set_xlabel('jari-jari M$^{2+}$ (pm)'); a2.set_ylabel('$|U$(MO)$| − |U$(MCO$_3$)$|$ (kJ mol$^{-1}$)'); koma(a2)
f.subplots_adjust(wspace=.4)
simpan(f, 'c_karbonat')
# === pendalaman (revisi 2): energi kisi dan titik leleh ===
d1 = [('NaF', 873, 993), ('NaCl', 746, 801), ('NaBr', 714, 747), ('NaI', 667, 661)]
d2 = [('MgO', 3799, 2852), ('CaO', 3432, 2613), ('SrO', 3230, 2531), ('BaO', 3059, 1923)]
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.9))
for ax, d, c, t in [(a1, d1, BIRU, 'natrium halida (1+, 1−)'), (a2, d2, JGT, 'oksida golongan 2 (2+, 2−)')]:
    ax.plot([x[1] for x in d], [x[2] for x in d], 'o-', color=c)
    for n_, u, m in d: ax.text(u + (0 if n_ != 'BaO' else 40), m + (25 if ax is a1 else 45), n_, fontsize=8, ha='center' if n_ != 'BaO' else 'left')
    ax.set_xlabel('|U| Kapustinskii (kJ mol$^{-1}$)'); ax.set_title(t, fontsize=8.8, color=TUA); koma(ax)
a1.set_ylabel('titik leleh (°C)'); a1.set_ylim(620, 1060); a2.set_ylim(1800, 3000)
simpan(f, 'c_leleh')
# === pendalaman (revisi 2): nitrat alkali dan jari-jari termokimia ===
kap = lambda nu, z, s: 1.2025e5 * nu * z / s * (1 - 34.5 / s)
rN = 174.3
f, ax = plt.subplots(figsize=(5.8, 3.4))
rc = np.linspace(60, 185, 200); ax.plot(rc, kap(2, 1, rc + rN), color=BIRU, lw=2, label=f'Kapustinskii, $r$(NO$_3^-$) = 174 pm')
dat = [('Li', 76, 848), ('Na', 102, 755), ('K', 138, 685), ('Rb', 152, 658), ('Cs', 167, 648)]
for e, x, y in dat:
    ax.plot(x, y, 'o', color=JGT if e != 'K' else TUA, ms=7, zorder=3); ax.annotate(e + 'NO$_3$', (x, y), (x + 4, y + 14), fontsize=8.5, color=TUA)
ax.annotate('dipakai untuk\nmenurunkan $r$', (138, 685), (150, 760), fontsize=8, color=TUA, arrowprops=dict(arrowstyle='->', color=ABU))
ax.set_xlabel('jari-jari kation (pm)'); ax.set_ylabel('entalpi kisi (kJ mol$^{-1}$)'); ax.set_xlim(55, 195); ax.set_ylim(600, 900); ax.legend(fontsize=8.3, loc='lower left'); koma(ax)
simpan(f, 'a_nitrat')
