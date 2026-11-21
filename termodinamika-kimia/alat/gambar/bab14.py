# Gambar Bab 14: termodinamika statistik
import os, numpy as np, matplotlib
from math import comb, factorial
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Circle, FancyArrowPatch
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R}/bab14/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
h = 6.62607015e-34; k = 1.380649e-23; c = 2.99792458e10

# 1. keadaan mikro: 3 kuantum di antara 3 molekul (kiri), W untuk N=20 molekul 20 kuantum (kanan)
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.1), gridspec_kw={'width_ratios': [1.1, 1]})
a1.set_xlim(0, 11); a1.set_ylim(-0.6, 4.4); a1.axis('off')
konf = [((3, 0, 0), 3), ((2, 1, 0), 6), ((1, 1, 1), 1)]
for j, ((n1, n2, n3), W) in enumerate(konf):
    x0 = 0.4 + j * 3.6
    for i, nq in enumerate((n1, n2, n3)):
        xx = x0 + i * 1.0; a1.plot([xx - 0.35, xx + 0.35], [0, 0], color=TUA, lw=1)
        for q in range(nq): a1.add_patch(Circle((xx, 0.45 + q * 0.55), 0.2, color=JT))
        a1.text(xx, -0.35, 'ABC'[i], ha='center', fontsize=8.5, color='#555555')
    a1.text(x0 + 1.0, 2.6, f'({n1},{n2},{n3})', ha='center', fontsize=9); a1.text(x0 + 1.0, 3.3, f'W = {W}', ha='center', fontsize=10, color=BIRU, fontweight='bold')
a1.text(5.5, 4.2, '3 kuantum energi, 3 molekul: total 10 keadaan mikro', ha='center', fontsize=8.8, color=TUA)
N, Q = 20, 20
# distribusi energi satu molekul: peluang molekul tertentu memegang n kuantum = C(Q-n+N-2, N-2)/C(Q+N-1, N-1)
n = np.arange(0, 12); P = [comb(Q - m + N - 2, N - 2) / comb(Q + N - 1, N - 1) for m in n]
a2.bar(n, P, color=BIRU, width=0.7, label='hitung langsung (N = 20)')
nn = np.linspace(0, 11, 200); a2.plot(nn, 0.5 * np.exp(-nn * np.log(2)), color=JT, lw=2, label='eksponensial $\\propto e^{-\\varepsilon/kT}$')
a2.set_xlabel('kuantum yang dipegang satu molekul'); a2.set_ylabel('peluang'); a2.legend(frameon=False, fontsize=8); koma(a2)
a2.set_title('20 molekul berbagi 20 kuantum', fontsize=9)
f.tight_layout(); simpan(f, 'mikro')

# 2. sebaran Boltzmann pada tingkat berjarak sama, tiga suhu
f, axs = plt.subplots(1, 3, figsize=(7.2, 2.9), sharey=True); lv = np.arange(0, 10)
for ax, x, t in zip(axs, [2.0, 0.7, 0.25], ['$kT$ = ε/2 (dingin)', '$kT$ ≈ 1,4ε', '$kT$ = 4ε (panas)']):
    p = np.exp(-lv * x); p /= p.sum()
    ax.barh(lv, p, color=BIRU, height=0.55); ax.set_title(t, fontsize=9); ax.set_xlim(0, 0.9); ax.set_xlabel('populasi')
    ax.xaxis.set_major_formatter(kom)
axs[0].set_ylabel('tingkat energi (kelipatan ε)'); axs[0].set_yticks(lv)
f.tight_layout(); simpan(f, 'boltzmann')

# 3. fungsi partisi: sistem dua tingkat dan osilator harmonik terhadap kT/ε
f, ax = plt.subplots(figsize=(6.0, 3.1)); t = np.linspace(0.02, 6, 400)
ax.plot(t, 1 + np.exp(-1 / t), color=BIRU, lw=2.2, label='dua tingkat (0 dan ε)')
ax.plot(t, 1 / (1 - np.exp(-1 / t)), color=JT, lw=2.2, label='osilator harmonik (0, ε, 2ε, …)')
ax.plot(t, t, color=JT, lw=1, ls=':', label='batas klasik $kT$/ε')
ax.axhline(1, color='#999999', lw=0.8); ax.annotate('hanya keadaan dasar\nterjangkau ($q$ → 1)', xy=(0.12, 1.0), xytext=(0.5, 0.25), fontsize=8.3, color='#666666', arrowprops=dict(arrowstyle='->', color='#999999'))
ax.set_xlabel('$kT$/ε'); ax.set_ylabel('$q$'); ax.set_xlim(0, 6); ax.set_ylim(0, 6.5); ax.legend(frameon=False, fontsize=8.5, loc='upper left', bbox_to_anchor=(0, 0.92)); koma(ax)
f.tight_layout(); simpan(f, 'q')

# 4. populasi rotasi HCl pada 298 K dan 1000 K
th = h * c * 10.59 / k; J = np.arange(0, 21)
f, ax = plt.subplots(figsize=(6.2, 3.0))
for T, col, off in [(298.15, BIRU, -0.2), (1000, JT, 0.2)]:
    p = (2 * J + 1) * np.exp(-J * (J + 1) * th / T); p /= p.sum(); ax.bar(J + off, p, width=0.4, color=col, label=f'{T:g} K'.replace('.', ','))
ax.set_xlabel('bilangan kuantum rotasi $J$'); ax.set_ylabel('fraksi molekul'); ax.set_xticks(J[::2]); ax.legend(frameon=False, fontsize=8.5); koma(ax)
ax.text(10, 0.15, 'puncak: $(2J+1)$ naik, $e^{-E_J/kT}$ turun', fontsize=8.5, color=TUA)
f.tight_layout(); simpan(f, 'rotasi')

# 5. kapasitas kalor getaran (fungsi Einstein) dan titik molekul pada 298 K
f, ax = plt.subplots(figsize=(6.2, 3.1)); x = np.linspace(0.02, 3, 400)
E = lambda y: (1 / y) ** 2 * np.exp(1 / y) / (np.exp(1 / y) - 1) ** 2
ax.plot(x, E(x), color=BIRU, lw=2.2)
for nm, nu in [('H$_2$', 4401), ('N$_2$', 2358.6), ('O$_2$', 1580), ('Cl$_2$', 559.7), ('I$_2$', 214.5)]:
    tv = h * c * nu / k; xx = 298.15 / tv; ax.plot(xx, E(xx), 'o', color=JT, ms=5)
    off = {'H$_2$': (0.02, 0.30), 'N$_2$': (0.15, 0.20), 'O$_2$': (0.32, 0.10)}
    if nm in off: ax.annotate(nm, xy=(xx, E(xx)), xytext=off[nm], fontsize=8.5, color=JT, arrowprops=dict(arrowstyle='-', color=JT, lw=0.6))
    else: ax.text(xx + 0.03, E(xx) - 0.06, nm, fontsize=8.5, color=JT)
ax.axhline(1, color='#999999', lw=0.8, ls=':'); ax.text(2.2, 1.03, 'batas klasik: $R$ per mode', fontsize=8.3, color='#666666')
ax.set_xlabel('$T/\\theta_\\mathrm{v}$'); ax.set_ylabel('$C_{V,\\mathrm{getaran}}/R$'); ax.set_xlim(0, 3); ax.set_ylim(0, 1.12); koma(ax)
ax.text(1.4, 0.45, 'titik: tiap molekul pada 298 K', fontsize=8.5, color=JT)
f.tight_layout(); simpan(f, 'einstein')

# 6. entropi molar standar N2, Ar, He: sumbangan translasi/rotasi dibanding nilai tabel
f, ax = plt.subplots(figsize=(6.0, 3.0))
nm = ['He', 'Ar', 'N$_2$']; tr = [126.15, 154.85, 150.42]; ro = [0, 0, 41.14]; tab = [126.15, 154.84, 191.61]
x = np.arange(3); ax.bar(x, tr, color=BIRU, width=0.5, label='translasi (Sackur–Tetrode)'); ax.bar(x, ro, bottom=tr, color=HJ, width=0.5, label='rotasi')
ax.plot(x, tab, 'D', color=JT, ms=7, label='nilai kalorimetri (Tabel 6.1)')
for i in range(3): ax.text(i + 0.3, tab[i], f'{tr[i] + ro[i]:.1f}'.replace('.', ','), fontsize=8.5, va='center')
ax.set_xticks(x); ax.set_xticklabels(nm); ax.set_ylabel('$S_\\mathrm{m}^\\circ$ (J K$^{-1}$ mol$^{-1}$)'); ax.set_ylim(0, 240); ax.legend(frameon=False, fontsize=8.3, loc='upper left'); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'entropi')

# 7. fraksi molekul dengan energi > Ea terhadap T
f, ax = plt.subplots(figsize=(6.0, 3.0)); T = np.linspace(250, 400, 200); Rg = 8.314
for Ea, col in [(50, BIRU), (75, HJ), (100, JT)]: ax.semilogy(T, np.exp(-Ea * 1000 / (Rg * T)), color=col, lw=2, label=f'$E_\\mathrm{{a}}$ = {Ea} kJ mol$^{{-1}}$')
ax.axvline(298.15, color='#bbbbbb', lw=0.8, ls=':'); ax.axvline(308.15, color='#bbbbbb', lw=0.8, ls=':'); ax.text(300, 1e-21, '25 → 35 °C', fontsize=8.3, color='#666666')
ax.set_xlabel('$T$ (K)'); ax.set_ylabel('fraksi $e^{-E_\\mathrm{a}/RT}$'); ax.legend(frameon=False, fontsize=8.5, loc='lower right'); ax.xaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'arrhenius')
# 8. ketajaman puncak W: fraksi kepala pada N lemparan koin
from math import lgamma
f, ax = plt.subplots(figsize=(6.0, 2.9))
for N, col in [(10, MUDA), (100, BIRU), (1000, HJ), (10000, JT)]:
    nn = np.arange(0, N + 1); lw = np.array([lgamma(N + 1) - lgamma(i + 1) - lgamma(N - i + 1) for i in nn]); w = np.exp(lw - lw.max())
    ax.plot(nn / N, w, color=col, lw=2, label=f'N = {N:,}'.replace(',', '.'))
ax.set_xlabel('fraksi kepala $n/N$'); ax.set_ylabel('$W/W_\\mathrm{maks}$'); ax.set_xlim(0, 1); ax.legend(frameon=False, fontsize=8.5); koma(ax)
f.tight_layout(); simpan(f, 'tajam')
# 9. kesetimbangan A <=> B: B lebih tinggi energinya tetapi tingkatnya rapat
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0), gridspec_kw={'width_ratios': [0.8, 1.2]})
eA = np.arange(0, 8) * 1.0; eB = 2.0 + np.arange(0, 30) * 0.2
for e in eA[eA < 6.5]: a1.plot([0, 1], [e, e], color=BIRU, lw=1.6)
for e in eB[eB < 6.5]: a1.plot([1.6, 2.6], [e, e], color=JT, lw=1.0)
a1.text(0.5, -0.6, 'A', ha='center', fontsize=11, color=BIRU, fontweight='bold'); a1.text(2.1, -0.6, 'B', ha='center', fontsize=11, color=JT, fontweight='bold')
a1.annotate('', xy=(1.3, 2.0), xytext=(1.3, 0), arrowprops=dict(arrowstyle='<->', color=TUA)); a1.text(1.35, 0.9, '$\\Delta E_0$', fontsize=9, color=TUA)
a1.set_xlim(-0.2, 2.8); a1.set_ylim(-1, 6.6); a1.axis('off'); a1.set_title('tingkat energi (satuan ε)', fontsize=9)
tt = np.linspace(0.1, 6, 300)
qA = np.array([np.exp(-eA / t).sum() for t in tt]); qB = np.array([np.exp(-eB / t).sum() for t in tt])
a2.plot(tt, qB / (qA + qB), color=JT, lw=2.2, label='fraksi B'); a2.plot(tt, qA / (qA + qB), color=BIRU, lw=2.2, label='fraksi A')
a2.axhline(0.5, color='#bbbbbb', lw=0.8, ls=':')
a2.set_xlabel('$kT$/ε'); a2.set_ylabel('fraksi'); a2.set_ylim(0, 1); a2.set_xlim(0, 6); a2.legend(frameon=False, fontsize=8.5, loc='center right'); koma(a2)
a2.text(0.12, 0.62, 'dingin:\nenergi\nmenang', fontsize=8.3, color=BIRU, va='top', ha='left', transform=a2.transData); a2.text(2.9, 0.9, 'panas: banyak keadaan menang', fontsize=8.3, color=JT)
f.tight_layout(); simpan(f, 'setimbang')
print('ok bab14')
