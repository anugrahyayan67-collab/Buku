# Gambar Bab 10: lingkaran Frost, energi resonansi, heterosiklik, benzilik, ion arenium, diagram energi SEAr,
# Friedel-Crafts, laju nitrasi, ion arenium anisol, distribusi o/m/p, Meisenheimer, benzuna, urutan sintesis
import os, io, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Circle, Rectangle
from scipy.interpolate import PchipInterpolator
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang, ukuran_px
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab10/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
koma = lambda v: f'{v:g}'.replace('.', ',')
def T(ax, x, y, s, c=TUA, fs=11, **k): ax.text(x, y, s, ha='center', va='center', color=c, fontsize=fs, **k)
def reaksi(ax, x1, x2, y, t='', c=TUA, t2='', fs=8.5):
    ax.annotate('', (x2, y), (x1, y), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.3))
    if t: T(ax, (x1 + x2) / 2, y + 0.38, t, fs=fs)
    if t2: T(ax, (x1 + x2) / 2, y - 0.38, t2, fs=fs)
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def mol(smi, hs=(), note=None):
    m = Chem.MolFromSmiles(smi)
    if hs: m = Chem.AddHs(m, onlyOnAtoms=tuple(hs))
    if note:
        for i, t in note.items(): m.GetAtomWithIdx(i).SetProp('atomNote', t)
    return m
def rd(smi, w=360, h=300, fs=30, hs=(), pad=0.15, note=None, m=None, bl=None):
    m = m or mol(smi, hs, note)
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = pad; o.annotationFontScale = 0.9
    if bl: o.fixedBondLength = bl
    o.updateAtomPalette({35: (0.71, 0.33, 0.11), 8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.10, 0.54, 0.42), 9: (0.10, 0.54, 0.42), 16: (0.75, 0.6, 0.1), 1: (0.05, 0.15, 0.28)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def gb(ax, smi, x0, x1, y0, y1, **k):
    k['w'], k['h'] = ukuran_px(ax, x0, x1, y0, y1); k['fs'] = min(k.get('fs', 25), 25); k.setdefault('bl', 40)
    pasang(ax, rd(smi, **k), x0, x1, y0, y1, zorder=2, maks=1.0)

# 1. lingkaran Frost
f, axs = plt.subplots(1, 3, figsize=(7.4, 2.9), dpi=220)
for ax, (n, ne, judul, ket, c) in zip(axs, [(6, 6, 'benzena', '6 elektron π: aromatik', HJ), (4, 4, 'siklobutadiena', '4 elektron π: antiaromatik', MERAH), (5, 6, 'anion siklopentadienil', '6 elektron π: aromatik', HJ)]):
    ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.45, 1.6); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0, 0), 1, fc='none', ec='#bbbbbb', lw=0.8))
    th = -np.pi / 2 + 2 * np.pi * np.arange(n) / n; P = np.c_[np.cos(th), np.sin(th)]
    ax.add_patch(Polygon(P, closed=True, fc='none', ec=TUA, lw=1.3))
    ax.plot([-1.5, 1.5], [0, 0], color='#999999', lw=0.7, ls='--')
    lev = sorted(set(np.round(P[:, 1], 6)))
    sisa = ne
    for y in lev:
        xs = sorted(P[np.isclose(P[:, 1], y), 0])
        for x in xs:
            ax.plot([x - 0.22, x + 0.22], [y, y], color=c, lw=2.2)
        isi = []
        for x in xs:
            k = min(2, sisa) if len(xs) == 1 else None
            isi.append(x)
        if len(xs) == 1:
            k = min(2, sisa); sisa -= k
            ax.text(xs[0], y + 0.03, '↑↓' if k == 2 else ('↑' if k == 1 else ''), ha='center', va='bottom', fontsize=8.5, color=TUA, family='DejaVu Sans')
        else:
            k = min(2 * len(xs), sisa); sisa -= k
            per = [2, 2] if k == 4 else ([1, 1] if k == 2 else [0, 0])
            for x, e in zip(xs, per):
                ax.text(x, y + 0.03, {2: '↑↓', 1: '↑', 0: ''}[e], ha='center', va='bottom', fontsize=8.5, color=TUA, family='DejaVu Sans')
    ax.set_title(judul, fontsize=9.5, color=TUA); ax.text(0, -1.38, ket, ha='center', fontsize=8.2, color=c)
axs[0].text(-1.85, 0.06, 'nonikatan', fontsize=6.5, color='#888888')
axs[0].text(-1.85, -0.75, 'ikatan', fontsize=6.5, color='#888888'); axs[0].text(-1.85, 0.75, 'antiikatan', fontsize=6.5, color='#888888')
plt.tight_layout(); f.savefig(f'{F}/frost.png', bbox_inches='tight'); plt.close(f)

# 2. energi resonansi
f, ax = plt.subplots(figsize=(6.0, 3.5), dpi=220)
lv = [('sikloheksena', 120, MUDA, '-'), ('sikloheksa-1,3-diena', 232, BIRU, '-'), ('"sikloheksatriena"\n(dibayangkan)', 360, '#999999', '--'), ('benzena', 208, HJ, '-')]
for i, (nm, v, c, ls) in enumerate(lv):
    x = i * 1.5
    ax.plot([x - 0.5, x + 0.5], [v, v], color=c, lw=3, ls=ls); ax.text(x, v + 9, nm, ha='center', fontsize=8.5, color=TUA)
    ax.annotate('', (x, 4), (x, v - 4), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.2)); ax.text(x + 0.06, v / 2, f'−{v}', fontsize=8.5, color=c)
ax.plot([-0.7, 5.2], [0, 0], color=TUA, lw=3); ax.text(2.25, -22, 'sikloheksana', ha='center', fontsize=9, color=TUA)
ax.annotate('', (4.95, 208), (4.95, 360), arrowprops=dict(arrowstyle='<->', color=JT, lw=1.3)); ax.plot([3.0, 4.95], [360, 360], color='#999999', lw=0.7, ls=':'); ax.plot([5.0, 4.95], [208, 208], color=HJ, lw=0.7)
ax.text(5.05, 284, '152\nenergi\nresonansi', fontsize=8.5, color=JT, va='center')
ax.set_xlim(-0.8, 6.0); ax.set_ylim(-35, 400); ax.set_xticks([]); ax.spines['bottom'].set_visible(False)
ax.set_ylabel('Energi relatif terhadap sikloheksana (kJ mol$^{-1}$)', fontsize=8.5)
plt.tight_layout(); f.savefig(f'{F}/resonansi.png', bbox_inches='tight'); plt.close(f)

# 3. ion dan heterosiklik aromatik
f, ax = kanv(7.6, 3.9, (0, 24), (0, 12.2))
dat = [('[cH-]1cccc1', 'anion siklopentadienil'), ('[cH+]1cccccc1', 'kation tropilium'), ('c1ccncc1', 'piridina'), ('c1cc[nH]c1', 'pirola'),
       ('c1ccoc1', 'furan'), ('c1ccsc1', 'tiofena'), ('c1cnc[nH]1', 'imidazola'), ('c1ccc2ccccc2c1', 'naftalena (10 e π)')]
for k, (s, nm) in enumerate(dat):
    i, j = k % 4, k // 4; x = i * 6.0; y = 6.3 - j * 6.1
    gb(ax, s, x + 0.6, x + 5.4, y + 1.0, y + 5.6, w=360, h=320); T(ax, x + 3.0, y + 0.6, nm, fs=8.5, c=HJ if k < 7 else TUA)
f.savefig(f'{F}/heterosiklik.png', bbox_inches='tight'); plt.close(f)

# 4. reaksi benzilik
f, ax = kanv(7.4, 3.6, (0, 22), (0, 10.8))
for y, s, t, p, c in [(9.0, 'CCCCc1ccccc1', 'KMnO₄, panas', 'OC(=O)c1ccccc1', HJ), (5.4, 'CC(C)(C)c1ccccc1', 'KMnO₄, panas', None, MERAH), (1.8, 'CCc1ccccc1', 'NBS, cahaya', 'CC(Br)c1ccccc1', HJ)]:
    gb(ax, s, 0.2, 5.4, y - 1.7, y + 1.7); reaksi(ax, 6.0, 10.0, y, t)
    if p: gb(ax, p, 10.6, 15.4, y - 1.7, y + 1.7)
    else: T(ax, 13.0, y, 'tidak bereaksi', fs=10, c=MERAH)
T(ax, 18.8, 9.0, 'rantai dipotong\nmenjadi –COOH', fs=8.5, c=HJ); T(ax, 18.8, 5.4, 'C benzilik tanpa H', fs=8.5, c=MERAH); T(ax, 18.8, 1.8, 'Br di C benzilik\n(radikal benzilik)', fs=8.5, c=HJ)
f.savefig(f'{F}/benzilik.png', bbox_inches='tight'); plt.close(f)

# helper: tambah H pada karbon sp3 cincin
def hs_sp3(smi):
    m = Chem.MolFromSmiles(smi)
    return [a.GetIdx() for a in m.GetAtoms() if a.GetSymbol() == 'C' and a.IsInRing() and a.GetHybridization() == Chem.HybridizationType.SP3 and a.GetTotalNumHs() == 1]

# 5. ion arenium (brominasi)
f, ax = kanv(7.8, 2.0, (0, 32), (0, 7.4))
gb(ax, 'c1ccccc1', 0, 3.6, 1.6, 5.8); T(ax, 4.5, 3.7, '+ Br$^+$', fs=10, c=JT)
reaksi(ax, 5.6, 7.6, 3.7, 'lambat', fs=8)
for k, s_ in enumerate(['BrC1C=CC=C[CH+]1', 'BrC1C=C[CH+]C=C1', 'BrC1[CH+]C=CC=C1']):
    x = 8.2 + k * 5.0; gb(ax, s_, x, x + 4.2, 0.9, 6.5, hs=hs_sp3(s_))
    if k < 2: T(ax, x + 4.6, 3.7, '↔', fs=14, family='DejaVu Sans')
ax.plot([8.1, 7.9, 7.9, 8.1], [6.6, 6.6, 0.8, 0.8], color=TUA, lw=1); ax.plot([22.6, 22.8, 22.8, 22.6], [6.6, 6.6, 0.8, 0.8], color=TUA, lw=1)
T(ax, 15.4, 0.35, 'ion arenium (tidak aromatik)', fs=8.2, c=HJ)
reaksi(ax, 23.2, 26.4, 3.7, '−H$^+$, cepat', fs=8)
gb(ax, 'Brc1ccccc1', 26.8, 31.4, 1.4, 6.2); T(ax, 29.1, 0.6, 'aromatik kembali', fs=8.2, c=HJ)
f.savefig(f'{F}/arenium.png', bbox_inches='tight'); plt.close(f)

# 6. diagram energi SEAr
f, ax = plt.subplots(figsize=(6.0, 3.4), dpi=220)
X = [0, 1.0, 2.0, 3.0, 3.6, 4.2, 5.4]; Y = [1.5, 1.6, 5.2, 3.6, 3.9, 3.6, 3.6]
xx = np.linspace(0, 3.0, 300); ax.plot(xx, PchipInterpolator([0, 1.0, 2.0, 3.0], [1.5, 1.6, 5.2, 3.6])(xx), color=TUA, lw=2.2)
xx = np.linspace(3.0, 5.6, 300); ax.plot(xx, PchipInterpolator([3.0, 3.8, 5.6], [3.6, 4.4, 0.5])(xx), color=HJ, lw=2.2)
ax.plot(xx, PchipInterpolator([3.0, 3.9, 5.6], [3.6, 4.6, 2.6])(xx), color=MERAH, lw=2, ls='--')
ax.text(2.0, 5.4, '‡', ha='center', fontsize=12, color=TUA); ax.text(3.0, 3.2, 'ion arenium', ha='center', fontsize=8.5, color=TUA)
ax.text(0.1, 1.85, 'ArH + E$^+$', fontsize=8.5, color=TUA)
ax.text(5.7, 0.5, 'substitusi:\nArE + H$^+$ (aromatik)', fontsize=8.2, color=HJ, ha='left', va='center')
ax.text(5.7, 2.6, 'adisi: produk\nnonaromatik', fontsize=8.2, color=MERAH, ha='left', va='center')
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('Koordinat reaksi'); ax.set_ylabel('Energi'); ax.set_ylim(0, 6.0); ax.set_xlim(-0.1, 7.3)
plt.tight_layout(); f.savefig(f'{F}/energi.png', bbox_inches='tight'); plt.close(f)

# 7. Friedel-Crafts: alkilasi lawan asilasi-reduksi
f, ax = kanv(7.6, 3.2, (0, 26), (0, 10.6))
gb(ax, 'c1ccccc1', 0, 3.6, 6.6, 10.2); reaksi(ax, 4.0, 9.2, 8.4, 'CH₃CH₂CH₂CH₂Cl, AlCl₃', fs=8)
gb(ax, 'CCC(C)c1ccccc1', 9.6, 14.6, 6.2, 10.6); T(ax, 19.5, 8.4, 'sec-butilbenzena (penataan ulang)\nbukan butilbenzena', fs=8.5, c=MERAH)
gb(ax, 'c1ccccc1', 0, 3.6, 1.0, 4.6); reaksi(ax, 4.0, 8.8, 2.8, 'CH₃CH₂CH₂COCl, AlCl₃', fs=8)
gb(ax, 'CCCC(=O)c1ccccc1', 9.0, 14.4, 0.4, 5.2); reaksi(ax, 14.8, 18.8, 2.8, 'H₂, Pd/C', t2='atau Zn(Hg), HCl', fs=8)
gb(ax, 'CCCCc1ccccc1', 19.2, 24.6, 0.4, 5.2); T(ax, 21.9, 0.2, 'butilbenzena', fs=8.5, c=HJ)
f.savefig(f'{F}/fc.png', bbox_inches='tight'); plt.close(f)

# 8. laju nitrasi (log)
f, ax = plt.subplots(figsize=(6.0, 3.0), dpi=220)
nm = ['–OH', '–CH₃', '–H', '–Cl', '–COOEt', '–NO₂']; v = [1000, 25, 1, 0.033, 0.0037, 6e-8]
cl = [HJ, HJ, '#999999', JG, JT, JT]
ax.bar(range(6), np.log10(v), color=cl, width=0.6)
lab = ['1000', '25', '1', '0,033', '0,0037', '6 × 10$^{-8}$']
for i, (a, t) in enumerate(zip(np.log10(v), lab)): ax.text(i, a + (0.25 if a >= 0 else -0.6), t, ha='center', fontsize=8.5)
ax.axhline(0, color=TUA, lw=0.8); ax.set_xticks(range(6)); ax.set_xticklabels(nm); ax.set_ylabel('log (laju relatif)'); ax.set_ylim(-8.8, 4.2)
ax.text(1.5, 3.0, 'pengaktif', ha='center', color=HJ, fontsize=9); ax.text(4.0, 1.6, 'penonaktif', ha='center', color=JT, fontsize=9)
plt.tight_layout(); f.savefig(f'{F}/laju.png', bbox_inches='tight'); plt.close(f)

# 9. ion arenium dari anisol (o, m, p)
NIT = '[N+](=O)[O-]'
baris = [('orto', ['CO[C+]1C(N)C=CC=C1', 'COC1=CC=C[CH+]C1N', 'COC1=C[CH+]C=CC1N', 'C[O+]=C1C=CC=CC1N']),
         ('meta', ['COC1=CC=CC(N)[CH+]1', 'COC1=CC(N)[CH+]C=C1', 'COC1=CC(N)C=C[CH+]1']),
         ('para', ['CO[C+]1C=CC(N)C=C1', 'COC1=C[CH+]C(N)C=C1', 'COC1=CC(N)[CH+]C=C1', 'C[O+]=C1C=CC(N)C=C1'])]
f, ax = kanv(7.8, 5.6, (0, 27), (0, 19.2))
for r, (nm, sm) in enumerate(baris):
    y = 13.0 - r * 6.4
    T(ax, 0.9, y + 2.4, nm, fs=10, c=TUA, fontweight='bold')
    for k, s in enumerate(sm):
        s2 = s.replace('(N)', '(' + NIT + ')').replace('C1N', 'C1' + NIT)
        x = 2.0 + k * 6.2
        if k == 3: ax.add_patch(FancyBboxPatch((x - 0.1, y - 0.1), 5.4, 5.4, boxstyle='round,pad=0.1', fc='#e8f5ef', ec=HJ, lw=1.3, zorder=0))
        gb(ax, s2, x, x + 5.2, y, y + 5.2, hs=hs_sp3(s2), w=380, h=380, fs=28, bl=32)
        if k < len(sm) - 1: T(ax, x + 5.7, y + 2.6, '↔', fs=13, family='DejaVu Sans')
    if nm == 'meta': T(ax, 21.3, y + 2.6, 'tidak ada struktur\noksonium', fs=8.5, c=MERAH)
T(ax, 22.3, 18.9, 'semua atom beroktet (oksonium)', fs=8.2, c=HJ)
f.savefig(f'{F}/anisol.png', bbox_inches='tight'); plt.close(f)

# 10. distribusi o/m/p
f, ax = plt.subplots(figsize=(6.2, 3.1), dpi=220)
dd = [('toluena', 63, 3, 34), ('klorobenzena', 35, 1, 64), ('fenol', 50, 0, 50), ('nitrobenzena', 7, 91, 2), ('asam benzoat', 22, 76, 2)]
xx = np.arange(len(dd))
for k, (lab, c) in enumerate([('orto', BIRU), ('meta', JT), ('para', HJ)]):
    vals = [d[1 + k] for d in dd]; ax.bar(xx + (k - 1) * 0.26, vals, 0.25, color=c, label=lab)
    for xi, vv in zip(xx + (k - 1) * 0.26, vals): ax.text(xi, vv + 1.5, str(vv), ha='center', fontsize=7)
for yv, c in [(40, '#888888'), (20, '#bbbbbb')]: ax.axhline(yv, color=c, lw=0.8, ls='--')
ax.text(2.0, 42.0, 'nilai statistik o, m (40%)', fontsize=7, color='#888888', ha='center'); ax.text(2.0, 22.0, 'nilai statistik p (20%)', fontsize=7, color='#888888', ha='center')
ax.set_xticks(xx); ax.set_xticklabels([d[0] for d in dd], fontsize=8.5); ax.set_ylabel('% produk nitrasi'); ax.set_ylim(0, 115)
ax.legend(frameon=False, fontsize=8, ncol=3, loc='upper center')
plt.tight_layout(); f.savefig(f'{F}/omp.png', bbox_inches='tight'); plt.close(f)

# 11. Meisenheimer
f, ax = kanv(7.8, 2.4, (0, 30), (0, 9.0))
gb(ax, 'Fc1ccc([N+](=O)[O-])cc1[N+](=O)[O-]', 0, 5.0, 1.6, 7.4); T(ax, 6.6, 5.6, '+ CH₃O$^-$', fs=9, c=BIRU)
reaksi(ax, 5.4, 8.0, 4.5, 'lambat', fs=7.5)
gb(ax, 'COC1(F)[CH-]C=C([N+](=O)[O-])C=C1[N+](=O)[O-]', 8.4, 14.4, 1.2, 8.0); T(ax, 14.9, 4.6, '↔', fs=13, family='DejaVu Sans')
gb(ax, 'COC1(F)C=CC(=[N+]([O-])[O-])C=C1[N+](=O)[O-]', 15.2, 21.2, 1.2, 8.0)
ax.plot([8.3, 8.1, 8.1, 8.3], [8.0, 8.0, 1.0, 1.0], color=TUA, lw=1); ax.plot([21.3, 21.5, 21.5, 21.3], [8.0, 8.0, 1.0, 1.0], color=TUA, lw=1)
T(ax, 14.8, 0.5, 'kompleks Meisenheimer (muatan − sampai ke O gugus nitro)', fs=8, c=HJ)
reaksi(ax, 21.8, 23.6, 4.5, '−F$^-$', fs=8)
gb(ax, 'COc1ccc([N+](=O)[O-])cc1[N+](=O)[O-]', 23.8, 29.6, 1.6, 7.4)
f.savefig(f'{F}/meisenheimer.png', bbox_inches='tight'); plt.close(f)

# 12. benzuna
f, ax = kanv(7.6, 2.8, (0, 28), (0, 10.2))
gb(ax, 'Clc1ccccc1', 0, 4.6, 2.8, 7.4, note={1: '*'}); reaksi(ax, 4.8, 7.8, 5.1, 'NH₂$^-$', t2='−NH₃, −Cl$^-$', fs=8)
cx, cy, r = 10.2, 5.1, 1.5
th = np.pi / 2 + np.pi / 3 * np.arange(6); P = np.c_[cx + r * np.cos(th), cy + r * np.sin(th)]
ax.add_patch(Polygon(P, closed=True, fc='none', ec=TUA, lw=1.6)); ax.add_patch(Circle((cx, cy), 0.85, fc='none', ec=TUA, lw=1.2))
q0, q1 = P[4], P[5]; n = (np.array([q0[0] + q1[0], q0[1] + q1[1]]) / 2 - [cx, cy]); n = n / np.linalg.norm(n) * 0.32
ax.plot([q0[0] + n[0], q1[0] + n[0]], [q0[1] + n[1], q1[1] + n[1]], color=MERAH, lw=1.6)
ax.text(q1[0] + 0.35, q1[1] - 0.1, '*', fontsize=12, color=JT)
T(ax, cx, 2.6, 'benzuna', fs=8.5, c=HJ); T(ax, cx, 1.3, 'ikatan π tambahan\n(sp² di bidang cincin)', fs=7, c=MERAH)
ax.annotate('', (17.6, 7.8), (12.4, 6.0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.2)); ax.annotate('', (17.6, 2.4), (12.4, 4.2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.2))
T(ax, 14.4, 7.9, 'NH₂$^-$; NH₃', fs=8); T(ax, 14.4, 2.1, 'NH₂$^-$; NH₃', fs=8)
gb(ax, 'Nc1ccccc1', 17.6, 22.2, 5.4, 10.0, note={1: '*'}); gb(ax, 'Nc1ccccc1', 17.6, 22.2, 0.2, 4.8, note={2: '*'})
T(ax, 25.2, 7.7, 'NH₂ pada C bertanda\n(± 50%)', fs=8.5, c=HJ); T(ax, 25.2, 2.5, 'NH₂ di sebelah\nC bertanda (± 50%)', fs=8.5, c=HJ)
T(ax, 2.3, 2.2, '* = ¹⁴C', fs=8.5, c=JT)
f.savefig(f'{F}/benzuna.png', bbox_inches='tight'); plt.close(f)

# 13. urutan sintesis bromonitrobenzena
f, ax = kanv(7.6, 3.2, (0, 26), (0, 10.6))
for y, a, ra, b, rb, c, lab, col in [(8.2, 'c1ccccc1', 'HNO₃, H₂SO₄', 'O=[N+]([O-])c1ccccc1', 'Br₂, FeBr₃', 'O=[N+]([O-])c1cccc(Br)c1', '1-bromo-3-nitrobenzena (meta)', BIRU),
                                     (2.6, 'c1ccccc1', 'Br₂, FeBr₃', 'Brc1ccccc1', 'HNO₃, H₂SO₄', 'O=[N+]([O-])c1ccc(Br)cc1', '1-bromo-4-nitrobenzena (+ orto)', HJ)]:
    gb(ax, a, 0, 3.4, y - 1.7, y + 1.7); reaksi(ax, 3.6, 7.2, y, ra, fs=8)
    gb(ax, b, 7.4, 11.6, y - 2.0, y + 2.0); reaksi(ax, 11.8, 15.4, y, rb, fs=8)
    gb(ax, c, 15.6, 20.6, y - 2.2, y + 2.2); T(ax, 23.3, y, lab.replace(' (', '\n('), fs=8.5, c=col)
f.savefig(f'{F}/sintesis.png', bbox_inches='tight'); plt.close(f)
print('ok')
