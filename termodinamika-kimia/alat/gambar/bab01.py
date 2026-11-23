# Gambar Bab 1 (perbaikan total): python3 alat/gambar/bab01.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Polygon, FancyBboxPatch
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab01/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def panah(ax, a, b, c=TUA, lw=1.4, ms=11, st='-|>'): ax.add_patch(FancyArrowPatch(a, b, arrowstyle=st, mutation_scale=ms, color=c, lw=lw))
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
Rg = 8.314

# 1. barometer dan manometer ujung terbuka
f, ax = plt.subplots(figsize=(7.0, 3.2)); ax.set_xlim(0, 20); ax.set_ylim(-0.6, 9.4); ax.set_aspect('equal'); ax.axis('off')
HG = '#9aa3ad'
# barometer
ax.add_patch(Rectangle((1.0, 0.0), 4.0, 1.4, fc=HG, ec=TUA, lw=1.2)); ax.add_patch(Rectangle((2.6, 0.6), 0.8, 8.2, fc='white', ec=TUA, lw=1.4))
ax.add_patch(Rectangle((2.6, 0.6), 0.8, 6.6, fc=HG, ec='none')); ax.plot([2.6, 2.6, 3.4, 3.4], [0.6, 8.8, 8.8, 0.6], color=TUA, lw=1.4)
ax.text(3.6, 8.1, 'hampa', ha='left', fontsize=8, color='#555555')
ax.annotate('', (4.4, 7.2), (4.4, 1.4), arrowprops=dict(arrowstyle='<->', color=JT, lw=1.1)); ax.text(4.6, 4.3, '$h$ = 760 mm\n(1 atm)', fontsize=8.5, color=JT, va='center')
for x in (1.4, 4.7): panah(ax, (x, 2.6), (x, 1.55), BIRU)
ax.text(0.55, 2.9, '$p_\\mathrm{atm}$', fontsize=9, color=BIRU)
ax.text(3.0, -0.5, 'barometer: $p_\\mathrm{atm} = \\rho g h$', ha='center', fontsize=9, color=TUA)
# manometer ujung terbuka
ax.add_patch(Circle((10.0, 5.2), 1.5, fc='#eaf3fb', ec=TUA, lw=1.4)); ax.text(10.0, 5.2, 'gas\n$p_\\mathrm{gas}$', ha='center', va='center', fontsize=9, color=TUA)
xl, xr = 12.6, 15.4; w = 0.6
ax.plot([11.5, xl], [5.2, 5.2], color=TUA, lw=1.4); ax.plot([11.5, xl - w / 2], [4.8, 4.8], color=TUA, lw=1.4)
ax.plot([xl - w / 2, xl - w / 2], [4.8, 1.0], color=TUA, lw=1.4); ax.plot([xl + w / 2, xl + w / 2], [5.2, 1.6], color=TUA, lw=1.4); ax.plot([xl, xl], [5.2, 5.2], color=TUA)
ax.plot([xl - w / 2, xl - w / 2], [5.2, 5.2]); ax.plot([xl - w / 2, xl + w / 2], [5.2, 5.2], color='none')
ax.add_patch(Rectangle((xl - w / 2, 1.0), w, 2.0, fc=HG, ec='none')); ax.add_patch(Rectangle((xr - w / 2, 1.0), w, 3.6, fc=HG, ec='none'))
ax.add_patch(Rectangle((xl - w / 2, 0.4), xr - xl + w, 0.6, fc=HG, ec='none'))
ax.plot([xl - w / 2, xl - w / 2, xr + w / 2, xr + w / 2], [4.8, 0.4, 0.4, 7.4], color=TUA, lw=1.4); ax.plot([xl + w / 2, xl + w / 2, xr - w / 2, xr - w / 2], [5.2, 1.0, 1.0, 7.4], color=TUA, lw=1.4)
ax.plot([11.5, xl + w / 2], [5.2, 5.2], color=TUA, lw=1.4)
panah(ax, (xr, 8.6), (xr, 7.0), BIRU); ax.text(xr + 0.4, 8.3, '$p_\\mathrm{atm}$ (ujung terbuka)', fontsize=8.5, color=BIRU)
ax.plot([xl + 0.5, xr + 1.6], [3.0, 3.0], color=JT, lw=0.8, ls=':'); ax.plot([xr + 0.4, xr + 1.6], [4.6, 4.6], color=JT, lw=0.8, ls=':')
ax.annotate('', (xr + 1.3, 4.6), (xr + 1.3, 3.0), arrowprops=dict(arrowstyle='<->', color=JT, lw=1.1)); ax.text(xr + 1.55, 3.8, '$\\Delta h$', fontsize=9, color=JT, va='center')
ax.text(13.6, -0.5, 'manometer: $p_\\mathrm{gas} = p_\\mathrm{atm} + \\rho g\\,\\Delta h$', ha='center', fontsize=9, color=TUA)
simpan(f, 'manometer')

# 2. isoterm Boyle: p terhadap V dan p terhadap 1/V
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.9))
V = np.linspace(4, 50, 300)
for T, c in [(273, MUDA), (373, BIRU), (473, TUA)]:
    a1.plot(V, Rg * T / V / 100, color=c, lw=2, label=f'{T} K'); a2.plot(1 / V, Rg * T / V / 100, color=c, lw=2)
a1.set_xlabel('$V$ (L)'); a1.set_ylabel('$p$ (bar)'); a1.set_title('isoterm: hiperbola $pV$ = tetap', fontsize=9); a1.legend(frameon=False, fontsize=8.5); a1.set_ylim(0, 10)
a2.set_xlabel('$1/V$ (L$^{-1}$)'); a2.set_ylabel('$p$ (bar)'); a2.set_title('$p$ terhadap $1/V$: garis lurus', fontsize=9); a2.set_xlim(0, 0.26); a2.set_ylim(0, 10)
for a in (a1, a2): koma(a)
f.text(0.5, -0.04, 'satu mol gas ideal; isoterm lebih tinggi pada suhu lebih tinggi', ha='center', fontsize=8.5, color='#555555')
f.tight_layout(); simpan(f, 'boyle')

# 3. Charles: V terhadap suhu Celsius, ekstrapolasi ke −273,15 °C
f, ax = plt.subplots(figsize=(6.4, 3.1))
t = np.linspace(-300, 300, 10); tu = np.linspace(-50, 300, 10)
for n, c in [(0.04, MUDA), (0.08, BIRU), (0.12, TUA)]:
    Vf = lambda tt: n * 0.08314 * (tt + 273.15)
    ax.plot(tu, Vf(tu), color=c, lw=2.2, label=f'{n:.2f} mol'.replace('.', ','))
    ax.plot([-273.15, -50], [0, Vf(-50)], color=c, lw=1.2, ls='--')
ax.plot(-273.15, 0, 'o', color=JT, ms=6); ax.annotate('−273,15 °C\n(0 K)', (-273.15, 0), (-250, 1.6), fontsize=9, color=JT, arrowprops=dict(arrowstyle='-', color=JT, lw=0.8))
ax.text(40, 0.25, 'garis padat: data (gas belum mencair)\ngaris putus: ekstrapolasi', fontsize=8, color='#555555')
ax.set_xlim(-300, 300); ax.set_ylim(0, 6); ax.set_xlabel('suhu (°C)'); ax.set_ylabel('$V$ pada 1 bar (L)'); ax.legend(frameon=False, fontsize=8.5, loc='upper left'); koma(ax)
f.tight_layout(); simpan(f, 'charles')

# 4. sebaran Maxwell–Boltzmann beberapa gas pada 298 K
f, ax = plt.subplots(figsize=(6.4, 3.0))
v = np.linspace(0, 2500, 600); T = 298.15
for nm, M, c in [('CO$_2$ (44)', 44.01e-3, TUA), ('N$_2$ (28)', 28.01e-3, BIRU), ('H$_2$O (18)', 18.02e-3, HJ), ('He (4)', 4.003e-3, JG)]:
    Fv = 4 * np.pi * (M / (2 * np.pi * Rg * T)) ** 1.5 * v ** 2 * np.exp(-M * v ** 2 / (2 * Rg * T))
    ax.plot(v, Fv * 1e3, color=c, lw=2, label=nm); vmp = np.sqrt(2 * Rg * T / M)
    ax.plot([vmp, vmp], [0, Fv.max() * 1e3], color=c, lw=0.8, ls=':')
ax.set_xlabel('kelajuan $v$ (m s$^{-1}$)'); ax.set_ylabel('$f(v)$ (10$^{-3}$ s m$^{-1}$)'); ax.set_xlim(0, 2500); ax.set_ylim(0, None)
ax.legend(frameon=False, fontsize=8.5, title='298 K, $M$ (g mol$^{-1}$)', title_fontsize=8.5); koma(ax)
f.tight_layout(); simpan(f, 'massa')

# 5. silinder tumbukan dan jalan bebas rata-rata
f, ax = plt.subplots(figsize=(7.0, 2.6)); ax.set_xlim(0, 20); ax.set_ylim(0, 6.4); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(Rectangle((1.6, 1.6), 15.0, 2.8, fc='#eaf3fb', ec=BIRU, lw=1, ls='--'))
from matplotlib.patches import Ellipse
ax.add_patch(Ellipse((1.6, 3.0), 0.9, 2.8, fc='#d6e8f7', ec=BIRU, lw=1)); ax.add_patch(Ellipse((16.6, 3.0), 0.9, 2.8, fc='none', ec=BIRU, lw=1, ls='--'))
ax.add_patch(Circle((1.6, 3.0), 0.7, fc=JT, ec='none')); panah(ax, (2.4, 3.0), (5.0, 3.0), JT, lw=1.8)
ax.annotate('', (0.6, 1.6), (0.6, 4.4), arrowprops=dict(arrowstyle='<->', color=TUA, lw=1)); ax.text(0.45, 3.0, '2$d$', ha='right', va='center', fontsize=9)
rng = np.random.default_rng(3)
for x, y, hit in [(5.6, 3.9, 1), (8.4, 2.1, 1), (11.0, 3.5, 1), (14.2, 2.6, 1), (6.8, 5.3, 0), (10.0, 0.8, 0), (13.0, 5.4, 0), (15.6, 0.9, 0), (4.0, 0.7, 0)]:
    ax.add_patch(Circle((x, y), 0.7, fc=BIRU if hit else MUDA, ec='white', lw=0.8, alpha=1 if hit else 0.8))
ax.text(9.0, 6.0, 'luas penampang tumbukan $\\sigma = \\pi d^2$', ha='center', fontsize=9, color=BIRU)
ax.annotate('', (1.6, 0.25), (16.6, 0.25), arrowprops=dict(arrowstyle='<->', color=TUA, lw=1)); ax.text(9.1, -0.25, 'panjang $\\bar v_\\mathrm{rel}\\,\\Delta t$ dalam selang $\\Delta t$', ha='center', va='top', fontsize=9)
ax.text(17.3, 3.0, 'molekul yang\npusatnya di dalam\nsilinder (biru tua)\nakan ditumbuk', fontsize=8.5, color=TUA, va='center')
simpan(f, 'silinder')
print('ok bab01')
