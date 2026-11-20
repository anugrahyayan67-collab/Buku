# Gambar Bab 13: python3 alat/gambar/bab13.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab13', 'fig')
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.tight_layout(); f.savefig(f'{D}/{n}.png'); plt.close(f)
# 13.1 sel Daniell
f, ax = plt.subplots(figsize=(5.6, 3.6), dpi=220); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(-0.8, 6.4)
for x0, isi, lab, el, ion in [(0.6, '#c8dff0', 'anode (oksidasi)', 'Zn', r'Zn$^{2+}$'), (6.4, '#9cc6ea', 'katode (reduksi)', 'Cu', r'Cu$^{2+}$')]:
    ax.add_patch(Rectangle((x0, 0.4), 3.0, 3.0, fc='white', ec=TUA, lw=1.8)); ax.add_patch(Rectangle((x0 + 0.05, 0.45), 2.9, 2.3, color=isi, lw=0))
    ax.add_patch(Rectangle((x0 + 1.25, 1.0), 0.5, 3.4, color=JT if el == 'Cu' else '#9aa3ab', ec=TUA, lw=1.2))
    ax.text(x0 + 1.5, 4.55, el, ha='center', fontsize=10, color=TUA, fontweight='bold'); ax.text(x0 + 0.35, 1.0, ion, fontsize=9.5, color=TUA)
    ax.text(x0 + 1.5, 0.0, lab, ha='center', fontsize=9.5, color=HJ)
ax.plot([3.0, 3.0, 7.0, 7.0], [2.2, 3.9, 3.9, 2.2], color='#dcc9a0', lw=12, solid_capstyle='butt'); ax.text(5.0, 4.1, 'jembatan garam', ha='center', fontsize=8.5, color=JT)
ax.plot([2.1, 2.1, 7.9, 7.9], [4.4, 5.8, 5.8, 4.4], color=TUA, lw=1.5)
ax.add_patch(FancyBboxPatch((4.4, 5.45), 1.2, 0.7, boxstyle='round,pad=0.02', fc='white', ec=TUA, lw=1.5)); ax.text(5.0, 5.8, 'V', ha='center', va='center', fontsize=11, color=TUA)
ax.annotate('', xy=(3.9, 6.05), xytext=(2.4, 6.05), arrowprops=dict(arrowstyle='-|>', color=BIRU, lw=1.6)); ax.text(3.15, 6.2, r'e$^-$', color=BIRU, ha='center', fontsize=9)
ax.text(2.1, -0.55, r'Zn $\rightarrow$ Zn$^{2+}$ + 2e$^-$', fontsize=8.5, color=TUA, ha='center'); ax.text(7.9, -0.55, r'Cu$^{2+}$ + 2e$^-$ $\rightarrow$ Cu', fontsize=8.5, color=TUA, ha='center')
simpan(f, 'daniell')
# 13.2 jendela kestabilan air
pH = np.linspace(0, 14, 50); l = 0.05916
f, ax = plt.subplots(figsize=(5.2, 3.7), dpi=220)
ax.plot(pH, 1.229 - l * pH, color=JT, lw=2.4); ax.plot(pH, -l * pH, color=BIRU, lw=2.4)
ax.fill_between(pH, -l * pH, 1.229 - l * pH, color=MUDA, alpha=0.25, lw=0)
ax.text(1.0, 1.32, r'O$_2$ dilepaskan (air teroksidasi)', color=JT, fontsize=9); ax.text(4.5, -0.75, r'H$_2$ dilepaskan (air tereduksi)', color=BIRU, fontsize=9)
ax.text(7.0, 0.45, 'air stabil', color=TUA, fontsize=10, ha='center', rotation=-14)
ax.set_xlim(0, 14); ax.set_ylim(-1.0, 1.6); ax.set_xlabel('pH'); ax.set_ylabel('E terhadap SHE (V)')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom); simpan(f, 'airstabil')
# 13.3 E° sel Pt|H2|HCl|AgCl|Ag terhadap suhu
t = np.array([0, 10, 20, 25, 30, 40, 50, 60]); E = np.array([0.23634, 0.23126, 0.22551, 0.22239, 0.21912, 0.21208, 0.20449, 0.19641])
c = np.polyfit(t, E, 2); tt = np.linspace(0, 60, 100)
f, ax = plt.subplots(figsize=(5.2, 3.6), dpi=220)
ax.plot(tt, np.polyval(c, tt), color=BIRU, lw=2); ax.plot(t, E, 'o', color=JT, ms=6, zorder=5)
s = np.polyval(np.polyder(c), 25); ax.plot([10, 40], [0.22239 + s * (-15), 0.22239 + s * 15], color=HJ, lw=1.4, ls='--')
ax.text(31, 0.2265, 'kemiringan di 25 °C:\n' + f'{s*1e3:.3f}'.replace('.', ',').replace('-', '−') + r' mV K$^{-1}$', color=HJ, fontsize=9)
ax.set_xlabel('t (°C)'); ax.set_ylabel(r'$E^\circ$ (V)'); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom); simpan(f, 'ET')
print('slope', s)
