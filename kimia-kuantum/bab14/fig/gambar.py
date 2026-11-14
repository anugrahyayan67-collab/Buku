#!/usr/bin/env python3
# Gambar Bab 14 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import numpy as np, itertools, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from math import pi
from sympy.physics.wigner import wigner_3j
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'mathtext.fontset': 'dejavusans',
                     'text.color': '#0e2748', 'axes.edgecolor': '#0e2748', 'axes.labelcolor': '#0e2748',
                     'xtick.color': '#0e2748', 'ytick.color': '#0e2748'})
TUA, B_, MUDA, J1, J2, H = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
def fmt(x, p=None):
    s = ('%g' % x) if abs(x) < 1e5 else ('%.0f' % x)
    return s.replace('.', ',').replace('-', '−')
KOMA = FuncFormatter(fmt)
def sv(f, n): f.savefig(n, dpi=220, bbox_inches='tight'); plt.close(f)
def sp(ax):
    for s in ['top', 'right']: ax.spines[s].set_visible(False)
def koma(ax, x=True, y=True):
    if x: ax.xaxis.set_major_formatter(KOMA)
    if y: ax.yaxis.set_major_formatter(KOMA)
def ribu(ax, x=False, y=True):
    f = FuncFormatter(lambda v, p: ('%d' % round(v)).replace('-', '−') if abs(v) < 10000 else ('%d %03d' % divmod(round(abs(v)), 1000)).replace(' ', ' ') if v >= 0 else '−' + ('%d %03d' % divmod(round(abs(v)), 1000)).replace(' ', ' '))
    if x: ax.xaxis.set_major_formatter(f)
    if y: ax.yaxis.set_major_formatter(f)

# ---------- CI kulit d^n dalam medan oktahedral (dengan label simetri)
MS = [2, 1, 0, -1, -2]; SO = [(m, s) for s in (1, -1) for m in MS]
CK = {}
for k in (2, 4):
    for a in MS:
        for b in MS: CK[k, a, b] = float((-1)**a * 5 * wigner_3j(2, k, 2, 0, 0, 0) * wigner_3j(2, k, 2, -a, a - b, b))
G = np.zeros((10,) * 4, dtype=object)
GI = {}
for p, q, r, t in itertools.product(range(10), repeat=4):
    (m1, s1), (m2, s2), (m3, s3), (m4, s4) = SO[p], SO[q], SO[r], SO[t]
    if s1 == s3 and s2 == s4 and m1 + m2 == m3 + m4:
        GI[p, q, r, t] = (CK[2, m1, m3] * CK[2, m4, m2], CK[4, m1, m3] * CK[4, m4, m2])
def op(ops, det):
    d, sg = list(det), 1
    for p, c in reversed(ops):
        if c == (p in d): return 0, None
        i = sum(x < p for x in d); sg *= (-1)**i
        d.insert(i, p) if c else d.remove(p)
    return sg, tuple(d)
CACHE = {}
def bagian(n, t2):
    """Matriks terpisah: H = Dq*H1 + F2*H2 + F4*H4 pada sektor 2Ms = t2."""
    if (n, t2) in CACHE: return CACHE[n, t2]
    dets = [d for d in itertools.combinations(range(10), n) if sum(SO[p][1] for p in d) == t2]
    idx = {d: i for i, d in enumerate(dets)}; N = len(dets)
    H1, H2, H4 = np.zeros((N, N)), np.zeros((N, N)), np.zeros((N, N))
    cf = {2: 1, 1: -4, 0: 6, -1: -4, -2: 1}
    for d in dets:
        j = idx[d]
        for p, q in itertools.product(range(10), repeat=2):
            (m1, s1), (m2, s2) = SO[p], SO[q]
            if s1 != s2: continue
            v = cf[m1] if m1 == m2 else (5 if abs(m1) == 2 and m2 == -m1 else 0)
            if v:
                sg, d2 = op([(p, 1), (q, 0)], d)
                if sg: H1[idx[d2], j] += sg * v
        for r, s in itertools.permutations(d, 2):
            for p, q in itertools.product(range(10), repeat=2):
                g = GI.get((p, q, r, s))
                if g is None: continue
                sg, d2 = op([(p, 1), (q, 1), (s, 0), (r, 0)], d)
                if sg and d2 in idx:
                    H2[idx[d2], j] += 0.5 * sg * g[0]; H4[idx[d2], j] += 0.5 * sg * g[1]
    M = np.array([sum(SO[p][0] for p in d) for d in dets])
    CACHE[n, t2] = (H1, H2, H4, (1j) ** (-M)); return CACHE[n, t2]
def tingkat(n, B, C, Dq):
    """Daftar (E, S, label) satu entri per tingkat (label simetri Oh tanpa g)."""
    smax = min(n, 10 - n)
    sek = {}
    for t2 in range(n % 2, smax + 1, 2):
        H1, H2, H4, ph = bagian(n, t2)
        Hm = Dq * H1 + (49 * B + 7 * C) * H2 + (63 * C / 5) * H4
        w, v = np.linalg.eigh(Hm)
        out = []; i = 0
        while i < len(w):
            j = i
            while j + 1 < len(w) and abs(w[j + 1] - w[i]) < 1e-6 * max(1, abs(w[i])) + 1e-7: j += 1
            V = v[:, i:j + 1]; chi = np.real(np.sum(np.abs(V) ** 2 * ph[:, None])); g = j - i + 1
            out.append([w[i], g, chi]); i = j + 1
        sek[t2] = out
    hasil = []
    for t2, L in sek.items():
        atas = [list(x) for x in sek.get(t2 + 2, [])]
        for e, g, chi in L:
            k = next((k for k, x in enumerate(atas) if abs(x[0] - e) < 1e-5 * max(1, abs(e))), None)
            if k is not None:
                # tingkat ini (sebagian) milik spin lebih tinggi
                gg = atas[k][1]
                if gg >= g: atas[k][1] -= g; atas[k][2] -= chi
                if atas[k][1] <= 0: atas.pop(k)
                if gg >= g: continue
                g -= gg; chi -= 0
            lab = {(1, 1): 'A1', (1, -1): 'A2', (2, 0): 'E', (3, 1): 'T1', (3, -1): 'T2'}.get((g, int(round(chi))), 'X')
            hasil.append((e, t2 / 2, lab))
    return sorted(hasil)

# ---------- 1. orbital d
def R3d(r): return r * r * np.exp(-r / 1.6)
f, axs = plt.subplots(1, 5, figsize=(7.4, 1.85))
L = 9.0; x = np.linspace(-L, L, 300); X, Y = np.meshgrid(x, x); rr = np.sqrt(X ** 2 + Y ** 2) + 1e-9
cm = matplotlib.colors.LinearSegmentedColormap.from_list('bj', [J2, J1, '#ffffff', MUDA, B_])
daftar = [('$d_{z^2}$', 'xz', lambda a, b: (3 * b * b - (a * a + b * b)) / 2), ('$d_{x^2-y^2}$', 'xy', lambda a, b: np.sqrt(3) / 2 * (a * a - b * b)),
          ('$d_{xy}$', 'xy', lambda a, b: np.sqrt(3) * a * b), ('$d_{xz}$', 'xz', lambda a, b: np.sqrt(3) * a * b), ('$d_{yz}$', 'yz', lambda a, b: np.sqrt(3) * a * b)]
for ax, (t, pl, fn) in zip(axs, daftar):
    psi = fn(X, Y) / rr ** 2 * R3d(rr); vm = np.abs(psi).max() * 0.75
    ax.contourf(X, Y, psi, levels=np.linspace(-vm, vm, 21), cmap=cm, extend='both')
    ax.contour(X, Y, psi, levels=[0], colors=TUA, linewidths=.5, linestyles='--')
    for px, py in [(7.5, 0), (-7.5, 0), (0, 7.5), (0, -7.5)]: ax.plot(px, py, 'o', color=J2, ms=5, mec=TUA, mew=.5)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(t, fontsize=10)
    ax.set_xlabel(f'bidang {pl}', fontsize=7.5)
    for s in ax.spines.values(): s.set_color('#ccc')
f.tight_layout(); sv(f, 'c_orbitald.png')

# ---------- 2. diagram pemecahan
f, ax = plt.subplots(figsize=(6.8, 3.4)); sp(ax)
kol = [('ion bebas', {'d': 0}), ('tetrahedral', {'e': -2.67, 't$_2$': 1.78}), ('oktahedral', {'t$_{2g}$': -4, 'e$_g$': 6}),
       ('oktahedral\nmemanjang', {'$d_{x^2-y^2}$': 8.0, '$d_{z^2}$': 4.0, '$d_{xy}$': -2.0, '$d_{xz}$, $d_{yz}$': -5.0}),
       ('bujur sangkar', {'$d_{x^2-y^2}$': 12.28, '$d_{xy}$': 2.28, '$d_{z^2}$': -4.28, '$d_{xz}$, $d_{yz}$': -5.14})]
deg = {'d': 5, 'e': 2, 't$_2$': 3, 't$_{2g}$': 3, 'e$_g$': 2, '$d_{xz}$, $d_{yz}$': 2}
pos = {}
for i, (nm, lv) in enumerate(kol):
    x0 = i * 1.6
    for k, E in lv.items():
        n = deg.get(k, 1); w = 0.22
        for j in range(n):
            xs = x0 - (n - 1) * w * 0.55 + j * w * 1.1
            ax.plot([xs - w / 2, xs + w / 2], [E, E], color=B_ if i != 0 else TUA, lw=2)
        dyl = {(4, '$d_{z^2}$'): 0.7, (4, '$d_{xz}$, $d_{yz}$'): -0.6, (3, '$d_{xz}$, $d_{yz}$'): -0.3}.get((i, k), 0)
        ax.text(x0 + n * w * 0.55 + 0.08, E + dyl, k, va='center', fontsize=7.5)
        pos[(i, k)] = E
    ax.text(x0, -7.2, nm, ha='center', va='top', fontsize=8.5)
for (a, b) in [((2, 'e$_g$'), (3, '$d_{x^2-y^2}$')), ((2, 'e$_g$'), (3, '$d_{z^2}$')), ((2, 't$_{2g}$'), (3, '$d_{xy}$')), ((2, 't$_{2g}$'), (3, '$d_{xz}$, $d_{yz}$')),
               ((3, '$d_{x^2-y^2}$'), (4, '$d_{x^2-y^2}$')), ((3, '$d_{z^2}$'), (4, '$d_{z^2}$')), ((3, '$d_{xy}$'), (4, '$d_{xy}$')), ((3, '$d_{xz}$, $d_{yz}$'), (4, '$d_{xz}$, $d_{yz}$')),
               ((0, 'd'), (1, 'e')), ((0, 'd'), (1, 't$_2$')), ((0, 'd'), (2, 't$_{2g}$')), ((0, 'd'), (2, 'e$_g$'))]:
    x1 = a[0] * 1.6 + 0.42 if a[0] != 0 else 0.42; x2 = b[0] * 1.6 - 0.42
    if a[0] == 0 and b[0] == 2: x1, x2 = 0.42, 2 * 1.6 - 0.42
    ax.plot([x1, x2], [pos[a], pos[b]], color='#999', lw=.6, ls='--')
ax.set_xlim(-0.6, 7.4); ax.set_ylim(-7.5, 13.5); ax.set_xticks([]); ax.spines['bottom'].set_visible(False)
ax.set_ylabel('energi ($Dq$)'); koma(ax, x=False); sv(f, 'c_pecah.png')

# ---------- 3. hidrasi dan jari-jari
ion = ['Ca', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']; dn = [0, 3, 4, 5, 6, 7, 8, 9, 10]
Hh = np.array([-1580, -1920, -1905, -1840, -1945, -2000, -2105, -2100, -2045.])
Do = np.array([0, 12400, 13900, 0, 10400, 9300, 8500, 12600, 0.]); fk = np.array([0, -1.2, -0.6, 0, -0.4, -0.8, -1.2, -0.6, 0])
Hc = Hh - fk * Do * 0.011962656
f, axs = plt.subplots(1, 2, figsize=(7.0, 2.9))
ax = axs[0]; sp(ax)
ax.plot(dn, Hh, 'o', color=B_, label='terukur'); ax.plot(dn, Hc, '^', color=J2, label='ESMK dikurangkan')
ax.plot([0, 5, 10], [-1580, -1840, -2045], '--', color='#999', lw=.8)
for d_, h_, nm in zip(dn, Hh, ion): ax.text(d_, h_ - 28, nm, ha='center', va='top', fontsize=7)
ax.set_xlabel('banyak elektron d'); ax.set_ylabel(r'$\Delta H_\mathrm{hid}$ (kJ/mol)'); ax.legend(frameon=False, fontsize=7.5); ribu(ax); ax.set_title('(a)', fontsize=9, loc='left')
ax = axs[1]; sp(ax)
ion2 = ['Ca', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn']; dn2 = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rr_ = [1.00, 0.86, 0.79, 0.80, 0.83, 0.78, 0.745, 0.69, 0.73, 0.74]
ax.plot(dn2, rr_, 'o-', color=B_, lw=1); ax.plot([0, 10], [1.0, 0.74], '--', color='#999', lw=.8)
for d_, r_, nm in zip(dn2, rr_, ion2): ax.text(d_, r_ + 0.012, nm, ha='center', fontsize=7)
ax.set_xlabel('banyak elektron d'); ax.set_ylabel('jari-jari M$^{2+}$ (Å)'); koma(ax); ax.set_title('(b)', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_hidrasi.png')

# ---------- 4. spin d6 dan transisi spin
f, axs = plt.subplots(1, 2, figsize=(7.0, 2.9))
ax = axs[0]; sp(ax); Dg = np.linspace(0.51, 35, 70); E5, E1 = [], []
for D in Dg:
    L = tingkat(6, 1.0, 4.8, D / 10)
    E5.append(min(e for e, S, l in L if S == 2)); E1.append(min(e for e, S, l in L if S == 0 and l == 'A1'))
ax.plot(Dg, E5, color=B_, lw=1.6, label='$^5T_{2g}$ (spin tinggi)'); ax.plot(Dg, E1, color=J2, lw=1.6, label='$^1A_{1g}$ (spin rendah)')
ax.axvline(20.0, color='#999', lw=.7, ls=':'); ax.text(20.5, max(E5) - 5, '20,0', fontsize=8)
ax.set_xlabel(r'$\Delta_o/B$'); ax.set_ylabel(r'$E/B$'); ax.legend(frameon=False, fontsize=7.5); koma(ax); ax.set_title('(a)', fontsize=9, loc='left')
ax = axs[1]; sp(ax); T = np.linspace(80, 320, 500); dHh, dSs, Rg = 8600., 48.8, 8.314
g1 = 1 / (1 + np.exp((dHh - T * dSs) / (Rg * T)))
from scipy.optimize import brentq
Gm = 2800.
g2 = [brentq(lambda g: np.log((1 - g) / g) - (dHh + Gm * (1 - 2 * g) - t * dSs) / (Rg * t), 1e-12, 1 - 1e-12) for t in T]
ax.plot(T, g1, color=B_, lw=1.6, label='molekul bebas'); ax.plot(T, g2, color=J2, lw=1.6, label='dengan interaksi')
ax.axvline(176, color='#999', lw=.7, ls=':'); ax.set_xlabel('$T$ (K)'); ax.set_ylabel(r'$\gamma_\mathrm{ST}$'); ax.legend(frameon=False, fontsize=7.5, loc='lower right'); koma(ax); ax.set_title('(b)', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_spin.png')

# ---------- 5. Jahn-Teller
f, axs = plt.subplots(1, 2, figsize=(7.0, 2.9), gridspec_kw={'width_ratios': [1, 1.3]})
ax = axs[0]; ax.axis('off')
def lvl(ax, x, y, n, lab, el=0, w=0.32):
    for j in range(n):
        xs = x + j * w * 1.15; ax.plot([xs, xs + w], [y, y], color=B_, lw=2)
    ax.text(x + n * w * 1.15 + 0.05, y, lab, va='center', fontsize=7.5)
lvl(ax, 0.0, 3.0, 2, '$e_g$'); lvl(ax, 0.0, -2.0, 3, '$t_{2g}$')
lvl(ax, 2.2, 3.8, 1, '$d_{x^2-y^2}$'); lvl(ax, 2.2, 2.2, 1, '$d_{z^2}$'); lvl(ax, 2.2, -1.5, 1, '$d_{xy}$'); lvl(ax, 2.2, -2.25, 2, '$d_{xz}$, $d_{yz}$')
for (x1, y1, x2, y2) in [(1.0, 3, 2.2, 3.8), (1.0, 3, 2.2, 2.2), (1.45, -2, 2.2, -1.5), (1.45, -2, 2.2, -2.25)]: ax.plot([x1, x2], [y1, y2], '--', color='#999', lw=.6)
for (x, y, s) in [(2.3, 3.8, '↑'), (2.27, 2.2, '↑↓')]: ax.text(x, y + 0.15, s, fontsize=8, color=J2)
ax.annotate('', xy=(3.9, 3.8), xytext=(3.9, 2.2), arrowprops=dict(arrowstyle='<->', color=TUA, lw=.7)); ax.text(4.0, 3.0, r'$\delta_1$', fontsize=8)
ax.text(0.2, -3.6, 'oktahedral', fontsize=8); ax.text(2.1, -3.6, 'memanjang (d⁹)', fontsize=8)
ax.set_xlim(-0.2, 4.6); ax.set_ylim(-4, 4.6); ax.set_title('(a)', fontsize=9, loc='left')
ax = axs[1]; sp(ax); EJT = 2000.; Q0 = 0.39; A = 2 * EJT / Q0; k = A / Q0; Q = np.linspace(-0.9, 0.9, 400)
ax.plot(Q, 0.5 * k * Q * Q - A * np.abs(Q), color=B_, lw=1.6, label='cabang bawah'); ax.plot(Q, 0.5 * k * Q * Q + A * np.abs(Q), color=J2, lw=1.6, label='cabang atas')
ax.plot(Q, 0.5 * k * Q * Q, color='#999', lw=.8, ls='--', label='elastik saja')
ax.annotate('', xy=(Q0, -EJT), xytext=(Q0, 3 * EJT), arrowprops=dict(arrowstyle='<->', color=TUA, lw=.7)); ax.text(Q0 + 0.03, EJT, r'$4E_\mathrm{JT}$', fontsize=8)
ax.set_ylim(-3000, 12000); ax.set_xlabel(r'$Q$ (Å)'); ax.set_ylabel('energi (cm$^{-1}$)'); ribu(ax); koma(ax, y=False); ax.legend(frameon=False, fontsize=7.5, loc='upper center'); ax.set_title('(b)', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_jt.png')

# ---------- 6. diagram OM ML6 (sigma)
aL = -15.0; blok = {'a1g': (-7.0, 4.0), 't1u': (-3.5, 2.5), 'eg': (-11.0, 2.8)}; MO = {}
for nm, (aM, b) in blok.items():
    E = np.linalg.eigvalsh([[aM, b], [b, aL]]); MO[nm] = E
f, ax = plt.subplots(figsize=(5.6, 4.2)); ax.axis('off')
def garis(x, y, n, col=B_, w=0.25):
    xs = [x - (n - 1) * w * 0.6 + j * w * 1.2 for j in range(n)]
    for xx in xs: ax.plot([xx - w / 2, xx + w / 2], [y, y], color=col, lw=2)
    return xs
lab = {'a1g': '$a_{1g}$', 't1u': '$t_{1u}$', 'eg': '$e_g$', 't2g': '$t_{2g}$'}
garis(0, -11.0, 5, TUA); garis(0, -7.0, 1, TUA); garis(0, -3.5, 3, TUA)
ax.text(-1.25, -11.0, '3d', va='center'); ax.text(-1.25, -7.0, '4s', va='center'); ax.text(-1.25, -3.5, '4p', va='center')
garis(6, aL, 6, TUA); ax.text(7.2, aL, '6 σ ligan\n($a_{1g}+e_g+t_{1u}$)', va='center', fontsize=8)
X = 3.0; nn = {'a1g': 1, 't1u': 3, 'eg': 2}
for nm, (lo, hi) in MO.items():
    dy = {'a1g': -0.35, 'eg': 0.2, 't1u': 0.0}[nm]
    garis(X, lo, nn[nm]); garis(X, hi, nn[nm]); ax.text(X + 0.95, lo + dy, lab[nm], va='center', fontsize=8); ax.text(X + 0.95, hi, lab[nm] + '*', va='center', fontsize=8)
    for yy in (lo, hi):
        ax.plot([0.75 if nm != 'a1g' else 0.3, X - 0.55], [blok[nm][0], yy], ':', color='#999', lw=.6); ax.plot([X + 0.55, 5.1], [yy, aL], ':', color='#999', lw=.6)
xs = garis(X, -11.0, 3); ax.text(X + 0.95, -11.0, '$t_{2g}$', va='center', fontsize=8)
ax.plot([0.75, X - 0.55], [-11, -11], ':', color='#999', lw=.6)
for xx in xs: ax.text(xx, -10.9, '↑↓', ha='center', fontsize=7, color=J2)
for nm in ('a1g', 't1u', 'eg'):
    for xx in garis(X, MO[nm][0], nn[nm]):
        if nm == 'a1g': ax.text(xx - 0.75, MO[nm][0] - 0.12, '↑↓', ha='center', va='center', fontsize=7, color=J2)
        else: ax.text(xx, MO[nm][0] + 0.1, '↑↓', ha='center', fontsize=7, color=J2)
ax.annotate('', xy=(X + 1.9, MO['eg'][1]), xytext=(X + 1.9, -11.0), arrowprops=dict(arrowstyle='<->', color=TUA, lw=.7))
ax.text(X + 2.0, -10.4, r'$\Delta_o$', fontsize=9)
ax.text(0, -18.0, 'logam', ha='center'); ax.text(X, -18.0, 'ML$_6$', ha='center'); ax.text(6, -18.0, 'ligan', ha='center')
ax.set_xlim(-1.6, 9.0); ax.set_ylim(-18.5, -1.5)
ax2 = ax.inset_axes([0.0, 0.0, 0.0001, 1]); ax2.set_ylim(-18.5, -1.5); ax2.set_yticks([-17, -15, -13, -11, -9, -7, -5, -3]); ax2.yaxis.set_major_formatter(KOMA); ax2.set_xticks([])
ax2.set_ylabel('energi (eV)', fontsize=8); ax2.tick_params(labelsize=7.5)
sv(f, 'c_om.png')

# ---------- 7. pengaruh pi
ad, Eeg = -11.0, MO['eg'][1]
f, axs = plt.subplots(1, 3, figsize=(7.0, 2.9), sharey=True)
for ax, (judul, api) in zip(axs, [('donor σ saja', None), ('donor π', -16.0), ('akseptor π', -7.0)]):
    ax.set_xticks([]); sp(ax); ax.spines['bottom'].set_visible(False)
    if api is None: t2 = ad
    else:
        E = np.linalg.eigvalsh([[ad, 1.0], [1.0, api]]); t2 = E[1] if api < ad else E[0]; tl = E[0] if api < ad else E[1]
        ax.plot([1.6, 2.4], [api, api], color=H, lw=2); ax.text(2.45, api, 'π' if api < ad else 'π*', va='center', fontsize=8, color=H)
        ax.plot([0.2, 0.8], [tl, tl], color=MUDA, lw=1.5); ax.plot([0.8, 1.6], [tl, api], ':', color='#999', lw=.6); ax.plot([0.8, 1.6], [t2, api], ':', color='#999', lw=.6)
    ax.plot([0.2, 0.8], [Eeg, Eeg], color=B_, lw=2); ax.text(0.85, Eeg + 0.25, '$e_g^*$', va='center', fontsize=8)
    ax.plot([0.2, 0.8], [t2, t2], color=J2, lw=2); ax.text(0.85, t2 - 0.3, '$t_{2g}$', va='center', fontsize=8)
    ax.annotate('', xy=(0.08, Eeg), xytext=(0.08, t2), arrowprops=dict(arrowstyle='<->', color=TUA, lw=.7))
    v = int(round((Eeg - t2) * 8065.544, -1))
    ax.text(0.15, (Eeg + t2) / 2, r'$\Delta_o$ = %d %03d cm$^{-1}$' % divmod(v, 1000), fontsize=7.2, va='center', ha='left',
            bbox=dict(fc='white', ec='none', pad=0.5))
    ax.set_title(judul, fontsize=9); ax.set_xlim(-0.1, 2.9)
axs[0].set_ylabel('energi (eV)'); axs[0].set_ylim(-16.8, -6.3); koma(axs[0], x=False)
f.tight_layout(); sv(f, 'c_pi.png')

# ---------- 8. diagram korelasi d2
f, ax = plt.subplots(figsize=(5.8, 4.0)); sp(ax)
ts = np.linspace(0.0013, 0.97, 120); data = {}
for k, t in enumerate(ts):
    Bv = 861 * (1 - t); L = tingkat(2, Bv, 4.42 * Bv, 2000 * t); cnt = {}
    for e, S, l in L:
        key = (S, l); i = cnt.get(key, 0); cnt[key] = i + 1
        data.setdefault((S, l, i), np.full(len(ts), np.nan))[k] = e
for (S, l, i), Es in data.items():
    ok = np.isfinite(Es)
    if l == 'X' or ok.sum() < 0.8 * len(ts): continue
    Es = np.interp(ts, ts[ok], Es[ok])
    ax.plot(ts, Es, color=B_ if S == 1 else J2, lw=1.4 if S == 1 else 1.0)
geser = -1.4 * 4.42 * 861   # A = -49F4 karena F0 = 0 dalam perhitungan
for nm, e in [('$^3F$', -8 * 861), ('$^1D$', -3 * 861 + 2 * 4.42 * 861), ('$^3P$', 7 * 861), ('$^1G$', 4 * 861 + 2 * 4.42 * 861), ('$^1S$', 14 * 861 + 7 * 4.42 * 861)]:
    ax.text(-0.02, e + geser + (600 if nm == '$^3P$' else (-600 if nm == '$^1D$' else 0)), nm, ha='right', va='center', fontsize=8)
for nm, e, isi in [('$t_{2g}^2$', -16000, '$^3T_{1g}$, $^1A_{1g}$, $^1E_g$, $^1T_{2g}$'), ('$t_{2g}e_g$', 4000, '$^3T_{1g}$, $^3T_{2g}$, $^1T_{1g}$, $^1T_{2g}$'), ('$e_g^2$', 24000, '$^3A_{2g}$, $^1A_{1g}$, $^1E_g$')]:
    ax.text(1.0, e + 1300, nm, va='bottom', ha='center', fontsize=8.5); ax.text(1.0, e - 1300, isi, va='top', ha='center', fontsize=6.3)
ax.set_xlim(-0.12, 1.18); ax.set_xticks([0, 0.97]); ax.set_xticklabels(['medan lemah\n(ion bebas)', 'medan kuat'])
ax.set_ylim(-20500, 36000); ax.set_ylabel('energi (cm$^{-1}$)'); ribu(ax); sv(f, 'c_korelasi.png')

# ---------- 9. Orgel pola F
f, ax = plt.subplots(figsize=(5.8, 3.6)); sp(ax); Bv = 860.
x = np.linspace(-2000, 2000, 401)
T1a, T1b = [], []
for xx in x:
    Dq = abs(xx); s = 1 if xx >= 0 else -1
    E = np.linalg.eigvalsh([[-6 * s * Dq, 4 * Dq], [4 * Dq, 15 * Bv]]); T1a.append(E[0]); T1b.append(E[1])
xa = np.abs(x); s = np.sign(x)
ax.plot(x, T1a, color=B_, lw=1.6); ax.plot(x, T1b, color=B_, lw=1.6)
ax.plot(x, 2 * s * xa, color=H, lw=1.6); ax.plot(x, 12 * s * xa, color=J2, lw=1.6)
ax.plot(x, -6 * s * xa, color=B_, lw=.7, ls='--'); ax.plot(x, 15 * Bv + 0 * x, color=B_, lw=.7, ls='--')
ax.axvline(0, color=TUA, lw=.6)
for (xx, yy, t) in [(2050, T1a[-1], '$T_1(F)$'), (2050, T1b[-1], '$T_1(P)$'), (2050, 4000, '$T_2$'), (2050, 24000, '$A_2$'),
                    (-2050, T1a[0], '$T_1(F)$'), (-2050, T1b[0], '$T_1(P)$'), (-2050, -4000, '$T_2$'), (-2050, -24000, '$A_2$')]:
    ax.text(xx, yy, t, fontsize=8, va='center', ha='left' if xx > 0 else 'right')
ax.text(-1000, 31000, 'd³, d⁸ oktahedral', ha='center', fontsize=8.5); ax.text(1000, 31000, 'd², d⁷ oktahedral', ha='center', fontsize=8.5)
ax.text(40, 15 * Bv + 900, '$P$', fontsize=8); ax.text(40, 700, '$F$', fontsize=8)
ax.set_xlabel('$Dq$ (cm$^{-1}$)'); ax.set_ylabel('energi (cm$^{-1}$)'); ax.set_xlim(-2600, 2600); ax.set_ylim(-26000, 33000)
ax.set_xticks([-2000, -1000, 0, 1000, 2000]); ax.set_xticklabels(['2000', '1000', '0', '1000', '2000']); ribu(ax)
sv(f, 'c_orgel.png')

# ---------- 10. Tanabe-Sugano
def kurva(n, gam, Dg):
    """Kurva per (S, label, indeks); titik yang gagal dilabeli (persilangan kebetulan) diisi NaN."""
    data = {}; S0 = []
    for k, D in enumerate(Dg):
        L = tingkat(n, 1.0, gam, D / 10); e0 = L[0][0]; S0.append(L[0][1])
        cnt = {}
        for e, S, l in L:
            key = (S, l); i = cnt.get(key, 0); cnt[key] = i + 1
            data.setdefault((S, l, i), np.full(len(Dg), np.nan))[k] = e - e0
    return data, S0
cfg = [(2, 4.42, 40, 70), (3, 4.5, 40, 75), (6, 4.8, 40, 75), (8, 4.71, 40, 70)]
f, axs = plt.subplots(2, 2, figsize=(7.2, 7.4))
for ax, (n, gam, xm, ym) in zip(axs.flat, cfg):
    sp(ax); Dg = np.linspace(0.0137, xm, 200) + 0.00731
    data, S0 = kurva(n, gam, Dg); S0 = np.array(S0); labs = []
    for (S, l, i), Es in data.items():
        if l == 'X' or np.nanmin(Es) > ym: continue
        ok = np.isfinite(Es)
        if ok.sum() < 0.8 * len(Es): continue
        Es = np.interp(Dg, Dg[ok], Es[ok])
        for seg in ([S0 == S0[0]], [S0 != S0[0]]):
            m = seg[0]
            if not m.any(): continue
            Sg = S0[m][0]; y = np.where(m, Es, np.nan)
            ax.plot(Dg, y, color=B_ if S == Sg else ('#888' if abs(S - Sg) > 1 else J2), lw=1.5 if S == Sg else .7)
        lbl = f'$^{int(2*S+1)}{l[0]}_{{{l[1:]}}}$' if len(l) > 1 else f'$^{int(2*S+1)}{l}$'
        if Es[-1] < ym * 0.97: labs.append([Es[-1], lbl])
    labs.sort(); jarak = ym * 0.028
    for j in range(1, len(labs)):
        if labs[j][0] - labs[j - 1][0] < jarak: labs[j][0] = labs[j - 1][0] + jarak
    for y, lbl in labs: ax.text(xm + 0.4, y, lbl, fontsize=6, va='center')
    if n == 6: ax.axvline(Dg[np.argmax(S0 != S0[0])], color='#999', lw=.7, ls=':')
    ax.set_xlim(0, xm + 5); ax.set_ylim(0, ym); ax.set_title(f'd{"⁰¹²³⁴⁵⁶⁷⁸⁹"[n]}   ($C/B$ = {fmt(gam)})', fontsize=9.5)
    ax.set_xlabel(r'$\Delta_o/B$'); ax.set_ylabel(r'$E/B$'); koma(ax)
f.tight_layout(); sv(f, 'c_tanabe.png')

# ---------- 11. spektrum model
def gs(x, x0, e, w): return e * np.exp(-4 * np.log(2) * ((x - x0) / w) ** 2)
from matplotlib.colors import hsv_to_rgb
def warna_nm(l):
    l = np.clip(l, 380, 750)
    if l < 440: r, g, b = -(l - 440) / 60, 0, 1
    elif l < 490: r, g, b = 0, (l - 440) / 50, 1
    elif l < 510: r, g, b = 0, 1, -(l - 510) / 20
    elif l < 580: r, g, b = (l - 510) / 70, 1, 0
    elif l < 645: r, g, b = 1, -(l - 645) / 65, 0
    else: r, g, b = 1, 0, 0
    return (r, g, b)
x = np.linspace(5000, 32000, 1200)
spk = [('[Ti(H$_2$O)$_6$]$^{3+}$', gs(x, 17400, 2.2, 3200) + gs(x, 20300, 3.8, 3600)),
       ('[Ni(H$_2$O)$_6$]$^{2+}$', gs(x, 8500, 2.0, 2600) + gs(x, 13800, 1.9, 2200) + gs(x, 15300, 1.4, 1800) + gs(x, 25300, 5.0, 3200)),
       ('[Cr(H$_2$O)$_6$]$^{3+}$', gs(x, 17400, 13.0, 3200) + gs(x, 24600, 15.0, 3600) + gs(x, 15000, 0.9, 200))]
f, axs = plt.subplots(3, 1, figsize=(6.4, 5.4), sharex=True)
for ax, (t, y) in zip(axs, spk):
    sp(ax)
    for nu in np.arange(13300, 26300, 100): ax.axvspan(nu, nu + 100, ymin=0, ymax=0.06, color=warna_nm(1e7 / nu), lw=0)
    ax.plot(x, y, color=TUA, lw=1.3); ax.fill_between(x, y, color=MUDA, alpha=.4)
    ax.set_ylabel(r'$\varepsilon$ (L mol$^{-1}$ cm$^{-1}$)', fontsize=8); ax.text(0.99, 0.85, t, transform=ax.transAxes, ha='right', fontsize=9); koma(ax, x=False)
    ax.set_ylim(-0.08 * y.max(), y.max() * 1.15)
axs[0].set_title('(a)', fontsize=9, loc='left'); axs[1].set_title('(b)', fontsize=9, loc='left'); axs[2].set_title('(c)', fontsize=9, loc='left')
axs[2].set_xlabel(r'$\tilde\nu$ (cm$^{-1}$)'); ribu(axs[2], x=True, y=False)
axs[2].annotate('$^2E_g$', xy=(15000, 1.0), xytext=(11000, 6), fontsize=8, arrowprops=dict(arrowstyle='->', lw=.6, color=TUA))
f.tight_layout(); sv(f, 'c_spektrum.png')

# ---------- 12. karbonil
q = [-2, -1, 0, 1, 2]; nu = [1748, 1859, 2000, 2090, 2204]; nm = ['Ti', 'V', 'Cr', 'Mn', 'Fe']
u = 1.66053906660e-27; mu = 12.000 * 15.9949 / 27.9949 * u; c = 2.99792458e10
kk = [mu * (2 * pi * c * v) ** 2 for v in nu]
f, axs = plt.subplots(1, 2, figsize=(7.0, 2.8))
for ax, y, yl, y0 in [(axs[0], nu, r'$\tilde\nu$(CO) (cm$^{-1}$)', 2143), (axs[1], kk, r'$k$(CO) (N/m)', mu * (2 * pi * c * 2143) ** 2)]:
    sp(ax); ax.plot(q, y, 'o-', color=B_); ax.axhline(y0, color='#999', ls='--', lw=.8)
    for qq, yy, n_ in zip(q, y, nm): ax.text(qq, yy + (y[-1] - y[0]) * 0.04, n_, ha='center', fontsize=8)
    ax.set_xlabel('muatan kompleks $n$'); ax.set_ylabel(yl); ax.set_xticks(q); ax.set_xticklabels(['−2', '−1', '0', '+1', '+2']); ribu(ax)
axs[0].text(-2.0, 2143 + 12, 'CO bebas', fontsize=7.5, color='#666'); axs[0].set_title('(a)', fontsize=9, loc='left'); axs[1].set_title('(b)', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_karbonil.png')
print('selesai')
