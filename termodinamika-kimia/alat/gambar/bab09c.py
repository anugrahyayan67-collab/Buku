# Gambar tambahan Bab 9: entalpi molar parsial (metode intersep) dan ultrasentrifus
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R0 = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R0}/bab09/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)

# 1. entalpi pencampuran model reguler w = -6,0 kJ/mol dan garis singgung di x_B = 0,25
f, ax = plt.subplots(figsize=(6.0, 3.3)); w = -6.0; x = np.linspace(0, 1, 300)
ax.plot(x, w * x * (1 - x), color=BIRU, lw=2.4, label='$\\Delta_\\mathrm{campur}H_\\mathrm{m}$')
x0 = 0.25; y0 = w * x0 * (1 - x0); s = w * (1 - 2 * x0)
ax.plot([0, 1], [y0 - s * x0, y0 + s * (1 - x0)], color=JT, lw=1.6, ls='--', label='garis singgung di $x_\\mathrm{B}$ = 0,25')
ax.plot(x0, y0, 'o', color=JT, ms=5)
ax.plot(0, w * x0 ** 2, 's', color=HJ, ms=6, clip_on=False); ax.plot(1, w * (1 - x0) ** 2, 's', color=HJ, ms=6, clip_on=False)
ax.text(0.03, 0.12, '$H_\\mathrm{A} - H^*_\\mathrm{A}$ = −0,375', fontsize=8.5, color=HJ)
ax.text(0.95, -3.68, '$H_\\mathrm{B} - H^*_\\mathrm{B}$ = −3,375', fontsize=8.5, color=HJ, ha='right')
ax.axhline(0, color='#999999', lw=0.8)
ax.set_xlabel('$x_\\mathrm{B}$'); ax.set_ylabel('kJ mol$^{-1}$'); ax.set_xlim(0, 1); ax.set_ylim(-3.8, 0.5)
ax.legend(frameon=False, fontsize=8.5, loc='lower left', bbox_to_anchor=(0.0, 0.05)); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'Hparsial')

# 2. sebaran konsentrasi protein di sel ultrasentrifus pada kesetimbangan sedimentasi
f, ax = plt.subplots(figsize=(6.0, 3.0)); R = 8.314; T = 293.15; om = 2 * np.pi * 8000 / 60; r = np.linspace(0.068, 0.072, 200)
for nm, M, vb, col in [('mioglobin, 17,8 kg mol$^{-1}$', 17.8, 0.741, MUDA), ('albumin serum, 66,4 kg mol$^{-1}$', 66.4, 0.734, BIRU), ('imunoglobulin G, 150 kg mol$^{-1}$', 150, 0.739, JT)]:
    Me = M * (1 - vb * 0.998); ax.semilogy(r * 100, np.exp(Me * om ** 2 * (r ** 2 - 0.068 ** 2) / (2 * R * T)), color=col, lw=2.2, label=nm)
ax.set_xlabel('jarak dari sumbu putar $r$ (cm)'); ax.set_ylabel('$c(r)/c$(meniskus)'); ax.legend(frameon=False, fontsize=8.3, loc='upper left')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',')))
ax.set_title('8000 putaran per menit, 20 °C', fontsize=9, color='#555555')
f.tight_layout(); simpan(f, 'sentrifus')
print('ok bab09c')
