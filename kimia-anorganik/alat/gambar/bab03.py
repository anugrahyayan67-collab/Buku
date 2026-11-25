#!/usr/bin/env python3
# Gambar Bab 3 Kimia Anorganik 1: simetri molekul dan teori grup. -> bab03/fig/*.png
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon, Circle
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab03', 'fig'); os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
TH, PH = np.deg2rad(30), np.deg2rad(20)
def P(v):
    x, y, z = v
    return (x * np.cos(TH) - y * np.sin(TH), (x * np.sin(TH) + y * np.cos(TH)) * np.sin(PH) + z * np.cos(PH),
            (x * np.sin(TH) + y * np.cos(TH)) * np.cos(PH) - z * np.sin(PH))
WARNA = {'O': '#d2553b', 'H': '#f4f6f4', 'N': '#3b6fb6', 'B': '#f0a8a0', 'F': '#9fd8a8', 'C': '#4a4f57', 'S': '#e9c94a', 'Xe': '#7fc0f0',
         'Cl': '#5cbf5c', 'P': '#f0a060', 'Pt': '#b0b8c0'}
JARI = {'H': .16, 'F': .2, 'Cl': .23}
def molekul(ax, atom, ikatan, cx=0, cy=0, s=1.0, label=True):
    Q = {k: P(v) for k, (e, v) in atom.items()}
    for a, b in ikatan:
        (x1, y1, d1), (x2, y2, d2) = Q[a], Q[b]
        ax.plot([cx + s * x1, cx + s * x2], [cy + s * y1, cy + s * y2], color=ABU, lw=3.2 * s, zorder=1 - (d1 + d2) / 20, solid_capstyle='round')
    for k, (e, v) in sorted(atom.items(), key=lambda t: -Q[t[0]][2]):
        x, y, d = Q[k]; r = JARI.get(e, .26) * s
        ax.add_patch(Circle((cx + s * x, cy + s * y), r, fc=WARNA[e], ec=TUA, lw=.9, zorder=2 - d / 10))
        if label: ax.text(cx + s * x, cy + s * y, e, ha='center', va='center', fontsize=7.5 * s, color=TUA if e not in ('C', 'N') else 'white', zorder=3 - d / 10, fontweight='bold')
    return Q
def sumbu(ax, p1, p2, cx, cy, s, teks, c=JGT):
    (x1, y1, _), (x2, y2, _) = P(p1), P(p2)
    ax.plot([cx + s * x1, cx + s * x2], [cy + s * y1, cy + s * y2], color=c, lw=1.4, ls='--', zorder=0.5)
    ax.text(cx + s * x2, cy + s * y2 + .08, teks, ha='center', va='bottom', fontsize=9, color=c, fontweight='bold')
def bidang(ax, sudut, cx, cy, s, c, al=.18):
    ax.add_patch(Polygon([(cx + s * P(v)[0], cy + s * P(v)[1]) for v in sudut], closed=True, fc=c, ec=c, alpha=al, lw=.8, zorder=0.3))

# 1. Unsur simetri pada H2O, NH3, BF3
f, ax = plt.subplots(figsize=(7.6, 3.0)); ax.axis('off'); ax.set_aspect('equal')
a = np.radians(104.5 / 2)
H2O = {'O': ('O', (0, 0, .25)), 'H1': ('H', (-np.sin(a), 0, .25 - np.cos(a))), 'H2': ('H', (np.sin(a), 0, .25 - np.cos(a)))}
bidang(ax, [(-1.1, 0, -1.0), (1.1, 0, -1.0), (1.1, 0, 1.1), (-1.1, 0, 1.1)], 0, 0, 1, BIRU)
bidang(ax, [(0, -.9, -1.0), (0, .9, -1.0), (0, .9, 1.1), (0, -.9, 1.1)], 0, 0, 1, HIJ)
molekul(ax, H2O, [('O', 'H1'), ('O', 'H2')]); sumbu(ax, (0, 0, -1.25), (0, 0, 1.35), 0, 0, 1, 'C₂')
ax.text(0, -1.75, 'H₂O: E, C$_2$, σ$_v$, σ$_v$′\n(C$_{2v}$)', ha='center', va='top', fontsize=9, color=TUA)
NH3 = {'N': ('N', (0, 0, .35))}
for k in range(3):
    t = np.radians(90 + 120 * k); NH3[f'H{k}'] = ('H', (.94 * np.cos(t), .94 * np.sin(t), -.05))
bidang(ax, [(0, 0, -1.0), (1.1 * np.cos(np.radians(90)), 1.1 * np.sin(np.radians(90)), -1.0), (1.1 * np.cos(np.radians(90)), 1.1 * np.sin(np.radians(90)), 1.1), (0, 0, 1.1)], 3.1, 0, 1, BIRU, .14)
molekul(ax, NH3, [('N', 'H0'), ('N', 'H1'), ('N', 'H2')], cx=3.1); sumbu(ax, (0, 0, -1.0), (0, 0, 1.35), 3.1, 0, 1, 'C₃')
ax.text(3.1, -1.75, 'NH₃: E, 2C$_3$, 3σ$_v$\n(C$_{3v}$)', ha='center', va='top', fontsize=9, color=TUA)
BF3 = {'B': ('B', (0, 0, 0))}
for k in range(3):
    t = np.radians(120 * k); BF3[f'F{k}'] = ('F', (1.0 * np.cos(t), 1.0 * np.sin(t), 0))
bidang(ax, [(1.4 * np.cos(np.radians(t)), 1.4 * np.sin(np.radians(t)), 0) for t in (0, 90, 180, 270)], 6.4, 0, 1, JG, .2)
molekul(ax, BF3, [('B', 'F0'), ('B', 'F1'), ('B', 'F2')], cx=6.4); sumbu(ax, (0, 0, -1.0), (0, 0, 1.2), 6.4, 0, 1, 'C₃')
sumbu(ax, (-1.35, 0, 0), (1.45, 0, 0), 6.4, 0, 1, 'C₂', HIJ)
ax.text(6.4, -1.75, 'BF₃: E, 2C$_3$, 3C$_2$, σ$_h$, 2S$_3$, 3σ$_v$\n(D$_{3h}$)', ha='center', va='top', fontsize=9, color=TUA)
ax.set_xlim(-1.6, 8.0); ax.set_ylim(-2.4, 1.7)
simpan(f, 'a_unsur')

# 2. Operasi S4 pada CH4: putar 90° lalu cerminkan pada bidang tegak lurus sumbu
f, axs = plt.subplots(1, 3, figsize=(7.4, 2.6))
t = np.array([(1, 1, 1), (-1, -1, 1), (1, -1, -1), (-1, 1, -1)], float) * .62
def ch4(ax, pos, judul):
    ax.axis('off'); ax.set_aspect('equal')
    at = {'C': ('C', (0, 0, 0))}; ik = []
    for i, v in enumerate(pos): at[f'H{i}'] = ('H', tuple(v)); ik.append(('C', f'H{i}'))
    Q = molekul(ax, at, ik, s=1.1, label=False)
    for i in range(4):
        x, y, _ = Q[f'H{i}']; ax.text(1.1 * x + .18, 1.1 * y + .1, str(i + 1), fontsize=9, color=JGT, fontweight='bold')
    sumbu(ax, (0, 0, -1.2), (0, 0, 1.25), 0, 0, 1.1, 'S₄')
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.6, 1.7); ax.set_title(judul, fontsize=9.5, color=TUA)
R4 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); S = np.diag([1, 1, -1])
ch4(axs[0], t, 'awal'); ch4(axs[1], t @ R4.T, 'putar 90° (C$_4$)'); ch4(axs[2], t @ R4.T @ S.T, 'lalu cerminkan (σ$_h$): sama!')
simpan(f, 'a_s4')

# 3. Diagram alir penentuan grup titik
f, ax = plt.subplots(figsize=(7.4, 6.6)); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 10.6)
def kotak(x, y, t, c='#edf5fc', ec=BIRU, w=2.8, h=.62):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.04,rounding_size=0.12', fc=c, ec=ec, lw=1.1))
    ax.text(x, y, t, ha='center', va='center', fontsize=8.6, color=TUA)
def hasil(x, y, t): kotak(x, y, t, '#fdf3e8', JGT, w=1.45, h=.52)
def panah(x1, y1, x2, y2, t=''):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=10, color=TUA, lw=1))
    if t: ax.text((x1 + x2) / 2 + .08, (y1 + y2) / 2 + .05, t, fontsize=8, color=JGT, fontweight='bold')
kotak(5, 10.1, 'Molekul linear?', w=2.6)
panah(6.3, 10.1, 7.7, 10.1, 'ya'); kotak(8.6, 10.1, 'ada i?', w=1.6)
panah(8.6, 9.8, 8.0, 9.15, 'ya'); hasil(7.8, 8.9, 'D$_{\\infty h}$'); panah(8.8, 9.8, 9.3, 9.15, 'tidak'); hasil(9.3, 8.9, 'C$_{\\infty v}$')
panah(5, 9.8, 5, 9.2, 'tidak'); kotak(5, 8.9, 'Simetri tinggi? (T, O, I)', w=3.4)
panah(6.7, 8.9, 8.0, 8.05, 'ya'); hasil(8.6, 7.75, 'T$_d$, O$_h$, I$_h$')
panah(5, 8.6, 5, 7.95, 'tidak'); kotak(5, 7.65, 'Cari sumbu C$_n$ dengan n terbesar', w=3.8)
panah(3.1, 7.65, 1.25, 7.27); kotak(1.2, 7.0, 'tidak ada C$_n$', '#f4f6f4', ABU, w=1.7, h=.5)
panah(1.2, 6.75, 1.2, 6.25); kotak(1.2, 6.0, 'ada σ? → C$_s$\nada i? → C$_i$\nlain → C$_1$', '#fdf3e8', JGT, w=1.8, h=.95)
panah(5, 7.35, 5, 6.7); kotak(5, 6.4, 'Ada n sumbu C$_2$ $\\perp$ C$_n$?', w=3.2)
panah(6.6, 6.4, 7.6, 6.4, 'ya'); kotak(8.4, 6.4, 'cabang D', '#e8f6f0', HIJ, w=1.5)
panah(8.4, 6.1, 8.4, 5.55); kotak(8.4, 5.25, 'σ$_h$? → D$_{nh}$\nnσ$_d$? → D$_{nd}$\nlain → D$_n$', '#fdf3e8', JGT, w=1.8, h=.95)
panah(5, 6.1, 5, 5.45, 'tidak'); kotak(5, 5.15, 'cabang C', '#e8f6f0', HIJ, w=1.5)
panah(5, 4.85, 5, 4.25); kotak(5, 3.85, 'σ$_h$? → C$_{nh}$\nnσ$_v$? → C$_{nv}$\nS$_{2n}$ saja? → S$_{2n}$\nlain → C$_n$', '#fdf3e8', JGT, w=2.4, h=1.25)
ax.text(5, 2.6, 'Contoh: H₂O C$_{2v}$ · NH₃ C$_{3v}$ · BF₃ D$_{3h}$ · XeF₄ D$_{4h}$ · CH₄ T$_d$ · SF₆ O$_h$ · CHFClBr C$_1$', ha='center', fontsize=8.6, color=TUA)
simpan(f, 'b_alir')

# 4. Mode getaran H2O dan CO2
f, axs = plt.subplots(1, 2, figsize=(7.6, 2.9), gridspec_kw={'width_ratios': [1.15, 1]})
ax = axs[0]; ax.axis('off'); ax.set_aspect('equal')
mode = [('regangan simetris\na$_1$, 3657 cm$^{-1}$', [(-.35, -.25), (.35, -.25)], (0, .2)),
        ('tekukan\na$_1$, 1595 cm$^{-1}$', [(.32, .12), (-.32, .12)], (0, -.12)),
        ('regangan asimetris\nb$_1$, 3756 cm$^{-1}$', [(.33, -.24), (.33, .24)], (-.12, 0))]
for k, (lab, vh, vo) in enumerate(mode):
    cx = 2.2 * k; O = (cx, .25); Hs = [(cx - .75, -.35), (cx + .75, -.35)]
    for hx, hy in Hs: ax.plot([O[0], hx], [O[1], hy], color=ABU, lw=3)
    ax.add_patch(Circle(O, .27, fc=WARNA['O'], ec=TUA)); [ax.add_patch(Circle(h, .17, fc=WARNA['H'], ec=TUA)) for h in Hs]
    for (hx, hy), (dx, dy) in zip(Hs, vh): ax.add_patch(FancyArrowPatch((hx, hy), (hx + dx, hy + dy), arrowstyle='-|>', mutation_scale=9, color=BIRU, lw=1.5))
    ax.add_patch(FancyArrowPatch(O, (O[0] + vo[0], O[1] + vo[1]), arrowstyle='-|>', mutation_scale=8, color=BIRU, lw=1.2))
    ax.text(cx, -.85, lab, ha='center', va='top', fontsize=8.3, color=TUA)
ax.set_xlim(-1.1, 5.5); ax.set_ylim(-1.8, .9); ax.set_title('H₂O: 3 mode, semua aktif IR dan Raman', fontsize=9.5, color=TUA)
ax = axs[1]; ax.axis('off'); ax.set_aspect('equal')
m2 = [('regangan simetris σ$_g^+$\n1333 cm$^{-1}$, Raman', [(-.3, 0), (0, 0), (.3, 0)]), ('regangan asimetris σ$_u^+$\n2349 cm$^{-1}$, IR', [(.25, 0), (-.25, 0), (.25, 0)]),
      ('tekukan π$_u$ (dua)\n667 cm$^{-1}$, IR', [(0, -.25), (0, .3), (0, -.25)])]
for k, (lab, vs) in enumerate(m2):
    y = 1.1 - 1.15 * k; xs = [-1.0, 0, 1.0]
    ax.plot([-1, 1], [y, y], color=ABU, lw=3)
    for x, e, (dx, dy) in zip(xs, ['O', 'C', 'O'], vs):
        ax.add_patch(Circle((x, y), .22, fc=WARNA[e], ec=TUA))
        if dx or dy: ax.add_patch(FancyArrowPatch((x, y), (x + dx * 1.4, y + dy * 1.4), arrowstyle='-|>', mutation_scale=9, color=BIRU, lw=1.8, zorder=6))
    ax.text(1.45, y, lab, ha='left', va='center', fontsize=8.2, color=TUA)
ax.set_xlim(-1.4, 3.6); ax.set_ylim(-1.6, 1.6); ax.set_title('CO₂: larangan bersama', fontsize=9.5, color=TUA)
simpan(f, 'c_getaran')

# 5. SALC orbital 1s H pada H2O dan NH3
f, axs = plt.subplots(1, 4, figsize=(7.6, 2.3))
def bulat(ax, x, y, tanda, r=.33):
    ax.add_patch(Circle((x, y), r, fc=JG if tanda > 0 else MUDA, ec=TUA, lw=.8, alpha=.9))
    ax.text(x, y, '+' if tanda > 0 else '−', ha='center', va='center', fontsize=11, fontweight='bold', color=TUA)
for ax, (judul, tanda) in zip(axs[:2], [('H₂O: a₁\n(1s₁ + 1s₂)', (1, 1)), ('H₂O: b₁\n(1s₁ − 1s₂)', (1, -1))]):
    ax.axis('off'); ax.set_aspect('equal'); ax.add_patch(Circle((0, .3), .16, fc=WARNA['O'], ec=TUA))
    for x, t2 in zip((-.75, .75), tanda): ax.plot([0, x], [.3, -.3], color=ABU, lw=1.5, zorder=0); bulat(ax, x, -.3, t2)
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1, .9); ax.set_title(judul, fontsize=9, color=TUA)
pos = [(np.cos(np.radians(90 + 120 * k)), np.sin(np.radians(90 + 120 * k))) for k in range(3)]
for ax, (judul, tanda) in zip(axs[2:], [('NH₃: a₁\n(1s₁ + 1s₂ + 1s₃)', (1, 1, 1)), ('NH₃: salah satu e\n(2·1s₁ − 1s₂ − 1s₃)', (1, -1, -1))]):
    ax.axis('off'); ax.set_aspect('equal'); ax.add_patch(Circle((0, 0), .15, fc=WARNA['N'], ec=TUA))
    for (x, y), t2 in zip(pos, tanda): ax.plot([0, .8 * x], [0, .8 * y], color=ABU, lw=1.5, zorder=0); bulat(ax, .8 * x, .8 * y, t2, .27 * (1.3 if (t2 > 0 and tanda == (1, -1, -1)) else 1))
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.1, 1.2); ax.set_title(judul, fontsize=9, color=TUA)
simpan(f, 'c_salc')
