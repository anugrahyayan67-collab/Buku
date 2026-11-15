#!/usr/bin/env python3
# Gambar Bab 17 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import sys, os, numpy as np, matplotlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kode'))
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from kq2 import *
import lda
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
ini = sys.argv[1:] or ['semua']
def mau(n): return 'semua' in ini or n in ini

def h2o_yz(R=0.9572, th=104.52):
    R *= ANG; h = np.radians(th) / 2
    return [('O', (0.0, 0.0, 0.0)), ('H', (0.0, R * np.sin(h), R * np.cos(h))), ('H', (0.0, -R * np.sin(h), R * np.cos(h)))]
def nilai_bf(b, X, Y, Z):
    dx, dy, dz = X - b.o[0], Y - b.o[1], Z - b.o[2]; r2 = dx * dx + dy * dy + dz * dz
    l, m, n = b.l; ang = dx ** l * dy ** m * dz ** n
    return ang * sum(b.N[k] * b.c[k] * np.exp(-b.e[k] * r2) for k in range(len(b.e)))
def nilai_mo(bfs, c, X, Y, Z): return sum(c[i] * nilai_bf(bfs[i], X, Y, Z) for i in range(len(bfs)))

# 1. diagram Pople
if mau('pople'):
    f, ax = plt.subplots(figsize=(6.6, 3.6)); ax.axis('off')
    kol = ['HF', 'MP2', 'CCSD', 'CCSD(T)', 'CI penuh']; bar = ['STO-3G', '6-31G', '6-31G*']
    data = {('STO-3G', 'HF'): '−74,9629', ('STO-3G', 'MP2'): '−0,0355', ('STO-3G', 'CCSD'): '−0,0494', ('STO-3G', 'CCSD(T)'): '−0,0494', ('STO-3G', 'CI penuh'): '−0,0495',
            ('6-31G', 'HF'): '−75,9840', ('6-31G', 'MP2'): '−0,1288', ('6-31G', 'CCSD'): '−0,1353', ('6-31G', 'CCSD(T)'): '−0,1363',
            ('6-31G*', 'HF'): '−76,0105', ('6-31G*', 'MP2'): '−0,1885', ('6-31G*', 'CCSD'): '−0,1973', ('6-31G*', 'CCSD(T)'): '−0,1992'}
    for j, b in enumerate(bar):
        for i, k in enumerate(kol):
            x, y = 0.9 + i * 1.05, 0.5 + j * 0.85
            ax.add_patch(plt.Rectangle((x, y), 0.95, 0.72, facecolor=MUDA if (b, k) in data else '#eeeeee', edgecolor='white', alpha=0.35 + 0.2 * j))
            ax.text(x + 0.475, y + 0.36, data.get((b, k), '—'), ha='center', va='center', fontsize=8.5)
        ax.text(0.85, 0.5 + j * 0.85 + 0.36, b, ha='right', va='center', fontsize=9)
    ax.add_patch(plt.Rectangle((0.9 + 4 * 1.05, 0.5 + 3 * 0.85), 0.95, 0.72, facecolor=J1, edgecolor='white'))
    ax.text(0.9 + 4 * 1.05 + 0.475, 0.5 + 3 * 0.85 + 0.36, 'tepat', ha='center', va='center', fontsize=8.5, color='white', weight='bold')
    ax.text(0.85, 0.5 + 3 * 0.85 + 0.36, 'basis lengkap', ha='right', va='center', fontsize=9)
    for i, k in enumerate(kol): ax.text(0.9 + i * 1.05 + 0.475, 0.32, k, ha='center', va='center', fontsize=9)
    ax.annotate('', xy=(6.25, 0.2), xytext=(0.9, 0.2), arrowprops=dict(arrowstyle='->', color=B, lw=1.3)); ax.text(3.6, 0.02, 'korelasi lebih lengkap', ha='center', fontsize=8.5, color=B)
    ax.annotate('', xy=(-0.55, 3.4), xytext=(-0.55, 0.5), arrowprops=dict(arrowstyle='->', color=B, lw=1.3)); ax.text(-0.68, 1.9, 'basis lebih besar', rotation=90, va='center', ha='right', fontsize=8.5, color=B)
    ax.text(3.6, 3.62, 'H₂O: kolom HF = energi total; kolom lain = energi korelasi ($E_h$)', ha='center', fontsize=8.5)
    ax.set_xlim(-0.95, 6.3); ax.set_ylim(-0.05, 3.8); sv(f, 'c_pople.png')

# 2. kurva H2
if mau('h2'):
    Rs = np.linspace(0.8, 6.0, 53); Er, Eu, Ef = [], [], []
    for R in Rs:
        at = [('H', (0, 0, 0)), ('H', (0, 0, R))]; S, T, V, I, b, l = ints(at, STO3G)
        rr = rhf(S, T, V, I, 2, enuc(at)); rr.update(S=S, T=T, V=V, I=I, b=b, lab=l, Enuc=enuc(at))
        Er.append(rr['E']); Eu.append(uhf(S, T, V, I, 1, 1, enuc(at), guess_mix=0.6)['E']); Ef.append(ci(rr)[0])
    S, T, V, I, b, l = ints([('H', (0, 0, 0))], STO3G); Eh_at = T[0, 0] + V[0, 0]
    f, ax = plt.subplots(figsize=(5.4, 3.4)); sp(ax)
    ax.plot(Rs, Er, color=J2, lw=1.6, label='RHF'); ax.plot(Rs, Eu, color=B, lw=1.6, ls='--', label='UHF'); ax.plot(Rs, Ef, color=TUA, lw=1.6, label='CI penuh')
    ax.axhline(2 * Eh_at, color='#999', lw=.8, ls=':'); ax.text(5.9, 2 * Eh_at + 0.012, '2 E(H)', ha='right', fontsize=8, color='#666')
    ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('$E$ ($E_h$)'); ax.set_ylim(-1.16, -0.6); ax.legend(frameon=False, fontsize=8.5); koma(ax); sv(f, 'c_h2kurva.png')

# 3. SCF
if mau('scf'):
    at = h2o_yz(); S, T, V, I, b, l = ints(at, STO3G); En = enuc(at)
    ra = rhf(S, T, V, I, 10, En, diis=False, tol=1e-12); rb = rhf(S, T, V, I, 10, En, diis=True, tol=1e-12)
    Ef = rb['E']
    f, ax = plt.subplots(figsize=(4.8, 3.0)); sp(ax)
    ea = [abs(e - Ef) for _, e in ra['hist']]; eb = [abs(e - Ef) for _, e in rb['hist']]
    def potong(L):
        out = []
        for x in L:
            out.append(x)
            if x < 1e-10: break
        return out
    ea, eb = potong(ea), potong(eb)
    ax.semilogy(range(1, len(ea) + 1), np.maximum(ea, 1e-13), 'o-', color=J2, ms=4, lw=1.2, label='tanpa DIIS')
    ax.semilogy(range(1, len(eb) + 1), np.maximum(eb, 1e-13), '^-', color=B, ms=4, lw=1.2, label='DIIS')
    ax.axhline(1e-10, color='#999', lw=.7, ls=':'); ax.set_xlabel('siklus'); ax.set_ylabel('|E − E$_\\mathrm{akhir}$| ($E_h$)'); ax.legend(frameon=False, fontsize=8.5)
    ax.set_ylim(1e-13, 10); koma(ax, y=False); sv(f, 'c_scf.png')

# 4. STO-nG
if mau('basis'):
    sets = [('STO-1G', [0.270950], [1.0], J1), ('STO-2G', [0.151623, 0.851819], [0.678914, 0.430129], H),
            ('STO-3G', [0.109818, 0.405771, 2.227660], [0.444635, 0.535328, 0.154329], B)]
    r = np.linspace(0, 5, 600); slat = np.exp(-r) / np.sqrt(np.pi)
    f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
    for ax in axs: sp(ax)
    axs[0].plot(r, slat, color=TUA, lw=2, label='Slater 1s'); axs[1].plot(r, 4 * np.pi * r * r * slat ** 2, color=TUA, lw=2)
    for nm, e, c, col in sets:
        bf = BF((0, 0, 0), (0, 0, 0), e, c); g = sum(bf.N[k] * bf.c[k] * np.exp(-bf.e[k] * r * r) for k in range(len(e)))
        axs[0].plot(r, g, color=col, lw=1.2, ls='--', label=nm); axs[1].plot(r, 4 * np.pi * r * r * g * g, color=col, lw=1.2, ls='--')
    axs[0].set_xlabel('$r$ (bohr)'); axs[0].set_ylabel('$\\psi(r)$'); axs[0].legend(frameon=False, fontsize=8)
    axs[1].set_xlabel('$r$ (bohr)'); axs[1].set_ylabel('$4\\pi r^2\\psi^2$')
    ia = axs[0].inset_axes([0.55, 0.12, 0.4, 0.32]); rr = np.linspace(0, 0.4, 100)
    ia.plot(rr, np.exp(-rr) / np.sqrt(np.pi), color=TUA, lw=1.5)
    for nm, e, c, col in sets:
        bf = BF((0, 0, 0), (0, 0, 0), e, c); ia.plot(rr, sum(bf.N[k] * bf.c[k] * np.exp(-bf.e[k] * rr * rr) for k in range(len(e))), color=col, lw=1, ls='--')
    ia.tick_params(labelsize=6); ia.xaxis.set_major_formatter(KOMA); ia.yaxis.set_major_formatter(KOMA)
    for ax in axs: koma(ax)
    f.tight_layout(); sv(f, 'c_basis.png')

# 5. orbital H2O
if mau('orbital'):
    at = h2o_yz(); r = energi(at, STO3G, 10); bfs = r['b']; C = r['C']
    g = np.linspace(-3.2, 3.2, 220); A, Bm = np.meshgrid(g, g)
    pan = [(1, '2a$_1$', 'yz'), (2, '1b$_2$', 'yz'), (3, '3a$_1$', 'yz'), (4, '1b$_1$', 'xz'), (5, '4a$_1$ (LUMO)', 'yz')]
    f, axs = plt.subplots(1, 5, figsize=(7.0, 1.9))
    for ax, (k, nm, bid) in zip(axs, pan):
        if bid == 'yz': X, Y, Zg = 0 * A, A, Bm + 0.6
        else: X, Y, Zg = A, 0 * A, Bm + 0.6
        val = nilai_mo(bfs, C[:, k], X, Y, Zg); m = np.abs(val).max(); lev = m * np.array([0.05, 0.15, 0.3, 0.5, 0.75])
        ax.contour(A, Bm + 0.6, val, levels=lev, colors=B, linewidths=.8); ax.contour(A, Bm + 0.6, val, levels=-lev[::-1], colors=J2, linewidths=.8)
        for e, xyz in at:
            p = (xyz[1], xyz[2]) if bid == 'yz' else (xyz[0], xyz[2])
            if bid == 'yz' or e == 'O': ax.plot(*p, 'o', color=TUA, ms=3)
        ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(nm + (' (bidang xz)' if bid == 'xz' else ''), fontsize=8)
        for s in ax.spines.values(): s.set_color('#bbb')
    f.tight_layout(); sv(f, 'c_orbital.png')

# 6. orbital terlokalisasi
if mau('lokal'):
    at = h2o_yz(); r = energi(at, STO3G, 10); M = dipints(r['b']); bfs = r['b']
    Cl = r['C'][:, :5].copy(); n = 5
    for sweep in range(200):
        ch = 0
        for i in range(n):
            for j in range(i):
                xi = np.array([Cl[:, i] @ M[k] @ Cl[:, i] for k in range(3)]); xj = np.array([Cl[:, j] @ M[k] @ Cl[:, j] for k in range(3)]); xij = np.array([Cl[:, i] @ M[k] @ Cl[:, j] for k in range(3)])
                Aa = np.sum(xij ** 2) - 0.25 * np.sum((xi - xj) ** 2); Bb = np.sum(xij * (xi - xj)); th = 0.25 * np.arctan2(Bb, -Aa)
                if abs(th) > 1e-10:
                    ci_, cj = Cl[:, i].copy(), Cl[:, j].copy(); Cl[:, i] = np.cos(th) * ci_ + np.sin(th) * cj; Cl[:, j] = -np.sin(th) * ci_ + np.cos(th) * cj; ch = max(ch, abs(th))
        if ch < 1e-9: break
    cent = np.array([[Cl[:, i] @ M[k] @ Cl[:, i] for k in range(3)] for i in range(n)])
    ib = [i for i in range(n) if abs(cent[i, 1]) > 0.3 and cent[i, 2] > 0][0]; lp = [i for i in range(n) if abs(cent[i, 0]) > 0.3]
    g = np.linspace(-3, 3, 220); A, Bm = np.meshgrid(g, g)
    f, axs = plt.subplots(1, 2, figsize=(5.6, 2.8))
    hb = at[1][1] if at[1][1][1] * cent[ib, 1] > 0 else at[2][1]; mid = 0.5 * np.array(hb)
    sgn = np.sign(nilai_mo(bfs, Cl[:, ib], np.array(mid[0]), np.array(mid[1]), np.array(mid[2])))
    val = sgn * nilai_mo(bfs, Cl[:, ib], 0 * A, A, Bm + 0.4); m = np.abs(val).max(); lev = m * np.array([0.04, 0.1, 0.2, 0.35, 0.55])
    axs[0].contour(A, Bm + 0.4, val, levels=lev, colors=B, linewidths=.8)
    axs[0].contour(A, Bm + 0.4, val, levels=-lev[::-1], colors=J2, linewidths=.8)
    for e, xyz in at: axs[0].plot(xyz[1], xyz[2], 'o', color=TUA, ms=3)
    axs[0].set_title('ikatan O–H (bidang yz)', fontsize=8.5)
    for k, col in zip(lp, [B, H]):
        val = nilai_mo(bfs, Cl[:, k], A, 0 * A, Bm + 0.4); m = np.abs(val).max(); sgn = np.sign(val[np.unravel_index(np.abs(val).argmax(), val.shape)])
        axs[1].contour(A, Bm + 0.4, sgn * val, levels=m * np.array([0.15, 0.3, 0.5, 0.75]), colors=col, linewidths=.8)
        axs[1].plot(cent[k, 0], cent[k, 2], '+', color=col, ms=8)
    axs[1].plot(0, 0, 'o', color=TUA, ms=3); axs[1].set_title('dua pasangan bebas (bidang xz)', fontsize=8.5)
    for ax in axs:
        ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values(): s.set_color('#bbb')
    f.tight_layout(); sv(f, 'c_lokal.png')

# 7. korelasi
if mau('korelasi'):
    f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8), gridspec_kw={'width_ratios': [1, 1.2]})
    for ax in axs: sp(ax)
    nm = ['MP2', 'CISD', 'CISD+Q', 'CCSD', 'CCSD(T)']; v = np.array([0.035493, 0.048773, 0.050013, 0.049359, 0.049426]) / 0.049475 * 100
    axs[0].barh(nm[::-1], v[::-1], color=[B, H, J1, MUDA, B][::-1]); axs[0].axvline(100, color=TUA, lw=.8, ls='--')
    for i, x in enumerate(v[::-1]): axs[0].text(x + 0.5, i, ('%.1f' % x).replace('.', ','), va='center', fontsize=7.5)
    axs[0].set_xlim(60, 108); axs[0].set_xlabel('% korelasi CI penuh (STO-3G)'); koma(axs[0], y=False)
    bas = ['STO-3G', '6-31G', '6-31G*']; d = {'MP2': [0.035493, 0.128796, 0.188472], 'CCSD': [0.049359, 0.135322, 0.197266], 'CCSD(T)': [0.049426, 0.136316, 0.199154]}
    x = np.arange(3); w = 0.26
    for k, (m, col) in enumerate(zip(d, [B, H, J2])): axs[1].bar(x + (k - 1) * w, -np.array(d[m]), w, color=col, label=m)
    axs[1].set_xticks(x); axs[1].set_xticklabels(bas); axs[1].set_ylabel('$E_\\mathrm{kor}$ ($E_h$)'); axs[1].legend(frameon=False, fontsize=8); koma(axs[1], x=False)
    f.tight_layout(); sv(f, 'c_korelasi.png')

# 8. DFT
if mau('dft'):
    f, axs = plt.subplots(1, 2, figsize=(6.8, 2.8))
    for ax in axs: sp(ax)
    s = np.linspace(0, 5, 300); k, mu = 0.804, 0.21951
    axs[0].plot(s, 1 + k - k / (1 + mu * s * s / k), color=B, lw=1.8, label='PBE'); axs[0].axhline(1, color=TUA, lw=.8, ls='--'); axs[0].text(4.9, 1.03, 'LDA', ha='right', fontsize=8)
    axs[0].axhline(1 + k, color='#999', lw=.7, ls=':'); axs[0].text(4.9, 1.82, 'batas 1 + κ', ha='right', fontsize=8, color='#666')
    axs[0].axvspan(0, 3, color=MUDA, alpha=.25); axs[0].set_xlabel('$s$'); axs[0].set_ylabel('$F_x(s)$'); axs[0].set_ylim(0.9, 1.95); koma(axs[0])
    d = lda.atom(Z=2, nel=2); r = d['r']; rho = d['rho']; rs = (3 / (4 * np.pi * rho)) ** (1 / 3)
    vx = -(3 / np.pi * rho) ** (1 / 3); ec = lda.pw92(rs, False); dd = 1e-6; dec = (lda.pw92(rs * (1 + dd), False) - lda.pw92(rs * (1 - dd), False)) / (2 * rs * dd); vc = ec - rs / 3 * dec
    m = r < 6
    axs[1].plot(r[m], 4 * np.pi * r[m] ** 2 * rho[m], color=B, lw=1.6, label='$4\\pi r^2\\rho$')
    axs[1].plot(r[m], (vx + vc)[m], color=J2, lw=1.6, label='$v_{xc}$ LDA'); axs[1].plot(r[m & (r > 0.4)], -1 / r[m & (r > 0.4)], color=TUA, lw=1, ls='--', label='$-1/r$')
    axs[1].axhline(0, color='#999', lw=.6); axs[1].set_xlabel('$r$ (bohr)'); axs[1].set_ylim(-2.6, 2.0); axs[1].legend(frameon=False, fontsize=8); koma(axs[1])
    f.tight_layout(); sv(f, 'c_dft.png')

# 9. Muller-Brown
if mau('pes'):
    Ak = [-200, -100, -170, 15]; ak = [-1, -1, -6.5, 0.7]; bk = [0, 0, 11, 0.6]; ck = [-10, -10, -6.5, 0.7]; xk = [1, 0, -0.5, -1]; yk = [0, 0.5, 1.5, 1]
    def Vmb(x, y): return sum(Ak[i] * np.exp(ak[i] * (x - xk[i]) ** 2 + bk[i] * (x - xk[i]) * (y - yk[i]) + ck[i] * (y - yk[i]) ** 2) for i in range(4))
    def gr(p, h=1e-6): return np.array([(Vmb(p[0] + h, p[1]) - Vmb(p[0] - h, p[1])) / (2 * h), (Vmb(p[0], p[1] + h) - Vmb(p[0], p[1] - h)) / (2 * h)])
    x = np.linspace(-1.6, 1.2, 300); y = np.linspace(-0.4, 2.0, 300); X, Y = np.meshgrid(x, y); Vg = Vmb(X, Y)
    f, ax = plt.subplots(figsize=(5.2, 4.0))
    cs = ax.contourf(X, Y, np.minimum(Vg, 60), levels=np.arange(-150, 61, 15), cmap='Blues_r'); ax.contour(X, Y, np.minimum(Vg, 60), levels=np.arange(-150, 61, 15), colors='white', linewidths=.4)
    mins = [(-0.558, 1.442), (0.623, 0.028), (-0.050, 0.467)]; sads = [((-0.822, 0.624), (-0.751, 0.660)), ((0.212, 0.293), None)]
    def hess(p, h=1e-4):
        Hm = np.zeros((2, 2))
        for i in range(2):
            for j in range(2):
                ei = np.eye(2)[i] * h; ej = np.eye(2)[j] * h
                Hm[i, j] = (Vmb(*(p + ei + ej)) - Vmb(*(p + ei - ej)) - Vmb(*(p - ei + ej)) + Vmb(*(p - ei - ej))) / (4 * h * h)
        return Hm
    for sp_, _ in sads:
        p0 = np.array(sp_); w, v = np.linalg.eigh(hess(p0)); d0 = v[:, 0]
        for sgn in [1, -1]:
            p = p0 + sgn * 0.01 * d0; path = [p0.copy(), p.copy()]
            for it in range(4000):
                g = gr(p); ng = np.linalg.norm(g)
                if ng < 0.5: break
                p = p - 0.002 * g / ng; path.append(p.copy())
            path = np.array(path); ax.plot(path[:, 0], path[:, 1], color=J1, lw=1.8)
    for m in mins: ax.plot(*m, 'o', color='white', mec=TUA, ms=7)
    for sp_, _ in sads: ax.plot(*sp_, '^', color=J2, mec=TUA, ms=8)
    for nm, p in zip(['A', 'B', 'C'], mins): ax.text(p[0] + 0.06, p[1] + 0.06, nm, color='white', fontsize=9, weight='bold')
    ax.text(-0.822 - 0.2, 0.624 - 0.05, 'S1', color='white', fontsize=9, weight='bold'); ax.text(0.212 + 0.06, 0.293 + 0.04, 'S2', color='white', fontsize=9, weight='bold')
    cb = f.colorbar(cs, ax=ax, shrink=.85); cb.set_label('V'); cb.ax.yaxis.set_major_formatter(KOMA)
    ax.set_xlabel('$x$'); ax.set_ylabel('$y$'); koma(ax); sv(f, 'c_pes.png')
# 10. mode normal H2O (Hessian HF/6-31G*)
if mau('frek'):
    import json
    from frek import proyeksi, MASS
    d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kode', 'hessian_h2o_631gs.json')))
    at = h2o(0.9473, 105.50); els = [a[0] for a in at]; x0 = np.array([c for a in at for c in a[1]], float)
    w, v = proyeksi(els, x0, np.array(d['H'])); m = np.repeat([MASS[e] for e in els], 3)
    f, axs = plt.subplots(1, 3, figsize=(6.8, 2.3))
    nama = ['tekuk', 'ulur simetris', 'ulur antisimetris']
    for ax, k, nm in zip(axs, [6, 7, 8], nama):
        dsp = (v[:, k] / np.sqrt(m)).reshape(3, 3); dsp = dsp / np.abs(dsp).max() * 0.9
        xy = x0.reshape(3, 3) / ANG
        for i in [1, 2]: ax.plot([xy[0, 0], xy[i, 0]], [xy[0, 2], xy[i, 2]], color='#bbb', lw=3, zorder=1)
        for i, e in enumerate(els):
            ax.plot(xy[i, 0], xy[i, 2], 'o', color=J2 if e == 'O' else B, ms=14 if e == 'O' else 9, zorder=2)
            if np.hypot(dsp[i, 0], dsp[i, 2]) > 0.2: ax.annotate('', xy=(xy[i, 0] + 0.45 * dsp[i, 0], xy[i, 2] + 0.45 * dsp[i, 2]), xytext=(xy[i, 0], xy[i, 2]), arrowprops=dict(arrowstyle='->', color=TUA, lw=1.4), zorder=3)
        ax.set_title(f'{nm}\n{w[k]:.0f} cm$^{{-1}}$', fontsize=8.5); ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-0.5, 1.3)
    f.tight_layout(); sv(f, 'c_frek.png')
# 11. alur kerja
if mau('alur'):
    f, ax = plt.subplots(figsize=(6.8, 2.2)); ax.axis('off')
    langkah = [('Pencarian\nkonformasi', 'MM, GFN2-xTB'), ('Optimasi\ngeometri', 'DFT-D, basis DZ/TZ'), ('Frekuensi', 'jenis titik, ZPE,\nH, S, G'),
               ('Energi titik\ntunggal', 'DLPNO-CCSD(T),\nhibrida ganda'), ('Solvasi,\nkeadaan\nstandar', 'PCM/SMD,\nkluster-kontinum'), ('Rata-rata\nBoltzmann', 'semua konformer\nyang relevan')]
    for k, (a, b) in enumerate(langkah):
        x = k * 1.15
        ax.add_patch(plt.Rectangle((x, 0.45), 0.95, 0.5, facecolor=[B, B, H, J2, H, TUA][k], edgecolor='white'))
        ax.text(x + 0.475, 0.7, a, ha='center', va='center', color='white', fontsize=8, weight='bold')
        ax.text(x + 0.475, 0.22, b, ha='center', va='center', fontsize=7.2)
        if k < len(langkah) - 1: ax.annotate('', xy=(x + 1.13, 0.7), xytext=(x + 0.97, 0.7), arrowprops=dict(arrowstyle='->', color=TUA, lw=1.2))
    ax.set_xlim(-0.05, 6.85); ax.set_ylim(0, 1.05); sv(f, 'c_alur.png')

# 12. laju vs penghalang
if mau('laju'):
    f, ax = plt.subplots(figsize=(4.8, 3.0)); sp(ax)
    G = np.linspace(20, 130, 200); kB, hP, R = 1.380649e-23, 6.62607015e-34, 8.314462618
    for T, col in [(200, B), (298.15, TUA), (400, J2)]:
        k = kB * T / hP * np.exp(-G * 1000 / (R * T)); ax.semilogy(G, k, color=col, lw=1.6, label=f'{T:g} K'.replace('.', ','))
    for y, t in [(1 / 3600, 't½ ≈ 1 jam'), (1.0, 't½ ≈ 1 s')]:
        ax.axhline(y * np.log(2), color='#999', lw=.6, ls=':'); ax.text(21, y * np.log(2) * 2.2, t, ha='left', fontsize=7.5, color='#666')
    ax.set_xlabel('$\\Delta G^\\ddagger$ (kJ/mol)'); ax.set_ylabel('$k$ (s$^{-1}$)'); ax.set_ylim(1e-12, 1e10); ax.legend(frameon=False, fontsize=8); koma(ax, y=False)
    sv(f, 'c_laju.png')
print('ok')
