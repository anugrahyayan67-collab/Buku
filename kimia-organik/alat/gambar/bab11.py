# Gambar Bab 11: gugus karbonil, mekanisme adisi, hidrat, asetal, glukosa, pH imina, stereo reduksi,
# Wolff-Kishner/Clemmensen, Wittig, Baeyer-Villiger, keto-enol, peta karbonil
import os, io, numpy as np, matplotlib, matplotlib.ticker
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Arc
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab11/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
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
def rd(smi, w=360, h=300, fs=30, hs=(), pad=0.15, lab=None):
    m = Chem.MolFromSmiles(smi)
    if hs: m = Chem.AddHs(m, onlyOnAtoms=tuple(hs))
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = pad
    o.updateAtomPalette({35: (0.71, 0.33, 0.11), 8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.10, 0.54, 0.42), 15: (0.55, 0.35, 0.65), 53: (0.45, 0.2, 0.6), 1: (0.05, 0.15, 0.28)})
    if lab:
        for i, t in lab.items(): o.atomLabels[i] = t
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))
def gb(ax, smi, x0, x1, y0, y1, **k): ax.imshow(rd(smi, **k), extent=[x0, x1, y0, y1], zorder=2)

# 1. gugus karbonil
f, ax = kanv(7.2, 2.4, (0, 24), (0, 8))
gb(ax, 'CC(C)=O', 0, 4.2, 1.6, 6.4); T(ax, 4.8, 4.0, '↔', fs=15, family='DejaVu Sans'); gb(ax, 'C[C+](C)[O-]', 5.4, 9.6, 1.6, 6.4)
T(ax, 4.8, 1.0, 'karbon δ+ (elektrofil), oksigen δ−', fs=8.5, c=HJ)
cx, cy = 16.0, 3.4
ax.plot([cx - 1.6, cx], [cy + 0.9, cy], color=TUA, lw=2); ax.plot([cx - 1.6, cx], [cy - 0.9, cy], color=TUA, lw=2)
ax.plot([cx, cx + 2.2], [cy + 0.08, cy + 0.08], color=JT, lw=2); ax.plot([cx, cx + 2.2], [cy - 0.08, cy - 0.08], color=JT, lw=2)
T(ax, cx + 2.6, cy, 'O', c=JT, fs=13); T(ax, cx - 0.1, cy - 0.55, 'C', fs=11)
ang = np.deg2rad(107); L = 3.6; nx, ny = cx + L * np.cos(ang), cy + L * np.sin(ang)
ax.annotate('', (cx - 0.05, cy + 0.25), (nx, ny), arrowprops=dict(arrowstyle='-|>', color=BIRU, lw=1.5)); T(ax, nx - 0.3, ny + 0.4, 'Nu$^-$', c=BIRU, fs=12)
ax.add_patch(Arc((cx, cy), 2.4, 2.4, theta1=0, theta2=107, color=HJ, lw=1)); T(ax, cx + 1.2, cy + 1.35, '≈107°', fs=9, c=HJ)
T(ax, cx + 0.3, 0.6, 'arah serangan ke orbital π*', fs=8.5, c=HJ)
f.savefig(f'{F}/karbonil.png', bbox_inches='tight'); plt.close(f)

# 2. mekanisme basa dan asam
f, ax = kanv(7.8, 3.6, (0, 30), (0, 13.6))
y = 10.4
gb(ax, 'CC(C)=O', 0, 3.6, y - 1.8, y + 1.8); T(ax, 4.3, y, '+ CN$^-$', fs=10, c=BIRU); reaksi(ax, 5.2, 7.6, y, 'serang')
gb(ax, 'CC(C)([O-])C#N', 7.8, 12.2, y - 2.0, y + 2.0); reaksi(ax, 12.6, 15.4, y, 'HCN', t2='(transfer H⁺)'.replace('⁺', '$^+$'))
gb(ax, 'CC(C)(O)C#N', 15.8, 20.2, y - 2.0, y + 2.0); T(ax, 24.6, y, 'basa: Nu kuat\nmenyerang dulu', fs=9, c=BIRU)
y = 3.4
gb(ax, 'CC(C)=O', 0, 3.6, y - 1.8, y + 1.8); reaksi(ax, 4.0, 6.0, y, 'H$^+$')
gb(ax, 'CC(C)=[OH+]', 6.2, 9.8, y - 1.8, y + 1.8); reaksi(ax, 10.2, 12.4, y, 'H₂O')
gb(ax, 'CC(C)(O)[OH2+]', 12.6, 16.8, y - 2.0, y + 2.0); reaksi(ax, 17.2, 19.4, y, '−H$^+$')
gb(ax, 'CC(C)(O)O', 19.6, 23.4, y - 2.0, y + 2.0); T(ax, 26.8, y, 'asam: C=O diaktifkan\ndulu, Nu lemah', fs=9, c=JT)
f.savefig(f'{F}/mekanisme.png', bbox_inches='tight'); plt.close(f)

# 3. konstanta hidrasi
f, ax = plt.subplots(figsize=(6.0, 3.0), dpi=220)
nm = ['heksafluoro-\naseton', 'kloral', 'formaldehida', 'asetaldehida', 'aseton']; K = [1.2e6, 2.8e4, 2.3e3, 1.06, 1.4e-3]
cl = [HJ, HJ, BIRU, JG, JT]
ax.bar(range(5), np.log10(K), color=cl, width=0.6)
lab = ['1,2 × 10$^6$', '2,8 × 10$^4$', '2,3 × 10$^3$', '1,06', '1,4 × 10$^{-3}$']
for i, (v, t) in enumerate(zip(np.log10(K), lab)): ax.text(i, v + (0.25 if v >= 0 else -0.6), t, ha='center', fontsize=8.5)
ax.axhline(0, color=TUA, lw=0.8); ax.set_xticks(range(5)); ax.set_xticklabels(nm, fontsize=8.5); ax.set_ylabel('log $K_\\mathrm{hid}$'); ax.set_ylim(-3.8, 7.2)
ax.text(3.9, 3.0, 'K > 1: hidrat dominan', fontsize=8, color=HJ, ha='center'); ax.text(1.0, -2.0, 'K < 1: karbonil dominan', fontsize=8, color=JT, ha='center')
plt.tight_layout(); f.savefig(f'{F}/hidrat.png', bbox_inches='tight'); plt.close(f)

# 4. asetal
f, ax = kanv(7.8, 3.4, (0, 30), (0, 12.6))
y = 9.4
gb(ax, 'CC=O', 0, 3.0, y - 1.5, y + 1.5); reaksi(ax, 3.3, 6.0, y, 'CH₃OH, H$^+$', dua=True, fs=8)
gb(ax, 'CC(O)OC', 6.2, 10.2, y - 1.9, y + 1.9); T(ax, 8.2, y - 2.3, 'hemiasetal', fs=8.5, c=HJ)
reaksi(ax, 10.5, 13.4, y, 'H$^+$, −H₂O', dua=True, fs=8)
gb(ax, 'C[CH]=[O+]C', 13.6, 17.4, y - 1.6, y + 1.6); T(ax, 15.5, y - 2.3, 'ion oksokarbenium', fs=8.5, c=HJ)
reaksi(ax, 17.7, 20.8, y, 'CH₃OH, −H$^+$', dua=True, fs=8)
gb(ax, 'CC(OC)OC', 21.0, 25.4, y - 1.9, y + 1.9); T(ax, 23.2, y - 2.3, 'asetal', fs=8.5, c=HJ)
y = 3.0
gb(ax, 'O=C1CCCCC1', 2.0, 5.8, y - 1.9, y + 1.9); T(ax, 6.6, y, '+', fs=12); gb(ax, 'OCCO', 7.2, 10.4, y - 1.4, y + 1.4)
reaksi(ax, 10.8, 15.4, y, 'TsOH, −H₂O', t2='H₃O$^+$ (balik)', dua=True, fs=8)
gb(ax, 'C1CCC2(CC1)OCCO2', 15.8, 20.6, y - 2.2, y + 2.2); T(ax, 24.6, y, 'asetal siklik:\ntahan basa dan\nnukleofil', fs=8.5, c=HJ)
f.savefig(f'{F}/asetal.png', bbox_inches='tight'); plt.close(f)

# 5. glukosa
f, ax = kanv(7.2, 2.8, (0, 26), (0, 10))
gb(ax, 'O=C[C@H](O)[C@@H](O)[C@H](O)[C@H](O)CO', 0, 9.0, 0.8, 9.6, w=520, h=420, fs=26); T(ax, 4.5, 0.5, 'D-glukosa rantai terbuka (< 0,003%)', fs=8.2, c=JT)
reaksi(ax, 9.6, 13.0, 5.2, 'O5 menyerang C1', dua=True, fs=8)
gb(ax, 'OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O', 13.4, 22.0, 0.8, 9.6, w=520, h=460, fs=26); T(ax, 17.7, 0.5, 'β-D-glukopiranosa (64%)', fs=8.2, c=HJ)
T(ax, 24.4, 5.2, '+ anomer α\n(36%)', fs=8.5)
f.savefig(f'{F}/glukosa.png', bbox_inches='tight'); plt.close(f)

# 6. laju pembentukan imina terhadap pH (model)
pH = np.linspace(0, 10, 400); H = 10 ** -pH
k1 = 1 / (1 + H / 10 ** -5.0)          # fraksi amina bebas (pKaH model 5)
k2 = H / 10 ** -4.6                     # dehidrasi dikatalisis asam
v = 1 / (1 / k1 + 1 / k2); v = v / v.max()
f, ax = plt.subplots(figsize=(5.4, 2.9), dpi=220)
ax.plot(pH, v, color=BIRU, lw=2.2); ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda t, _: f'{t:.1f}'.replace('.', ','))); ax.set_xlabel('pH'); ax.set_ylabel('laju relatif'); ax.set_ylim(0, 1.15); ax.set_xlim(0, 10)
i = np.argmax(v); ax.axvline(pH[i], color='#999999', lw=0.8, ls=':')
ax.text(1.2, 0.55, 'amina\nterprotonasi\n(RNH$_3^+$)', fontsize=8, color=JT, ha='center'); ax.text(8.3, 0.55, 'dehidrasi\nkurang asam', fontsize=8, color=JT, ha='center')
ax.text(pH[i], 1.07, 'maksimum ± pH ' + f'{pH[i]:.1f}'.replace('.', ','), fontsize=8, color=TUA, ha='center')
plt.tight_layout(); f.savefig(f'{F}/imina.png', bbox_inches='tight'); plt.close(f)

# 7. stereokimia reduksi 4-tert-butilsikloheksanon
f, ax = kanv(7.2, 3.2, (0, 24), (0, 10.4))
gb(ax, 'CC(C)(C)C1CCC(=O)CC1', 0, 5.6, 2.8, 7.6)
ax.annotate('', (11.0, 8.2), (6.0, 6.0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 7.6, 8.1, 'NaBH₄ (kecil)', fs=8.5)
ax.annotate('', (11.0, 2.2), (6.0, 4.4), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 7.6, 2.3, 'L-Selectride (besar)', fs=8.5)
gb(ax, 'CC(C)(C)[C@H]1CC[C@H](O)CC1', 11.2, 16.8, 5.6, 10.4, hs=(4, 7)); T(ax, 20.4, 8.0, 'trans (OH ekuatorial)\n± 90%', fs=8.5, c=HJ)
gb(ax, 'CC(C)(C)[C@H]1CC[C@@H](O)CC1', 11.2, 16.8, 0.0, 4.8, hs=(4, 7)); T(ax, 20.4, 2.4, 'cis (OH aksial)\nutama', fs=8.5, c=JT)
f.savefig(f'{F}/stereo.png', bbox_inches='tight'); plt.close(f)

# 8. Wolff-Kishner dan Clemmensen
f, ax = kanv(7.6, 3.0, (0, 28), (0, 10.4))
gb(ax, 'CCC(=O)c1ccccc1', 0, 5.2, 2.8, 7.6)
ax.annotate('', (10.0, 8.4), (5.6, 6.2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 7.4, 8.4, 'H₂NNH₂', fs=8.5)
gb(ax, 'CCC(=NN)c1ccccc1', 10.2, 15.4, 6.0, 10.4); T(ax, 12.8, 5.7, 'hidrazon', fs=8, c=HJ)
ax.annotate('', (21.0, 6.4), (15.8, 8.2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 18.9, 8.4, 'KOH, 200 °C, −N₂', fs=8)
ax.annotate('', (21.0, 4.0), (5.6, 4.0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.3)); T(ax, 12.8, 2.5, 'Zn(Hg), HCl pekat (Clemmensen, asam)', fs=8.5)
gb(ax, 'CCCc1ccccc1', 20.6, 25.8, 2.8, 7.6); T(ax, 23.2, 2.4, 'propilbenzena', fs=8.5, c=HJ)
T(ax, 6.5, 0.6, 'Wolff–Kishner (basa) di atas; Clemmensen (asam) di bawah', fs=8, c=TUA)
f.savefig(f'{F}/wk.png', bbox_inches='tight'); plt.close(f)

# 9. Wittig
f, ax = kanv(7.8, 3.2, (0, 30), (0, 11.6))
y = 9.0
T(ax, 1.4, y, 'Ph₃P', fs=11); T(ax, 4.0, y, '+  CH₃I', fs=10); reaksi(ax, 5.4, 7.6, y, 'SN2')
T(ax, 10.6, y, 'Ph₃P$^+$–CH₃  I$^-$', fs=10); reaksi(ax, 13.4, 15.4, y, 'BuLi')
T(ax, 18.8, y + 0.4, 'Ph₃P=CH₂', fs=11, c=BIRU); T(ax, 18.8, y - 0.5, '(Ph₃P$^+$–CH₂$^-$)', fs=8.5, c=BIRU); T(ax, 24.5, y, 'ilida', fs=9, c=HJ)
y = 3.2
gb(ax, 'O=C1CCCCC1', 0, 3.8, y - 1.9, y + 1.9); T(ax, 5.6, y + 0.6, '+ Ph₃P=CH₂', fs=9, c=BIRU); reaksi(ax, 4.4, 8.4, y)
gb(ax, 'C1CCC2(CC1)CP(C)(C)(C)O2', 8.6, 13.4, y - 2.4, y + 2.4, lab={8: 'Ph', 9: 'Ph', 10: 'Ph'}); T(ax, 11.0, 0.3, 'oksafosfetana', fs=8.2, c=HJ)
reaksi(ax, 13.8, 16.0, y)
gb(ax, 'C=C1CCCCC1', 16.2, 20.0, y - 1.9, y + 1.9); T(ax, 22.8, y, '+ Ph₃P=O', fs=10, c=JT); T(ax, 22.8, y - 1.0, '(P=O sangat kuat)', fs=8, c=JT)
T(ax, 18.1, 0.6, 'C=C tepat di tempat C=O', fs=8.2, c=HJ)
f.savefig(f'{F}/wittig.png', bbox_inches='tight'); plt.close(f)

# 10. Baeyer-Villiger
f, ax = kanv(7.6, 3.2, (0, 28), (0, 11.2))
y = 8.4
gb(ax, 'O=C1CCCCC1', 0, 3.8, y - 1.9, y + 1.9); reaksi(ax, 4.2, 7.8, y, 'mCPBA')
gb(ax, 'O=C1CCCCCO1', 8.2, 12.4, y - 2.1, y + 2.1); T(ax, 16.8, y, 'ε-kaprolakton\n(O disisipkan ke cincin)', fs=8.5, c=HJ)
y = 2.8
gb(ax, 'CC(=O)c1ccccc1', 0, 4.6, y - 1.9, y + 1.9); reaksi(ax, 5.0, 7.8, y, 'mCPBA')
gb(ax, 'CC(O)(OOC(=O)c1cccc(Cl)c1)c1ccccc1', 8.0, 15.0, y - 2.6, y + 2.6, w=520, h=360, fs=24); T(ax, 11.5, 0.1, 'zat antara Criegee', fs=8, c=BIRU)
reaksi(ax, 15.4, 18.6, y, 'fenil', t2='bermigrasi', fs=8)
gb(ax, 'CC(=O)Oc1ccccc1', 19.0, 23.6, y - 1.9, y + 1.9); T(ax, 25.8, y, 'fenil asetat', fs=8.5, c=HJ)
f.savefig(f'{F}/bv.png', bbox_inches='tight'); plt.close(f)

# 11. keto-enol
f, ax = kanv(7.8, 3.4, (0, 30), (0, 12.4))
y = 9.2
gb(ax, 'CC(C)=O', 0, 3.6, y - 1.8, y + 1.8); reaksi(ax, 4.0, 6.6, y, 'OH$^-$', t2='−H₂O', fs=8)
gb(ax, '[CH2-]C(C)=O', 6.8, 10.4, y - 1.8, y + 1.8); T(ax, 11.0, y, '↔', fs=13, family='DejaVu Sans'); gb(ax, 'C=C(C)[O-]', 11.6, 15.2, y - 1.8, y + 1.8)
T(ax, 11.0, y - 2.4, 'ion enolat (resonansi)', fs=8.2, c=BIRU)
reaksi(ax, 15.6, 18.4, y, 'H₂O', t2='−OH$^-$', fs=8)
gb(ax, 'C=C(C)O', 18.6, 22.2, y - 1.8, y + 1.8); T(ax, 25.8, y, 'enol (sangat sedikit\npada aseton)', fs=8.5, c=HJ)
y = 3.0
gb(ax, 'CC(C)=O', 0, 3.6, y - 1.8, y + 1.8); reaksi(ax, 4.0, 6.6, y, 'H$^+$', fs=8)
gb(ax, 'CC(C)=[OH+]', 6.8, 10.4, y - 1.8, y + 1.8); reaksi(ax, 10.8, 13.6, y, 'H₂O', t2='−H₃O$^+$ (H α)', fs=8)
gb(ax, 'C=C(C)O', 13.8, 17.4, y - 1.8, y + 1.8); T(ax, 22.6, y, 'asam: protonasi O dulu,\nlalu H α lepas', fs=8.5, c=JT)
f.savefig(f'{F}/enol.png', bbox_inches='tight'); plt.close(f)

# 12. peta karbonil
f, ax = kanv(7.6, 6.6, (-12.6, 12.6), (-11.0, 10.6))
ax.add_patch(FancyBboxPatch((-2.3, -0.9), 4.6, 1.8, boxstyle='round,pad=0.25', fc=TUA, ec=TUA)); T(ax, 0, 0, 'ALDEHIDA\nKETON', c='white', fs=10.5, fontweight='bold')
items = [('alkohol', 'NaBH₄; LiAlH₄', JT), ('alkohol (C–C baru)', 'RMgX; RLi', HJ), ('alkohol propargilik', 'RC≡C$^-$', HJ), ('sianohidrin', 'HCN, KCN', HJ),
         ('alkena (Wittig)', 'Ph₃P=CR₂', HJ), ('hidrat', 'H₂O', JT), ('asetal', '2 ROH, H$^+$', JT), ('imina / enamina', 'RNH₂ / R₂NH', JT),
         ('oksim, hidrazon', 'NH₂OH; NH₂NH₂', JT), ('alkana (CH₂)', 'Wolff–Kishner atau\nClemmensen', JT), ('ester / lakton', 'mCPBA', JT),
         ('asam karboksilat', 'Jones; haloform', JT), ('keton α-halo', 'X₂, H$^+$', JT)]
n = len(items)
for i, (p, r, c) in enumerate(items):
    th = np.pi / 2 - 2 * np.pi * i / n; x, y = 10.0 * np.cos(th), 9.0 * np.sin(th)
    ax.annotate('', (x * 0.76, y * 0.80), (x * 0.24, y * 0.12), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.2))
    ax.add_patch(FancyBboxPatch((x - 2.15, y - 0.85), 4.3, 1.7, boxstyle='round,pad=0.1', fc='white', ec=c, lw=1.1))
    T(ax, x, y + 0.32, p, c=c, fs=7.8, fontweight='bold'); T(ax, x, y - 0.38, r, fs=6.4)
T(ax, 0, -10.6, 'hijau: reaksi pembentuk ikatan C–C', c=HJ, fs=8.5)
f.savefig(f'{F}/peta.png', bbox_inches='tight'); plt.close(f)
print('ok')
