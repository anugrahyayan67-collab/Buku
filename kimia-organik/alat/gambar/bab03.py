# Gambar Bab 3: skala pKa, fraksi terionisasi, skema ekstraksi
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 9.5, 'axes.spines.top': False, 'axes.spines.right': False})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
F = f'{R}/bab03/fig'; os.makedirs(F, exist_ok=True)
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))

# 1. skala pKa
f, ax = plt.subplots(figsize=(7.6, 2.6), dpi=220)
ax.set_xlim(-12, 52); ax.set_ylim(-1.9, 3.2); ax.axis('off')
ax.annotate('', (52, 0), (-12, 0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.4))
for x in range(-10, 51, 10):
    ax.plot([x, x], [-0.12, 0.12], color=TUA, lw=1); ax.text(x, -0.45, f'{x}'.replace('-', '−'), ha='center', fontsize=8.5, color=TUA)
ax.text(52, 0.3, 'pKa', ha='right', fontsize=9, color=TUA, style='italic')
dat = [(-7, 'HCl', 1), (-1.7, 'H₃O$^+$', 2), (4.8, 'RCOOH', 1), (9.3, 'R–NH₃$^+$', 2.1), (10, 'ArOH', 1), (15.7, 'H₂O', 2), (16, 'ROH', 1.1), (19, 'R₂C=O (α-H)', 2.6), (25, 'RC≡CH', 1), (38, 'NH₃', 1.6), (44, 'CH₂=CH₂', 2.4), (50, 'CH₄', 1)]
for x, t, y in dat:
    ax.plot([x, x], [0.15, y - 0.15], color='#9aa5b1', lw=0.8); ax.plot(x, 0, 'o', color=BIRU, ms=4, zorder=3)
    ax.text(x, y, t, ha='center', fontsize=8.8, color=TUA)
for x in (-1.7, 15.7): ax.plot([x, x], [-0.7, -1.05], color=JT, lw=1.4)
ax.annotate('', (15.7, -0.88), (-1.7, -0.88), arrowprops=dict(arrowstyle='<->', color=JT, lw=1.0)); ax.text(7.0, -1.3, 'rentang yang dapat diukur langsung di dalam air', ha='center', fontsize=8, color=JT)
ax.text(-11.5, -1.75, '← asam lebih kuat', fontsize=9, color=JT); ax.text(51.5, -1.75, 'asam lebih lemah →', fontsize=9, color=HJ, ha='right')
f.savefig(f'{F}/skala.png', bbox_inches='tight'); plt.close(f)

# 2. fraksi terionisasi
f, ax = plt.subplots(figsize=(5.6, 3.2), dpi=220)
pH = np.linspace(0, 14, 400)
for p, n, c in [(4.76, 'asam asetat (4,76)', BIRU), (10.0, 'fenol (10,0)', JT), (10.6, 'ion metilamonium (10,6)', HJ)]:
    ax.plot(pH, 1 / (1 + 10 ** (p - pH)), color=c, lw=2, label=n)
for x, t, ha, dx in [(1.5, 'lambung', 'left', 0.12), (7.4, 'darah', 'right', -0.12), (8.3, 'NaHCO₃', 'left', 0.12)]:
    ax.axvline(x, color='#9aa5b1', lw=0.8, ls=(0, (3, 2))); ax.text(x + dx, 1.03, t, fontsize=8, color=TUA, ha=ha)
ax.axhline(0.5, color='#c9d2db', lw=0.7)
ax.set_xlabel('pH'); ax.set_ylabel('bagian terionisasi (bentuk basa konjugat)')
ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom); ax.set_ylim(0, 1.1); ax.set_xlim(0, 14)
ax.legend(frameon=False, fontsize=7.5, loc='lower left', bbox_to_anchor=(0.0, 0.5))
f.savefig(f'{F}/fraksi.png', bbox_inches='tight'); plt.close(f)

# 3. skema ekstraksi
f, ax = plt.subplots(figsize=(7.6, 3.6), dpi=220); ax.set_xlim(0, 20); ax.set_ylim(0, 10); ax.axis('off')
def kotak(x, y, w, h, t, fc, ec=TUA):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08,rounding_size=0.25', fc=fc, ec=ec, lw=1))
    ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=8.2, color=TUA)
def panah(x1, y1, x2, y2, t=''):
    ax.annotate('', (x2, y2), (x1, y1), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1))
    if t: ax.text((x1 + x2) / 2 + 0.15, (y1 + y2) / 2, t, fontsize=7.8, color=JT, va='center')
kotak(0.2, 7.6, 4.6, 1.9, 'eter: asam benzoat,\nfenol, anilina, naftalena', '#eef4fa')
panah(2.5, 7.5, 2.5, 6.2, 'HCl')
kotak(0.2, 4.5, 4.6, 1.6, 'eter: asam benzoat,\nfenol, naftalena', '#eef4fa')
kotak(5.6, 7.6, 4.8, 1.9, 'air: ion anilinium\n→ NaOH → anilina', '#fdf1e6', JT)
panah(4.8, 7.0, 5.6, 7.9)
panah(2.5, 4.4, 2.5, 3.1, 'NaHCO₃')
kotak(0.2, 1.4, 4.6, 1.6, 'eter: fenol, naftalena', '#eef4fa')
kotak(5.6, 4.5, 4.8, 1.6, 'air: ion benzoat\n→ HCl → asam benzoat', '#fdf1e6', JT)
panah(4.8, 4.9, 5.6, 5.2)
panah(4.8, 2.6, 11.0, 4.9); ax.text(7.2, 3.05, 'NaOH', fontsize=7.8, color=JT, rotation=20); panah(4.8, 2.0, 11.0, 2.0)
kotak(11.0, 4.5, 4.2, 1.6, 'air: ion fenoksida\n→ HCl → fenol', '#fdf1e6', JT)
kotak(11.0, 1.4, 4.2, 1.6, 'eter: naftalena\n→ uapkan', '#eef4fa')
ax.text(16.5, 8.8, 'lapisan eter', color=BIRU, fontsize=8.5); ax.add_patch(FancyBboxPatch((16.0, 8.75), 0.35, 0.3, boxstyle='round,pad=0.02', fc='#eef4fa', ec=TUA, lw=0.8))
ax.text(16.5, 8.1, 'lapisan air', color=JT, fontsize=8.5); ax.add_patch(FancyBboxPatch((16.0, 8.05), 0.35, 0.3, boxstyle='round,pad=0.02', fc='#fdf1e6', ec=JT, lw=0.8))
f.savefig(f'{F}/ekstraksi.png', bbox_inches='tight'); plt.close(f)
print('ok')

# ================= gambar tambahan =================
import sys, io; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, matplotlib.ticker
from lewis import molekul, lengkung, resonansi, panah, MERAH
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D
from PIL import Image
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
koma = lambda v: f'{v:g}'.replace('.', ',').replace('-', '−')
fmt = matplotlib.ticker.FuncFormatter(lambda q, _: koma(round(q, 3)))
def kanv(w, h, xl, yl):
    f, ax = plt.subplots(figsize=(w, h), dpi=220); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect('equal'); ax.axis('off'); return f, ax
def T(ax, x, y, s, c=TUA, fs=10, **k): ax.text(x, y, s, ha=k.pop('ha', 'center'), va=k.pop('va', 'center'), color=c, fontsize=fs, **k)
def simpan(f, n): f.savefig(f'{F}/{n}.png', bbox_inches='tight'); plt.close(f)
def rd(smi, w=420, h=300, bl=45, fs=28):
    m = Chem.MolFromSmiles(smi); d = rdMolDraw2D.MolDraw2DCairo(w, h); o = d.drawOptions(); o.bondLineWidth = 3; o.fixedFontSize = fs; o.padding = 0.12; o.fixedBondLength = bl
    o.updateAtomPalette({8: (0.71, 0.33, 0.11), 7: (0.11, 0.46, 0.74), 17: (0.1, 0.54, 0.42)}); o.setBackgroundColour((1, 1, 1, 0))
    rdMolDraw2D.PrepareAndDrawMolecule(d, m); d.FinishDrawing(); return Image.open(io.BytesIO(d.GetDrawingText()))

# 4. transfer proton dengan pasangan konjugat
f, ax = kanv(7.4, 2.6, (0, 30), (0, 10))
P1 = molekul(ax, {'H': (0, 0, 'H'), 'Cl': (1.2, 0, 'Cl')}, [('H', 'Cl', 1)], lp={'Cl': [90, 0, 270]}, ox=1.2, oy=5.0, s=1.5)
P2 = molekul(ax, {'O': (0, 0, 'O'), 'a': (-0.8, -0.65, 'H'), 'b': (0.8, -0.65, 'H')}, [('O', 'a', 1), ('O', 'b', 1)], lp={'O': [60, 120]}, ox=7.8, oy=5.2, s=1.5)
lengkung(ax, P2['O'] + np.array([-0.55, 0.65]), P1['H'] + np.array([0.15, 0.35]), rad=0.45)
lengkung(ax, (P1['H'] + P1['Cl']) / 2 + np.array([0, -0.15]), P1['Cl'] + np.array([0.2, -0.55]), rad=0.6)
T(ax, 4.9, 5.3, '+', fs=14); panah(ax, (11.0, 5.2), (13.4, 5.2))
molekul(ax, {'Cl': (0, 0, 'Cl')}, [], lp={'Cl': [0, 90, 180, 270]}, muatan={'Cl': ('-', 45)}, ox=15.2, oy=5.2, s=1.5)
T(ax, 17.6, 5.3, '+', fs=14)
molekul(ax, {'O': (0, 0, 'O'), 'a': (-0.8, -0.65, 'H'), 'b': (0.8, -0.65, 'H'), 'c': (0, 1.1, 'H')}, [('O', 'a', 1), ('O', 'b', 1), ('O', 'c', 1)], lp={'O': [270]}, muatan={'O': ('+', 35)}, ox=20.5, oy=4.9, s=1.5)
for x, t, c in [(2.1, 'asam', MERAH), (7.8, 'basa', BIRU), (15.2, 'basa konjugat', BIRU), (20.5, 'asam konjugat', MERAH)]: T(ax, x, 1.6, t, fs=9, c=c, fontweight='bold')
ax.annotate('', (15.2, 0.9), (2.1, 0.9), arrowprops=dict(arrowstyle='-', color=MERAH, lw=0.8, connectionstyle='arc3,rad=0.12'))
ax.annotate('', (20.5, 9.3), (7.8, 9.3), arrowprops=dict(arrowstyle='-', color=BIRU, lw=0.8, connectionstyle='arc3,rad=-0.12'))
T(ax, 8.6, -0.3, 'pasangan konjugat', fs=8, c=MERAH); T(ax, 14.2, 10.4, 'pasangan konjugat', fs=8, c=BIRU)
T(ax, 26.5, 5.2, 'panah lengkung:\nbasa memberi\npasangan elektron\nkepada H', fs=8.3, c='#555555')
simpan(f, 'transfer')

# 5. ΔG° terhadap pKa
f, ax = plt.subplots(figsize=(5.6, 3.0), dpi=220)
pk = np.linspace(-10, 50, 100); ax.plot(pk, 2.303 * 8.314 * 298.15 * pk / 1000, color=BIRU, lw=2)
for p_, n_ in [(-7, 'HCl'), (4.76, 'CH₃COOH'), (10.0, 'fenol'), (15.7, 'H₂O'), (25, 'etuna'), (50, 'metana')]:
    g = 2.303 * 8.314 * 298.15 * p_ / 1000; ax.plot(p_, g, 'o', color=JT, ms=5); ax.text(p_ + 1.2, g - 9, n_, fontsize=8, color=TUA)
ax.axhline(0, color='#bbbbbb', lw=0.7); ax.set_xlabel('p$K$$_a$'); ax.set_ylabel('Δ$G$° ionisasi (kJ mol$^{-1}$)')
ax.xaxis.set_major_formatter(fmt); ax.yaxis.set_major_formatter(fmt); ax.text(-8, 230, 'Δ$G$° = 2,303$RT$·p$K$$_a$ = 5,71·p$K$$_a$ kJ mol$^{-1}$ (25 °C)', fontsize=8.5, color=TUA)
plt.tight_layout(); simpan(f, 'dG')

# 6. faktor atom: periode dan golongan
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.8), dpi=220)
for a, nm, v, ttl in [(a1, ['CH₄', 'NH₃', 'H₂O', 'HF'], [50, 38, 15.7, 3.2], 'dalam satu periode:\nkeelektronegatifan naik →'), (a2, ['HF', 'HCl', 'HBr', 'HI'], [3.2, -7, -9, -10], 'dalam satu golongan:\nukuran atom naik →')]:
    bars = a.bar(nm, v, color=[BIRU, HJ, JT, MERAH]); a.axhline(0, color='#999999', lw=0.7); a.set_ylabel('p$K$$_a$'); a.yaxis.set_major_formatter(fmt)
    for b, val in zip(bars, v): a.text(b.get_x() + b.get_width() / 2, val + 1.2 if val >= 0 else val / 2, koma(val), ha='center', va='bottom' if val >= 0 else 'center', fontsize=8.5, color=TUA if val >= 0 else 'white', fontweight='bold' if val < 0 else 'normal')
    a.set_title(ttl, fontsize=9, color=TUA)
a2.set_ylim(-13, 6); plt.tight_layout(); simpan(f, 'atom')

# 7. delokalisasi muatan: etoksida, fenoksida, asetat
f, ax = plt.subplots(1, 3, figsize=(7.4, 2.6), dpi=220)
dat = [('CC[O-]', 'etoksida: muatan pada satu O\npKa etanol 16'), ('[O-]c1ccccc1', 'fenoksida: muatan ke O dan\ntiga C cincin · pKa fenol 10,0'), ('CC(=O)[O-]', 'asetat: muatan terbagi rata\npada dua O · pKa 4,76')]
for a, (s, t) in zip(ax, dat): a.imshow(rd(s, w=420, h=320, bl=48)); a.axis('off'); a.set_title(t, fontsize=8.5, color=TUA, y=-0.2)
plt.tight_layout(); simpan(f, 'delokal')

# 7b. resonansi fenoksida
f, ax = plt.subplots(1, 4, figsize=(7.6, 2.2), dpi=220)
for a, s in zip(ax, ['[O-]c1ccccc1', 'O=C1C=CC=C[CH-]1', 'O=C1C=C[CH-]C=C1', 'O=C1[CH-]C=CC=C1']):
    a.imshow(rd(s, w=380, h=340, bl=42)); a.axis('off')
for k in range(3): f.text(0.25 + k * 0.245, 0.5, '↔', ha='center', va='center', fontsize=16, color=TUA, family='DejaVu Sans')
plt.tight_layout(w_pad=2.5); simpan(f, 'fenoksida')

# 8. efek induktif
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.9), dpi=220)
nm = ['CH₃', 'ClCH₂', 'Cl₂CH', 'Cl₃C', 'F₃C']; v = [4.76, 2.86, 1.29, 0.65, 0.23]
b = a1.bar(nm, v, color=[MUDA, BIRU, BIRU, TUA, HJ]); a1.set_title('X–COOH: makin banyak halogen,\nmakin asam', fontsize=9, color=TUA)
for bb, val in zip(b, v): a1.text(bb.get_x() + bb.get_width() / 2, val + 0.08, koma(val), ha='center', fontsize=8.5, color=TUA)
nm2 = ['tanpa Cl', 'Cl di C2', 'Cl di C3', 'Cl di C4']; v2 = [4.82, 2.84, 4.05, 4.52]
b = a2.bar(nm2, v2, color=[MUDA, TUA, BIRU, MUDA]); a2.set_title('asam klorobutanoat: efek melemah\ndengan jarak', fontsize=9, color=TUA)
for bb, val in zip(b, v2): a2.text(bb.get_x() + bb.get_width() / 2, val + 0.08, koma(val), ha='center', fontsize=8.5, color=TUA)
for a in (a1, a2): a.set_ylabel('p$K$$_a$'); a.yaxis.set_major_formatter(fmt); a.set_ylim(0, 5.6); a.tick_params(axis='x', labelsize=8.5)
plt.tight_layout(); simpan(f, 'induktif')

# 9. hibridisasi dan keasaman C–H
f, ax = plt.subplots(figsize=(5.6, 2.9), dpi=220)
s_ = [25, 33.3, 50]; pk_ = [50, 44, 25]; nm = ['etana (sp³)', 'etena (sp²)', 'etuna (sp)']
ax.plot(s_, pk_, 'o-', color=JT, lw=2, ms=7)
for x, y, t in zip(s_, pk_, nm): ax.text(x + 1, y + 1.5, t, fontsize=9, color=TUA)
ax.set_xlabel('karakter s orbital pasangan bebas (%)'); ax.set_ylabel('p$K$$_a$'); ax.xaxis.set_major_formatter(fmt); ax.set_xlim(20, 58); ax.set_ylim(20, 56)
plt.tight_layout(); simpan(f, 'orbital')

# 10. kebasaan amina dan heterosiklik
f, ax = plt.subplots(figsize=(6.8, 3.2), dpi=220)
nm = ['guanidina', 'dimetilamina', 'metilamina', 'amonia', 'imidazola', 'piridina', 'anilina', 'amida', 'pirola']; v = [13.6, 10.7, 10.6, 9.25, 7.0, 5.2, 4.6, -0.5, -3.8]
c = [HJ, BIRU, BIRU, BIRU, HJ, JG, JT, MERAH, MERAH]
b = ax.barh(nm[::-1], v[::-1], color=c[::-1]); ax.axvline(0, color='#999999', lw=0.7)
lbl = ['13,6', '10,7', '10,6', '9,25', '7,0', '5,2', '4,6', '−0,5', '−3,8'][::-1]
for bb, val, lb in zip(b, v[::-1], lbl): ax.text(val + (0.3 if val >= 0 else -0.3), bb.get_y() + bb.get_height() / 2, lb, va='center', ha='left' if val >= 0 else 'right', fontsize=8.5, color=TUA)
ax.set_xlabel('p$K$$_{aH}$ (makin besar, makin basa)'); ax.xaxis.set_major_formatter(fmt); ax.set_xlim(-6, 16)
plt.tight_layout(); simpan(f, 'amina')

# 11. asam dan basa Lewis
f, ax = kanv(7.4, 2.6, (0, 30), (0, 10))
A = molekul(ax, {'N': (0, 0, 'N'), 'a': (-0.6, 0.9, 'H'), 'b': (-0.6, -0.9, 'H'), 'c': (-1.15, 0, 'H')}, [('N', 'a', 1), ('N', 'b', 1), ('N', 'c', 1)], lp={'N': [0]}, ox=3.0, oy=5.2, s=1.5)
B = molekul(ax, {'B': (0, 0, 'B'), 'a': (0.6, 0.9, 'F'), 'b': (0.6, -0.9, 'F'), 'c': (1.15, 0, 'F')}, [('B', 'a', 1), ('B', 'b', 1), ('B', 'c', 1)], ox=7.6, oy=5.2, s=1.5)
lengkung(ax, A['N'] + np.array([0.55, 0.15]), B['B'] + np.array([-0.35, 0.1]), rad=-0.5)
T(ax, 2.6, 2.0, 'basa Lewis\n(memberi pasangan\nelektron)', fs=8.3, c=BIRU); T(ax, 9.0, 2.0, 'asam Lewis\n(B hanya\n6 elektron)', fs=8.3, c=MERAH)
panah(ax, (12.5, 5.2), (15.0, 5.2))
molekul(ax, {'N': (0, 0, 'N'), 'a': (-0.6, 0.9, 'H'), 'b': (-0.6, -0.9, 'H'), 'c': (-1.15, 0, 'H'), 'B': (1.5, 0, 'B'), 'd': (2.1, 0.9, 'F'), 'e': (2.1, -0.9, 'F'), 'f': (2.65, 0, 'F')},
        [('N', 'a', 1), ('N', 'b', 1), ('N', 'c', 1), ('N', 'B', 1), ('B', 'd', 1), ('B', 'e', 1), ('B', 'f', 1)], muatan={'N': ('+', 60), 'B': ('-', 120)}, ox=18.0, oy=5.2, s=1.5)
T(ax, 20.0, 2.0, 'kompleks asam–basa Lewis\n(ikatan koordinasi N→B)', fs=8.5)
T(ax, 27.5, 5.2, 'contoh asam Lewis\nlain: AlCl₃, FeBr₃,\nH$^+$, karbokation', fs=8.3, c='#555555')
simpan(f, 'lewis')
print('ok tambahan')
