# Gambar Bab 7: selektivitas radikal, NBS, SN2, laju SN2, SN1, E2, E2 sikloheksana, peta keputusan
import os, io, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Ellipse, FancyBboxPatch, Circle
from scipy.interpolate import CubicSpline
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang
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
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = 0.18
    o.updateAtomPalette({35: (0.71, 0.33, 0.11), 8: (0.71, 0.33, 0.11)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))

# 2. NBS sikloheksena (digambar manual: ukuran cincin seragam, titik radikal jelas)
def heksa(ax, cx, cy, ganda=(), titik=None, br=None, r=1.0):
    V = [np.array([cx + r * np.cos(np.radians(90 - 60 * k)), cy + r * np.sin(np.radians(90 - 60 * k))]) for k in range(6)]
    for k in range(6): ax.plot(*zip(V[k], V[(k + 1) % 6]), color=TUA, lw=1.5, solid_capstyle='round')
    c = np.array([cx, cy])
    for a_, b_ in ganda:
        p_, q_ = V[a_] + (c - V[a_]) * 0.2, V[b_] + (c - V[b_]) * 0.2; m_ = (p_ + q_) / 2; p_, q_ = m_ + (p_ - m_) * 0.8, m_ + (q_ - m_) * 0.8
        ax.plot(*zip(p_, q_), color=TUA, lw=1.5, solid_capstyle='round')
    if titik is not None: u = (V[titik] - c) / r; ax.add_patch(Circle(V[titik] + u * 0.22, 0.075, color=MERAH, zorder=5))
    if br is not None:
        u = (V[br] - c) / r; e = V[br] + u * 0.75; ax.plot(*zip(V[br], V[br] + u * 0.5), color=TUA, lw=1.5); T(ax, *(e + u * 0.3), 'Br', c=JT, fs=10.5, fontweight='bold')
f, ax = plt.subplots(figsize=(7.4, 1.9), dpi=220); ax.set_xlim(0, 21); ax.set_ylim(0.2, 5); ax.set_aspect('equal'); ax.axis('off')
Y = 2.9
heksa(ax, 1.6, Y, ganda=[(0, 1)]); reaksi(ax, 3.1, 5.1, Y, 'Br·')
heksa(ax, 6.6, Y, ganda=[(0, 1)], titik=2); T(ax, 8.85, Y, '↔', fs=15, family='DejaVu Sans'); heksa(ax, 11.1, Y, ganda=[(1, 2)], titik=0)
reaksi(ax, 12.7, 14.9, Y, 'Br₂'); heksa(ax, 16.5, Y, ganda=[(0, 1)], br=2)
T(ax, 8.85, 0.85, 'radikal alilik (dua penyumbang setara)', fs=8.2, c=HJ); T(ax, 3.9, 2.35, '− HBr', fs=8, c='#555555'); T(ax, 13.8, 2.35, '− Br·', fs=8, c='#555555')
T(ax, 1.6, 0.85, 'sikloheksena', fs=8.2); T(ax, 17.0, 0.85, '3-bromosikloheksena', fs=8.2)
f.savefig(f'{F}/nbs.png', bbox_inches='tight'); plt.close(f)

# 3. SN2: Nu dari belakang, keadaan transisi, inversi
f, ax = kanv(7.6, 2.6, (0, 22), (-3.2, 3.6))
def pusat(ax, cx, cy, arah, gugus=('H', 'CH₃', 'C₂H₅')):
    # arah = -1: payung menghadap kiri (gugus condong ke kiri); +1 ke kanan
    ujung = [(cx + arah * 0.55, cy + 1.25), (cx + arah * 1.0, cy - 0.75), (cx - arah * 0.35, cy - 1.3)]
    jen = ['-', 'baji', 'putus']
    for (x, y), j, g in zip(ujung, jen, gugus):
        ikat(ax, (cx, cy), (x, y), j, sh=(0.34, 0.0)); T(ax, x + arah * 0.35 * (1 if g != 'H' else 0.6), y + (0.25 if y > cy else -0.25), g, fs=9)
    T(ax, cx, cy, 'C', fs=12)
T(ax, 1.0, 0, 'HO$^-$', c=BIRU, fs=12); pusat(ax, 4.3, 0, -1); ikat(ax, (4.3, 0), (6.1, 0), sh=(0.34, 0.1)); T(ax, 6.5, 0, 'Br', c=JT, fs=12)
panah(ax, (1.55, 0.35), (3.9, 0.25), rad=-0.35); panah(ax, (5.1, -0.15), (6.45, -0.4), rad=0.45)
reaksi(ax, 7.4, 8.6, 0)
# keadaan transisi
cx = 12.0; T(ax, 9.9, 0, 'HO', c=BIRU, fs=11); ikat(ax, (10.3, 0), (cx, 0), 'separuh', sh=(0.15, 0.34)); ikat(ax, (cx, 0), (13.8, 0), 'separuh', sh=(0.34, 0.1)); T(ax, 14.2, 0, 'Br', c=JT, fs=11)
for (x, y), j, g in zip([(cx, 1.35), (cx - 0.7, -1.0), (cx + 0.7, -1.0)], ['-', 'baji', 'putus'], ['H', 'CH₃', 'C₂H₅']):
    ikat(ax, (cx, 0), (x, y), j, sh=(0.34, 0)); T(ax, x, y + (0.3 if y > 0 else -0.3), g, fs=9)
T(ax, cx, 0, 'C', fs=12); ax.plot([9.6, 9.4, 9.4, 9.6], [1.9, 1.9, -1.9, -1.9], color=TUA, lw=1); ax.plot([14.6, 14.8, 14.8, 14.6], [1.9, 1.9, -1.9, -1.9], color=TUA, lw=1); T(ax, 15.05, 1.95, '‡', fs=12)
T(ax, 9.9, 0.55, 'δ−', fs=8, c=BIRU); T(ax, 14.2, 0.55, 'δ−', fs=8, c=JT); 
reaksi(ax, 15.3, 16.5, 0)
pusat(ax, 19.3, 0, 1); ikat(ax, (17.9, 0), (19.3, 0), sh=(0.12, 0.34)); T(ax, 17.5, 0, 'HO', c=BIRU, fs=12); T(ax, 21.2, -1.9, '+ Br$^-$', c=JT, fs=11)
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
for x, y, t in [(0.45, 0.35, 'R₃C–Br\n+ H₂O'), (3, 3.85, 'R$_3$C$^+$'), (5, 1.6, 'R$_3$C–OH$_2^+$'), (7, 0.1, 'R$_3$C–OH\n+ H$_3$O$^+$')]: T(ax, x, y, t, fs=8)
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
    r = np.radians(a); ikat(ax, (cx + 1.0 * np.cos(r), 1.0 * np.sin(r)), (cx + 1.7 * np.cos(r), 1.7 * np.sin(r)), sh=(0, 0)); T(ax, cx + 2.05 * np.cos(r) - (0.35 if g == 'Br' else 0), 2.05 * np.sin(r), g, fs=9.5, c=JT if g == 'Br' else TUA)
ax.plot(cx, 0, 'o', color=TUA, ms=4, zorder=3)
T(ax, cx - 2.3, 2.9, 'B:$^-$', c=BIRU)
panah(ax, (cx - 1.9, 2.7), (cx - 0.25, 2.05), rad=-0.3, c=BIRU); panah(ax, (cx + 0.15, 1.3), (cx + 0.3, 0.35), rad=-0.5); panah(ax, (cx + 0.12, -1.25), (cx + 0.6, -1.85), rad=0.5)
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

# ================= versi render WebGL (3D) =================
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r3d'))
from r3d import render, spek_molekul, tampil, konformer, tegakkan, aksial, atom_ikat, kamera_terbaik, arahkan_z, koord, pas
TMP = os.path.join(F, '_r3d'); os.makedirs(TMP, exist_ok=True)
def bingkai(f, rect): a = f.add_axes(rect); a.axis('off'); return a
def satuan(v): v = np.asarray(v, float); return v / np.linalg.norm(v)
def lob(d, L=1.0, w=0.36, c=0xf4b942, o=(0, 0, 0), a=1.0, k=0.7): return {'d': list(map(float, d)), 'L': L, 'w': w, 'c': c, 'o': list(map(float, o)), 'a': a, 'k': k}
AKS, BRW, PUCAT, NUW = '#2f7fd6', '#a8462a', 0xc9d6e4, '#8a63c9'
J = []
# --- E2 sikloheksana: Br aksial (H β aksial anti-periplanar, biru) vs Br ekuatorial
def bromo(want_ax):
    def syarat(m, P):
        ring = [a.GetIdx() for a in m.GetAtoms() if a.IsInRing()]; return aksial(m, P, 1, 0, ring) == want_ax
    m, P = konformer('BrC1CCCCC1', syarat, n=200); ring = [a.GetIdx() for a in m.GetAtoms() if a.IsInRing()]
    P = tegakkan(P, ring); P = arahkan_z(P, P[1]);
    if P[1][2] > 0: P = P * [1, -1, -1]
    vb = satuan(P[0] - P[1]); anti = []
    for c in (2, 6):
        for n in m.GetAtomWithIdx(c).GetNeighbors():
            if n.GetSymbol() == 'H' and np.dot(satuan(P[n.GetIdx()] - P[c]), vb) < -0.9: anti.append(n.GetIdx())
    at, ik = atom_ikat(m, P); return dict(spek_molekul(at, ik, warna={i: AKS for i in anti}), w=820, h=600, zoom=2.75)
for nm, w in (('ax', True), ('eq', False)):
    sp = bromo(w); sp['camdir'] = kamera_terbaik([a['p'] for a in sp['atoms']], (6, 24)); J.append((sp, f'{TMP}/e2_{nm}.png'))
# --- SN1: model gugus disatukan (CH3, C2H5 sebagai bola) agar bentuk datar dan dua sisi serangan jelas
GW = {'H': ('#f4f4f4', 0.25, 1.09), 'CH$_3$': ('#7a828e', 0.42, 1.5), 'C$_2$H$_5$': ('#d9874a', 0.5, 1.55)}
GA = {'H': 270, 'CH$_3$': 150, 'C$_2$H$_5$': 30}
def model(nu):  # nu = 0 kation; +1/-1 posisi Nu
    at = [{'p': [0, 0, 0], 'r': 0.34, 'c': 0x3b4049}]; bd = []; lab = {}
    for g, ang in GA.items():
        c_, r_, L = GW[g]; t = np.radians(ang); zc = -nu * 0.334; v = np.array([np.cos(t) * np.sqrt(1 - zc ** 2), np.sin(t) * np.sqrt(1 - zc ** 2), zc]) * L
        at.append({'p': list(map(float, v)), 'r': r_, 'c': int(c_[1:], 16)}); bd.append({'p': [0, 0, 0], 'q': list(map(float, v)), 'r': 0.085, 'c': 0xb9bfc7}); lab[g] = v * (1 + (r_ + 0.5) / L) + [0, 0, -0.1]
    if nu:
        v = np.array([0, 0, nu * 1.5]); at.append({'p': list(v), 'r': 0.4, 'c': int(NUW[1:], 16)}); bd.append({'p': [0, 0, 0], 'q': list(map(float, v)), 'r': 0.085, 'c': 0xb9bfc7}); lab['Nu'] = v + [0.75, 0, 0]
    return {'atoms': at, 'bonds': bd}, lab
CAMS = [0.0, -1, 0.42]; LBS = {}
sp, lab = model(0); sp.update(w=760, h=820, camdir=CAMS, up=[0, 0, 1], lobes=[lob((0, 0, 1), 1.1, 0.4, PUCAT, a=0.55), lob((0, 0, -1), 1.1, 0.4, PUCAT, a=0.55)])
sp['labels'] = [[0, 0, 0], [0, 0, 1.2], [0, 0, -1.2]] + [list(map(float, v)) for v in lab.values()]; LBS['kat'] = list(lab); J.append((pas(sp, 0.55), f'{TMP}/sn1_kat.png'))
for nm, sz in (('atas', 1), ('bawah', -1)):
    sp, lab = model(sz); sp.update(w=720, h=600, camdir=[CAMS[0], CAMS[1], CAMS[2] * sz], up=[0, 0, 1]); sp['labels'] = [list(map(float, v)) for v in lab.values()]; LBS[nm] = list(lab); J.append((pas(sp, 0.45), f'{TMP}/sn1_{nm}.png'))
PR = render(J)

f = plt.figure(figsize=(7.2, 2.7), dpi=220)
for k, (nm, t, c_) in enumerate([('ax', 'Br aksial: H β aksial (biru) anti-periplanar → E2 cepat', HJ), ('eq', 'Br ekuatorial: tidak ada H anti-periplanar', MERAH)]):
    a = bingkai(f, [k * 0.5, 0.14, 0.5, 0.86]); tampil(a, f'{TMP}/e2_{nm}.png'); f.text(k * 0.5 + 0.25, 0.03, t, ha='center', fontsize=8.4, color=c_)
f.savefig(f'{F}/e2siklo.png', bbox_inches='tight'); plt.close(f)

f = plt.figure(figsize=(7.2, 3.4), dpi=220)
a = bingkai(f, [0.0, 0.05, 0.32, 0.86]); fn = f'{TMP}/sn1_kat.png'; tampil(a, fn); q = np.array(PR[fn])
for l, p_ in zip(LBS['kat'], q[3:]): a.text(*p_, l, ha='center', va='center', fontsize=9.5, color=TUA, fontweight='bold')
a.text(q[0][0] + 60, q[0][1] - 55, 'C$^+$', fontsize=10, color=JT, fontweight='bold')
for s_, y_ in ((1, q[1][1] - 170), (-1, q[2][1] + 170)):
    a.text(q[0][0] - 230, y_, 'Nu$^-$', fontsize=10, color=NUW, fontweight='bold', ha='center', va='center')
    a.add_patch(FancyArrowPatch((q[0][0] - 190, y_ + 20 * s_), (q[0][0] - 30, q[1 if s_ > 0 else 2][1] + 60 * s_), connectionstyle=f'arc3,rad={-0.3 * s_}', arrowstyle='-|>', mutation_scale=10, color=NUW, lw=1.3))
f.text(0.16, 0.97, 'karbokation datar (sp²), orbital p kosong', ha='center', fontsize=8.2, color=HJ)
for k, (nm, t) in enumerate([('atas', 'Nu dari atas  ≈ 50%'), ('bawah', 'Nu dari bawah  ≈ 50%')]):
    y0 = 0.5 if k == 0 else 0.02; a = bingkai(f, [0.52, y0, 0.3, 0.47]); fn = f'{TMP}/sn1_{nm}.png'; tampil(a, fn)
    for l, p_ in zip(LBS[nm], PR[fn]): a.text(*p_, l, ha='center', va='center', fontsize=8.5, color=NUW if l == 'Nu' else TUA, fontweight='bold')
    f.text(0.84, y0 + 0.23, t, fontsize=8.8, color=TUA, va='center')
    f.add_artist(FancyArrowPatch((0.34, 0.5 + (0.1 if k == 0 else -0.1)), (0.5, y0 + 0.23), transform=f.transFigure, arrowstyle='-|>', mutation_scale=11, color=TUA, lw=1.3))
f.text(0.9, 0.5, 'enansiomer', fontsize=8.5, color=HJ, ha='center', va='center')
f.savefig(f'{F}/sn1.png', bbox_inches='tight'); plt.close(f)
print('ok webgl')
