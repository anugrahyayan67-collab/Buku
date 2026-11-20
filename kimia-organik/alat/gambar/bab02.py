# Gambar Bab 2: gugus alkil, contoh nama IUPAC
import os, io, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab02/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'

def gbr(smi, sorot=(), w=420, h=300):
    m = Chem.MolFromSmiles(smi)
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions()
    o.bondLineWidth = 3; o.fixedFontSize = 28; o.padding = 0.15; o.dummiesAreAttachments = True
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.1, 0.54, 0.42), 35: (0.55, 0.2, 0.1)})
    at = [a.GetIdx() for p in sorot for t in m.GetSubstructMatches(Chem.MolFromSmarts(p)) for a in [m.GetAtomWithIdx(i) for i in t]]
    rdMolDraw2D.PrepareAndDrawMolecule(d, m, highlightAtoms=at, highlightAtomColors={i: (0.5, 0.75, 0.94) for i in at},
                                       highlightBonds=[b.GetIdx() for b in m.GetBonds() if b.GetBeginAtomIdx() in at and b.GetEndAtomIdx() in at],
                                       highlightBondColors={b.GetIdx(): (0.5, 0.75, 0.94) for b in m.GetBonds()})
    d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))

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
