# Gambar tambahan Bab 2 (perbaikan total): python3 alat/gambar/bab02b.py
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab02/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)

# 1. diagram Z umum dari van der Waals tereduksi
f, ax = plt.subplots(figsize=(6.4, 3.4))
def Z_vdw(pr, Tr):
    # cari akar V_r terbesar (uap) dari pr = 8Tr/(3Vr-1) - 3/Vr^2
    c = [3 * pr, -(pr + 8 * Tr), 9, -3]; r = np.roots(c); r = r[np.isreal(r)].real; r = r[r > 1 / 3]
    Vr = r.max() if pr < 1 or Tr > 1 else r.max(); return 3 * pr * Vr / (8 * Tr)
pr = np.linspace(0.01, 8, 400)
for Tr, c in [(1.0, JT), (1.2, JG), (1.5, HJ), (2.0, BIRU), (3.0, TUA)]:
    Z = [Z_vdw(p, Tr) for p in pr]
    if Tr == 1.0: Z = [Z_vdw(p, Tr) if p <= 1 else np.nan for p in pr]
    ax.plot(pr, Z, color=c, lw=2, label=f'$T_r$ = {Tr:g}'.replace('.', ','))
ax.axhline(1, color='#999999', lw=0.8, ls='--'); ax.text(0.15, 1.04, 'gas ideal', ha='left', fontsize=8.5, color='#777777')
ax.set_xlabel('tekanan tereduksi $p_r = p/p_\\mathrm{c}$'); ax.set_ylabel('$Z = pV_\\mathrm{m}/RT$'); ax.set_xlim(0, 8); ax.set_ylim(0, 1.5)
ax.legend(frameon=False, fontsize=8.5, ncol=1, loc='lower right'); koma(ax)
f.tight_layout(); simpan(f, 'zumum')

# 2. koefisien virial kedua B(T) dicocokkan pada data Tabel 2.3 (B = b' - a'/T)
f, ax = plt.subplots(figsize=(6.4, 3.0)); T = np.linspace(150, 1000, 300)
for nm, B273, TB, c in [('He', 11.9, 22.6, JG), ('N$_2$', -10.5, 327.2, BIRU), ('Ar', -21.7, 411.5, HJ), ('CO$_2$', -149.7, 714.8, TUA)]:
    a_ = B273 / (1 / TB - 1 / 273.15); b_ = a_ / TB; ax.plot(T, b_ - a_ / T, color=c, lw=2, label=nm)
    if TB > 150: ax.plot(TB, 0, 'o', color=c, ms=5)
ax.axhline(0, color='#999999', lw=0.8); ax.text(560, -45, 'titik: suhu Boyle $T_\\mathrm{B}$ ($B$ = 0)', fontsize=8.5, color='#555555')
ax.set_xlabel('$T$ (K)'); ax.set_ylabel('$B$ (cm$^3$ mol$^{-1}$)'); ax.set_ylim(-250, 60); ax.set_xlim(150, 1000); ax.legend(frameon=False, fontsize=8.5, loc='lower right'); koma(ax)
f.tight_layout(); simpan(f, 'virialB')

# 3. kurva inversi Joule–Thomson van der Waals (tereduksi) dan data N2
f, ax = plt.subplots(figsize=(6.0, 3.3))
V = np.concatenate([np.linspace(0.45, 5, 4000), np.logspace(np.log10(5), 4, 4000)]); Tq = (-6 / V ** 2) / (8 / (3 * V - 1) - 24 * V / (3 * V - 1) ** 2); pq = 8 * Tq / (3 * V - 1) - 3 / V ** 2
ok = (Tq > 0) & (pq > 0); ax.plot(pq[ok], Tq[ok], color=TUA, lw=2.2)
ax.fill(np.r_[0, pq[ok], 0], np.r_[Tq[ok][0], Tq[ok], Tq[ok][-1]], color=MUDA, alpha=0.35, lw=0)
ax.text(3.5, 2.6, 'μ$_\\mathrm{JT}$ > 0\nmendingin saat memuai', ha='center', fontsize=9, color=BIRU)
ax.text(6.3, 6.0, 'μ$_\\mathrm{JT}$ < 0\nmemanas saat memuai', ha='center', fontsize=9, color=JT)
ax.annotate('suhu inversi atas\n$T_r$ = 6,75 (= 2$a$/$Rb$)', (0.05, 6.75), (2.2, 7.4), fontsize=8.5, color=TUA, arrowprops=dict(arrowstyle='->', color=TUA, lw=0.8))
ax.set_xlabel('$p_r$'); ax.set_ylabel('$T_r$'); ax.set_xlim(0, 10); ax.set_ylim(0, 8); koma(ax)
f.tight_layout(); simpan(f, 'inversi')

# 4. diagram fasa CO2 dengan daerah superkritis
f, ax = plt.subplots(figsize=(6.0, 3.4))
Tt, pt, Tc, pc = 216.58, 5.185, 304.13, 73.77
Tv = np.linspace(Tt, Tc, 100); Hv = np.log(pc / pt) / (1 / Tt - 1 / Tc); pv = pt * np.exp(-Hv * (1 / Tv - 1 / Tt))
Ts = np.linspace(170, Tt, 60); Hs = 3200 * 0 + 26100 / 8.314; ps = pt * np.exp(-Hs * (1 / Ts - 1 / Tt))
ax.semilogy(Tv, pv, color=TUA, lw=2); ax.semilogy(Ts, ps, color=TUA, lw=2); ax.semilogy([Tt, Tt + 6], [pt, 300], color=TUA, lw=2)
ax.fill_between([Tc, 340], [pc, pc], [400, 400], color=JG, alpha=0.3); ax.text(322, 160, 'fluida\nsuperkritis', ha='center', fontsize=9, color=JT)
ax.plot(Tc, pc, 'o', color=JT, ms=6); ax.annotate('titik kritis\n304,1 K; 73,8 bar', (Tc, pc), (262, 140), fontsize=8.5, color=JT, arrowprops=dict(arrowstyle='->', color=JT, lw=0.8))
ax.plot(Tt, pt, 'o', color=BIRU, ms=6); ax.annotate('titik tripel\n216,6 K; 5,2 bar', (Tt, pt), (232, 1.6), fontsize=8.5, color=BIRU, arrowprops=dict(arrowstyle='->', color=BIRU, lw=0.8))
ax.text(195, 40, 'padat', fontsize=10, color=TUA); ax.text(255, 60, 'cair', fontsize=10, color=TUA); ax.text(290, 8, 'gas', fontsize=10, color=TUA)
ax.axhline(1.013, color='#999999', lw=0.8, ls=':'); ax.text(228, 1.15, '1 atm: es kering menyublim pada 194,7 K', fontsize=8, color='#666666')
ax.set_xlim(170, 340); ax.set_ylim(0.5, 400); ax.set_xlabel('$T$ (K)'); ax.set_ylabel('$p$ (bar, skala log)')
ax.yaxis.set_major_formatter(kom); ax.xaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'co2')
print('ok bab02b')
