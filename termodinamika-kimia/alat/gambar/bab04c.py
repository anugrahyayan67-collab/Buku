import os, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10})
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, JT, HJ = '#0e2748', '#1b75bc', '#b5541c', '#1a8a6a'
f, ax = plt.subplots(figsize=(6.4, 3.8)); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(-880, 120)
def lv(x0, x1, y, t, c=TUA, atas=True): ax.plot([x0, x1], [y, y], color=c, lw=2.2); ax.text((x0 + x1) / 2, y + (14 if atas else -18), t, ha='center', va='bottom' if atas else 'top', fontsize=9, color=c)
def ar(x, y0, y1, t, c, dx=0.12): ax.add_patch(FancyArrowPatch((x, y0), (x, y1), arrowstyle='-|>', mutation_scale=12, color=c, lw=1.8)); ax.text(x + dx, (y0 + y1) / 2, t, fontsize=8.8, color=c, va='center')
lv(2.5, 7.5, 0, 'Na$^+$(g) + Cl$^-$(g)')
lv(0.5, 3.6, -787.4, 'NaCl(s)', atas=False); lv(6.0, 9.4, -783.5, 'Na$^+$(aq) + Cl$^-$(aq)', c=HJ, atas=False)
ar(2.8, -787.4, 0, 'entalpi kisi\n+787,4', JT); ar(7.0, 0, -783.5, 'hidrasi kedua ion\n−783,5', BIRU)
ax.add_patch(FancyArrowPatch((3.6, -800), (6.0, -800), arrowstyle='-|>', mutation_scale=12, color=HJ, lw=1.8)); ax.text(4.8, -812, 'pelarutan +3,9', ha='center', va='top', fontsize=9, color=HJ, fontweight='bold')
ax.text(0.0, 100, 'kJ mol$^{-1}$, 25 °C', fontsize=8.5, color='#666666')
f.savefig(f'{R}/bab04/fig/pelarutan.png', dpi=220, bbox_inches='tight'); plt.close(f); print('ok')
