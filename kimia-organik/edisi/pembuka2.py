#!/usr/bin/env python3
# Ilustrasi pembuka bab Kimia Organik 1 (gaya terang, sesuai isi bab).
# python3 edisi/pembuka2.py -> _kerja/pembuka/bNN.png, bNN.txt
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
E = os.path.dirname(os.path.abspath(__file__)); K = f'{E}/_kerja/pembuka'; os.makedirs(K, exist_ok=True)
TUA, UT, MU, EM, AB = '#143d2a', '#2e8b57', '#9fd8a8', '#e9b949', '#8a9a90'
WARNA = {'C': '#3b4a42', 'H': '#f4f6f4', 'O': '#d2553b', 'N': '#3b6fb6'}
JARI = {'C': 0.30, 'H': 0.19, 'O': 0.30, 'N': 0.30}
W, H = 8.27, 5.0
def kanvas():
    f = plt.figure(figsize=(W, H), dpi=220); ax = f.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect('equal'); return f, ax
def simpan(n, f, cap):
    f.savefig(f'{K}/b{n:02d}.png', transparent=True); plt.close(f); open(f'{K}/b{n:02d}.txt', 'w').write(cap)
def molekul(ax, atom, ikatan, dx, dy, s=1.0):
    P = {k: (dx + s * x, dy + s * y) for k, (e, x, y) in atom.items()}
    for a, b in ikatan: ax.plot(*zip(P[a], P[b]), color=AB, lw=5 * s, solid_capstyle='round', zorder=1)
    for k, (e, x, y) in sorted(atom.items(), key=lambda t: t[1][0] == 'H'):
        r = JARI[e] * s; X, Y = P[k]
        ax.add_patch(Circle((X, Y), r, fc=WARNA[e], ec=TUA, lw=1.0, zorder=3))
        ax.add_patch(Circle((X - 0.3 * r, Y + 0.3 * r), 0.35 * r, fc='white', ec='none', alpha=0.35, zorder=4))
    return P

# Bab 1: dua molekul C2H6O, etanol (ikatan hidrogen) dan dimetil eter
f, ax = kanvas()
et = {'C1': ('C', 0, 0), 'C2': ('C', 0.95, 0.45), 'O': ('O', 1.9, 0), 'Ho': ('H', 2.6, 0.35),
      'h1': ('H', -0.55, 0.55), 'h2': ('H', -0.5, -0.5), 'h3': ('H', 0.1, -0.75), 'h4': ('H', 0.85, 1.2), 'h5': ('H', 1.15, -0.25 + 0.95)}
et['h5'] = ('H', 1.45, 1.05)
ik = [('C1', 'C2'), ('C2', 'O'), ('O', 'Ho'), ('C1', 'h1'), ('C1', 'h2'), ('C1', 'h3'), ('C2', 'h4'), ('C2', 'h5')]
P1 = molekul(ax, et, ik, 0.9, 2.6, 0.95)
P2 = molekul(ax, et, ik, 3.6, 0.9, 0.95)
ax.plot([P1['Ho'][0] + 0.15, P2['O'][0] - 0.05], [P1['Ho'][1] - 0.15, P2['O'][1] + 0.25], color=UT, lw=2.2, ls=(0, (2, 2)), zorder=0)
ax.text(3.45, 2.75, 'ikatan hidrogen', color=UT, fontsize=10, rotation=-40, family='Liberation Sans')
eter = {'Ca': ('C', 0, 0), 'O': ('O', 0.85, 0.5), 'Cb': ('C', 1.7, 0),
        'a1': ('H', -0.6, 0.5), 'a2': ('H', -0.45, -0.55), 'a3': ('H', 0.1, -0.7), 'b1': ('H', 2.3, 0.5), 'b2': ('H', 2.15, -0.55), 'b3': ('H', 1.6, -0.7)}
ike = [('Ca', 'O'), ('O', 'Cb'), ('Ca', 'a1'), ('Ca', 'a2'), ('Ca', 'a3'), ('Cb', 'b1'), ('Cb', 'b2'), ('Cb', 'b3')]
molekul(ax, eter, ike, 5.55, 3.2, 0.95)
ax.text(1.9, 4.55, 'etanol · td 78 °C', color=TUA, fontsize=12, fontweight='bold', family='Liberation Sans')
ax.text(5.2, 4.55, 'dimetil eter · td −24 °C', color=TUA, fontsize=12, fontweight='bold', family='Liberation Sans')
ax.text(6.3, 0.75, 'C₂H₆O', color=EM, fontsize=22, fontweight='bold', family='Liberation Sans')
simpan(1, f, 'Etanol dan dimetil eter mempunyai rumus molekul yang sama, C₂H₆O. Hanya etanol yang mempunyai ikatan O–H, sehingga molekul-molekulnya saling terkait oleh ikatan hidrogen dan mendidih 102 derajat lebih tinggi.')
print('ok')

# Bab 2: satu molekul, tiga nama (parasetamol)
import io
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
m = Chem.MolFromSmiles('CC(=O)Nc1ccc(O)cc1')
d = rdMolDraw2D.MolDraw2DCairo(900, 560); o = d.drawOptions(); o.bondLineWidth = 5; o.fixedFontSize = 44; o.clearBackground = False
o.updateAtomPalette({8: (0.82, 0.33, 0.23), 7: (0.23, 0.44, 0.71), 6: (0.08, 0.24, 0.16)})
rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing()
img = Image.open(io.BytesIO(d.GetDrawingText()))
f, ax = kanvas()
ax.imshow(img, extent=[0.3, 4.9, 0.9, 3.76], zorder=2)
for y, t, c, s in [(3.95, 'parasetamol', TUA, 20), (3.05, 'N-(4-hidroksifenil)asetamida', UT, 13), (2.3, 'asetaminofen', AB, 15), (1.55, 'C₈H₉NO₂', EM, 18)]:
    ax.text(5.15, y, t, color=c, fontsize=s, fontweight='bold', family='Liberation Sans')
simpan(2, f, 'Satu molekul, tiga nama: parasetamol (nama generik), N-(4-hidroksifenil)asetamida (nama IUPAC), dan asetaminofen. Nama IUPAC adalah deskripsi struktur yang dapat dibaca kembali menjadi gambar molekul.')
print('ok2')

# Bab 3: asam asetat dan etanol
def rd(smi, w=600, h=420):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 5; o.fixedFontSize = 46; o.clearBackground = False
    o.updateAtomPalette({8: (0.82, 0.33, 0.23), 7: (0.23, 0.44, 0.71), 6: (0.08, 0.24, 0.16)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))
f, ax = kanvas()
ax.imshow(rd('CC(=O)O'), extent=[0.3, 3.5, 1.6, 3.85], zorder=2)
ax.imshow(rd('CCO'), extent=[4.6, 7.8, 1.6, 3.85], zorder=2)
ax.text(1.9, 4.3, 'asam asetat', ha='center', color=TUA, fontsize=15, fontweight='bold', family='Liberation Sans')
ax.text(6.2, 4.3, 'etanol', ha='center', color=TUA, fontsize=15, fontweight='bold', family='Liberation Sans')
ax.text(1.9, 1.2, 'pKa 4,76', ha='center', color=UT, fontsize=17, fontweight='bold', family='Liberation Sans')
ax.text(6.2, 1.2, 'pKa 16', ha='center', color=AB, fontsize=17, fontweight='bold', family='Liberation Sans')
ax.text(4.05, 2.6, '10¹¹ ×', ha='center', color=EM, fontsize=22, fontweight='bold', family='Liberation Sans')
ax.annotate('', (3.4, 2.25), (4.7, 2.25), arrowprops=dict(arrowstyle='-|>', color=EM, lw=2.2))
simpan(3, f, 'Asam asetat dan etanol sama-sama melepas proton dari ikatan O–H, tetapi asam asetat sekitar seratus miliar kali lebih asam. Perbedaannya terletak pada basa konjugatnya: muatan negatif ion asetat tersebar di dua oksigen.')
print('ok3')

# Bab 4: sikloheksana kursi dengan aksial dan ekuatorial
f, ax = kanvas()
Pk = np.array([(0, 0), (0.85, 0.75), (2.15, 0.5), (3.0, 0.85), (2.15, 0.1), (0.85, 0.35)]) * 1.35 + np.array([0.9, 1.6])
nk = [False, True, False, True, False, True]; cen = Pk.mean(0)
for i in range(6):
    ax.plot([Pk[i][0], Pk[i][0]], [Pk[i][1], Pk[i][1] + (0.9 if nk[i] else -0.9)], color=UT, lw=4, solid_capstyle='round', zorder=1)
    d = Pk[(i + 2) % 6] - Pk[(i + 1) % 6]; d = d / np.linalg.norm(d)
    if np.dot(d, Pk[i] - cen) < 0: d = -d
    ax.plot([Pk[i][0], Pk[i][0] + 0.85 * d[0]], [Pk[i][1], Pk[i][1] + 0.85 * d[1]], color=EM, lw=4, solid_capstyle='round', zorder=1)
for i in range(6): ax.plot(*zip(Pk[i], Pk[(i + 1) % 6]), color=TUA, lw=5, solid_capstyle='round', zorder=2)
for i in range(6): ax.add_patch(Circle(Pk[i], 0.11, fc=TUA, ec='none', zorder=3))
ax.text(6.55, 3.3, 'aksial', color=UT, fontsize=18, fontweight='bold', family='Liberation Sans')
ax.text(6.55, 2.6, 'ekuatorial', color=EM, fontsize=18, fontweight='bold', family='Liberation Sans')
simpan(4, f, 'Sikloheksana dalam bentuk kursi, bebas tegangan. Setiap karbon mempunyai satu ikatan aksial (tegak, hijau) dan satu ikatan ekuatorial (ke samping, kuning). Gugus besar lebih suka posisi ekuatorial.')
print('ok4')

# Bab 5: karvon R dan S sebagai bayangan cermin
def rd5(smi, w=560, h=440):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 5; o.fixedFontSize = 40; o.clearBackground = False
    o.updateAtomPalette({8: (0.82, 0.33, 0.23), 6: (0.08, 0.24, 0.16)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))
f, ax = kanvas()
ax.imshow(rd5('CC1=CC[C@H](CC1=O)C(C)=C'), extent=[0.4, 3.6, 1.2, 3.7], zorder=2)
ax.imshow(rd5('CC1=CC[C@@H](CC1=O)C(C)=C'), extent=[4.7, 7.9, 1.2, 3.7], zorder=2)
ax.plot([4.15, 4.15], [0.9, 4.2], color=UT, lw=2.5, ls=(0, (5, 4)))
ax.text(2.0, 4.25, '(R)-karvon', ha='center', color=TUA, fontsize=15, fontweight='bold', family='Liberation Sans')
ax.text(6.3, 4.25, '(S)-karvon', ha='center', color=TUA, fontsize=15, fontweight='bold', family='Liberation Sans')
ax.text(2.0, 0.75, 'bau daun mint', ha='center', color=UT, fontsize=14, family='Liberation Sans')
ax.text(6.3, 0.75, 'bau biji jintan', ha='center', color=EM, fontsize=14, family='Liberation Sans')
simpan(5, f, 'Dua enansiomer karvon: rumus, titik didih, dan kerapatannya sama, tetapi (R)-karvon berbau daun mint dan (S)-karvon berbau biji jintan, karena reseptor bau di hidung bersifat kiral.')
print('ok5')

# Bab 6: profil energi reaksi dua langkah dengan intermediet
from scipy.interpolate import CubicSpline as _CS
f, ax = kanvas()
X6 = [0.5, 1.6, 3.0, 4.2, 5.3, 6.6, 7.8]; Y6 = [1.6, 1.8, 4.2, 2.7, 3.6, 0.9, 0.8]
xx = np.linspace(0.5, 7.8, 700); yy = _CS(X6, Y6, bc_type='clamped')(xx)
for lw, al in [(14, .06), (8, .12), (3.5, 1)]: ax.plot(xx, yy, color=UT, lw=lw, alpha=al, solid_capstyle='round')
ax.add_patch(Circle((4.2, 2.7), 0.13, fc=EM, ec='none', zorder=5))
ax.text(3.0, 4.45, '‡', ha='center', color=TUA, fontsize=24, family='DejaVu Sans'); ax.text(5.3, 3.85, '‡', ha='center', color=TUA, fontsize=20, family='DejaVu Sans')
ax.text(4.2, 2.2, 'intermediet', ha='center', color=EM, fontsize=13, fontweight='bold', family='Liberation Sans')
ax.text(0.6, 1.0, 'Nu:⁻  +  E⁺', color=TUA, fontsize=15, fontweight='bold', family='DejaVu Sans')
ax.text(6.4, 0.25, 'produk', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(6, f, 'Profil energi reaksi dua langkah: pereaksi naik melewati keadaan transisi (‡) ke intermediet, lalu melewati keadaan transisi kedua menuju produk. Mekanisme menjelaskan setiap langkah dengan gerak pasangan elektron dari nukleofil ke elektrofil.')
print('ok6')

# Bab 7: substitusi lawan eliminasi
def rd7(smi, w=420, h=300):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 5; o.fixedFontSize = 38; o.clearBackground = False
    o.updateAtomPalette({35: (0.82, 0.45, 0.15), 8: (0.82, 0.33, 0.23), 6: (0.08, 0.24, 0.16)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))
f, ax = kanvas()
ax.imshow(rd7('CCCCBr'), extent=[0.3, 2.7, 2.65, 4.45], zorder=2); ax.imshow(rd7('CCCCOCC'), extent=[5.0, 8.0, 2.65, 4.45], zorder=2)
ax.imshow(rd7('CC(C)(C)Br'), extent=[0.5, 2.6, 0.35, 2.15], zorder=2); ax.imshow(rd7('C=C(C)C'), extent=[5.4, 7.4, 0.35, 2.15], zorder=2)
for y, t, c in [(3.55, 'SN2: substitusi', UT), (1.25, 'E2: eliminasi', EM)]:
    ax.annotate('', (4.9, y), (2.9, y), arrowprops=dict(arrowstyle='-|>', color=c, lw=3)); ax.text(3.9, y + 0.3, t, ha='center', color=c, fontsize=13, fontweight='bold', family='Liberation Sans')
ax.text(3.9, 2.4, 'NaOCH₂CH₃, etanol', ha='center', color=TUA, fontsize=12, family='Liberation Sans')
simpan(7, f, 'Pereaksi yang sama, hasil yang berbeda: 1-bromobutana (primer) memberi eter lewat substitusi SN2, sedangkan 2-bromo-2-metilpropana (tersier) memberi alkena lewat eliminasi E2.')
print('ok7')

# Bab 8: HBr + propena, dengan dan tanpa peroksida
f, ax = kanvas()
ax.imshow(rd7('CC=C'), extent=[0.3, 2.5, 1.55, 3.45], zorder=2)
ax.imshow(rd7('CC(Br)C'), extent=[5.4, 7.7, 2.75, 4.65], zorder=2); ax.imshow(rd7('BrCCC'), extent=[5.2, 7.9, 0.35, 2.15], zorder=2)
for y0, y1, t, c in [(2.7, 3.7, 'HBr', UT), (2.3, 1.25, 'HBr + peroksida', EM)]:
    ax.annotate('', (5.1, y1), (2.8, y0), arrowprops=dict(arrowstyle='-|>', color=c, lw=3)); ax.text(3.75, (y0 + y1) / 2 + (0.45 if y1 > y0 else -0.5), t, ha='center', color=c, fontsize=13, fontweight='bold', family='Liberation Sans')
ax.text(6.55, 4.75, 'Markovnikov (ionik)', ha='center', color=UT, fontsize=12, family='Liberation Sans')
ax.text(6.55, 0.15, 'anti-Markovnikov (radikal)', ha='center', color=EM, fontsize=12, family='Liberation Sans')
simpan(8, f, 'Satu alkena, satu pereaksi, dua produk: tanpa peroksida HBr beradisi lewat karbokation dan bromin masuk ke karbon tengah; dengan peroksida reaksi berantai radikal menaruh bromin di karbon ujung.')
print('ok8')

# Bab 9: tiga alkohol C4H10O dan dikromat
f, ax = kanvas()
for i, (smi, nm, hasil, c) in enumerate([('CCCCO', 'butan-1-ol', 'hijau', UT), ('CCC(C)O', 'butan-2-ol', 'hijau', UT), ('CC(C)(C)O', '2-metilpropan-2-ol', 'tetap jingga', '#d9822b')]):
    x = 0.4 + i * 2.65
    ax.imshow(rd7(smi), extent=[x, x + 2.2, 2.3, 4.1], zorder=2)
    ax.text(x + 1.1, 2.0, nm, ha='center', color=TUA, fontsize=12, family='Liberation Sans')
    ax.add_patch(Circle((x + 1.1, 1.0), 0.42, fc=c, ec=TUA, lw=1.2, zorder=3))
    ax.text(x + 1.1, 0.25, hasil, ha='center', color=c, fontsize=11.5, fontweight='bold', family='Liberation Sans')
ax.text(W / 2, 4.6, 'K₂Cr₂O₇, H₂SO₄ (jingga)', ha='center', color=TUA, fontsize=13, fontweight='bold', family='Liberation Sans')
simpan(9, f, 'Tiga alkohol dengan rumus C₄H₁₀O diuji dengan dikromat yang berwarna jingga. Alkohol primer dan sekunder mengubahnya menjadi hijau (Cr³⁺), sedangkan alkohol tersier tidak, karena karbon pembawa –OH-nya tidak mempunyai atom H.')
print('ok9')

# Bab 10: alkena mengadisi, benzena mensubstitusi
f, ax = kanvas()
ax.imshow(rd7('C1=CCCCC1'), extent=[0.5, 2.5, 2.75, 4.55], zorder=2); ax.imshow(rd7('BrC1CCCCC1Br'), extent=[5.3, 7.7, 2.65, 4.65], zorder=2)
ax.imshow(rd7('c1ccccc1'), extent=[0.5, 2.5, 0.35, 2.15], zorder=2); ax.imshow(rd7('Brc1ccccc1'), extent=[5.3, 7.7, 0.3, 2.2], zorder=2)
for y, t, t2, c in [(3.65, 'adisi', 'Br₂', UT), (1.25, 'substitusi', 'Br₂, FeBr₃', EM)]:
    ax.annotate('', (5.1, y), (2.9, y), arrowprops=dict(arrowstyle='-|>', color=c, lw=3)); ax.text(4.0, y + 0.3, t2, ha='center', color=TUA, fontsize=12, family='Liberation Sans')
    ax.text(4.0, y - 0.5, t, ha='center', color=c, fontsize=13, fontweight='bold', family='Liberation Sans')
simpan(10, f, 'Sikloheksena mengadisi bromin dan kehilangan ikatan rangkapnya, sedangkan benzena mengganti satu atom H dengan Br dan mempertahankan cincin aromatiknya. Kestabilan enam elektron π yang tersebar merata membuat benzena memilih substitusi.')
print('ok10')

# Bab 11: glukosa rantai terbuka dan cincin
f, ax = kanvas()
def rd11(smi, w=560, h=460):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 5; o.fixedFontSize = 32; o.clearBackground = False
    o.updateAtomPalette({8: (0.82, 0.33, 0.23), 6: (0.08, 0.24, 0.16)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))
ax.imshow(rd11('O=C[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO'), extent=[0.2, 3.6, 0.9, 3.9], zorder=2)
ax.imshow(rd11('OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O'), extent=[4.6, 8.0, 0.8, 4.0], zorder=2)
ax.annotate('', (4.5, 2.55), (3.7, 2.55), arrowprops=dict(arrowstyle='-|>', color=UT, lw=3)); ax.annotate('', (3.7, 2.25), (4.5, 2.25), arrowprops=dict(arrowstyle='-|>', color=EM, lw=3))
ax.text(1.9, 0.45, 'rantai terbuka: < 0,003%', ha='center', color=EM, fontsize=12.5, fontweight='bold', family='Liberation Sans')
ax.text(6.3, 0.45, 'hemiasetal siklik: > 99,99%', ha='center', color=UT, fontsize=12.5, fontweight='bold', family='Liberation Sans')
ax.text(W / 2, 4.6, 'glukosa dalam air', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(11, f, 'Glukosa adalah aldehida, tetapi dalam air hampir seluruhnya berbentuk cincin. Gugus –OH pada C5 menyerang gugus aldehida dalam molekul yang sama dan membentuk hemiasetal siklik: adisi nukleofilik pada gugus karbonil.')
print('ok11')

# Bab 12: ester lawan amida
f, ax = kanvas()
ax.imshow(rd11('CC(=O)Oc1ccccc1C(=O)O'), extent=[0.3, 3.7, 1.4, 4.2], zorder=2)
ax.imshow(rd11('CC(=O)NC(C)C(=O)NC(C)C(=O)O'), extent=[4.6, 8.0, 1.4, 4.2], zorder=2)
ax.text(2.0, 4.45, 'ester (aspirin)', ha='center', color=EM, fontsize=14, fontweight='bold', family='Liberation Sans')
ax.text(6.3, 4.45, 'amida (ikatan peptida)', ha='center', color=UT, fontsize=14, fontweight='bold', family='Liberation Sans')
ax.text(2.0, 0.75, 'terhidrolisis oleh uap air\n(berbau cuka)', ha='center', color=EM, fontsize=12, family='Liberation Sans')
ax.text(6.3, 0.75, 'bertahan ratusan tahun\npada pH netral', ha='center', color=UT, fontsize=12, family='Liberation Sans')
simpan(12, f, 'Dua turunan asam karboksilat dengan nasib yang sangat berbeda: ester aspirin perlahan terhidrolisis oleh uap air, sedangkan ikatan amida pada protein hampir tidak pernah putus tanpa enzim. Perbedaannya terletak pada gugus pergi dan resonansi.')
print('ok12')

# Bab 13: trimetilamina dan jeruk nipis
f, ax = kanvas()
ax.imshow(rd11('CN(C)C'), extent=[0.6, 3.0, 1.6, 3.8], zorder=2)
ax.imshow(rd11('C[NH+](C)C'), extent=[5.3, 7.7, 1.6, 3.8], zorder=2)
ax.annotate('', (5.1, 2.85), (3.3, 2.85), arrowprops=dict(arrowstyle='-|>', color=UT, lw=3)); ax.annotate('', (3.3, 2.45), (5.1, 2.45), arrowprops=dict(arrowstyle='-|>', color=EM, lw=3))
ax.text(4.2, 3.2, 'H⁺ (jeruk nipis)', ha='center', color=UT, fontsize=12.5, fontweight='bold', family='DejaVu Sans')
ax.text(4.2, 1.85, 'OH⁻', ha='center', color=EM, fontsize=12.5, fontweight='bold', family='DejaVu Sans')
ax.text(1.8, 0.8, 'trimetilamina\nmudah menguap: bau amis', ha='center', color=EM, fontsize=12, family='Liberation Sans')
ax.text(6.5, 0.8, 'ion trimetilamonium\ntidak menguap: tidak berbau', ha='center', color=UT, fontsize=12, family='Liberation Sans')
simpan(13, f, 'Bau amis ikan berasal dari trimetilamina yang mudah menguap. Asam dalam jeruk nipis memprotonasinya menjadi ion trimetilamonium yang tidak menguap, sehingga baunya hilang; dalam basa, amina bebas kembali.')
print('ok13')

# Bab 14: spektrum IR dan MS aseton (skematis)
f, ax = kanvas()
X = np.linspace(400, 4000, 2000)
A = 0.9 * np.exp(-0.5 * ((X - 1715) / 14) ** 2) + 0.35 * np.exp(-0.5 * ((X - 3000) / 20) ** 2) + 0.4 * np.exp(-0.5 * ((X - 1360) / 9) ** 2) + 0.35 * np.exp(-0.5 * ((X - 1220) / 12) ** 2)
Y = 2.6 + 1.6 * np.exp(-1.6 * A)
xs = 0.5 + (4000 - X) / 3600 * 7.2
for lw, al in [(10, .08), (3, 1)]: ax.plot(xs, Y, color=UT, lw=lw, alpha=al)
ax.text(0.5 + (4000 - 1715) / 3600 * 7.2 + 1.3, 3.05, 'C=O 1715 cm⁻¹', ha='center', color=EM, fontsize=13, fontweight='bold', family='DejaVu Sans')
for m, h in [(15, 0.15), (43, 1.4), (58, 0.9)]:
    x = 1.0 + (m - 10) / 55 * 6.0; ax.add_patch(plt.Rectangle((x - 0.08, 0.5), 0.16, h, fc=TUA, ec='none'))
    ax.text(x, 0.5 + h + 0.12, str(m), ha='center', color=TUA, fontsize=11, family='Liberation Sans')
ax.text(6.6, 1.0, 'm/z 58 = M⁺·\n43 = CH₃CO⁺', ha='left', color=TUA, fontsize=11, family='DejaVu Sans')
ax.text(W / 2, 4.65, 'aseton dalam dua spektrum', ha='center', color=TUA, fontsize=14, fontweight='bold', family='Liberation Sans')
simpan(14, f, 'Aseton dilihat dengan dua alat: spektrum inframerah memperlihatkan pita C=O yang kuat pada 1715 cm⁻¹, dan spektrum massa memperlihatkan ion molekul m/z 58 serta ion asetil m/z 43 dari pemutusan α (skematis).')
print('ok14')
