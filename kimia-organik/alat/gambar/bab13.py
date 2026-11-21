# Gambar Bab 13: inversi nitrogen, pKaH, membuat amina, eliminasi Hofmann, diazonium, metil jingga,
# heterosiklik, amina dalam biologi
import os, io, numpy as np, matplotlib, matplotlib.ticker
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang, ukuran_px
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab13/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
koma = lambda v: f'{v:g}'.replace('.', ',').replace('-', '−')
def T(ax, x, y, s, c=TUA, fs=11, **k): ax.text(x, y, s, ha='center', va='center', color=c, fontsize=fs, **k)
def reaksi(ax, x1, x2, y, t='', c=TUA, t2='', fs=8.5, dua=False):
    if dua:
        ax.annotate('', (x2, y + 0.12), (x1, y + 0.12), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.1))
        ax.annotate('', (x1, y - 0.12), (x2, y - 0.12), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.1))
    else: ax.annotate('', (x2, y), (x1, y), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.3))
    if t: T(ax, (x1 + x2) / 2, y + 0.42, t, fs=fs)
    if t2: T(ax, (x1 + x2) / 2, y - 0.42, t2, fs=fs)
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def rd(smi, w=360, h=300, fs=30, pad=0.15, hs=(), bl=None):
    m = Chem.MolFromSmiles(smi)
    if hs: m = Chem.AddHs(m, onlyOnAtoms=tuple(hs))
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = pad
    if bl: o.fixedBondLength = bl
    o.updateAtomPalette({35: (0.71, 0.33, 0.11), 8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.10, 0.54, 0.42), 9: (0.10, 0.54, 0.42), 16: (0.75, 0.6, 0.1), 53: (0.45, 0.2, 0.6), 1: (0.05, 0.15, 0.28)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def gb(ax, smi, x0, x1, y0, y1, **k):
    k['w'], k['h'] = ukuran_px(ax, x0, x1, y0, y1); k['fs'] = min(k.get('fs', 25), 25); k.setdefault('bl', 40)
    pasang(ax, rd(smi, **k), x0, x1, y0, y1, zorder=2, maks=1.0)

# 1. inversi nitrogen (render 3D, model gugus disatukan)
import sys as _sy; _sy.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3d'))
from r3d import render, pas, tampil
TMP = os.path.join(F, '_r3d'); os.makedirs(TMP, exist_ok=True)
def lob(d, L, w, c, o=(0, 0, 0), a=1.0, k=0.7): return {'d': list(map(float, d)), 'L': L, 'w': w, 'c': c, 'o': list(map(float, o)), 'a': a, 'k': k}
GR = [('R$_1$', 0x1a8a6a, 150), ('R$_2$', 0x8a63c9, 30), ('R$_3$', 0xd9874a, 270)]
def amina(arah):  # arah +1: pasangan bebas ke atas; 0: datar (TS); -1: ke bawah
    zc = -arah * 0.36; at = [{'p': [0, 0, 0], 'r': 0.32, 'c': 0x3f72d6}]; bd = []; lab = []
    for nm, c_, ang in GR:
        t = np.radians(ang); v = np.array([np.cos(t) * np.sqrt(1 - zc ** 2), np.sin(t) * np.sqrt(1 - zc ** 2), zc]) * 1.5
        at.append({'p': list(map(float, v)), 'r': 0.36, 'c': c_}); bd.append({'p': [0, 0, 0], 'q': list(map(float, v)), 'r': 0.085, 'c': 0xb9bfc7}); lab.append(v * 1.55 + [0, 0, -0.12])
    if arah: lobes = [lob((0, 0, arah), 1.1, 0.42, 0x7fb4ec, (0, 0, 0.28 * arah), k=0.75)]
    else: lobes = [lob((0, 0, 1), 0.95, 0.34, 0x7fb4ec, a=0.75), lob((0, 0, -1), 0.95, 0.34, 0x7fb4ec, a=0.75)]
    sp = {'atoms': at, 'bonds': bd, 'lobes': lobes, 'w': 600, 'h': 640, 'camdir': [0.1, -1, 0.42 if arah >= 0 else -0.42], 'up': [0, 0, 1], 'labels': [list(map(float, l)) for l in lab] + [[0, 0, 0]]}
    return pas(sp, 0.45)
J = [(amina(1), f'{TMP}/inv_a.png'), (amina(0), f'{TMP}/inv_ts.png'), (amina(-1), f'{TMP}/inv_b.png')]
PR = render(J)
f = plt.figure(figsize=(7.4, 3.0), dpi=220)
for k, (fn, x0) in enumerate([(J[0][1], 0.0), (J[1][1], 0.37), (J[2][1], 0.74)]):
    a = f.add_axes([x0, 0.16, 0.26, 0.74]); a.axis('off'); tampil(a, fn); q = PR[fn]
    for (nm, c_, _), p_ in zip(GR, q[:3]): a.text(*p_, nm, ha='center', va='center', fontsize=9.5, color='#%06x' % c_, fontweight='bold')
from matplotlib.patches import FancyArrowPatch as _FAP
for x in (0.285, 0.655):
    f.add_artist(_FAP((x, 0.565), (x + 0.065, 0.565), transform=f.transFigure, arrowstyle='-|>', mutation_scale=9, color=TUA, lw=1.1))
    f.add_artist(_FAP((x + 0.065, 0.515), (x, 0.515), transform=f.transFigure, arrowstyle='-|>', mutation_scale=9, color=TUA, lw=1.1))
f.text(0.5, 0.95, 'keadaan transisi datar (sp²), pasangan bebas di orbital p', ha='center', fontsize=8.6, color=TUA)
f.text(0.5, 0.03, 'penghalang ± 25 kJ mol$^{-1}$: miliaran kali per detik', ha='center', fontsize=8.8, color=HJ)
f.savefig(f'{F}/inversi.png', bbox_inches='tight'); plt.close(f)

# 2. pKaH
d2 = [('piperidina', 11.1, BIRU), ('dimetilamina', 10.73, BIRU), ('metilamina', 10.64, BIRU), ('trimetilamina', 9.80, BIRU), ('amonia', 9.25, '#999999'),
      ('imidazola', 7.0, HJ), ('4-metoksianilina', 5.3, JG), ('piridina', 5.2, HJ), ('anilina', 4.6, JG), ('4-nitroanilina', 1.0, JG), ('asetamida', -0.5, JT), ('pirola', -3.8, JT)]
f, ax = plt.subplots(figsize=(6.0, 3.8), dpi=220)
y = np.arange(len(d2))[::-1]
ax.barh(y, [v for _, v, _ in d2], color=[c for *_, c in d2], height=0.65)
for yi, (n, v, c) in zip(y, d2): ax.text(v + (0.25 if v >= 0 else -0.25), yi, (koma(v) + ',0' if float(v).is_integer() and abs(v) < 100 else koma(v)), va='center', ha='left' if v >= 0 else 'right', fontsize=8.5)
ax.axvline(0, color=TUA, lw=0.8); ax.set_yticks(y); ax.set_yticklabels([n for n, *_ in d2], fontsize=8.5); ax.set_xlabel('pKaH (lebih besar = basa lebih kuat)'); ax.set_xlim(-5.5, 12.8)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda q, _: koma(q)))
plt.tight_layout(); f.savefig(f'{F}/pkah.png', bbox_inches='tight'); plt.close(f)

# 3. membuat amina
f, ax = kanv(7.8, 4.2, (0, 30), (0, 16.2))
y = 13.4
gb(ax, 'O=C1[N-]C(=O)c2ccccc12', 0, 3.8, y - 1.9, y + 1.9); T(ax, 5.5, y, '+ CH₃CH₂CH₂Br', fs=8); reaksi(ax, 7.6, 8.9, y + 0.9, 'SN2')
gb(ax, 'CCCN1C(=O)c2ccccc2C1=O', 8.8, 13.8, y - 1.9, y + 1.9); reaksi(ax, 14.2, 16.8, y, 'H₂NNH₂')
gb(ax, 'CCCN', 17.0, 20.0, y - 1.3, y + 1.3); T(ax, 24.6, y, 'Gabriel:\namina primer murni', fs=8.5, c=HJ)
y = 8.0
gb(ax, 'O=C1CCCCC1', 0, 3.4, y - 1.8, y + 1.8); T(ax, 5.2, y, '+ CH₃CH₂NH₂', fs=8); reaksi(ax, 6.9, 8.6, y, '−H₂O', dua=True)
gb(ax, 'CCN=C1CCCCC1', 8.8, 13.2, y - 1.8, y + 1.8); reaksi(ax, 13.6, 16.8, y, 'NaBH₃CN')
gb(ax, 'CCNC1CCCCC1', 17.0, 21.4, y - 1.8, y + 1.8); T(ax, 25.4, y, 'aminasi reduktif', fs=8.5, c=HJ)
y = 2.6
gb(ax, 'CC(=O)Nc1ccccc1', 0, 4.6, y - 1.9, y + 1.9); reaksi(ax, 5.0, 8.6, y, 'LiAlH₄; H₂O')
gb(ax, 'CCNc1ccccc1', 8.8, 13.2, y - 1.9, y + 1.9); T(ax, 18.8, y, 'reduksi amida: C=O → CH₂', fs=8.5, c=HJ)
f.savefig(f'{F}/buat.png', bbox_inches='tight'); plt.close(f)

# 4. Hofmann
f, ax = kanv(7.6, 2.8, (0, 28), (0, 10.0))
gb(ax, 'CCC(C)N', 0, 3.8, 3.2, 6.8); reaksi(ax, 4.0, 7.0, 5.0, 'CH₃I berlebih')
gb(ax, 'CCC(C)[N+](C)(C)C', 7.2, 11.8, 2.8, 7.2); T(ax, 12.1, 6.6, 'I$^-$', fs=10)
T(ax, 14.6, 5.0, 'Ag₂O, H₂O\npanas (E2)', fs=8.5); ax.annotate('', (16.8, 7.6), (13.2, 5.9), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); ax.annotate('', (16.8, 2.4), (13.2, 4.1), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.0, ls='--'))
gb(ax, 'C=CCC', 17.0, 20.4, 6.0, 9.4); T(ax, 24.2, 7.7, 'but-1-ena (utama)\nalkena Hofmann', fs=8.5, c=HJ)
gb(ax, 'C/C=C/C', 17.0, 20.4, 0.6, 4.0); T(ax, 24.2, 2.3, 'but-2-ena (sedikit)\nalkena Zaitsev', fs=8.5, c=JT)
T(ax, 9.5, 1.2, 'gugus pergi besar: H diambil\ndari CH₃ ujung', fs=8, c=TUA)
f.savefig(f'{F}/hofmann.png', bbox_inches='tight'); plt.close(f)

# 5. diazonium map
f, ax = kanv(7.2, 6.0, (-12, 12), (-10, 10))
gb(ax, 'N#[N+]c1ccccc1', -2.8, 2.8, -2.2, 2.2, bl=52, w=560)
prod = [('Clc1ccccc1', 'CuCl'), ('Brc1ccccc1', 'CuBr'), ('N#Cc1ccccc1', 'CuCN'), ('Ic1ccccc1', 'KI'), ('Fc1ccccc1', 'HBF₄, panas'),
        ('Oc1ccccc1', 'H₂O, panas'), ('c1ccccc1', 'H₃PO₂'), ('Oc1ccc(cc1)N=Nc1ccccc1', 'fenol (kopling)')]
for i, (s_, r) in enumerate(prod):
    th = np.pi / 2 - 2 * np.pi * i / len(prod); x, y = 8.8 * np.cos(th), 7.4 * np.sin(th)
    ax.annotate('', (x * 0.62, y * 0.62), (x * 0.3, y * 0.3), arrowprops=dict(arrowstyle='-|>', color=HJ if i < 7 else BIRU, lw=1.2))
    w = 6.0 if i == 7 else 3.6
    gb(ax, s_, x - w / 2, x + w / 2, y - 1.5, y + 1.5, bl=52, w=int(360 * w / 3.6))
    mx, my = x * 0.47, y * 0.47; n = np.array([-np.sin(th), np.cos(th)]) * 1.15
    T(ax, mx + n[0], my + n[1], r, fs=7.5)
T(ax, 0, -9.6, 'dari anilina: NaNO₂, HCl, 0–5 °C', fs=8.5, c=TUA)
f.savefig(f'{F}/diazonium.png', bbox_inches='tight'); plt.close(f)

# 6. metil jingga
f, ax = kanv(7.8, 3.2, (0, 30), (0, 12))
y = 9.0
gb(ax, 'N#[N+]c1ccc(cc1)S(=O)(=O)[O-]', 0, 6.0, y - 2.0, y + 2.0); T(ax, 6.6, y, '+', fs=12); gb(ax, 'CN(C)c1ccccc1', 7.0, 10.6, y - 1.8, y + 1.8)
reaksi(ax, 11.0, 13.6, y, 'kopling', t2='(para)')
gb(ax, 'CN(C)c1ccc(cc1)N=Nc1ccc(cc1)S(=O)(=O)[O-]', 13.8, 26.0, y - 2.4, y + 2.4, w=720, h=240, fs=26)
ax.add_patch(FancyBboxPatch((26.6, y - 0.8), 2.6, 1.6, boxstyle='round,pad=0.1', fc='#f4d03f', ec='none')); T(ax, 27.9, y, 'kuning', fs=8.5)
ax.annotate('', (19.6, 3.9), (19.6, 6.4), arrowprops=dict(arrowstyle='-|>', color=MERAH, lw=1.3)); ax.annotate('', (20.4, 6.4), (20.4, 3.9), arrowprops=dict(arrowstyle='-|>', color=HJ, lw=1.3))
T(ax, 17.4, 5.2, 'H$^+$ (pH < 3,1)', fs=8.5, c=MERAH); T(ax, 22.4, 5.2, 'OH$^-$ (pH > 4,4)', fs=8.5, c=HJ)
y = 2.0
gb(ax, 'C[N+](C)=C1C=CC(C=C1)=NNc1ccc(cc1)S(=O)(=O)[O-]', 13.8, 26.0, y - 2.2, y + 2.2, w=720, h=240, fs=26)
ax.add_patch(FancyBboxPatch((26.6, y - 0.8), 2.6, 1.6, boxstyle='round,pad=0.1', fc='#d9453b', ec='none')); T(ax, 27.9, y, 'merah', fs=8.5, c='white')
T(ax, 6.0, 2.0, 'metil jingga\n(indikator, pH 3,1–4,4)', fs=9, c=TUA)
f.savefig(f'{F}/azo.png', bbox_inches='tight'); plt.close(f)

# 7. heterosiklik: posisi serangan dan ion arenium pirola
f, ax = kanv(7.8, 3.8, (0, 30), (0, 14.4))
gb(ax, 'c1ccncc1', 0, 4.0, 9.0, 13.4)
T(ax, 9.8, 12.2, 'piridina (miskin elektron)', fs=9.5, c=JT, fontweight='bold')
T(ax, 9.8, 10.9, 'E$^+$: lambat, di C3', fs=9, c=TUA); T(ax, 9.8, 9.8, 'Nu$^-$: di C2 dan C4', fs=9, c=TUA)
gb(ax, 'c1cc2ccccc2[nH]1', 16.0, 20.8, 9.0, 13.4); T(ax, 25.2, 11.2, 'indola: E$^+$ di C3\n(cincin benzena tetap utuh)', fs=9, c=HJ)
gb(ax, 'c1cc[nH]c1', 0, 3.6, 2.2, 6.0); T(ax, 1.8, 1.4, 'pirola (kaya elektron)', fs=8.5, c=HJ)
reaksi(ax, 4.0, 6.4, 4.1, 'Br$^+$', t2='di C2')
for k, s in enumerate(['BrC1[CH+]C=CN1', 'BrC1C=C[CH+]N1', 'BrC1C=CC=[NH+]1']):
    x = 6.8 + k * 6.6; gb(ax, s, x, x + 4.6, 1.8, 6.6, hs=(1,))
    if k < 2: T(ax, x + 5.6, 4.1, '↔', fs=13, family='DejaVu Sans')
ax.add_patch(FancyBboxPatch((19.9, 1.7), 4.8, 5.0, boxstyle='round,pad=0.1', fc='none', ec=HJ, lw=1.2))
T(ax, 22.3, 0.8, 'iminium: semua oktet', fs=8, c=HJ); T(ax, 27.6, 4.1, 'tiga struktur\n(C3: hanya dua)', fs=8.5, c=TUA)
f.savefig(f'{F}/hetero.png', bbox_inches='tight'); plt.close(f)

# 8. amina dalam biologi
f, ax = kanv(7.8, 4.6, (0, 30), (0, 17.6))
for i, (a, b, na, nb) in enumerate([('N[C@@H](Cc1ccc(O)cc1)C(=O)O', 'NCCc1ccc(O)c(O)c1', 'tirosina', 'dopamina'),
                                    ('N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O', 'NCCc1c[nH]c2ccc(O)cc12', 'triptofan', 'serotonin'),
                                    ('N[C@@H](Cc1c[nH]cn1)C(=O)O', 'NCCc1c[nH]cn1', 'histidina', 'histamina')]):
    x = i * 10.0
    gb(ax, a, x + 0.0, x + 4.4, 12.6, 17.2); reaksi(ax, x + 4.5, x + 5.9, 14.9, '−CO₂', fs=7.5)
    gb(ax, b, x + 6.0, x + 9.8, 12.6, 17.2); T(ax, x + 2.2, 12.2, na, fs=8, c=TUA); T(ax, x + 7.9, 12.2, nb, fs=8, c=HJ)
T(ax, 15.0, 10.6, 'dekarboksilasi oleh enzim (piridoksal fosfat)', fs=8.5, c=BIRU)
for i, (s, n) in enumerate([('COc1ccc2nccc([C@@H](O)[C@@H]3C[C@@H]4CCN3C[C@@H]4C=C)c2c1', 'kinina'), ('Cn1cnc2c1c(=O)n(C)c(=O)n2C', 'kafeina'), ('CN1CCC[C@H]1c1cccnc1', 'nikotina')]):
    x = 1.0 + i * 10.0
    gb(ax, s, x, x + 8.0, 1.4, 9.4, w=420, h=400, fs=24); T(ax, x + 4.0, 0.7, n, fs=9, c=JT)
f.savefig(f'{F}/biologi.png', bbox_inches='tight'); plt.close(f)
print('ok')
