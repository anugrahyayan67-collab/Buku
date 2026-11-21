# Gambar Bab 4: Newman, energi putaran, tegangan cincin, kursi, pembalikan kursi
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab04/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))

# 1. Newman etana
def newman(ax, depan, belakang, lab_d, lab_b, judul):
    ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.9, 1.9); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0, 0), 0.7, fc='white', ec=TUA, lw=1.6, zorder=2))
    for a, t in zip(belakang, lab_b):
        r = np.radians(a); ax.plot([0.7 * np.cos(r), 1.35 * np.cos(r)], [0.7 * np.sin(r), 1.35 * np.sin(r)], color=JT, lw=1.6, zorder=1)
        ax.text(1.6 * np.cos(r), 1.6 * np.sin(r), t, ha='center', va='center', color=JT, fontsize=10)
    for a, t in zip(depan, lab_d):
        r = np.radians(a); ax.plot([0, 1.25 * np.cos(r)], [0, 1.25 * np.sin(r)], color=TUA, lw=1.8, zorder=3)
        ax.text(1.5 * np.cos(r), 1.5 * np.sin(r), t, ha='center', va='center', color=TUA, fontsize=10)
    ax.plot(0, 0, 'o', color=TUA, ms=4, zorder=4); ax.set_title(judul, color=TUA, fontsize=10, y=-0.08)
f, ax = plt.subplots(1, 2, figsize=(5.6, 2.9), dpi=220)
newman(ax[0], [90, 210, 330], [30, 150, 270], 'HHH', 'HHH', 'goyang (60°)')
newman(ax[1], [90, 210, 330], [100, 220, 340], 'HHH', 'HHH', 'tindih (0°)')
plt.tight_layout(); f.savefig(f'{F}/newman.png', bbox_inches='tight'); plt.close(f)

# 2. energi putaran etana dan butana
phi = np.linspace(0, 360, 721)
Eet = 6 * (1 + np.cos(np.radians(3 * phi)))
# butana: titik kunci (sudut CH3-C-C-CH3): 0:19, 60:3.8, 120:16, 180:0, 240:16, 300:3.8, 360:19
from scipy.interpolate import CubicSpline
xs = np.array([0, 60, 120, 180, 240, 300, 360]); ys = np.array([19, 3.8, 16, 0, 16, 3.8, 19])
cs = CubicSpline(xs, ys, bc_type='periodic'); Ebu = cs(phi)
f, ax = plt.subplots(2, 1, figsize=(5.6, 4.6), dpi=220, sharex=True)
ax[0].plot(phi, Eet, color=BIRU, lw=2); ax[0].set_ylabel('E (kJ mol$^{-1}$)'); ax[0].set_ylim(-1, 14); ax[0].text(5, 12.6, 'etana', color=TUA, fontsize=10)
ax[1].plot(phi, Ebu, color=JT, lw=2); ax[1].set_ylabel('E (kJ mol$^{-1}$)'); ax[1].set_ylim(-2, 27); ax[1].set_xlim(-15, 375)
for x, y, t in [(0, 19, '19\ntindih\nCH₃/CH₃'), (60, 3.8, 'gauche\n3,8'), (120, 16, 'tindih H/CH₃\n16'), (180, 0, 'anti 0'), (300, 3.8, 'gauche\n3,8')]:
    ax[1].annotate(t, (x, y), textcoords='offset points', xytext=(14 if x == 0 else 0, 8 if (y > 10 or x == 180) else -26), ha='center', fontsize=7.6, color=TUA)
ax[1].text(330, 20.5, 'butana', color=TUA, fontsize=10)
ax[1].set_xlabel('sudut torsi (°)'); ax[1].set_xticks(range(0, 361, 60))
for a in ax: a.yaxis.set_major_formatter(kom)
plt.tight_layout(); f.savefig(f'{F}/putar.png', bbox_inches='tight'); plt.close(f)

# 3. tegangan cincin
n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]; s = [115, 110, 27, 0, 27, 40, 54, 50, 46, 17, 0]
f, ax = plt.subplots(figsize=(5.0, 2.9), dpi=220)
ax.bar(n, s, color=[JT if v > 60 else (HJ if v < 5 else BIRU) for v in s], width=0.7)
for x, v in zip(n, s): ax.text(x, v + 2, str(v), ha='center', fontsize=7.8, color=TUA)
ax.set_xlabel('jumlah karbon cincin'); ax.set_ylabel('tegangan cincin (kJ mol$^{-1}$)'); ax.set_xticks(n)
f.savefig(f'{F}/tegangan.png', bbox_inches='tight'); plt.close(f)

# 4. kursi aksial/ekuatorial (gambar kursi baku: sisi sejajar)
P = np.array([(-0.2, -0.4), (0.9, 0.6), (2.1, 0.35), (2.9, 0.75), (1.8, -0.25), (0.6, 0.0)]); P = (P - P.mean(0)) * 1.15
naik = [False, True, False, True, False, True]
def kursi(ax, aks=True, eq=True, c_ring=TUA, ca=BIRU, ce=JT, lw=2, L=0.6):
    for i in range(6): ax.plot(*zip(P[i], P[(i + 1) % 6]), color=c_ring, lw=lw, zorder=2)
    cen = P.mean(0)
    for i in range(6):
        if aks: ax.plot([P[i][0], P[i][0]], [P[i][1], P[i][1] + (L if naik[i] else -L)], color=ca, lw=lw * 0.9, zorder=1)
        if eq:
            d = P[(i + 2) % 6] - P[(i + 1) % 6]; d = d / np.linalg.norm(d)
            if np.dot(d, P[i] - cen) < 0: d = -d
            ax.plot([P[i][0], P[i][0] + L * d[0]], [P[i][1], P[i][1] + L * d[1]], color=ce, lw=lw * 0.9, zorder=1)
f, ax = plt.subplots(1, 2, figsize=(7.0, 2.8), dpi=220)
for a, (A, Eq, t) in zip(ax, [(True, False, 'aksial'), (False, True, 'ekuatorial')]):
    a.set_xlim(-2.2, 2.2); a.set_ylim(-1.0, 1.1); a.set_aspect('equal'); a.axis('off'); kursi(a, A, Eq)
    a.set_title(t, color=BIRU if A else JT, fontsize=10.5, y=-0.1)
plt.tight_layout(); f.savefig(f'{F}/kursi.png', bbox_inches='tight'); plt.close(f)

# 5. pembalikan kursi
f, ax = plt.subplots(figsize=(6.2, 3.0), dpi=220)
x = [0, 1, 2, 3, 4, 5, 6]; y = [0, 45, 23, 29, 23, 45, 0]; lab = ['kursi', 'setengah-\nkursi', 'putar-\nperahu', 'perahu', 'putar-\nperahu', 'setengah-\nkursi', 'kursi']
xx = np.linspace(0, 6, 600); yy = CubicSpline(x, y, bc_type='clamped')(xx)
ax.plot(xx, yy, color=BIRU, lw=2)
for a, b, t in zip(x, y, lab):
    ax.plot(a, b, 'o', color=JT, ms=4); ax.text(a, b + 3, f'{b}', ha='center', fontsize=8, color=TUA); ax.text(a, -9, t, ha='center', va='top', fontsize=7.6, color=TUA)
ax.set_ylim(-20, 55); ax.set_xlim(-0.5, 6.5); ax.set_yticks(range(0, 51, 10)); ax.set_xticks([]); ax.set_ylabel('E (kJ mol$^{-1}$)'); ax.spines['bottom'].set_visible(False)
f.savefig(f'{F}/balik.png', bbox_inches='tight'); plt.close(f)
print('ok')

# ================= gambar tambahan =================
import io
from matplotlib.patches import Polygon, FancyArrowPatch, Ellipse
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
def simpan(f, n): f.savefig(f'{F}/{n}.png', bbox_inches='tight'); plt.close(f)
def T(ax, x, y, s, c=TUA, fs=10, **k): ax.text(x, y, s, ha=k.pop('ha', 'center'), va=k.pop('va', 'center'), color=c, fontsize=fs, **k)
def rd(smi, w=420, h=320, bl=45, fs=26, hs=False):
    m = Chem.MolFromSmiles(smi)
    if hs: m = Chem.AddHs(m, explicitOnly=False, onlyOnAtoms=tuple(a.GetIdx() for a in m.GetAtoms() if a.HasProp('_CIPCode') or a.GetChiralTag() != Chem.ChiralType.CHI_UNSPECIFIED))
    d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 3; o.fixedFontSize = fs; o.padding = 0.12; o.fixedBondLength = bl
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 1: (0.11, 0.46, 0.74)}); o.setBackgroundColour((1, 1, 1, 0))
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))

# 6. titik didih dan titik leleh alkana rantai lurus
n = np.arange(1, 11)
bp = [-161.5, -88.6, -42.1, -0.5, 36.1, 68.7, 98.4, 125.6, 150.8, 174.1]
mp = [-182.5, -182.8, -187.7, -138.3, -129.7, -95.3, -90.6, -56.8, -53.5, -29.7]
f, ax = plt.subplots(figsize=(5.8, 3.1), dpi=220)
ax.plot(n, bp, 'o-', color=JT, lw=1.8, label='titik didih'); ax.plot(n, mp, 's-', color=BIRU, lw=1.6, label='titik leleh')
ax.axhline(25, color='#bbbbbb', lw=0.7, ls='--'); ax.text(10.2, 30, 'suhu kamar', fontsize=8, color='#777777', ha='right')
ax.set_xlabel('jumlah atom karbon'); ax.set_ylabel('suhu (°C)'); ax.set_xticks(n); ax.yaxis.set_major_formatter(kom); ax.legend(frameon=False, fontsize=8.5, loc='upper left')
ax.text(5.3, -175, 'titik leleh naik bergerigi: rantai genap\nterkemas lebih rapat dalam kristal', fontsize=7.8, color=BIRU)
plt.tight_layout(); simpan(f, 'sifat')

# 7. isomer pentana dan titik didihnya
f, ax = plt.subplots(1, 3, figsize=(7.0, 2.4), dpi=220)
for a, (s, nm, t) in zip(ax, [('CCCCC', 'pentana', '36,1 °C'), ('CC(C)CC', '2-metilbutana', '27,7 °C'), ('CC(C)(C)C', '2,2-dimetilpropana', '9,5 °C')]):
    a.imshow(rd(s, w=420, h=300, bl=50)); a.axis('off'); a.set_title(f'{nm}\ntitik didih {t}', fontsize=9, color=TUA, y=-0.25)
f.text(0.5, 0.97, 'makin bercabang → makin bulat → luas kontak lebih kecil → gaya dispersi lebih lemah', ha='center', fontsize=8.5, color=JT)
plt.tight_layout(rect=(0, 0, 1, 0.93)); simpan(f, 'cabang')

# 8. kuda-kuda etana
f, ax = plt.subplots(1, 2, figsize=(6.0, 2.8), dpi=220)
for a, (rot, t) in zip(ax, [(0, 'goyang'), (60, 'tindih')]):
    a.set_xlim(-2.2, 2.6); a.set_ylim(-2.1, 2.3); a.set_aspect('equal'); a.axis('off')
    c1 = np.array([-0.6, -0.6]); c2 = np.array([0.6, 0.6]); a.plot(*zip(c1, c2), color=TUA, lw=2)
    for c, offs, col in [(c1, 0, TUA), (c2, rot, JT)]:
        for k in range(3):
            ang = np.radians(90 + 120 * k + offs + (180 if c is c1 else 0) + (10 if (c is c2 and rot == 60) else 0)); v = np.array([np.cos(ang), 0.75 * np.sin(ang)]) * 1.0
            a.plot([c[0], c[0] + v[0]], [c[1], c[1] + v[1]], color=col, lw=1.6); a.text(c[0] + v[0] * 1.3, c[1] + v[1] * 1.3, 'H', ha='center', va='center', fontsize=9.5, color=col)
    a.text(c1[0] - 0.3, c1[1] - 0.05, 'C', fontsize=9, color=TUA, ha='right'); a.set_title(t, fontsize=10, color=TUA, y=-0.08)
plt.tight_layout(); simpan(f, 'kuda')

# 9. Newman butana
f, ax = plt.subplots(1, 4, figsize=(7.6, 2.4), dpi=220)
conf = [(180, 'anti (180°)\n0 kJ mol$^{-1}$'), (60, 'gauche (60°)\n3,8'), (120, 'tindih H/CH₃ (120°)\n16'), (0, 'tindih CH₃/CH₃ (0°)\n19')]
for a, (phi_, t) in zip(ax, conf):
    front = [90, 210, 330]; lab_f = ['CH₃', 'H', 'H']
    dd = 18 if phi_ % 120 == 0 else 0
    back = [(90 + phi_ + dd) % 360, (210 + phi_ + dd) % 360, (330 + phi_ + dd) % 360]
    newman(a, front, back, lab_f, ['CH₃', 'H', 'H'], '')
    a.set_title(t, fontsize=8.2, color=TUA, y=-0.2)
plt.tight_layout(); simpan(f, 'newmanbutana')

# 10. cincin kecil: siklopropana, siklobutana, siklopentana (perspektif)
f, ax = plt.subplots(1, 3, figsize=(7.4, 2.6), dpi=220)
for a in ax: a.set_xlim(-1.8, 1.8); a.set_ylim(-1.5, 1.6); a.set_aspect('equal'); a.axis('off')
tri = np.array([(-1.0, -0.4), (1.0, -0.4), (0.0, 0.25)])
ax[0].add_patch(Polygon(tri, closed=True, fc='#eef4fa', ec=TUA, lw=2))
for i in range(3):
    p, q = tri[i], tri[(i + 1) % 3]; m = (p + q) / 2; n_ = m - tri.mean(0); n_ /= np.linalg.norm(n_)
    ax[0].plot(*zip(p, m + n_ * 0.22, q), color=JT, lw=1.2, ls=(0, (3, 2)))
    for s in (1, -1): ax[0].plot([p[0], p[0]], [p[1], p[1] + 0.6 * s], color=BIRU, lw=1.3)
ax[0].set_title('siklopropana: datar, 60°,\nikatan "pisang" (jingga), C–H bertindih', fontsize=8.3, color=TUA, y=-0.22)
sq = np.array([(-1.0, -0.5), (0.4, -0.75), (1.0, -0.1), (-0.4, 0.45)])
ax[1].add_patch(Polygon(sq, closed=True, fc='#eef4fa', ec=TUA, lw=2)); ax[1].plot([-0.4, -0.4], [0.45, 0.9], color='none')
ax[1].plot(*zip(sq[3], sq[3] + np.array([0, 0.5])), color=BIRU, lw=1.3); ax[1].plot(*zip(sq[1], sq[1] + np.array([0, -0.5])), color=BIRU, lw=1.3)
ax[1].annotate('', (-0.4, 0.95), (-0.4, 0.45), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.2)); ax[1].text(-0.25, 1.1, 'terlipat ±25°', fontsize=8, color=JT)
ax[1].set_title('siklobutana: lipatan kupu-kupu', fontsize=8.3, color=TUA, y=-0.22)
pen = np.array([(-1.1, -0.3), (-0.3, -0.75), (0.8, -0.55), (1.0, 0.1), (0.0, 0.55)])
ax[2].add_patch(Polygon(pen[[0, 1, 2, 3]], closed=False, fill=False, ec=TUA, lw=2)); ax[2].plot(*zip(pen[3], pen[0]), color=TUA, lw=0.8, ls='--')
flap = np.array([0.0, 1.05]); ax[2].plot(*zip(pen[3], flap, pen[0]), color=TUA, lw=2); ax[2].plot(*flap, 'o', color=JT, ms=6)
ax[2].text(0.25, 1.25, 'satu karbon keluar bidang', fontsize=8, color=JT)
ax[2].set_title('siklopentana: amplop', fontsize=8.3, color=TUA, y=-0.22)
plt.tight_layout(); simpan(f, 'cincinkecil')

# 11. kursi dan perahu
def ring(ax, Q, c=TUA, lw=2):
    for i in range(6): ax.plot(*zip(Q[i], Q[(i + 1) % 6]), color=c, lw=lw, zorder=2)
f, ax = plt.subplots(1, 2, figsize=(7.0, 2.8), dpi=220)
for a in ax: a.set_xlim(-2.2, 2.2); a.set_ylim(-1.3, 1.5); a.set_aspect('equal'); a.axis('off')
kursi(ax[0], True, False, L=0.5); ax[0].set_title('kursi: semua ikatan goyang,\ntanpa tegangan', fontsize=9, color=TUA, y=-0.12)
B = np.array([(-1.5, 0.35), (-0.65, -0.1), (0.65, -0.1), (1.5, 0.35), (0.65, 0.2), (-0.65, 0.2)])
ring(ax[1], B)
for i, up in [(0, True), (3, True)]:
    ax[1].plot([B[i][0], B[i][0] + (0.35 if i == 0 else -0.35)], [B[i][1], B[i][1] + 0.65], color=MERAH if False else JT, lw=1.6)
ax[1].plot([-1.15, 1.15], [1.0, 1.0], color='#c0392b', lw=1.0, ls=(0, (2, 2))); ax[1].text(0, 1.18, 'H tiang bendera berdesakan', fontsize=8.3, color='#c0392b', ha='center')
ax[1].text(-1.15, 1.0, 'H', fontsize=9, color=JT, ha='center', va='bottom'); ax[1].text(1.15, 1.0, 'H', fontsize=9, color=JT, ha='center', va='bottom')
ax[1].set_title('perahu: ikatan bertindih di sisi,\nH tiang bendera berdesakan (+29 kJ mol$^{-1}$)', fontsize=9, color=TUA, y=-0.12)
plt.tight_layout(); simpan(f, 'perahu')

# 12. metilsikloheksana aksial dan ekuatorial
def sub(ax, i, aksial, lab, c=JT, L=0.6):
    cen = P.mean(0)
    if aksial: d = np.array([0, 1.0 if naik[i] else -1.0])
    else:
        d = P[(i + 2) % 6] - P[(i + 1) % 6]; d = d / np.linalg.norm(d)
        if np.dot(d, P[i] - cen) < 0: d = -d
    e = P[i] + d * L; ax.plot(*zip(P[i], e), color=c, lw=2, zorder=3); ax.text(*(e + d * 0.28), lab, ha='center', va='center', fontsize=9.5, color=c, fontweight='bold'); return e
f, ax = plt.subplots(1, 2, figsize=(7.2, 3.0), dpi=220)
for a in ax: a.set_xlim(-2.4, 2.4); a.set_ylim(-1.6, 1.6); a.set_aspect('equal'); a.axis('off'); kursi(a, False, False)
e = sub(ax[0], 1, True, 'CH₃')
for j in (3, 5):
    h = sub(ax[0], j, True, 'H', c=BIRU, L=0.55); ax[0].plot(*zip(e, h), color='#c0392b', lw=1.0, ls=(0, (2, 2)))
ax[0].set_title('CH₃ aksial: dua tolakan 1,3-diaksial\n(lebih tinggi 7,3 kJ mol$^{-1}$; 5%)', fontsize=9, color=TUA, y=-0.12)
sub(ax[1], 1, False, 'CH₃'); [sub(ax[1], j, True, 'H', c=BIRU, L=0.55) for j in (3, 5)]
ax[1].set_title('CH₃ ekuatorial: menjauhi cincin\n(lebih stabil; 95% pada 25 °C)', fontsize=9, color=TUA, y=-0.12)
f.text(0.5, 0.55, '⇌', ha='center', va='center', fontsize=20, color=TUA, family='DejaVu Sans')
plt.tight_layout(w_pad=3); simpan(f, 'metil')

# 13. nilai A
nm = ['–CN', '–F', '–Br', '–Cl', '–OH', '–COOH', '–CH₃', '–CH₂CH₃', '–CH(CH₃)₂', '–C₆H₅', '–C(CH₃)₃']; v = [0.8, 1.0, 2.0, 2.2, 3.6, 5.9, 7.3, 7.5, 9.2, 11.7, 20]
f, ax = plt.subplots(figsize=(6.0, 3.2), dpi=220)
b = ax.barh(nm[::-1], v[::-1], color=[JT if x >= 15 else (BIRU if x >= 7 else MUDA) for x in v[::-1]])
for bb, x in zip(b, v[::-1]): ax.text(x + 0.3, bb.get_y() + bb.get_height() / 2, ('± ' if x == 20 else '') + kom(x, 0), va='center', fontsize=8.3, color=TUA)
ax.set_xlabel('nilai A (kJ mol$^{-1}$): preferensi ekuatorial'); ax.xaxis.set_major_formatter(kom); ax.set_xlim(0, 23)
plt.tight_layout(); simpan(f, 'nilaiA')

# 14. cis-1,3-dimetilsikloheksana: e,e lawan a,a
f, ax = plt.subplots(1, 2, figsize=(7.2, 3.0), dpi=220)
for a in ax: a.set_xlim(-2.4, 2.4); a.set_ylim(-1.6, 1.6); a.set_aspect('equal'); a.axis('off'); kursi(a, False, False)
sub(ax[0], 1, False, 'CH₃'); sub(ax[0], 3, False, 'CH₃'); ax[0].set_title('e,e: kedua CH₃ ekuatorial\n(jauh lebih stabil)', fontsize=9, color=HJ, y=-0.12)
e1 = sub(ax[1], 1, True, 'CH₃'); e2 = sub(ax[1], 3, True, 'CH₃'); ax[1].plot(*zip(e1, e2), color='#c0392b', lw=1.2, ls=(0, (2, 2)))
ax[1].set_title('a,a: kedua CH₃ aksial dan saling\nberdesakan (1,3-diaksial CH₃/CH₃)', fontsize=9, color='#c0392b', y=-0.12)
f.text(0.5, 0.75, '⇌', ha='center', va='center', fontsize=20, color=TUA, family='DejaVu Sans'); f.text(0.5, 0.97, 'cis-1,3-dimetilsikloheksana', ha='center', fontsize=10, color=TUA, fontweight='bold')
plt.tight_layout(w_pad=3, rect=(0, 0, 1, 0.94)); simpan(f, 'dimetil')

# 15. dekalin dan steroid
f, ax = plt.subplots(1, 3, figsize=(7.6, 2.6), dpi=220)
dat = [('[H][C@]12CCCC[C@@]1([H])CCCC2', 'trans-dekalin: H jembatan\nberseberangan, kaku'), ('[H][C@]12CCCC[C@]1([H])CCCC2', 'cis-dekalin: H jembatan\nsepihak, dapat membalik'),
       ('C[C@]12CC[C@H]3[C@@H](CC[C@@H]4CCCC[C@]34C)[C@@H]1CCC2', 'kerangka steroid (5α-androstana):\nempat cincin menyatu')]
for a, (s, t) in zip(ax, dat): a.imshow(rd(s, w=460, h=340, bl=34, fs=22)); a.axis('off'); a.set_title(t, fontsize=8.3, color=TUA, y=-0.22)
plt.tight_layout(); simpan(f, 'dekalin')

# 16. energi per gram bahan bakar
f, ax = plt.subplots(figsize=(5.6, 2.8), dpi=220)
nm = ['hidrogen', 'metana', 'oktana', 'etanol', 'glukosa']; v = [142, 55.5, 47.9, 29.7, 15.6]
b = ax.bar(nm, v, color=[MUDA, BIRU, BIRU, JT, JT])
for bb, x in zip(b, v): ax.text(bb.get_x() + bb.get_width() / 2, x + 2, kom(x, 0), ha='center', fontsize=8.5, color=TUA)
ax.set_ylabel('kalor pembakaran (kJ g$^{-1}$)'); ax.set_ylim(0, 160); ax.text(3.0, 70, 'sudah mengandung O:\nsebagian "sudah terbakar"', fontsize=8, color=JT, ha='center')
plt.tight_layout(); simpan(f, 'bakar')
print('ok tambahan')
