# Gambar Bab 9: titik didih, fenoksida, pKa, reduksi, alkohol->halida, tangga oksidasi, kuinon,
# autoksidasi, Williamson, eter mahkota, pembukaan epoksida, peta alkohol
import os, io, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang, ukuran_px
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab09/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
koma = lambda v: f'{v:g}'.replace('.', ',')
def T(ax, x, y, s, c=TUA, fs=11, **k): ax.text(x, y, s, ha='center', va='center', color=c, fontsize=fs, **k)
def reaksi(ax, x1, x2, y, t='', c=TUA, t2='', fs=8.5):
    ax.annotate('', (x2, y), (x1, y), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.3))
    if t: T(ax, (x1 + x2) / 2, y + 0.35, t, fs=fs)
    if t2: T(ax, (x1 + x2) / 2, y - 0.35, t2, fs=fs)
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def rd(smi, w=360, h=300, fs=30, hs=(), pad=0.15, bl=None):
    m = Chem.MolFromSmiles(smi)
    if hs: m = Chem.AddHs(m, onlyOnAtoms=tuple(hs))
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = pad
    if bl: o.fixedBondLength = bl
    o.updateAtomPalette({35: (0.71, 0.33, 0.11), 8: (0.71, 0.33, 0.11), 17: (0.10, 0.54, 0.42), 16: (0.75, 0.6, 0.1), 1: (0.05, 0.15, 0.28)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def gb(ax, smi, x0, x1, y0, y1, **k):
    k['w'], k['h'] = ukuran_px(ax, x0, x1, y0, y1); k['fs'] = min(k.get('fs', 25), 25); k.setdefault('bl', 40)
    pasang(ax, rd(smi, **k), x0, x1, y0, y1, maks=1.0)

# 1. titik didih
f, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
grup = [('M ≈ 45 g mol$^{-1}$', ['propana', 'dimetil eter', 'etanol'], [-42, -24, 78]), ('M ≈ 73 g mol$^{-1}$', ['pentana', 'dietil eter', 'butan-1-ol'], [36, 35, 117])]
warna = [MUDA, JG, BIRU]
for g, (judul, nm, bp) in enumerate(grup):
    for i, (n, v) in enumerate(zip(nm, bp)):
        x = g * 4 + i; ax.bar(x, v, 0.75, color=warna[i]); ax.text(x, v + (4 if v >= 0 else -10), f'{v}'.replace('-', '−'), ha='center', fontsize=8.5)
        ax.text(x, -62, n, ha='center', fontsize=8, rotation=0)
    ax.text(g * 4 + 1, 132, judul, ha='center', fontsize=9, color=TUA)
ax.axhline(0, color=TUA, lw=0.8); ax.set_xticks([]); ax.set_ylabel('Titik didih (°C)'); ax.set_ylim(-70, 140); ax.spines['bottom'].set_visible(False)
plt.tight_layout(); f.savefig(f'{F}/didih.png', bbox_inches='tight'); plt.close(f)

# 2. resonansi fenoksida
f, ax = kanv(7.6, 1.8, (0, 24), (0, 5.6))
sm = ['[O-]c1ccccc1', 'O=C1C=CC=C[CH-]1', 'O=C1C=C[CH-]C=C1', 'O=C1[CH-]C=CC=C1']
for i, s in enumerate(sm):
    x = i * 6.2; gb(ax, s, x, x + 4.6, 0.3, 5.3)
    if i < 3: T(ax, x + 5.4, 2.8, '↔', fs=16, family='DejaVu Sans')
T(ax, 8.5, 0.15, 'orto', fs=8, c=HJ); T(ax, 14.7, 0.15, 'para', fs=8, c=HJ); T(ax, 20.9, 0.15, 'orto', fs=8, c=HJ)
f.savefig(f'{F}/fenoksida.png', bbox_inches='tight'); plt.close(f)

# 3. pKa alkohol dan fenol
d3 = [('2-metilpropan-2-ol', 18, MUDA), ('etanol', 16, MUDA), ('metanol', 15.5, MUDA), ('2,2,2-trifluoroetanol', 12.4, BIRU), ('4-metilfenol', 10.3, JG),
      ('fenol', 10.0, JG), ('4-klorofenol', 9.4, JG), ('3-nitrofenol', 8.4, JT), ('4-nitrofenol', 7.15, JT), ('asam pikrat', 0.4, JT)]
f, ax = plt.subplots(figsize=(6.0, 3.6), dpi=220)
y = np.arange(len(d3))[::-1]
ax.barh(y, [v for _, v, _ in d3], color=[c for *_, c in d3], height=0.65)
for yi, (n, v, c) in zip(y, d3): ax.text(v + 0.3, yi, koma(v), va='center', fontsize=8.5)
ax.set_yticks(y); ax.set_yticklabels([n for n, *_ in d3], fontsize=8.5); ax.set_xlabel('pKa (lebih kecil = lebih asam)'); ax.set_xlim(0, 20.5); ax.set_xticks(range(0, 21, 4))
plt.tight_layout(); f.savefig(f'{F}/pka.png', bbox_inches='tight'); plt.close(f)

# 4. reduksi karbonil
f, ax = kanv(7.4, 3.9, (0, 22), (0, 11.6))
baris = [(9.4, 'CCCC=O', 'CCCCO', 'NaBH₄ atau LiAlH₄', 'aldehida → alkohol primer'), (5.6, 'CC(=O)CC', 'CC(O)CC', 'NaBH₄ atau LiAlH₄', 'keton → alkohol sekunder'),
         (1.8, 'CCC(=O)OC', 'CCCO', '(1) LiAlH₄; (2) H₃O$^+$', 'ester → alkohol primer (+ CH₃OH)')]
for y, a, b, r, t in baris:
    gb(ax, a, 0.2, 4.6, y - 1.8, y + 1.8); reaksi(ax, 5.0, 9.6, y, r); gb(ax, b, 10.0, 14.4, y - 1.8, y + 1.8); T(ax, 18.4, y, t, fs=8.5, c=HJ)
f.savefig(f'{F}/reduksi.png', bbox_inches='tight'); plt.close(f)

# 5. alkohol -> halida / tosilat
f, ax = kanv(7.6, 3.4, (0, 23), (0, 10.4))
gb(ax, 'C[C@@H](O)CC', 0, 4.4, 3.2, 7.2, hs=(1,)); T(ax, 2.2, 2.9, '(R)-butan-2-ol', fs=8.5, c=HJ)
ax.annotate('', (8.6, 8.6), (4.6, 6.2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 5.7, 8.3, 'PBr₃', fs=8.5)
gb(ax, 'C[C@H](Br)CC', 8.8, 13.0, 6.6, 10.4, hs=(1,)); T(ax, 16.4, 8.5, '(S)-2-bromobutana\ninversi (SN2)', fs=8.5, c=JT)
ax.annotate('', (8.6, 2.0), (4.6, 4.2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 5.8, 2.3, 'TsCl, piridina', fs=8.5)
gb(ax, 'C[C@@H](OS(=O)(=O)c1ccc(C)cc1)CC', 8.6, 14.8, 0.0, 4.4, hs=(1,), w=520); T(ax, 11.7, 4.5, 'retensi (C–O tidak putus)', fs=8, c=HJ)
reaksi(ax, 15.0, 17.6, 2.2, 'NaBr, DMF')
gb(ax, 'C[C@H](Br)CC', 17.8, 21.8, 0.2, 4.2, hs=(1,)); T(ax, 19.8, 0.0, '(S), inversi', fs=8, c=JT)
f.savefig(f'{F}/halida.png', bbox_inches='tight'); plt.close(f)

# 6. tangga oksidasi
f, ax = kanv(7.6, 2.9, (-0.4, 23), (-3.2, 5.6))
anak = [('CH₄', 'alkana', -4), ('CH₃OH', 'alkohol', -2), ('HCHO', 'aldehida', 0), ('HCOOH', 'asam karboksilat', 2), ('CO₂', 'karbon dioksida', 4)]
for i, (r, g, n) in enumerate(anak):
    x = 1.6 + i * 4.8; yb = i * 0.75
    ax.add_patch(FancyBboxPatch((x - 1.6, yb), 3.2, 1.5, boxstyle='round,pad=0.08', fc='white', ec=BIRU, lw=1.2))
    T(ax, x, yb + 0.95, r, fs=11); T(ax, x, yb + 0.4, g, fs=7.5, c='#555555'); T(ax, x, yb + 2.0, f'{n:+d}'.replace('+0', '0').replace('-', '−'), fs=10, c=JT, fontweight='bold')
    if i < 4: ax.annotate('', (x + 3.1, yb + 1.1), (x + 1.7, yb + 0.6), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.2))
T(ax, 11.2, 5.1, 'bilangan oksidasi karbon', fs=8.5, c=JT)
for y, t, c in [(-0.9, 'alkohol primer: RCH₂OH → RCHO → RCOOH (dua langkah)', HJ), (-1.8, 'alkohol sekunder: R₂CHOH → R₂C=O (berhenti, tidak ada H lagi pada C)', BIRU), (-2.7, 'alkohol tersier: R₃COH → tidak teroksidasi (tidak ada H pada C karbinol)', MERAH)]:
    ax.text(0.2, y, t, color=c, fontsize=8.5, va='center')
f.savefig(f'{F}/tangga.png', bbox_inches='tight'); plt.close(f)

# 7. kuinon
f, ax = kanv(6.0, 1.8, (0, 18), (0, 5.4))
gb(ax, 'Oc1ccc(O)cc1', 0, 5.6, 0.2, 5.2); gb(ax, 'O=C1C=CC(=O)C=C1', 11.4, 17.0, 0.2, 5.2)
ax.annotate('', (10.8, 3.0), (6.2, 3.0), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.3)); ax.annotate('', (6.2, 2.4), (10.8, 2.4), arrowprops=dict(arrowstyle='-|>', color=HJ, lw=1.3))
T(ax, 8.5, 3.5, 'oksidasi: −2H$^+$, −2e$^-$', fs=8.5, c=JT); T(ax, 8.5, 1.85, 'reduksi: +2H$^+$, +2e$^-$', fs=8.5, c=HJ)
T(ax, 2.8, 0.05, 'hidrokuinon', fs=8.5); T(ax, 14.2, 0.05, 'p-benzokuinon', fs=8.5)
f.savefig(f'{F}/kuinon.png', bbox_inches='tight'); plt.close(f)

# 8. autoksidasi dan antioksidan
f, ax = kanv(6.8, 3.6, (0, 20), (0, 10.6))
def kotak(x, y, t, c, w=3.0):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - 0.6), w, 1.2, boxstyle='round,pad=0.1', fc='white', ec=c, lw=1.4)); T(ax, x, y, t, c=c, fs=10.5)
kotak(4.0, 8.4, 'R·', JT); kotak(10.0, 8.4, 'ROO·', JT); kotak(10.0, 3.6, 'ROOH', TUA); kotak(4.0, 3.6, 'R–H (lemak)', TUA, w=3.6)
ax.add_patch(FancyArrowPatch((5.6, 8.4), (8.4, 8.4), arrowstyle='-|>', mutation_scale=12, color=JT, lw=1.5)); T(ax, 7.0, 9.45, '+ O₂ (sangat cepat)', fs=8.5)
ax.add_patch(FancyArrowPatch((10.0, 7.7), (10.0, 4.3), arrowstyle='-|>', mutation_scale=12, color=JT, lw=1.5)); T(ax, 11.6, 6.0, 'ambil H\ndari R–H', fs=8.5)
ax.add_patch(FancyArrowPatch((5.9, 3.6), (8.3, 3.6), arrowstyle='-', color=JT, lw=1.2, ls='--'))
ax.add_patch(FancyArrowPatch((4.0, 4.3), (4.0, 7.7), arrowstyle='-|>', mutation_scale=12, color=JT, lw=1.5)); T(ax, 1.9, 6.0, 'R· baru\n(rantai\nberlanjut)', fs=8.5)
ax.add_patch(FancyArrowPatch((11.6, 8.4), (15.0, 8.4), arrowstyle='-|>', mutation_scale=12, color=HJ, lw=1.8)); T(ax, 13.3, 9.45, '+ ArOH (lebih cepat)', fs=8.5, c=HJ)
kotak(16.8, 8.4, 'ROOH + ArO·', HJ, w=3.8); T(ax, 16.8, 6.9, 'ArO· stabil (resonansi,\nterlindung): rantai berhenti', fs=8.2, c=HJ)
T(ax, 7.0, 1.5, 'siklus propagasi autoksidasi', fs=9, c=JT); T(ax, 16.6, 4.6, 'antioksidan:\nBHT, vitamin E', fs=9, c=HJ)
f.savefig(f'{F}/autoksidasi.png', bbox_inches='tight'); plt.close(f)

# 9. Williamson
f, ax = kanv(7.6, 3.0, (0, 23), (0, 9.4))
gb(ax, 'CC(C)(C)[O-]', 0, 3.8, 5.0, 9.0); T(ax, 4.3, 7.0, '+', fs=13); T(ax, 5.8, 7.0, 'CH₃I', fs=12)
reaksi(ax, 7.4, 11.0, 7.0, 'SN2', c=HJ); gb(ax, 'COC(C)(C)C', 11.4, 15.4, 5.0, 9.0); T(ax, 19.0, 7.0, 'berhasil:\nhalida metil', fs=9, c=HJ)
T(ax, 1.8, 2.5, 'CH₃O$^-$', fs=12); T(ax, 4.3, 2.5, '+', fs=13); gb(ax, 'CC(C)(C)Br', 4.6, 8.0, 0.6, 4.4)
reaksi(ax, 8.4, 11.0, 2.5, 'E2', c=MERAH); gb(ax, 'C=C(C)C', 11.6, 14.6, 0.8, 4.2); T(ax, 16.6, 2.5, '+ CH₃OH', fs=9); T(ax, 20.4, 2.5, 'gagal:\nhalida tersier', fs=9, c=MERAH)
f.savefig(f'{F}/williamson.png', bbox_inches='tight'); plt.close(f)

# 10. eter mahkota: render 3D (konformer dengan keenam O paling melingkar mengelilingi K+)
import sys as _sy; _sy.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3d'))
from r3d import render, spek_molekul, tampil, atom_ikat, pas, normal_cincin
from rdkit.Chem import AllChem
TMP = os.path.join(F, '_r3d'); os.makedirs(TMP, exist_ok=True)
m = Chem.AddHs(Chem.MolFromSmiles('C1COCCOCCOCCOCCOCCO1')); ids = AllChem.EmbedMultipleConfs(m, numConfs=300, randomSeed=5); AllChem.MMFFOptimizeMoleculeConfs(m, maxIters=2000)
Oi = [a_.GetIdx() for a_ in m.GetAtoms() if a_.GetSymbol() == 'O']; best = None
for cid in ids:
    P = m.GetConformer(cid).GetPositions(); c = P[Oi].mean(0); d = np.linalg.norm(P[Oi] - c, axis=1); sk = d.std() + abs(d.mean() - 2.8)
    if best is None or sk < best[0]: best = (sk, P)
P = best[1]; c, n = normal_cincin(P, Oi); P = P - P[Oi].mean(0)
from ilustrasi import _rot
P = P @ _rot(n); at, ik = atom_ikat(m, P)
sp = spek_molekul(at, ik); sp['atoms'].append({'p': [0, 0, 0], 'r': 0.62, 'c': 0x8a63c9})
for i in Oi:   # interaksi ion–dipol K+···O sebagai garis putus
    q = P[i]; L = np.linalg.norm(q)
    for t0 in np.arange(0.25, 0.86, 0.12): sp['bonds'].append({'p': list(map(float, q * t0)), 'q': list(map(float, q * (t0 + 0.06))), 'r': 0.035, 'c': 0x8a63c9})
sp.update(w=900, h=760, camdir=[0.2, -1, 1.15], up=[0, 0, 1]); sp['labels'] = [[0, 0, 0]]
PR = render([(pas(sp, 0.3), f'{TMP}/mahkota.png')])
print('O–K', np.round(np.linalg.norm(P[Oi], axis=1), 2))
f = plt.figure(figsize=(4.4, 3.7), dpi=220); a_ = f.add_axes([0, 0, 1, 1]); fn = f'{TMP}/mahkota.png'; tampil(a_, fn)
q = PR[fn][0]; a_.text(q[0], q[1], 'K$^+$', fontsize=12, color='white', fontweight='bold', ha='center', va='center')
f.savefig(f'{F}/mahkota.png', bbox_inches='tight'); plt.close(f)

# 11. epoksida asam lawan basa
f, ax = kanv(7.6, 3.2, (0, 23), (0, 10))
gb(ax, 'CC1(C)CO1', 0, 4.0, 3.0, 7.0)
ax.annotate('', (9.4, 8.2), (4.4, 6.0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 6.0, 8.2, 'NaOCH₃, CH₃OH', fs=8.5)
gb(ax, 'CC(C)(O)COC', 9.6, 14.4, 5.6, 10.0); T(ax, 18.6, 8.0, 'serang CH₂ (kurang terhalang)\nSN2', fs=8.5, c=HJ)
ax.annotate('', (9.4, 1.8), (4.4, 4.0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 6.0, 1.9, 'CH₃OH, H$^+$', fs=8.5)
gb(ax, 'COC(C)(C)CO', 9.6, 14.4, 0.0, 4.4); T(ax, 18.6, 2.2, 'serang C tersier (memikul δ+)\nmirip SN1, tetap dari belakang', fs=8.5, c=JT)
f.savefig(f'{F}/epoksida.png', bbox_inches='tight'); plt.close(f)

# 12. peta alkohol
f, ax = kanv(7.6, 7.0, (-12.6, 12.6), (-11.6, 11.0))
ax.add_patch(FancyBboxPatch((-2.0, -0.9), 4.0, 1.8, boxstyle='round,pad=0.25', fc=TUA, ec=TUA)); T(ax, 0, 0, 'ALKOHOL\nR–OH', c='white', fs=11, fontweight='bold')
luar = [('alkil halida', 'HX; SOCl₂; PBr₃', JT), ('tosilat', 'TsCl, piridina', JT), ('alkena', 'H₂SO₄ panas; POCl₃', JT), ('eter', 'NaH lalu R\'X', JT),
        ('aldehida', 'PCC; Swern; DMP', JT), ('keton', 'oksidasi alkohol 2°', JT), ('asam karboksilat', 'Jones; KMnO₄', JT), ('silil eter', 'TBSCl, imidazol', JT)]
dalam = [('alkena', 'H₃O$^+$; BH₃ lalu H₂O₂', HJ), ('aldehida, keton', 'NaBH₄; LiAlH₄', HJ), ('ester, asam', 'LiAlH₄', HJ), ('karbonil + RMgX', 'Grignard', HJ), ('epoksida', 'Nu$^-$ atau H₃O$^+$', HJ), ('alkil halida', 'OH$^-$ (SN2)', HJ)]
items = [(p, r, c, '→') for p, r, c in luar] + [(p, r, c, '←') for p, r, c in dalam]
n = len(items)
for i, (p, r, c, arah) in enumerate(items):
    th = np.pi / 2 - 2 * np.pi * i / n; x, y = 10.0 * np.cos(th), 9.4 * np.sin(th)
    a, b = (x * 0.22, y * 0.14), (x * 0.78, y * 0.84)
    if arah == '←': a, b = b, a
    ax.annotate('', b, a, arrowprops=dict(arrowstyle='-|>', color=c, lw=1.2))
    ax.add_patch(FancyBboxPatch((x - 1.95, y - 0.8), 3.9, 1.6, boxstyle='round,pad=0.1', fc='white', ec=c, lw=1.1))
    T(ax, x, y + 0.32, p, c=c, fs=8.4, fontweight='bold'); T(ax, x, y - 0.33, r, fs=6.8)
T(ax, -9.5, -11.0, '→ reaksi alkohol', c=JT, fs=8.5); T(ax, 9.0, -11.0, '← cara membuat alkohol', c=HJ, fs=8.5)
f.savefig(f'{F}/peta.png', bbox_inches='tight'); plt.close(f)
print('ok')
