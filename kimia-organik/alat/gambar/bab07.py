# Gambar Bab 7: selektivitas radikal, NBS, SN2, laju SN2, SN1, E2, E2 sikloheksana, peta keputusan
import os, io, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Ellipse, FancyBboxPatch, Circle
from scipy.interpolate import CubicSpline
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab07/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'

def T(ax, x, y, s, c=TUA, fs=11, **k): ax.text(x, y, s, ha='center', va='center', color=c, fontsize=fs, **k)
def ikat(ax, p, q, jenis='-', c=TUA, lw=1.8, sh=(0.12, 0.12)):
    p, q = np.array(p, float), np.array(q, float); d = q - p; L = np.linalg.norm(d); u = d / L
    a, b = p + u * sh[0], q - u * sh[1]
    if jenis == '-': ax.plot(*zip(a, b), color=c, lw=lw)
    elif jenis == 'baji':
        n = np.array([-u[1], u[0]]) * 0.09; ax.add_patch(Polygon([a, b + n, b - n], fc=c, ec=c))
    elif jenis == 'putus':
        n = np.array([-u[1], u[0]])
        for t in np.linspace(0.1, 1, 7): m = a + (b - a) * t; w = 0.09 * t; ax.plot([m[0] - n[0] * w, m[0] + n[0] * w], [m[1] - n[1] * w, m[1] + n[1] * w], color=c, lw=1.3)
    elif jenis == 'separuh': ax.plot(*zip(a, b), color=c, lw=lw, ls=(0, (2, 2)))
def panah(ax, p, q, rad=0.4, c=MERAH, lw=1.4):
    ax.add_patch(FancyArrowPatch(p, q, connectionstyle=f'arc3,rad={rad}', arrowstyle='-|>', mutation_scale=11, color=c, lw=lw))
def reaksi(ax, x1, x2, y, t='', c=TUA):
    ax.annotate('', (x2, y), (x1, y), arrowprops=dict(arrowstyle='-|>', color=c, lw=1.3))
    if t: T(ax, (x1 + x2) / 2, y + 0.3, t, fs=8.5)
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax

# 1. selektivitas radikal
f, ax = plt.subplots(1, 2, figsize=(7.2, 2.8), dpi=220)
dat = [('propana', ['1-halo', '2-halo'], [45.5, 54.5], [3.5, 96.5]), ('2-metilpropana', ['1-halo-2-metil', '2-halo-2-metil'], [64.3, 35.7], [0.6, 99.4])]
for a, (judul, lab, cl, br) in zip(ax, dat):
    x = np.arange(2); a.bar(x - 0.18, cl, 0.34, color=HJ, label='Cl₂, cahaya (25 °C)'); a.bar(x + 0.18, br, 0.34, color=JT, label='Br₂, cahaya (125 °C)')
    for xi, v in zip(x - 0.18, cl): a.text(xi, v + 2, f'{v:g}'.replace('.', ','), ha='center', fontsize=7.5)
    for xi, v in zip(x + 0.18, br): a.text(xi, v + 2, f'{v:g}'.replace('.', ','), ha='center', fontsize=7.5)
    a.set_xticks(x); a.set_xticklabels(lab, fontsize=8.5); a.set_ylim(0, 112); a.set_title(judul, fontsize=9.5, color=TUA); a.set_ylabel('% produk')
ax[0].legend(frameon=False, fontsize=7.5, loc='upper left')
plt.tight_layout(); f.savefig(f'{F}/radsel.png', bbox_inches='tight'); plt.close(f)

def rd(smi, w=360, h=300, fs=30):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 3; o.fixedFontSize = fs; o.padding = 0.18
    o.updateAtomPalette({35: (0.71, 0.33, 0.11), 8: (0.71, 0.33, 0.11)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))

# 2. NBS sikloheksena
f, ax = plt.subplots(figsize=(7.4, 1.9), dpi=220); ax.set_xlim(0, 20); ax.set_ylim(0, 5); ax.axis('off')
for x0, smi in [(0.0, 'C1=CCCCC1'), (5.6, '[CH]1C=CCCC1'), (10.0, '[CH]1CCCC=C1'), (15.6, 'BrC1C=CCCC1')]:
    ax.imshow(rd(smi), extent=[x0, x0 + 4.2, 0.2, 4.6])
reaksi(ax, 4.1, 5.6, 2.4, 'Br·'); T(ax, 9.8, 2.4, '↔', fs=16); reaksi(ax, 14.2, 15.6, 2.4, 'Br₂')
T(ax, 9.8, 0.25, 'radikal alilik (dua penyumbang setara)', fs=8, c=HJ)
f.savefig(f'{F}/nbs.png', bbox_inches='tight'); plt.close(f)

# 3. SN2: Nu dari belakang, keadaan transisi, inversi
f, ax = kanv(7.6, 2.6, (0, 22), (-3.2, 3.6))
def pusat(ax, cx, cy, arah, gugus=('H', 'CH₃', 'C₂H₅')):
    # arah = -1: payung menghadap kiri (gugus condong ke kiri); +1 ke kanan
    ujung = [(cx + arah * 0.55, cy + 1.25), (cx + arah * 1.0, cy - 0.75), (cx - arah * 0.35, cy - 1.3)]
    jen = ['-', 'baji', 'putus']
    for (x, y), j, g in zip(ujung, jen, gugus):
        ikat(ax, (cx, cy), (x, y), j, sh=(0.16, 0.0)); T(ax, x + arah * 0.35 * (1 if g != 'H' else 0.6), y + (0.25 if y > cy else -0.25), g, fs=9)
    T(ax, cx, cy, 'C', fs=12)
T(ax, 1.0, 0, 'HO$^-$', c=BIRU, fs=12); pusat(ax, 4.3, 0, -1); ikat(ax, (4.3, 0), (6.1, 0)); T(ax, 6.5, 0, 'Br', c=JT, fs=12)
panah(ax, (1.55, 0.35), (3.9, 0.25), rad=-0.35); panah(ax, (5.1, -0.15), (6.45, -0.4), rad=0.45)
reaksi(ax, 7.4, 8.6, 0)
# keadaan transisi
cx = 12.0; T(ax, 9.9, 0, 'HO', c=BIRU, fs=11); ikat(ax, (10.3, 0), (cx, 0), 'separuh'); ikat(ax, (cx, 0), (13.8, 0), 'separuh'); T(ax, 14.2, 0, 'Br', c=JT, fs=11)
for (x, y), j, g in zip([(cx, 1.35), (cx - 0.7, -1.0), (cx + 0.7, -1.0)], ['-', 'baji', 'putus'], ['H', 'CH₃', 'C₂H₅']):
    ikat(ax, (cx, 0), (x, y), j, sh=(0.16, 0)); T(ax, x, y + (0.3 if y > 0 else -0.3), g, fs=9)
T(ax, cx, 0, 'C', fs=12); ax.plot([9.6, 9.4, 9.4, 9.6], [1.9, 1.9, -1.9, -1.9], color=TUA, lw=1); ax.plot([14.6, 14.8, 14.8, 14.6], [1.9, 1.9, -1.9, -1.9], color=TUA, lw=1); T(ax, 15.05, 1.95, '‡', fs=12)
T(ax, cx + 0.2, 0.4, 'δ−', fs=7.5, c=BIRU); 
reaksi(ax, 15.3, 16.5, 0)
pusat(ax, 19.3, 0, 1); ikat(ax, (17.9, 0), (19.3, 0)); T(ax, 17.5, 0, 'HO', c=BIRU, fs=12); T(ax, 21.3, -2.7, '+ Br$^-$', c=JT, fs=11)
T(ax, 4.3, 3.2, 'nukleofil menyerang dari belakang', fs=8.2, c=HJ); T(ax, 19.3, 3.2, 'konfigurasi terbalik', fs=8.2, c=HJ)
f.savefig(f'{F}/sn2.png', bbox_inches='tight'); plt.close(f)

# 4. laju SN2
f, ax = plt.subplots(figsize=(5.4, 2.8), dpi=220)
lab = ['metil', 'etil\n(1°)', 'isobutil\n(1°, cabang β)', 'isopropil\n(2°)', 'neopentil', 'tert-butil\n(3°)']; val = [30, 1, 0.03, 0.03, 1e-5, 1e-8]
ax.bar(range(6), val, color=[HJ, BIRU, BIRU, MUDA, JG, '#c9d2db']); ax.set_yscale('log'); ax.set_ylim(1e-8, 300)
for i, v in enumerate(val): ax.text(i, v * 1.6, ['30', '1', '0,03', '0,03', '$10^{-5}$', '≈ 0'][i], ha='center', fontsize=8, color=TUA)
ax.set_xticks(range(6)); ax.set_xticklabels(lab, fontsize=7.6); ax.set_ylabel('laju relatif SN2 (log)')
ax.set_yticks([1e-8, 1e-6, 1e-4, 1e-2, 1, 100]); ax.set_yticklabels(['$10^{-8}$', '$10^{-6}$', '$10^{-4}$', '$10^{-2}$', '1', '$10^{2}$'])
f.savefig(f'{F}/sn2laju.png', bbox_inches='tight'); plt.close(f)

# 5. diagram energi SN1
f, ax = plt.subplots(figsize=(5.8, 2.9), dpi=220)
X = [0, 1, 2, 3, 4, 5, 6, 7]; Y = [1.5, 1.6, 6.2, 4.4, 5.0, 2.2, 2.6, 0.6]; xx = np.linspace(0, 7, 600)
ax.plot(xx, CubicSpline(X, Y, bc_type='clamped')(xx), color=BIRU, lw=2)
for x, y, t in [(2, 6.5, '‡₁ (lambat)'), (4, 5.35, '‡₂'), (6, 2.95, '‡₃')]: T(ax, x, y, t, fs=8.5, c=JT)
for x, y, t in [(0.2, 1.1, 'R₃C–Br\n+ H₂O'), (3, 3.85, 'R$_3$C$^+$'), (5, 1.6, 'R$_3$C–OH$_2^+$'), (7, 0.1, 'R$_3$C–OH\n+ H$_3$O$^+$')]: T(ax, x, y, t, fs=8)
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('koordinat reaksi'); ax.set_ylabel('energi'); ax.set_ylim(-0.6, 7.2)
f.savefig(f'{F}/sn1energi.png', bbox_inches='tight'); plt.close(f)

# 6. SN1 stereokimia: karbokation datar diserang dari atas/bawah
f, ax = kanv(7.0, 2.8, (0, 19), (-3.6, 3.8))
cx, cy = 5.0, 0
for s in (1, -1): ax.add_patch(Ellipse((cx, cy + 0.85 * s), 0.7, 1.5, fc='white', ec=TUA, lw=1.1))
for (x, y), g, dx, dy in [((cx - 1.4, 0.15), 'CH₃', -0.5, 0), ((cx + 1.4, 0.15), 'C₂H₅', 0.55, 0), ((cx + 1.0, -0.65), 'C₃H₇', 0.6, -0.25)]:
    ikat(ax, (cx, cy), (x, y), '-', sh=(0.25, 0)); T(ax, x + dx, y + dy, g, fs=8.5)
T(ax, cx, cy, 'C$^+$', fs=11, c=JT)
T(ax, cx - 2.4, 3.0, 'Nu$^-$', c=BIRU); T(ax, cx - 2.4, -3.0, 'Nu$^-$', c=BIRU)
panah(ax, (cx - 2.0, 2.8), (cx - 0.15, 1.75), rad=-0.3, c=BIRU); panah(ax, (cx - 2.0, -2.8), (cx - 0.15, -1.75), rad=0.3, c=BIRU)
reaksi(ax, 8.2, 10.0, 1.6); reaksi(ax, 8.2, 10.0, -1.6)
T(ax, 13.7, 1.7, 'Nu di atas', fs=9.5); T(ax, 13.7, -1.5, 'Nu di bawah', fs=9.5)
T(ax, 13.7, 0.1, 'enansiomer', fs=8.5, c=HJ); T(ax, 17.6, 1.7, '≈ 50%', fs=9, c=TUA); T(ax, 17.6, -1.5, '≈ 50%', fs=9, c=TUA)
T(ax, cx, 3.5, 'karbokation datar (sp²), orbital p kosong', fs=8.2, c=HJ)
f.savefig(f'{F}/sn1.png', bbox_inches='tight'); plt.close(f)

# 7. E2 anti-periplanar (Newman) dengan panah
f, ax = kanv(7.0, 2.8, (0, 20), (-3.4, 3.4))
cx = 5.0; ax.add_patch(Circle((cx, 0), 1.0, fc='white', ec=TUA, lw=1.5, zorder=1))
for a, g in [(90, 'H'), (210, 'CH₃'), (330, 'H')]:
    r = np.radians(a); ikat(ax, (cx, 0), (cx + 1.6 * np.cos(r), 1.6 * np.sin(r)), sh=(0, 0)); T(ax, cx + 1.95 * np.cos(r), 1.95 * np.sin(r), g, fs=9.5, c=BIRU if a == 90 else TUA)
for a, g in [(270, 'Br'), (30, 'CH₃'), (150, 'H')]:
    r = np.radians(a); ikat(ax, (cx + 1.0 * np.cos(r), 1.0 * np.sin(r)), (cx + 1.7 * np.cos(r), 1.7 * np.sin(r)), sh=(0, 0)); T(ax, cx + 2.05 * np.cos(r), 2.05 * np.sin(r), g, fs=9.5, c=JT if g == 'Br' else TUA)
ax.plot(cx, 0, 'o', color=TUA, ms=4, zorder=3)
T(ax, cx - 2.3, 2.9, 'B:$^-$', c=BIRU)
panah(ax, (cx - 1.9, 2.7), (cx - 0.25, 2.05), rad=-0.3, c=BIRU); panah(ax, (cx + 0.15, 1.3), (cx + 0.3, 0.35), rad=-0.5); panah(ax, (cx + 0.15, -1.2), (cx + 0.2, -2.25), rad=0.6)
T(ax, cx, -3.1, 'H dan Br anti-periplanar (180°)', fs=8.3, c=HJ)
reaksi(ax, 8.8, 10.6, 0)
# alkena
ikat(ax, (13.0, 0), (15.0, 0), sh=(0.2, 0.2)); ax.plot([13.2, 14.8], [0.18, 0.18], color=TUA, lw=1.8)
for (x, y), g in [((12.0, 1.0), 'H'), ((12.0, -1.0), 'CH₃'), ((16.0, 1.0), 'CH₃'), ((16.0, -1.0), 'H')]:
    ikat(ax, (13.0 if x < 14 else 15.0, 0), (x, y), sh=(0.15, 0.2)); T(ax, x + (-0.35 if x < 14 else 0.35), y + (0.2 if y > 0 else -0.2), g, fs=9.5)
T(ax, 14.0, -2.4, '+ BH + Br$^-$', fs=9.5); T(ax, 14.0, 2.6, '(E)-but-2-ena', fs=8.5, c=HJ)
f.savefig(f'{F}/e2.png', bbox_inches='tight'); plt.close(f)

# 8. E2 sikloheksana: aksial vs ekuatorial
Pk = np.array([(0, 0), (0.85, 0.75), (2.15, 0.5), (3.0, 0.85), (2.15, 0.1), (0.85, 0.35)]) - np.array([1.5, 0.4])
nk = [False, True, False, True, False, True]
def kursi(ax, ox, br_aks):
    P = Pk + np.array([ox, 0]); cen = P.mean(0)
    for i in range(6): ikat(ax, P[i], P[(i + 1) % 6], sh=(0, 0))
    i = 2  # karbon yang membawa Br (turun): aksial ke bawah
    if br_aks:
        ikat(ax, P[i], P[i] + [0, -0.75], sh=(0, 0.1), c=JT); T(ax, P[i][0], P[i][1] - 0.95, 'Br', c=JT, fs=10)
        for j in (1, 3): ikat(ax, P[j], P[j] + [0, 0.75], sh=(0, 0.1), c=BIRU); T(ax, P[j][0], P[j][1] + 0.95, 'H', c=BIRU, fs=10)
    else:
        d = P[(i + 2) % 6] - P[(i + 1) % 6]; d = d / np.linalg.norm(d)
        if np.dot(d, P[i] - cen) < 0: d = -d
        ikat(ax, P[i], P[i] + 0.75 * d, sh=(0, 0.1), c=JT); T(ax, P[i][0] + 0.95 * d[0], P[i][1] + 0.95 * d[1], 'Br', c=JT, fs=10)
f, ax = kanv(7.0, 2.6, (-2.2, 8.4), (-1.9, 2.1))
kursi(ax, 0, True); kursi(ax, 6.0, False)
T(ax, 0, -1.7, 'Br aksial: anti-periplanar dengan H aksial → E2 cepat', fs=7.8, c=HJ)
T(ax, 6.0, -1.7, 'Br ekuatorial: tidak ada H anti-periplanar', fs=7.8, c=MERAH)
f.savefig(f'{F}/e2siklo.png', bbox_inches='tight'); plt.close(f)

# 9. peta keputusan (tabel visual)
f, ax = plt.subplots(figsize=(7.6, 3.2), dpi=220); ax.set_xlim(0, 5); ax.set_ylim(0, 5); ax.axis('off')
kol = ['nukleofil kuat,\nbasa lemah\n(I$^-$, CN$^-$, N$_3^-$, RS$^-$)', 'nukleofil kuat,\nbasa kuat\n(OH$^-$, RO$^-$)', 'basa kuat,\nbesar\n(t-BuO$^-$)', 'nukleofil/basa\nlemah\n(H₂O, ROH)']
bar = ['metil', 'primer', 'sekunder', 'tersier']
isi = [[('SN2', HJ), ('SN2', HJ), ('SN2', HJ), ('—', '#c9d2db')],
       [('SN2', HJ), ('SN2\n(E2 kecil)', HJ), ('E2', JT), ('—', '#c9d2db')],
       [('SN2', HJ), ('E2\n(SN2 kecil)', JT), ('E2', JT), ('SN1/E1\n(lambat)', BIRU)],
       [('SN1/E1', BIRU), ('E2', JT), ('E2', JT), ('SN1/E1', BIRU)]]
for j, k in enumerate(kol): ax.text(1.5 + j * 0.9 + 0.45 - 0.45, 4.55, k, ha='center', va='center', fontsize=7.4, color=TUA)
for i, b in enumerate(bar):
    y = 3.55 - i * 0.9; ax.text(0.55, y, b, ha='center', va='center', fontsize=9, color=TUA, fontweight='bold')
    for j in range(4):
        t, c = isi[i][j]; x = 1.08 + j * 0.9
        ax.add_patch(FancyBboxPatch((x, y - 0.37), 0.84, 0.74, boxstyle='round,pad=0.01,rounding_size=0.06', fc=c, ec='white', alpha=0.85 if c != '#c9d2db' else 0.6))
        ax.text(x + 0.42, y, t, ha='center', va='center', fontsize=8.2, color='white' if c != '#c9d2db' else TUA, fontweight='bold')
ax.text(0.55, 4.55, 'substrat ↓\npereaksi →', ha='center', va='center', fontsize=7.4, color=TUA)
f.savefig(f'{F}/peta.png', bbox_inches='tight'); plt.close(f)
print('ok')
