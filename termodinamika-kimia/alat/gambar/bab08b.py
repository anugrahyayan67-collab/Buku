# Gambar tambahan Bab 8 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab08/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)

# 1. μ terhadap T untuk padat, cair, gas, pada dua tekanan (skematis)
f, ax = plt.subplots(figsize=(6.2, 3.4)); T = np.linspace(0, 10, 200)
mu_s = 2 - 0.25 * T; mu_l = 3 - 0.45 * T; mu_g = 6.2 - 0.95 * T
ax.plot(T, mu_s, color=BIRU, lw=2.2, label='padat'); ax.plot(T, mu_l, color=HJ, lw=2.2, label='cair'); ax.plot(T, mu_g, color=JT, lw=2.2, label='gas')
mu_g2 = mu_g + 0.8; ax.plot(T, mu_g2, color=JT, lw=1.4, ls='--', label='gas, tekanan lebih tinggi')
Tm = 5.0; Tb = (6.2 - 3) / 0.5; Tb2 = (7.0 - 3) / 0.5
for x, t in [(Tm, '$T_\\mathrm{f}$'), (Tb, '$T_\\mathrm{b}$'), (Tb2, "$T_\\mathrm{b}'$")]:
    ax.axvline(x, color='#bbbbbb', lw=0.8, ls=':'); ax.text(x, -4.6, t, ha='center', fontsize=9)
ax.text(1.5, -3.9, 'padat stabil', color=BIRU, fontsize=8.5, ha='center'); ax.text((Tm + Tb) / 2, -3.9, 'cair stabil', color=HJ, fontsize=8.5, ha='center'); ax.text(8.9, -3.9, 'gas stabil', color=JT, fontsize=8.5, ha='center')
ax.set_xlim(0, 10); ax.set_ylim(-4.3, 4); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('suhu $T$'); ax.set_ylabel('potensial kimia μ'); ax.legend(frameon=False, fontsize=8.3, loc='upper right')
f.tight_layout(); simpan(f, 'muT')

# 2. tekanan uap beberapa cairan (Clausius–Clapeyron dari titik didih normal dan Δvap H)
f, ax = plt.subplots(figsize=(6.2, 3.3)); Rg = 8.314
for nm, Tb, H, c in [('dietil eter', 307.8, 26.5, JG), ('aseton', 329.2, 29.1, HJ), ('etanol', 351.4, 38.6, BIRU), ('air', 373.15, 40.7, TUA)]:
    T = np.linspace(273.15, 390, 200); p = 101.325 * np.exp(-H * 1000 / Rg * (1 / T - 1 / Tb))
    ax.plot(T - 273.15, p, color=c, lw=2, label=nm); ax.plot(Tb - 273.15, 101.325, 'o', color=c, ms=5)
ax.axhline(101.325, color='#888888', lw=0.8, ls='--'); ax.text(2, 106, '1 atm: titik didih normal (titik)', fontsize=8.3, color='#666666')
ax.set_xlim(0, 115); ax.set_ylim(0, 200); ax.set_xlabel('suhu (°C)'); ax.set_ylabel('tekanan uap (kPa)'); ax.legend(frameon=False, fontsize=8.5, loc='upper left', bbox_to_anchor=(0, 0.92)); koma(ax)
f.tight_layout(); simpan(f, 'uap')

# 3. klasifikasi Ehrenfest: G, S, Cp untuk transisi orde pertama dan kedua (skematis)
f, axs = plt.subplots(2, 3, figsize=(7.2, 4.2)); T = np.linspace(0, 2, 400); Tt = 1.0
a, b = T < Tt, T >= Tt
G1 = np.where(a, -0.6 * T, -0.6 * Tt - 1.2 * (T - Tt)); S1 = np.where(a, 0.6, 1.2)
axs[0, 0].plot(T, G1, color=TUA, lw=2); axs[0, 1].plot(T[a], S1[a], color=BIRU, lw=2); axs[0, 1].plot(T[b], S1[b], color=BIRU, lw=2)
axs[0, 2].plot(T[a], 0.3 + 0 * T[a], color=JT, lw=2); axs[0, 2].plot(T[b], 0.3 + 0 * T[b], color=JT, lw=2); axs[0, 2].annotate('', (Tt, 1.6), (Tt, 0.3), arrowprops=dict(arrowstyle='->', color=JT, lw=1.6)); axs[0, 2].text(Tt + 0.08, 1.4, 'tak hingga', fontsize=8, color=JT); axs[0, 2].set_ylim(0, 1.8)
x = T - Tt; Cp2 = np.where(a, 0.3 + 0.6 * T ** 2, 0.25); S2 = np.cumsum(Cp2 / np.maximum(T, 1e-3)) * (T[1] - T[0]); G2 = -np.cumsum(S2) * (T[1] - T[0])
axs[1, 0].plot(T, G2, color=TUA, lw=2); axs[1, 1].plot(T, S2, color=BIRU, lw=2); axs[1, 2].plot(T[a], Cp2[a], color=JT, lw=2); axs[1, 2].plot(T[b], Cp2[b], color=JT, lw=2)
for i, t in enumerate(['$G$', '$S = -(\\partial G/\\partial T)_p$', '$C_p = T(\\partial S/\\partial T)_p$']): axs[0, i].set_title(t, fontsize=9.5)
axs[0, 0].set_ylabel('orde pertama\n(meleleh, mendidih)', fontsize=9); axs[1, 0].set_ylabel('orde kedua\n(transisi λ, titik Curie)', fontsize=9)
for ax in axs.flat:
    ax.set_xticks([Tt]); ax.set_xticklabels(['$T_\\mathrm{trs}$']); ax.set_yticks([]); ax.axvline(Tt, color='#cccccc', lw=0.8, ls=':')
f.tight_layout(); simpan(f, 'orde')
print('ok bab08b')
