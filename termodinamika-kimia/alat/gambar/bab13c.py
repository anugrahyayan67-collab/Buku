# Gambar tambahan Bab 13: tangga potensial, kurva pengosongan, titrasi redoks, pH meter
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R0 = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def simpan(f, n): f.savefig(f'{R0}/bab13/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
S = 0.05916

# 1. tangga potensial standar
data = [('Li$^+$/Li', -3.040), ('Na$^+$/Na', -2.714), ('Zn$^{2+}$/Zn', -0.762), ('Fe$^{2+}$/Fe', -0.447), ('PbSO$_4$/Pb', -0.359), ('H$^+$/H$_2$', 0.0),
        ('AgCl/Ag', 0.222), ('Cu$^{2+}$/Cu', 0.340), ('Fe$^{3+}$/Fe$^{2+}$', 0.771), ('Ag$^+$/Ag', 0.800), ('O$_2$/H$_2$O', 1.229), ('Cl$_2$/Cl$^-$', 1.358),
        ('MnO$_4^-$/Mn$^{2+}$', 1.507), ('PbO$_2$/PbSO$_4$', 1.691)]
f, ax = plt.subplots(figsize=(6.4, 4.6)); ax.set_xlim(-1.2, 10); ax.set_ylim(-3.3, 2.0)
for i, (t, e) in enumerate(data):
    ax.plot([3.6, 4.6], [e, e], color=TUA, lw=1.6)
    side = i % 2; x = 4.75 if side == 0 else 3.45; ha = 'left' if side == 0 else 'right'
    ax.text(x, e, f'{t}  {e:+.3f}'.replace('.', ',').replace('-', '−') if side == 0 else f'{e:+.3f}  {t}'.replace('.', ',').replace('-', '−'), va='center', ha=ha, fontsize=7.8, color=TUA)
ax.annotate('', xy=(8.6, 1.8), xytext=(8.6, -3.1), arrowprops=dict(arrowstyle='->', color=JT, lw=1.8)); ax.text(8.8, -0.6, 'bentuk teroksidasi\nmakin kuat\nsebagai pengoksidasi', fontsize=8.3, color=JT, va='center')
ax.annotate('', xy=(0.9, -3.1), xytext=(0.9, 1.8), arrowprops=dict(arrowstyle='->', color=BIRU, lw=1.8)); ax.text(-1.2, -1.6, 'bentuk tereduksi\nmakin kuat\nsebagai\npereduksi', fontsize=8.3, color=BIRU, va='center')
ax.annotate('', xy=(6.9, 0.340), xytext=(6.9, -0.762), arrowprops=dict(arrowstyle='<->', color=HJ, lw=1.4)); ax.text(7.0, -0.21, 'sel Daniell\n1,102 V', fontsize=8.3, color=HJ, va='center')
ax.plot([6.3, 6.9], [0.34, 0.34], color=HJ, lw=0.6, ls=':'); ax.plot([6.3, 6.9], [-0.762, -0.762], color=HJ, lw=0.6, ls=':')
ax.spines[['left', 'bottom']].set_visible(False); ax.set_xticks([]); ax.set_yticks([])
ax.text(4.1, 1.93, '$E^\\circ$ (V) pada 25 °C', ha='center', fontsize=9, color=TUA)
f.tight_layout(); simpan(f, 'tangga')

# 2. kurva pengosongan sel Daniell (awal 1 mol/L masing-masing)
f, ax = plt.subplots(figsize=(6.0, 3.0)); x = np.linspace(0, 1 - 1e-9, 4000)
E = 1.102 - S / 2 * np.log10((1 + x) / (1 - x)); ax.plot(x * 100, E, color=BIRU, lw=2.2)
for xx in [0.5, 0.9, 0.99]:
    e = 1.102 - S / 2 * np.log10((1 + xx) / (1 - xx)); ax.plot(xx * 100, e, 'o', color=JT, ms=4.5); ax.text(xx * 100 - 2, e - (0.13 if xx > 0.95 else 0.07), f'{e:.3f} V'.replace('.', ','), fontsize=8.2, color=JT, ha='right')
ax.set_xlabel('Cu$^{2+}$ yang sudah bereaksi (%)'); ax.set_ylabel('$E$ (V)'); ax.set_xlim(0, 100); ax.set_ylim(0.6, 1.2); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
ax.text(5, 0.7, 'awal: [Zn$^{2+}$] = [Cu$^{2+}$] = 1 mol L$^{-1}$', fontsize=8.3, color='#555555')
f.tight_layout(); simpan(f, 'pengosongan')

# 3. kurva titrasi Fe2+ dengan Ce4+
f, ax = plt.subplots(figsize=(6.0, 3.1))
f1 = np.linspace(0.005, 0.9999, 600); f2 = np.linspace(1.0001, 2.0, 600)
ax.plot(f1 * 100, 0.771 + S * np.log10(f1 / (1 - f1)), color=BIRU, lw=2.2); ax.plot(f2 * 100, 1.61 + S * np.log10(f2 - 1), color=BIRU, lw=2.2)
ax.plot([99.99, 100.01], [0.771 + S * 4, 1.61 - S * 4], color=BIRU, lw=2.2)
ax.plot(100, (0.771 + 1.61) / 2, 'o', color=JT, ms=5); ax.text(103, 1.17, 'titik ekivalen\n1,19 V', fontsize=8.3, color=JT, va='center')
ax.axhline(0.771, color='#bbbbbb', lw=0.8, ls=':'); ax.axhline(1.61, color='#bbbbbb', lw=0.8, ls=':')
ax.text(150, 0.80, '$E^\\circ$(Fe$^{3+}$/Fe$^{2+}$) = 0,771 V', fontsize=8.2, color='#666666'); ax.text(5, 1.64, '$E^\\circ$(Ce$^{4+}$/Ce$^{3+}$) = 1,61 V', fontsize=8.2, color='#666666')
ax.set_xlabel('Ce$^{4+}$ ditambahkan (% dari ekivalen)'); ax.set_ylabel('$E$ terhadap SHE (V)'); ax.set_xlim(0, 200); ax.set_ylim(0.5, 1.75); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'titrasi')

# 4. garis kalibrasi pH meter pada 25 dan 40 °C
f, ax = plt.subplots(figsize=(6.0, 3.0)); pH = np.linspace(0, 14, 50)
for T, col, lab in [(298.15, BIRU, '25 °C: 59,16 mV per satuan pH'), (313.15, JT, '40 °C: 62,13 mV per satuan pH')]:
    s = 8.314462618 * T * np.log(10) / 96485.33; ax.plot(pH, 0.412 - s * (pH - 7), color=col, lw=2, label=lab)
ax.plot(7, 0.412, 'o', color=TUA, ms=5); ax.plot(4.01, 0.589, 's', color=HJ, ms=5); ax.annotate('sampel Contoh 13.15:\n0,5890 V → pH 4,01', xy=(4.01, 0.589), xytext=(5.6, 0.75), fontsize=8.2, color=HJ, arrowprops=dict(arrowstyle='->', color=HJ, lw=0.8))
ax.set_xlabel('pH'); ax.set_ylabel('$E$ sel (V)'); ax.set_xlim(0, 14); ax.legend(frameon=False, fontsize=8.3, loc='lower left'); ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'phmeter')
print('ok bab13c')
