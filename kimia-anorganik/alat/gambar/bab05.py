#!/usr/bin/env python3
# Gambar Bab 5 Kimia Anorganik 1: padatan ionik dan struktur kristal. -> bab05/fig/*.png
import os, itertools, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyArrowPatch
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab05', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
def koma(ax):
    from matplotlib.ticker import FuncFormatter
    for a in (ax.xaxis, ax.yaxis): a.set_major_formatter(FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−')))
TH, PH = np.deg2rad(24), np.deg2rad(16)
def P(v):
    x, y, z = v
    return (x * np.cos(TH) - y * np.sin(TH), (x * np.sin(TH) + y * np.cos(TH)) * np.sin(PH) + z * np.cos(PH), (x * np.sin(TH) + y * np.cos(TH)) * np.cos(PH) - z * np.sin(PH))
def kubus(ax, s=1, c=ABU, lw=1, sel=((0, 0, 0), (1, 1, 1))):
    (x0, y0, z0), (x1, y1, z1) = sel
    V = [(x, y, z) for x in (x0, x1) for y in (y0, y1) for z in (z0, z1)]
    for a, b in itertools.combinations(V, 2):
        if sum(u != w for u, w in zip(a, b)) == 1:
            pa, pb = P(np.array(a) * s), P(np.array(b) * s); ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color=c, lw=lw, zorder=1)
def bola(ax, atom, s=1, ikat=(), dmax=None):
    """atom: list (x,y,z, warna, jari)"""
    pts = [(P(np.array(p[:3]) * s), p) for p in atom]
    if dmax:
        for (pa, a), (pb, b) in itertools.combinations(pts, 2):
            d = np.linalg.norm(np.array(a[:3]) - np.array(b[:3]))
            if d < dmax and a[3] != b[3]: ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color='#b8c2cc', lw=1.6, zorder=2)
    for (X, Y, dd), p in sorted(pts, key=lambda t: -t[0][2]):
        ax.add_patch(Circle((X, Y), p[4], fc=p[3], ec=TUA, lw=.7, zorder=3 - dd / 10))
        ax.add_patch(Circle((X - .3 * p[4], Y + .3 * p[4]), .3 * p[4], fc='white', ec='none', alpha=.35, zorder=3.01 - dd / 10))
def siap(ax, judul):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(judul, fontsize=9.5, color=TUA); ax.autoscale_view()
def dalam(p, e=1e-6): return all(-e <= u <= 1 + e for u in p)

# 1. Kemasan rapat: lapisan A, B, C dari atas
f, axs = plt.subplots(1, 2, figsize=(7.4, 3.4))
r = .5; vb = np.array([1, 0]); vc = np.array([.5, np.sqrt(3) / 2])
def lapis(ax, off, c, al, z):
    for i in range(-1, 6):
        for j in range(-1, 5):
            p = i * vb + j * vc + off
            if 0 < p[0] < 4.6 and 0 < p[1] < 3.6: ax.add_patch(Circle(p, r * .97, fc=c, ec=TUA, lw=.6, alpha=al, zorder=z))
A = np.array([.3, .3]); B = A + (vb + vc) / 3; C = A + 2 * (vb + vc) / 3
lapis(axs[0], A, MUDA, 1, 1); lapis(axs[0], B, JG, .7, 2)
lapis(axs[1], A, MUDA, 1, 1); lapis(axs[1], B, JG, .7, 2)
for k in range(5):
    for j in range(4):
        p = C + k * vb + j * vc
        if 0 < p[0] < 4.6 and 0 < p[1] < 3.6: axs[1].add_patch(Circle(p, .16, fc=HIJ, ec=TUA, lw=.6, zorder=3))
        q = A + k * vb + j * vc
        if 0 < q[0] < 4.6 and 0 < q[1] < 3.6: axs[0].add_patch(Circle(q, .16, fc=BIRU, ec=TUA, lw=.6, zorder=3))
axs[0].set_title('hcp: ABAB… (lapis ketiga tepat di atas A)', fontsize=9.3, color=TUA)
axs[1].set_title('ccp: ABCABC… (lapis ketiga di posisi C)', fontsize=9.3, color=TUA)
for ax in axs: ax.set_xlim(0, 4.6); ax.set_ylim(0, 3.6); ax.set_aspect('equal'); ax.axis('off')
simpan(f, 'a_kemas')

# 2. Rongga tetrahedral dan oktahedral + penampang rasio jari-jari
f, axs = plt.subplots(1, 3, figsize=(7.8, 2.8))
tet = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
bola(axs[0], [(*np.array(t) * .5, MUDA, .3) for t in tet] + [(0, 0, 0, JGT, .12)], dmax=1.0); siap(axs[0], 'rongga tetrahedral (KB 4)')
okt = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
bola(axs[1], [(*np.array(t) * .7, MUDA, .27) for t in okt] + [(0, 0, 0, JGT, .14)], dmax=.8); siap(axs[1], 'rongga oktahedral (KB 6)')
ax = axs[2]; R = 1; rr = np.sqrt(2) - 1
for x, y in [(1, 1), (-1, 1), (1, -1), (-1, -1)]: ax.add_patch(Circle((x, y), R, fc=MUDA, ec=TUA, lw=.8))
ax.add_patch(Circle((0, 0), rr, fc=JG, ec=TUA, lw=.8)); ax.plot([-1, 1], [-1, 1], color=TUA, lw=.8)
ax.text(0, -2.25, 'diagonal: $2r_- + 2r_+ = 2\\sqrt{2}\\,r_-$\n$r_+/r_- = \\sqrt{2} - 1 = 0{,}414$', ha='center', va='top', fontsize=8.6, color=TUA)
ax.set_xlim(-2.1, 2.1); ax.set_ylim(-3.4, 2.1); ax.set_aspect('equal'); ax.axis('off'); ax.set_title('penampang oktahedral', fontsize=9.5, color=TUA)
simpan(f, 'a_rongga')

# 3. Sel satuan kubus: sc, bcc, fcc dengan hitungan
f, axs = plt.subplots(1, 3, figsize=(7.8, 2.9))
sudut = [p for p in itertools.product((0, 1), repeat=3)]
muka = [(.5, .5, 0), (.5, .5, 1), (.5, 0, .5), (.5, 1, .5), (0, .5, .5), (1, .5, .5)]
for ax, (nm, isi, hit) in zip(axs, [('kubus sederhana', sudut, '8 × ⅛ = 1'), ('kubus pusat badan (bcc)', sudut + [(.5, .5, .5)], '8 × ⅛ + 1 = 2'),
                                    ('kubus pusat muka (fcc)', sudut + muka, '8 × ⅛ + 6 × ½ = 4')]):
    kubus(ax); bola(ax, [(*p, MUDA if p in sudut else JG, .1) for p in isi]); siap(ax, nm)
    ax.text(.5 * (P((0, 0, 0))[0] + P((1, 1, 0))[0]), P((0, 0, 0))[1] - .28, hit, ha='center', fontsize=9, color=JGT)
simpan(f, 'a_sel')

# 4. Struktur prototipe AX dan AX2
f, axs = plt.subplots(1, 4, figsize=(8.2, 2.6))
fcc = [p for p in sudut] + muka
na = [p for p in itertools.product((0, .5, 1), repeat=3) if sum(np.array(p) == .5) in (1, 3)]
bola(axs[0], [(*p, '#9fd8a8', .13) for p in fcc] + [(*p, '#b48ae0', .08) for p in na], dmax=.51); kubus(axs[0]); siap(axs[0], 'NaCl (KB 6:6)')
bola(axs[1], [(*p, '#9fd8a8', .13) for p in sudut] + [(.5, .5, .5, '#e9c94a', .15)], dmax=.9); kubus(axs[1]); siap(axs[1], 'CsCl (KB 8:8)')
tetr = [(.25, .25, .25), (.75, .75, .25), (.75, .25, .75), (.25, .75, .75)]
bola(axs[2], [(*p, '#e9c94a', .1) for p in fcc] + [(*p, '#5a6470', .085) for p in tetr], dmax=.44); kubus(axs[2]); siap(axs[2], 'sfalerit ZnS (KB 4:4)')
f8 = [p for p in itertools.product((.25, .75), repeat=3)]
bola(axs[3], [(*p, '#9fd8a8', .09) for p in fcc] + [(*p, '#f4f6f4', .12) for p in f8], dmax=.44)
for p in fcc: pass
kubus(axs[3]); siap(axs[3], 'fluorit CaF₂ (KB 8:4)')
simpan(f, 'b_ax')

# 5. Rutil dan perovskit
f, axs = plt.subplots(1, 2, figsize=(6.4, 3.0))
u = .305; c = 295.9 / 459.4
ti = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, c), (1, 0, c), (0, 1, c), (1, 1, c), (.5, .5, c / 2)]
o = [(u, u, 0), (1 - u, 1 - u, 0), (u, u, c), (1 - u, 1 - u, c), (.5 + u, .5 - u, c / 2), (.5 - u, .5 + u, c / 2)]
kubus(axs[0], sel=((0, 0, 0), (1, 1, c))); bola(axs[0], [(*p, '#b0b8c0', .1) for p in ti] + [(*p, '#d2553b', .085) for p in o], dmax=.46); siap(axs[0], 'rutil TiO₂ (KB 6:3)')
oo = [(.5, .5, 0), (.5, .5, 1), (.5, 0, .5), (.5, 1, .5), (0, .5, .5), (1, .5, .5)]
kubus(axs[1]); bola(axs[1], [(*p, '#7fc0f0', .14) for p in sudut] + [(*p, '#d2553b', .09) for p in oo] + [(.5, .5, .5, '#b0b8c0', .08)], dmax=.51)
siap(axs[1], 'perovskit SrTiO₃ (Ti KB 6, Sr KB 12)')
simpan(f, 'b_rutil')

# 6. Rasio jari-jari halida alkali vs struktur nyata
cat = {'Li': 76, 'Na': 102, 'K': 138, 'Rb': 152, 'Cs': 167}; an = {'F': 133, 'Cl': 181, 'Br': 196, 'I': 220}
f, ax = plt.subplots(figsize=(6.4, 3.1))
for i, cc in enumerate(cat):
    for j, a in enumerate(an):
        rr = min(cat[cc], an[a]) / max(cat[cc], an[a]); cs = cc == 'Cs' and a != 'F'
        ax.scatter(rr, i + (j - 1.5) * .12, s=40, marker='s' if cs else 'o', color=JGT if cs else BIRU, zorder=3)
        ax.text(rr, i + (j - 1.5) * .12 + .02, f' {cc}{a}', fontsize=6.5, va='center', color=TUA)
for x, l in [(.414, 'KB 6'), (.732, 'KB 8')]: ax.axvline(x, color=ABU, ls='--', lw=1); ax.text(x + .005, 4.55, l + ' →', fontsize=8.5, color=ABU)
ax.set_yticks(range(5), list(cat)); ax.set_xlabel('rasio jari-jari (ion kecil / ion besar)'); ax.set_xlim(.3, 1.02); ax.set_ylim(-.6, 4.9); koma(ax); ax.set_yticks(range(5)); ax.set_yticklabels(list(cat))
ax.scatter([], [], marker='o', color=BIRU, label='struktur NaCl (KB 6)'); ax.scatter([], [], marker='s', color=JGT, label='struktur CsCl (KB 8)'); ax.legend(fontsize=8, loc='lower right')
simpan(f, 'b_rasio')

# 7. Bragg + pola serbuk NaCl lawan KCl
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.8, 3.0), gridspec_kw={'width_ratios': [1, 1.4]})
for y in (0, -1, -2):
    a1.plot(np.arange(5) - .5, [y] * 5, 'o', color=BIRU, ms=6)
th = np.radians(25); L = 1.5
for x0, y0 in [(1.0, 0), (1.0 + np.tan(np.pi / 2 - th) * 0 + 1 / np.tan(th), -1)]:
    pass
xa = 1.6; xb = xa + 1 / np.tan(th)
a1.annotate('', (xa, 0), (xa - L * np.cos(th), L * np.sin(th)), arrowprops=dict(arrowstyle='-|>', color=JGT, lw=1.4))
a1.annotate('', (xa + L * np.cos(th), L * np.sin(th)), (xa, 0), arrowprops=dict(arrowstyle='-|>', color=JGT, lw=1.4))
xb = xa + np.cos(th) / np.sin(th) * 1 * 0 + 0
a1.annotate('', (xa, -1), (xa - (L + 1 / np.sin(th)) * np.cos(th), -1 + (L + 1 / np.sin(th)) * np.sin(th)), arrowprops=dict(arrowstyle='-|>', color=HIJ, lw=1.4))
a1.annotate('', (xa + (L + 1 / np.sin(th)) * np.cos(th), -1 + (L + 1 / np.sin(th)) * np.sin(th)), (xa, -1), arrowprops=dict(arrowstyle='-|>', color=HIJ, lw=1.4))
a1.annotate('', (xa + .15, -1), (xa + .15, 0), arrowprops=dict(arrowstyle='<->', color=TUA, lw=.8)); a1.text(xa + .22, -.55, '$d$', fontsize=10)
a1.text(xa - 1.0, .12, 'θ', fontsize=10, color=JGT); a1.text(.2, -2.8, '$n\\lambda = 2d\\,\\sin\\theta$', fontsize=11, color=TUA)
a1.set_xlim(-2.6, 5.4); a1.set_ylim(-3.1, 2.4); a1.set_aspect('equal'); a1.axis('off')
lam = 154.06; x = np.linspace(20, 70, 2000)
for a, fA, fB, nm, dy, c in [(564.0, 18, 10, 'NaCl', 1.15, BIRU), (629.2, 18, 18, 'KCl', 0, JGT)]:
    y = np.zeros_like(x)
    for hkl, m in [((1, 1, 1), 8), ((2, 0, 0), 6), ((2, 2, 0), 12), ((3, 1, 1), 24), ((2, 2, 2), 8), ((4, 0, 0), 6)]:
        h, k, l = hkl; d = a / np.sqrt(h * h + k * k + l * l); tt = 2 * np.degrees(np.arcsin(lam / 2 / d))
        F = fA + fB if h % 2 == 0 else fA - fB; t = np.radians(tt / 2); lp = (1 + np.cos(2 * t) ** 2) / (np.sin(t) ** 2 * np.cos(t))
        I = m * F * F * lp; y += I * np.exp(-((x - tt) / .12) ** 2)
        if I > 0 and tt < 69: a2.text(tt, dy + .02 + I / 2.2e5 * 1 if False else dy + .03 + min(1, I / 3.2e5), f'{h}{k}{l}', ha='center', fontsize=6.5, color=c)
    a2.plot(x, dy + np.minimum(y / 3.2e5, 1), color=c, lw=1.2); a2.text(21, dy + .5, nm, color=c, fontsize=10, fontweight='bold')
a2.set_xlabel('2θ (°), Cu Kα'); a2.set_yticks([]); a2.set_ylim(-.05, 2.4)
for s in ('top', 'right', 'left'): a2.spines[s].set_visible(False)
simpan(f, 'c_bragg')

# 8. Cacat Schottky dan Frenkel
f, axs = plt.subplots(1, 2, figsize=(7.2, 3.0))
for ax, judul in zip(axs, ['cacat Schottky (NaCl)', 'cacat Frenkel (AgCl)']):
    for i in range(6):
        for j in range(5):
            kat = (i + j) % 2 == 0
            if judul.startswith('cacat S') and ((i, j) in [(2, 1), (3, 3)]):
                ax.add_patch(Circle((i, j), .32 if not kat else .2, fc='none', ec=JGT, lw=1.2, ls='--')); continue
            if judul.startswith('cacat F') and (i, j) == (2, 2):
                ax.add_patch(Circle((i, j), .2, fc='none', ec=JGT, lw=1.2, ls='--')); continue
            ax.add_patch(Circle((i, j), .2 if kat else .32, fc=JG if kat else MUDA, ec=TUA, lw=.6))
    ax.set_xlim(-.6, 5.6); ax.set_ylim(-.6, 4.6); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(judul, fontsize=9.5, color=TUA)
axs[1].add_patch(Circle((2.5, 2.5), .15, fc=JG, ec=JGT, lw=1.4)); axs[1].annotate('', (2.43, 2.4), (2.12, 2.12), arrowprops=dict(arrowstyle='-|>', color=JGT, lw=1))
axs[0].text(2.5, -.55, 'pasangan kekosongan kation + anion', ha='center', fontsize=8.5, color=JGT)
axs[1].text(2.5, -.55, 'kation pindah ke celah antarkisi', ha='center', fontsize=8.5, color=JGT)
simpan(f, 'c_cacat')

# 9. Intan dan grafit
f, axs = plt.subplots(1, 2, figsize=(6.8, 3.2))
dia = fcc + tetr
kubus(axs[0]); bola(axs[0], [(*p, '#4a4f57', .07) for p in fcc] + [(*p, '#8a9aa8', .07) for p in tetr], dmax=.44)
for (pa) in tetr:
    for q in fcc:
        if np.linalg.norm(np.array(pa) - np.array(q)) < .44:
            A_, B_ = P(pa), P(q); axs[0].plot([A_[0], B_[0]], [A_[1], B_[1]], color='#b8c2cc', lw=1.6, zorder=2)
siap(axs[0], 'intan: setiap C tetrahedral, C–C 154 pm')
ax = axs[1]
def hexlap(z, dx, c):
    b = 1.0; a1 = np.array([np.sqrt(3) * b, 0]); a2 = np.array([np.sqrt(3) / 2 * b, 1.5 * b])
    tr = lambda q: (q[0] + .55 * q[1] + dx, .32 * q[1] + z)
    seen = set()
    for i in range(-1, 4):
        for j in range(0, 3):
            cc = i * a1 + j * a2
            V = [cc + b * np.array([np.cos(np.radians(30 + 60 * k)), np.sin(np.radians(30 + 60 * k))]) for k in range(6)]
            if not (0 <= cc[0] - (j * a2[0]) * 0 <= 5.5): continue
            for k in range(6):
                pa, pb = tr(V[k]), tr(V[(k + 1) % 6]); ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color=c, lw=1.3, zorder=1)
                key = (round(V[k][0], 2), round(V[k][1], 2))
                if key not in seen: seen.add(key); ax.add_patch(Circle(tr(V[k]), .09, fc=c, ec=TUA, lw=.4, zorder=2))
hexlap(0, 0, '#4a4f57'); hexlap(2.1, np.sqrt(3) / 2, '#8a9aa8'); hexlap(4.2, 0, '#4a4f57')
ax.annotate('', (9.0, 2.1), (9.0, 0), arrowprops=dict(arrowstyle='<->', color=JGT)); ax.text(9.1, 1, '335 pm', color=JGT, fontsize=8.5)
ax.set_xlim(-1.5, 10); ax.set_ylim(-1.2, 6.4); ax.set_aspect('equal'); ax.axis('off'); ax.set_title('grafit: lapisan heksagonal, C–C 142 pm', fontsize=9.5, color=TUA)
simpan(f, 'c_karbon')

# 10. Kristal lawan kaca (jaringan acak Zachariasen, 2D)
rng = np.random.default_rng(3)
f, axs = plt.subplots(1, 2, figsize=(7.2, 3.1))
for ax, acak, judul in zip(axs, (0, 1), ['kristal: cincin teratur', 'kaca: jaringan acak']):
    pts = {}
    for i in range(-1, 7):
        for j in range(-1, 6):
            for s in (0, 1):
                x = np.sqrt(3) * (i + j / 2) + s * np.sqrt(3) / 2 * 0; y = 1.5 * j + s
                pts[(i, j, s)] = np.array([x, y]) + (rng.normal(0, .11, 2) if acak else 0)
    keys = list(pts)
    E = []
    for a, b in itertools.combinations(keys, 2):
        (i, j, s), (k, l, t) = a, b
        if s == t: continue
        A_, B_ = (a, b) if s == 0 else (b, a)
        (i, j, _), (k, l, _) = A_, B_
        if (k, l) in [(i, j), (i, j - 1), (i + 1, j - 1)]: E.append((A_, B_))
    for a, b in E:
        pa, pb = pts[a], pts[b]
        if all(0 < q[0] < 8 and 0 < q[1] < 6 for q in (pa, pb)):
            ax.plot(*zip(pa, pb), color=ABU, lw=1.2, zorder=1); m = (pa + pb) / 2; ax.add_patch(Circle(m, .13, fc='#d2553b', ec=TUA, lw=.4, zorder=3))
    for q in pts.values():
        if 0 < q[0] < 8 and 0 < q[1] < 6: ax.add_patch(Circle(q, .17, fc=BIRU, ec=TUA, lw=.5, zorder=2))
    ax.set_xlim(.2, 7.8); ax.set_ylim(.2, 5.8); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(judul, fontsize=9.5, color=TUA)
simpan(f, 'c_kaca')
