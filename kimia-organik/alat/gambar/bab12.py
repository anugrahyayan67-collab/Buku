# Gambar Bab 12: karboksilat dan dimer, pKa, tangga kereaktifan, adisi-eliminasi, Fischer, saponifikasi,
# amida, nitril, reduksi ester, sabun dan misel, polimer kondensasi, penisilin
import os, io, numpy as np, matplotlib, matplotlib.ticker
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang, ukuran_px
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab12/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
koma = lambda v: f'{v:g}'.replace('.', ',')
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
def rd(smi, w=360, h=300, fs=30, pad=0.15, hl=None, bl=None):
    m = Chem.MolFromSmiles(smi)
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = pad
    if bl: o.fixedBondLength = bl
    o.updateAtomPalette({35: (0.71, 0.33, 0.11), 8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.10, 0.54, 0.42), 16: (0.75, 0.6, 0.1), 1: (0.05, 0.15, 0.28)})
    if hl:
        bonds = [b.GetIdx() for b in m.GetBonds() if b.GetBeginAtomIdx() in hl and b.GetEndAtomIdx() in hl]
        rdMolDraw2D.PrepareAndDrawMolecule(d, m, highlightAtoms=hl, highlightBonds=bonds, highlightAtomColors={i: (0.98, 0.75, 0.7) for i in hl}, highlightBondColors={b: (0.98, 0.75, 0.7) for b in bonds})
    else: rdMolDraw2D.PrepareAndDrawMolecule(d, m)
    d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def gb(ax, smi, x0, x1, y0, y1, **k):
    k['w'], k['h'] = ukuran_px(ax, x0, x1, y0, y1); k['fs'] = min(k.get('fs', 25), 25); k.setdefault('bl', 30)
    pasang(ax, rd(smi, **k), x0, x1, y0, y1, zorder=2, maks=1.0)

# 1. karboksilat dan dimer
f, ax = kanv(7.4, 2.4, (0, 26), (0, 8.4))
gb(ax, 'CC(=O)[O-]', 0, 4.0, 2.0, 6.4); T(ax, 4.6, 4.2, '↔', fs=15, family='DejaVu Sans'); gb(ax, 'CC([O-])=O', 5.2, 9.2, 2.0, 6.4)
T(ax, 4.6, 1.2, 'kedua C–O setara (127 pm)', fs=8.5, c=HJ)
# dimer manual
def L(p, q, c=TUA, lw=1.6, ls='-'): ax.plot([p[0], q[0]], [p[1], q[1]], color=c, lw=lw, ls=ls)
def L2(p, q):
    p, q = np.array(p), np.array(q); d = q - p; n = np.array([-d[1], d[0]]) / np.linalg.norm(d) * 0.1
    L(p + n, q + n); L(p - n, q - n)
cx = 17.6
for C, Me, Od, Oh, H in [((15.2, 4.2), (13.4, 4.2), (16.1, 5.5), (16.1, 2.9), (17.0, 2.9)), ((20.0, 4.2), (21.8, 4.2), (19.1, 2.9), (19.1, 5.5), (18.2, 5.5))]:
    T(ax, *C, 'C', fs=12); T(ax, *Me, 'CH₃', fs=10); T(ax, *Od, 'O', c=JT, fs=12); T(ax, *Oh, 'O', c=JT, fs=12); T(ax, *H, 'H', fs=11)
    sgn = 1 if Me[0] < C[0] else -1
    def seg(P, Q, a=0.35, b=0.35):
        P, Q = np.array(P, float), np.array(Q, float); u = (Q - P) / np.linalg.norm(Q - P); return P + a * u, Q - b * u
    L(*seg(C, Me, 0.3, 0.6)); L2(*seg(C, Od)); L(*seg(C, Oh)); L(*seg(Oh, H, 0.3, 0.3))
L((17.3, 2.9), (18.8, 2.9), c=BIRU, lw=1.4, ls=(0, (2, 2))); L((16.4, 5.5), (17.9, 5.5), c=BIRU, lw=1.4, ls=(0, (2, 2)))
T(ax, cx, 1.2, 'dimer: dua ikatan hidrogen', fs=8.5, c=BIRU)
f.savefig(f'{F}/karboksilat.png', bbox_inches='tight'); plt.close(f)

# 2. pKa
f, ax = plt.subplots(1, 2, figsize=(7.0, 2.8), dpi=220)
n1 = ['CH₃COOH', 'ClCH₂COOH', 'Cl₂CHCOOH', 'Cl₃CCOOH']; v1 = [4.76, 2.86, 1.29, 0.65]
n2 = ['butanoat', '4-kloro', '3-kloro', '2-kloro']; v2 = [4.82, 4.52, 4.05, 2.86]
for a, n, v, c, t in [(ax[0], n1, v1, BIRU, 'jumlah Cl'), (ax[1], n2, v2, JT, 'letak Cl pada asam butanoat')]:
    a.bar(range(4), v, color=c, width=0.6)
    for i, x in enumerate(v): a.text(i, x + 0.1, koma(x), ha='center', fontsize=8.5)
    a.set_xticks(range(4)); a.set_xticklabels(n, fontsize=7.8); a.set_ylim(0, 5.6); a.set_title(t, fontsize=9.5, color=TUA)
    a.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda q, _: koma(q)))
ax[0].set_ylabel('pKa')
plt.tight_layout(); f.savefig(f'{F}/pka.png', bbox_inches='tight'); plt.close(f)

# 3. tangga kereaktifan
f, ax = kanv(6.4, 3.8, (0, 18), (-1.0, 10.4))
tg = [('klorida asam', 'RCOCl', 'Cl⁻', '−7', MERAH), ('anhidrida', 'RCOOCOR', 'RCOO⁻', '4,8', JT), ('ester', 'RCOOR\'', 'R\'O⁻', '16', JG), ('amida', 'RCONH₂', 'NH₂⁻', '38', HJ)]
for i, (nm, rm, lg, pk, c) in enumerate(tg):
    y = 8.6 - i * 2.4; x = 1.0 + i * 1.3
    ax.add_patch(FancyBboxPatch((x, y - 0.75), 7.2, 1.5, boxstyle='round,pad=0.1', fc='white', ec=c, lw=1.5))
    T(ax, x + 2.0, y, nm, c=c, fs=10.5, fontweight='bold'); T(ax, x + 5.4, y, rm, fs=10)
    T(ax, 14.6, y, lg.replace('⁻', '$^-$'), fs=10, c=TUA); T(ax, 16.8, y, pk, fs=10, c=TUA)
T(ax, 14.6, 10.1, 'gugus pergi', fs=8.5, c='#555555'); T(ax, 16.8, 10.1, 'pKa HY', fs=8.5, c='#555555')
ax.annotate('', (0.4, 0.6), (0.4, 9.4), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.5))
ax.text(0.0, 5.0, 'makin stabil, makin tidak reaktif', rotation=90, va='center', ha='center', fontsize=8.5, color=TUA)
T(ax, 7.0, -0.6, 'reaksi mudah "menuruni tangga"', fs=8.5, c=HJ)
f.savefig(f'{F}/tangga.png', bbox_inches='tight'); plt.close(f)

# 4. adisi-eliminasi
f, ax = kanv(7.6, 2.2, (0, 28), (0, 7.6))
gb(ax, 'CC(=O)Cl', 0, 3.8, 1.6, 6.0); T(ax, 4.6, 3.8, '+ CH₃O$^-$', fs=10, c=BIRU); reaksi(ax, 5.8, 8.4, 3.8, 'adisi')
gb(ax, 'CC([O-])(Cl)OC', 8.6, 13.4, 1.2, 6.4); T(ax, 11.0, 0.7, 'zat antara tetrahedral', fs=8.5, c=HJ)
reaksi(ax, 13.8, 16.8, 3.8, 'eliminasi', t2='−Cl$^-$')
gb(ax, 'CC(=O)OC', 17.2, 21.4, 1.6, 6.0); T(ax, 24.6, 3.8, 'Y diganti Nu\n(substitusi asil)', fs=8.5, c=HJ)
f.savefig(f'{F}/adisi.png', bbox_inches='tight'); plt.close(f)

# 5. Fischer
f, ax = kanv(7.8, 3.6, (0, 30), (0, 13.6))
y = 10.4
gb(ax, 'CC(=O)O', 0, 3.4, y - 1.7, y + 1.7); reaksi(ax, 3.6, 5.4, y, 'H$^+$', dua=True)
gb(ax, 'CC(O)=[OH+]', 5.6, 9.2, y - 1.8, y + 1.8); reaksi(ax, 9.4, 11.8, y, 'CH₃OH', dua=True)
gb(ax, 'CC(O)(O)[OH+]C', 12.0, 16.4, y - 2.0, y + 2.0); reaksi(ax, 16.6, 19.0, y, 'transfer H$^+$', dua=True, fs=7.5)
gb(ax, 'CC(O)([OH2+])OC', 19.2, 23.6, y - 2.0, y + 2.0)
y = 3.4
reaksi(ax, 2.0, 5.0, y, '−H₂O', dua=True)
gb(ax, 'CC(OC)=[OH+]', 5.4, 9.4, y - 1.8, y + 1.8); reaksi(ax, 9.8, 12.0, y, '−H$^+$', dua=True)
gb(ax, 'CC(=O)OC', 12.4, 16.2, y - 1.8, y + 1.8); T(ax, 21.6, y, 'metil asetat\n(semua langkah reversibel; K ≈ 4)', fs=8.5, c=HJ)
f.savefig(f'{F}/fischer.png', bbox_inches='tight'); plt.close(f)

# 6. saponifikasi
f, ax = kanv(7.8, 2.2, (0, 32), (0, 7.6))
gb(ax, 'CC(=O)OC', 0, 3.8, 1.6, 6.0); T(ax, 4.5, 3.8, '+ OH$^-$', fs=10, c=BIRU); reaksi(ax, 5.4, 7.2, 3.8)
gb(ax, 'CC([O-])(O)OC', 7.4, 11.8, 1.2, 6.4); reaksi(ax, 12.0, 14.0, 3.8)
gb(ax, 'CC(=O)O', 14.2, 17.6, 1.6, 6.0); T(ax, 19.0, 3.8, '+ CH₃O$^-$', fs=9.5, c=BIRU)
reaksi(ax, 20.6, 23.4, 3.8, 'asam–basa', t2='K ≈ 10$^{11}$', c=MERAH, fs=8)
gb(ax, 'CC(=O)[O-]', 23.6, 27.2, 1.6, 6.0); T(ax, 29.4, 3.8, '+ CH₃OH', fs=9.5)
T(ax, 25.4, 0.9, 'tidak reversibel', fs=8.5, c=MERAH)
f.savefig(f'{F}/saponifikasi.png', bbox_inches='tight'); plt.close(f)

# 7. amida
f, ax = kanv(7.0, 2.4, (0, 24), (0, 8.2))
gb(ax, 'CC(=O)N(C)C', 0, 4.6, 1.8, 6.6); T(ax, 5.3, 4.2, '↔', fs=15, family='DejaVu Sans'); gb(ax, 'CC([O-])=[N+](C)C', 6.0, 10.6, 1.8, 6.6)
T(ax, 5.3, 1.0, 'resonansi amida', fs=8.5, c=HJ)
for i, t in enumerate(['C–N 132 pm (amina: 147 pm)', 'enam atom gugus amida sebidang', 'rotasi C–N terhambat (± 80 kJ mol$^{-1}$)', 'N tidak basa; protonasi pada O']):
    ax.text(12.4, 6.4 - i * 1.45, '• ' + t, fontsize=9, color=TUA, va='center')
f.savefig(f'{F}/amida.png', bbox_inches='tight'); plt.close(f)

# 8. nitril
f, ax = kanv(6.6, 4.2, (-11, 11), (-7.2, 7.2))
gb(ax, 'CCC#N', -2.2, 2.2, -1.6, 1.6)
for (x, y, smi, r, lab) in [(-6.5, 4.4, 'CCC(=O)O', 'H₃O$^+$, panas', 'asam karboksilat'), (6.5, 4.4, 'CCCN', 'LiAlH₄; H₂O', 'amina primer'),
                            (-6.5, -4.4, 'CCC=O', 'DIBAL-H; H₂O', 'aldehida'), (6.5, -4.4, 'CCC(C)=O', 'CH₃MgBr; H₃O$^+$', 'keton')]:
    ax.annotate('', (x * 0.55, y * 0.55), (x * 0.25, y * 0.3), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3))
    T(ax, x * 0.42 + (2.2 if x > 0 else -2.2), y * 0.42, r, fs=8)
    gb(ax, smi, x - 2.0, x + 2.0, y - 1.6, y + 1.6); T(ax, x, y - 2.1 if y < 0 else y + 2.0, lab, fs=8.5, c=HJ)
f.savefig(f'{F}/nitril.png', bbox_inches='tight'); plt.close(f)

# 9. reduksi ester
f, ax = kanv(7.2, 3.6, (0, 24), (0, 12))
gb(ax, 'CCOC(=O)c1ccccc1', 0, 5.4, 3.6, 8.4)
for y, r, smi, lab in [(10.0, 'LiAlH₄; H₂O', 'OCc1ccccc1', 'benzil alkohol (dua H$^-$)'), (6.0, 'DIBAL-H, −78 °C; H₂O', 'O=Cc1ccccc1', 'benzaldehida (satu H$^-$)'), (2.0, '2 CH₃CH₂MgBr; H₃O$^+$', 'CCC(O)(CC)c1ccccc1', '3-fenilpentan-3-ol')]:
    ax.annotate('', (12.0, y), (5.8, 6.0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.2)); T(ax, 10.2, y + 0.75 if y > 6.0 else (y + 0.5 if y == 6.0 else y - 0.75), r, fs=8)
    gb(ax, smi, 12.2, 16.6, y - 1.8, y + 1.8); T(ax, 20.4, y, lab, fs=8.5, c=HJ)
f.savefig(f'{F}/reduksi.png', bbox_inches='tight'); plt.close(f)

# 10. sabun dan misel
f, ax = kanv(7.4, 3.0, (0, 26), (0, 10.6))
T(ax, 5.6, 8.4, 'trigliserida + 3 NaOH', fs=10.5); ax.annotate('', (5.6, 6.0), (5.6, 7.7), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3))
T(ax, 5.6, 5.2, 'gliserol + 3 RCOO$^-$ Na$^+$', fs=10.5, c=HJ); T(ax, 5.6, 4.2, '(sabun)', fs=9, c=HJ)
T(ax, 5.6, 2.0, 'kepala ionik (hidrofilik)\nekor hidrokarbon (hidrofobik)', fs=8.5, c=TUA)
cx, cy, rr = 18.6, 5.3, 4.2
ax.add_patch(Circle((cx, cy), 2.0, fc='#fbe3c9', ec='none')); T(ax, cx, cy, 'minyak', fs=9, c=JT)
for k in range(22):
    th = 2 * np.pi * k / 22; hx, hy = cx + rr * np.cos(th), cy + rr * np.sin(th)
    ex, ey = cx + 2.1 * np.cos(th), cy + 2.1 * np.sin(th)
    xs = np.linspace(hx, ex, 9); ys = np.linspace(hy, ey, 9); per = np.array([-np.sin(th), np.cos(th)]) * 0.18 * np.array([1, -1, 1, -1, 1, -1, 1, -1, 1])[:, None]
    ax.plot(xs + per[:, 0], ys + per[:, 1], color=TUA, lw=0.9)
    ax.add_patch(Circle((hx, hy), 0.32, fc=BIRU, ec='none'))
T(ax, cx, 0.3, 'misel dalam air', fs=8.5, c=BIRU)
f.savefig(f'{F}/sabun.png', bbox_inches='tight'); plt.close(f)

# 11. polimer kondensasi
f, ax = kanv(7.6, 3.4, (0, 28), (0, 12.4))
y = 9.2
gb(ax, 'OC(=O)CCCCC(=O)O', 0, 5.6, y - 1.8, y + 1.8); T(ax, 6.2, y, '+', fs=12); gb(ax, 'NCCCCCCN', 6.6, 11.6, y - 1.6, y + 1.6)
reaksi(ax, 11.9, 14.2, y, 'panas', t2='−H₂O')
gb(ax, '*NCCCCCCNC(=O)CCCCC(=O)*', 14.4, 24.6, y - 2.0, y + 2.0, w=620, h=260, fs=26); T(ax, 26.6, y, 'nilon-6,6', fs=9.5, c=HJ)
y = 3.0
gb(ax, 'OC(=O)c1ccc(cc1)C(=O)O', 0, 5.6, y - 2.0, y + 2.0); T(ax, 6.2, y, '+', fs=12); gb(ax, 'OCCO', 6.8, 10.6, y - 1.4, y + 1.4)
reaksi(ax, 11.9, 14.2, y, 'katalis', t2='−H₂O')
gb(ax, '*OCCOC(=O)c1ccc(cc1)C(=O)*', 14.4, 24.6, y - 2.2, y + 2.2, w=620, h=280, fs=26); T(ax, 26.6, y, 'PET', fs=9.5, c=HJ)
f.savefig(f'{F}/polimer.png', bbox_inches='tight'); plt.close(f)

# 12. penisilin
pen = 'CC1(C)S[C@@H]2[C@H](NC(=O)Cc3ccccc3)C(=O)N2[C@H]1C(=O)O'
m = Chem.MolFromSmiles(pen); ri = m.GetRingInfo(); b4 = [list(r) for r in ri.AtomRings() if len(r) == 4][0]
f, ax = kanv(7.4, 3.0, (0, 26), (0, 9.6))
gb(ax, pen, -0.5, 10.5, 0.6, 9.6, w=560, h=520, fs=24, hl=b4); T(ax, 4.5, 0.4, 'penisilin G (cincin β-laktam disorot)', fs=8.2, c=MERAH)
T(ax, 11.4, 6.0, 'Ser–OH enzim', fs=10, c=BIRU); ax.annotate('', (14.6, 4.6), (11.4, 5.4), arrowprops=dict(arrowstyle='-|>', color=BIRU, lw=1.3))
T(ax, 11.4, 3.4, 'cincin tegang\nresonansi amida lemah', fs=8.2, c=MERAH)
ax.add_patch(FancyBboxPatch((14.9, 2.6), 10.4, 4.0, boxstyle='round,pad=0.15', fc='#eef5fb', ec=BIRU, lw=1.1))
T(ax, 20.1, 5.6, 'enzim terasilasi', fs=10, c=BIRU, fontweight='bold')
T(ax, 20.1, 4.3, 'Ser–O–C(=O)–penisilin (ester)', fs=9, c=TUA); T(ax, 20.1, 3.2, 'transpeptidase berhenti bekerja', fs=8.5, c=HJ)
f.savefig(f'{F}/penisilin.png', bbox_inches='tight'); plt.close(f)
print('ok')
