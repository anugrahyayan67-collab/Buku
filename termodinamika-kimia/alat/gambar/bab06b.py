# Gambar tambahan Bab 6 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab06/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)

# 1. aturan Trouton
D = [('CCl$_4$', 29.82, 349.9), ('benzena', 30.72, 353.2), ('sikloheksana', 29.97, 353.9), ('H$_2$S', 18.67, 212.8), ('metana', 8.19, 111.7), ('NH$_3$', 23.33, 239.8), ('etanol', 38.56, 351.4), ('air', 40.66, 373.15)]
f, ax = plt.subplots(figsize=(6.4, 3.0))
v = [h * 1000 / T for _, h, T in D]; cols = [BIRU if x < 95 else JT for x in v]
ax.bar(range(len(D)), v, color=cols, width=0.62)
for i, x in enumerate(v): ax.text(i, x + 2, f'{x:.0f}', ha='center', fontsize=8.5)
ax.axhline(85, color=HJ, lw=1, ls='--'); ax.text(-0.4, 124, '- - - aturan Trouton ≈ 85 J K$^{-1}$ mol$^{-1}$', fontsize=8.5, color=HJ)
ax.set_xticks(range(len(D))); ax.set_xticklabels([d[0] for d in D], fontsize=8.5, rotation=20); ax.set_ylabel('Δ$_\\mathrm{vap}$S (J K$^{-1}$ mol$^{-1}$)'); ax.set_ylim(0, 135)
ax.text(6.0, 124, 'ikatan hidrogen:\ncairan lebih teratur', ha='center', fontsize=8, color=JT)
f.tight_layout(); simpan(f, 'trouton')

# 2. entropi air terhadap suhu, 250–400 K, acuan S°(l, 298) = 69,91
f, ax = plt.subplots(figsize=(6.2, 3.2))
Cs, Cl, Cg = 37.8, 75.3, 33.6; Sl298 = 69.91
Sl = lambda T: Sl298 + Cl * np.log(T / 298.15)
Tm, Tb = 273.15, 373.15
Ts = np.linspace(230, Tm, 50); Tl = np.linspace(Tm, Tb, 80); Tg = np.linspace(Tb, 420, 40)
S_s = Sl(Tm) - 6010 / Tm + Cs * np.log(Ts / Tm); S_l = Sl(Tl); S_g = Sl(Tb) + 40660 / Tb + Cg * np.log(Tg / Tb)
ax.plot(Ts, S_s, color=BIRU, lw=2.2); ax.plot(Tl, S_l, color=HJ, lw=2.2); ax.plot(Tg, S_g, color=JT, lw=2.2)
ax.plot([Tm, Tm], [S_s[-1], S_l[0]], color='#888888', lw=1.2, ls='--'); ax.plot([Tb, Tb], [S_l[-1], S_g[0]], color='#888888', lw=1.2, ls='--')
ax.text(Tm + 3, (S_s[-1] + S_l[0]) / 2, 'meleleh\n+22,0', fontsize=8.5, va='center'); ax.text(Tb - 3, (S_l[-1] + S_g[0]) / 2, 'mendidih\n+109,0', fontsize=8.5, va='center', ha='right')
ax.text(245, S_s[0] + 6, 'es', color=BIRU); ax.text(320, Sl(320) + 6, 'cair', color=HJ); ax.text(395, S_g[-1] - 14, 'uap', color=JT)
ax.set_xlabel('$T$ (K)'); ax.set_ylabel('$S_\\mathrm{m}$ (J K$^{-1}$ mol$^{-1}$)'); ax.set_xlim(230, 420); koma(ax)
f.tight_layout(); simpan(f, 'pemanasan')

# 3. entropi molar standar: pola dari Tabel 6.1
Z = [('C(intan)', 2.38, 's'), ('C(grafit)', 5.74, 's'), ('Fe', 27.28, 's'), ('NaCl', 72.13, 's'), ('I$_2$(s)', 116.14, 's'), ('H$_2$O(l)', 69.91, 'l'), ('Hg(l)', 76.02, 'l'), ('He', 126.15, 'g'), ('Ar', 154.84, 'g'), ('N$_2$', 191.61, 'g'), ('H$_2$O(g)', 188.83, 'g'), ('CO$_2$', 213.74, 'g'), ('I$_2$(g)', 260.69, 'g')]
f, ax = plt.subplots(figsize=(6.8, 3.0)); c = {'s': BIRU, 'l': HJ, 'g': JT}
ax.bar(range(len(Z)), [z[1] for z in Z], color=[c[z[2]] for z in Z], width=0.65)
ax.set_xticks(range(len(Z))); ax.set_xticklabels([z[0] for z in Z], rotation=40, ha='right', fontsize=8.3); ax.set_ylabel('$S_\\mathrm{m}^\\circ$ (J K$^{-1}$ mol$^{-1}$)')
for t, x, cc in [('padat', 2, BIRU), ('cair', 5.5, HJ), ('gas', 10, JT)]: ax.text(x, 245, t, ha='center', color=cc, fontsize=9.5, fontweight='bold')
ax.set_ylim(0, 280); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'Spola')

# 4. pembekuan air: entropi sistem, lingkungan, total terhadap suhu
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.0, 3.0)); T = np.linspace(250, 295, 100)
dSsys = -6010 / 273.15 * np.ones_like(T); dSsur = 6010 / T
a1.plot(T, dSsys, color=BIRU, lw=2, label='Δ$S_\\mathrm{sistem}$ (air → es)'); a1.plot(T, dSsur, color=JT, lw=2, label='Δ$S_\\mathrm{lingkungan}$ = Δ$_\\mathrm{fus}H/T$')
a1.axhline(0, color='#888888', lw=0.8); a1.set_ylim(-30, 30); a1.legend(frameon=False, fontsize=8, loc='center right'); a1.set_xlabel('suhu (K)'); a1.set_ylabel('Δ$S$ (J K$^{-1}$ mol$^{-1}$)')
a2.plot(T, dSsys + dSsur, color=HJ, lw=2.4); a2.axhline(0, color='#888888', lw=0.8); a2.axvline(273.15, color='#888888', lw=0.8, ls=':')
a2.fill_between(T, dSsys + dSsur, 0, where=(T < 273.15), color=HJ, alpha=0.15)
a2.text(259, -0.6, 'membeku\nspontan', ha='center', fontsize=8.5, color=HJ); a2.text(286, 0.5, 'tidak\nmembeku', ha='center', fontsize=8.5, color='#666666')
a2.set_xlabel('suhu (K)'); a2.set_ylabel('Δ$S_\\mathrm{total}$ (J K$^{-1}$ mol$^{-1}$)')
for a_ in (a1, a2): koma(a_)
f.tight_layout(); simpan(f, 'beku')
print('ok bab06b')
