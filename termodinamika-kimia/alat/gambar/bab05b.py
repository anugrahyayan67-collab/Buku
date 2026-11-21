# Gambar tambahan Bab 5 (perbaikan total)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle, Rectangle
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab05/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def panah(ax, a, b, c=TUA, lw=2.2, ms=14): ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw))
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)

# 1. mesin kalor dan mesin pendingin
f, axs = plt.subplots(1, 2, figsize=(7.0, 3.4))
for ax, judul, balik in [(axs[0], 'mesin kalor', False), (axs[1], 'mesin pendingin / pompa kalor', True)]:
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    ax.add_patch(FancyBboxPatch((1.5, 8.2), 7, 1.3, boxstyle='round,pad=0.1', fc='#fbe3d4', ec=JT)); ax.text(5, 8.85, 'reservoir panas $T_\\mathrm{h}$', ha='center', va='center', color=JT, fontsize=9)
    ax.add_patch(FancyBboxPatch((1.5, 0.5), 7, 1.3, boxstyle='round,pad=0.1', fc='#dcecf9', ec=BIRU)); ax.text(5, 1.15, 'reservoir dingin $T_\\mathrm{c}$', ha='center', va='center', color=BIRU, fontsize=9)
    ax.add_patch(Circle((5, 5), 1.3, fc='white', ec=TUA, lw=1.6)); ax.text(5, 5, 'mesin', ha='center', va='center', fontsize=9, color=TUA)
    if not balik:
        panah(ax, (5, 8.1), (5, 6.35), JT); ax.text(5.3, 7.2, '$|q_\\mathrm{h}|$', color=JT)
        panah(ax, (5, 3.65), (5, 1.9), BIRU); ax.text(5.3, 2.7, '$|q_\\mathrm{c}|$', color=BIRU)
        panah(ax, (6.35, 5), (9.3, 5), HJ); ax.text(7.6, 5.35, '$|w|$ keluar', color=HJ, fontsize=9)
        ax.text(5, -0.5, '$\\eta = |w|/|q_\\mathrm{h}| \\leq 1 - T_\\mathrm{c}/T_\\mathrm{h}$', ha='center', fontsize=9.5)
    else:
        panah(ax, (5, 6.35), (5, 8.1), JT); ax.text(5.3, 7.2, '$|q_\\mathrm{h}|$', color=JT)
        panah(ax, (5, 1.9), (5, 3.65), BIRU); ax.text(5.3, 2.7, '$|q_\\mathrm{c}|$', color=BIRU)
        panah(ax, (9.3, 5), (6.35, 5), HJ); ax.text(7.4, 5.35, '$|w|$ masuk', color=HJ, fontsize=9)
        ax.text(5, -0.5, 'kalor dipompa "naik" dari dingin ke panas', ha='center', fontsize=9)
    ax.set_title(judul, fontsize=10, color=TUA)
f.tight_layout(); simpan(f, 'mesin')

# 2. efisiensi Carnot terhadap suhu reservoir panas
f, ax = plt.subplots(figsize=(6.0, 3.1)); Th = np.linspace(300, 1500, 300)
for Tc, c in [(280, BIRU), (300, TUA), (350, JT)]:
    ax.plot(Th, 1 - Tc / Th, color=c, lw=2, label=f'$T_\\mathrm{{c}}$ = {Tc} K')
for T, t in [(373, 'air mendidih\n373 K'), (823, 'uap turbin\n823 K'), (1400, 'turbin gas\n1400 K')]:
    e = 1 - 300 / T; ax.plot(T, e, 'o', color=HJ, ms=5); ax.annotate(t + f'\n(η = {e:.2f})'.replace('.', ','), (T, e), (T - 40 if T > 1000 else T + 40, e + 0.1 if T < 500 else e - 0.27), fontsize=8, color=HJ)
ax.set_xlabel('$T_\\mathrm{h}$ (K)'); ax.set_ylabel('efisiensi Carnot'); ax.set_ylim(0, 1); ax.set_xlim(300, 1500); ax.legend(frameon=False, fontsize=8.5, loc='lower right'); koma(ax)
f.tight_layout(); simpan(f, 'efisiensi')

# 3. siklus Carnot pada diagram T–S
f, ax = plt.subplots(figsize=(5.4, 3.3))
S1, S2, Th, Tc = 10, 18.64, 500, 300
ax.add_patch(Rectangle((S1, Tc), S2 - S1, Th - Tc, fc='#e6f2e9', ec='none'))
ax.add_patch(Rectangle((S1, 0), S2 - S1, Tc, fc='#dcecf9', ec='none'))
for (a, b), c, t in [(((S1, Th), (S2, Th)), JT, '1→2 isotermal, menyerap $q_\\mathrm{h} = T_\\mathrm{h}\\Delta S$'), (((S2, Th), (S2, Tc)), TUA, ''), (((S2, Tc), (S1, Tc)), BIRU, ''), (((S1, Tc), (S1, Th)), TUA, '')]:
    panah(ax, a, b, c, lw=2.2, ms=12)
ax.text((S1 + S2) / 2, Th + 15, '1→2 isotermal: menyerap $q_\\mathrm{h} = T_\\mathrm{h}\\Delta S$', ha='center', fontsize=8.5, color=JT)
ax.text((S1 + S2) / 2, Tc - 35, '3→4 isotermal: membuang $|q_\\mathrm{c}| = T_\\mathrm{c}\\Delta S$', ha='center', fontsize=8.5, color=BIRU)
ax.text(S2 + 0.3, 400, '2→3\nadiabatik\n(ΔS = 0)', fontsize=8.5, va='center'); ax.text(S1 - 0.3, 400, '4→1\nadiabatik', fontsize=8.5, va='center', ha='right')
ax.text((S1 + S2) / 2, 400, 'luas = $|w|$', ha='center', fontsize=9.5, color=HJ, fontweight='bold'); ax.text((S1 + S2) / 2, 140, 'luas = $|q_\\mathrm{c}|$', ha='center', fontsize=9, color=BIRU)
ax.set_xlim(6, 23); ax.set_ylim(0, 580); ax.set_xlabel('$S$ (J K$^{-1}$)'); ax.set_ylabel('$T$ (K)'); koma(ax)
f.tight_layout(); simpan(f, 'ts')

# 4. koefisien kinerja pendingin dan pompa kalor
f, ax = plt.subplots(figsize=(6.0, 3.0)); dT = np.linspace(5, 60, 200)
Tc = 273.15 + 4; ax.plot(dT, Tc / dT, color=BIRU, lw=2, label='pendingin: $T_\\mathrm{c}/(T_\\mathrm{h}-T_\\mathrm{c})$, $T_\\mathrm{c}$ = 4 °C')
Th = 273.15 + 40; ax.plot(dT, Th / dT, color=JT, lw=2, label='pompa kalor: $T_\\mathrm{h}/(T_\\mathrm{h}-T_\\mathrm{c})$, $T_\\mathrm{h}$ = 40 °C')
ax.set_ylim(0, 65); ax.set_xlabel('beda suhu $T_\\mathrm{h} - T_\\mathrm{c}$ (K)'); ax.set_ylabel('koefisien kinerja maksimum'); ax.legend(frameon=False, fontsize=8.3); koma(ax)
f.tight_layout(); simpan(f, 'cop')
print('ok bab05b')
