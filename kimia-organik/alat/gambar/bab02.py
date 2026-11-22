# Gambar Bab 2: gugus alkil, contoh nama IUPAC
import os, io, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab02/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'

def gbr(smi, sorot=(), w=420, h=300):
    m = Chem.MolFromSmiles(smi)
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions()
    o.bondLineWidth = 2; o.fixedFontSize = 28; o.padding = 0.15; o.dummiesAreAttachments = True
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.1, 0.54, 0.42), 35: (0.55, 0.2, 0.1)})
    at = [a.GetIdx() for p in sorot for t in m.GetSubstructMatches(Chem.MolFromSmarts(p)) for a in [m.GetAtomWithIdx(i) for i in t]]
    rdMolDraw2D.PrepareAndDrawMolecule(d, m, highlightAtoms=at, highlightAtomColors={i: (0.5, 0.75, 0.94) for i in at},
                                       highlightBonds=[b.GetIdx() for b in m.GetBonds() if b.GetBeginAtomIdx() in at and b.GetEndAtomIdx() in at],
                                       highlightBondColors={b.GetIdx(): (0.5, 0.75, 0.94) for b in m.GetBonds()})
    d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))

def lembar(daftar, nama, kol, ukuran):
    baris = (len(daftar) + kol - 1) // kol
    f, ax = plt.subplots(baris, kol, figsize=ukuran, dpi=220)
    for a in ax.flat: a.axis('off')
    for a, (s, t, sor) in zip(ax.flat, daftar):
        a.imshow(gbr(s, sor)); a.set_title(t, fontsize=9.5, color=TUA, y=-0.14)
    plt.tight_layout(); f.savefig(f'{F}/{nama}', bbox_inches='tight'); plt.close(f)

lembar([('*CCC', 'propil', ()), ('*C(C)C', 'isopropil (1-metiletil)', ()), ('*CCCC', 'butil', ()),
        ('*C(C)CC', 'sec-butil (1-metilpropil)', ()), ('*CC(C)C', 'isobutil (2-metilpropil)', ()), ('*C(C)(C)C', 'tert-butil (1,1-dimetiletil)', ())],
       'alkil.png', 3, (7.4, 4.4))
lembar([('CC=CC(O)C', 'pent-3-en-2-ol', ('[OX2H]',)), ('CC(=O)CC(O)C', '4-hidroksipentan-2-on', ('[CX3](=O)',)),
        ('ClCCCC(=O)O', 'asam 4-klorobutanoat', ('C(=O)[OH]',)), ('OCCC(N)C=O', '2-amino-4-hidroksibutanal', ('[CX3H1](=O)',)),
        ('CC(=O)OCC', 'etil etanoat', ('C(=O)O',)), ('CCC(C)N', 'butan-2-amina', ('[NX3H2]',))],
       'contoh.png', 3, (7.4, 4.4))
print('ok')

# ================= gambar tambahan =================
import numpy as np
from matplotlib.patches import FancyBboxPatch
def gbrn(smi, notes=None, hl=(), hlc=None, w=440, h=300, bl=None, fs=26):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions()
    o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = 0.15; o.annotationFontScale = 0.75
    if bl: o.fixedBondLength = bl
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.1, 0.54, 0.42), 35: (0.55, 0.2, 0.1), 16: (0.72, 0.53, 0.04)})
    for i, t in (notes or {}).items(): m.GetAtomWithIdx(i).SetProp('atomNote', t)
    hl = list(hl); col = hlc or {}
    hb = [b.GetIdx() for b in m.GetBonds() if b.GetBeginAtomIdx() in hl and b.GetEndAtomIdx() in hl]
    rdMolDraw2D.PrepareAndDrawMolecule(d, m, highlightAtoms=hl, highlightBonds=hb, highlightAtomColors={i: col.get(i, (0.5, 0.75, 0.94)) for i in hl},
                                       highlightBondColors={b: col.get(m.GetBondWithIdx(b).GetBeginAtomIdx(), (0.5, 0.75, 0.94)) for b in hb})
    d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def sorot(smi, smarts):
    m = Chem.MolFromSmiles(smi); return [i for p in smarts for t in m.GetSubstructMatches(Chem.MolFromSmarts(p)) for i in t]
def grid(items, nama, kol, ukuran, fs_t=9):
    baris = (len(items) + kol - 1) // kol
    f, ax = plt.subplots(baris, kol, figsize=ukuran, dpi=220)
    for a in np.atleast_1d(ax).flat: a.axis('off')
    for a, (img, t) in zip(np.atleast_1d(ax).flat, items):
        a.imshow(img); a.set_title(t, fontsize=fs_t, color=TUA, y=-0.16)
    plt.tight_layout(); f.savefig(f'{F}/{nama}', bbox_inches='tight'); plt.close(f)

# 3. galeri gugus fungsi
G = [('C=C', 'alkena', ['C=C']), ('C#C', 'alkuna', ['C#C']), ('c1ccccc1', 'arena', ['c']), ('CCCl', 'haloalkana', ['[Cl]']),
     ('CCO', 'alkohol', ['[OX2H]']), ('Oc1ccccc1', 'fenol', ['[OX2H]']), ('CCOCC', 'eter', ['[OD2]([#6])[#6]']), ('CCN', 'amina', ['[NX3]']),
     ('CCC=O', 'aldehida', ['[CX3H1]=O']), ('CC(C)=O', 'keton', ['[#6][CX3](=O)[#6]']), ('CC(=O)O', 'asam karboksilat', ['C(=O)[OH]']),
     ('CC(=O)OC', 'ester', ['C(=O)O[#6]']), ('CC(N)=O', 'amida', ['C(=O)N']), ('CC#N', 'nitril', ['C#N']), ('CCS', 'tiol', ['[SX2H]'])]
grid([(gbrn(s, hl=sorot(s, p), bl=70, fs=32, w=420, h=300), t) for s, t, p in G], 'gugus.png', 5, (7.4, 5.0))

# 4. parasetamol dengan gugus berwarna
s = 'CC(=O)Nc1ccc(O)cc1'; am = sorot(s, ['C(=O)N']); fe = sorot(s, ['[OX2H]']); ar = sorot(s, ['c'])
col = {**{i: (0.94, 0.63, 0.38) for i in am}, **{i: (0.5, 0.75, 0.94) for i in fe}, **{i: (0.72, 0.88, 0.80) for i in ar}}
f, ax = plt.subplots(figsize=(6.4, 2.6), dpi=220); ax.axis('off')
ax.imshow(gbrn(s, hl=am + fe + ar, hlc=col, w=700, h=320, bl=50))
for x, t, c in [(0.12, 'amida', JT), (0.5, 'arena (cincin benzena)', HJ), (0.88, 'fenol', BIRU)]: ax.text(x, -0.06, t, transform=ax.transAxes, ha='center', color=c, fontsize=10, fontweight='bold')
plt.tight_layout(); f.savefig(f'{F}/parasetamol.png', bbox_inches='tight'); plt.close(f)

# 5. karbon primer-kuaterner pada 2,2,4-trimetilpentana
s = 'CC(C)(C)CC(C)C'; m = Chem.MolFromSmiles(s)
kel = {}
for a in m.GetAtoms():
    n = sum(1 for b in a.GetNeighbors() if b.GetSymbol() == 'C'); kel[a.GetIdx()] = ['', '1', '2', '3', '4'][n]
warna = {'1': (0.5, 0.75, 0.94), '2': (0.72, 0.88, 0.80), '3': (0.94, 0.63, 0.38), '4': (0.95, 0.55, 0.55)}
f, ax = plt.subplots(figsize=(5.6, 2.6), dpi=220); ax.axis('off')
ax.imshow(gbrn(s, notes=kel, hl=list(kel), hlc={i: warna[kel[i]] for i in kel}, w=640, h=300, bl=55))
ax.text(0.5, -0.06, 'angka = jumlah tetangga karbon: 1 primer (biru), 2 sekunder (hijau),\n3 tersier (jingga), 4 kuaterner (merah)', transform=ax.transAxes, ha='center', fontsize=8.5, color=TUA)
plt.tight_layout(); f.savefig(f'{F}/karbon.png', bbox_inches='tight'); plt.close(f)

# 6. rantai induk dan penomoran: 3-etil-5-metilheptana
s = 'CCC(C)CC(CC)CC'
m = Chem.MolFromSmiles(s)
# rantai: idx 0-1-2-4-5-6-7 (via etil) atau 0-1-2-4-5-8-9; pilih penomoran memberi 3-etil-5-metil
chain = [9, 8, 5, 4, 2, 1, 0]
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 2.6), dpi=220)
for a in (a1, a2): a.axis('off')
a1.imshow(gbrn(s, notes={i: str(k + 1) for k, i in enumerate([0, 1, 2, 4, 5, 8, 9])}, hl=[0, 1, 2, 4, 5, 8, 9], w=520, h=320, bl=45))
a1.set_title('penomoran A: cabang di 3 dan 5\n(3-metil, 5-etil)', fontsize=8.5, color=TUA, y=-0.2)
a2.imshow(gbrn(s, notes={i: str(k + 1) for k, i in enumerate(chain)}, hl=chain, hlc={i: (0.72, 0.88, 0.80) for i in chain}, w=520, h=320, bl=45))
a2.set_title('penomoran B: cabang juga di 3 dan 5;\nabjad: etil lebih dulu → 3-etil-5-metilheptana', fontsize=8.5, color=HJ, y=-0.2)
plt.tight_layout(); f.savefig(f'{F}/induk.png', bbox_inches='tight'); plt.close(f)

# 7. lima isomer C6H14
I = [('CCCCCC', 'heksana'), ('CC(C)CCC', '2-metilpentana'), ('CCC(C)CC', '3-metilpentana'), ('CC(C)(C)CC', '2,2-dimetilbutana'), ('CC(C)C(C)C', '2,3-dimetilbutana')]
grid([(gbrn(s, w=420, h=280, bl=62), t) for s, t in I], 'isomer.png', 5, (7.6, 1.9), fs_t=8.5)

# 8. sikloalkana
I = [('C1CC1', 'siklopropana'), ('C1CCC1', 'siklobutana'), ('C1CCCC1', 'siklopentana'), ('C1CCCCC1', 'sikloheksana'),
     ('CC1CCCCC1', 'metilsikloheksana'), ('CCC1CC(C)CC(C)C1', '1-etil-3,5-dimetilsikloheksana')]
grid([(gbrn(s, w=420, h=320, bl=40), t) for s, t in I], 'siklo.png', 3, (7.0, 4.4), fs_t=8.8)

# 9. bisiklik (digambar manual)
f, ax = plt.subplots(figsize=(7.0, 2.9), dpi=220); ax.axis('off'); ax.set_xlim(0, 24); ax.set_ylim(-1.2, 7.4); ax.set_aspect('equal')
N = {1: (1.5, 3.2), 2: (3.0, 1.6), 3: (5.6, 1.6), 4: (7.1, 3.2), 5: (5.8, 4.1), 6: (2.8, 4.1), 7: (4.3, 5.9)}
for a, b in [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (1, 7), (7, 4)]:
    ax.plot([N[a][0], N[b][0]], [N[a][1], N[b][1]], color=TUA, lw=2.2 if (a, b) in [(1, 2), (2, 3), (3, 4)] else 1.6, zorder=2)
for k in (1, 4): ax.plot(*N[k], 'o', ms=11, color=JG, zorder=3)
for k, (x, y) in N.items(): ax.text(x + {1: -0.5, 2: -0.4, 3: 0.4, 4: 0.5, 5: 0.35, 6: -0.35, 7: 0}[k], y + {1: -0.3, 2: -0.5, 3: -0.5, 4: -0.3, 5: 0.35, 6: 0.35, 7: 0.4}[k], str(k), fontsize=8.5, color=BIRU, ha='center')
ax.text(4.3, -0.6, 'norbornana: jalur 2, 2, 1\nbisiklo[2.2.1]heptana', ha='center', fontsize=9, color=TUA)
r = 1.5; c1 = np.array([15.8, 3.2]); c2 = c1 + np.array([2 * r * np.cos(np.radians(30)), 0])
for c in (c1, c2):
    P = [c + r * np.array([np.cos(np.radians(30 + 60 * k)), np.sin(np.radians(30 + 60 * k))]) for k in range(7)]
    ax.add_patch(plt.Polygon(P[:6], closed=True, fc='none', ec=TUA, lw=1.8, joinstyle='round', zorder=2))
bh = [c1 + r * np.array([np.cos(np.radians(30)), np.sin(np.radians(30))]), c1 + r * np.array([np.cos(np.radians(-30)), np.sin(np.radians(-30))])]
for p in bh: ax.plot(*p, 'o', ms=11, color=JG, zorder=3)
ax.plot([bh[0][0], bh[1][0]], [bh[0][1], bh[1][1]], color=JT, lw=3, zorder=2)
ax.text(c1[0] + 1.3, 5.6, 'atom jembatan', ha='center', fontsize=8.5, color=JT)
ax.text(c1[0] + 1.3, -0.6, 'dekalin: jalur 4, 4, 0\nbisiklo[4.4.0]dekana', ha='center', fontsize=9, color=TUA)
ax.text(4.3, 7.0, 'atom jembatan (jingga): C1 dan C4', ha='center', fontsize=8.5, color=JT)
f.savefig(f'{F}/bisiklik.png', bbox_inches='tight'); plt.close(f)

# 10. alkena dan alkuna
I = [('CCC=C(C)C', '2-metilpent-2-ena', {5: '1', 3: '2', 2: '3', 1: '4', 0: '5'}), ('CC#CC(C)CC', '4-metilheks-2-una', {0: '1', 1: '2', 2: '3', 3: '4', 5: '5', 6: '6'}),
     ('C=CC=CC', 'penta-1,3-diena', {0: '1', 1: '2', 2: '3', 3: '4', 4: '5'})]
grid([(gbrn(s, notes=n, w=440, h=300, bl=48), t) for s, t, n in I], 'alkena.png', 3, (7.2, 2.2), fs_t=9)

# 11. tangga prioritas gugus fungsi
f, ax = plt.subplots(figsize=(6.6, 3.4), dpi=220); ax.axis('off'); ax.set_xlim(0, 20); ax.set_ylim(0, 10.5)
P = [('asam karboksilat', 'asam …-oat'), ('ester', '…-oat'), ('amida', '-amida'), ('nitril', '-nitril'), ('aldehida', '-al'), ('keton', '-on'), ('alkohol', '-ol'), ('amina', '-amina')]
for i, (g, ak) in enumerate(P):
    y = 9.6 - i * 1.15; w = 11 - i * 0.9
    ax.add_patch(FancyBboxPatch((1.0, y - 0.45), w, 0.9, boxstyle='round,pad=0.05', fc=plt.cm.Blues(0.85 - i * 0.08), ec='none'))
    ax.text(1.4, y, f'{i + 1}. {g}', va='center', fontsize=9.5, color='white' if i < 4 else TUA, fontweight='bold'); ax.text(1.0 + w + 0.4, y, ak, va='center', fontsize=9, color=JT)
ax.annotate('', (18.6, 9.8), (18.6, 1.2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.2)); ax.text(19.2, 5.5, 'prioritas naik', rotation=90, va='center', fontsize=8.5, color=TUA)
ax.text(1.0, 0.25, 'hanya awalan: halo- (fluoro-, kloro-, bromo-, iodo-), nitro-, alkoksi-', fontsize=8.5, color='#555555')
f.savefig(f'{F}/prioritas.png', bbox_inches='tight'); plt.close(f)

# 12. turunan benzena
I = [('Cc1ccccc1', 'toluena'), ('Oc1ccccc1', 'fenol'), ('Nc1ccccc1', 'anilina'), ('OC(=O)c1ccccc1', 'asam benzoat'),
     ('O=Cc1ccccc1', 'benzaldehida'), ('COc1ccccc1', 'anisol'), ('C=Cc1ccccc1', 'stirena'), ('CC(=O)c1ccccc1', 'asetofenon')]
grid([(gbrn(s, w=400, h=320, bl=40), t) for s, t in I], 'benzena.png', 4, (7.2, 3.8), fs_t=9)

# 13. orto meta para
I = [('Cc1ccccc1C', 'o-xilena (1,2-)'), ('Cc1cccc(C)c1', 'm-xilena (1,3-)'), ('Cc1ccc(C)cc1', 'p-xilena (1,4-)'), ('Nc1ccc(Br)cc1', '4-bromoanilina (p-bromoanilina)')]
grid([(gbrn(s, w=420, h=340, bl=40), t) for s, t in I], 'omp.png', 4, (7.4, 2.2), fs_t=8.5)
print('ok tambahan')
