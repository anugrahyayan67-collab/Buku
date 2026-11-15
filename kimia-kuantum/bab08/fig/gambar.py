#!/usr/bin/env python3
# Gambar Bab 8 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from math import pi
from scipy.linalg import eigh
from scipy.optimize import minimize
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'mathtext.fontset': 'dejavusans',
                     'text.color': '#0e2748', 'axes.edgecolor': '#0e2748', 'axes.labelcolor': '#0e2748',
                     'xtick.color': '#0e2748', 'ytick.color': '#0e2748'})
TUA, B, MUDA, J1, J2, H = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
KOMA = FuncFormatter(lambda x, p: ('%g' % x).replace('.', ',').replace('-', '−'))
def sv(f, n): f.savefig(n, dpi=220, bbox_inches='tight'); plt.close(f)
def sp(ax):
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
def koma(ax, x=True, y=True):
    if x: ax.xaxis.set_major_formatter(KOMA)
    if y: ax.yaxis.set_major_formatter(KOMA)
def kstr(v, d=2): return (f'%.{d}f' % v).replace('.', ',').replace('-', '−')

# 0. helium: W(zeta) dan muatan efektif
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
ax = axs[0]; sp(ax); z = np.linspace(1.2, 2.2, 300)
ax.plot(z, z * z - 27 / 8 * z, color=B, lw=1.8, label='$W(\\zeta)$')
ax.axhline(-2.86168, color=H, lw=1, ls='--'); ax.text(1.21, -2.857, 'Hartree–Fock', color=H, fontsize=7.5, va='bottom')
ax.axhline(-2.903724, color=J2, lw=1, ls='--'); ax.text(1.21, -2.899, 'eksak', color=J2, fontsize=7.5, va='bottom')
ax.plot([27 / 16], [-(27 / 16) ** 2], 'o', color=TUA, ms=4); ax.annotate('$\\zeta = 27/16$', (27 / 16, -(27 / 16) ** 2), (1.75, -2.70), fontsize=8, arrowprops=dict(arrowstyle='->', color=TUA, lw=.7))
ax.plot([2], [-2.75], 's', color=J1, ms=4); ax.text(2.03, -2.80, 'orde\npertama', fontsize=7.5, color=J2)
ax.set_xlim(1.2, 2.2); ax.set_ylim(-2.95, -2.45); ax.set_xlabel('$\\zeta$'); ax.set_ylabel('$W$ ($E_h$)'); koma(ax)
ax = axs[1]; sp(ax); r = np.linspace(0, 3, 300); zt = 2.0
q = 1 - np.exp(-2 * zt * r) * (1 + 2 * zt * r + 2 * (zt * r) ** 2)
ax.plot(r, 2 - q, color=B, lw=1.8); ax.axhline(27 / 16, color=J2, lw=1, ls='--'); ax.text(2.0, 1.71, '$\\zeta = 1{,}69$', color=J2, fontsize=8)
ax.axhline(2, color='#999', lw=.6, ls=':'); ax.axhline(1, color='#999', lw=.6, ls=':')
ax2 = ax.twinx(); ax2.fill_between(r, 0, 4 * zt ** 3 * r * r * np.exp(-2 * zt * r), color=MUDA, alpha=.4, lw=0); ax2.set_yticks([]); ax2.set_ylim(0, 3.2)
for s in ['top', 'right']: ax2.spines[s].set_visible(False)
ax.text(0.9, 1.25, 'rapat radial\nelektron 1s', fontsize=7.5, color=B)
ax.set_xlim(0, 3); ax.set_ylim(0.9, 2.1); ax.set_xlabel('$r$ ($a_0$)'); ax.set_ylabel('$Z_\\mathrm{ef}(r)$'); koma(ax); ax.set_zorder(ax2.get_zorder() + 1); ax.patch.set_visible(False)
f.subplots_adjust(wspace=0.38); sv(f, 'c_zeta.png')

# 1. MacDonald: akar menyelang
cols = [[1.0132], [1.0132, 4.2555], [1.000015, 4.2555, 10.348], [1.000015, 4.0023, 10.348, 20.315]]
lab = ['$\\{f_1\\}$', '$\\{f_1, f_3\\}$', '$\\{f_1, f_2, f_3\\}$', '$\\{f_1, \\ldots, f_4\\}$']
f, ax = plt.subplots(figsize=(5.0, 3.4)); sp(ax)
for n in range(1, 5): ax.axhline(n * n, color='#999', lw=.7, ls='--'); ax.text(4.55, n * n, f'$E_{n}$', va='center', fontsize=8)
for i, c in enumerate(cols):
    for k, w in enumerate(c):
        ax.plot([i + 0.7, i + 1.3], [w, w], color=[B, H, J2, TUA][k], lw=2.2)
        if i + 1 < len(cols) and k < len(cols[i + 1]): ax.plot([i + 1.3, i + 1.7], [w, cols[i + 1][k]], color='#bbb', lw=.6)
ax.set_xticks(range(1, 5)); ax.set_xticklabels(lab, fontsize=8); ax.set_xlim(0.5, 4.8); ax.set_ylim(0, 22)
ax.set_ylabel('$W/E_1$'); koma(ax, x=False); sv(f, 'c_macdonald.png')

# 2. hidrogen dalam basis Gauss
def HS(al):
    A = al[:, None] + al[None, :]; S = (pi / A) ** 1.5; return 3 * al[:, None] * al[None, :] / A * S - 2 * pi / A, S
def en(l):
    al = np.exp(l); Hm, S = HS(al); return eigh(Hm, S, eigvals_only=True)[0]
hasil = {}
for g in ([0.3], [0.2, 1.3], [0.15, 0.7, 4.0], [0.12, 0.45, 2.0, 13.0], [0.06, 0.2, 0.6, 2, 7, 30]):
    r_ = minimize(en, np.log(g), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 40000, 'maxfev': 40000})
    r_ = minimize(en, r_.x, method='BFGS'); hasil[len(g)] = (np.exp(r_.x), r_.fun)
et = {}
for n in (4, 6, 8, 10, 12):
    def e2(p):
        al = np.exp(p[0]) * np.exp(p[1]) ** np.arange(n); Hm, S = HS(al); return eigh(Hm, S, eigvals_only=True)[0]
    r_ = minimize(e2, np.log([0.05, 3.0]), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-13}); et[n] = r_.fun
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
ax = axs[0]; sp(ax); r = np.linspace(0, 4, 400)
ax.plot(r, np.exp(-r) / np.sqrt(pi), color=TUA, lw=2, label='eksak')
for n, cl in [(1, J2), (2, H), (3, B)]:
    al, _ = hasil[n]; Hm, S = HS(al); w, C = eigh(Hm, S); c = C[:, 0] * np.sign(C[:, 0].sum())
    ax.plot(r, (c[:, None] * np.exp(-np.outer(al, r * r))).sum(0), color=cl, lw=1.2, ls='--' if n == 1 else '-', label=f'{n} Gauss')
ax.legend(frameon=False, fontsize=8); ax.set_xlabel('$r$ ($a_0$)'); ax.set_ylabel('$\\psi(r)$'); ax.set_xlim(0, 4); ax.set_ylim(0, 0.6); koma(ax)
ax = axs[1]; sp(ax)
nn = sorted(hasil); ax.semilogy(nn, [(hasil[n][1] + 0.5) * 1000 for n in nn], 'o-', color=B, lw=1.3, ms=4, label='eksponen bebas')
ne = sorted(et); ax.semilogy(ne, [(et[n] + 0.5) * 1000 for n in ne], 's--', color=J2, lw=1.1, ms=4, label='bertempera rata')
ax.set_xlabel('jumlah fungsi Gauss'); ax.set_ylabel('galat energi (m$E_h$)'); ax.legend(frameon=False, fontsize=8); ax.set_xticks([2, 4, 6, 8, 10, 12]); koma(ax, y=False)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: ('%g' % x).replace('.', ',')))
f.subplots_adjust(wspace=0.4); sv(f, 'c_gauss.png')

# 3. kotak dengan dasar miring, V0 = 5 E1
N = 30; E1 = pi * pi / 2; V0 = 5 * E1; n = np.arange(1, N + 1)
def xmn(m, k): return 0.5 if m == k else (0 if (m + k) % 2 == 0 else -8 * m * k / (pi ** 2 * (m * m - k * k) ** 2))
X = np.array([[xmn(m, k) for k in n] for m in n]); Hm = np.diag((n * pi) ** 2 / 2) + V0 * X
w, C = np.linalg.eigh(Hm); c = C[:, 0] * np.sign(C[0, 0])
x = np.linspace(0, 1, 400); phi = np.sqrt(2) * np.sin(np.outer(n, x) * pi)
psi_ex = c @ phi; psi0 = phi[0]
a = np.array([0] + [V0 * X[m, 0] / (E1 - (m + 1) ** 2 * E1) for m in range(1, N)]); a[0] = 1
psi1 = a @ phi; psi1 /= np.sqrt(np.trapezoid(psi1 ** 2, x))
f, ax = plt.subplots(figsize=(4.8, 3.0)); sp(ax)
ax2 = ax.twinx(); ax2.fill_between(x, 0, x, color=J1, alpha=.18, lw=0); ax2.set_ylim(0, 1.6); ax2.set_yticks([])
for s in ['top', 'right']: ax2.spines[s].set_visible(False)
ax.plot(x, psi0, color='#999', lw=1, label='$\\psi_1^{(0)}$')
ax.plot(x, psi1, color=J2, lw=1.4, ls='--', label='$\\psi_1^{(0)} + \\psi_1^{(1)}$')
ax.plot(x, psi_ex, color=B, lw=2, label='eksak')
ax.text(0.60, 0.12, '$V = V_0x/L$', color=J2, fontsize=8)
ax.legend(frameon=False, fontsize=8, loc='upper right'); ax.set_xlabel('$x/L$'); ax.set_ylabel('$\\psi$'); ax.set_xlim(0, 1); ax.set_ylim(0, 1.75); koma(ax)
ax.set_zorder(ax2.get_zorder() + 1); ax.patch.set_visible(False); sv(f, 'c_miring.png')

# 4. tolakan tingkat dan deret asimtotik kuartik
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9))
ax = axs[0]; sp(ax); d = np.linspace(-4, 4, 600); V = 0.5
ax.plot(d, -d / 2, color='#bbb', lw=.9); ax.plot(d, d / 2, color='#bbb', lw=.9)
ax.plot(d, -np.sqrt(d * d / 4 + V * V), color=B, lw=2); ax.plot(d, np.sqrt(d * d / 4 + V * V), color=B, lw=2)
for sgn in (1, -1):
    dd = d[(sgn * d) > 0.45]
    ax.plot(dd, -dd / 2 - V * V / dd, color=J2, lw=1.1, ls='--'); ax.plot(dd, dd / 2 + V * V / dd, color=J2, lw=1.1, ls='--')
ax.annotate('', xy=(0, V), xytext=(0, -V), arrowprops=dict(arrowstyle='<->', color=H, lw=1)); ax.text(0.12, -0.15, '$2|V|$', color=H, fontsize=8)
ax.set_xlabel('$\\delta$ (satuan $2V$)'); ax.set_ylabel('$E$ (satuan $2V$)'); ax.set_ylim(-2.3, 2.3); koma(ax)
ax = axs[1]; sp(ax); lam = np.linspace(0, 0.3, 200)
Xo = np.zeros((90, 90))
for k in range(89): Xo[k, k + 1] = Xo[k + 1, k] = np.sqrt((k + 1) / 2)
X4 = np.linalg.matrix_power(Xo, 4)[:70, :70]; H0 = np.diag(np.arange(70) + 0.5)
ex = [np.linalg.eigvalsh(H0 + l * X4)[0] for l in lam]
co = [0.5, 0.75, -21 / 8, 333 / 16, -30885 / 128]
ax.plot(lam, ex, color=TUA, lw=2.2, label='eksak')
for k, cl in zip(range(1, 5), [J2, H, B, J1]):
    ax.plot(lam, sum(co[j] * lam ** j for j in range(k + 1)), color=cl, lw=1.1, ls='--', label=f'orde {k}')
ax.set_ylim(0.45, 0.8); ax.set_xlim(0, 0.3); ax.set_xlabel('$\\lambda$'); ax.set_ylabel('$E_0$'); ax.legend(frameon=False, fontsize=7.5, ncol=2, loc='upper left'); koma(ax)
sv(f, 'c_orde2.png')

# 5. galat ion mirip helium
Z = np.arange(1, 7)
ex = np.array([-0.527751, -2.903724, -7.279913, -13.655566, -22.030972, -32.406247])
hf = np.array([-0.487930, -2.861680, -7.236415, -13.611299, -21.986234, -32.361193])
p1 = -Z * Z + 5 * Z / 8; vr = -(Z - 5 / 16) ** 2; p2 = p1 - 0.157666
f, ax = plt.subplots(figsize=(5.0, 3.0)); sp(ax)
ax.plot(Z, p1 - ex, 'o-', color=J2, lw=1.4, ms=4, label='perturbasi orde pertama')
ax.plot(Z, vr - ex, 's-', color=B, lw=1.4, ms=4, label='variasi, muatan efektif')
ax.plot(Z, p2 - ex, '^-', color=H, lw=1.4, ms=4, label='perturbasi orde kedua')
ax.plot(Z, hf - ex, ':', color=TUA, lw=1.2, label='Hartree–Fock (energi korelasi)')
ax.axhline(0, color='#999', lw=.6)
ax.set_xticks(Z); ax.set_xticklabels(['H$^-$', 'He', 'Li$^+$', 'Be$^{2+}$', 'B$^{3+}$', 'C$^{4+}$']); ax.set_ylabel('$E - E_\\mathrm{eksak}$ ($E_h$)')
ax.legend(frameon=False, fontsize=7.5, loc='upper center', ncol=2); koma(ax, x=False); ax.set_ylim(-0.02, 0.24); sv(f, 'c_isoelektron.png')

# 6. keadaan tereksitasi helium
Js, Ks, Jp, Kp = 17 * 2 / 81, 16 * 2 / 729, 59 * 2 / 243, 112 * 2 / 6561
f, ax = plt.subplots(figsize=(5.6, 4.0)); sp(ax); ax.spines['bottom'].set_visible(False); ax.set_xticks([])
def lv(x, y, cl, t=None, lw=2):
    ax.plot([x - .32, x + .32], [y, y], color=cl, lw=lw)
    if t: ax.text(x + .36, y, t, fontsize=7.5, va='center')
lv(0, -2.5, TUA, '1s2s, 1s2p\n(8 keadaan)')
lv(1.3, -2.5 + Js, B, '1s2s'); lv(1.3, -2.5 + Jp, H, '1s2p')
for y_, cl, t_, dy in [(-2.5 + Js - Ks, B, '$2^3$S', 0), (-2.5 + Js + Ks, B, '$2^1$S', 0.007), (-2.5 + Jp - Kp, H, '$2^3$P', -0.007), (-2.5 + Jp + Kp, H, '$2^1$P', 0)]:
    lv(2.6, y_, cl); ax.text(2.6 + .36, y_ + dy, t_, fontsize=7.5, va='center')
exs = {'$2^3$S': -2.175229, '$2^1$S': -2.145974, '$2^3$P': -2.133164, '$2^1$P': -2.123843}
for (k, v), cl, dy in zip(exs.items(), [B, B, H, H], [0, -0.008, 0.0, 0.009]):
    lv(3.9, v, cl); ax.text(3.9 + .36, v + dy, k, fontsize=7.5, va='center')
for y0, y1, x0 in [(-2.5, -2.5 + Js, 0), (-2.5, -2.5 + Jp, 0)]: ax.plot([x0 + .32, 1.3 - .32], [y0, y1], color='#bbb', lw=.6)
for y0, d_, cl in [(-2.5 + Js, Ks, B), (-2.5 + Jp, Kp, H)]:
    for s in (-1, 1): ax.plot([1.3 + .32, 2.6 - .32], [y0, y0 + s * d_], color='#bbb', lw=.6)
for x_, t in [(0, 'orde nol'), (1.3, '$+J$'), (2.6, '$\\pm K$'), (3.9, 'eksak')]: ax.text(x_, -1.93, t, ha='center', fontsize=8.5)
ax.set_xlim(-0.5, 4.7); ax.set_ylim(-2.55, -1.9); ax.set_ylabel('$E$ ($E_h$)'); koma(ax, x=False); sv(f, 'c_hetereksitasi.png')

# 7. Stark dan dispersi
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9))
ax = axs[0]; sp(ax); F = np.linspace(0, 1, 50)
ax.plot(F, 3 * F, color=J2, lw=1.8); ax.plot(F, -3 * F, color=B, lw=1.8); ax.plot(F, 0 * F, color=TUA, lw=1.8)
ax.text(0.12, 1.5, '$(2s - 2p_0)/\\sqrt{2}$', fontsize=7.5, ha='left', color=J2); ax.text(0.5, -1.15, '$(2s + 2p_0)/\\sqrt{2}$', fontsize=7.5, ha='left', color=B)
ax.text(0.75, 0.2, '$2p_{\\pm1}$', fontsize=7.5)
ax.set_xlabel('$F$ (satuan sembarang)'); ax.set_ylabel('$E^{(1)}$ (satuan $F$)'); ax.set_xlim(0, 1); koma(ax)
ia = ax.inset_axes([0.04, 0.05, 0.3, 0.28]); zz = np.linspace(-14, 14, 400)
s2 = (2 - np.abs(zz)) * np.exp(-np.abs(zz) / 2) / np.sqrt(32 * pi); p0 = zz * np.exp(-np.abs(zz) / 2) / np.sqrt(32 * pi)
ia.plot(zz, ((s2 + p0) / np.sqrt(2)) ** 2, color=B, lw=1); ia.plot(zz, ((s2 - p0) / np.sqrt(2)) ** 2, color=J2, lw=1)
ia.set_xticks([]); ia.set_yticks([]); ia.set_title('rapat sepanjang $z$', fontsize=6.5)
ax = axs[1]; sp(ax)
dat = [('He', 1.461, 4.22), ('Ne', 6.38, 27.07), ('Ar', 64.3, 87.30), ('Kr', 129.6, 119.93), ('Xe', 285.9, 165.05)]
c6 = [d_[1] for d_ in dat]; tb = [d_[2] for d_ in dat]
ax.loglog(c6, tb, 'o-', color=B, lw=1.2, ms=5)
for nm, a_, t_ in dat: ax.text(a_ * 1.15, t_ * 0.86, nm, fontsize=8)
ax.set_xlabel('$C_6$ (satuan atom)'); ax.set_ylabel('titik didih (K)')
for axis in (ax.xaxis, ax.yaxis): axis.set_major_formatter(FuncFormatter(lambda x, p: ('%g' % x).replace('.', ',')))
f.subplots_adjust(wspace=0.38); sv(f, 'c_stark.png')

# 8. Rabi
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
ax = axs[0]; sp(ax); t = np.linspace(0, 4 * pi, 500)
for dl, lw_, cl in [(0, 2, B), (1, 1.3, H), (2, 0.9, J2)]:
    Om = np.sqrt(1 + dl * dl); ax.plot(t, np.sin(Om * t / 2) ** 2 / Om ** 2, color=cl, lw=lw_, label=f'$\\delta = {dl}\\Omega$'.replace('= 0\\Omega', '= 0').replace('= 1\\Omega', '= \\Omega'))
tt = t[t < 2.4]; ax.plot(tt, tt * tt / 4, color=TUA, lw=1, ls='--', label='orde pertama')
ax.set_xlim(0, 4 * pi); ax.set_xticks([0, pi, 2 * pi, 3 * pi, 4 * pi]); ax.set_xticklabels(['0', '$\\pi$', '$2\\pi$', '$3\\pi$', '$4\\pi$'])
ax.set_ylim(0, 1.42); ax.set_xlabel('$\\Omega t$'); ax.set_ylabel('$P_{i\\to f}$'); ax.legend(frameon=False, fontsize=7.5, loc='upper center', ncol=2); koma(ax, x=False)
ax = axs[1]; sp(ax); dw = np.linspace(-12, 12, 800)
for T_, cl, lw_ in [(1, J2, 1.2), (2, B, 1.8)]:
    y = np.where(np.abs(dw) < 1e-9, T_ * T_ / 4, np.sin(dw * T_ / 2) ** 2 / np.where(np.abs(dw) < 1e-9, 1, dw * dw))
    ax.plot(dw, y, color=cl, lw=lw_, label=['$t$', '$2t$'][T_ - 1])
ax.set_xlabel('$\\omega - \\omega_{fi}$ (satuan $1/t$)'); ax.set_yticks([]); ax.legend(frameon=False, fontsize=8); ax.set_ylabel('$P_{i\\to f}$ (relatif)'); koma(ax, y=False)
sv(f, 'c_rabi.png')

# 9. fungsi delta dan diagram Grotrian
f, axs = plt.subplots(1, 2, figsize=(6.8, 3.0), gridspec_kw={'width_ratios': [1.15, 1]})
ax = axs[0]; sp(ax); xx = np.linspace(-6, 6, 1200)
for T_, cl, lw_ in [(2, J2, 1), (4, H, 1.3), (8, B, 1.8)]:
    y = np.sin(xx * T_ / 2) ** 2 / (xx / 2) ** 2 / (2 * pi * T_); ax.plot(xx, y, color=cl, lw=lw_, label=f'$t = {T_}$')
ax.set_xlabel('$\\omega_{fi}$'); ax.set_ylabel('$\\sin^2(\\omega_{fi}t/2)\\,/\\,[2\\pi t(\\omega_{fi}/2)^2]$', fontsize=8); ax.legend(frameon=False, fontsize=8); koma(ax)
ax = axs[1]; ax.axis('off')
E = {n: -1 / (2 * n * n) for n in (1, 2, 3)}; xs = {'s': 0, 'p': 1, 'd': 2}
for l, x0 in xs.items():
    for n in (1, 2, 3):
        if 'spd'.index(l) < n:
            ax.plot([x0 - .3, x0 + .3], [E[n], E[n]], color=TUA, lw=2); ax.text(x0 + .32, E[n], f'{n}{l}', fontsize=7.5, va='center')
    ax.text(x0, -0.02, l, ha='center', fontsize=9, color=B)
pairs = [((1, 's'), (2, 'p')), ((1, 's'), (3, 'p')), ((2, 's'), (2, 'p')), ((2, 's'), (3, 'p')), ((3, 's'), (2, 'p')), ((3, 's'), (3, 'p')), ((2, 'p'), (3, 'd')), ((3, 'p'), (3, 'd'))]
for (n1, l1), (n2, l2) in pairs:
    if (n1, l1) == (2, 's') and (n2, l2) == (2, 'p'): continue
    if (n1, l1) == (3, 's') and (n2, l2) == (3, 'p'): continue
    if (n1, l1) == (3, 'p') and (n2, l2) == (3, 'd'): continue
    ax.plot([xs[l1] + .3 * (1 if xs[l2] > xs[l1] else -1), xs[l2] - .3 * (1 if xs[l2] > xs[l1] else -1)], [E[n1], E[n2]], color=J2, lw=.9)
ax.set_xlim(-0.5, 2.6); ax.set_ylim(-0.58, 0.0); ax.text(1, -0.57, 'hidrogen, $n \\leq 3$', ha='center', fontsize=8)
sv(f, 'c_emas.png')
print('selesai')
