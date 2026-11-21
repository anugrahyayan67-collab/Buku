# Gambar Bab 14: spektrum EM, getaran CH2, peta korelasi IR, spektrum IR skematis, skema MS, pola isotop,
# spektrum massa skematis, McLafferty, data gabungan
import os, io, numpy as np, matplotlib, matplotlib.ticker
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from rdk import rapat, pasang, ukuran_px
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab14/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
koma = lambda v: f'{v:g}'.replace('.', ',').replace('-', '−')
fmt = matplotlib.ticker.FuncFormatter(lambda q, _: koma(q))
def T(ax, x, y, s, c=TUA, fs=11, **k): ax.text(x, y, s, ha='center', va='center', color=c, fontsize=fs, **k)
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def rd(smi, w=360, h=300, fs=30, pad=0.15, bl=None):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 2; o.fixedFontSize = fs; o.padding = pad
    if bl: o.fixedBondLength = bl
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 1: (0.05, 0.15, 0.28)})
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return rapat(Image.open(io.BytesIO(d.GetDrawingText())))
def gb(ax, smi, x0, x1, y0, y1, **k):
    k['w'], k['h'] = ukuran_px(ax, x0, x1, y0, y1); k['fs'] = min(k.get('fs', 25), 25); k.setdefault('bl', 40)
    pasang(ax, rd(smi, **k), x0, x1, y0, y1, zorder=2, maks=1.0)

# 1. spektrum elektromagnetik
f, ax = plt.subplots(figsize=(7.2, 2.2), dpi=220)
reg = [(-12, -8, 'sinar X', '#bbbbbb'), (-8, -6.4, 'UV', '#b39ddb'), (-6.4, -6.1, '', '#ffffff'), (-6.1, -3.0, 'inframerah', '#f4a582'), (-3.0, -0.5, 'gelombang mikro', '#d9d9d9'), (-0.5, 1.5, 'radio', '#92c5de')]
for a, b, t, c in reg: ax.add_patch(Rectangle((a, 0), b - a, 1, fc=c, ec='white'))
xs = np.linspace(-6.4, -6.1, 50)
for x0, x1 in zip(xs[:-1], xs[1:]): ax.add_patch(Rectangle((x0, 0), x1 - x0, 1, fc=plt.cm.rainbow_r((x0 + 6.4) / 0.3), ec='none'))
for a, b, t, c in reg:
    if t: ax.text((a + b) / 2, 0.5, t, ha='center', va='center', fontsize=8.5, color=TUA)
ax.text(-6.25, 1.15, 'tampak', ha='center', fontsize=8, color=TUA)
for x, t, c in [(-6.7, 'UV–Vis:\nelektron π → π*', '#6a51a3'), (-5.1, 'IR: getaran ikatan\n(4000–400 cm$^{-1}$)', JT), (0.5, 'NMR: spin inti', BIRU)]:
    ax.annotate(t, (x, 0), (x, -0.75), ha='center', va='center', fontsize=8.2, color=c, arrowprops=dict(arrowstyle='-|>', color=c, lw=1))
ax.set_xlim(-12, 1.5); ax.set_ylim(-1.3, 1.4); ax.set_yticks([]); ax.spines['left'].set_visible(False)
ax.set_xticks([-10, -8, -6, -4, -2, 0]); ax.set_xticklabels(['10$^{-10}$', '10$^{-8}$', '10$^{-6}$', '10$^{-4}$', '10$^{-2}$', '1']); ax.set_xlabel('panjang gelombang (m)   ←  energi foton makin besar')
plt.tight_layout(); f.savefig(f'{F}/em.png', bbox_inches='tight'); plt.close(f)

# 2. getaran CH2
f, ax = kanv(7.2, 2.0, (0, 28), (0, 7.4))
modes = [('regang simetris', '± 2850', [(-1, 1), (1, 1)]), ('regang asimetris', '± 2925', [(-1, 1), (-1, -1)]), ('gunting', '± 1465', [(1, 0), (-1, 0)]), ('goyang', '± 720', [(1, 0), (1, 0)])]
for i, (nm, v, ar) in enumerate(modes):
    cx = 3.5 + i * 7.0; cy = 3.6
    ax.add_patch(Circle((cx, cy), 0.55, fc='#555555', ec='none')); T(ax, cx, cy, 'C', c='white', fs=9)
    for k, (hx, hy) in enumerate([(cx - 1.6, cy + 1.6), (cx + 1.6, cy + 1.6)]):
        ax.plot([cx, hx], [cy, hy], color=TUA, lw=2); ax.add_patch(Circle((hx, hy), 0.38, fc='white', ec=TUA, lw=1.2)); T(ax, hx, hy, 'H', fs=8)
        sgn = -1 if k == 0 else 1
        if i == 0: d = np.array([sgn, 1]) * 0.7
        elif i == 1: d = np.array([sgn, 1]) * 0.7 * (1 if k == 0 else -1)
        elif i == 2: d = np.array([-sgn, 0]) * 0.8
        else: d = np.array([1, 0]) * 0.8
        ax.add_patch(FancyArrowPatch((hx, hy), (hx + d[0], hy + d[1]), arrowstyle='-|>', mutation_scale=9, color=MERAH, lw=1.3))
    T(ax, cx, 1.6, nm, fs=8.5, c=HJ if i < 2 else BIRU); T(ax, cx, 0.8, v + ' cm$^{-1}$', fs=8)
f.savefig(f'{F}/getaran.png', bbox_inches='tight'); plt.close(f)

# 3. peta korelasi
f, ax = plt.subplots(figsize=(7.2, 3.4), dpi=220)
rows = [('O–H alkohol', 3200, 3550, BIRU), ('O–H asam', 2500, 3300, BIRU), ('N–H', 3300, 3500, HJ), ('≡C–H', 3270, 3330, JG), ('=C–H, Ar–H', 3000, 3100, JG),
        ('C–H sp³', 2850, 3000, JG), ('C–H aldehida', 2700, 2850, JG), ('C≡N', 2210, 2260, MERAH), ('C≡C', 2100, 2260, MERAH), ('C=O', 1650, 1800, JT),
        ('C=C', 1620, 1680, '#7b3294'), ('cincin aromatik', 1450, 1600, '#7b3294'), ('C–O', 1000, 1300, TUA)]
for i, (n, a, b, c) in enumerate(rows):
    y = len(rows) - i; ax.barh(y, b - a, left=a, height=0.6, color=c); ax.text(b + 40, y, n, ha='right', va='center', fontsize=8)
ax.axvline(3000, color='#999999', lw=0.8, ls='--'); ax.text(3000, len(rows) + 0.9, '3000', ha='center', fontsize=8, color='#777777')
ax.axvspan(400, 1500, color='#eeeeee', zorder=0); ax.text(950, 0.2, 'daerah sidik jari', ha='center', fontsize=8, color='#777777')
ax.set_xlim(4400, 400); ax.set_ylim(-0.3, len(rows) + 1.3); ax.set_yticks([]); ax.spines['left'].set_visible(False); ax.set_xlabel('bilangan gelombang (cm$^{-1}$)')
plt.tight_layout(); f.savefig(f'{F}/korelasi.png', bbox_inches='tight'); plt.close(f)

# spektrum IR skematis
X = np.linspace(400, 4000, 3600)
def ir(bands, seed=0):
    rng = np.random.default_rng(seed); A = np.zeros_like(X)
    for c, d, w in bands: A += d * np.exp(-0.5 * ((X - c) / w) ** 2)
    for c in rng.uniform(600, 1450, 9): A += rng.uniform(0.05, 0.22) * np.exp(-0.5 * ((X - c) / rng.uniform(5, 12)) ** 2)
    return 100 * np.exp(-A * 1.6)
CH3 = [(2960, 0.9, 12), (2930, 1.0, 12), (2870, 0.6, 10), (1465, 0.45, 9), (1380, 0.3, 6)]
def panel(ax, bands, judul, ann, seed):
    ax.plot(X, ir(bands, seed), color=TUA, lw=0.9); ax.set_xlim(4000, 400); ax.set_ylim(-30, 108); ax.axhline(0, color='#dddddd', lw=0.6)
    ax.text(3950, 60, judul, fontsize=9, color=TUA, fontweight='bold', va='bottom')
    for x, t, c in ann: ax.annotate(t, (x, ir(bands, seed)[np.argmin(abs(X - x))] - 2), (x, -18), ha='center', va='center', fontsize=7.2, color=c, arrowprops=dict(arrowstyle='-', color=c, lw=0.6))
    ax.set_yticks([0, 50, 100]); ax.tick_params(labelsize=7.5)
def tiga(nama, panels):
    f, axs = plt.subplots(len(panels), 1, figsize=(7.0, 1.75 * len(panels)), dpi=220, sharex=True)
    for ax, (b, j, a, s) in zip(axs, panels): panel(ax, b, j, a, s)
    axs[-1].set_xlabel('bilangan gelombang (cm$^{-1}$)'); axs[len(panels) // 2].set_ylabel('% transmitansi')
    plt.tight_layout(h_pad=1.6); f.savefig(f'{F}/{nama}.png', bbox_inches='tight'); plt.close(f)
tiga('ir1', [(CH3 + [(725, 0.25, 6)], 'heksana', [(2930, 'C–H sp³', JG)], 1),
             (CH3 + [(3080, 0.35, 10), (1640, 0.45, 8), (990, 0.6, 6), (910, 0.8, 6)], 'heks-1-ena', [(3080, '=C–H', JG), (1640, 'C=C', '#7b3294'), (910, '=CH₂ (tekuk)', TUA)], 2),
             (CH3 + [(3310, 1.0, 12), (2120, 0.3, 10), (630, 0.7, 10)], 'heks-1-una', [(3310, '≡C–H', JG), (2120, 'C≡C', MERAH)], 3)])
tiga('ir2', [(CH3 + [(3330, 1.0, 110), (1060, 0.9, 15)], 'heksan-1-ol', [(3330, 'O–H (lebar)', BIRU), (1060, 'C–O', TUA)], 4),
             ([(3000, 0.7, 280)] + CH3 + [(1710, 1.4, 14), (1290, 0.6, 15), (940, 0.4, 25)], 'asam heksanoat', [(2700, 'O–H asam (sangat lebar)', BIRU), (1710, 'C=O', JT)], 5),
             (CH3 + [(3370, 0.35, 18), (3290, 0.3, 18), (1600, 0.3, 15), (800, 0.4, 40)], 'heksan-1-amina', [(3330, 'dua N–H', HJ)], 6)])
tiga('ir3', [(CH3 + [(1715, 1.5, 12), (1360, 0.5, 8)], 'heksan-2-on', [(1715, 'C=O 1715', JT)], 7),
             (CH3 + [(2820, 0.35, 8), (2720, 0.35, 8), (1725, 1.5, 12)], 'heksanal', [(2720, 'C–H aldehida', JG), (1725, 'C=O 1725', JT)], 8),
             (CH3 + [(1740, 1.5, 12), (1180, 1.1, 18), (1250, 0.5, 12)], 'etil butanoat', [(1740, 'C=O 1740', JT), (1180, 'C–O', TUA)], 9),
             (CH3 + [(2250, 0.6, 9)], 'heksananitril', [(2250, 'C≡N 2250', MERAH)], 10)])

# 7. skema MS
f, ax = kanv(7.2, 2.6, (0, 28), (0, 10))
ax.add_patch(FancyBboxPatch((0.5, 3.0), 5.0, 4.0, boxstyle='round,pad=0.2', fc='#eef5fb', ec=BIRU)); T(ax, 3.0, 6.0, 'sumber ion', fs=9, c=BIRU, fontweight='bold')
T(ax, 3.0, 4.6, 'M + e$^-$ → M$^{+\\cdot}$ + 2e$^-$', fs=7.2); T(ax, 3.0, 3.6, '(70 eV)', fs=8)
ax.annotate('', (8.2, 5.0), (5.9, 5.0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.4)); T(ax, 7.0, 5.6, 'percepat', fs=8)
th = np.linspace(np.pi / 2, 0, 100)
for r, c, lab in [(5.0, MERAH, 'ringan'), (6.5, HJ, 'sedang'), (8.0, BIRU, 'berat')]:
    xs, ys = 8.4 + r * np.cos(th + np.pi), 5.0 - r + r * np.sin(th + np.pi / 2) * 0 + 0
    x = 8.4 + r * np.sin(np.linspace(0, np.pi / 2, 80)); y = 5.0 - r + r * np.cos(np.linspace(0, np.pi / 2, 80))
    ax.plot(x, y, color=c, lw=1.6); ax.text(x[-1] + 0.3, y[-1], lab, fontsize=7.5, color=c, va='center')
ax.add_patch(Rectangle((8.4, -0.2), 4.0, 5.6, fc='#f2f2f2', ec='#999999', zorder=0)); T(ax, 10.4, 6.2, 'medan magnet', fs=8.5, c='#555555')
T(ax, 14.2, -2.9, '→ detektor', fs=8.5)
ax.set_ylim(-3.2, 8.0)
# contoh spektrum kecil
axi = f.add_axes([0.66, 0.18, 0.32, 0.65]);
for m, h in [(15, 10), (43, 100), (58, 64)]: axi.bar(m, h, width=1.2, color=TUA)
axi.set_xlim(10, 65); axi.set_ylim(0, 115); axi.set_xlabel('m/z', fontsize=8); axi.set_ylabel('kelimpahan relatif', fontsize=7.5); axi.tick_params(labelsize=7)
axi.text(43, 104, 'puncak dasar', ha='center', fontsize=7, color=JT); axi.text(58, 68, 'M$^{+\\cdot}$', ha='center', fontsize=7.5, color=BIRU)
axi.set_title('aseton (skematis)', fontsize=8)
f.savefig(f'{F}/alat.png', bbox_inches='tight'); plt.close(f)

# 8. pola isotop
pCl = (0.7576, 0.2424); pBr = (0.5069, 0.4931)
def pola(*p):
    d = {0: 1.0}
    for a, b in p:
        nd = {}
        for k, v in d.items(): nd[k] = nd.get(k, 0) + v * a; nd[k + 2] = nd.get(k + 2, 0) + v * b
        d = nd
    mx = max(d.values()); return {k: 100 * v / mx for k, v in d.items()}
f, axs = plt.subplots(1, 4, figsize=(7.2, 2.2), dpi=220, sharey=True)
for ax, (n, p) in zip(axs, [('satu Cl', (pCl,)), ('satu Br', (pBr,)), ('dua Cl', (pCl, pCl)), ('dua Br', (pBr, pBr))]):
    d = pola(*p); ks = sorted(d)
    ax.bar(ks, [d[k] for k in ks], width=0.6, color=HJ if 'Cl' in n else JT)
    for k in ks: ax.text(k, d[k] + 3, f'{d[k]:.0f}', ha='center', fontsize=7.5)
    ax.set_xticks(ks); ax.set_xticklabels(['M' if k == 0 else f'M+{k}' for k in ks], fontsize=7.5); ax.set_title(n, fontsize=9, color=TUA); ax.set_ylim(0, 118); ax.set_xlim(-1.2, max(ks) + 1.2)
axs[0].set_ylabel('relatif')
plt.tight_layout(); f.savefig(f'{F}/isotop.png', bbox_inches='tight'); plt.close(f)

# 9. spektrum massa skematis
def ms(ax, peaks, judul, lab):
    for m, h in peaks: ax.bar(m, h, width=0.9, color=TUA)
    for m, t, c in lab:
        h = dict(peaks)[m]; ax.text(m, h + 4, t, ha='center', fontsize=7.2, color=c)
    ax.set_ylim(0, 125); ax.set_ylabel('relatif'); ax.set_title(judul, fontsize=9, color=TUA, loc='left')
f, axs = plt.subplots(2, 1, figsize=(6.6, 4.0), dpi=220)
ms(axs[0], [(27, 30), (29, 72), (57, 100), (58, 4), (86, 20), (87, 1.2)], 'pentan-3-on (M = 86)', [(29, '29\nC₂H₅$^+$', TUA), (57, '57\nC₂H₅CO$^+$', JT), (86, '86 M$^{+\\cdot}$', BIRU)])
ms(axs[1], [(27, 12), (29, 14), (41, 18), (43, 100), (57, 10), (58, 55), (71, 6), (85, 5), (100, 8)], 'heksan-2-on (M = 100)', [(43, '43\nCH₃CO$^+$', JT), (58, '58\nMcLafferty', HJ), (85, '85', TUA), (100, '100 M$^{+\\cdot}$', BIRU)])
axs[0].set_xlim(20, 95); axs[1].set_xlim(20, 108); axs[1].set_xlabel('m/z')
plt.tight_layout(); f.savefig(f'{F}/ms1.png', bbox_inches='tight'); plt.close(f)

# 10. McLafferty
f, ax = kanv(7.2, 2.2, (0, 28), (0, 8.6))
gb(ax, 'CCCCC(C)=O', 0, 6.0, 1.6, 7.0); T(ax, 3.0, 1.0, 'heksan-2-on$^{+\\cdot}$ (m/z 100)', fs=8.5, c=BIRU)
T(ax, 9.6, 6.0, 'H γ pindah ke O\n(cincin enam)', fs=8.5, c=MERAH); ax.annotate('', (12.6, 4.2), (7.0, 4.2), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.4)); T(ax, 9.8, 3.4, 'Cα–Cβ putus', fs=8.5)
gb(ax, 'C=C(C)O', 13.0, 17.4, 2.0, 6.6); T(ax, 15.2, 1.0, 'enol$^{+\\cdot}$, m/z 58', fs=8.5, c=HJ)
T(ax, 18.6, 4.2, '+', fs=13); gb(ax, 'C=CC', 19.6, 23.4, 2.4, 6.2); T(ax, 21.5, 1.0, 'propena (netral, 42)', fs=8.5, c='#777777')
T(ax, 26.0, 4.2, 'tidak\nterdeteksi', fs=8, c='#777777')
f.savefig(f'{F}/mclafferty.png', bbox_inches='tight'); plt.close(f)

# 11. data gabungan (asetofenon)
f, axs = plt.subplots(2, 1, figsize=(6.8, 4.2), dpi=220)
bands = [(3060, 0.3, 12), (2960, 0.2, 12), (1685, 1.5, 12), (1600, 0.5, 8), (1580, 0.4, 7), (1450, 0.4, 8), (1360, 0.5, 8), (1265, 1.0, 12), (760, 0.8, 8), (690, 0.8, 8)]
panel(axs[0], bands, 'IR', [(3060, 'C–H sp²', JG), (1685, 'C=O 1685', JT)], 11)
axs[0].set_ylabel('% T'); axs[0].set_xlabel('bilangan gelombang (cm$^{-1}$)', labelpad=12)
for m, h in [(43, 12), (51, 30), (77, 80), (78, 7), (105, 100), (106, 8), (120, 30), (121, 2.6)]: axs[1].bar(m, h, width=0.9, color=TUA)
for m, h, t in [(51, 30, '51'), (77, 80, '77'), (105, 100, '105'), (120, 30, '120')]: axs[1].text(m, h + 4, t, ha='center', fontsize=7.5)
axs[1].set_xlim(35, 130); axs[1].set_ylim(0, 120); axs[1].set_xlabel('m/z'); axs[1].set_ylabel('relatif'); axs[1].set_title('MS', fontsize=9, color=TUA, loc='left')
plt.tight_layout(h_pad=2.0); f.savefig(f'{F}/gabung.png', bbox_inches='tight'); plt.close(f)
print('ok')
