# Gambar Bab 8: python3 alat/gambar/bab08.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab08', 'fig')
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
R = 8.314
kom = FuncFormatter(lambda x, p: (f'{x:g}').replace('.', ',').replace('-', '−'))
def logfmt(x, p):
    s = f'{x:.6f}'.rstrip('0').rstrip('.')
    return s.replace('.', ',').replace('-', '−')

def diagram(nama, Tt, pt, Tc, pc, dHsub, lebur, Tmin, Tmax, pmin, pmax, label, titik, garis1atm=True, ekstra=()):
    f, ax = plt.subplots(figsize=(5.6, 4.0), dpi=220)
    B = np.log(pc / pt) / (1 / Tt - 1 / Tc)
    T = np.linspace(Tt, Tc, 300); ax.plot(T, pt * np.exp(-B * (1 / T - 1 / Tt)), color=TUA, lw=2.2)
    T = np.linspace(Tmin, Tt, 200); ax.plot(T, pt * np.exp(-dHsub / R * (1 / T - 1 / Tt)), color=TUA, lw=2.2)
    p = np.geomspace(pt, pmax, 200); ax.plot(Tt + (p - pt) / lebur, p, color=TUA, lw=2.2)
    ax.plot([Tt], [pt], 'o', color=JT, ms=6, zorder=5); ax.plot([Tc], [pc], 'o', color=JT, ms=6, zorder=5)
    for x, y in ekstra: ax.plot([x], [y], 's', color=HJ, ms=5, zorder=5)
    ax.set_yscale('log'); ax.set_xlim(Tmin, Tmax); ax.set_ylim(pmin, pmax)
    ax.yaxis.set_major_formatter(FuncFormatter(logfmt))
    if garis1atm: ax.axhline(1.01325, color=BIRU, lw=1, ls=':')
    for x, y, t, kw in label: ax.text(x, y, t, **kw)
    for x, y, t in titik: ax.text(x, y, t, fontsize=8.5, color=JT)
    ax.set_xlabel('T (K)'); ax.set_ylabel('p (bar)')
    f.tight_layout(); f.savefig(f'{D}/{nama}.png'); plt.close(f)

big = dict(fontsize=12, color=TUA, ha='center', fontweight='bold')
# air: titik tripel 273,16 K, 611,657 Pa; titik kritis 647,1 K, 220,64 bar
diagram('air', 273.16, 611.657e-5, 647.1, 220.64, 51060, -134.6, 200, 720, 1e-5, 2000,
        [(235, 1, 'PADAT', big), (400, 50, 'CAIR', big), (500, 1e-3, 'GAS', big), (690, 600, 'fluida\nsuperkritis', dict(fontsize=8.5, color=HJ, ha='center')),
         (705, 1.25, '1 atm', dict(fontsize=8, color=BIRU, ha='right'))],
        [(280, 2e-3, 'titik tripel\n273,16 K; 0,00612 bar'), (560, 330, 'titik kritis\n647 K; 221 bar')])
# CO2: tripel 216,55 K, 5,18 bar; kritis 304,13 K, 73,8 bar
diagram('co2', 216.55, 5.18, 304.13, 73.8, 26100, 50, 170, 330, 0.1, 1000,
        [(200, 150, 'PADAT', big), (262, 120, 'CAIR', big), (285, 1.5, 'GAS', big), (318, 400, 'fluida\nsuperkritis', dict(fontsize=8.5, color=HJ, ha='center')),
         (172, 1.2, '1 atm', dict(fontsize=8, color=BIRU))],
        [(222, 3.0, 'titik tripel\n216,6 K; 5,18 bar'), (272, 95, 'titik kritis\n304 K; 73,8 bar'), (198, 0.6, '194,7 K\n(menyublim)'), (291, 22, '298 K; 64 bar')],
        ekstra=[(194.65, 1.01325), (298.15, 64.3)])
# plot Clausius-Clapeyron
T = np.array([20, 40, 60, 80, 100]) + 273.15; P = np.array([2.339, 7.384, 19.946, 47.414, 101.325])
m, b = np.polyfit(1 / T, np.log(P), 1)
f, ax = plt.subplots(figsize=(5.0, 3.5), dpi=220)
x = np.linspace(2.62, 3.46, 50); ax.plot(x, m * x / 1000 + b, color=BIRU, lw=2)
ax.plot(1000 / T, np.log(P), 'o', color=JT, ms=7, zorder=5)
for t, xx, yy in zip([20, 40, 60, 80, 100], 1000 / T, np.log(P)): ax.text(xx + 0.03, yy + 0.12, f'{t} °C', fontsize=8.5, color=TUA)
ax.text(2.75, 1.4, f'kemiringan = {m:.0f} K'.replace('-', '−').replace('.', ','), fontsize=10, color=BIRU)
ax.set_xlabel(r'1000/T ($\mathregular{K^{-1}}$)'); ax.set_ylabel('ln (p/kPa)')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); f.savefig(f'{D}/cc.png'); plt.close(f)
print('slope', m)
