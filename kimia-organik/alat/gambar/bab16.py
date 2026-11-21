# Gambar Bab 16: strategi sintesis. Tingkat oksidasi, peta interkonversi, Grignard, sinton, pohon retrosintesis,
# urutan aromatik, gugus pelindung, hasil keseluruhan, linear/konvergen, ibuprofen BHC, parasetamol
import os, io, numpy as np, matplotlib, matplotlib.ticker
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang, ukuran_px
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False, 'mathtext.fontset': 'dejavusans'})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab16/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
koma = lambda v: f'{v:g}'.replace('.', ',').replace('-', '−')
fmt = matplotlib.ticker.FuncFormatter(lambda q, _: koma(round(q, 3)))
def T(ax, x, y, s, c=TUA, fs=10, **k): ax.text(x, y, s, ha=k.pop('ha', 'center'), va=k.pop('va', 'center'), color=c, fontsize=fs, **k)
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def panah(ax, a, b, c=TUA, lw=1.4, ms=11, **k): ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw, **k))
def retro(ax, a, b, c=TUA):
    (x0, y), (x1, _) = a, b
    for dy in (0.09, -0.09): ax.plot([x0, x1 - 0.12], [y + dy, y + dy], color=c, lw=1.3)
    ax.plot([x1 - 0.35, x1, x1 - 0.35], [y + 0.28, y, y - 0.28], color=c, lw=1.3)
def simpan(f, n): f.savefig(f'{F}/{n}.png', bbox_inches='tight'); plt.close(f)
def rd(smi, w=360, h=260, fs=26, bl=None, hl=(), hb=()):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = 0.08
    if bl: o.fixedBondLength = bl
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 35: (0.55, 0.25, 0.10), 12: (0.10, 0.54, 0.42), 1: (0.05, 0.15, 0.28)})
    o.setBackgroundColour((1, 1, 1, 0)); rdMolDraw2D.PrepareAndDrawMolecule(d, m, highlightAtoms=list(hl), highlightBonds=list(hb), highlightAtomColors={i: (0.94, 0.63, 0.38) for i in hl}, highlightBondColors={i: (0.94, 0.63, 0.38) for i in hb})
    d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def gb(ax, smi, x0, x1, y0, y1, **k):
    w, h = ukuran_px(ax, x0, x1, y0, y1); k['fs'] = min(k.get('fs', 25), 25); k['bl'] = max(k.get('bl', 40), 36)
    pasang(ax, rd(smi, w=w, h=h, **k), x0, x1, y0, y1, zorder=2, maks=1.0)
def skema(ax, items, y0, y1, x=0.0, wm=3.0, wa=2.2, bl=34, fs=24):
    for it in items:
        if isinstance(it, tuple):
            ax.annotate('', (x + wa - 0.15, (y0 + y1) / 2), (x + 0.15, (y0 + y1) / 2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3))
            T(ax, x + wa / 2, (y0 + y1) / 2 + 0.35, it[0], fs=7.8, va='bottom', c=JT);
            if len(it) > 1: T(ax, x + wa / 2, (y0 + y1) / 2 - 0.3, it[1], fs=7.4, va='top', c='#555555')
            x += wa
        else:
            smi, lab = it if isinstance(it, list) else (it, None)
            gb(ax, smi, x, x + wm, y0, y1, bl=bl, fs=fs)
            if lab: T(ax, x + wm / 2, y0 + 1.2, lab, fs=7.8, va='top')
            x += wm
    return x

# 1. tingkat oksidasi
f, ax = kanv(7.4, 3.3, (0, 30), (0, 13))
kol = [('tingkat 0', ['alkana', 'R–H']), ('tingkat 1', ['alkohol', 'eter', 'alkil halida', 'amina']), ('tingkat 2', ['aldehida', 'keton', 'asetal', 'imina']),
       ('tingkat 3', ['asam karboksilat', 'ester, amida', 'klorida asam', 'nitril']), ('tingkat 4', ['CO₂', 'karbonat', 'urea'])]
for i, (h, gs) in enumerate(kol):
    x = 3 + i * 6
    ax.add_patch(FancyBboxPatch((x - 2.4, 2.2), 4.8, 8.0, boxstyle='round,pad=0.1', fc=['#eef4fa', '#e3eef8', '#d6e7f6', '#c6def3', '#b8d6f0'][i], ec='none'))
    T(ax, x, 9.5, h, fs=9.5, fontweight='bold')
    for j, g in enumerate(gs): T(ax, x, 8.2 - j * 1.4, g, fs=8.6)
panah(ax, (4.0, 11.4), (26.0, 11.4), c=JT, lw=1.6); T(ax, 15, 12.3, 'oksidasi: PCC, H₂CrO₄, KMnO₄, O₃', c=JT, fs=8.8)
panah(ax, (26.0, 1.2), (4.0, 1.2), c=BIRU, lw=1.6); T(ax, 15, 0.3, 'reduksi: NaBH₄, LiAlH₄, H₂/katalis', c=BIRU, fs=8.8)
simpan(f, 'tingkat')

# 2. peta interkonversi
f, ax = kanv(7.6, 5.4, (0, 30), (0, 21))
N = {'alkuna': (2.5, 18), 'alkena': (10, 18), 'alkana': (2.5, 12.5), 'epoksida': (17, 18), 'alkil halida': (6, 9), 'alkohol': (15, 11.5),
     'eter': (15, 4.5), 'aldehida/keton': (23.5, 15.5), 'asam': (27, 9.5), 'ester': (27, 4), 'amida': (21.5, 1.3), 'nitril': (9.5, 3), 'amina': (3, 4)}
for k, (x, y) in N.items():
    ax.add_patch(FancyBboxPatch((x - 2.1, y - 0.75), 4.2, 1.5, boxstyle='round,pad=0.12', fc=TUA if k == 'alkohol' else '#dfeaf5', ec='none', zorder=3))
    T(ax, x, y, k, fs=8.6, c='white' if k == 'alkohol' else TUA, fontweight='bold', zorder=4)
E = [('alkuna', 'alkena', 'H₂, Lindlar\nNa, NH₃', 0, (0, 0.9)), ('alkena', 'alkana', 'H₂, Pd', 0.0, (-0.6, 0.3)), ('alkuna', 'aldehida/keton', 'H₂O, HgSO₄', -0.3, (-4.0, 2.9)),
     ('alkena', 'epoksida', 'RCO₃H', 0, (0, 0.5)), ('epoksida', 'alkohol', 'Nu$^-$ atau H₃O$^+$', 0, (1.3, 0.2)), ('alkena', 'alkohol', 'H₃O$^+$\nBH₃; H₂O₂', 0.15, (-0.9, -0.4)),
     ('alkohol', 'alkena', 'H₂SO₄, Δ', 0.15, (1.1, 0.3)), ('alkena', 'alkil halida', 'HBr', 0.12, (-0.8, 0)), ('alkil halida', 'alkena', 'basa (E2)', 0.12, (0.9, 0)),
     ('alkohol', 'alkil halida', 'PBr₃, SOCl₂', 0.12, (0, 0.5)), ('alkil halida', 'alkohol', 'OH$^-$', 0.12, (0, -0.5)), ('alkohol', 'eter', 'NaH; RX', 0, (0.9, 0)),
     ('alkohol', 'aldehida/keton', 'PCC', 0.15, (-0.3, 0.6)), ('aldehida/keton', 'alkohol', 'NaBH₄', 0.15, (0.4, -0.6)), ('aldehida/keton', 'asam', 'H₂CrO₄', 0, (0.9, 0.3)),
     ('asam', 'ester', 'ROH, H$^+$', 0.2, (-2.3, 0)), ('ester', 'asam', 'NaOH;\nH₃O$^+$', 0.2, (1.9, 0)), ('ester', 'amida', 'R₂NH', 0, (0.5, -0.5)),
     ('ester', 'alkohol', 'LiAlH₄', 0.0, (0.3, 0.5)), ('alkil halida', 'nitril', 'CN$^-$', 0, (0.7, 0)), ('nitril', 'asam', 'H₃O$^+$, Δ', -0.15, (0, -0.6)),
     ('nitril', 'amina', 'LiAlH₄', 0, (0, 0.45)), ('amida', 'amina', 'LiAlH₄', -0.22, (0, -1.6)), ('alkil halida', 'amina', 'N₃$^-$; LiAlH₄', 0, (-1.4, 0)),
     ('alkena', 'aldehida/keton', 'O₃', 0.18, (0, 0.5))]
def tepi(a, b):
    (x0, y0), (x1, y1) = N[a], N[b]; v = np.array([x1 - x0, y1 - y0]); L = np.hypot(*v); u = v / L
    k = min(2.3 / max(abs(u[0]), 1e-9), 0.9 / max(abs(u[1]), 1e-9)); return np.array([x0, y0]) + u * k, np.array([x1, y1]) - u * k
for a, b, lab, rad, off in E:
    p, q = tepi(a, b)
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=9, color=BIRU, lw=1.0, connectionstyle=f'arc3,rad={rad}', zorder=2))
    m = (p + q) / 2 + np.array(off); T(ax, m[0], m[1], lab, fs=6.6, c=JT, zorder=5, bbox=dict(boxstyle='round,pad=0.1', fc='white', ec='none', alpha=0.85))
simpan(f, 'peta')

# 3. Grignard
f, ax = kanv(7.4, 4.6, (0, 30), (0, 19))
gb(ax, 'Br[Mg]c1ccccc1', 11.5, 18.5, 5.6, 10.1, bl=30)
prod = [('OCc1ccccc1', 'H₂C=O', 'alkohol 1°', (3.5, 14.6)), ('CC(O)c1ccccc1', 'CH₃CHO', 'alkohol 2°', (15, 15.6)), ('CC(C)(O)c1ccccc1', '(CH₃)₂C=O', 'alkohol 3°', (26.5, 14.6)),
        ('OC(=O)c1ccccc1', 'CO₂', 'asam (+1 C)', (5, 3.0)), ('OCCc1ccccc1', 'oksirana', 'alkohol (+2 C)', (25, 3.0))]
for smi, rg, lab, (x, y) in prod:
    gb(ax, smi, x - 3.4, x + 3.4, y - 2.3, y + 2.3, bl=28)
    T(ax, x, y + 2.7 if y > 10 else y - 2.8, lab, fs=8.5, c=HJ, fontweight='bold')
    v = np.array([x - 15, y - 7.85]); u = v / np.hypot(*v); a = np.array([15, 7.85]) + u * np.where(abs(u[0]) < 0.3, 2.0, 3.6); b = np.array([x, y]) - u * np.where(abs(u[0]) < 0.3, 2.0, 3.0)
    panah(ax, a, b, c=BIRU, lw=1.2, ms=10); mm = a + 0.68 * (b - a)
    if abs(u[0]) < 0.3: T(ax, mm[0] + 0.5, (a[1] + b[1]) / 2, rg + ';\nH₃O$^+$', fs=7.8, c=JT, ha='left')
    else:
        mm = (a + b) / 2; nv = np.array([-u[1], u[0]]) * np.sign(u[0]) * (1 if u[1] > 0 else -1); mm = mm + np.array([0, 1.0 if u[1] > 0 else -1.0])
        T(ax, mm[0], mm[1], rg + '; H₃O$^+$', fs=7.8, c=JT, rotation=np.degrees(np.arctan2(u[1], u[0])) if u[0] > 0 else np.degrees(np.arctan2(-u[1], -u[0])))
simpan(f, 'grignard')

# 4. sinton
f, ax = kanv(7.4, 3.0, (0, 30), (0, 12))
gb(ax, 'OC(CCC)c1ccccc1', 0, 7.4, 3.2, 9.6, bl=30, hb=[1])
T(ax, 3.7, 2.6, '1-fenilbutan-1-ol', fs=8.5); T(ax, 3.7, 10.4, 'target', fs=8.5, c=HJ, fontweight='bold')
retro(ax, (8.0, 6.4), (10.2, 6.4)); T(ax, 9.1, 7.3, 'putus C1–C2', fs=7.8, c=JT)
T(ax, 14.6, 8.2, 'sinton', fs=8.5, c=HJ, fontweight='bold')
T(ax, 14.6, 6.6, 'C₆H₅–CH$^+$–OH', fs=9.5); T(ax, 14.6, 4.9, '$^-$CH₂CH₂CH₃', fs=9.5)
T(ax, 14.6, 3.4, 'elektrofil + nukleofil', fs=7.8, c='#666666')
panah(ax, (17.6, 6.0), (19.6, 6.0), c=TUA)
T(ax, 25.0, 10.4, 'padanan sintetik', fs=8.5, c=HJ, fontweight='bold')
gb(ax, 'O=Cc1ccccc1', 19.8, 25.0, 5.2, 9.8, bl=28); T(ax, 22.4, 4.9, 'benzaldehida', fs=8)
T(ax, 25.6, 7.3, '+', fs=12)
gb(ax, 'CCC[Mg]Br', 25.8, 30.0, 5.4, 9.2, bl=28); T(ax, 27.9, 4.9, 'PrMgBr', fs=8)
T(ax, 24.9, 2.3, 'sintesis maju: PrMgBr + PhCHO, lalu H₃O$^+$', fs=8, c=BIRU)
simpan(f, 'sinton')

# 5. pohon retrosintesis 4-fenilbutan-2-ol
f, ax = kanv(7.4, 4.4, (0, 30), (0, 18))
gb(ax, 'CC(O)CCc1ccccc1', 9.5, 20.5, 12.4, 17.8, bl=30)
T(ax, 15, 12.0, '4-fenilbutan-2-ol', fs=8.8, fontweight='bold')
for x, lab in [(7.5, '(a) putus C2–C3'), (22.5, '(c) putus C3–C4')]:
    ax.plot([15, x], [11.4, 9.4], color=TUA, lw=1.1); ax.plot([15, x], [11.1, 9.1], color=TUA, lw=1.1)
    dv = np.array([x - 15, -2.0]); dv /= np.hypot(*dv); nv = np.array([-dv[1], dv[0]]); e = np.array([x, 9.25])
    for sg in (1, -1): ax.plot([e[0], e[0] - dv[0] * 0.6 + sg * nv[0] * 0.45], [e[1], e[1] - dv[1] * 0.6 + sg * nv[1] * 0.45], color=TUA, lw=1.1)
    T(ax, (15 + x) / 2 + (-2.4 if x < 15 else 2.4), 10.9, lab, fs=8, c=JT)
gb(ax, 'CC=O', 1.0, 4.6, 5.0, 8.6, bl=28); T(ax, 5.0, 6.8, '+', fs=12); gb(ax, 'Br[Mg]CCc1ccccc1', 5.4, 13.6, 4.6, 9.0, bl=28)
T(ax, 7.3, 3.8, 'asetaldehida + 2-feniletil-MgBr\n(Grignard dari halida yang perlu dibuat dulu)', fs=7.8, c='#555555')
gb(ax, 'Br[Mg]Cc1ccccc1', 16.2, 22.6, 4.6, 9.0, bl=28); T(ax, 23.0, 6.8, '+', fs=12); gb(ax, 'CC1CO1', 23.4, 27.6, 5.0, 8.6, bl=28)
T(ax, 22.2, 3.8, 'benzil-MgBr + metiloksirana\n(dari toluena: NBS, lalu Mg): lebih pendek', fs=7.8, c=HJ)
T(ax, 22.2, 1.3, 'Grignard menyerang C epoksida yang kurang tersubstitusi', fs=7.6, c='#555555')
simpan(f, 'pohonretro')

# 6. urutan aromatik
f, ax = kanv(7.4, 3.6, (0, 30), (0, 14.5))
T(ax, 7.5, 14.0, 'nitrasi dulu → meta', fs=9.5, c=JT, fontweight='bold'); T(ax, 22.5, 14.0, 'brominasi dulu → para', fs=9.5, c=BIRU, fontweight='bold')
ax.plot([15, 15], [0.5, 13.5], color='#cccccc', lw=0.8)
gb(ax, 'c1ccccc1', 0.3, 4.3, 8.0, 12.5, bl=26); panah(ax, (4.4, 10.2), (6.4, 10.2)); T(ax, 5.4, 11.4, 'HNO₃\nH₂SO₄', fs=7.5, c=JT)
gb(ax, 'O=[N+]([O-])c1ccccc1', 6.4, 11.6, 8.0, 12.8, bl=26); panah(ax, (9.0, 7.9), (9.0, 6.4)); T(ax, 10.9, 7.2, 'Br₂, FeBr₃', fs=7.5, c=JT)
gb(ax, 'O=[N+]([O-])c1cccc(Br)c1', 5.2, 12.8, 1.0, 6.4, bl=26); T(ax, 9.0, 0.6, 'm-bromonitrobenzena', fs=8.2, fontweight='bold')
gb(ax, 'c1ccccc1', 15.3, 19.3, 8.0, 12.5, bl=26); panah(ax, (19.4, 10.2), (21.4, 10.2)); T(ax, 20.4, 11.4, 'Br₂\nFeBr₃', fs=7.5, c=BIRU)
gb(ax, 'Brc1ccccc1', 21.4, 26.4, 8.0, 12.8, bl=26); panah(ax, (24.0, 7.9), (24.0, 6.4)); T(ax, 26.0, 7.2, 'HNO₃, H₂SO₄', fs=7.5, c=BIRU)
gb(ax, 'O=[N+]([O-])c1ccc(Br)cc1', 18.4, 29.6, 1.6, 6.2, bl=26); T(ax, 24.0, 0.6, 'p-bromonitrobenzena (+ sedikit o)', fs=8.2, fontweight='bold')
simpan(f, 'urutan')

# 7. gugus pelindung
f, ax = kanv(7.6, 2.2, (0, 36.4), (0, 10))
x = skema(ax, [['CC(=O)CCC(=O)OC', 'keto ester'], ('HOCH₂CH₂OH', 'H$^+$ (lindungi)'), ['CC1(CCC(=O)OC)OCCO1', 'asetal ester'], ('LiAlH₄', 'lalu H₂O'),
               ['CC1(CCCO)OCCO1', 'asetal alkohol'], ('H₃O$^+$', '(lepas)'), ['CC(=O)CCCO', '5-hidroksipentan-2-on']], 2.0, 8.6, x=0.0, wm=6.0, wa=4.1, bl=34, fs=24)
simpan(f, 'lindung')

# 8. hasil keseluruhan
f, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
n = np.arange(0, 21)
for p, c in [(0.95, HJ), (0.90, BIRU), (0.80, JT), (0.70, MERAH)]:
    ax.plot(n, 100 * p ** n, color=c, lw=1.8, marker='o', ms=3); lx = {0.95: 20, 0.90: 20, 0.80: 7, 0.70: 4}[p]
    ax.text(lx + 0.3, 100 * p ** lx + (0 if lx == 20 else 4), f'{koma(round(p * 100))}%', color=c, va='center', fontsize=8.5, fontweight='bold')
ax.axvline(10, color='#bbbbbb', lw=0.7, ls='--'); ax.text(10.2, 92, '10 langkah', fontsize=8, color='#777777')
ax.set_xlabel('jumlah langkah'); ax.set_ylabel('hasil keseluruhan (%)'); ax.set_xlim(0, 22); ax.set_ylim(0, 102); ax.set_xticks(range(0, 21, 2))
ax.text(11, 72, 'angka: hasil per langkah', fontsize=8, color='#555555')
plt.tight_layout(); simpan(f, 'hasil')

# 9. linear vs konvergen
f, ax = kanv(7.4, 3.4, (0, 30), (0, 13.6))
def kot(x, y, t, c='#dfeaf5', tc=TUA): ax.add_patch(FancyBboxPatch((x - 0.9, y - 0.6), 1.8, 1.2, boxstyle='round,pad=0.08', fc=c, ec='none')); T(ax, x, y, t, fs=9, c=tc, fontweight='bold')
T(ax, 1.0, 12.6, 'linear: 6 langkah berurutan', fs=9, ha='left', c=TUA, fontweight='bold')
xs = [2 + i * 3.6 for i in range(7)]
for i, x in enumerate(xs):
    kot(x, 10.6, 'ABCDEFG'[i], c=TUA if i == 6 else '#dfeaf5', tc='white' if i == 6 else TUA)
    if i: panah(ax, (xs[i - 1] + 1.0, 10.6), (x - 1.0, 10.6), lw=1.1, ms=9)
T(ax, 28.0, 10.6, '0,8⁶ = 26%', fs=9, c=JT, ha='left')
T(ax, 1.0, 7.6, 'konvergen: dua cabang 3 langkah + penggabungan', fs=9, ha='left', c=TUA, fontweight='bold')
for row, (y, ls) in enumerate([(5.6, 'ABCD'), (1.6, 'EFGH')]):
    for i, l in enumerate(ls):
        x = 2 + i * 3.6; kot(x, y, l)
        if i: panah(ax, (x - 2.6, y), (x - 1.0, y), lw=1.1, ms=9)
kot(18.0, 3.6, 'T', c=TUA, tc='white'); panah(ax, (13.8, 5.4), (17.0, 3.9), lw=1.1, ms=9); panah(ax, (13.8, 1.8), (17.0, 3.3), lw=1.1, ms=9)
T(ax, 20.0, 3.6, 'rangkaian terpanjang 4 langkah:\n0,8⁴ = 41%', fs=9, c=HJ, ha='left')
simpan(f, 'konvergen')

# 10. ibuprofen BHC
f, ax = kanv(7.6, 2.3, (0, 33.6), (0, 9.6))
skema(ax, [['CC(C)Cc1ccccc1', 'isobutilbenzena'], ('Ac₂O', 'HF (katalis)'), ['CC(C)Cc1ccc(cc1)C(C)=O', None], ('H₂', 'Ni Raney'),
           ['CC(C)Cc1ccc(cc1)C(C)O', None], ('CO', 'Pd (katalis)'), ['CC(C)Cc1ccc(cc1)C(C)C(=O)O', 'ibuprofen']], 1.8, 8.6, x=0, wm=6.2, wa=2.9, bl=30, fs=22)
simpan(f, 'ibuprofen')

# 11. parasetamol
f, ax = kanv(7.6, 2.3, (0, 33.6), (0, 9.6))
skema(ax, [['Oc1ccccc1', 'fenol'], ('HNO₃ encer', 'pisahkan para'), ['Oc1ccc(cc1)[N+](=O)[O-]', '4-nitrofenol'], ('H₂, Pd/C', None),
           ['Oc1ccc(N)cc1', '4-aminofenol'], ('Ac₂O', 'H₂O'), ['CC(=O)Nc1ccc(O)cc1', 'parasetamol']], 1.8, 8.6, x=0, wm=5.8, wa=3.2, bl=34, fs=24)
simpan(f, 'parasetamol')
print('selesai')
