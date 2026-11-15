#!/usr/bin/env python3
# Gambar Bab 12 Kimia Kuantum. Jalankan dari folder fig/: python3 gambar.py
import json, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.colors import LinearSegmentedColormap
from math import pi, sqrt, factorial
from scipy import integrate
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
def kt(s): return s.replace('.', ',')

# 1. bentuk orbital hibrida (hidrogenik, Z = 3,25), bidang xz
Z = 3.25
def R20(r): return 2 * (Z / 2) ** 1.5 * (1 - Z * r / 2) * np.exp(-Z * r / 2)
def R21(r): return (Z / 2) ** 1.5 * Z * r / sqrt(3) * np.exp(-Z * r / 2) / sqrt(1)
L = 3.2; x = np.linspace(-L, L, 500); X, Zc = np.meshgrid(x, x); rr = np.hypot(X, Zc) + 1e-9; ct = Zc / rr
s = -R20(rr) / sqrt(4 * pi); pz = R21(rr) * sqrt(3 / (4 * pi)) * ct
def hyb(a): return sqrt(a) * s + sqrt(1 - a) * pz
panel = [(s, '2s'), (pz, '2p$_z$'), (hyb(0.5), 'sp (50% s)'), (hyb(1 / 3), 'sp$^2$ (33% s)'), (hyb(0.25), 'sp$^3$ (25% s)'), (hyb(0.2), 'sp$^4$ (20% s)')]
f, axs = plt.subplots(2, 3, figsize=(6.6, 4.5))
for ax, (psi, t) in zip(axs.flat, panel):
    vm = np.abs(psi).max() * 0.55
    ax.contourf(X, Zc, psi, levels=np.linspace(-vm, vm, 23), cmap=CM, extend='both')
    ax.contour(X, Zc, psi, levels=[0], colors=TUA, linewidths=.6, linestyles='--')
    ax.plot(0, 0, 'o', color=TUA, ms=2.5); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(t, fontsize=9)
    for sp in ax.spines.values(): sp.set_color('#ccc')
f.tight_layout(); sv(f, 'c_hibrida.png')

# 2. sudut antarhibrida terhadap karakter s
f, ax = plt.subplots(figsize=(5.4, 3.2)); sp_(ax)
a = np.linspace(0, 0.5, 400); ax.plot(100 * a, np.degrees(np.arccos(-a / (1 - a))), color=B, lw=1.8)
for nm, al, dx, dy in [('sp$^3$', .25, 1.2, -4), ('sp$^2$', 1 / 3, 1.2, -4), ('sp', .5, -4, -8)]:
    th = np.degrees(np.arccos(-al / (1 - al))); ax.plot(100 * al, th, 'o', color=TUA, ms=5); ax.text(100 * al + dx, th + dy, nm, fontsize=8.5)
for nm, th in [('H$_2$O', 104.52), ('NH$_3$', 106.67), ('PH$_3$', 93.3), ('H$_2$S', 92.1)]:
    c = np.cos(np.radians(th)); al = -c / (1 - c); ax.plot(100 * al, th, 's', color=J2, ms=4.5); ax.text(100 * al + 1.0, th - 3.8 if nm != 'NH$_3$' else th + 1.5, nm, fontsize=8, color=J2)
ax.axhline(90, color='#999', lw=.7, ls='--'); ax.text(41, 91.5, 'p murni: 90°', fontsize=7.5, color='#666')
ax.set_xlabel('karakter s tiap hibrida ikatan (%)'); ax.set_ylabel('sudut antarhibrida (°)'); ax.set_xlim(0, 52); ax.set_ylim(85, 185); koma(ax)
sv(f, 'c_sudut.png')

# 3. tumpang tindih terhadap karakter s (orbital Slater C 1,625; H 1,0)
A0 = 0.529177
def Ns(n, z): return (2 * z) ** (n + .5) / sqrt(factorial(2 * n))
def rad(n, z, r): return Ns(n, z) * r ** (n - 1) * np.exp(-z * r)
def ov(fa, fb, Rb):
    def g(rho, zz):
        ra = np.hypot(rho, zz); rb = np.hypot(rho, zz - Rb); ca = zz / ra if ra > 0 else 1; cb = (Rb - zz) / rb if rb > 0 else 1
        return 2 * pi * rho * fa(ra, ca) * fb(rb, cb)
    return integrate.dblquad(g, -25, Rb + 25, 0, 25, epsabs=1e-8)[0]
zC = 1.625
sC = lambda r, c: rad(2, zC, r) / sqrt(4 * pi); pC = lambda r, c: rad(2, zC, r) * sqrt(3 / (4 * pi)) * c
hH = lambda r, c: rad(1, 1.0, r) / sqrt(4 * pi)
al = np.linspace(0, 1, 301)
f, ax = plt.subplots(figsize=(5.6, 3.3)); sp_(ax)
Rb = 1.09 / A0; Ss, Sp = ov(sC, hH, Rb), ov(pC, hH, Rb)
ax.plot(100 * al, np.sqrt(al) * Ss + np.sqrt(1 - al) * Sp, color=J2, lw=1.7, label='C–H (109 pm)')
for Rang, col, lab in [(1.54, B, 'C–C (154 pm)'), (1.339, H, 'C–C (134 pm)'), (1.203, TUA, 'C–C (120 pm)')]:
    Rb = Rang / A0; Sss, Ssp, Spp = ov(sC, sC, Rb), ov(sC, pC, Rb), ov(pC, pC, Rb)
    S = al * Sss + 2 * np.sqrt(al * (1 - al)) * Ssp + (1 - al) * Spp
    ax.plot(100 * al, S, color=col, lw=1.5, label=lab); ax.plot(100 * al[S.argmax()], S.max(), 'o', color=col, ms=3.5)
for v, t in [(25, 'sp$^3$'), (100 / 3, 'sp$^2$'), (50, 'sp')]: ax.axvline(v, color='#bbb', lw=.7, ls=':'); ax.text(v + 0.8, 0.915, t, fontsize=8, color='#666')
ax.set_xlabel('karakter s hibrida karbon (%)'); ax.set_ylabel('integral tumpang tindih $S$'); ax.set_xlim(0, 100); ax.set_ylim(0.28, 0.95)
ax.legend(frameon=False, fontsize=7.8, loc='lower center', ncol=2); koma(ax); sv(f, 'c_tumpang.png')

# 4. metana dalam kubus dan ikatan bengkok siklopropana
f = plt.figure(figsize=(6.6, 3.1))
ax = f.add_subplot(1, 2, 1, projection='3d')
cor = np.array([[i, j, k] for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)])
for p in cor:
    for q in cor:
        if np.sum(np.abs(p - q)) == 2: ax.plot(*zip(p, q), color='#bbb', lw=.7)
Hs = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
for h in Hs: ax.plot([0, h[0]], [0, h[1]], [0, h[2]], color=B, lw=2.2); ax.scatter(*h, color=MUDA, s=70, edgecolor=TUA, depthshade=False)
ax.scatter(0, 0, 0, color=TUA, s=110, depthshade=False)
ax.text(1.1, 1.1, 1.25, '(1, 1, 1)', fontsize=7.5); ax.text(1.1, -1.1, -1.35, '(1, −1, −1)', fontsize=7.5)
ax.set_box_aspect((1, 1, 1)); ax.set_axis_off(); ax.view_init(18, 28); ax.set_title('(a) CH$_4$: arah ke sudut kubus', fontsize=9)
ax = f.add_subplot(1, 2, 2); ax.set_aspect('equal'); ax.axis('off')
P = np.array([[np.cos(t), np.sin(t)] for t in np.radians([90, 210, 330])])
for i in range(3):
    for j in range(i + 1, 3): ax.plot(*zip(P[i], P[j]), color='#999', lw=.8, ls='--')
dev = np.radians(22.4)
for i in range(3):
    for j in range(3):
        if i == j: continue
        d = P[j] - P[i]; d /= np.linalg.norm(d); out = -(P[i] + P[j]) / 2; out /= np.linalg.norm(out)
        sgn = np.sign(d[0] * out[1] - d[1] * out[0]); c, s_ = np.cos(dev), np.sin(dev)
        # putar d ke arah luar sebesar dev
        cand1 = np.array([d[0] * c - d[1] * s_, d[0] * s_ + d[1] * c]); cand2 = np.array([d[0] * c + d[1] * s_, -d[0] * s_ + d[1] * c])
        v = cand1 if (cand1 @ (P[i] - 0)) > (cand2 @ (P[i] - 0)) else cand2
        ax.annotate('', xy=P[i] + 0.62 * v, xytext=P[i], arrowprops=dict(arrowstyle='-|>', color=B, lw=1.6, mutation_scale=9))
for p in P: ax.plot(*p, 'o', color=TUA, ms=10)
ax.text(P[1][0] + 0.32, P[1][1] + 0.1, '60°', ha='center', fontsize=8, color='#666'); ax.text(0, -1.0, 'sudut antarhibrida ± 105°', ha='center', fontsize=8, color=B)
ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.15, 1.35); ax.set_title('(b) ikatan bengkok siklopropana', fontsize=9)
sv(f, 'c_metana.png')

# 5. sudut ikatan hidrida terhadap periode
f, ax = plt.subplots(figsize=(5.2, 3.0)); sp_(ax)
per = [2, 3, 4, 5]
ax.plot(per, [104.52, 92.1, 90.6, 90.3], 'o-', color=B, lw=1.5, label='H$_2$O, H$_2$S, H$_2$Se, H$_2$Te')
ax.plot(per, [106.67, 93.3, 92.1, 91.6], 's-', color=J2, lw=1.5, label='NH$_3$, PH$_3$, AsH$_3$, SbH$_3$')
ax.axhline(109.47, color='#999', lw=.7, ls='--'); ax.text(4.25, 108.0, 'tetrahedral 109,47°', fontsize=7.5, color='#666')
ax.axhline(90, color='#999', lw=.7, ls=':'); ax.text(4.5, 88.2, 'p murni 90°', fontsize=7.5, color='#666')
ax.set_xticks(per); ax.set_xlabel('periode atom pusat'); ax.set_ylabel('sudut H–X–H (°)'); ax.set_ylim(86, 112)
ax.legend(frameon=False, fontsize=8); koma(ax); sv(f, 'c_hidrida.png')

# 6. sifat dan hibridisasi
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9))
ax = axs[0]; sp_(ax)
pts = [('CH$_4$', 25, 125), ('C$_2$H$_4$', 100 / 3, 156), ('C$_2$H$_2$', 50, 249)]
for nm, s_, j in pts: ax.plot(s_, j, 'o', color=B, ms=5); ax.text(s_ + 1.2, j - 9, nm, fontsize=8)
xx = np.linspace(0, 55, 10); ax.plot(xx, 5 * xx, color='#999', lw=.9, ls='--'); ax.text(6, 60, '$J = 500\\,\\alpha$ Hz', fontsize=8, color='#666')
for nm, j in [('siklopropana', 161), ('benzena', 158)]: ax.axhline(j, xmin=0, xmax=0.0, color='w')
ax.set_xlabel('karakter s, $\\alpha$ (%)'); ax.set_ylabel('$^1J(^{13}$C–H) (Hz)'); ax.set_xlim(0, 55); ax.set_ylim(0, 290); koma(ax); ax.set_title('(a)', fontsize=9, loc='left')
ax = axs[1]; sp_(ax)
dat = [('sp$^3$–sp$^3$', .5, 153.5), ('sp$^3$–sp$^2$', .25 + 1 / 3, 150.1), ('sp$^3$–sp', .75, 145.9), ('sp$^2$–sp$^2$', 2 / 3, 146.7), ('sp$^2$–sp', 1 / 3 + .5, 143.1), ('sp–sp', 1.0, 137.6)]
xs = np.array([d[1] for d in dat]); ys = np.array([d[2] for d in dat]); cc = np.polyfit(xs, ys, 1)
ax.plot(xs, ys, 'o', color=J2, ms=5); xx = np.linspace(.45, 1.05, 10); ax.plot(xx, np.polyval(cc, xx), color='#999', lw=.9, ls='--')
for nm, x_, y_ in dat: ax.text(x_ + 0.015, y_ + 0.5, nm, fontsize=7)
ax.set_xlabel('jumlah karakter s kedua hibrida'); ax.set_ylabel('panjang ikatan C–C tunggal (pm)'); koma(ax); ax.set_title('(b)', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_sifat.png')

# 7. ikatan tiga pusat
f, axs = plt.subplots(1, 2, figsize=(6.6, 3.2))
r2 = sqrt(2)
orbs = [(r2, [0.5, 0.707, 0.5]), (0, [0.707, 0, -0.707]), (-r2, [0.5, -0.707, 0.5])]
for ax, (judul, ne, lab) in zip(axs, [('(a) 3 pusat 4 elektron: F–Xe–F', 4, ['F', 'Xe', 'F']), ('(b) 3 pusat 2 elektron: B–H–B', 2, ['B', 'H', 'B'])]):
    ax.axis('off'); ax.set_xlim(-0.2, 4.4); ax.set_ylim(-2.1, 2.0); ax.set_title(judul, fontsize=9)
    sisa = ne
    for k, (E, c) in enumerate(orbs):
        y = -E * 1.0
        ax.plot([0.2, 1.4], [y, y], color=TUA, lw=1.6)
        nel = min(2, sisa); sisa -= nel
        for q in range(nel): ax.annotate('', xy=(0.65 + 0.3 * q, y + (0.28 if q == 0 else -0.28)), xytext=(0.65 + 0.3 * q, y - (0.28 if q == 0 else -0.28)), arrowprops=dict(arrowstyle='-|>', color=J2, lw=1.1, mutation_scale=7))
        ax.text(-0.15, y, ['$\\alpha + \\sqrt{2}\\beta$', '$\\alpha$', '$\\alpha - \\sqrt{2}\\beta$'][k].replace('+', '+'), fontsize=7.5, ha='right', va='center') if False else None
        ax.text(1.5, y, ['ikatan', 'nonikatan', 'antiikatan'][k], fontsize=7.5, va='center', color='#666')
        for i, ci in enumerate(c):
            xc = 2.7 + 0.6 * i
            if abs(ci) > 1e-6: ax.add_patch(plt.Circle((xc, y), 0.32 * abs(ci), color=B if ci > 0 else J2, alpha=.9))
            else: ax.plot(xc, y, 'x', color='#999', ms=4)
    for i, t in enumerate(lab): ax.text(2.7 + 0.6 * i, -2.0, t, ha='center', fontsize=8.5)
    ax.text(0.2, 1.75, 'energi naik ke atas', fontsize=7, color='#999')
sv(f, 'c_3pusat.png')

# 8. benzena: entalpi hidrogenasi dan tingkat IV
f, axs = plt.subplots(1, 2, figsize=(6.8, 3.1), gridspec_kw={'width_ratios': [1.25, 1]})
ax = axs[0]; ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(-400, 120)
lv = [(0.3, 0, 'sikloheksatriena\nhipotetis'), (0.3, 0, '')]
ax.plot([0.5, 3.0], [0, 0], color=TUA, lw=1.5); ax.text(1.75, 12, 'sikloheksatriena\nhipotetis', ha='center', fontsize=7.5, va='bottom')
ax.plot([3.8, 6.3], [-150.7, -150.7], color=B, lw=1.5); ax.text(5.05, -140, 'benzena', ha='center', fontsize=8, va='bottom')
ax.plot([0.5, 9.5], [-359.1, -359.1], color=TUA, lw=1.5); ax.text(5, -390, 'sikloheksana', ha='center', fontsize=8)
ax.annotate('', xy=(1.4, -359.1), xytext=(1.4, 0), arrowprops=dict(arrowstyle='-|>', color=J2, lw=1.2)); ax.text(1.55, -200, '3 × 119,7\n= 359,1', fontsize=7.5, color=J2)
ax.annotate('', xy=(5.6, -359.1), xytext=(5.6, -150.7), arrowprops=dict(arrowstyle='-|>', color=J2, lw=1.2)); ax.text(5.75, -270, '208,4', fontsize=7.5, color=J2)
ax.annotate('', xy=(4.3, -150.7), xytext=(4.3, 0), arrowprops=dict(arrowstyle='<|-|>', color=H, lw=1.2)); ax.text(3.0, -80, 'resonansi\n150,7', fontsize=7.5, color=H)
ax.text(0.0, 108, '(a) entalpi hidrogenasi (kJ/mol)', fontsize=8.5)
ax = axs[1]; ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(-3.0, 0.75)
for x0, E, t in [(0.5, -1.5, 'satu Kekulé'), (3.7, -2.4, 'dua Kekulé'), (6.9, -2.6056, 'lima struktur')]:
    ax.plot([x0, x0 + 2.4], [E, E], color=B, lw=1.6); ax.text(x0 + 1.2, E - 0.2, ('$Q - %s\\,|J|$' % ('%.3g' % -E).replace('.', '{,}')), ha='center', fontsize=7.5)
    ax.text(x0 + 1.2, 0.22, t, ha='center', fontsize=7.5)
ax.plot([0.3, 9.6], [0, 0], color='#999', lw=.7, ls='--'); ax.text(0.2, 0, '$Q$', fontsize=8, ha='right', va='center')
ax.text(0.0, 0.62, '(b) energi ikatan valensi', fontsize=8.5)
f.tight_layout(); sv(f, 'c_benzena.png')

# 9. kurva energi H2
d = json.load(open('h2curves.json')); R_ = np.array(d['R']); eh = 27.211386
f, ax = plt.subplots(figsize=(5.6, 3.3)); sp_(ax)
for k, col, lab in [('HF', J2, 'OM (RHF)'), ('HL', H, 'Heitler–London'), ('GVB', B, 'GVB (= IK minimal)')]:
    ax.plot(R_, (np.array(d[k]) + 1) * eh, color=col, lw=1.7, label=lab)
ax.plot([1.401], [-4.747], '*', color=TUA, ms=9); ax.text(1.5, -4.85, 'eksak', fontsize=8)
ax.axhline(0, color='#999', lw=.7, ls='--'); ax.text(6.0, 0.15, 'H + H', fontsize=8)
ax.set_xlabel('$R$ (bohr)'); ax.set_ylabel('$E - 2E_\\mathrm{H}$ (eV)'); ax.set_xlim(0.8, 7); ax.set_ylim(-5.2, 3.0)
ax.legend(frameon=False, fontsize=8, loc='upper right'); koma(ax); sv(f, 'c_h2gvb.png')

# 10. spektrum fotoelektron skematik CH4 dan H2O
f, axs = plt.subplots(1, 2, figsize=(6.8, 2.9))
E = np.linspace(10, 26, 1600)
g = lambda x0, w, a: a * np.exp(-((E - x0) / w) ** 2)
ax = axs[0]; sp_(ax)
y = g(13.8, .35, .75) + g(14.4, .4, 1.0) + g(15.0, .35, .8) + g(22.9, .55, .45)
ax.plot(E, y, color=B, lw=1.4); ax.fill_between(E, y, color=MUDA, alpha=.4)
ax.text(14.4, 1.08, '1t$_2$', ha='center', fontsize=8.5); ax.text(22.9, 0.53, '2a$_1$', ha='center', fontsize=8.5)
ax.axvline(16.5, color=J2, lw=.9, ls='--'); ax.text(16.7, 0.9, 'rata-rata\n16,5 eV', fontsize=7.2, color=J2)
ax.set_xlabel('energi ionisasi (eV)'); ax.set_yticks([]); ax.set_ylim(0, 1.25); koma(ax, y=False); ax.set_title('(a) CH$_4$', fontsize=9, loc='left')
ax = axs[1]; sp_(ax)
y = g(12.62, .18, 1.0) + g(14.74, .45, .6) + g(18.51, .55, .45)
ax.plot(E, y, color=B, lw=1.4); ax.fill_between(E, y, color=MUDA, alpha=.4)
for x0, t, h_ in [(12.62, '1b$_1$', 1.04), (14.74, '3a$_1$', .66), (18.51, '1b$_2$', .52)]: ax.text(x0, h_ + 0.03, t, ha='center', fontsize=8.5)
ax.set_xlabel('energi ionisasi (eV)'); ax.set_yticks([]); ax.set_ylim(0, 1.25); ax.set_xlim(10, 22); koma(ax, y=False); ax.set_title('(b) H$_2$O', fontsize=9, loc='left')
f.tight_layout(); sv(f, 'c_fotoelektron.png')
print('selesai')
