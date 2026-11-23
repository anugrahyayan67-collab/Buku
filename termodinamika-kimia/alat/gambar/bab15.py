# Gambar Bab 15: termodinamika permukaan
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Circle, Rectangle, Arc, Wedge
plt.rcParams.update({'font.family': 'Liberation Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': True})
R0 = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
kom = FuncFormatter(lambda x, p: f'{x:g}'.replace('.', ',').replace('-', '−'))
def koma(ax): ax.xaxis.set_major_formatter(kom); ax.yaxis.set_major_formatter(kom)
def simpan(f, n): f.savefig(f'{R0}/bab15/fig/{n}.png', dpi=220, bbox_inches='tight'); plt.close(f)
R = 8.314; NA = 6.022e23; k = 1.381e-23

# 1. molekul di dalam cairan dan di permukaan
f, ax = plt.subplots(figsize=(5.6, 3.0)); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 5.6)
ax.add_patch(Rectangle((0.3, 0.3), 9.4, 3.9, color=MUDA, alpha=0.35, lw=0)); ax.plot([0.3, 9.7], [4.2, 4.2], color=BIRU, lw=2)
for (x, y, lab) in [(2.6, 2.0, 'di dalam'), (7.2, 3.85, 'di permukaan')]:
    ax.add_patch(Circle((x, y), 0.33, color=JT, zorder=4))
    for ang in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        xx, yy = x + 1.0 * np.cos(ang), y + 1.0 * np.sin(ang)
        if yy > 4.2: continue
        ax.add_patch(Circle((xx, yy), 0.27, color=BIRU, alpha=0.8, zorder=3)); ax.annotate('', xy=(x + 0.62 * np.cos(ang), y + 0.62 * np.sin(ang)), xytext=(x + 0.36 * np.cos(ang), y + 0.36 * np.sin(ang)), arrowprops=dict(arrowstyle='->', color=TUA, lw=1.1))
    ax.text(x, 0.55 if y < 3 else 2.25, lab, ha='center', fontsize=9, color=TUA)
ax.annotate('', xy=(7.2, 2.95), xytext=(7.2, 3.45), arrowprops=dict(arrowstyle='->', color=JT, lw=2)); ax.text(8.45, 3.0, 'tarikan bersih\nke dalam', fontsize=8.3, color=JT)
ax.text(5.0, 4.75, 'udara', ha='center', fontsize=9, color='#666666'); ax.text(1.2, 3.75, 'cairan', fontsize=9, color=BIRU)
f.tight_layout(); simpan(f, 'molekul')

# 2. tegangan permukaan: data air terhadap suhu dan beberapa cairan
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0), gridspec_kw={'width_ratios': [1.1, 1]})
t = np.array([0, 20, 25, 50, 75, 100]); gm = np.array([75.64, 72.75, 71.97, 67.94, 63.58, 58.85])
a1.plot(t, gm, 'o', color=BIRU, ms=5); p = np.polyfit(t, gm, 1); tt = np.linspace(0, 100, 50); a1.plot(tt, np.polyval(p, tt), color=BIRU, lw=1.6)
a1.set_xlabel('$t$ (°C)'); a1.set_ylabel('$\\gamma$ (mN m$^{-1}$)'); a1.set_title('air', fontsize=9); koma(a1)
a1.text(40, 73, f'kemiringan ≈ {p[0]:.3f}'.replace('.', ',') + ' mN m$^{-1}$ K$^{-1}$', fontsize=8.3, color=TUA)
nm = ['heksana', 'etanol', 'aseton', 'benzena', 'gliserol', 'air']; gv = [17.9, 22.0, 23.0, 28.2, 63.4, 72.0]
a2.barh(nm, gv, color=[MUDA, MUDA, MUDA, MUDA, HJ, BIRU]); a2.set_xlabel('$\\gamma$ pada 20–25 °C (mN m$^{-1}$)'); a2.xaxis.set_major_formatter(kom)
for i, v in enumerate(gv): a2.text(v + 1, i, f'{v:g}'.replace('.', ','), va='center', fontsize=8.3)
a2.text(28, 0.4, 'raksa: 485', fontsize=8.3, color=JT); a2.set_xlim(0, 85)
f.tight_layout(); simpan(f, 'gamma')

# 3. tekanan Laplace terhadap jari-jari
f, ax = plt.subplots(figsize=(6.0, 3.0)); r = np.logspace(-9, -2, 200)
ax.loglog(r * 1e6, 2 * 0.072 / r / 1e5, color=BIRU, lw=2.2, label='tetes air (2γ/$r$, γ = 72 mN m$^{-1}$)')
ax.loglog(r * 1e6, 4 * 0.025 / r / 1e5, color=JT, lw=2.2, ls='--', label='gelembung sabun (4γ/$r$, γ = 25 mN m$^{-1}$)')
ax.axhline(1, color='#999999', lw=0.8, ls=':'); ax.text(2e3, 1.3, '1 bar', fontsize=8.3, color='#666666')
ax.plot(1, 1.44, 'o', color=BIRU, ms=5); ax.text(1.4, 2.2, '1 µm: 1,44 bar', fontsize=8.3, color=BIRU)
ax.set_xlabel('jari-jari $r$ (µm)'); ax.set_ylabel('$\\Delta p$ (bar)'); ax.legend(frameon=False, fontsize=8.3, loc='upper right')
fm = FuncFormatter(lambda v, q: (f'{v:g}' if v >= 1e-3 and v < 1e5 else f'$10^{{{int(np.round(np.log10(v)))}}}$').replace('.', ','))
ax.xaxis.set_major_formatter(fm); ax.yaxis.set_major_formatter(fm)
f.tight_layout(); simpan(f, 'laplace')

# 4. kapilaritas dan sudut kontak
f, ax = plt.subplots(figsize=(7.0, 3.4)); ax.axis('off'); ax.set_xlim(0, 14); ax.set_ylim(0, 7)
ax.add_patch(Rectangle((0.3, 0.3), 6.2, 2.0, color=MUDA, alpha=0.5, lw=0)); ax.add_patch(Rectangle((7.5, 0.3), 6.2, 2.0, color='#b9bec6', alpha=0.8, lw=0))
for x0, h, col in [(1.5, 3.0, MUDA), (3.6, 1.7, MUDA), (9.2, -0.8, '#b9bec6'), (11.3, -0.45, '#b9bec6')]:
    w = 0.5 if x0 in (1.5, 9.2) else 0.9
    ax.add_patch(Rectangle((x0, 1.3), w, 4.6, fc='none', ec=TUA, lw=1.4))
    ax.add_patch(Rectangle((x0 + 0.03, 1.3), w - 0.06, 1.0 + h, color=col, alpha=0.8 if col != MUDA else 0.6, lw=0))
    yy = 2.3 + h; xs = np.linspace(x0 + 0.03, x0 + w - 0.03, 30); dep = (0.18 if col == MUDA else -0.15) * ((xs - x0 - w / 2) / (w / 2)) ** 2
    ax.plot(xs, yy + dep, color=BIRU if col == MUDA else TUA, lw=1.4)
ax.annotate('', xy=(0.9, 5.3), xytext=(0.9, 2.3), arrowprops=dict(arrowstyle='<->', color=JT, lw=1.2)); ax.text(0.35, 3.7, '$h$', fontsize=11, color=JT)
ax.text(3.4, 6.5, 'air dalam kaca: naik\n(θ < 90°; makin sempit, makin tinggi)', ha='center', fontsize=8.6, color=BIRU)
ax.text(10.6, 6.5, 'raksa dalam kaca: turun\n(θ ≈ 140°)', ha='center', fontsize=8.6, color=TUA)
f.tight_layout(); simpan(f, 'kapiler')

# 5. sudut kontak (persamaan Young)
f, axs = plt.subplots(1, 3, figsize=(7.2, 2.2))
for ax, th, lab in zip(axs, [30, 90, 140], ['membasahi (θ = 30°)', 'θ = 90°', 'tidak membasahi (θ = 140°)']):
    ax.axis('off'); ax.set_aspect('equal'); ax.set_xlim(-1.6, 1.6); ax.set_ylim(-0.3, 1.9); ax.plot([-1.6, 1.6], [0, 0], color=TUA, lw=2)
    thr = np.radians(th); Rr = 1 / np.sin(thr) if th != 90 else 1; yc = -Rr * np.cos(thr)
    phi = np.linspace(-np.pi / 2 - (np.pi - thr), -np.pi / 2 + (np.pi - thr), 200) if False else None
    a = np.linspace(0, 2 * np.pi, 400); xs = Rr * np.cos(a); ys = yc + Rr * np.sin(a); m = ys >= 0
    sc = 0.9 / max(1, np.max(np.abs(xs[m]))); ax.fill(xs[m] * sc, ys[m] * sc, color=MUDA, alpha=0.8); ax.plot(xs[m] * sc, ys[m] * sc, color=BIRU, lw=1.5)
    xe = np.max(xs[m]) * sc; L = 0.55; ax.plot([xe, xe - L * np.cos(thr)], [0, L * np.sin(thr)], color=JT, lw=1.4)
    ax.add_patch(Arc((xe, 0), 0.5, 0.5, theta1=180 - th, theta2=180, color=JT, lw=1.2)); ax.text(0, -0.28, lab, ha='center', fontsize=8.3, color=TUA)
f.tight_layout(); simpan(f, 'kontak')

# 6. persamaan Kelvin
f, ax = plt.subplots(figsize=(6.0, 3.0)); r = np.logspace(0, 3, 200)  # nm
c = 2 * 0.072 * 18.07e-6 / (R * 298.15)
ax.semilogx(r, np.exp(c / (r * 1e-9)), color=BIRU, lw=2.2, label='tetes (permukaan cembung)'); ax.semilogx(r, np.exp(-c / (r * 1e-9)), color=JT, lw=2.2, label='pori atau celah (cekung)')
ax.axhline(1, color='#999999', lw=0.8); ax.set_xlabel('jari-jari kelengkungan $r$ (nm)'); ax.set_ylabel('$p/p^*$'); ax.set_ylim(0, 3.0); ax.legend(frameon=False, fontsize=8.5)
ax.plot(10, 1.111, 'o', color=BIRU, ms=4.5); ax.text(11.5, 1.2, '10 nm: 1,11', fontsize=8.3, color=BIRU); ax.plot(2, 0.592, 'o', color=JT, ms=4.5); ax.text(2.3, 0.45, '2 nm: 0,59', fontsize=8.3, color=JT)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, q: f'{v:g}')); ax.yaxis.set_major_formatter(kom)
f.tight_layout(); simpan(f, 'kelvin')

# 7. nukleasi homogen: ΔG(r) untuk uap air jenuh-lewat
f, ax = plt.subplots(figsize=(6.0, 3.1)); T = 293.15; g = 0.0728; Vm = 18.07e-6; r = np.linspace(0.01e-9, 2.5e-9, 400)
for S, col in [(2, MUDA), (4, BIRU), (8, JT)]:
    dgv = R * T * np.log(S) / Vm; G = (-4 / 3 * np.pi * r ** 3 * dgv + 4 * np.pi * r ** 2 * g) / (k * T)
    ax.plot(r * 1e9, G, color=col, lw=2.2, label=f'$S$ = {S}'); rs = 2 * g / dgv; Gs = 16 * np.pi * g ** 3 / (3 * dgv ** 2) / (k * T)
    if rs < 2.5e-9: ax.plot(rs * 1e9, Gs, 'o', color=col, ms=5); ax.text(rs * 1e9 + 0.04, Gs + 6, f'{Gs:.0f} $kT$', fontsize=8.3, color=col)
ax.axhline(0, color='#999999', lw=0.8); ax.set_xlabel('jari-jari inti $r$ (nm)'); ax.set_ylabel('$\\Delta G(r)/kT$'); ax.set_ylim(-60, 220); ax.legend(frameon=False, fontsize=8.5, loc='upper right'); koma(ax)
ax.text(0.08, -45, 'titik: inti kritis $r^*$ dan penghalang $\\Delta G^*$', fontsize=8.3, color=TUA)
f.tight_layout(); simpan(f, 'nukleasi')

# 8. tegangan permukaan larutan surfaktan dan CMC
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0), gridspec_kw={'width_ratios': [1.3, 1]})
lc = np.linspace(-5, -1, 300); cmc = np.log10(8.2e-3); gm = np.where(lc < cmc, 72.0 - 13.0e-3 * 1000 * np.log(1 + 10 ** (lc - (-4.2))) / 2.0 * 0 + 0, 0)
x = 10 ** lc; gam = 72.0 - 1000 * 2 * R * 298.15 * 2.62e-6 * np.log(1 + x / 6.0e-4)
gc = 72.0 - 1000 * 2 * R * 298.15 * 2.62e-6 * np.log(1 + 8.2e-3 / 6.0e-4); gam = np.where(lc < cmc, gam, gc)
a1.plot(lc, gam, color=BIRU, lw=2.2); a1.axvline(cmc, color=JT, lw=1, ls=':'); a1.text(cmc + 0.05, 55, 'CMC\n8,2 mmol L$^{-1}$', fontsize=8.3, color=JT)
a1.set_xlabel('log ($c$ / mol L$^{-1}$)'); a1.set_ylabel('$\\gamma$ (mN m$^{-1}$)'); a1.set_title('SDS dalam air, 25 °C (model)', fontsize=9); koma(a1)
a2.axis('off'); a2.set_xlim(-1.6, 1.6); a2.set_ylim(-1.6, 1.6)
for ang in np.linspace(0, 2 * np.pi, 16, endpoint=False):
    a2.plot([0.35 * np.cos(ang), 1.05 * np.cos(ang)], [0.35 * np.sin(ang), 1.05 * np.sin(ang)], color=TUA, lw=1.4)
    a2.add_patch(Circle((1.17 * np.cos(ang), 1.17 * np.sin(ang)), 0.13, color=JT))
a2.text(0, -1.55, 'misel: ekor hidrokarbon di dalam,\nkepala ionik menghadap air', ha='center', fontsize=8.0, color=TUA)
f.tight_layout(); simpan(f, 'misel')

# 9. isoterm Langmuir dan BET
f, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.0)); p = np.linspace(0, 40, 300)
for K, col in [(0.05, MUDA), (0.20, BIRU), (1.0, JT)]: a1.plot(p, K * p / (1 + K * p), color=col, lw=2.2, label=f'$K$ = {K:g} kPa$^{{-1}}$'.replace('.', ','))
ps = np.array([1, 2, 5, 10, 20, 40]); a1.plot(ps, np.array([0.417, 0.714, 1.25, 1.667, 2.0, 2.222]) / 2.5, 'o', color=BIRU, ms=4)
a1.set_xlabel('$p$ (kPa)'); a1.set_ylabel('$\\theta$'); a1.set_ylim(0, 1.05); a1.legend(frameon=False, fontsize=8.0, loc='lower right'); a1.set_title('Langmuir: satu lapisan', fontsize=9); koma(a1)
x = np.linspace(0.001, 0.8, 300); c = 100
a2.plot(x, c * x / ((1 - x) * (1 - x + c * x)), color=JT, lw=2.2, label='BET, $c$ = 100'); a2.axhline(1, color='#999999', lw=0.8, ls=':'); a2.text(0.42, 0.55, 'satu lapisan penuh', fontsize=8.0, color='#666666')
xd = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30]); a2.plot(xd, np.array([35.4, 40.8, 44.5, 48.1, 51.8, 55.8]) / 40, 'o', color=JT, ms=4)
a2.set_xlabel('$p/p^*$'); a2.set_ylabel('$V/V_\\mathrm{mono}$'); a2.set_ylim(0, 5); a2.legend(frameon=False, fontsize=8.3, loc='upper left'); a2.set_title('BET: banyak lapisan', fontsize=9); koma(a2)
f.tight_layout(); simpan(f, 'isoterm')
print('ok bab15')
