#!/usr/bin/env python3
# Gambar Bab 10 Kimia Anorganik 1: pelarut tak berair. -> bab10/fig/*.png
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab10', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
from matplotlib.ticker import FuncFormatter
def koma(ax, sb='xy'):
    fm = FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−'))
    if 'x' in sb: ax.xaxis.set_major_formatter(fm)
    if 'y' in sb: ax.yaxis.set_major_formatter(fm)
# 1. hidrasi ion: Na+ dan Cl-
f, axs = plt.subplots(1, 2, figsize=(6.8, 3.2))
def air(ax, x, y, ang, keO):
    # O di (x,y); dua H mengarah menjauh (keO=True: O menghadap ion)
    ax.add_patch(Circle((x, y), .2, fc='#d2553b', ec=TUA, zorder=3))
    for d in (-52, 52):
        a = np.radians(ang + d); ax.add_patch(Circle((x + .3 * np.cos(a), y + .3 * np.sin(a)), .13, fc='white', ec=TUA, zorder=2))
for ax, ion, c, r, judul in [(axs[0], 'Na$^+$', '#b48ae0', .38, 'kation: O menghadap ion'), (axs[1], 'Cl$^-$', '#9fd8a8', .55, 'anion: H menghadap ion')]:
    ax.add_patch(Circle((0, 0), r, fc=c, ec=TUA, zorder=3)); ax.text(0, 0, ion, ha='center', va='center', fontsize=12, zorder=4)
    for k in range(6):
        t = np.radians(60 * k + 15); d = r + .38
        x, y = d * np.cos(t), d * np.sin(t)
        if ion.startswith('Na'): air(ax, x, y, np.degrees(t), True)
        else:
            # H menghadap ion: O lebih jauh
            xo, yo = (d + .25) * np.cos(t), (d + .25) * np.sin(t); ax.add_patch(Circle((xo, yo), .2, fc='#d2553b', ec=TUA, zorder=3))
            ax.add_patch(Circle(((d - .02) * np.cos(t), (d - .02) * np.sin(t)), .13, fc='white', ec=TUA, zorder=4))
            a2 = t + np.radians(105); ax.add_patch(Circle((xo + .3 * np.cos(a2), yo + .3 * np.sin(a2)), .13, fc='white', ec=TUA, zorder=2))
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(judul, fontsize=9.5, color=TUA)
simpan(f, 'a_hidrasi')
# 2. energi pasangan ion terhadap tetapan dielektrik
nm = ['vakum', 'heksana', 'THF', 'NH$_3$ cair', 'metanol', 'asetonitril', 'DMSO', 'air', 'HF cair']; eps = [1, 1.9, 7.6, 22.4, 32.7, 37.5, 46.7, 78.4, 84]
E = [492.7 / e_ for e_ in eps]
f, ax = plt.subplots(figsize=(6.4, 3.0)); ax.bar(range(len(nm)), E, color=[JGT if e_ > 40 else BIRU for e_ in E], edgecolor=TUA); ax.set_yscale('log')
ax.set_xticks(range(len(nm))); ax.set_xticklabels(nm, fontsize=8, rotation=25); ax.axhline(2.48, color=HIJ, ls='--', lw=1); ax.set_ylim(1.4, 900); ax.text(8.45, 1.75, '$kT$ (298 K) = 2,48', color=HIJ, fontsize=8, ha='right')
for i, (v, e_) in enumerate(zip(E, eps)): ax.text(i, v * 1.15, f'ε = {e_:g}'.replace('.', ','), ha='center', fontsize=7)
ax.set_ylabel('energi tarik Na$^+$···Cl$^-$\npada 282 pm (kJ mol$^{-1}$)'); koma(ax, 'y')
simpan(f, 'a_eps')
# 3. bilangan donor dan akseptor Gutmann
sv = [('air', 18.0, 54.8), ('metanol', 19.0, 41.5), ('DMSO', 29.8, 19.3), ('DMF', 26.6, 16.0), ('asetonitril', 14.1, 18.9), ('aseton', 17.0, 12.5), ('THF', 20.0, 8.0), ('piridina', 33.1, 14.2), ('dietil eter', 19.2, 3.9), ('nitrometana', 2.7, 20.5), ('heksana', 0, 0), ('diklorometana', 1.0, 20.4)]
f, ax = plt.subplots(figsize=(6.0, 3.8))
for n_, dn, an in sv:
    ax.scatter(dn, an, color=BIRU, zorder=3); dy = -3.2 if n_ == 'nitrometana' else .9
    ax.text(dn + .6, an + dy, n_, fontsize=8, color=TUA)
ax.set_xlabel('bilangan donor DN (kemampuan memberi pasangan elektron)'); ax.set_ylabel('bilangan akseptor AN'); ax.set_xlim(-2, 40); ax.set_ylim(-3, 62); koma(ax)
simpan(f, 'b_dnan')
# 4. Kw dan pH netral
T = [0, 25, 37, 50, 75, 100]; pKw = [14.94, 14.00, 13.62, 13.26, 12.70, 12.26]
f, ax = plt.subplots(figsize=(5.6, 2.9)); ax.plot(T, pKw, 'o-', color=BIRU, label='p$K_w$'); ax.plot(T, [p / 2 for p in pKw], 's-', color=JGT, label='pH netral')
ax.set_xlabel('suhu (°C)'); ax.set_ylabel('nilai'); ax.legend(fontsize=8.5); koma(ax)
simpan(f, 'b_kw')
# 5. elektron tersolvasi dalam amonia
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0), gridspec_kw={'width_ratios': [1, 1.3]})
a1.add_patch(Circle((0, 0), .55, fc=MUDA, ec=BIRU, alpha=.5, ls='--')); a1.text(0, 0, 'e$^-$', ha='center', va='center', fontsize=14, color=BIRU)
for k in range(6):
    t = np.radians(60 * k); x, y = 1.0 * np.cos(t), 1.0 * np.sin(t)
    a1.add_patch(Circle((x, y), .2, fc='#3b6fb6', ec=TUA)); a1.text(x, y, 'N', ha='center', va='center', color='white', fontsize=7)
    for d in (-40, 0, 40):
        a = t + np.radians(d) * 0 + 0; aa = np.radians(np.degrees(t) + 180 + d)
        a1.add_patch(Circle((x + .28 * np.cos(aa), y + .28 * np.sin(aa)), .09, fc='white', ec=TUA))
a1.set_xlim(-1.6, 1.6); a1.set_ylim(-1.6, 1.6); a1.set_aspect('equal'); a1.axis('off'); a1.set_title('rongga berisi elektron\n(H dari NH$_3$ menghadap ke dalam)', fontsize=8.8, color=TUA)
lam = np.linspace(300, 2500, 500); A = np.exp(-((1239.84 / lam - 0.8) / 0.35) ** 2)
a2.plot(lam, A, color=BIRU); a2.axvspan(380, 750, color=JG, alpha=.2); a2.text(565, .9, 'cahaya\ntampak', ha='center', fontsize=8)
a2.set_xlabel('panjang gelombang (nm)'); a2.set_ylabel('serapan (relatif)'); a2.set_yticks([]); koma(a2, 'x'); a2.set_title('serapan merah–inframerah → larutan biru', fontsize=8.8, color=TUA)
simpan(f, 'b_elektron')
# 6. titik leleh garam dan cairan ionik
nm = ['Na$_3$AlF$_6$', 'NaCl', 'KCl', 'LiCl–KCl\n(eutektik)', '[BMIM]Cl', '[EMIM][BF$_4$]', '[BMIM][PF$_6$]']; tl = [1012, 801, 770, 352, 70, 15, 10]
f, ax = plt.subplots(figsize=(6.4, 3.0)); ax.bar(range(len(nm)), tl, color=[JGT] * 4 + [HIJ] * 3, edgecolor=TUA); ax.axhline(100, color=BIRU, ls='--', lw=1); ax.text(6.2, 120, '100 °C', color=BIRU, fontsize=8.5, ha='right')
ax.set_xticks(range(len(nm))); ax.set_xticklabels(nm, fontsize=7.8); ax.set_ylabel('titik leleh (°C)'); koma(ax, 'y')
simpan(f, 'c_ionik')
# 7. diagram fasa CO2 (skematis, titik kunci dari data)
f, ax = plt.subplots(figsize=(5.8, 3.8))
Tt, pt, Tc, pc = -56.6, 5.18, 31.0, 73.8
Ts = np.linspace(-100, Tt, 50); ps = pt * np.exp(26.0 * (1 / (Tt + 273.15) - 1 / (Ts + 273.15)) * 100 / 4.0)
ps = pt * np.exp((Ts - Tt) / 13.3)
Tl = np.linspace(Tt, Tc, 50); pl = pt * np.exp(np.log(pc / pt) * (Tl - Tt) / (Tc - Tt))
ax.semilogy(Ts, ps, color=TUA); ax.semilogy(Tl, pl, color=TUA); ax.semilogy([Tt, Tt + 6], [pt, 1000], color=TUA)
ax.fill_between([Tc, 80], pc, 1000, color=JG, alpha=.3); ax.text(48, 300, 'fluida\nsuperkritis', ha='center', fontsize=9, color=JGT)
ax.plot([Tt], [pt], 'o', color=TUA); ax.plot([Tc], [pc], 'o', color=JGT)
ax.text(Tt - 2, pt * 1.3, 'titik tripel\n−56,6 °C; 5,2 bar', fontsize=7.8, ha='right'); ax.text(Tc + 2, pc * .55, 'titik kritis\n31,0 °C; 73,8 bar', fontsize=7.8)
ax.text(-80, 60, 'padat', fontsize=10); ax.text(0, 150, 'cair', fontsize=10); ax.text(20, 2, 'gas', fontsize=10)
ax.axhline(1, color=ABU, ls=':', lw=1); ax.plot([-78.5], [1], 'o', color=ABU, ms=4); ax.text(-75, .68, 'pada 1 bar CO$_2$ padat menyublim (−78,5 °C)', fontsize=7.5, color=ABU)
ax.set_xlim(-100, 80); ax.set_ylim(.5, 1000); ax.set_xlabel('suhu (°C)'); ax.set_ylabel('tekanan (bar)'); koma(ax, 'x')
simpan(f, 'c_co2')
