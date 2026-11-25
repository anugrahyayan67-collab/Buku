#!/usr/bin/env python3
# Gambar Bab 4 Kimia Anorganik 1: orbital molekul. -> bab04/fig/*.png
import os, json, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab04')
D = f'{R}/fig'; os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'mathtext.fontset': 'dejavusans'})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
J = json.load(open(f'{R}/_hitung.json'))
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
def koma(ax):
    from matplotlib.ticker import FuncFormatter
    for a in (ax.xaxis, ax.yaxis): a.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−')))

def lev(ax, x, y, lab='', e=0, w=.5, c=TUA, n=1, gap=.1, kiri=False, fs=9, hf=.02):
    """tingkat energi (n garis merosot berdampingan) dengan e elektron"""
    tot = n * w + (n - 1) * gap; x0 = x - tot / 2; xs = []
    for k in range(n):
        a = x0 + k * (w + gap); ax.plot([a, a + w], [y, y], color=c, lw=2, solid_capstyle='butt'); xs.append(a + w / 2)
    # isi elektron: Hund
    isi = [0] * n
    for k in range(e):
        isi[k % n if k < n else k - n] += 1
    y0, y1 = ax.get_ylim(); hh = hf * (y1 - y0); x0_, x1_ = ax.get_xlim(); dx = .022 * (x1_ - x0_)
    for xm, m in zip(xs, isi):
        if m >= 1: ax.annotate('', (xm - dx, y + 1.1 * hh), (xm - dx, y - .9 * hh), arrowprops=dict(arrowstyle='-|>', color=JGT, lw=1.2, mutation_scale=7))
        if m == 2: ax.annotate('', (xm + dx, y - 1.1 * hh), (xm + dx, y + .9 * hh), arrowprops=dict(arrowstyle='-|>', color=JGT, lw=1.2, mutation_scale=7))
    if lab:
        if kiri: ax.text(x0 - .08, y, lab, ha='right', va='center', fontsize=fs, color=c)
        else: ax.text(x0 + tot + .08, y, lab, ha='left', va='center', fontsize=fs, color=c)
    return x0, x0 + tot
def hub(ax, a, b, ya, yb): ax.plot([a, b], [ya, yb], color=ABU, lw=.8, ls=(0, (3, 2)))
def kosong(ax): ax.set_xticks([]); [s.set_visible(False) for k, s in ax.spines.items() if k != 'left']

# 1. LCAO H2: fungsi gelombang sepanjang sumbu dan diagram energi
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 2.9), gridspec_kw={'width_ratios': [1.4, 1]})
x = np.linspace(-3.5, 3.5, 600); A, B = np.exp(-abs(x + .7)), np.exp(-abs(x - .7))
for s, c, lab, dy in [(1, BIRU, 'ikatan: ψ$_A$ + ψ$_B$', 1.6), (-1, JGT, 'antiikatan: ψ$_A$ − ψ$_B$', -.6)]:
    a1.plot(x, A + s * B + dy, color=c, lw=2); a1.fill_between(x, dy, A + s * B + dy, color=c, alpha=.15)
    a1.axhline(dy, color=ABU, lw=.6); a1.text(-3.4, dy + 1.25, lab, color=c, fontsize=9)
for xa in (-.7, .7):
    for dy in (1.6, -.6): a1.add_patch(Circle((xa, dy), .09, color=TUA, zorder=4))
a1.text(0, -1.75, 'simpul di tengah', ha='center', color=JGT, fontsize=8.5); a1.axis('off'); a1.set_ylim(-2.1, 3.4)
a2.set_xlim(-1.1, 4.6); a2.set_ylim(-2.4, 2.6)
lev(a2, 0, 0, 'H 1s', 1, kiri=True); lev(a2, 3, 0, 'H 1s', 1)
lev(a2, 1.5, -1.6, 'σ$_g$ (ikatan)', 2); lev(a2, 1.5, 2, 'σ$_u$* (antiikatan)')
for xa, xb in [(.25, 1.25), (2.75, 1.75)]: hub(a2, xa, xb, 0, -1.6); hub(a2, xa, xb, 0, 2)
a2.annotate('', (1.5, -.05), (1.5, -1.5), arrowprops=dict(arrowstyle='<->', color=ABU, lw=.8)); a2.text(1.58, -.8, 'Δ$E_+$', fontsize=8, color=ABU)
a2.annotate('', (1.5, 1.9), (1.5, .05), arrowprops=dict(arrowstyle='<->', color=ABU, lw=.8)); a2.text(1.58, 1, 'Δ$E_-$ > Δ$E_+$', fontsize=8, color=ABU)
a2.set_xlim(-1.1, 4.6); a2.set_ylim(-2.4, 2.6); a2.axis('off')
simpan(f, 'a_lcao')

# 2. Diatomik periode 2: O2 (tanpa pencampuran) dan N2 (dengan pencampuran)
f, axs = plt.subplots(1, 2, figsize=(7.8, 4.4))
def diatom(ax, judul, nae, ns, mix):
    # energi (sembarang): 2s -6, 2p 0
    s, p = -6, 0
    ax.set_xlim(-1.1, 5.6); ax.set_ylim(-8.4, 3.6)
    Y = {'sg': -7.3, 'su': -4.9, 'pu': -1.3, 'sgp': -.4 if mix else -2.3, 'pg': 1.3, 'sup': 2.8}
    e = nae - 0  # elektron valensi total
    order = ['sg', 'su', 'sgp', 'pu', 'pg', 'sup'] if not mix else ['sg', 'su', 'pu', 'sgp', 'pg', 'sup']
    kap = {'sg': 2, 'su': 2, 'sgp': 2, 'pu': 4, 'pg': 4, 'sup': 2}; isi = {}
    for k in order: isi[k] = min(kap[k], e); e -= isi[k]
    lev(ax, 0, s, '2s', 2, kiri=True); lev(ax, 4, s, '2s', 2)
    lev(ax, 0, p, '2p', ns, n=3, w=.3, gap=.06, kiri=True); lev(ax, 4, p, '2p', ns, n=3, w=.3, gap=.06)
    nm = {'sg': 'σ$_g$(2s)', 'su': 'σ$_u$*(2s)', 'pu': 'π$_u$', 'sgp': 'σ$_g$(2p)', 'pg': 'π$_g$*', 'sup': 'σ$_u$*(2p)'}
    for k in Y:
        n = 2 if k in ('pu', 'pg') else 1
        c = HIJ if (mix and k in ('sgp', 'su')) else TUA
        lev(ax, 2, Y[k], nm[k], isi[k], n=n, w=.45 if n == 2 else .6, c=c)
        src = [(s, s)] if k in ('sg', 'su') else [(p, p)]
        for (ya, yb) in src: hub(ax, .35, 1.6 if n == 1 else 1.45, ya, Y[k]); hub(ax, 3.65, 2.4 if n == 1 else 2.55, yb, Y[k])
    ax.set_title(judul, fontsize=10, color=TUA); ax.set_xlim(-1.1, 5.6); ax.set_ylim(-8.4, 3.6); ax.axis('off')
diatom(axs[0], 'O$_2$ (16 elektron valensi): tanpa pencampuran s–p', 12, 4, False)
diatom(axs[1], 'N$_2$ (10 elektron valensi): dengan pencampuran s–p', 10, 3, True)
axs[0].text(2, -8.2, 'dua elektron tak berpasangan di π$_g$* → paramagnetik', ha='center', fontsize=8.5, color=JGT)
axs[1].text(2, -8.2, 'σ$_g$(2p) terdorong di atas π$_u$ (hijau: orbital yang bercampur)', ha='center', fontsize=8.5, color=HIJ)
simpan(f, 'a_diatom')

# 3. Tren B2–F2: orde ikatan, panjang, energi disosiasi
mol = ['B$_2$', 'C$_2$', 'N$_2$', 'O$_2$', 'F$_2$']; OI = [1, 2, 3, 2, 1]; L = [159, 124, 110, 121, 141]; Dd = [290, 602, 945, 498, 159]
f, ax = plt.subplots(figsize=(6.2, 3.0)); xx = np.arange(5)
ax.bar(xx, Dd, color=MUDA, edgecolor=BIRU, width=.55); ax.set_ylabel('energi disosiasi (kJ mol$^{-1}$)', color=BIRU)
for i, (d, o) in enumerate(zip(Dd, OI)): ax.text(i, d + 18, f'orde {o}', ha='center', fontsize=8.5, color=TUA)
ax2 = ax.twinx(); ax2.plot(xx, L, 'o-', color=JGT, lw=2); ax2.set_ylabel('panjang ikatan (pm)', color=JGT); ax2.set_ylim(90, 170)
ax.set_ylim(0, 1100); koma(ax); ax.set_xticks(xx); ax.set_xticklabels(mol)
simpan(f, 'a_tren')

# 4. CO heteronuklir dengan energi orbital atom (Gray)
f, ax = plt.subplots(figsize=(5.6, 4.6))
Cs, Cp, Os, Op = -19.47, -10.66, -32.36, -15.87
ax.set_xlim(-1.4, 5.6); ax.set_ylim(-36, 0)
lev(ax, 0, Cs, 'C 2s', 2, kiri=True); lev(ax, 0, Cp, 'C 2p', 2, n=3, w=.3, gap=.06, kiri=True)
lev(ax, 4, Os, 'O 2s', 2); lev(ax, 4, Op, 'O 2p', 4, n=3, w=.3, gap=.06)
MO = [('3σ', -34, 2, 1), ('4σ', -21.8, 2, 1), ('1π', -17.3, 4, 2), ('5σ (HOMO)', -14.9, 2, 1), ('2π* (LUMO)', -7.5, 0, 2), ('6σ*', -3, 0, 1)]
for nm, y, e, n in MO:
    lev(ax, 2, y, nm, e, n=n, w=.45 if n == 2 else .6, c=JGT if 'HOMO' in nm or 'LUMO' in nm else TUA)
hub(ax, .35, 1.7, Cs, -34); hub(ax, 3.65, 2.3, Os, -34); hub(ax, .35, 1.7, Cs, -21.8); hub(ax, 3.65, 2.3, Op, -21.8)
hub(ax, .5, 1.55, Cp, -17.3); hub(ax, 3.5, 2.45, Op, -17.3); hub(ax, .35, 1.7, Cp, -14.9); hub(ax, .5, 1.55, Cp, -7.5); hub(ax, 3.5, 2.45, Op, -7.5)
ax.set_ylabel('energi (eV)'); ax.set_xlim(-1.4, 5.6); ax.set_ylim(-36, 0); kosong(ax); koma(ax)
ax.text(-1.3, -27.5, 'oksigen lebih rendah:\norbital ikatan condong ke O,\nHOMO dan LUMO condong ke C', ha='left', va='top', fontsize=8.3, color=TUA)
simpan(f, 'a_co')

# 5. Spektrum fotoelektron batang: N2, CO, H2O (eksperimen) + Koopmans
f, axs = plt.subplots(3, 1, figsize=(6.6, 4.4), sharex=True)
DATA = [('N$_2$', [(15.58, '3σ$_g$'), (16.93, '1π$_u$'), (18.75, '2σ$_u$*')]),
        ('CO', [(14.01, '5σ'), (16.91, '1π'), (19.72, '4σ')]),
        ('H$_2$O', [(12.62, '1b$_2$'), (14.74, '3a$_1$'), (18.51, '1b$_1$')])]
for ax, (m, pk) in zip(axs, DATA):
    xx = np.linspace(11, 21, 800); y = sum((1.6 if 'π' in l else 1) * np.exp(-((xx - e) / .12) ** 2) for e, l in pk)
    ax.plot(xx, y, color=BIRU, lw=1.6); ax.fill_between(xx, 0, y, color=MUDA, alpha=.4)
    for e, l in pk: ax.text(e, 1.75 if 'π' in l else 1.15, l, ha='center', fontsize=8.5, color=TUA)
    ax.text(11.1, 1.4, m, fontsize=11, fontweight='bold', color=TUA); ax.set_ylim(0, 2.3); ax.set_yticks([])
    for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
axs[-1].set_xlabel('energi ionisasi (eV)'); koma(axs[-1])
simpan(f, 'a_pes')

# 6. Diagram MO H2O (molekul di bidang xz, sesuai Bab 3)
f, ax = plt.subplots(figsize=(6.2, 4.8)); ax.set_xlim(-2, 6); ax.set_ylim(-39, 9)
lev(ax, 0, -32.4, 'O 2s (a$_1$)', 2, kiri=True)
for xo, l in [(-.5, 'a$_1$'), (0, 'b$_1$'), (.5, 'b$_2$')]:
    ax.plot([xo - .17, xo + .17], [-15.9, -15.9], color=TUA, lw=2); ax.text(xo, -15.3, l, ha='center', fontsize=8, color=TUA)
ax.text(-.8, -15.9, 'O 2p', ha='right', va='center', fontsize=9, color=TUA)
lev(ax, 4.2, -13.6, 'SALC a$_1$, b$_1$\n(H 1s)', 0, n=2, w=.4, gap=.1)
MO = [('2a$_1$', -36.4, 2, TUA), ('1b$_1$', -19.0, 2, TUA), ('3a$_1$', -15.4, 2, TUA), ('1b$_2$ (tak berikatan)', -13.4, 2, JGT), ('4a$_1$*', 5.0, 0, TUA), ('2b$_1$*', 7.0, 0, TUA)]
for nm, y, e, c in MO: lev(ax, 2.1, y, nm, e, c=c)
for y in (-36.4, -15.4, 5.0): hub(ax, .3, 1.8, -32.4 if y == -36.4 else -15.9, y); hub(ax, 3.85, 2.4, -13.6, y)
for y in (-19.0, 7.0): hub(ax, .17, 1.8, -15.9, y); hub(ax, 4.3, 2.4, -13.6, y)
hub(ax, .67, 1.8, -15.9, -13.4)
ax.set_ylabel('energi orbital (eV, perhitungan)'); ax.set_xlim(-2, 6); ax.set_ylim(-39, 9); kosong(ax); koma(ax)
simpan(f, 'b_h2o')

# 7. CH4 dan SF6 secara ringkas: diagram MO CH4
f, ax = plt.subplots(figsize=(5.8, 4.2)); ax.set_xlim(-2, 6.2); ax.set_ylim(-28, 10)
lev(ax, 0, -19.5, 'C 2s (a$_1$)', 2, kiri=True); lev(ax, 0, -10.7, 'C 2p (t$_2$)', 2, n=3, w=.3, gap=.06, kiri=True)
lev(ax, 4.2, -13.6, 'SALC a$_1$ + t$_2$\n(4 × H 1s)', 4, n=4, w=.22, gap=.05)
for nm, y, e, n in [('2a$_1$', -25.7, 2, 1), ('1t$_2$', -14.8, 6, 3), ('3a$_1$*', 5.3, 0, 1), ('2t$_2$*', 7.5, 0, 3)]:
    lev(ax, 2.1, y, nm, e, n=n, w=.3 if n == 3 else .6, gap=.06)
for ya, y in [(-19.5, -25.7), (-19.5, 5.3)]: hub(ax, .3, 1.8, ya, y); hub(ax, 3.7, 2.4, -13.6, y)
for y in (-14.8, 7.5): hub(ax, .5, 1.55, -10.7, y); hub(ax, 3.7, 2.65, -13.6, y)
ax.set_ylabel('energi orbital (eV, perhitungan)'); ax.set_xlim(-2, 6.2); ax.set_ylim(-28, 10); kosong(ax); koma(ax)
ax.text(2.1, -27.5, 'PES eksperimen: 23 eV (a$_1$) dan 14 eV (t$_2$)', ha='center', fontsize=8.5, color=JGT)
simpan(f, 'b_ch4')

# 8. Ikatan tiga pusat: 3c-2e (diborana) dan 3c-4e (XeF2/I3-)
f, axs = plt.subplots(1, 2, figsize=(7.6, 3.4))
def tiga(ax, judul, e, lab):
    sk = [((1, 1.41, 1), 'ikatan', -1.6), ((1, 0, -1), 'tak berikatan', 0), ((1, -1.41, 1), 'antiikatan', 1.6)]
    ee = [min(2, e), min(2, max(0, e - 2)), 0]; ax.set_xlim(-.5, 5.3); ax.set_ylim(-2.7, 2.3)
    for k, ((a, b, c), nm, y) in enumerate(sk):
        lev(ax, 3.3, y, nm, ee[k], w=.6, hf=.045)
        for xa, co in zip((0, .8, 1.6), (a, b, c)):
            if co == 0: ax.add_patch(Circle((xa, y), .07, color=ABU)); continue
            r = .16 + .1 * abs(co) / 1.41
            ax.add_patch(Circle((xa, y), r, fc=JG if co > 0 else MUDA, ec=TUA, lw=.7))
        for xa, l in zip((0, .8, 1.6), lab): ax.text(xa, -2.45, l, ha='center', fontsize=9, color=TUA)
    ax.set_title(judul, fontsize=9.5, color=TUA); ax.set_xlim(-.5, 5.3); ax.set_ylim(-2.7, 2.3); ax.set_aspect('equal'); ax.axis('off')
tiga(axs[0], '3c-2e: B–H–B pada diborana', 2, ('B', 'H', 'B'))
tiga(axs[1], '3c-4e: F–Xe–F pada XeF$_2$', 4, ('F', 'Xe', 'F'))
simpan(f, 'c_tigapusat')

# 9. Diagram Walsh H2O dari perhitungan
W = {int(k): v for k, v in J['walsh'].items()}; th = sorted(W)
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.6), gridspec_kw={'width_ratios': [1.5, 1]}); f.subplots_adjust(wspace=.45)
lab = ['2a$_1$', '1b$_1$ (bidang)', '3a$_1$', r'1b$_2$ ($\perp$ bidang)', '4a$_1$ (kosong)']
cl = [ABU, BIRU, JGT, HIJ, ABU]
for i in range(1, 5):
    y = [W[t]['orb'][i] for t in th]; a1.plot(th, y, color=cl[i], lw=2, ls='--' if i == 4 else '-')
    a1.text(181, y[-1] + (.9 if i == 3 else (-.7 if i == 2 else 0)), lab[i], fontsize=8.3, color=cl[i], va='center')
a1.axvline(104.5, color=ABU, lw=.8, ls=':'); a1.text(105.5, 1, '104,5°', fontsize=8, color=ABU)
a1.set_xlabel('sudut H–O–H (°)'); a1.set_ylabel('energi orbital (eV)'); a1.set_xlim(88, 205); koma(a1)
a2.plot(th, [W[t]['Erel_kJ'] for t in th], color=TUA, lw=2); a2.set_xlabel('sudut H–O–H (°)'); a2.set_ylabel('energi total relatif (kJ mol$^{-1}$)'); koma(a2)
simpan(f, 'c_walsh')

# 10. CO ke logam: donasi σ dan donasi balik π
f, axs = plt.subplots(1, 2, figsize=(7.4, 2.4))
for ax, judul in zip(axs, ['donasi σ: 5σ CO → d logam kosong', 'donasi balik π: d logam terisi → 2π* CO']):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-2.4, 3.4); ax.set_ylim(-1.3, 1.3); ax.set_title(judul, fontsize=9.3, color=TUA)
    ax.add_patch(Circle((-1.6, 0), .18, color='#b0b8c0', ec=TUA)); ax.text(-1.6, -.42, 'M', ha='center', fontsize=9)
    ax.add_patch(Circle((.4, 0), .14, color='#4a4f57')); ax.add_patch(Circle((1.5, 0), .14, color='#d2553b'))
    ax.text(.4, -.42, 'C', ha='center', fontsize=9); ax.text(1.5, -.42, 'O', ha='center', fontsize=9)
axs[0].add_patch(Ellipse((-.15, 0), .9, .55, fc=JG, ec=TUA, alpha=.85)); axs[0].add_patch(Ellipse((-1.1, 0), .55, .5, fc=MUDA, ec=TUA, alpha=.6))
axs[0].annotate('', (-1.0, .45), (-.2, .45), arrowprops=dict(arrowstyle='-|>', color=JGT))
for s in (1, -1):
    axs[1].add_patch(Ellipse((-1.2, s * .45), .45, .6, angle=45 * s, fc=JG if s > 0 else MUDA, ec=TUA, alpha=.85))
    axs[1].add_patch(Ellipse((-2.0, s * .45), .45, .6, angle=-45 * s, fc=MUDA if s > 0 else JG, ec=TUA, alpha=.85))
    axs[1].add_patch(Ellipse((.4, s * .45), .38, .62, fc=MUDA if s > 0 else JG, ec=TUA, alpha=.85))
    axs[1].add_patch(Ellipse((1.5, s * .38), .3, .5, fc=JG if s > 0 else MUDA, ec=TUA, alpha=.85))
axs[1].annotate('', (.1, .8), (-.9, .8), arrowprops=dict(arrowstyle='-|>', color=JGT))
simpan(f, 'c_karbonil')
