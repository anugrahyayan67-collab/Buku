# Alat bantu menggambar struktur Lewis, panah lengkung, dan struktur resonansi dengan matplotlib
import re, numpy as np
from matplotlib.patches import FancyArrowPatch, Circle
TUA, BIRU, MUDA, JG, JT, HJ = '#0e2748', '#1b75bc', '#7fc0f0', '#f0a060', '#b5541c', '#1a8a6a'
MERAH = '#c0392b'
WARNA = {'O': JT, 'N': BIRU, 'Cl': HJ, 'F': HJ, 'Br': '#8b3a1a', 'I': '#6a3d9a', 'S': '#b8860b', 'H': TUA, 'C': TUA}

def molekul(ax, atom, ikatan, lp=None, muatan=None, ox=0.0, oy=0.0, s=1.0, fs=12, lw=1.25, gap=0.24, warna=None, z=3):
    """atom: {nama: (x, y, label)}; label '' = titik sudut karbon tanpa huruf.
    ikatan: [(a, b, orde)] orde 1, 2, 3, 'w' (baji), 'h' (garis putus), 'p' (ikatan parsial putus-putus).
    lp: {nama: [sudut, ...]} pasangan bebas; muatan: {nama: (teks, sudut)}."""
    P = {k: np.array([ox + s * v[0], oy + s * v[1]]) for k, v in atom.items()}
    lab = {k: v[2] for k, v in atom.items()}
    for a, b, o in ikatan:
        p, q = P[a], P[b]; d = q - p; L = np.hypot(*d); u = d / L; n = np.array([-u[1], u[0]])
        g1 = gap * s * (1 + 0.8 * (len(lab[a]) - 1) * abs(u[0])) if lab[a] else 0.0; g2 = gap * s * (1 + 0.8 * (len(lab[b]) - 1) * abs(u[0])) if lab[b] else 0.0
        p1, q1 = p + u * g1, q - u * g2
        if o == 'w':
            w = 0.09 * s; ax.fill([p1[0], q1[0] + n[0] * w, q1[0] - n[0] * w], [p1[1], q1[1] + n[1] * w, q1[1] - n[1] * w], color=TUA, zorder=z)
        elif o == 'h':
            for t in np.linspace(0.1, 1, 6):
                c = p1 + (q1 - p1) * t; w = 0.09 * s * t; ax.plot([c[0] - n[0] * w, c[0] + n[0] * w], [c[1] - n[1] * w, c[1] + n[1] * w], color=TUA, lw=1.1, zorder=z)
        elif o == 'p':
            ax.plot([p1[0], q1[0]], [p1[1], q1[1]], color=TUA, lw=lw, ls=(0, (2, 2)), zorder=z)
        else:
            offs = {1: [0], 2: [-0.055, 0.055], 3: [-0.09, 0, 0.09]}[o]
            for f in offs:
                ax.plot([p1[0] + n[0] * f * s, q1[0] + n[0] * f * s], [p1[1] + n[1] * f * s, q1[1] + n[1] * f * s], color=TUA, lw=lw, zorder=z, solid_capstyle='round')
    for k, (x, y) in P.items():
        if lab[k]:
            m = re.match(r'[A-Z][a-z]?', lab[k]); el = m.group() if m else 'C'
            c = (warna or {}).get(k, WARNA.get(el, TUA))
            ax.text(x, y, lab[k], ha='center', va='center', fontsize=fs * s ** 0.3, color=c, fontweight='bold', zorder=z + 1)
    for k, angs in (lp or {}).items():
        for a in angs:
            u = np.array([np.cos(np.radians(a)), np.sin(np.radians(a))]); n = np.array([-u[1], u[0]]); c = P[k] + u * 0.32 * s
            for f in (-0.07, 0.07): ax.add_patch(Circle(c + n * f * s, 0.028 * s, color=TUA, zorder=z + 1))
    for k, (t, a) in (muatan or {}).items():
        u = np.array([np.cos(np.radians(a)), np.sin(np.radians(a))]); c = P[k] + u * 0.42 * s
        ax.add_patch(Circle(c, 0.11 * s, fc='white', ec=MERAH if t == '+' else BIRU, lw=1.0, zorder=z + 1))
        ax.text(c[0], c[1] - 0.005, '+' if t == '+' else '−', ha='center', va='center', fontsize=9 * s ** 0.3, color=MERAH if t == '+' else BIRU, fontweight='bold', zorder=z + 2)
    return P

def lengkung(ax, p, q, rad=0.4, c=MERAH, lw=1.3, ms=10, z=6):
    ax.add_patch(FancyArrowPatch(p, q, connectionstyle=f'arc3,rad={rad}', arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw, zorder=z))

def resonansi(ax, x, y, w=0.9, c=TUA):
    ax.add_patch(FancyArrowPatch((x - w / 2, y), (x + w / 2, y), arrowstyle='<|-|>', mutation_scale=10, color=c, lw=1.3))

def panah(ax, a, b, c=TUA, lw=1.4, ms=11):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=ms, color=c, lw=lw))

def tengah(P, a, b, f=0.5):
    return P[a] + (P[b] - P[a]) * f
