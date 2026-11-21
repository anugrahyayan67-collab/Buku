# Gambar tambahan Bab 12: K terhadap ΔG°, pengaruh tekanan, pasangan ATP, spesiasi asam
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R0 = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R0}/bab12/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
R = 8.314

# 1. log K terhadap ΔrG° pada 298 K dan 1000 K
f, ax = plt.subplots(figsize=(6.2, 3.2)); G = np.linspace(-100, 100, 400)
ax.axvspan(-100, -50, color=HJ, alpha=0.08, lw=0); ax.axvspan(50, 100, color=JT, alpha=0.08, lw=0)
for T, col in [(298.15, BIRU), (1000, JT)]: ax.plot(G, -G * 1000 / (R * T * np.log(10)), color=col, lw=2.2, label=f'{T:g} K'.replace('.', ','))
ax.axhline(0, color='#999999', lw=0.8); ax.axvline(0, color='#999999', lw=0.8)
ax.text(-97, -8, 'praktis\ntuntas', fontsize=8.5, color=HJ); ax.text(62, 12, 'praktis tidak\nberjalan', fontsize=8.5, color=JT)
ax.annotate('5,7 kJ mol$^{-1}$ = satu\ndekade *K* pada 25 °C'.replace('*', ''), xy=(-20, 3.5), xytext=(5, 10), fontsize=8.3, color=TUA, arrowprops=dict(arrowstyle='->', color=TUA, lw=0.8))
ax.set_xlabel('$\\Delta_\\mathrm{r}G^\\circ$ (kJ mol$^{-1}$)'); ax.set_ylabel('$\\log K$'); ax.set_xlim(-100, 100); ax.set_ylim(-18, 18)
ax.legend(frameon=False, fontsize=8.5, loc='lower left'); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'logK')

# 2. derajat penguraian N2O4 terhadap tekanan total, K = 0,148
f, ax = plt.subplots(figsize=(6.0, 3.0)); p = np.logspace(-3, 2, 300); K = 0.148
ax.semilogx(p, np.sqrt(K / (K + 4 * p)), color=BIRU, lw=2.2, label='derajat penguraian α')
ax.semilogx(p, 2 * np.sqrt(K / (K + 4 * p)) / (1 + np.sqrt(K / (K + 4 * p))), color=JT, lw=2, ls='--', label='fraksi mol NO$_2$')
for pp in [0.1, 1, 10]:
    a = np.sqrt(K / (K + 4 * pp)); ax.plot(pp, a, 'o', color=BIRU, ms=5); t = f'{a:.3f}'.replace('.', ',')
    if pp < 5: ax.text(pp * 0.55, a - 0.09, t, fontsize=8.3, color=BIRU)
    else: ax.annotate(t, xy=(pp, a), xytext=(22, 0.22), fontsize=8.3, color=BIRU, arrowprops=dict(arrowstyle='-', color=BIRU, lw=0.6))
ax.set_xlabel('tekanan total (bar)'); ax.set_ylabel('α atau $x_{\\mathrm{NO}_2}$'); ax.set_ylim(0, 1.05); ax.legend(frameon=False, fontsize=8.5)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, q: f'{x:g}'.replace('.', ','))); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'tekanan')

# 3. pasangan reaksi ATP: diagram tingkat energi Gibbs standar biokimia
f, ax = plt.subplots(figsize=(6.4, 3.3)); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(-39, 22)
def tingkat(x, y, t, c, bawah=False):
    ax.plot([x, x + 2.2], [y, y], color=c, lw=3); ax.text(x + 1.1, y - 3.6 if bawah else y + 1.4, t, ha='center', fontsize=8.6, color=c)
tingkat(0.2, 0, 'glukosa + P$_\\mathrm{i}$', TUA, True); tingkat(0.2, 13.8, 'glukosa-6-P', TUA)
ax.annotate('', xy=(1.3, 13.4), xytext=(1.3, 0.4), arrowprops=dict(arrowstyle='->', color=JT, lw=1.8)); ax.text(1.45, 6, '+13,8', fontsize=9, color=JT)
tingkat(3.8, 0, 'ATP + H$_2$O', TUA); tingkat(3.8, -30.5, 'ADP + P$_\\mathrm{i}$', TUA, True)
ax.annotate('', xy=(4.9, -30.1), xytext=(4.9, -0.4), arrowprops=dict(arrowstyle='->', color=HJ, lw=1.8)); ax.text(5.05, -16, '−30,5', fontsize=9, color=HJ)
tingkat(7.4, 0, 'glukosa + ATP', TUA); tingkat(7.4, -16.7, 'glukosa-6-P + ADP', TUA, True)
ax.annotate('', xy=(8.5, -16.3), xytext=(8.5, -0.4), arrowprops=dict(arrowstyle='->', color=BIRU, lw=1.8)); ax.text(8.65, -8, '−16,7', fontsize=9, color=BIRU)
ax.text(2.9, 4, '+', fontsize=16, color=TUA, ha='center'); ax.text(6.5, 4, '=', fontsize=16, color=TUA, ha='center')
ax.text(1.3, -8, "$K'$ = 0,0038", ha='center', fontsize=8.6); ax.text(4.9, -37.5, "$K'$ = 2,2 × 10$^5$", ha='center', fontsize=8.6); ax.text(8.5, -25, "$K'$ = 840", ha='center', fontsize=8.6)
ax.text(5, 20, '$\\Delta_\\mathrm{r}G^{\\circ\\prime}$ (kJ mol$^{-1}$) pada 25 °C', ha='center', fontsize=9, color=TUA)
f.tight_layout(); simpan(f, 'atp')

# 4. spesiasi asam asetat dan ion amonium terhadap pH
f, ax = plt.subplots(figsize=(6.2, 3.0)); pH = np.linspace(0, 14, 400)
for pKa, a, b, col in [(4.76, 'CH$_3$COOH', 'CH$_3$COO$^-$', BIRU), (9.25, 'NH$_4^+$', 'NH$_3$', JT)]:
    fb = 1 / (1 + 10 ** (pKa - pH)); ax.plot(pH, 1 - fb, color=col, lw=2.2); ax.plot(pH, fb, color=col, lw=2.2, ls='--')
    ax.axvline(pKa, color=col, lw=0.7, ls=':'); ax.text(pKa, 1.05, ha='center', s= f'p$K_\\mathrm{{a}}$ = {pKa:g}'.replace('.', ','), fontsize=8.3, color=col)
ax.text(1.0, 0.88, 'CH$_3$COOH', fontsize=8.5, color=BIRU); ax.text(6.0, 0.88, 'CH$_3$COO$^-$', fontsize=8.5, color=BIRU)
ax.text(6.2, 0.12, 'NH$_4^+$', fontsize=8.5, color=JT); ax.text(11.6, 0.12, 'NH$_3$', fontsize=8.5, color=JT)
ax.set_xlabel('pH'); ax.set_ylabel('fraksi'); ax.set_xlim(0, 14); ax.set_ylim(0, 1.12); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'spesiasi')
print('ok bab12c')
