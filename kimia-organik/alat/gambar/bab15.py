# Gambar Bab 15: NMR. Tingkat spin, FID, perisai, anisotropi, geseran kimia, uji penggantian,
# spektrum 1H skematis (etil asetat, etanol/D2O, propanol, keton aromatik), pohon kopling, Pascal, dd stirena, 13C, DEPT
import os, io, numpy as np, matplotlib, matplotlib.ticker
from math import comb
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch, Ellipse, Polygon, Arc
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False, 'mathtext.fontset': 'dejavusans'})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab15/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
koma = lambda v: f'{v:g}'.replace('.', ',').replace('-', '−')
fmt = matplotlib.ticker.FuncFormatter(lambda q, _: koma(round(q, 3)))
def T(ax, x, y, s, c=TUA, fs=10, **k): ax.text(x, y, s, ha=k.pop('ha', 'center'), va=k.pop('va', 'center'), color=c, fontsize=fs, **k)
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def panah(ax, a, b, c=TUA, lw=1.4, ms=11, **k): ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw, **k))
def simpan(f, n): f.savefig(f'{F}/{n}.png', bbox_inches='tight'); plt.close(f)

# ---------- simulasi spektrum 1H orde pertama ----------
MHZ = 300
def garis(d, n, kop=(), mhz=MHZ):
    pos = [(d * mhz, float(n))]
    for k, J in kop:
        w = [comb(k, i) / 2 ** k for i in range(k + 1)]
        pos = [(p + (i - k / 2) * J, a * w[i]) for p, a in pos for i in range(k + 1)]
    return [(p / mhz, a) for p, a in pos]
def jejak(x, sinyal, mhz=MHZ):
    y = np.zeros_like(x)
    for s in sinyal:
        lw = s.get('w', 0.9) / mhz
        for p, a in garis(s['d'], s['n'], s.get('kop', ()), mhz):
            y += a * (lw / 2) ** 2 / ((x - p) ** 2 + (lw / 2) ** 2) * (0.9 / s.get('w', 0.9))
    return y
def spektrum(ax, sinyal, xl, judul=None, inset=True, integ=True, tms=True, ins_w=0.55, ins_h=None):
    x = np.linspace(xl[1], xl[0], 40000); sg = list(sinyal) + ([{'d': 0.0, 'n': 1.2}] if tms else [])
    y = jejak(x, sg); y = y / y.max()
    ax.plot(x, y, color=TUA, lw=0.8); ax.set_xlim(*xl); ax.set_ylim(-0.32, 1.98)
    ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.xaxis.set_major_formatter(fmt)
    if integ:
        c = np.cumsum(jejak(x, sinyal)[::-1])[::-1]; c = c / c.max()
        ax.plot(x, 0.15 + 0.7 * c, color=JT, lw=1.0, alpha=0.9)
        for s in sinyal:
            ax.text(s.get('lx', s['d']), -0.2, s.get('lab', f"{s['n']}H"), ha='center', va='center', fontsize=7.6, color='white', fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', fc=JT, ec='none'))
    for s in sinyal:
        m = (abs(x - s['d']) < 0.08); hpk = y[m].max() if m.any() else 0.1
        if s.get('kop') and inset:
            g = garis(s['d'], s['n'], s['kop']); half = (max(p for p, _ in g) - min(p for p, _ in g)) / 2 + 0.012
            cx = s.get('ix', s['d']); wd = s.get('iw', ins_w * (xl[0] - xl[1]) / 10)
            ia = ax.inset_axes([cx - wd / 2, s.get('iy', 1.2), wd, ins_h or 0.55], transform=ax.transData)
            xi = np.linspace(s['d'] - half, s['d'] + half, 3000); yi = jejak(xi, [s]); ia.plot(xi, yi / yi.max(), color=BIRU, lw=0.9)
            ia.set_xlim(s['d'] + half, s['d'] - half); ia.set_ylim(-0.05, 1.15); ia.axis('off')
            ia.text(0.5, -0.1, (s.get('teks', '') + ' ' + s.get('nama', '')).strip(), transform=ia.transAxes, ha='center', va='top', fontsize=7.4, color=BIRU)
        elif s.get('teks'):
            ax.text(s.get('tx', s['d']), min(hpk, 1.0) + 0.05, s['teks'], ha='center', va='bottom', fontsize=7.6, color=TUA)
    if tms: ax.text(0, 1.05, 'TMS', ha='center', fontsize=7.5, color='#777777')
    if judul: ax.text(xl[0] - 0.02 * (xl[0] - xl[1]), 1.96, judul, fontsize=9.5, color=TUA, fontweight='bold', va='top')
    ax.set_xlabel('δ (ppm)')
# 1. tingkat energi spin
f, ax = plt.subplots(figsize=(6.4, 3.0), dpi=220)
B = np.linspace(0, 10.5, 50); ax.plot(B, B * 0.5, color=JT, lw=2); ax.plot(B, -B * 0.5, color=BIRU, lw=2); ax.plot([-1.2, 0], [0, 0], color=TUA, lw=2)
ax.text(10.6, 5.25, 'β (melawan medan)', color=JT, va='center', fontsize=9); ax.text(10.6, -5.25, 'α (searah medan)', color=BIRU, va='center', fontsize=9)
for b, t in [(7.05, '300 MHz'), (9.40, '400 MHz')]:
    ax.annotate('', (b, b * 0.5), (b, -b * 0.5), arrowprops=dict(arrowstyle='<->', color=TUA, lw=1.1)); ax.text(b - 0.15, 0.4, f'Δ$E$\n{t}', ha='right', va='center', fontsize=8.5, color=TUA)
    ax.plot([b, b], [-6.2, -b * 0.5], color='#aaaaaa', lw=0.6, ls='--')
ax.set_xlim(-1.4, 14.5); ax.set_ylim(-6.2, 6.2); ax.set_yticks([]); ax.spines['left'].set_visible(False)
ax.set_xticks([0, 2, 4, 6, 7.05, 9.40]); ax.xaxis.set_major_formatter(fmt); ax.set_xlabel('kuat medan $B_0$ (T)')
ax.text(-1.3, 0.6, 'tanpa\nmedan', fontsize=8, color=TUA, va='bottom'); ax.text(0.5, 5.6, 'energi', fontsize=8.5, color='#666666')
plt.tight_layout(); simpan(f, 'tingkat')

# 2. FID dan spektrum
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.4), dpi=220, gridspec_kw={'width_ratios': [1.25, 1]})
t = np.linspace(0, 1.0, 4000); fid = np.exp(-t / 0.28) * (np.cos(2 * np.pi * 21 * t) + 0.6 * np.cos(2 * np.pi * 47 * t))
a1.plot(t, fid, color=TUA, lw=0.7); a1.set_xlabel('waktu (s)'); a1.set_yticks([]); a1.spines['left'].set_visible(False); a1.xaxis.set_major_formatter(fmt); a1.set_title('FID (sinyal terhadap waktu)', fontsize=9, color=TUA)
nu = np.linspace(0, 70, 2000); sp = 1 / (1 + ((nu - 21) / 0.9) ** 2) + 0.6 / (1 + ((nu - 47) / 0.9) ** 2)
a2.plot(nu, sp, color=BIRU, lw=1.0); a2.set_xlim(70, 0); a2.set_yticks([]); a2.spines['left'].set_visible(False); a2.set_xlabel('frekuensi relatif (Hz)'); a2.set_title('spektrum (sinyal terhadap frekuensi)', fontsize=9, color=TUA)
f.text(0.535, 0.55, 'transformasi\nFourier  →', ha='center', fontsize=8.5, color=JT)
plt.tight_layout(w_pad=4); simpan(f, 'fid')

# 3. perisai
f, ax = kanv(7.2, 2.9, (0, 27), (0, 10.4))
panah(ax, (2.0, 0.8), (2.0, 9.6), c=TUA, lw=2); T(ax, 2.0, 10.1, '$B_0$', fs=11)
ax.add_patch(Ellipse((7.0, 5.2), 6.0, 2.2, fc='none', ec=MUDA, lw=6, alpha=0.6)); ax.add_patch(Circle((7.0, 5.2), 0.45, fc=JT, ec='none')); T(ax, 7.0, 5.2, 'H', c='white', fs=9)
ax.add_patch(FancyArrowPatch((9.9, 5.6), (8.6, 6.2), connectionstyle='arc3,rad=0.3', arrowstyle='-|>', mutation_scale=12, color=BIRU, lw=1.5))
T(ax, 7.0, 7.1, 'elektron bersirkulasi', c=BIRU, fs=8.5)
panah(ax, (7.0, 4.4), (7.0, 2.0), c=MERAH, lw=1.8); T(ax, 7.0, 1.4, '$B_\\mathrm{imbas}$ melawan $B_0$', c=MERAH, fs=8.5)
T(ax, 7.0, 9.0, '$B_\\mathrm{efektif} = B_0(1-\\sigma)$', fs=10)
ax.plot([13.0, 25.0], [4.6, 4.6], color=TUA, lw=1.2)
for i, d in enumerate(range(10, -1, -2)):
    x = 13.0 + i * 2.4; ax.plot([x, x], [4.6, 4.35], color=TUA, lw=1); T(ax, x, 3.9, str(d), fs=8.5)
T(ax, 19.0, 3.1, 'δ (ppm)', fs=9)
ax.add_patch(Rectangle((24.85, 4.6), 0.3, 1.0, fc=TUA)); T(ax, 25.4, 5.2, 'TMS', fs=8, ha='left')
panah(ax, (18.6, 6.0), (13.2, 6.0), c=JT, lw=1.6); T(ax, 15.8, 7.0, 'terawaperisai\nmedan bawah\nfrekuensi lebih tinggi', c=JT, fs=8, va='bottom')
panah(ax, (19.4, 6.0), (24.4, 6.0), c=BIRU, lw=1.6); T(ax, 21.9, 7.0, 'terperisai\nmedan atas\nfrekuensi lebih rendah', c=BIRU, fs=8, va='bottom')
T(ax, 19.0, 1.5, 'kerapatan elektron kecil  ←  →  kerapatan elektron besar', fs=8.2, c='#555555')
simpan(f, 'perisai')

# 4. anisotropi
f, ax = kanv(7.4, 3.3, (0, 30), (0, 13))
for cx, tl in [(5, '(a) benzena'), (15, '(b) C=C dan C=O'), (25, '(c) C≡C')]:
    T(ax, cx, 12.4, tl, fs=9.5, fontweight='bold'); panah(ax, (cx - 4.3, 1.0), (cx - 4.3, 4.0), c=TUA, lw=1.6); T(ax, cx - 4.3, 4.6, '$B_0$', fs=9)
# (a) cincin dilihat dari samping
ax.add_patch(Ellipse((5, 6.5), 5.0, 1.3, fc='#dfeaf5', ec=TUA, lw=1.4))
for sx in (-1, 1):
    ax.add_patch(Arc((5 + sx * 2.4, 6.5), 3.0, 6.0, theta1=90 if sx > 0 else -90 if False else 90, theta2=270 if sx < 0 else 270, color=MERAH, lw=1.0) if False else Ellipse((5 + sx * 2.6, 6.5), 3.0, 6.2, fc='none', ec=MERAH, lw=0.9, ls='--'))
panah(ax, (5, 9.2), (5, 7.4), c=MERAH, lw=1.3); T(ax, 5, 10.0, 'medan imbas', c=MERAH, fs=7.8)
for sx in (-1, 1):
    ax.add_patch(Circle((5 + sx * 2.8, 6.5), 0.35, fc=JT, ec='none')); T(ax, 5 + sx * 2.8, 6.5, 'H', c='white', fs=7)
T(ax, 5, 6.5, '$\\ominus$', c=BIRU, fs=12); T(ax, 1.6, 8.4, '$\\oplus$', c=JT, fs=12); T(ax, 8.4, 8.4, '$\\oplus$', c=JT, fs=12)
T(ax, 5, 2.6, 'H aromatik: δ 6,5–8,5', fs=8.2, c=JT)
# (b) C=C
ax.add_patch(Polygon([[13.6, 6.5], [16.4, 6.5], [17.6, 9.3], [12.4, 9.3]], closed=True, fc='#dfeaf5', ec='none')); ax.add_patch(Polygon([[13.6, 6.5], [16.4, 6.5], [17.6, 3.7], [12.4, 3.7]], closed=True, fc='#dfeaf5', ec='none'))
ax.plot([14.0, 16.0], [6.65, 6.65], color=TUA, lw=1.6); ax.plot([14.0, 16.0], [6.35, 6.35], color=TUA, lw=1.6)
for x, s in [(14.0, -1), (16.0, 1)]:
    ax.plot([x, x + s * 1.2], [6.5, 6.5], color=TUA, lw=1.2) if False else None
ax.plot([16.0, 17.4], [6.5, 7.3], color=TUA, lw=1.4); ax.add_patch(Circle((17.7, 7.45), 0.35, fc=JT, ec='none')); T(ax, 17.7, 7.45, 'H', c='white', fs=7)
ax.plot([14.0, 12.6], [6.5, 7.3], color=TUA, lw=1.4); ax.plot([14.0, 12.6], [6.5, 5.7], color=TUA, lw=1.4); ax.plot([16.0, 17.4], [6.5, 5.7], color=TUA, lw=1.4)
T(ax, 15, 8.6, '$\\ominus$', c=BIRU, fs=12); T(ax, 15, 4.4, '$\\ominus$', c=BIRU, fs=12); T(ax, 18.6, 6.5, '$\\oplus$', c=JT, fs=12); T(ax, 11.4, 6.5, '$\\oplus$', c=JT, fs=12)
T(ax, 15, 2.6, 'vinil 4,5–6,5; CHO 9,5–10,5', fs=8.2, c=JT)
# (c) alkuna vertikal
ax.add_patch(Polygon([[25, 6.5], [23.2, 11.2], [26.8, 11.2]], closed=True, fc='#dfeaf5', ec='none')); ax.add_patch(Polygon([[25, 6.5], [23.2, 1.8 + 1.0], [26.8, 2.8]], closed=True, fc='#dfeaf5', ec='none'))
for dx in (-0.18, 0, 0.18): ax.plot([25 + dx, 25 + dx], [5.6, 7.4], color=TUA, lw=1.4)
ax.plot([25, 25], [7.4, 8.5], color=TUA, lw=1.4); ax.add_patch(Circle((25, 8.85), 0.35, fc=JT, ec='none')); T(ax, 25, 8.85, 'H', c='white', fs=7)
ax.plot([25, 25], [4.6, 5.6], color=TUA, lw=1.4); T(ax, 25, 4.2, 'R', fs=8)
ax.add_patch(Ellipse((25, 6.5), 2.2, 0.8, fc='none', ec=MERAH, lw=1.0)); panah(ax, (26.3, 6.6), (26.1, 6.85), c=MERAH, lw=1.0, ms=8)
T(ax, 26.0, 10.3, '$\\ominus$', c=BIRU, fs=12); T(ax, 27.6, 6.5, '$\\oplus$', c=JT, fs=12)
T(ax, 25, 1.4, '≡C–H terperisai: δ 2,5', fs=8.2, c=BIRU)
simpan(f, 'cincin')

# 5. peta geseran kimia 1H
f, ax = plt.subplots(figsize=(7.2, 3.5), dpi=220)
rows = [('R–COOH', 10.0, 13.0, MERAH), ('aldehida O=C–H', 9.5, 10.5, JT), ('aromatik Ar–H', 6.5, 8.5, '#7b3294'), ('vinil C=C–H', 4.5, 6.5, '#7b3294'),
        ('H–C–O', 3.3, 4.5, BIRU), ('H–C–Cl, H–C–Br', 2.5, 4.0, BIRU), ('H–C–N', 2.2, 3.0, HJ), ('≡C–H', 2.4, 3.1, JG), ('Ar–CH₃ (benzilik)', 2.2, 2.5, JG),
        ('O=C–CH (α karbonil)', 2.0, 2.6, JG), ('C=C–CH₃ (alilik)', 1.6, 2.0, JG), ('alkil CH₃, CH₂, CH', 0.8, 1.7, TUA), ('R–OH, R–NH₂ (beragam)', 1.0, 5.0, '#999999')]
for i, (n, a, b, c) in enumerate(rows):
    y = len(rows) - i; ax.barh(y, b - a, left=a, height=0.62, color=c); ax.text(b + 0.15, y, n, ha='right', va='center', fontsize=7.8, color=TUA)
ax.set_xlim(13.5, -0.3); ax.set_xticks(range(0, 14)); ax.set_ylim(-0.4, len(rows) + 0.8); ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.set_xlabel('δ (ppm)')
ax.text(13.3, -0.15, '← terawaperisai (medan bawah)', fontsize=7.8, color='#777777', ha='left'); ax.text(-0.2, -0.15, 'terperisai (medan atas) →', fontsize=7.8, color='#777777', ha='right')
plt.tight_layout(); simpan(f, 'geseran')

# 6. uji penggantian (topik)
def rdh(smi, hidx, hl_atoms=(), w=380, h=300, fs=26):
    m = Chem.AddHs(Chem.MolFromSmiles(smi), onlyOnAtoms=tuple(hidx)); Chem.AssignStereochemistry(m, cleanIt=True, force=True)
    from rdkit.Chem import AllChem; AllChem.Compute2DCoords(m)
    hs = [a.GetIdx() for a in m.GetAtoms() if a.GetSymbol() == 'H']
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 3; o.fixedFontSize = fs; o.padding = 0.12
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 17: (0.10, 0.54, 0.42), 1: (0.05, 0.15, 0.28)})
    for i, a in enumerate(hs): o.atomLabels[a] = 'H' + ('ᵃ' if i == 0 else 'ᵇ')
    cols = {hs[0]: (0.94, 0.63, 0.38), hs[1]: (0.50, 0.75, 0.94)}
    rdMolDraw2D.PrepareAndDrawMolecule(d, m, highlightAtoms=hs, highlightAtomColors=cols, highlightBonds=[]); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))
f, ax = kanv(7.4, 3.0, (0, 30), (0, 12))
pan = [('CCC', [1], '(a) propana', 'ganti Hᵃ atau Hᵇ →\nsenyawa identik', 'homotopik: setara', HJ),
       ('CCO', [1], '(b) etanol', 'ganti Hᵃ atau Hᵇ →\nsepasang enansiomer', 'enantiotopik: setara\n(dalam pelarut akiral)', BIRU),
       ('C[C@@H](Cl)CC', [3], '(c) ($R$)-2-klorobutana', 'ganti Hᵃ atau Hᵇ →\nsepasang diastereomer', 'diastereotopik:\ntidak setara', JT)]
for i, (smi, hidx, tl, s1, s2, c) in enumerate(pan):
    cx = 5 + i * 10; ax.imshow(rdh(smi, hidx), extent=[cx - 4.4, cx + 4.4, 4.6, 11.3], zorder=2)
    T(ax, cx, 11.7, tl, fs=9, fontweight='bold'); T(ax, cx, 3.7, s1, fs=8); T(ax, cx, 1.3, s2, fs=8.5, c=c, fontweight='bold')
simpan(f, 'topik')

# 7. etil asetat
f, ax = plt.subplots(figsize=(7.2, 3.3), dpi=220)
ea = [{'d': 4.12, 'n': 2, 'kop': [(3, 7.1)], 'nama': 'kuartet', 'teks': 'OCH₂', 'iw': 0.42},
      {'d': 2.05, 'n': 3, 'teks': 'CH₃C=O\nsinglet'},
      {'d': 1.26, 'n': 3, 'kop': [(2, 7.1)], 'nama': 'triplet', 'teks': 'CH₃ (etil)', 'iw': 0.42}]
spektrum(ax, ea, (5.0, -0.2), judul='CH₃COOCH₂CH₃')
plt.tight_layout(); simpan(f, 'etilasetat')

# 8. pohon kopling (kuartet dan triplet)
f, ax = kanv(7.4, 3.8, (0, 30), (0, 15))
def spin(ax, x, y, ss, fs=9):
    for k, s in enumerate(ss): T(ax, x + (k - (len(ss) - 1) / 2) * 0.62, y, '↑' if s == 'a' else '↓', c=BIRU if s == 'a' else JT, fs=fs, fontweight='bold')
def pohon(ax, x0, n, judul, sub):
    T(ax, x0, 14.3, judul, fs=9.5, fontweight='bold'); T(ax, x0, 13.4, sub, fs=8)
    import itertools
    grup = {}
    for c in itertools.product('ab', repeat=n): grup.setdefault(c.count('b'), []).append(c)
    sp = 2.6; xs = {k: x0 + (k - n / 2) * sp for k in grup}
    for k, cs in grup.items():
        for j, c in enumerate(cs): spin(ax, xs[k], 11.8 - j * 0.9, c)
        ax.plot([xs[k], xs[k]], [1.6, 1.6 + 2.0 * len(cs)], color=TUA, lw=3); T(ax, xs[k], 0.9, str(len(cs)), fs=9, c=TUA)
    ax.plot([x0 - n / 2 * sp - 1, x0 + n / 2 * sp + 1], [1.6, 1.6], color='#999999', lw=0.8)
    ax.annotate('', (xs[0], 0.35), (xs[1], 0.35), arrowprops=dict(arrowstyle='<->', color=MERAH, lw=0.9)); T(ax, (xs[0] + xs[1]) / 2, -0.15, '$J$', c=MERAH, fs=9)
pohon(ax, 8.0, 3, 'sinyal CH₂ (3 tetangga)', 'keadaan spin ketiga H metil'); pohon(ax, 23.0, 2, 'sinyal CH₃ (2 tetangga)', 'keadaan spin kedua H metilena')
T(ax, 8.0, 0.0 - 0.9 + 0.3, '', fs=1)
simpan(f, 'pohon')

# 9. Pascal
f, ax = kanv(7.2, 3.6, (0, 30), (0, 15))
nm = ['singlet', 'doblet', 'triplet', 'kuartet', 'kuintet', 'sekstet', 'septet']
for n in range(7):
    y = 13.6 - n * 2.05; T(ax, 1.4, y + 0.35, f'n = {n}', fs=8.5); T(ax, 4.6, y + 0.35, nm[n], fs=8.5, c=BIRU)
    w = [comb(n, i) for i in range(n + 1)]; mx = max(w)
    for i, v in enumerate(w):
        x = 16 + (i - n / 2) * 1.5; ax.plot([x, x], [y - 0.5, y - 0.5 + 1.55 * v / mx], color=TUA, lw=2.4)
    T(ax, 26.0, y + 0.35, ' : '.join(map(str, w)), fs=8.2, c=JT)
simpan(f, 'pascal')

# 10. dd stirena
f, ax = kanv(7.4, 3.6, (0, 33), (0, 15.5))
Jt, Jc, Jg = 17.6, 10.9, 0.9; sc = 0.16
def dd(ax, x0, J1, J2, l1, l2, tl):
    T(ax, x0, 14.6, tl, fs=9, fontweight='bold'); ax.plot([x0, x0], [12.0, 13.6], color=TUA, lw=1.2)
    a = [x0 - J1 * sc / 2, x0 + J1 * sc / 2]
    for x in a: ax.plot([x0, x], [12.0, 10.2], color=TUA, lw=0.9); ax.plot([x, x], [10.2, 8.6], color=TUA, lw=0.9)
    T(ax, x0 + J1 * sc / 2 + 0.5, 11.3, l1, fs=7.8, c=JT, ha='left')
    for x in a:
        for s in (-1, 1): ax.plot([x, x + s * J2 * sc / 2], [8.6, 6.8], color=TUA, lw=0.9); ax.plot([x + s * J2 * sc / 2] * 2, [6.8, 4.8], color=BIRU, lw=2.4)
    T(ax, x0 + J1 * sc / 2 + J2 * sc / 2 + 0.5, 7.7, l2, fs=7.8, c=JT, ha='left')
pos = [(5.5, Jt, Jc, '$J_{ab}$ 17,6', '$J_{ac}$ 10,9', 'H$_a$  δ 6,72'), (16.5, Jt, Jg, '$J_{ab}$ 17,6', '$J_{bc}$ 0,9', 'H_b  δ 5,75'.replace('H_b', 'H$_b$')), (27.5, Jc, Jg, '$J_{ac}$ 10,9', '$J_{bc}$ 0,9', 'H$_c$  δ 5,24')]
for x0, J1, J2, l1, l2, tl in pos: dd(ax, x0, J1, J2, l1, l2, tl)
mol = Chem.MolFromSmiles('C=Cc1ccccc1')
d = rdMolDraw2D.MolDraw2DCairo(520, 300); o = d.drawOptions(); o.bondLineWidth = 3; o.fixedFontSize = 28; o.padding = 0.1
mH = Chem.AddHs(mol, onlyOnAtoms=(0, 1)); from rdkit.Chem import AllChem; AllChem.Compute2DCoords(mH)
hs = [a.GetIdx() for a in mH.GetAtoms() if a.GetSymbol() == 'H']
# H pada C1 = a; H pada C0: tentukan cis/trans terhadap Ha lewat koordinat
cf = mH.GetConformer(); P = lambda i: np.array([cf.GetAtomPosition(i).x, cf.GetAtomPosition(i).y])
ha = [h for h in hs if mH.GetAtomWithIdx(h).GetNeighbors()[0].GetIdx() == 1][0]; h0 = [h for h in hs if mH.GetAtomWithIdx(h).GetNeighbors()[0].GetIdx() == 0]
ax_ = P(1) - P(0); side = lambda i: np.sign(ax_[0] * (P(i) - P(0))[1] - ax_[1] * (P(i) - P(0))[0])
hc = [h for h in h0 if side(h) == side(ha)][0]; hb = [h for h in h0 if h != hc][0]
o.atomLabels[ha] = 'H<sub>a</sub>'; o.atomLabels[hb] = 'H<sub>b</sub>'; o.atomLabels[hc] = 'H<sub>c</sub>'
rdMolDraw2D.PrepareAndDrawMolecule(d, mH); d.FinishDrawing(); ax.imshow(Image.open(io.BytesIO(d.GetDrawingText())), extent=[11.0, 22.0, -0.4, 4.4], zorder=2)
T(ax, 5.0, 2.0, 'H$_b$: trans terhadap H$_a$\nH$_c$: cis terhadap H$_a$', fs=8.5, c=TUA)
simpan(f, 'dd')

# 11. etanol dan D2O
f, (a1, a2) = plt.subplots(2, 1, figsize=(7.2, 4.6), dpi=220)
et = [{'d': 3.69, 'n': 2, 'kop': [(3, 7.0)], 'nama': 'kuartet', 'teks': 'CH₂O', 'iw': 0.5},
      {'d': 2.60, 'n': 1, 'w': 14, 'teks': 'OH (s lebar)'},
      {'d': 1.22, 'n': 3, 'kop': [(2, 7.0)], 'nama': 'triplet', 'teks': 'CH₃', 'iw': 0.5}]
spektrum(a1, et, (5.2, -0.2), judul='etanol, CDCl₃')
et2 = [et[0], {'d': 4.70, 'n': 1, 'w': 8, 'teks': 'HOD'}, et[2]]
spektrum(a2, et2, (5.2, -0.2), judul='setelah dikocok dengan D₂O', integ=False)
a2.annotate('OH hilang', (2.6, 0.05), (2.6, 0.7), ha='center', fontsize=8, color=MERAH, arrowprops=dict(arrowstyle='-|>', color=MERAH, lw=0.9))
plt.tight_layout(h_pad=1.2); simpan(f, 'd2o')

# 12. propan-1-ol dan propan-2-ol
f, (a1, a2) = plt.subplots(2, 1, figsize=(7.2, 4.8), dpi=220)
p1 = [{'d': 3.58, 'n': 2, 'kop': [(2, 6.7)], 'nama': 'triplet', 'teks': 'CH₂O', 'iw': 0.42},
      {'d': 2.20, 'n': 1, 'w': 14, 'teks': 'OH', 'ty': 0.42},
      {'d': 1.57, 'n': 2, 'kop': [(5, 7.0)], 'nama': 'sekstet', 'teks': 'CH₂', 'iw': 0.5, 'ix': 1.78},
      {'d': 0.94, 'n': 3, 'kop': [(2, 7.4)], 'nama': 'triplet', 'teks': 'CH₃', 'iw': 0.42, 'ix': 0.80}]
spektrum(a1, p1, (4.6, -0.2), judul='propan-1-ol')
p2 = [{'d': 4.02, 'n': 1, 'kop': [(6, 6.1)], 'nama': 'septet', 'teks': 'CHO', 'iw': 0.5},
      {'d': 2.00, 'n': 1, 'w': 14, 'teks': 'OH', 'ty': 0.42},
      {'d': 1.20, 'n': 6, 'kop': [(1, 6.1)], 'nama': 'doblet', 'teks': '(CH₃)₂', 'iw': 0.42}]
spektrum(a2, p2, (4.6, -0.2), judul='propan-2-ol')
plt.tight_layout(h_pad=1.2); simpan(f, 'propanol')

# 13. peta geseran 13C
f, ax = plt.subplots(figsize=(7.2, 3.0), dpi=220)
rows = [('C=O keton', 200, 220, MERAH), ('C=O aldehida', 190, 205, MERAH), ('C=O asam, ester, amida', 160, 185, JT), ('C aromatik', 110, 160, '#7b3294'),
        ('C=C alkena', 100, 150, '#7b3294'), ('C≡N', 115, 125, HJ), ('C≡C', 65, 90, JG), ('C–O', 50, 90, BIRU), ('C–N', 30, 60, HJ), ('C–Cl, C–Br', 25, 65, HJ), ('alkil', 5, 45, TUA)]
for i, (n, a, b, c) in enumerate(rows):
    y = len(rows) - i; ax.barh(y, b - a, left=a, height=0.62, color=c); ax.text(b + 3, y, n, ha='right', va='center', fontsize=7.8, color=TUA)
ax.set_xlim(225, -5); ax.set_ylim(0.3, len(rows) + 0.7); ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.set_xlabel('δ (ppm)')
plt.tight_layout(); simpan(f, 'karbon')

# 14. DEPT butan-2-on
f, axs = plt.subplots(3, 1, figsize=(7.2, 4.4), dpi=220, sharex=True)
C = [(209.3, 0.35, 'C', 'C=O'), (36.9, 1.0, 'CH2', 'CH₂'), (29.4, 0.95, 'CH3', 'CH₃C=O'), (7.9, 0.9, 'CH3', 'CH₃')]
for ax, (tl, rule) in zip(axs, [('¹³C (pemisahan proton)', lambda t: 1), ('DEPT-135', lambda t: {'C': 0, 'CH': 1, 'CH2': -1, 'CH3': 1}[t]), ('DEPT-90', lambda t: 1 if t == 'CH' else 0)]):
    ax.axhline(0, color='#bbbbbb', lw=0.7)
    for d, h, t, lab in C:
        s = rule(t)
        if s: ax.plot([d, d], [0, s * h], color=TUA if s > 0 else MERAH, lw=2.2)
        if tl.startswith('¹³C'): ax.text(d + {36.9: 1.5, 29.4: -1.5}.get(d, 0), h + 0.08, f'{koma(d)}\n{lab}', ha={36.9: 'right', 29.4: 'left'}.get(d, 'center'), va='bottom', fontsize=7.2, color=TUA)
    ax.text(170, 1.2, tl, fontsize=9, color=TUA, fontweight='bold', va='top'); ax.set_ylim(-1.25, 1.65); ax.set_yticks([]); ax.spines['left'].set_visible(False)
axs[1].text(36.9 + 4, -0.9, 'CH₂ ke bawah', fontsize=7.5, color=MERAH, ha='right'); axs[1].text(209.3, 0.25, 'C=O hilang', fontsize=7.5, color='#777777', ha='center')
axs[2].text(110, 0.3, 'tidak ada CH: kosong', fontsize=8, color='#777777', ha='center')
axs[2].set_xlim(225, -5); axs[2].set_xlabel('δ (ppm)'); plt.tight_layout(h_pad=0.4); simpan(f, 'dept')

# 15. gabung: dua keton aromatik
f, (a1, a2) = plt.subplots(2, 1, figsize=(7.2, 4.8), dpi=220)
Y = [{'d': 7.96, 'n': 2, 'kop': [(1, 7.6)], 'nama': 'd', 'iw': 0.55, 'ix': 8.3, 'lx': 8.15},
     {'d': 7.55, 'n': 1, 'kop': [(2, 7.4)], 'nama': 't', 'iw': 0.55, 'ix': 7.55, 'lx': 7.62},
     {'d': 7.45, 'n': 2, 'kop': [(2, 7.6)], 'nama': 't', 'iw': 0.55, 'ix': 6.8, 'lx': 7.1},
     {'d': 2.99, 'n': 2, 'kop': [(3, 7.2)], 'nama': 'kuartet', 'iw': 0.55},
     {'d': 1.22, 'n': 3, 'kop': [(2, 7.2)], 'nama': 'triplet', 'iw': 0.55}]
spektrum(a1, Y, (8.8, -0.2), judul='Y,  C₉H₁₀O')
Z = [{'d': 7.30, 'n': 5, 'kop': [(2, 1.5)], 'w': 6, 'lab': '5H'}, {'d': 3.69, 'n': 2, 'lab': '2H'}, {'d': 2.15, 'n': 3, 'lab': '3H'}]
spektrum(a2, Z, (8.8, -0.2), judul='Z,  C₉H₁₀O', inset=False)
plt.tight_layout(h_pad=1.2); simpan(f, 'gabung')
print('selesai')
