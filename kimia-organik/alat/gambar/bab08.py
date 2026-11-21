# Gambar Bab 8: kalor hidrogenasi, mekanisme HBr, diagram Markovnikov, hidroborasi, bromonium,
# hidrogenasi, dihidroksilasi, ozonolisis, propagasi radikal, keasaman alkuna, Lindlar/Na-NH3, tautomer, peta
import os, io, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle
from scipy.interpolate import CubicSpline, PchipInterpolator
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang, ukuran_px
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab08/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
koma = lambda v: f'{v:g}'.replace('.', ',')

def T(ax, x, y, s, c=TUA, fs=11, **k): ax.text(x, y, s, ha='center', va='center', color=c, fontsize=fs, **k)
def garis(ax, p, q, c=TUA, lw=1.8, sh=(0.0, 0.0), off=0.0):
    p, q = np.array(p, float), np.array(q, float); d = q - p; u = d / np.linalg.norm(d); n = np.array([-u[1], u[0]])
    a, b = p + u * sh[0] + n * off, q - u * sh[1] + n * off; ax.plot(*zip(a, b), color=c, lw=lw)
def panah(ax, p, q, rad=0.4, c=MERAH, lw=1.4):
    ax.add_patch(FancyArrowPatch(p, q, connectionstyle=f'arc3,rad={rad}', arrowstyle='-|>', mutation_scale=11, color=c, lw=lw))
def reaksi(ax, x1, x2, y, t='', c=TUA, t2='', fs=8.5):
    ax.annotate('', (x2, y), (x1, y), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.3))
    if t: T(ax, (x1 + x2) / 2, y + 0.32, t, fs=fs)
    if t2: T(ax, (x1 + x2) / 2, y - 0.32, t2, fs=fs)
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def rd(smi, w=360, h=300, fs=30, hs=(), pad=0.18, bl=None):
    m = Chem.MolFromSmiles(smi)
    if hs: m = Chem.AddHs(m, onlyOnAtoms=tuple(hs))
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = pad
    if bl: o.fixedBondLength = bl
    o.updateAtomPalette({35: (0.71, 0.33, 0.11), 8: (0.71, 0.33, 0.11), 5: (0.11, 0.46, 0.74), 1: (0.05, 0.15, 0.28)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def gb(ax, smi, x0, x1, y0, y1, **k):
    k['w'], k['h'] = ukuran_px(ax, x0, x1, y0, y1); k['fs'] = min(k.get('fs', 25), 25); k.setdefault('bl', 30)
    pasang(ax, rd(smi, **k), x0, x1, y0, y1, maks=1.0)

# 1. kalor hidrogenasi butena (sumbu terputus: hanya selisih yang penting)
f, ax = plt.subplots(figsize=(6.0, 3.4), dpi=220)
dat = [('but-1-ena', 127, JG), ('cis-but-2-ena', 120, BIRU), ('trans-but-2-ena', 116, HJ)]
y0 = 104
for i, (nm, v, c) in enumerate(dat):
    x = i * 1.6
    ax.plot([x + 0.5, 3.75], [v, v], color=c, lw=0.7, ls=':'); ax.plot([x - 0.5, x + 0.5], [v, v], color=c, lw=3); ax.text(x, v + 0.8, nm, ha='center', fontsize=9, color=TUA)
    ax.annotate('', (x, y0 + 0.4), (x, v - 0.4), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.4))
    ax.text(x + 0.08, (v + y0) / 2 + 1.5, f'ΔH° = −{v}', ha='left', fontsize=8.5, color=c)
ax.plot([-0.7, 3.9], [y0, y0], color=TUA, lw=3); ax.text(1.6, y0 - 1.6, 'butana (+ H₂ sudah bereaksi)', ha='center', fontsize=9, color=TUA)
for xb in (-0.2, 1.4, 3.0): ax.text(xb, (y0 + 109) / 2, '≈', fontsize=14, color='#888888', ha='center', va='center', rotation=90)
for a_, b_ in [(127, 120), (120, 116)]:
    ax.annotate('', (3.85, b_), (3.85, a_), arrowprops=dict(arrowstyle='<->', color=TUA, lw=1))
    ax.text(3.95, (a_ + b_) / 2, f'{a_ - b_} kJ', fontsize=8.5, va='center', color=TUA)
ax.plot([3.85, 3.85], [116, 127], alpha=0)
ax.set_xlim(-0.8, 4.6); ax.set_ylim(101, 130); ax.axis('off')
plt.tight_layout(); f.savefig(f'{F}/hidro.png', bbox_inches='tight'); plt.close(f)

# 2. mekanisme HBr + 2-metilpropena
f, ax = kanv(7.6, 2.3, (0, 23), (-2.2, 2.6))
def isobut(ax, x, y, kation=False, br=False):
    T(ax, x, y, 'C', fs=12)
    for dx, dy in [(-1.0, 0.75), (-1.0, -0.75)]:
        garis(ax, (x, y), (x + dx, y + dy), sh=(0.25, 0.35)); T(ax, x + dx - 0.25, y + dy, 'H₃C', fs=10)
    if kation:
        garis(ax, (x, y), (x + 1.3, y), sh=(0.25, 0.4)); T(ax, x + 1.75, y, 'CH₃', fs=10); T(ax, x + 0.05, y + 0.45, '+', fs=12, c=MERAH)
    elif br:
        garis(ax, (x, y), (x + 1.3, y), sh=(0.25, 0.4)); T(ax, x + 1.75, y, 'CH₃', fs=10)
        garis(ax, (x, y), (x, y - 1.1), sh=(0.38, 0.3)); T(ax, x, y - 1.4, 'Br', fs=11, c=JT)
    else:
        garis(ax, (x, y), (x + 1.3, y), sh=(0.25, 0.4), off=0.07); garis(ax, (x, y), (x + 1.3, y), sh=(0.25, 0.4), off=-0.07); T(ax, x + 1.75, y, 'CH₂', fs=10)
isobut(ax, 2.2, 0)
T(ax, 5.3, 1.2, 'H', fs=11, c=BIRU); garis(ax, (5.3, 1.2), (6.5, 1.2), sh=(0.25, 0.3)); T(ax, 6.85, 1.2, 'Br', fs=11, c=JT)
panah(ax, (2.85, 0.15), (5.15, 1.0), rad=-0.35); panah(ax, (5.9, 1.35), (6.8, 1.55), rad=-0.6)
reaksi(ax, 7.6, 9.0, 0, 'lambat')
isobut(ax, 11.0, 0, kation=True); T(ax, 14.6, 0.9, 'Br$^-$', fs=11, c=JT)
panah(ax, (14.3, 0.75), (11.25, 0.35), rad=0.35)
reaksi(ax, 15.4, 16.8, 0, 'cepat')
isobut(ax, 19.0, 0.4, br=True)
T(ax, 3.0, -1.8, 'elektron π menyerang H', fs=8.2, c=HJ); T(ax, 11.6, -1.8, 'karbokation tersier', fs=8.2, c=HJ); T(ax, 19.6, -1.9, '2-bromo-2-metilpropana', fs=8.2, c=HJ)
f.savefig(f'{F}/hbr.png', bbox_inches='tight'); plt.close(f)

# 3. diagram energi dua arah protonasi
f, ax = plt.subplots(figsize=(6.0, 3.4), dpi=220)
X = [0, 1.0, 2.2, 3.2, 4.4]
for Y, c, lab in [([1.0, 1.05, 6.4, 4.6, 4.8], JG, 'via karbokation primer'), ([1.0, 1.05, 4.2, 2.3, 2.5], BIRU, 'via karbokation tersier')]:
    xx = np.linspace(0, 3.2, 300); yy = PchipInterpolator(X[:4], Y[:4])(xx); ax.plot(xx, yy, color=c, lw=2.2, label=lab)
    xx2 = np.linspace(3.2, 4.8, 200); yy2 = CubicSpline([3.2, 3.7, 4.8], [Y[3], Y[3] + 0.5, 0.2], bc_type='clamped')(xx2); ax.plot(xx2, yy2, color=c, lw=2.2, ls=(0, (4, 2)))
ax.text(2.2, 6.65, '‡', ha='center', fontsize=12, color=JT); ax.text(2.2, 4.45, '‡', ha='center', fontsize=12, color=BIRU)
ax.text(3.2, 4.15, '(CH₃)₂CHCH₂$^+$', ha='center', fontsize=8.5, color=JT); ax.text(3.2, 1.75, '(CH₃)₃C$^+$', ha='center', fontsize=8.5, color=BIRU)
ax.text(0.1, 1.35, 'alkena + HBr', fontsize=8.5, color=TUA)
ax.annotate('', (1.65, 4.2), (1.65, 6.4), arrowprops=dict(arrowstyle='<->', color=TUA, lw=0.9)); ax.text(1.55, 5.3, 'beda\nbesar', ha='right', fontsize=8, color=TUA, va='center')
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('Koordinat reaksi'); ax.set_ylabel('Energi'); ax.set_ylim(0, 7.3)
ax.legend(frameon=False, fontsize=8, loc='upper right')
plt.tight_layout(); f.savefig(f'{F}/markov.png', bbox_inches='tight'); plt.close(f)

# 4. hidroborasi-oksidasi 1-metilsiklopentena
f, ax = kanv(7.6, 2.0, (0, 23), (0, 6))
gb(ax, 'CC1=CCCC1', 0, 4.4, 0.6, 5.4)
reaksi(ax, 4.6, 7.4, 3.0, 'BH₃·THF', t2='adisi syn')
m_b = 'C[C@H]1CCC[C@@H]1[BH2]'; gb(ax, m_b, 7.6, 12.6, 0.4, 5.6, hs=(1,))
reaksi(ax, 12.8, 15.8, 3.0, 'H₂O₂, NaOH', t2='retensi')
gb(ax, 'C[C@H]1CCC[C@@H]1O', 16.0, 21.0, 0.4, 5.6, hs=(1,))
T(ax, 10.1, 0.15, 'H dan B di sisi yang sama', fs=8, c=HJ); T(ax, 18.5, 0.15, 'trans-2-metilsiklopentanol', fs=8, c=HJ)
T(ax, 22.2, 3.0, '+ enan-\nsiomer', fs=8)
f.savefig(f'{F}/hidroborasi.png', bbox_inches='tight'); plt.close(f)

# 5. bromonium
f, ax = kanv(7.6, 2.0, (0, 23), (0, 6))
gb(ax, 'C1=CCCC1', 0, 4.0, 0.8, 5.2)
reaksi(ax, 4.2, 6.6, 3.0, 'Br₂')
gb(ax, 'C1C[C@@H]2[Br+][C@@H]2C1', 6.8, 11.6, 0.5, 5.5, hs=(2, 4))
T(ax, 12.9, 1.1, 'Br$^-$', fs=11, c=JT); panah(ax, (12.5, 1.35), (10.7, 2.2), rad=-0.35)
T(ax, 13.0, 0.25, 'dari belakang', fs=7.5, c=HJ)
reaksi(ax, 13.6, 15.6, 3.0)
gb(ax, 'Br[C@@H]1CCC[C@H]1Br', 15.8, 20.6, 0.5, 5.5)
T(ax, 9.2, 0.1, 'ion bromonium', fs=8, c=HJ); T(ax, 18.2, 0.1, 'trans-1,2-dibromosiklopentana', fs=8, c=HJ)
T(ax, 22.0, 3.0, '+ enan-\nsiomer', fs=8)
f.savefig(f'{F}/bromonium.png', bbox_inches='tight'); plt.close(f)

# 6. hidrogenasi di permukaan logam
f, ax = kanv(7.4, 2.6, (0, 22), (-1.6, 5.4))
for x in np.arange(0.5, 10.6, 0.8): ax.add_patch(Circle((x, -0.6), 0.38, fc=MUDA, ec=BIRU, lw=0.8))
T(ax, 5.5, -1.35, 'permukaan logam (Pd, Pt, Ni)', fs=8, c=BIRU)
for x in [1.3, 2.9, 7.3, 8.9]: ax.add_patch(Circle((x, 0.05), 0.2, fc='white', ec=TUA, lw=1)); T(ax, x, 0.05, 'H', fs=7)
# alkena datar di atas permukaan
cx = 5.1; ax.plot([cx - 0.8, cx + 0.8], [1.5, 1.5], color=TUA, lw=1.8); ax.plot([cx - 0.8, cx + 0.8], [1.68, 1.68], color=TUA, lw=1.8)
for sx in (-1, 1):
    for dy in (0.55, -0.15): garis(ax, (cx + sx * 0.8, 1.59), (cx + sx * 1.6, 1.59 + dy), lw=1.5)
T(ax, cx, 2.75, 'alkena menempel dengan satu sisinya', fs=8, c=HJ)
ax.annotate('', (cx - 0.8, 1.3), (2.9, 0.3), arrowprops=dict(arrowstyle='-|>', color=MERAH, lw=1.2, connectionstyle='arc3,rad=-0.2'))
ax.annotate('', (cx + 0.8, 1.3), (7.3, 0.3), arrowprops=dict(arrowstyle='-|>', color=MERAH, lw=1.2, connectionstyle='arc3,rad=0.2'))
T(ax, 5.1, 3.7, 'kedua H masuk dari bawah (syn)', fs=8.5, c=MERAH)
gb(ax, 'CC1=C(C)CCCC1', 11.2, 15.0, 0.4, 4.6)
reaksi(ax, 15.1, 17.4, 2.5, 'H₂, Pd/C')
gb(ax, 'C[C@@H]1CCCC[C@@H]1C', 17.5, 21.9, 0.2, 4.8, hs=(1, 6))
T(ax, 19.7, -0.3, 'cis (meso)', fs=8, c=HJ)
f.savefig(f'{F}/hidrogenasi.png', bbox_inches='tight'); plt.close(f)

# 7. dihidroksilasi syn dan anti
f, ax = kanv(7.6, 3.6, (0, 23), (0, 11))
gb(ax, 'C1=CCCCC1', 0, 4.2, 3.4, 7.6)
ax.annotate('', (7.6, 8.6), (4.3, 6.4), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 4.6, 8.9, 'OsO₄ (kat.), NMO', fs=8.5)
gb(ax, 'O[C@@H]1CCCC[C@@H]1O', 7.8, 12.4, 6.3, 10.9, hs=(1, 6))
T(ax, 15.6, 8.6, 'cis-diol (syn, meso)', fs=9, c=HJ)
ax.annotate('', (7.6, 2.4), (4.3, 4.6), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 5.3, 2.7, 'mCPBA', fs=8.5)
gb(ax, 'C1CC[C@@H]2O[C@@H]2C1', 7.4, 11.6, 0.2, 4.6, hs=(3, 5))
reaksi(ax, 12.0, 15.2, 2.4, 'H₃O$^+$', t2='dari belakang')
gb(ax, 'O[C@@H]1CCCC[C@H]1O', 15.4, 20.0, 0.1, 4.7, hs=(1, 6))
T(ax, 21.6, 2.4, 'trans-diol\n(anti, rasemat)', fs=9, c=HJ)
f.savefig(f'{F}/diol.png', bbox_inches='tight'); plt.close(f)

# 8. ozonolisis
f, ax = kanv(7.6, 4.0, (0, 23), (0, 12))
gb(ax, 'CC(C)=CCC', 0, 3.2, 7.0, 11.0)
reaksi(ax, 3.5, 5.5, 9.0, 'O₃, −78 °C')
gb(ax, 'CCC1OOOC1(C)C', 5.6, 9.6, 6.8, 11.2); T(ax, 7.6, 6.6, 'molozonida', fs=8, c=HJ)
reaksi(ax, 9.7, 11.1, 9.0)
gb(ax, 'CC(C)=[O+][O-]', 11.2, 14.4, 7.0, 11.0); T(ax, 14.8, 9.0, '+', fs=12); gb(ax, 'CCC=O', 15.1, 17.7, 7.4, 10.6)
T(ax, 14.4, 6.6, 'karbonil oksida + aldehida', fs=8, c=HJ)
reaksi(ax, 17.8, 19.0, 9.0)
gb(ax, 'CCC1OC(C)(C)OO1', 19.1, 23.0, 6.8, 11.2); T(ax, 21.0, 6.6, 'ozonida', fs=8, c=HJ)
# baris bawah: ringkasan
gb(ax, 'CC(C)=CCC', 2.0, 6.4, 0.6, 5.2)
ax.plot([4.0, 4.0], [1.0, 4.8], color=MERAH, lw=1.2, ls=(0, (3, 2)))
reaksi(ax, 6.8, 11.2, 2.9, '(1) O₃; (2) (CH₃)₂S', fs=8.5)
gb(ax, 'CC(C)=O', 11.6, 14.8, 1.0, 4.8); T(ax, 15.6, 2.9, '+', fs=12); gb(ax, 'CCC=O', 16.3, 19.5, 1.0, 4.8)
T(ax, 13.2, 0.6, 'aseton', fs=8.5, c=HJ); T(ax, 17.9, 0.6, 'propanal', fs=8.5, c=HJ); T(ax, 4.2, 0.4, 'potong di C=C', fs=8, c=MERAH)
f.savefig(f'{F}/ozon.png', bbox_inches='tight'); plt.close(f)

# 9. propagasi radikal HX
f, ax = plt.subplots(figsize=(5.6, 3.2), dpi=220)
X = np.arange(3); s1 = [267 - 350, 267 - 294, 267 - 239]; s2 = [432 - 413, 366 - 413, 298 - 413]
ax.bar(X - 0.18, s1, 0.34, color=BIRU, label='propagasi 1: X· + C=C'); ax.bar(X + 0.18, s2, 0.34, color=JG, label='propagasi 2: C· + HX')
for xi, v in list(zip(X - 0.18, s1)) + list(zip(X + 0.18, s2)): ax.text(xi, v + (4 if v > 0 else -10), f'{v:+d}'.replace('-', '−'), ha='center', fontsize=8)
ax.axhline(0, color=TUA, lw=0.8); ax.set_xticks(X); ax.set_xticklabels(['HCl', 'HBr', 'HI']); ax.set_ylabel('ΔH° (kJ mol$^{-1}$)'); ax.set_ylim(-135, 50)
ax.add_patch(FancyBboxPatch((0.6, -128), 0.8, 172, boxstyle='round,pad=0.02', fc='none', ec=HJ, lw=1.2, ls='--'))
ax.legend(frameon=False, fontsize=7.8, loc='lower left')
plt.tight_layout(); f.savefig(f'{F}/radikal.png', bbox_inches='tight'); plt.close(f)

# 10. keasaman dan sifat s
f, ax = plt.subplots(figsize=(5.6, 3.0), dpi=220)
nm = ['etana\n(sp³, 25% s)', 'etena\n(sp², 33% s)', 'etuna\n(sp, 50% s)', 'amonia', 'air']; pk = [50, 44, 25, 38, 15.7]; cl = [MUDA, BIRU, TUA, '#b0b0b0', '#b0b0b0']
ax.bar(range(5), pk, color=cl, width=0.6)
for i, v in enumerate(pk): ax.text(i, v + 1.2, koma(v), ha='center', fontsize=8.5)
ax.set_xticks(range(5)); ax.set_xticklabels(nm, fontsize=8); ax.set_ylabel('pKa'); ax.set_ylim(0, 57)
ax.axvline(2.5, color='#999999', lw=0.8, ls=':'); ax.text(3.5, 54, 'pembanding', ha='center', fontsize=8, color='#777777')
plt.tight_layout(); f.savefig(f'{F}/asetilida.png', bbox_inches='tight'); plt.close(f)

# 11. Lindlar lawan Na/NH3
f, ax = kanv(7.0, 3.2, (0, 21), (0, 9.6))
gb(ax, 'CC#CCC', 0, 4.8, 2.8, 6.8)
ax.annotate('', (10.0, 7.3), (5.0, 5.4), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 6.6, 7.2, 'H₂, katalis Lindlar', fs=8.5)
ax.annotate('', (10.0, 2.3), (5.0, 4.2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 6.6, 2.3, 'Na, NH₃ cair', fs=8.5)
gb(ax, 'C/C=C\\CC', 10.2, 15.0, 5.0, 9.6, hs=(1, 2)); T(ax, 17.9, 7.3, '(Z)-pent-2-ena\nadisi syn', fs=9, c=HJ)
gb(ax, 'C/C=C/CC', 10.2, 15.0, 0.0, 4.6, hs=(1, 2)); T(ax, 17.9, 2.3, '(E)-pent-2-ena\nlewat radikal vinil', fs=9, c=JT)
f.savefig(f'{F}/lindlar.png', bbox_inches='tight'); plt.close(f)

# 12. dua cara hidrasi heks-1-una dan tautomerisasi
f, ax = kanv(7.6, 3.4, (0, 23), (0, 10.4))
gb(ax, 'C#CCCCC', 0, 4.2, 3.2, 7.2)
for y, enol, karb, t1, t2, c in [(7.9, 'C=C(O)CCCC', 'CC(=O)CCCC', 'H₂O, H₂SO₄, HgSO₄', 'heksan-2-on', HJ),
                                  (2.5, 'OC=CCCCC', 'O=CCCCCC', '(1) 9-BBN; (2) H₂O₂, NaOH', 'heksanal', JT)]:
    ax.annotate('', (7.0, y), (4.4, 5.2 + (0.6 if y > 5 else -0.6)), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3))
    T(ax, 5.3, y + (0.9 if y > 5 else -0.9), t1, fs=8.2)
    gb(ax, enol, 7.1, 11.9, y - 2.3, y + 2.3); T(ax, 9.5, y + 1.35 if y > 5 else y - 1.35, 'enol', fs=8, c=BIRU)
    ax.annotate('', (15.0, y + 0.15), (12.2, y + 0.15), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.2)); ax.annotate('', (12.2, y - 0.15), (13.6, y - 0.15), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=0.8))
    T(ax, 13.6, y + 0.65, 'tautomerisasi', fs=7.5)
    gb(ax, karb, 15.2, 20.0, y - 2.3, y + 2.3); T(ax, 21.6, y, t2, fs=9, c=c)
f.savefig(f'{F}/tautomer.png', bbox_inches='tight'); plt.close(f)

# 13. peta reaksi alkena
f, ax = kanv(7.6, 6.2, (-12.5, 12.5), (-10.2, 10.2))
ax.add_patch(FancyBboxPatch((-1.9, -0.8), 3.8, 1.6, boxstyle='round,pad=0.25', fc=TUA, ec=TUA)); T(ax, 0, 0, 'ALKENA\nC=C', c='white', fs=11, fontweight='bold')
item = [('alkana', 'H₂, Pd/C', 'syn', HJ), ('haloalkana', 'HX', 'Markovnikov', BIRU), ('haloalkana', 'HBr, ROOR', 'anti-Markovnikov', JT),
        ('alkohol', 'H₃O$^+$ atau Hg(OAc)₂', 'Markovnikov', BIRU), ('alkohol', 'BH₃; H₂O₂, NaOH', 'anti-Markovnikov, syn', JT),
        ('dihalida 1,2', 'X₂', 'anti', HJ), ('halohidrin', 'X₂, H₂O', 'anti', HJ), ('epoksida', 'mCPBA', 'syn', HJ),
        ('diol 1,2', 'OsO₄, NMO', 'syn', HJ), ('diol 1,2', 'mCPBA; H₃O$^+$', 'anti', HJ), ('aldehida/keton', 'O₃; (CH₃)₂S', 'C=C putus', TUA), ('polimer', 'inisiator radikal', 'pertumbuhan rantai', TUA)]
n = len(item)
for i, (p, r, s, c) in enumerate(item):
    th = np.pi / 2 - 2 * np.pi * i / n; x, y = 9.0 * np.cos(th), 7.6 * np.sin(th)
    ax.annotate('', (x * 0.74, y * 0.80), (x * 0.24, y * 0.14), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.2))
    ax.add_patch(FancyBboxPatch((x - 1.95, y - 0.95), 3.9, 1.9, boxstyle='round,pad=0.12', fc='white', ec=c, lw=1.1))
    T(ax, x, y + 0.5, p, c=c, fs=8.6, fontweight='bold'); T(ax, x, y - 0.05, r, fs=6.9); T(ax, x, y - 0.55, s, fs=6.4, c='#555555')
f.savefig(f'{F}/peta.png', bbox_inches='tight'); plt.close(f)
print('ok')
