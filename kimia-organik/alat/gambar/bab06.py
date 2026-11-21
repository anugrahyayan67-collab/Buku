# Gambar Bab 6: diagram energi, Hammond, karbokation, kendali kinetik/termodinamik
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from scipy.interpolate import CubicSpline
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab06/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
def kurva(ax, x, y, c=BIRU):
    xx = np.linspace(x[0], x[-1], 500); ax.plot(xx, CubicSpline(x, y, bc_type='clamped')(xx), color=c, lw=2)
def gaya(ax):
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('koordinat reaksi'); ax.set_ylabel('energi')

# 1. diagram energi
f, ax = plt.subplots(1, 2, figsize=(7.2, 2.9), dpi=220)
kurva(ax[0], [0, 1, 2, 3, 4], [2, 2.3, 6, 1.5, 0.8]); gaya(ax[0])
ax[0].text(2, 6.3, '‡', ha='center', fontsize=13, color=JT); ax[0].text(0, 2.3, 'pereaksi', fontsize=8.5, color=TUA); ax[0].text(3.2, 0.3, 'produk', fontsize=8.5, color=TUA)
ax[0].annotate('', (1.0, 6.0), (1.0, 2.05), arrowprops=dict(arrowstyle='<->', color=JT)); ax[0].text(0.55, 4.0, '$E_a$', color=JT, fontsize=10)
ax[0].annotate('', (3.9, 0.85), (3.9, 2.0), arrowprops=dict(arrowstyle='<->', color=HJ)); ax[0].plot([0, 3.9], [2, 2], color='#c9d2db', lw=0.8, ls=':'); ax[0].text(3.95, 1.3, 'ΔG°', color=HJ, fontsize=9)
ax[0].set_ylim(0, 7.2); ax[0].set_title('satu langkah', fontsize=9.5, color=TUA)
kurva(ax[1], [0, 1, 2, 3, 4, 5, 6], [2, 2.2, 6.2, 4.0, 5.2, 1.0, 0.8]); gaya(ax[1])
ax[1].text(2, 6.5, '‡₁', ha='center', fontsize=12, color=JT); ax[1].text(4, 5.6, '‡₂', ha='center', fontsize=12, color=JT)
ax[1].text(3, 3.4, 'I', ha='center', fontsize=11, color=BIRU, fontweight='bold'); ax[1].text(0, 2.3, 'pereaksi', fontsize=8.5, color=TUA); ax[1].text(5.1, 0.3, 'produk', fontsize=8.5, color=TUA)
ax[1].set_ylim(0, 7.2); ax[1].set_title('dua langkah, dengan intermediet', fontsize=9.5, color=TUA)
plt.tight_layout(); f.savefig(f'{F}/energi.png', bbox_inches='tight'); plt.close(f)

# 2. Hammond
f, ax = plt.subplots(1, 2, figsize=(6.8, 2.8), dpi=220)
kurva(ax[0], [0, 1.2, 2.6, 3.2, 4], [1, 1.4, 5.6, 5.0, 4.8], JT); gaya(ax[0]); ax[0].set_ylim(0, 6.6)
ax[0].text(2.6, 5.9, '‡ mirip produk', ha='center', fontsize=8.5, color=JT); ax[0].text(0, 0.4, 'pereaksi', fontsize=8.5); ax[0].text(3.3, 4.2, 'produk', fontsize=8.5)
ax[0].set_title('endoterm: keadaan transisi lambat', fontsize=9, color=TUA)
kurva(ax[1], [0, 0.8, 1.4, 2.8, 4], [4.8, 5.0, 5.6, 1.4, 1.0], HJ); gaya(ax[1]); ax[1].set_ylim(0, 6.6)
ax[1].text(1.4, 5.9, '‡ mirip pereaksi', ha='center', fontsize=8.5, color=HJ); ax[1].text(0, 4.2, 'pereaksi', fontsize=8.5); ax[1].text(3.3, 0.4, 'produk', fontsize=8.5)
ax[1].set_title('eksoterm: keadaan transisi awal', fontsize=9, color=TUA)
plt.tight_layout(); f.savefig(f'{F}/hammond.png', bbox_inches='tight'); plt.close(f)

# 3. karbokation: hiperkonjugasi + urutan
f, ax = plt.subplots(1, 2, figsize=(7.2, 2.9), dpi=220, gridspec_kw={'width_ratios': [1, 1.25]})
a = ax[0]; a.set_xlim(-2.2, 2.4); a.set_ylim(-1.8, 1.9); a.set_aspect('equal'); a.axis('off')
for s in (1, -1): a.add_patch(Ellipse((0.8, 0.62 * s), 0.55, 1.15, fc='white', ec=TUA, lw=1.2))
a.text(0.8, 0.62, 'kosong', ha='center', va='center', fontsize=7, color=TUA)
a.plot(0.8, 0, 'o', color=TUA, ms=6); a.text(1.05, -0.12, 'C$^+$', fontsize=10, color=JT)
a.plot([0.8, -0.4], [0, 0], color=TUA, lw=2); a.plot(-0.4, 0, 'o', color=TUA, ms=6)
a.plot([-0.4, -0.4], [0, 1.0], color=BIRU, lw=2.2); a.text(-0.55, 1.15, 'H', fontsize=10, color=BIRU)
a.add_patch(Ellipse((-0.25, 0.75), 0.4, 0.95, angle=-20, fc=MUDA, ec=BIRU, lw=1, alpha=0.6))
a.annotate('', (0.55, 0.75), (-0.05, 0.85), arrowprops=dict(arrowstyle='-|>', color=JT, lw=1.3, connectionstyle='arc3,rad=-0.3'))
a.plot([-0.4, -1.2], [0, -0.6], color=TUA, lw=1.5); a.plot([-0.4, -1.0], [0, -1.0], color=TUA, lw=1.5)
a.set_title('hiperkonjugasi: σ(C–H) → p kosong', fontsize=8.8, color=TUA, y=-0.08)
b = ax[1]; lab = ['CH$_3^+$', 'RCH$_2^+$\n(1°)', 'R$_2$CH$^+$\n(2°)', 'R$_3$C$^+$\n(3°)', 'alilik /\nbenzilik']; val = [1, 2, 3, 4, 4.3]
b.bar(range(5), val, color=[MUDA, BIRU, BIRU, TUA, HJ], width=0.65)
b.set_xticks(range(5)); b.set_xticklabels(lab, fontsize=8); b.set_yticks([]); b.set_ylabel('kestabilan (kualitatif)')
b.set_title('kestabilan karbokation', fontsize=9, color=TUA)
plt.tight_layout(); f.savefig(f'{F}/kation.png', bbox_inches='tight'); plt.close(f)

# 4. kendali kinetik vs termodinamik
f, ax = plt.subplots(figsize=(5.6, 3.0), dpi=220)
X = [-2, -1, 0, 1, 2]; Y = [2.6, 6.2, 5.0, 7.0, 1.2]; xx = np.linspace(-2, 2, 600); yy = CubicSpline(X, Y, bc_type='clamped')(xx)
ax.plot(xx[xx <= 0], yy[xx <= 0], color=JT, lw=2); ax.plot(xx[xx >= 0], yy[xx >= 0], color=HJ, lw=2)
ax.text(0, 4.5, 'intermediet', ha='center', fontsize=8.5, color=TUA)
ax.text(-2, 1.6, 'produk K\n(kinetik)', ha='center', fontsize=8.5, color=JT); ax.text(2, 0.2, 'produk T\n(termodinamik)', ha='center', fontsize=8.5, color=HJ)
ax.text(-1, 6.45, 'penghalang\nrendah', ha='center', fontsize=7.8, color=JT); ax.text(1, 7.3, 'penghalang tinggi', ha='center', fontsize=7.8, color=HJ)
gaya(ax); ax.set_ylim(-0.6, 8.2); ax.set_xlim(-2.6, 2.6)
f.savefig(f'{F}/kendali.png', bbox_inches='tight'); plt.close(f)
print('ok')

# ================= gambar tambahan =================
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matplotlib.ticker
from matplotlib.patches import FancyArrowPatch, Ellipse, Circle, FancyBboxPatch
from lewis import molekul as _mol, lengkung, resonansi, panah, MERAH
from functools import partial
molekul = partial(_mol, fs=10.5, gap=0.22)
koma = lambda v: f'{v:g}'.replace('.', ',').replace('-', '−')
fmt = matplotlib.ticker.FuncFormatter(lambda q, _: koma(round(q, 3)))
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def T(ax, x, y, s, c=TUA, fs=10, **k): ax.text(x, y, s, ha=k.pop('ha', 'center'), va=k.pop('va', 'center'), color=c, fontsize=fs, **k)
def simpan(f, n): f.savefig(f'{F}/{n}.png', bbox_inches='tight'); plt.close(f)
def dp(ax, x, y, t, c): ax.text(x, y, t, ha='center', va='center', fontsize=8.5, color=c, fontweight='bold')

# 5. nukleofil dan elektrofil
f, ax = kanv(7.4, 3.6, (0, 30), (0, 14))
T(ax, 1.0, 12.4, 'nukleofil: kaya elektron (pasangan bebas atau ikatan π)', fs=9.5, c=BIRU, ha='left', fontweight='bold')
molekul(ax, {'O': (0, 0, 'O'), 'H': (1.0, 0, 'H')}, [('O', 'H', 1)], lp={'O': [90, 180, 270]}, muatan={'O': ('-', 135)}, ox=2.5, oy=9.2, s=1.6)
molekul(ax, {'O': (0, 0, 'O'), 'a': (-0.8, -0.65, 'H'), 'b': (0.8, -0.65, 'H')}, [('O', 'a', 1), ('O', 'b', 1)], lp={'O': [60, 120]}, ox=8.0, oy=9.4, s=1.6)
molekul(ax, {'N': (0, 0, 'N'), 'a': (-0.8, -0.6, 'H'), 'b': (0.8, -0.6, 'H'), 'c': (0, -1.0, 'H')}, [('N', 'a', 1), ('N', 'b', 1), ('N', 'c', 1)], lp={'N': [90]}, ox=13.0, oy=9.6, s=1.6)
molekul(ax, {'C': (0, 0, 'C'), 'N': (1.2, 0, 'N')}, [('C', 'N', 3)], lp={'C': [180], 'N': [0]}, muatan={'C': ('-', 100)}, ox=17.5, oy=9.2, s=1.6)
molekul(ax, {'a': (0, 0, 'C'), 'b': (1.3, 0, 'C'), 'h1': (-0.8, 0.6, 'H'), 'h2': (-0.8, -0.6, 'H'), 'h3': (2.1, 0.6, 'H'), 'h4': (2.1, -0.6, 'H')}, [('a', 'b', 2), ('a', 'h1', 1), ('a', 'h2', 1), ('b', 'h3', 1), ('b', 'h4', 1)], ox=23.5, oy=9.2, s=1.6)
for x, t in [(3.2, 'hidroksida'), (8.0, 'air'), (13.0, 'amonia'), (18.3, 'sianida'), (24.3, 'alkena (π)')]: T(ax, x, 7.2, t, fs=8.3)
T(ax, 1.0, 5.6, 'elektrofil: miskin elektron (muatan +, δ+, atau orbital kosong)', fs=9.5, c=MERAH, ha='left', fontweight='bold')
T(ax, 2.8, 2.8, 'H$^+$', fs=14, c=MERAH, fontweight='bold')
molekul(ax, {'C': (0, 0, 'C'), 'a': (-0.9, 0.55, 'H'), 'b': (-0.9, -0.55, 'H'), 'c': (1.0, 0, 'H')}, [('C', 'a', 1), ('C', 'b', 1), ('C', 'c', 1)], muatan={'C': ('+', 90)}, ox=8.0, oy=2.8, s=1.6)
molekul(ax, {'C': (0, 0, 'C'), 'O': (1.3, 0, 'O'), 'a': (-0.8, 0.65, 'H'), 'b': (-0.8, -0.65, 'H')}, [('C', 'O', 2), ('C', 'a', 1), ('C', 'b', 1)], lp={'O': [45, -45]}, ox=12.8, oy=2.8, s=1.6); dp(ax, 12.8, 3.65, 'δ+', MERAH); dp(ax, 14.5, 3.65, 'δ−', BIRU)
molekul(ax, {'C': (0, 0, 'C'), 'Br': (1.4, 0, 'Br'), 'a': (-0.9, 0.6, 'H'), 'b': (-0.9, -0.6, 'H'), 'c': (0, -1.0, 'H')}, [('C', 'Br', 1), ('C', 'a', 1), ('C', 'b', 1), ('C', 'c', 1)], lp={'Br': [90, 0, 270]}, ox=18.5, oy=2.9, s=1.6); dp(ax, 18.5, 3.8, 'δ+', MERAH)
molekul(ax, {'B': (0, 0, 'B'), 'a': (0.7, 0.75, 'F'), 'b': (0.7, -0.75, 'F'), 'c': (-1.0, 0, 'F')}, [('B', 'a', 1), ('B', 'b', 1), ('B', 'c', 1)], ox=25.0, oy=2.8, s=1.6)
for x, t in [(2.8, 'proton'), (8.0, 'karbokation'), (13.6, 'karbon karbonil'), (19.4, 'karbon alkil halida'), (25.0, 'BF₃ (orbital kosong)')]: T(ax, x, 0.5, t, fs=8.3)
simpan(f, 'nukelek')

# 6. panah lengkung SN2
f, ax = kanv(7.4, 2.4, (0, 30), (0, 9))
A = molekul(ax, {'O': (0, 0, 'O'), 'H': (-1.0, 0, 'H')}, [('O', 'H', 1)], lp={'O': [90, 270, 0]}, muatan={'O': ('-', 45)}, ox=2.6, oy=4.5, s=1.6)
B = molekul(ax, {'C': (0, 0, 'C'), 'Br': (1.5, 0, 'Br'), 'a': (-0.5, 0.95, 'H'), 'b': (-0.5, -0.95, 'H'), 'c': (-0.9, 0.0, 'H')}, [('C', 'Br', 1), ('C', 'a', 1), ('C', 'b', 1)], lp={'Br': [90, 0, 270]}, ox=8.2, oy=4.5, s=1.6)
ax.plot([B['C'][0], B['C'][0] + 0.55], [4.5, 4.5], color='none')
lengkung(ax, A['O'] + np.array([0.45, 0.0]), B['C'] + np.array([-0.35, 0.05]), rad=-0.35)
lengkung(ax, (B['C'] + B['Br']) / 2 + np.array([0, 0.15]), B['Br'] + np.array([0.1, 0.55]), rad=-0.6)
panah(ax, (12.6, 4.5), (15.0, 4.5))
molekul(ax, {'O': (0, 0, 'O'), 'H': (-1.0, 0, 'H'), 'C': (1.4, 0, 'C'), 'a': (1.9, 0.95, 'H'), 'b': (1.9, -0.95, 'H'), 'c': (2.4, 0, 'H')}, [('O', 'H', 1), ('O', 'C', 1), ('C', 'a', 1), ('C', 'b', 1), ('C', 'c', 1)], lp={'O': [90, 270]}, ox=17.0, oy=4.5, s=1.6)
T(ax, 22.6, 4.6, '+', fs=13)
molekul(ax, {'Br': (0, 0, 'Br')}, [], lp={'Br': [0, 90, 180, 270]}, muatan={'Br': ('-', 45)}, ox=24.3, oy=4.5, s=1.6)
T(ax, 6.0, 0.8, 'panah berpangkal pada pasangan elektron (pasangan bebas atau ikatan)\ndan berujung di tempat pasangan itu menjadi ikatan baru atau pasangan bebas', fs=8.3, c='#444444')
T(ax, 27.8, 4.5, 'ikatan\nC–O baru', fs=8, c=HJ)
simpan(f, 'sn2panah')

# 7. empat pola langkah polar
f, ax = kanv(7.4, 8.2, (0, 30), (0, 33))
S7 = 1.75
def judul(y, t, ket): T(ax, 0.3, y, t, fs=9.5, ha='left', c=BIRU, fontweight='bold'); T(ax, 29.7, y, ket, fs=8.2, ha='right', c='#555555')
# (1)
judul(32.0, '1. serangan nukleofil', 'nukleofil memberi pasangan elektron')
A = molekul(ax, {'Br': (0, 0, 'Br')}, [], lp={'Br': [90, 180, 270, 0]}, muatan={'Br': ('-', 135)}, ox=3.0, oy=28.0, s=S7)
B = molekul(ax, {'C': (0, 0, 'C'), 'a': (1.0, 0.65, 'CH₃'), 'b': (1.0, -0.65, 'CH₃'), 'c': (-0.6, 1.0, 'CH₃')}, [('C', 'a', 1), ('C', 'b', 1), ('C', 'c', 1)], muatan={'C': ('+', 200)}, ox=9.0, oy=28.0, s=S7)
lengkung(ax, A['Br'] + np.array([0.55, 0.3]), B['C'] + np.array([-0.45, 0.2]), rad=-0.4)
panah(ax, (13.6, 28.0), (16.2, 28.0))
molekul(ax, {'Br': (0, 0, 'Br'), 'C': (1.5, 0, 'C'), 'a': (2.5, 0.65, 'CH₃'), 'b': (2.5, -0.65, 'CH₃'), 'c': (1.5, 1.15, 'CH₃')}, [('Br', 'C', 1), ('C', 'a', 1), ('C', 'b', 1), ('C', 'c', 1)], lp={'Br': [90, 180, 270]}, ox=18.5, oy=28.0, s=S7)
# (2)
judul(23.5, '2. lepasnya gugus pergi', 'ikatan putus; elektron pergi bersama gugus pergi')
A = molekul(ax, {'C': (0, 0, 'C'), 'O': (1.5, 0, 'O'), 'h1': (2.3, 0.65, 'H'), 'h2': (2.3, -0.65, 'H'), 'r1': (-1.0, 0.65, 'CH₃'), 'r2': (-1.0, -0.65, 'CH₃'), 'r3': (0, 1.15, 'CH₃')},
            [('C', 'O', 1), ('O', 'h1', 1), ('O', 'h2', 1), ('C', 'r1', 1), ('C', 'r2', 1), ('C', 'r3', 1)], lp={'O': [270]}, muatan={'O': ('+', 90)}, ox=3.8, oy=19.3, s=S7)
lengkung(ax, (A['C'] + A['O']) / 2 + np.array([0, -0.2]), A['O'] + np.array([0.15, -0.75]), rad=0.6)
panah(ax, (10.2, 19.3), (12.6, 19.3))
molekul(ax, {'C': (0, 0, 'C'), 'r1': (-1.0, 0.65, 'CH₃'), 'r2': (-1.0, -0.65, 'CH₃'), 'r3': (1.2, 0, 'CH₃')}, [('C', 'r1', 1), ('C', 'r2', 1), ('C', 'r3', 1)], muatan={'C': ('+', 90)}, ox=16.2, oy=19.3, s=S7)
T(ax, 21.6, 19.4, '+', fs=12)
molekul(ax, {'O': (0, 0, 'O'), 'a': (-0.85, -0.7, 'H'), 'b': (0.85, -0.7, 'H')}, [('O', 'a', 1), ('O', 'b', 1)], lp={'O': [60, 120]}, ox=24.5, oy=19.8, s=S7)
# (3)
judul(15.0, '3. transfer proton', 'asam–basa: proton berpindah')
A = molekul(ax, {'O': (0, 0, 'O'), 'R': (-1.2, 0, 'R'), 'H': (0, 1.1, 'H')}, [('O', 'R', 1), ('O', 'H', 1)], lp={'O': [270, 0]}, ox=3.0, oy=10.4, s=S7)
B = molekul(ax, {'H': (0, 0, 'H'), 'Br': (1.4, 0, 'Br')}, [('H', 'Br', 1)], lp={'Br': [90, 0, 270]}, ox=7.4, oy=10.4, s=S7)
lengkung(ax, A['O'] + np.array([0.65, -0.3]), B['H'] + np.array([0.0, -0.45]), rad=0.5)
lengkung(ax, (B['H'] + B['Br']) / 2 + np.array([0, 0.2]), B['Br'] + np.array([0, 0.75]), rad=-0.6)
panah(ax, (13.0, 10.4), (15.4, 10.4))
molekul(ax, {'O': (0, 0, 'O'), 'R': (-1.2, 0, 'R'), 'H': (0, 1.1, 'H'), 'H2': (1.0, -0.6, 'H')}, [('O', 'R', 1), ('O', 'H', 1), ('O', 'H2', 1)], lp={'O': [240]}, muatan={'O': ('+', 45)}, ox=18.5, oy=10.4, s=S7)
T(ax, 22.4, 10.5, '+', fs=12)
molekul(ax, {'Br': (0, 0, 'Br')}, [], lp={'Br': [0, 90, 180, 270]}, muatan={'Br': ('-', 45)}, ox=24.8, oy=10.4, s=S7)
# (4)
judul(6.5, '4. penataan ulang (geseran 1,2-hidrida)', 'karbokation 2° → karbokation 3° (lebih stabil)')
A = molekul(ax, {'c2': (0, 0, 'C'), 'c3': (1.6, 0, 'C'), 'H': (1.6, 1.2, 'H'), 'm': (-1.1, 0.6, 'CH₃'), 'm2': (2.7, -0.65, 'CH₃'), 'm3': (2.7, 0.65, 'CH₃')}, [('c2', 'c3', 1), ('c3', 'H', 1), ('c2', 'm', 1), ('c3', 'm2', 1), ('c3', 'm3', 1)],
            muatan={'c2': ('+', 270)}, ox=3.8, oy=2.0, s=S7)
lengkung(ax, (A['c3'] + A['H']) / 2 + np.array([-0.2, 0]), A['c2'] + np.array([0.2, 0.5]), rad=0.5)
panah(ax, (11.6, 2.2), (14.0, 2.2))
molekul(ax, {'c2': (0, 0, 'C'), 'c3': (1.6, 0, 'C'), 'H': (0, 1.2, 'H'), 'm': (-1.1, 0.6, 'CH₃'), 'm2': (2.7, -0.65, 'CH₃'), 'm3': (2.7, 0.65, 'CH₃')}, [('c2', 'c3', 1), ('c2', 'H', 1), ('c2', 'm', 1), ('c3', 'm2', 1), ('c3', 'm3', 1)],
        muatan={'c3': ('+', 270)}, ox=17.6, oy=2.0, s=S7)
simpan(f, 'pola')

# 8. ΔH dari energi ikatan
f, ax = plt.subplots(figsize=(6.0, 3.0), dpi=220)
X = ['Cl', 'Br', 'I']; putus = [439 + 242, 439 + 192, 439 + 151]; bentuk = [350 + 432, 294 + 366, 239 + 298]
x = np.arange(3); ax.bar(x - 0.2, putus, 0.38, color=BIRU, label='ikatan putus (CH₃–H + X–X)'); ax.bar(x + 0.2, bentuk, 0.38, color=JT, label='ikatan terbentuk (CH₃–X + H–X)')
for i in range(3):
    dH = putus[i] - bentuk[i]; ax.text(i, max(putus[i], bentuk[i]) + 25, f'Δ$H$° = {"+" if dH > 0 else ""}{koma(dH)}', ha='center', fontsize=8.5, color=TUA, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels([f'X = {t}' for t in X]); ax.set_ylabel('energi ikatan (kJ mol$^{-1}$)'); ax.set_ylim(0, 1050); ax.legend(frameon=False, fontsize=8, loc='upper right', ncol=1)
plt.tight_layout(); simpan(f, 'bde')

# 9. distribusi Maxwell–Boltzmann (skematis)
f, ax = plt.subplots(figsize=(5.8, 3.0), dpi=220)
E = np.linspace(0, 40, 800)
for T_, c, lab in [(1.0, BIRU, 'suhu rendah'), (1.4, JT, 'suhu tinggi')]:
    y = np.sqrt(E) * np.exp(-E / (4 * T_)) / (T_ ** 1.5); ax.plot(E, y, color=c, lw=2, label=lab); ax.fill_between(E, y, where=E > 22, color=c, alpha=0.25)
ax.axvline(22, color=TUA, lw=1, ls='--'); ax.text(22.5, 0.75, '$E_a$', fontsize=10, color=TUA)
ax.text(27, 0.25, 'molekul dengan\nenergi ≥ $E_a$', fontsize=8.3, color=TUA)
ax.set_xlabel('energi kinetik molekul'); ax.set_ylabel('jumlah molekul'); ax.set_yticks([]); ax.set_xticks([]); ax.legend(frameon=False, fontsize=8.5)
plt.tight_layout(); simpan(f, 'mb')

# 10. geometri karbokation, radikal, karbanion
f, ax = plt.subplots(1, 3, figsize=(7.4, 2.8), dpi=220)
for a in ax: a.set_xlim(-2, 2); a.set_ylim(-2, 2); a.set_aspect('equal'); a.axis('off')
def subst(a, angs, z=(0, 0, 0)):
    for ang in angs: r = np.radians(ang); a.plot([0, 1.1 * np.cos(r)], [0, 0.55 * np.sin(r) - 0.0], color=TUA, lw=2); a.text(1.35 * np.cos(r), 0.7 * np.sin(r), 'R', ha='center', va='center', fontsize=9, color=TUA)
subst(ax[0], [165, 15, 240]); 
for s in (1, -1): ax[0].add_patch(Ellipse((0, s * 0.85), 0.55, 1.4, fc='none', ec=BIRU, lw=1.4, ls='--'))
ax[0].set_title('karbokation: sp², datar,\norbital p kosong', fontsize=8.6, color=TUA, y=-0.12)
for a_, pyr, e in [(ax[1], 0.25, 1), (ax[2], 0.6, 2)]:
    for ang in (210, 330, 270):
        r = np.radians(ang); a_.plot([0, 1.1 * np.cos(r)], [0, 0.55 * np.sin(r) - pyr], color=TUA, lw=2); a_.text(1.35 * np.cos(r), 0.7 * np.sin(r) - pyr - 0.15, 'R', ha='center', va='center', fontsize=9, color=TUA)
    a_.add_patch(Ellipse((0, 0.75), 0.6, 1.2, fc=MUDA if e == 2 else '#dbeefc', ec=BIRU, lw=1.2, alpha=0.8))
    for k in range(e): a_.add_patch(Circle(((-0.1 if e == 2 and k == 0 else 0.1 if e == 2 else 0), 0.85), 0.07, color=TUA))
ax[1].set_title('radikal: hampir datar,\nsatu elektron', fontsize=8.6, color=TUA, y=-0.12)
ax[2].set_title('karbanion: sp³, piramidal,\npasangan bebas', fontsize=8.6, color=TUA, y=-0.12)
for a in ax: a.plot(0, 0, 'o', color=TUA, ms=5)
plt.tight_layout(); simpan(f, 'geometri')

# 11. siklus propagasi radikal
f, ax = kanv(6.4, 3.2, (0, 24), (0, 12))
ax.add_patch(Circle((12, 6), 3.4, fc='none', ec=BIRU, lw=1.6, ls='--'))
T(ax, 12, 9.9, 'Cl·', fs=13, c=MERAH, fontweight='bold'); T(ax, 12, 2.1, '·CH₃', fs=13, c=MERAH, fontweight='bold')
ax.add_patch(FancyArrowPatch((14.6, 8.4), (14.6, 3.6), connectionstyle='arc3,rad=-0.45', arrowstyle='-|>', mutation_scale=14, color=TUA, lw=1.6))
ax.add_patch(FancyArrowPatch((9.4, 3.6), (9.4, 8.4), connectionstyle='arc3,rad=-0.45', arrowstyle='-|>', mutation_scale=14, color=TUA, lw=1.6))
T(ax, 19.8, 7.2, '+ CH₄', fs=10); T(ax, 19.8, 4.8, '→ HCl', fs=10, c=HJ); T(ax, 19.8, 9.0, 'propagasi 1 (Δ$H$° = +7)', fs=8.2, c='#555555')
T(ax, 4.2, 4.8, '+ Cl₂', fs=10); T(ax, 4.2, 7.2, '→ CH₃Cl', fs=10, c=HJ); T(ax, 4.2, 3.0, 'propagasi 2 (Δ$H$° = −108)', fs=8.2, c='#555555')
T(ax, 12, 11.4, 'inisiasi: Cl₂ + $h\\nu$ → 2 Cl·   ·   terminasi: dua radikal bergabung', fs=8.5, c=TUA)
T(ax, 12, 6.0, 'satu Cl· memutar\nrantai ribuan kali', fs=8, c=BIRU)
simpan(f, 'rantai')
print('ok tambahan')
