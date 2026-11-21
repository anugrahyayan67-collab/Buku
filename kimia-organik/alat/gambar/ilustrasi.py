# Alat ilustrasi 3D berbayang: cuping orbital, bola-batang, sumbu xyz (matplotlib mplot3d)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource, to_rgb
EMAS, JINGGA, BIRU3, MERAH3, HIJAU3, ABU = '#f6b73c', '#e8893a', '#5b8fd6', '#e0707a', '#4fb38a', '#9aa5b1'
CPK = {'C': '#3a3f47', 'H': '#f2f2f2', 'O': '#d9483b', 'N': '#3d6fd1', 'Cl': '#3fb36b', 'F': '#8fd16a', 'Br': '#a2482a', 'S': '#e6c229'}
RAD = {'C': 0.36, 'H': 0.24, 'O': 0.34, 'N': 0.34, 'Cl': 0.44, 'F': 0.30, 'Br': 0.48, 'S': 0.44}
LS = LightSource(azdeg=315, altdeg=40)

def ax3d(fig, rect, lim=1.6, elev=18, azim=-60):
    ax = fig.add_axes(rect, projection='3d'); ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=elev, azim=azim); ax.set_axis_off(); return ax

def sumbu(ax, L=1.5, lab=True, c='#4a5560', lw=0.8, fs=9):
    for v, t in [((1, 0, 0), 'x'), ((0, 1, 0), 'y'), ((0, 0, 1), 'z')]:
        v = np.array(v) * L; ax.plot([-v[0], v[0]], [-v[1], v[1]], [-v[2], v[2]], color=c, lw=lw, zorder=1)
        ax.quiver(v[0] * 0.92, v[1] * 0.92, v[2] * 0.92, v[0] * 0.08, v[1] * 0.08, v[2] * 0.08, color=c, lw=lw, arrow_length_ratio=1.0)
        if lab: ax.text(v[0] * 1.1, v[1] * 1.1, v[2] * 1.1, t, fontsize=fs, color=c, style='italic', ha='center', va='center')

def _rot(d):
    d = np.array(d, float); d /= np.linalg.norm(d); z = np.array([0, 0, 1.0])
    v = np.cross(z, d); s = np.linalg.norm(v); c = np.dot(z, d)
    if s < 1e-9: return np.eye(3) if c > 0 else np.diag([1, -1, -1])
    vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]]); return np.eye(3) + vx + vx @ vx * ((1 - c) / s ** 2)

def permukaan(ax, X, Y, Z, warna, alpha=1.0):
    rgb = np.array(to_rgb(warna)); n = X.shape
    # normal kira-kira untuk shading
    shade = LS.shade_normals(_normal(X, Y, Z), fraction=0.9) if True else None
    fc = np.clip(rgb[None, None, :] * (0.45 + 0.75 * shade[..., None]), 0, 1)
    fc = np.concatenate([fc, np.full(n + (1,), alpha)], axis=-1)
    ax.plot_surface(X, Y, Z, facecolors=fc, rstride=1, cstride=1, linewidth=0, edgecolor='none', antialiased=False, shade=False)

def _normal(X, Y, Z):
    dx1 = np.gradient(X, axis=0); dy1 = np.gradient(Y, axis=0); dz1 = np.gradient(Z, axis=0)
    dx2 = np.gradient(X, axis=1); dy2 = np.gradient(Y, axis=1); dz2 = np.gradient(Z, axis=1)
    N = np.stack([dy1 * dz2 - dz1 * dy2, dz1 * dx2 - dx1 * dz2, dx1 * dy2 - dy1 * dx2], -1)
    N /= np.linalg.norm(N, axis=-1, keepdims=True) + 1e-12
    return N

def tetes(ax, arah, L=1.0, w=0.36, warna=EMAS, pusat=(0, 0, 0), n=48, m=40, alpha=1.0, pangkal=0.0, bentuk=0.7):
    """Cuping berbentuk tetes: sumbu sepanjang 'arah', panjang L, lebar maksimum w."""
    d = np.array(arah, float); d /= np.linalg.norm(d)
    t = np.linspace(0, 1, m); ph = np.linspace(0, 2 * np.pi, n); Tt, P = np.meshgrid(t, ph)
    rho = w * 1.45 * Tt ** bentuk * np.sqrt(np.clip(1 - Tt ** 2, 0, None))
    X, Y, Z = rho * np.cos(P), rho * np.sin(P), pangkal + Tt * L
    pts = np.stack([X, Y, Z], -1) @ _rot(d).T
    permukaan(ax, pts[..., 0] + pusat[0], pts[..., 1] + pusat[1], pts[..., 2] + pusat[2], warna, alpha)

def orbital_p(ax, arah, skala=1.0, pusat=(0, 0, 0), w1=BIRU3, w2=MERAH3, alpha=1.0):
    tetes(ax, arah, 0.95 * skala, 0.36 * skala, w1, pusat, alpha=alpha); tetes(ax, -np.array(arah, float), 0.95 * skala, 0.36 * skala, w2, pusat, alpha=alpha)

def orbital_s(ax, r=0.6, pusat=(0, 0, 0), w=BIRU3):
    u = np.linspace(0, 2 * np.pi, 48); v = np.linspace(0, np.pi, 32); U, V = np.meshgrid(u, v)
    permukaan(ax, pusat[0] + r * np.cos(U) * np.sin(V), pusat[1] + r * np.sin(U) * np.sin(V), pusat[2] + r * np.cos(V), w)

def orbital_hibrid(ax, arah, frac_s=0.25, skala=1.0, pusat=(0, 0, 0), w=EMAS, w_kecil=JINGGA, alpha=1.0):
    tetes(ax, arah, 1.1 * skala, 0.42 * skala, w, pusat, alpha=alpha, bentuk=0.75)
    tetes(ax, -np.array(arah, float), 0.3 * skala, 0.16 * skala, w_kecil, pusat, alpha=alpha, bentuk=0.6)

def bola(ax, p, el, s=1.0):
    u = np.linspace(0, 2 * np.pi, 28); v = np.linspace(0, np.pi, 18); U, V = np.meshgrid(u, v); r = RAD[el] * s
    permukaan(ax, p[0] + r * np.cos(U) * np.sin(V), p[1] + r * np.sin(U) * np.sin(V), p[2] + r * np.cos(V), CPK[el])

def batang(ax, p, q, r=0.07, w='#9aa0a8', n=14):
    p, q = np.array(p, float), np.array(q, float); d = q - p; L = np.linalg.norm(d)
    t = np.linspace(0, 1, 2); a = np.linspace(0, 2 * np.pi, n); A, Tt = np.meshgrid(a, t)
    X, Y, Z = r * np.cos(A), r * np.sin(A), Tt * L; pts = np.stack([X, Y, Z], -1) @ _rot(d).T
    permukaan(ax, pts[..., 0] + p[0], pts[..., 1] + p[1], pts[..., 2] + p[2], w)

def molekul3d(ax, atom, ikatan, s=1.0):
    """atom: list (el, (x,y,z)); ikatan: list (i, j). Digambar dari belakang ke depan menurut kedalaman pandang."""
    for i, j in ikatan: batang(ax, atom[i][1], atom[j][1])
    for el, p in atom: bola(ax, p, el, s)
