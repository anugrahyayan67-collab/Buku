#!/usr/bin/env python3
# Gambar Bab 9 Kimia Anorganik 1: oksidasi dan reduksi. -> bab09/fig/*.png
import os, json, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'bab09'); D = f'{R}/fig'; os.makedirs(D, exist_ok=True)
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
TUA, BIRU, MUDA, JG, JGT, HIJ, ABU = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a', '#8a9aa8'
def simpan(f, nama): f.savefig(f'{D}/{nama}.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok', nama)
from matplotlib.ticker import FuncFormatter
def koma(ax, sb='xy'):
    fm = FuncFormatter(lambda v, p: f'{v:g}'.replace('.', ',').replace('-', '−'))
    if 'x' in sb: ax.xaxis.set_major_formatter(fm)
    if 'y' in sb: ax.yaxis.set_major_formatter(fm)
k = 0.05916
# 1. sel Daniell
f, ax = plt.subplots(figsize=(6.4, 3.4)); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(-.9, 6)
for x0, nm, larutan, c in [(.6, 'Zn', 'ZnSO₄(aq)', MUDA), (6.2, 'Cu', 'CuSO₄(aq)', '#9ec9ef')]:
    ax.add_patch(Rectangle((x0, .5), 3.2, 2.6, fc=c, ec=TUA, alpha=.5)); ax.plot([x0, x0, x0 + 3.2, x0 + 3.2], [3.6, .5, .5, 3.6], color=TUA, lw=1.5)
    ax.add_patch(Rectangle((x0 + 1.3, 1.1), .6, 3.2, fc='#b0b8c0' if nm == 'Zn' else '#c87533', ec=TUA)); ax.text(x0 + 1.6, 4.5, nm, ha='center', fontsize=11, fontweight='bold')
    ax.text(x0 + 1.6, .75, larutan, ha='center', fontsize=8.5)
ax.plot([3.4, 3.4, 6.8, 6.8], [2.5, 3.4, 3.4, 2.5], color=ABU, lw=8, solid_capstyle='butt'); ax.text(5.1, 3.7, 'jembatan garam (KNO₃)', ha='center', fontsize=8.5)
ax.plot([2.2, 2.2, 7.8, 7.8], [4.3, 5.4, 5.4, 4.3], color=TUA, lw=1.4); ax.add_patch(Rectangle((4.4, 5.05), 1.4, .7, fc='white', ec=TUA)); ax.text(5.1, 5.4, 'V = 1,10 V', ha='center', va='center', fontsize=9)
ax.annotate('', (4.0, 5.6), (2.8, 5.6), arrowprops=dict(arrowstyle='-|>', color=JGT)); ax.text(3.4, 5.75, 'e$^-$', color=JGT, fontsize=9, ha='center')
ax.text(2.2, -.3, 'anode (−)\nZn → Zn$^{2+}$ + 2e$^-$', ha='center', fontsize=8, color=TUA); ax.text(7.8, -.3, 'katode (+)\nCu$^{2+}$ + 2e$^-$ → Cu', ha='center', fontsize=8, color=TUA)
simpan(f, 'a_sel')
# 2. jendela kestabilan air
pH = np.linspace(0, 14, 50)
f, ax = plt.subplots(figsize=(6.2, 4.0))
ax.fill_between(pH, -k * pH, 1.229 - k * pH, color=MUDA, alpha=.35); ax.plot(pH, 1.229 - k * pH, color=BIRU, lw=2); ax.plot(pH, -k * pH, color=BIRU, lw=2)
ax.text(10, 0.95, 'O$_2$ / H$_2$O', color=BIRU, fontsize=9); ax.text(10, -.45, 'H$^+$ / H$_2$', color=BIRU, fontsize=9); ax.text(3, .45, 'air stabil', color=BIRU, fontsize=10)
for nm, e_, c in [('F$_2$/F$^-$ 2,87', 2.87, JGT), ('MnO$_4^-$/Mn$^{2+}$ (pH 0) 1,51', 1.51, JGT), ('Fe$^{3+}$/Fe$^{2+}$ 0,77', .771, HIJ), ('Zn$^{2+}$/Zn −0,76', -.762, HIJ), ('Na$^+$/Na −2,71', -2.71, JGT)]:
    ax.axhline(e_, color=c, ls='--', lw=1); ax.text(.2, e_ + .06, nm, fontsize=8, color=c)
ax.set_xlabel('pH'); ax.set_ylabel('$E$ (V terhadap SHE)'); ax.set_ylim(-3, 3.1); ax.set_xlim(0, 14); koma(ax)
simpan(f, 'a_air')
# 3. Frost Mn
nA = {0: 0, 2: -2.36, 3: -0.85, 4: 0.10, 6: 4.62, 7: 5.18}; nB = {0: 0, 2: -3.12, 3: -3.02, 4: -3.22, 6: -2.02, 7: -1.46}
labA = {0: 'Mn', 2: 'Mn$^{2+}$', 3: 'Mn$^{3+}$', 4: 'MnO$_2$', 6: 'MnO$_4^{2-}$', 7: 'MnO$_4^-$'}
labB = {0: 'Mn', 2: 'Mn(OH)$_2$', 3: 'Mn$_2$O$_3$', 4: 'MnO$_2$', 6: 'MnO$_4^{2-}$', 7: 'MnO$_4^-$'}
f, ax = plt.subplots(figsize=(6.0, 4.0))
for d, lab, c, nm in [(nA, labA, JGT, 'pH 0'), (nB, labB, BIRU, 'pH 14')]:
    xs = sorted(d); ax.plot(xs, [d[x] for x in xs], 'o-', color=c, label=nm)
    for x in xs: ax.text(x + .1, d[x] + (.25 if c == JGT else -.45), lab[x], fontsize=8, color=c)
ax.set_xlabel('bilangan oksidasi'); ax.set_ylabel('$NE$° (V)'); ax.legend(fontsize=9, loc='upper left'); koma(ax); ax.set_xlim(-.3, 8)
simpan(f, 'b_frost')
# 4. Pourbaix Fe
P = json.load(open(f'{R}/_pourbaix.json')); c = 1e-6
f, ax = plt.subplots(figsize=(6.2, 4.4)); x = np.linspace(0, 14, 400)
ax.plot(x, 1.229 - k * x, color=BIRU, ls='--', lw=1); ax.plot(x, -k * x, color=BIRU, ls='--', lw=1)
pH3, pH2 = P['pH3'], P['pH2']; Efe = -0.447 + k / 2 * np.log10(c)
# batas
ax.plot([0, pH3], [.771, .771], color=TUA, lw=2)                                # Fe3+/Fe2+
ax.plot([pH3, pH3], [.771, 1.6], color=TUA, lw=2)                               # Fe3+/Fe(OH)3
xa = np.linspace(pH3, pH2, 50); ax.plot(xa, P['E0a'] - 3 * k * xa - k * np.log10(c), color=TUA, lw=2)   # Fe(OH)3/Fe2+
Eb = P['E0a'] - 3 * k * pH2 - k * np.log10(c); xb = np.linspace(pH2, 14, 50); ax.plot(xb, Eb - k * (xb - pH2), color=TUA, lw=2)  # Fe(OH)3/Fe(OH)2
ax.plot([0, pH2], [Efe, Efe], color=TUA, lw=2)                                    # Fe2+/Fe
ax.plot([pH2, pH2], [Efe, Eb], color=TUA, lw=2)                                   # Fe2+/Fe(OH)2
xc = np.linspace(pH2, 14, 50); ax.plot(xc, Efe - k * (xc - pH2), color=TUA, lw=2)  # Fe(OH)2/Fe
for t, (xx, yy) in {'Fe$^{3+}$': (.8, 1.2), 'Fe$^{2+}$': (3.5, .1), 'Fe(OH)$_3$ (karat)': (8.3, 1.0), 'Fe(OH)$_2$': (10.8, -.55), 'Fe (logam)': (5, -1.1)}.items(): ax.text(xx, yy, t, fontsize=10, color=TUA)
ax.text(11.3, .3, 'O$_2$/H$_2$O', color=BIRU, fontsize=8); ax.text(.3, -.2, 'H$^+$/H$_2$', color=BIRU, fontsize=8)
ax.set_xlim(0, 14); ax.set_ylim(-1.4, 1.6); ax.set_xlabel('pH'); ax.set_ylabel('$E$ (V)'); koma(ax)
simpan(f, 'b_pourbaix')
# 5. Ellingham
ell = json.load(open(f'{R}/_ellingham.json')); T = np.linspace(300, 2300, 50)
f, ax = plt.subplots(figsize=(6.6, 4.4))
warna = {'4Ag+O2→2Ag2O': ABU, '4Cu+O2→2Cu2O': JG, '2Fe+O2→2FeO': JGT, '2Zn+O2→2ZnO': '#7a7a7a', '4/3Al+O2→2/3Al2O3': HIJ, '2Mg+O2→2MgO': BIRU, '2C+O2→2CO': TUA, 'C+O2→CO2': TUA, '2CO+O2→2CO2': TUA}
import re
for nm, (h, s) in ell.items():
    y = h - T * s / 1000; ls = '-' if 'C' not in nm.split('+')[0] or nm.startswith('4Cu') else '--'
    if nm.startswith(('2C+', 'C+', '2CO')): ls = '--'
    ax.plot(T, y, color=warna[nm], ls=ls, lw=1.8); lab = re.sub(r'(\d)(?=[A-Za-z(])', '', nm) if False else nm
    dy = {'2Fe+O2→2FeO': 18, '2Zn+O2→2ZnO': -18, '2C+O2→2CO': 22, '4/3Al+O2→2/3Al2O3': -18}.get(nm, 0)
    ax.text(2310, y[-1] + dy, re.sub(r'([A-Za-z\)])(\d+)', r'\1$_{\2}$', nm), fontsize=7, va='center', color=warna[nm])
ax.axhline(0, color=ABU, lw=.6); ax.set_xlabel('suhu (K)'); ax.set_ylabel('Δ$G$° (kJ per mol O$_2$)'); ax.set_xlim(300, 2900); koma(ax)
simpan(f, 'c_ellingham')
# 6. tangga potensial biologis (pH 7)
bio = [('NAD$^+$/NADH', -.32), ('FAD/FADH$_2$', -.22), ('ubikuinon/ubikuinol', .045), ('sitokrom c (Fe$^{3+}$/Fe$^{2+}$)', .254), ('O$_2$/H$_2$O', .816)]
f, ax = plt.subplots(figsize=(5.6, 3.2))
for i, (nm, e_) in enumerate(bio):
    ax.plot([0, 1], [e_, e_], color=TUA, lw=2); ax.text(1.05, e_, nm, va='center', fontsize=9)
    if i < len(bio) - 1: ax.annotate('', (.5, bio[i + 1][1] - .02), (.5, e_ + .02), arrowprops=dict(arrowstyle='-|>', color=JGT))
ax.set_xlim(-.2, 3.2); ax.set_xticks([]); ax.set_ylabel("$E$°' (V, pH 7)"); koma(ax, 'y'); ax.set_ylim(-.45, .95)
for s_ in ('top', 'right', 'bottom'): ax.spines[s_].set_visible(False)
ax.text(1.7, -.38, 'elektron mengalir ke $E$° yang lebih positif:\nΔ$G$ total ≈ −219 kJ per NADH', fontsize=8.5, color=JGT)
simpan(f, 'c_bio')
