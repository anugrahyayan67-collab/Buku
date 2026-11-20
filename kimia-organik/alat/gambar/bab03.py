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
ax.set_xlim(-12, 52); ax.set_ylim(-1.6, 3.2); ax.axis('off')
ax.annotate('', (52, 0), (-12, 0), arrowprops=dict(arrowstyle='-|>', color=TUA, lw=1.4))
for x in range(-10, 51, 10):
    ax.plot([x, x], [-0.12, 0.12], color=TUA, lw=1); ax.text(x, -0.45, f'{x}'.replace('-', '−'), ha='center', fontsize=8.5, color=TUA)
ax.text(52, 0.3, 'pKa', ha='right', fontsize=9, color=TUA, style='italic')
dat = [(-7, 'HCl', 1), (-1.7, 'H₃O$^+$', 2), (4.8, 'RCOOH', 1), (9.3, 'R–NH₃$^+$', 2.1), (10, 'ArOH', 1), (15.7, 'H₂O', 2), (16, 'ROH', 1.1), (19, 'R₂C=O (α-H)', 2.6), (25, 'RC≡CH', 1), (38, 'NH₃', 1.6), (44, 'CH₂=CH₂', 2.4), (50, 'CH₄', 1)]
for x, t, y in dat:
    ax.plot([x, x], [0.15, y - 0.15], color='#9aa5b1', lw=0.8); ax.plot(x, 0, 'o', color=BIRU, ms=4, zorder=3)
    ax.text(x, y, t, ha='center', fontsize=8.8, color=TUA)
for x in (-1.7, 15.7): ax.plot([x, x], [-0.7, -1.05], color=JT, lw=1.6, ls=(0, (2, 1.5)))
ax.text(-11.5, -1.5, '← asam lebih kuat', fontsize=9, color=JT); ax.text(51.5, -1.5, 'asam lebih lemah →', fontsize=9, color=HJ, ha='right')
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
panah(4.8, 2.2, 11.0, 2.2); ax.text(7.4, 2.45, 'NaOH', fontsize=7.8, color=JT)
kotak(11.0, 4.5, 4.2, 1.6, 'air: ion fenoksida\n→ HCl → fenol', '#fdf1e6', JT)
kotak(11.0, 1.4, 4.2, 1.6, 'eter: naftalena\n→ uapkan', '#eef4fa')
panah(13.1, 3.1, 13.1, 4.4)
ax.text(16.5, 8.8, 'lapisan eter', color=BIRU, fontsize=8.5); ax.add_patch(FancyBboxPatch((16.0, 8.75), 0.35, 0.3, boxstyle='round,pad=0.02', fc='#eef4fa', ec=TUA, lw=0.8))
ax.text(16.5, 8.1, 'lapisan air', color=JT, fontsize=8.5); ax.add_patch(FancyBboxPatch((16.0, 8.05), 0.35, 0.3, boxstyle='round,pad=0.02', fc='#fdf1e6', ec=JT, lw=0.8))
f.savefig(f'{F}/ekstraksi.png', bbox_inches='tight'); plt.close(f)
print('ok')
