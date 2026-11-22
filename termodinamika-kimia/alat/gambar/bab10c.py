# Gambar tambahan Bab 10: fungsi pencampuran, sifat koligatif pada diagram p-T, osmometer
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Rectangle, FancyArrowPatch
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R0 = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R0}/bab10/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
R = 8.314

# 1. fungsi pencampuran per mol, dalam satuan RT
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0)); x = np.linspace(0.001, 0.999, 400); s = x * np.log(x) + (1 - x) * np.log(1 - x)
a1.plot(x, -s, color=HJ, lw=2.2, label='$T\\Delta_\\mathrm{mix}S/nRT$'); a1.plot(x, s, color=BIRU, lw=2.2, label='$\\Delta_\\mathrm{mix}G/nRT$')
a1.axhline(0, color=JT, lw=2, ls='--', label='$\\Delta_\\mathrm{mix}H$ = 0'); a1.set_title('larutan ideal', fontsize=9)
a1.set_xlabel('$x_\\mathrm{A}$'); a1.set_ylim(-0.8, 0.8); a1.legend(frameon=False, fontsize=8, loc='center'); koma = lambda ax: (ax.xaxis.set_major_formatter(kom), ax.yaxis.set_major_formatter(kom)); koma(a1)
for b, col in [(0, BIRU), (1.5, HJ), (2.0, TUA), (2.7, JT)]:
    a2.plot(x, s + b * x * (1 - x), color=col, lw=2, label=f'β = {b:g}'.replace('.', ','))
a2.axhline(0, color='#999999', lw=0.8); a2.set_title('$\\Delta_\\mathrm{mix}G/nRT$ dengan $\\Delta_\\mathrm{mix}H = \\beta RTx_\\mathrm{A}x_\\mathrm{B}$', fontsize=9)
a2.set_xlabel('$x_\\mathrm{A}$'); a2.legend(frameon=False, fontsize=8, loc='lower center', ncol=2); a2.set_ylim(-0.8, 0.1); koma(a2)
a2.annotate('dua minimum:\nterpisah dua lapisan', xy=(0.12, s[48] + 2.7 * x[48] * (1 - x[48])), xytext=(0.32, 0.0), fontsize=7.8, color=JT, arrowprops=dict(arrowstyle='->', color=JT, lw=0.7))
f.tight_layout(); simpan(f, 'campur')

# 2. diagram p-T air dengan larutan (x_air = 0,90, dibesar-besarkan)
f, ax = plt.subplots(figsize=(6.2, 3.4)); Tt, pt = 273.16, 0.6117
T1 = np.linspace(255, Tt, 100); T2 = np.linspace(Tt, 385, 200)
psub = pt * np.exp(-51100 / R * (1 / T1 - 1 / Tt)); pvap = pt * np.exp(-45050 / R * (1 / T2 - 1 / Tt))
# kalibrasi kurva uap supaya melewati 101,3 kPa di 373,15 K: pakai ΔH efektif
dH = R * np.log(101.325 / pt) / (1 / Tt - 1 / 373.15); pvap = pt * np.exp(-dH / R * (1 / T2 - 1 / Tt))
ax.semilogy(T1, psub, color=TUA, lw=2); ax.semilogy(T2, pvap, color=BIRU, lw=2.2, label='air murni')
xw = 0.90; Tf = 1 / (1 / Tt - R * np.log(xw) / (dH - 51100) * -1)  # titik potong larutan dengan kurva sublimasi
Tf = 1 / (1 / Tt + R * np.log(xw) / (dH - 51100)); T3 = np.linspace(Tf, 385, 200)
ax.semilogy(T3, xw * pt * np.exp(-dH / R * (1 / T3 - 1 / Tt)), color=JT, lw=2.2, ls='--', label='larutan ($x_\\mathrm{air}$ = 0,90)')
ax.plot([Tf, Tf], [0.1, 160], color='#cccccc', lw=0.6); ax.plot([Tt, Tt], [0.1, 160], color='#cccccc', lw=0.6)
Tb = 1 / (1 / 373.15 + R * np.log(xw) / dH)
ax.axhline(101.325, color='#999999', lw=0.8, ls=':'); ax.text(257, 115, '1 atm', fontsize=8.3, color='#666666')
ax.annotate('', xy=(Tb, 101.325), xytext=(373.15, 101.325), arrowprops=dict(arrowstyle='<->', color=JT, lw=1.3)); ax.text((Tb + 373.15) / 2 - 4, 125, '$\\Delta T_\\mathrm{b}$', ha='center', fontsize=9, color=JT)
ax.annotate('', xy=(Tf, 0.2), xytext=(Tt, 0.2), arrowprops=dict(arrowstyle='<->', color=JT, lw=1.3)); ax.text((Tf + Tt) / 2, 0.24, '$\\Delta T_\\mathrm{f}$', ha='center', fontsize=9, color=JT)
ax.text(258, 0.35, 'es', fontsize=9, color=TUA); ax.text(300, 30, 'cair', fontsize=9, color=BIRU); ax.text(340, 3, 'uap', fontsize=9, color=TUA)
ax.annotate('', xy=(330, 0.9 * pt * np.exp(-dH / R * (1 / 330 - 1 / Tt))), xytext=(330, pt * np.exp(-dH / R * (1 / 330 - 1 / Tt))), arrowprops=dict(arrowstyle='->', color=JT, lw=1.3))
ax.text(332, 11, '$\\Delta p$', fontsize=9, color=JT)
ax.set_xlabel('$T$ (K)'); ax.set_ylabel('$p$ (kPa)'); ax.set_xlim(255, 385); ax.set_ylim(0.15, 160); ax.legend(frameon=False, fontsize=8.3, loc='lower right')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',')))
f.tight_layout(); simpan(f, 'koligatif')
print('Tf', Tf - Tt, 'Tb', Tb - 373.15)

# 3. osmometer skematis
f, ax = plt.subplots(figsize=(5.2, 3.4)); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 7)
ax.add_patch(Rectangle((1, 0.5), 8, 2.2, fc='none', ec=TUA, lw=2))
ax.add_patch(Rectangle((1.05, 0.55), 3.9, 1.8, color=MUDA, alpha=0.6, lw=0)); ax.add_patch(Rectangle((5.05, 0.55), 3.9, 1.8, color=BIRU, alpha=0.45, lw=0))
ax.plot([5, 5], [0.5, 2.7], color=JT, lw=2.5, ls=(0, (2, 1.5)))
ax.add_patch(Rectangle((6.6, 2.7), 0.8, 3.6, fc='white', ec=TUA, lw=1.6)); ax.add_patch(Rectangle((6.65, 2.35), 0.7, 2.9, color=BIRU, alpha=0.45, lw=0))
ax.add_patch(Rectangle((2.6, 2.7), 0.8, 3.6, fc='white', ec=TUA, lw=1.6)); ax.add_patch(Rectangle((2.65, 2.35), 0.7, 0.55, color=MUDA, alpha=0.6, lw=0))
ax.annotate('', xy=(8.0, 5.25), xytext=(8.0, 2.9), arrowprops=dict(arrowstyle='<->', color=TUA, lw=1.3)); ax.text(8.15, 4.0, '$h$', fontsize=11, color=TUA)
ax.plot([3.4, 8.0], [2.9, 2.9], color=TUA, lw=0.6, ls=':'); ax.plot([7.4, 8.0], [5.25, 5.25], color=TUA, lw=0.6, ls=':')
ax.annotate('', xy=(5.8, 1.6), xytext=(4.2, 1.6), arrowprops=dict(arrowstyle='->', color=JT, lw=2)); ax.text(3.0, 1.15, 'pelarut', fontsize=8.5, color=JT, ha='center')
ax.text(3.0, 0.15, 'pelarut murni', fontsize=9, color=TUA, ha='center'); ax.text(7.0, 0.15, 'larutan', fontsize=9, color=TUA, ha='center')
ax.text(5.0, 3.1, 'membran\nsemipermeabel', fontsize=8.3, color=JT, ha='center')
ax.text(5.0, 6.5, 'pada kesetimbangan: Π = ρ$gh$', fontsize=10, color=TUA, ha='center')
f.tight_layout(); simpan(f, 'osmometer')
print('ok bab10c')
