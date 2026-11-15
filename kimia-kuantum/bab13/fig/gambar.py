#!/usr/bin/env python3
# Gambar Bab 13 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Ellipse, Polygon, Circle, FancyArrowPatch
from math import pi, sqrt, factorial
from eht import eht, ppp
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'mathtext.fontset': 'dejavusans',
                     'text.color': '#0e2748', 'axes.edgecolor': '#0e2748', 'axes.labelcolor': '#0e2748',
                     'xtick.color': '#0e2748', 'ytick.color': '#0e2748'})
TUA, B, MUDA, J1, J2, H = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
KOMA = FuncFormatter(lambda x, p: ('%g' % x).replace('.', ',').replace('-', '−'))
CM = LinearSegmentedColormap.from_list('bj', [J2, J1, '#ffffff', MUDA, B])
def sv(f, n): f.savefig(n, dpi=220, bbox_inches='tight'); plt.close(f)
def sp_(ax):
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
def koma(ax, x=True, y=True):
    if x: ax.xaxis.set_major_formatter(KOMA)
    if y: ax.yaxis.set_major_formatter(KOMA)
def kk(v, d=2):
    t = ('%.' + str(d) + 'f') % v
    if float(t) == 0: t = t.replace('-', '')
    return t.replace('.', ',').replace('-', '−')
A0 = 0.529177

def h2o(th, R=0.958):
    t = np.radians(th / 2)
    return [('O', (0, 0, 0)), ('H', (0, R * np.sin(t), R * np.cos(t))), ('H', (0, -R * np.sin(t), R * np.cos(t)))]

# 1. orbital molekul air (EHT): evaluasi orbital Slater pada bidang
e, C, S, bf = eht(h2o(104.5))
ZET = {'O': 2.275, 'H': 1.3}
def sto(b, X, Y, Z):
    el = b[8].split()[0]; z = ZET[el]; cen = b[5] * A0
    dx, dy, dz = X - cen[0], Y - cen[1], Z - cen[2]; r = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2) / A0 + 1e-12
    if b[8].endswith('1s'): return 2 * z ** 1.5 * np.exp(-z * r) / sqrt(4 * pi)
    N = (2 * z) ** 2.5 / sqrt(24)
    if b[8].endswith('2s'): return N * r * np.exp(-z * r) / sqrt(4 * pi)
    comp = [dx, dy, dz][b[7]] / A0
    return N * comp * np.exp(-z * r) * sqrt(3 / (4 * pi))
g = np.linspace(-2.0, 2.0, 400); U, V = np.meshgrid(g, g)
f, axs = plt.subplots(1, 4, figsize=(7.0, 2.1))
for ax, (k, nm, bidang) in zip(axs, [(0, '2a$_1$', 'yz'), (1, '1b$_2$', 'yz'), (2, '3a$_1$', 'yz'), (3, '1b$_1$', 'xz')]):
    if bidang == 'yz': X, Y, Z = 0 * U, U, -V + 0.3
    else: X, Y, Z = U, 0 * U, -V + 0.3
    psi = sum(C[i, k] * sto(bf[i], X, Y, Z) for i in range(len(bf)))
    if psi[200, 200] < 0 and k != 1: psi = -psi
    vm = np.abs(psi).max() * 0.6
    ax.contourf(U, V, psi, levels=np.linspace(-vm, vm, 21), cmap=CM, extend='both')
    ax.contour(U, V, psi, levels=[0], colors=TUA, linewidths=.5, linestyles='--')
    for el, p in h2o(104.5):
        pu, pv = (p[1], -(p[2] - 0.3)) if bidang == 'yz' else (p[0], -(p[2] - 0.3))
        if bidang == 'xz' and el == 'H': continue
        ax.plot(pu, pv, 'o', color=TUA, ms=3 if el == 'H' else 4)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f'{nm} ({kk(e[k], 1)} eV)', fontsize=8.5)
    for s in ax.spines.values(): s.set_color('#ccc')
f.tight_layout(); sv(f, 'c_air.png')

# 2. diagram Walsh H2O (EHT), sumbu terpatah
ths = np.arange(80, 181, 2.0)
E = np.array([eht(h2o(t))[0][:6] for t in ths])
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(5.4, 3.9), sharex=True, gridspec_kw={'height_ratios': [1, 2.2], 'hspace': 0.08})
lab = [('2a$_1$', '2σ$_g$'), ('1b$_2$', '1σ$_u$'), ('3a$_1$', '1π$_u$'), ('1b$_1$', '1π$_u$'), ('4a$_1$', '3σ$_g$'), ('2b$_2$', '2σ$_u$')]
cols = [TUA, B, J2, H, '#777', '#777']
for ax in (ax1, ax2):
    for k in range(1, 5):
        ax.plot(ths, E[:, k], color=cols[k], lw=1.8)
    ax.axvline(104.5, color='#999', lw=.7, ls=':')
for k in (1, 2, 3):
    ax2.text(78, E[0, k] + {1: 0, 2: -0.12, 3: 0.12}[k], lab[k][0], ha='right', va='center', fontsize=8.5, color=cols[k])
ax2.text(182, E[-1, 1], lab[1][1], ha='left', va='center', fontsize=8.5, color=cols[1])
ax2.text(182, E[-1, 2], '1π$_u$', ha='left', va='center', fontsize=8.5, color=TUA)
ax1.text(78, E[0, 4], lab[4][0], ha='right', va='center', fontsize=8.5, color=cols[4]); ax1.text(182, E[-1, 4], lab[4][1], ha='left', va='center', fontsize=8.5, color=cols[4])
ax1.set_ylim(-1.2, 3.6); ax2.set_ylim(-18.2, -14.4)
ax1.spines['bottom'].set_visible(False); ax2.spines['top'].set_visible(False); ax1.tick_params(bottom=False)
for s_ in ['top', 'right']: ax1.spines[s_].set_visible(False)
ax2.spines['right'].set_visible(False)
d = .012; kw = dict(transform=ax1.transAxes, color=TUA, clip_on=False, lw=.8)
ax1.plot((-d, +d), (-d * 2.2, +d * 2.2), **kw); kw.update(transform=ax2.transAxes); ax2.plot((-d, +d), (1 - d, 1 + d), **kw)
ax1.text(105.5, 2.6, 'H$_2$O 104,5°', fontsize=7.5, color='#666'); ax1.text(170, 0.2, 'linear', fontsize=7.5, color='#666'); ax1.text(82, 2.6, 'bengkok', fontsize=7.5, color='#666')
ax2.set_xlim(70, 192); ax2.set_xlabel('sudut H–O–H (°)'); f.text(0.0, 0.5, 'energi orbital (eV)', rotation=90, va='center')
koma(ax1); koma(ax2); sv(f, 'c_walsh.png')

# 3. tingkat Hückel dan koefisien: etilena, alil, butadiena
def huck(n, bonds):
    A = np.zeros((n, n))
    for i, j in bonds: A[i, j] = A[j, i] = 1
    x, Cm = np.linalg.eigh(A); return x[::-1], Cm[:, ::-1]
f, axs = plt.subplots(1, 3, figsize=(7.0, 3.3), sharey=True)
for ax, (nm, n, ne) in zip(axs, [('etilena', 2, 2), ('alil (radikal)', 3, 3), ('butadiena', 4, 4)]):
    x, Cm = huck(n, [(i, i + 1) for i in range(n - 1)])
    ax.axis('off'); ax.set_xlim(-0.6, 3.4); ax.set_ylim(-2.25, 2.4); ax.set_title(nm, fontsize=9)
    sisa = ne
    for k in range(n):
        y = x[k]
        ax.plot([-0.4, 0.4], [y, y], color=TUA, lw=1.6)
        ax.text(-0.5, y, kk(x[k], 3) if abs(x[k]) > 1e-9 else '0', ha='right', va='center', fontsize=7.5)
        nel = min(2, sisa); sisa -= nel
        for q in range(nel):
            xx = -0.12 + 0.24 * q; d = 0.16 if q == 0 else -0.16
            ax.annotate('', xy=(xx, y + d), xytext=(xx, y - d), arrowprops=dict(arrowstyle='-|>', color=J2, lw=1, mutation_scale=6))
        for i in range(n):
            c = Cm[i, k]; xc = 0.9 + 0.65 * i
            ax.plot([xc - 0.3, xc + 0.3] if i < n - 1 else [xc, xc], [y, y], color='#ddd', lw=.6)
            if abs(c) > 1e-6: ax.add_patch(Circle((xc, y), 0.42 * abs(c), color=B if c > 0 else J2))
            else: ax.plot(xc, y, 'x', color='#999', ms=3.5)
    axs[0].text(-0.55, -2.2, '$x$ dalam $E = \\alpha + x\\beta$', fontsize=7.5, color='#666')
sv(f, 'c_huckel.png')

# 4. lingkaran Frost
f, axs = plt.subplots(1, 6, figsize=(7.4, 2.2))
for ax, (n, ne, nm) in zip(axs, [(3, 2, 'C$_3$H$_3^+$'), (4, 4, 'C$_4$H$_4$'), (5, 6, 'C$_5$H$_5^-$'), (6, 6, 'C$_6$H$_6$'), (7, 6, 'C$_7$H$_7^+$'), (8, 8, 'C$_8$H$_8$')]):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.5, 2.6)
    ax.add_patch(Circle((0, 0), 2, fill=False, color='#bbb', lw=.8)); ax.axhline(0, color='#ddd', lw=.6)
    ang = -pi / 2 + 2 * pi * np.arange(n) / n
    lv = sorted(set(np.round(2 * np.sin(-ang) * -1, 6)))
    pts = [(2 * np.cos(a), 2 * np.sin(a)) for a in ang]
    ax.add_patch(Polygon(pts, closed=True, fill=False, color=B, lw=1.1))
    # isi elektron dari bawah, dengan aturan Hund pada tingkat berdegenerasi
    levels = {}
    for (px, py) in pts: levels.setdefault(round(py, 5), []).append(px)
    sisa = ne
    for py in sorted(levels):
        xs_ = sorted(levels[py]); m = len(xs_); nel_lv = min(2 * m, sisa); sisa -= nel_lv
        isi = [0] * m
        for q in range(nel_lv): isi[q % m] += 1
        for px, nq in zip(xs_, isi):
            ax.plot([px - 0.5, px + 0.5], [py, py], color=TUA, lw=1.5)
            for q in range(nq):
                xx = px - 0.14 + 0.28 * q if nq == 2 else px; dd = 0.36 if q == 0 else -0.36
                ax.annotate('', xy=(xx, py + dd), xytext=(xx, py - dd), arrowprops=dict(arrowstyle='-|>', color=J2, lw=1.1, mutation_scale=7))
    ax.set_title(nm, fontsize=8.5)
sv(f, 'c_frost.png')

# 5. poliena: tingkat menuju pita, dan energi serapan
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9))
ax = axs[0]; sp_(ax)
for N in range(2, 21, 2):
    x = 2 * np.cos(np.pi * np.arange(1, N + 1) / (N + 1))
    for xi in x: ax.plot([N - 0.6, N + 0.6], [xi, xi], color=B if xi > 0 else J2, lw=.9)
ax.axhline(2, color='#999', lw=.6, ls='--'); ax.axhline(-2, color='#999', lw=.6, ls='--')
ax.set_xlabel('banyaknya atom karbon $N$'); ax.set_ylabel('$x$ dalam $E = \\alpha + x\\beta$'); ax.set_xticks(range(2, 21, 4)); koma(ax)
ax.set_title('(a) tingkat π poliena linear', fontsize=9, loc='left')
ax = axs[1]; sp_(ax)
gap = np.array([4 * np.sin(np.pi / (2 * (N + 1))) for N in (2, 4, 6, 8, 10)])
lam = np.array([162, 217, 258, 290, 334]); Eex = 1239.84 / lam
cc = np.polyfit(gap, Eex, 1); xx = np.linspace(0.4, 2.1, 10)
ax.plot(gap, Eex, 'o', color=J2, ms=5); ax.plot(xx, np.polyval(cc, xx), color='#999', lw=.9, ls='--')
for g_, e_, t in zip(gap, Eex, ['C$_2$', 'C$_4$', 'C$_6$', 'C$_8$', 'C$_{10}$']): ax.text(g_ + 0.04, e_ - 0.35, t, fontsize=7.5)
ax.set_xlabel('celah HOMO–LUMO Hückel ($|\\beta|$)'); ax.set_ylabel('energi serapan (eV)'); koma(ax)
ax.set_title('(b) serapan UV poliena', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_poliena.png')

# 6. muatan π: piridina, pirola, azulena
def huckq(n, bonds, h=None, k=None, nel=None, n0=None):
    A = np.zeros((n, n))
    for idx, (i, j) in enumerate(bonds): A[i, j] = A[j, i] = 1 if k is None else k[idx]
    if h:
        for i, v in h.items(): A[i, i] = v
    x, Cm = np.linalg.eigh(A); x = x[::-1]; Cm = Cm[:, ::-1]; nel = n if nel is None else nel
    occ = np.array([min(2, max(0, nel - 2 * i)) for i in range(n)])
    P = (Cm * occ) @ Cm.T; n0 = np.ones(n) if n0 is None else np.array(n0)
    return n0 - np.diag(P)
def poly(n, rot=0):
    R = 1 / (2 * np.sin(pi / n)); return np.array([(R * np.cos(rot + 2 * pi * k / n), R * np.sin(rot + 2 * pi * k / n)) for k in range(n)])
f, axs = plt.subplots(1, 3, figsize=(7.0, 2.6))
ring6 = [(i, (i + 1) % 6) for i in range(6)]; ring5 = [(i, (i + 1) % 5) for i in range(5)]
q = huckq(6, ring6, h={0: 0.5}); P6 = poly(6, pi / 2)
q5 = huckq(5, ring5, h={0: 1.5}, k=[0.8 if 0 in b else 1 for b in ring5], nel=6, n0=[2, 1, 1, 1, 1]); P5 = poly(5, pi / 2)
for ax, P_, qq, lab0, nm in [(axs[0], P6, q, 'N', 'piridina'), (axs[1], P5, q5, 'N–H', 'pirola')]:
    ax.add_patch(Polygon(P_, closed=True, fill=False, color=B, lw=1.4)); ax.set_aspect('equal'); ax.axis('off')
    for i, (px, py) in enumerate(P_):
        ax.text(px * 1.42, py * 1.42, kk(qq[i], 2), ha='center', va='center', fontsize=7.5, color=J2 if qq[i] > 0 else B)
    ax.text(P_[0][0], P_[0][1] * 0.62, lab0, ha='center', va='center', fontsize=8.5)
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.5, 1.6); ax.set_title(nm, fontsize=9)
ax = axs[2]; ax.set_aspect('equal'); ax.axis('off')
# azulena: tujuh-cincin 0..6, lima-cincin 6,7,8,9,0 ; sisi bersama 0–6 vertikal di x=0
R7 = 1 / (2 * np.sin(pi / 7)); a7 = R7 * np.cos(pi / 7); R5 = 1 / (2 * np.sin(pi / 5)); a5 = R5 * np.cos(pi / 5)
c7 = np.array([-a7, 0]); c5 = np.array([a5, 0])
p0 = np.array([0, -0.5]); p6 = np.array([0, 0.5])
def keliling(c, start, n, arah):
    v = start - c; ang0 = np.arctan2(v[1], v[0]); Rr = np.linalg.norm(v)
    return [c + Rr * np.array([np.cos(ang0 + arah * 2 * pi * k / n), np.sin(ang0 + arah * 2 * pi * k / n)]) for k in range(n)]
H7 = keliling(c7, p0, 7, -1)   # 0,1,...,6 searah jarum jam di kiri
H5 = keliling(c5, p6, 5, -1)   # 6,7,8,9,0
XY = np.array(H7 + [H5[1], H5[2], H5[3]])
azb = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 0), (6, 7), (7, 8), (8, 9), (9, 0)]
qa = huckq(10, azb)
for i, j in azb: ax.plot(*zip(XY[i], XY[j]), color=B, lw=1.4)
cen = XY.mean(0)
for i, (px, py) in enumerate(XY):
    d = np.array([px, py]) - (c7 if i <= 6 else c5)
    if i in (0, 6): d = np.array([0, py])
    d = d / np.linalg.norm(d); ax.text(px + 0.45 * d[0], py + 0.45 * d[1], kk(qa[i], 2), ha='center', va='center', fontsize=7, color=J2 if qa[i] > 0 else B)
ax.set_xlim(-2.6, 2.0); ax.set_ylim(-1.8, 1.8); ax.set_title('azulena', fontsize=9)
sv(f, 'c_muatan.png')

# 7. asena: energi ionisasi dan pita p
xs = np.array([1.0, 0.618, 0.4142, 0.295, 0.2197]); ip = np.array([9.24, 8.14, 7.44, 6.97, 6.63]); pb = 1239.84 / np.array([203, 286, 375, 471, 580])
nm = ['benzena', 'naftalena', 'antrasena', 'tetrasena', 'pentasena']
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
ax = axs[0]; sp_(ax); c1 = np.polyfit(xs, ip, 1); xx = np.linspace(0.15, 1.05, 10)
ax.plot(xs, ip, 'o', color=B, ms=5); ax.plot(xx, np.polyval(c1, xx), color='#999', lw=.9, ls='--')
for a, b_, t in zip(xs, ip, nm): ax.text(a + 0.02, b_ - 0.25, t, fontsize=7)
ax.set_xlabel('$x_\\mathrm{HOMO}$ Hückel'); ax.set_ylabel('energi ionisasi (eV)'); koma(ax); ax.set_title('(a)', fontsize=9, loc='left')
ax = axs[1]; sp_(ax); c2 = np.polyfit(2 * xs, pb, 1); xx = np.linspace(0.3, 2.1, 10)
ax.plot(2 * xs, pb, 's', color=J2, ms=5); ax.plot(xx, np.polyval(c2, xx), color='#999', lw=.9, ls='--')
for a, b_, t in zip(2 * xs, pb, nm): ax.text(a + 0.04, b_ - 0.3, t, fontsize=7)
ax.set_xlabel('celah HOMO–LUMO ($|\\beta|$)'); ax.set_ylabel('energi pita $p$ (eV)'); koma(ax); ax.set_title('(b)', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_asena.png')

# 8. reaksi elektrosiklik: lobus ujung HOMO butadiena
f, axs = plt.subplots(1, 2, figsize=(6.6, 2.6))
def porb(ax, x0, tanda, miring=0):
    for s, dy in [(1, 0.42), (-1, -0.42)]:
        col = B if s * tanda > 0 else J2
        ax.add_patch(Ellipse((x0 + np.sin(np.radians(miring)) * dy, dy * np.cos(np.radians(miring))), 0.32, 0.8, angle=-miring, color=col, alpha=.9))
for ax, (judul, t1, t4, rot) in zip(axs, [('(a) termal: HOMO ψ$_2$, konrotasi', 1, -1, 'kon'), ('(b) fotokimia: HOMO ψ$_3$, disrotasi', 1, 1, 'dis')]):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-2.2, 2.2); ax.set_ylim(-1.5, 1.6); ax.set_title(judul, fontsize=8.5)
    ax.plot([-1.3, -0.45, 0.45, 1.3], [0, -0.55, -0.55, 0], color='#999', lw=1.2)
    for xx in [-0.45, 0.45]: ax.plot(xx, -0.55, 'o', color='#999', ms=4)
    porb(ax, -1.3, t1); porb(ax, 1.3, t4)
    ax.text(-1.3, -1.35, 'C1', ha='center', fontsize=8); ax.text(1.3, -1.35, 'C4', ha='center', fontsize=8)
    for x0, arah in [(-1.3, 1), (1.3, 1 if rot == 'kon' else -1)]:
        a_, b_ = (x0 - 0.42, x0 + 0.42) if arah > 0 else (x0 + 0.42, x0 - 0.42)
        ax.add_patch(FancyArrowPatch((a_, 0.95), (b_, 0.95), connectionstyle='arc3,rad=%g' % (-0.6 * arah), arrowstyle='-|>', mutation_scale=9, color=TUA, lw=1.1))
    ax.text(0, -1.0, 'searah (konrotasi)' if rot == 'kon' else 'berlawanan (disrotasi)', ha='center', fontsize=7.5, color=TUA)
    ax.text(0, 0.35, 'lobus sefase\nharus bertemu', ha='center', fontsize=7, color='#666')
sv(f, 'c_elektrosiklik.png')

# 9. keadaan tereksitasi benzena: Hückel, PPP-CIS, percobaan
Rb = 1.397
xyz = [(Rb * np.cos(np.radians(60 * k)), Rb * np.sin(np.radians(60 * k)), 0) for k in range(6)]
_, _, _, s1, s3, fo = ppp(xyz, [(k, (k + 1) % 6) for k in range(6)])
f, ax = plt.subplots(figsize=(5.6, 2.9)); ax.axis('off'); ax.set_xlim(0, 10.4); ax.set_ylim(4.2, 7.55)
for x0, t in [(0.3, 'Hückel'), (3.6, 'PPP-CIS'), (7.4, 'percobaan')]: ax.text(x0 + 1.1, 7.4, t, ha='center', fontsize=8.5)
ax.plot([0.3, 2.5], [4.78, 4.78], color=B, lw=2.2); ax.text(1.4, 4.95, '$2|\\beta|$ = 4,78', ha='center', fontsize=7.5); ax.text(1.4, 4.5, '(4 keadaan)', ha='center', fontsize=7.5)
for E_, t in [(s1[0], '$^1B_{2u}$'), (s1[1], '$^1B_{1u}$'), (s1[2], '$^1E_{1u}$')]:
    ax.plot([3.6, 5.8], [E_, E_], color=B, lw=1.8); ax.text(5.95, E_, t + '  ' + kk(E_, 2), va='center', fontsize=7.5)
for E_ in [4.90, 6.20, 6.94]:
    ax.plot([7.9, 9.6], [E_, E_], color=J2, lw=1.8); ax.text(9.7, E_, kk(E_, 2), va='center', fontsize=7.5)
ax.text(0.1, 4.25, 'energi eksitasi singlet (eV)', fontsize=7.5, color='#666')
sv(f, 'c_ppp.png')

# 10. pita energi rantai Hückel
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9))
ax = axs[0]; sp_(ax); k = np.linspace(-pi, pi, 400)
ax.plot(k / pi, 2 * np.cos(k), color=B, lw=1.6, label='rantai seragam')
b1, b2 = 1.15, 0.85; Ek = np.abs(b1 + b2 * np.exp(1j * 2 * k / 2 * 1))
ka = np.linspace(-pi / 2, pi / 2, 300); Ealt = np.abs(b1 + b2 * np.exp(2j * ka))
ax.plot(ka / pi, Ealt, color=J2, lw=1.6, label='berselang-seling'); ax.plot(ka / pi, -Ealt, color=J2, lw=1.6)
ax.axhline(0, color='#999', lw=.6, ls=':'); ax.set_xlabel('$ka/\\pi$'); ax.set_ylabel('$x$ dalam $E = \\alpha + x\\beta$')
ax.annotate('', xy=(0.5, 0.32), xytext=(0.5, -0.32), arrowprops=dict(arrowstyle='<|-|>', color=TUA, lw=.9, mutation_scale=6)); ax.text(0.53, 0.0, 'celah', fontsize=7.5, va='center')
ax.legend(frameon=False, fontsize=7.5, loc='lower center'); koma(ax); ax.set_title('(a) hubungan dispersi', fontsize=9, loc='left')
ax = axs[1]; sp_(ax)
E_ = np.linspace(-1.999, 1.999, 600); dos = 1 / (pi * np.sqrt(4 - E_ ** 2))
ax.plot(dos, E_, color=B, lw=1.5); ax.fill_betweenx(E_, 0, dos, where=E_ > 0, color=MUDA, alpha=.5)
ax.axhline(0, color=J2, lw=.9, ls='--'); ax.text(0.55, 0.12, 'tingkat Fermi', fontsize=7.2, color=J2)
ax.set_xlim(0, 1.0); ax.set_xlabel('rapat keadaan (per atom per $|\\beta|$)'); ax.set_ylabel('$x$'); koma(ax); ax.set_title('(b) rapat keadaan', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_pita.png')

# 11. grafena: struktur pita dan rapat keadaan
a1 = np.array([1.5, sqrt(3) / 2]); a2 = np.array([1.5, -sqrt(3) / 2])   # dalam satuan a_cc
def Eg(kx, ky): return np.abs(1 + np.exp(1j * (kx * a1[0] + ky * a1[1])) + np.exp(1j * (kx * a2[0] + ky * a2[1])))
G = np.array([0, 0]); K = np.array([2 * pi / 3, 2 * pi / (3 * sqrt(3))]); M = np.array([2 * pi / 3, 0])
path = [G, K, M, G]; seg = []; s = [0]
for P1, P2 in zip(path[:-1], path[1:]):
    t = np.linspace(0, 1, 200); pts = P1 + np.outer(t, P2 - P1); seg.append(pts); s.append(s[-1] + np.linalg.norm(P2 - P1))
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9), gridspec_kw={'width_ratios': [1.6, 1]})
ax = axs[0]; sp_(ax)
for i, pts in enumerate(seg):
    ss = np.linspace(s[i], s[i + 1], len(pts)); e_ = Eg(pts[:, 0], pts[:, 1])
    ax.plot(ss, e_, color=B, lw=1.5); ax.plot(ss, -e_, color=J2, lw=1.5)
for xv in s: ax.axvline(xv, color='#ccc', lw=.6)
ax.set_xticks(s); ax.set_xticklabels(['Γ', 'K', 'M', 'Γ']); ax.axhline(0, color='#999', lw=.6, ls=':')
ax.set_ylabel('$(E - \\alpha)/|\\beta|$'); koma(ax, x=False); ax.set_title('(a) pita π grafena', fontsize=9, loc='left')
ax = axs[1]; sp_(ax)
n = 900; kx = np.linspace(-pi, pi, n); ky = np.linspace(-pi, pi, n); KX, KY = np.meshgrid(kx, ky)
ee = Eg(KX, KY).ravel(); hist, ed = np.histogram(np.concatenate([ee, -ee]), bins=160, density=True)
ax.plot(hist, 0.5 * (ed[1:] + ed[:-1]), color=B, lw=1.2); ax.axhline(0, color=J2, lw=.9, ls='--')
ax.set_xlabel('rapat keadaan'); ax.set_xticks([]); ax.set_ylabel('$(E - \\alpha)/|\\beta|$'); koma(ax, x=False); ax.set_title('(b)', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_grafena.png')
print('selesai')
