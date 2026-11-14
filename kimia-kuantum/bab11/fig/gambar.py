#!/usr/bin/env python3
# Gambar Bab 11 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
# h2p_eksak.json: energi total eksak H2+ (1sσg dan 2pσu, hartree) dari penyelesaian koordinat eliptik (Contoh 11.c2).
import json, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle
from scipy.special import expi
from scipy.interpolate import CubicSpline
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'mathtext.fontset': 'dejavusans',
                     'text.color': '#0e2748', 'axes.edgecolor': '#0e2748', 'axes.labelcolor': '#0e2748',
                     'xtick.color': '#0e2748', 'ytick.color': '#0e2748'})
TUA, B, MUDA, J1, J2, H = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
EV = 27.211386
KOMA = FuncFormatter(lambda x, p: ('%g' % x).replace('.', ',').replace('-', '−'))
CM = LinearSegmentedColormap.from_list('bj', [J2, J1, '#ffffff', MUDA, B])
def sv(f, n): f.savefig(n, dpi=220, bbox_inches='tight'); plt.close(f)
def sp(ax):
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
def koma(ax, x=True, y=True):
    if x: ax.xaxis.set_major_formatter(KOMA)
    if y: ax.yaxis.set_major_formatter(KOMA)
def SJK(R):
    S = np.exp(-R) * (1 + R + R * R / 3); J = -(1 - (1 + R) * np.exp(-2 * R)) / R; K = -(1 + R) * np.exp(-R)
    return S, J, K
def lcao_h2p(R):
    S, J, K = SJK(R); return -0.5 + 1 / R + (J + K) / (1 + S), -0.5 + 1 / R + (J - K) / (1 - S)

# ------------------------------------------------ 1. koordinat
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.7))
ax = axs[0]; ax.set_aspect('equal'); ax.axis('off')
A, Bp, e = np.array([-1, 0]), np.array([1, 0]), np.array([0.35, 1.15])
ax.plot(*zip(A, Bp), color=TUA, lw=1); ax.plot(*zip(A, e), color=B, lw=1.2); ax.plot(*zip(Bp, e), color=J2, lw=1.2)
for P, t in [(A, 'A'), (Bp, 'B')]: ax.add_patch(Circle(P, 0.09, color=TUA)); ax.text(P[0], P[1] - 0.28, t, ha='center', fontsize=9)
ax.add_patch(Circle(e, 0.06, color=H)); ax.text(e[0] + 0.1, e[1] + 0.08, 'e$^-$', fontsize=9)
ax.text(-0.5, 0.65, '$r_A$', color=B, fontsize=10); ax.text(0.78, 0.6, '$r_B$', color=J2, fontsize=10); ax.text(0, -0.25, '$R$', ha='center', fontsize=10)
ax.annotate('', xy=(1.7, 0), xytext=(-1.7, 0), arrowprops=dict(arrowstyle='->', color='#999', lw=0.7)); ax.text(1.72, 0.05, '$z$', fontsize=9)
ax.set_xlim(-1.8, 1.9); ax.set_ylim(-0.6, 1.5)
ax = axs[1]; ax.set_aspect('equal'); sp(ax); ax.axis('off')
R = 2.0; mu = np.linspace(-1, 1, 300)
for lam in [1.15, 1.4, 1.8, 2.4]:
    z = R / 2 * lam * mu; rho = R / 2 * np.sqrt((lam ** 2 - 1) * (1 - mu ** 2))
    ax.plot(z, rho, color=B, lw=1); ax.plot(z, -rho, color=B, lw=1)
lams = np.linspace(1, 3, 300)
for m in [-0.75, -0.4, 0, 0.4, 0.75]:
    z = R / 2 * lams * m; rho = R / 2 * np.sqrt((lams ** 2 - 1) * (1 - m ** 2))
    ax.plot(z, rho, color=J1, lw=1); ax.plot(z, -rho, color=J1, lw=1)
for P in (-1, 1): ax.add_patch(Circle((P, 0), 0.07, color=TUA))
ax.text(-1, -0.3, 'A', ha='center'); ax.text(1, -0.3, 'B', ha='center')
ax.text(2.45, 0.95, '$\\lambda$ tetap', color=B, fontsize=8.5); ax.text(1.9, 2.0, '$\\mu$ tetap', color=J2, fontsize=8.5)
ax.set_xlim(-3, 3.3); ax.set_ylim(-2.3, 2.3)
sv(f, 'c_koordinat.png')

# ------------------------------------------------ 2. kurva H2+ eksak vs LCAO
d = json.load(open('h2p_eksak.json')); Rx, Eg, Eu = map(np.array, (d['R'], d['g'], d['u']))
f, ax = plt.subplots(figsize=(5.6, 3.6)); sp(ax)
Rs = np.linspace(0.6, 10, 300); Lp, Lm = lcao_h2p(Rs)
ax.plot(Rx, (Eg + 0.5) * EV, color=B, lw=2, label='eksak $1\\sigma_g$'); ax.plot(Rx, (Eu + 0.5) * EV, color=J2, lw=2, label='eksak $1\\sigma_u$')
ax.plot(Rs, (Lp + 0.5) * EV, color=B, lw=1.2, ls='--', label='LCAO $\\psi_+$'); ax.plot(Rs, (Lm + 0.5) * EV, color=J2, lw=1.2, ls='--', label='LCAO $\\psi_-$')
ax.axhline(0, color='#999', lw=0.6); ax.set_xlim(0.5, 10); ax.set_ylim(-3.5, 9)
ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('$E - E(\\mathrm{H} + \\mathrm{H}^+)$ (eV)'); koma(ax); ax.legend(frameon=False, fontsize=8)
sv(f, 'c_kurva_h2p.png')

# ------------------------------------------------ 3. integral S, J, K
Rs = np.linspace(0.05, 6, 400); S, J, K = SJK(Rs)
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
ax = axs[0]; sp(ax)
ax.plot(Rs, S, color=H, lw=1.8, label='$S$'); ax.plot(Rs, J, color=B, lw=1.8, label='$J$'); ax.plot(Rs, K, color=J2, lw=1.8, label='$K$')
ax.plot(Rs[Rs > 0.8], -1 / Rs[Rs > 0.8], color='#999', ls=':', lw=1, label='$-1/R$')
ax.axhline(0, color='#bbb', lw=0.5); ax.set_ylim(-1.3, 1.05); ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('hartree'); koma(ax); ax.legend(frameon=False, fontsize=8, ncol=2)
ax = axs[1]; sp(ax); Rs = np.linspace(0.8, 6, 300); S, J, K = SJK(Rs); Lp, Lm = lcao_h2p(Rs)
ax.plot(Rs, (J + 1 / Rs) * EV, color='#777', lw=1.6, label='klasik: $J + 1/R$')
ax.plot(Rs, (Lp + 0.5) * EV, color=B, lw=1.8, label='$E_+ - E_{1s}$'); ax.plot(Rs, (Lm + 0.5) * EV, color=J2, lw=1.8, label='$E_- - E_{1s}$')
ax.axhline(0, color='#bbb', lw=0.5); ax.set_ylim(-2.5, 6); ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('eV'); koma(ax); ax.legend(frameon=False, fontsize=8)
f.tight_layout(); sv(f, 'c_integral.png')

# ------------------------------------------------ 4. orbital H2+ (LCAO, R = 2)
x = np.linspace(-3.5, 3.5, 351); zz = np.linspace(-3, 3, 301); X, Z = np.meshgrid(x, zz)
R = 2.0; S = SJK(R)[0]
rA = np.sqrt((X + R / 2) ** 2 + Z ** 2); rB = np.sqrt((X - R / 2) ** 2 + Z ** 2)
a = np.exp(-rA) / np.sqrt(np.pi); b = np.exp(-rB) / np.sqrt(np.pi)
pp = (a + b) / np.sqrt(2 * (1 + S)); pm = (a - b) / np.sqrt(2 * (1 - S)); dr = pp ** 2 - 0.5 * (a ** 2 + b ** 2)
f, axs = plt.subplots(1, 3, figsize=(6.9, 2.3))
for ax, F, t in [(axs[0], pp, '$\\psi_+ = 1\\sigma_g$'), (axs[1], pm, '$\\psi_- = 1\\sigma_u$'), (axs[2], dr, 'kerapatan selisih')]:
    m = np.abs(F).max(); ax.contourf(X, Z, F, levels=np.linspace(-m, m, 21), cmap=CM)
    ax.contour(X, Z, F, levels=np.linspace(-m, m, 11), colors=TUA, linewidths=0.4)
    ax.plot([-1, 1], [0, 0], 'o', color='k', ms=3); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(t, fontsize=8.5)
    for s in ax.spines.values(): s.set_visible(False)
sv(f, 'c_orbital_h2p.png')

# ------------------------------------------------ 5. diagram korelasi
f, ax = plt.subplots(figsize=(5.8, 4.2)); sp(ax)
T = lambda E: -np.log10(-np.asarray(E))
data = [('$1s\\sigma_g$', -2, -1.1026, -0.5, '$\\sigma_g1s$', B), ('$2p\\sigma_u$', -0.5, -0.6675, -0.5, '$\\sigma_u^*1s$', B),
        ('$2s\\sigma_g$', -0.5, -0.3609, -0.125, '$\\sigma_g2s$', B), ('$2p\\pi_u$', -0.5, -0.4288, -0.125, '$\\pi_u2p$', H),
        ('$3p\\sigma_u$', -2 / 9, -0.2554, -0.125, '$\\sigma_u^*2s$', B), ('$3d\\sigma_g$', -2 / 9, -0.2358, -0.125, '$\\sigma_g2p$', B),
        ('$3d\\pi_g$', -2 / 9, -0.2267, -0.125, '$\\pi_g^*2p$', H)]
for nm, e0, e1, e2, kan, c in data:
    ax.plot([0, 1, 2], [T(e0), T(e1), T(e2)], color=c, lw=1.2, marker='o', ms=3)
pos = {'$2s\\sigma_g$': (0.66, 0.49, 'right'), '$2p\\pi_u$': (1.07, 0.322, 'left'), '$3p\\sigma_u$': (0.66, 0.555, 'right'),
       '$3d\\sigma_g$': (0.66, 0.725, 'right'), '$3d\\pi_g$': (0.66, 0.79, 'right')}
for nm, e0, e1, e2, kan, c in data:
    if nm in pos:
        x0, y0, ha = pos[nm]
        ax.annotate(nm, xy=(1, T(e1)), xytext=(x0, y0), fontsize=7.2, va='center', ha=ha, color=c,
                    arrowprops=dict(arrowstyle='-', color=c, lw=0.5, shrinkA=1, shrinkB=2))
    else: ax.text(1.05, T(e1), nm, fontsize=7.2, va='center', color=c)
kanan = [('$\\sigma_g1s$, $\\sigma_u^*1s$', -0.5), ('$\\sigma_g2s$, $\\sigma_u^*2s$, $\\sigma_g2p$,\n$\\pi_u2p$, $\\pi_g^*2p$, ...', -0.125)]
for t, e in kanan: ax.text(2.08, T(e), t, fontsize=7.2, va='center')
for t, e in [('He$^+$ 1s', -2), ('He$^+$ 2s, 2p', -0.5), ('He$^+$ 3s, 3p, 3d', -2 / 9)]: ax.text(-0.08, T(e), t, fontsize=7.2, va='center', ha='right')
ax.set_xticks([0, 1, 2]); ax.set_xticklabels(['$R = 0$', '$R = 2$ bohr', '$R = \\infty$'])
yt = [-2, -1, -0.5, -0.3, -0.2, -0.125]; ax.set_yticks([T(v) for v in yt]); ax.set_yticklabels([('%g' % v).replace('.', ',').replace('-', '−') for v in yt])
ax.set_ylabel('$E_\\mathrm{el}$ (hartree)'); ax.set_xlim(-0.75, 2.9)
sv(f, 'c_korelasi.png')

# ------------------------------------------------ 6. bentuk orbital sigma, pi, delta
x = np.linspace(-4.2, 4.2, 281); zz = np.linspace(-3.2, 3.2, 215); X, Z = np.meshgrid(x, zz); R = 2.2; Zs = 2.6
def s2(dx): r = np.sqrt((X - dx) ** 2 + Z ** 2); return r * np.exp(-Zs * r / 2)
def pz(dx, sgn): r = np.sqrt((X - dx) ** 2 + Z ** 2); return sgn * (X - dx) * np.exp(-Zs * r / 2)
def px(dx): r = np.sqrt((X - dx) ** 2 + Z ** 2); return Z * np.exp(-Zs * r / 2)
def dd(dx): r = np.sqrt((X - dx) ** 2 + Z ** 2); return 0.5 * Z ** 2 * np.exp(-1.6 * r)
orbs = [('$\\sigma_g2s$', s2(-R / 2) + s2(R / 2)), ('$\\sigma_u^*2s$', s2(-R / 2) - s2(R / 2)),
        ('$\\sigma_g2p$', pz(-R / 2, 1) + pz(R / 2, -1)), ('$\\sigma_u^*2p$', pz(-R / 2, 1) - pz(R / 2, -1)),
        ('$\\pi_u2p$', px(-R / 2) + px(R / 2)), ('$\\pi_g^*2p$', px(-R / 2) - px(R / 2)),
        ('$\\delta_g$', dd(-R / 2) + dd(R / 2)), ('$\\delta_u^*$', dd(-R / 2) - dd(R / 2))]
f, axs = plt.subplots(2, 4, figsize=(6.9, 3.5))
for ax, (t, F) in zip(axs.flat, orbs):
    m = np.abs(F).max(); ax.contourf(X, Z, F, levels=np.linspace(-m, m, 21), cmap=CM)
    ax.contour(X, Z, F, levels=[-0.6 * m, -0.3 * m, -0.1 * m, 0.1 * m, 0.3 * m, 0.6 * m], colors=TUA, linewidths=0.35)
    ax.plot([-R / 2, R / 2], [0, 0], 'o', color='k', ms=2.5); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(t, fontsize=9)
    for s in ax.spines.values(): s.set_visible(False)
f.subplots_adjust(wspace=0.05, hspace=0.15); sv(f, 'c_sigmapi.png')

# ------------------------------------------------ 7. tren diatom periode 2
mol = ['Li₂', 'Be₂', 'B₂', 'C₂', 'N₂', 'O₂', 'F₂', 'Ne₂']; orde = [1, 0, 1, 2, 3, 2, 1, 0]
D0 = [1.05, 0.10, 2.8, 6.2, 9.76, 5.12, 1.60, 0.003]; Re = [267, 245, 159, 124, 110, 121, 141, 310]
f, axs = plt.subplots(2, 1, figsize=(5.6, 4.2), sharex=True)
ax = axs[0]; sp(ax); xx = np.arange(8)
ax.bar(xx, orde, color=MUDA, width=0.6, label='orde ikatan'); ax.set_ylabel('orde ikatan'); ax.set_ylim(0, 3.6)
ax2 = ax.twinx(); ax2.plot(xx, D0, 'o-', color=J2, lw=1.5, label='$D_0$'); ax2.set_ylabel('$D_0$ (eV)', color=J2); ax2.set_ylim(0, 11); ax2.spines['top'].set_visible(False)
koma(ax2); ax.text(4.0, 3.2, 'batang: orde ikatan;  titik: $D_0$', fontsize=7.5, ha='center')
ax = axs[1]; sp(ax); ax.plot(xx, Re, 's-', color=B, lw=1.5); ax.set_ylabel('$R_e$ (pm)'); ax.set_xticks(xx); ax.set_xticklabels(mol)
sv(f, 'c_tren.png')

# ------------------------------------------------ 8 dan 12. diagram OM (fungsi umum)
def diagram(ax, kiri, kanan, mos, judul, ylim):
    sp(ax); ax.spines['bottom'].set_visible(False); ax.set_xticks([])
    def lv(x, E, w, c=TUA): ax.plot([x - w / 2, x + w / 2], [E, E], color=c, lw=1.8, solid_capstyle='round')
    for lab, E, n in kiri:
        xs = [0.5] if n == 1 else [0.25, 0.5, 0.75]
        for xv in xs: lv(xv, E, 0.2)
        ax.text(0.5, E - 0.9, lab, ha='center', va='top', fontsize=7)
    for lab, E, n in kanan:
        xs = [4.5] if n == 1 else [4.25, 4.5, 4.75]
        for xv in xs: lv(xv, E, 0.2)
        ax.text(4.5, E - 0.9, lab, ha='center', va='top', fontsize=7)
    ys = []
    for lab, E, deg, ne, kosong in sorted(mos, key=lambda m: m[1]):
        y = E if not ys or E - ys[-1] >= 1.3 else ys[-1] + 1.3
        ys.append(y)
    ylab = dict(zip([m[0] for m in sorted(mos, key=lambda m: m[1])], ys))
    for lab, E, deg, ne, kosong in mos:
        xs = [2.5] if deg == 1 else [2.2, 2.8]
        c = '#999' if kosong else TUA
        if deg == 1: isi = ['↑↓' if ne == 2 else ('↑' if ne == 1 else '')]
        else: isi = {0: ['', ''], 1: ['↑', ''], 2: ['↑', '↑'], 3: ['↑↓', '↑'], 4: ['↑↓', '↑↓']}[ne]
        for xv, t in zip(xs, isi):
            lv(xv, E, 0.45, c)
            if t: ax.text(xv, E + 0.15, t, ha='center', va='bottom', fontsize=7.5, color=J2, fontweight='bold')
        ax.text(3.2, ylab[lab], lab, va='center', fontsize=7.5, color=c)
    ax.set_xlim(-0.2, 5.2); ax.set_ylim(*ylim); ax.set_title(judul, fontsize=9); koma(ax, x=False)
f, axs = plt.subplots(1, 2, figsize=(6.8, 4.6), sharey=True)
diagram(axs[0], [('O 2s', -32.4, 1), ('O 2p', -15.9, 3)], [('O 2s', -32.4, 1), ('O 2p', -15.9, 3)],
        [('$2\\sigma_g$', -40.0, 1, 2, False), ('$2\\sigma_u$', -24.6, 1, 2, False), ('$3\\sigma_g$', -18.2, 1, 2, False), ('$1\\pi_u$', -16.7, 2, 4, False),
         ('$1\\pi_g$', -12.3, 2, 2, False), ('$3\\sigma_u$', -6.0, 1, 0, True)], 'O₂', (-42, -2))
diagram(axs[1], [('N 2s', -25.6, 1), ('N 2p', -13.2, 3)], [('N 2s', -25.6, 1), ('N 2p', -13.2, 3)],
        [('$2\\sigma_g$', -37.3, 1, 2, False), ('$2\\sigma_u$', -18.75, 1, 2, False), ('$1\\pi_u$', -16.9, 2, 4, False), ('$3\\sigma_g$', -15.58, 1, 2, False),
         ('$1\\pi_g$', -7.0, 2, 0, True), ('$3\\sigma_u$', -4.0, 1, 0, True)], 'N₂', (-42, -2))
axs[0].set_ylabel('energi (eV)'); sv(f, 'c_mo_n2o2.png')
f, axs = plt.subplots(1, 2, figsize=(6.8, 4.4), sharey=True)
diagram(axs[0], [('H 1s', -13.6, 1)], [('F 2s', -40.2, 1), ('F 2p', -18.7, 3)],
        [('$2\\sigma$', -39.6, 1, 2, False), ('$3\\sigma$', -19.1, 1, 2, False), ('$1\\pi$', -16.0, 2, 4, False), ('$4\\sigma^*$', -5.0, 1, 0, True)], 'HF', (-43, 0))
diagram(axs[1], [('C 2s', -19.4, 1), ('C 2p', -10.7, 3)], [('O 2s', -32.4, 1), ('O 2p', -15.9, 3)],
        [('$3\\sigma$', -38.3, 1, 2, False), ('$4\\sigma$', -19.7, 1, 2, False), ('$1\\pi$', -16.9, 2, 4, False), ('$5\\sigma$', -14.0, 1, 2, False),
         ('$2\\pi^*$', -4.0, 2, 0, True), ('$6\\sigma^*$', -1.5, 1, 0, True)], 'CO', (-43, 0))
axs[0].set_ylabel('energi (eV)'); sv(f, 'c_mo_hf_co.png')

# ------------------------------------------------ 9. kurva H2: OM, HL, CI (zeta = 1)
g = 0.5772156649
def integral(R, z=1.0):
    w = z * R; e = np.exp
    S = e(-w) * (1 + w + w * w / 3); Sp = e(w) * (1 - w + w * w / 3)
    Haa = z * z / 2 - z - (1 - (1 + w) * e(-2 * w)) / R; Hab = -z * z * S / 2 + (z * z - 2 * z) * (1 + w) * e(-w)
    aaaa = 5 * z / 8; aabb = z * (1 / w - e(-2 * w) * (1 / w + 11 / 8 + 3 * w / 4 + w * w / 6))
    aaab = z * (e(-w) * (w + 1 / 8 + 5 / (16 * w)) - e(-3 * w) * (1 / 8 + 5 / (16 * w)))
    abab = z / 5 * (-e(-2 * w) * (-25 / 8 + 23 * w / 4 + 3 * w * w + w ** 3 / 3) + 6 / w * (S * S * (g + np.log(w)) + Sp * Sp * expi(-4 * w) - 2 * S * Sp * expi(-2 * w)))
    return S, Haa, Hab, aaaa, aabb, aaab, abab
def h2(R):
    S, Haa, Hab, aaaa, aabb, aaab, abab = integral(R)
    hg, hu = (Haa + Hab) / (1 + S), (Haa - Hab) / (1 - S)
    Jgg = (aaaa + aabb + 2 * abab + 4 * aaab) / (2 * (1 + S) ** 2); Juu = (aaaa + aabb + 2 * abab - 4 * aaab) / (2 * (1 - S) ** 2); Kgu = (aaaa - aabb) / (2 * (1 - S * S))
    OM = 2 * hg + Jgg + 1 / R; HL = (2 * Haa + aabb + 2 * S * Hab + abab) / (1 + S * S) + 1 / R
    CI = np.linalg.eigvalsh(np.array([[2 * hg + Jgg, Kgu], [Kgu, 2 * hu + Juu]]))[0] + 1 / R
    return OM, HL, CI
Rs = np.linspace(0.7, 9, 200); V = np.array([h2(r) for r in Rs])
f, ax = plt.subplots(figsize=(5.6, 3.6)); sp(ax)
for i, (t, c) in enumerate([('OM', B), ('Heitler–London', H), ('CI', J2)]): ax.plot(Rs, (V[:, i] + 1) * EV, color=c, lw=1.8, label=t)
ax.plot([1.401], [-4.747], '*', color=TUA, ms=11, label='minimum eksak')
ax.axhline(0, color='#999', lw=0.6); ax.axhline(0.3125 * EV, color=B, lw=0.6, ls=':'); ax.text(6.2, 0.3125 * EV + 0.25, 'batas OM: 8,5 eV', fontsize=7.5, color=B)
ax.set_xlim(0.7, 9); ax.set_ylim(-5.5, 10); ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('$E - 2E(\\mathrm{H})$ (eV)'); koma(ax); ax.legend(frameon=False, fontsize=8, loc='center right')
sv(f, 'c_h2.png')

# ------------------------------------------------ 10. virial H2+ eksak
cs = CubicSpline(Rx, Eg); dE = cs.derivative(); Rs = np.linspace(0.9, 10, 400)
E_ = cs(Rs); T_ = -E_ - Rs * dE(Rs); V_ = 2 * E_ + Rs * dE(Rs)
f, ax = plt.subplots(figsize=(5.6, 3.5)); sp(ax)
ax.plot(Rs, (E_ + 0.5), color=TUA, lw=2, label='$\\Delta E$'); ax.plot(Rs, T_ - 0.5, color=J2, lw=1.8, label='$\\Delta T$'); ax.plot(Rs, V_ + 1, color=B, lw=1.8, label='$\\Delta V$')
ax.axhline(0, color='#999', lw=0.6); ax.axvline(1.997, color='#bbb', lw=0.6, ls='--'); ax.text(2.05, 0.33, '$R_e$', fontsize=8)
ax.set_xlim(0.9, 10); ax.set_ylim(-0.4, 0.4); ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('perubahan energi (hartree)'); koma(ax); ax.legend(frameon=False, fontsize=8.5)
sv(f, 'c_virial.png')

# ------------------------------------------------ 11. daerah mengikat (Berlin)
x = np.linspace(-4, 4, 401); zz = np.linspace(-3, 3, 301); X, Z = np.meshgrid(x, zz); R = 2.0
rA = np.sqrt((X + R / 2) ** 2 + Z ** 2) + 1e-9; rB = np.sqrt((X - R / 2) ** 2 + Z ** 2) + 1e-9
cA = (X + R / 2) / rA; cB = -(X - R / 2) / rB
fb = cA / rA ** 2 + cB / rB ** 2
zt = 1.24; a = np.exp(-zt * rA); b = np.exp(-zt * rB); rho = (a + b) ** 2
f, ax = plt.subplots(figsize=(5.4, 3.4)); ax.set_aspect('equal')
ax.contourf(X, Z, (fb > 0).astype(float), levels=[0.5, 1.5], colors=[MUDA], alpha=0.55)
ax.contour(X, Z, fb, levels=[0], colors=B, linewidths=1.2)
ax.contour(X, Z, rho / rho.max(), levels=[0.02, 0.05, 0.1, 0.2, 0.4, 0.7], colors=TUA, linewidths=0.6)
ax.plot([-1, 1], [0, 0], 'o', color='k', ms=4)
ax.text(0, 2.2, 'daerah mengikat', ha='center', fontsize=8.5, color=B); ax.text(-3.2, 0.3, 'antiikat', fontsize=8.5, color=J2); ax.text(2.4, 0.3, 'antiikat', fontsize=8.5, color=J2)
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
sv(f, 'c_berlin.png')
print('selesai')

# ------------------------------------------------ 13. tingkat getaran H2+ dari kurva eksak
from scipy.linalg import eigh_tridiagonal
U = CubicSpline(Rx, Eg); mu = 1836.15267 / 2
Rg = np.linspace(0.8, 12, 6000); hh = Rg[1] - Rg[0]
Ev, Sv = eigh_tridiagonal(1 / (mu * hh ** 2) + U(Rg), -np.ones(len(Rg) - 1) / (2 * mu * hh ** 2), select='v', select_range=(-0.7, -0.5))
f, ax = plt.subplots(figsize=(5.4, 3.5)); sp(ax)
Rp = np.linspace(1.0, 11, 400); ax.plot(Rp, (U(Rp) + 0.5) * EV, color=TUA, lw=1.8)
for e in Ev:
    m = U(Rp) <= e; ax.plot(Rp[m], np.full(m.sum(), (e + 0.5) * EV), color=B, lw=0.8)
ax.axhline(0, color='#999', lw=0.7, ls='--'); ax.set_xlim(1.0, 11); ax.set_ylim(-2.9, 0.4)
ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('$E - E(\\mathrm{H} + \\mathrm{H}^+)$ (eV)'); koma(ax)
sv(f, 'c_vib_h2p.png')
print('tingkat:', len(Ev))

# ------------------------------------------------ 14. H2 RHF/UHF/FCI (PySCF, cc-pVTZ); data dari h2_pyscf.json
dq = json.load(open('h2_pyscf.json')); Rq = np.array(dq['R']); EH = -0.4998098
f, ax = plt.subplots(figsize=(5.6, 3.6)); sp(ax)
for k, t, c in [('uhf', 'UHF', H), ('rhf', 'RHF', B), ('fci', 'CI lengkap', J2)]:
    cq = CubicSpline(Rq, (np.array(dq[k]) - 2 * EH) * EV); rr = np.linspace(0.6, 8, 300); ax.plot(rr, cq(rr), color=c, lw=1.8, label=t)
ax.axvline(2.30, color='#999', lw=0.7, ls='--'); ax.text(2.38, 3.6, 'Coulson–Fischer', fontsize=7.5, color='#666')
ax.axhline(0, color='#999', lw=0.6); ax.set_xlim(0.6, 8); ax.set_ylim(-5.2, 5)
ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('$E - 2E(\\mathrm{H})$ (eV)'); koma(ax); ax.legend(frameon=False, fontsize=8, loc='lower right')
sv(f, 'c_h2_uhf.png')
