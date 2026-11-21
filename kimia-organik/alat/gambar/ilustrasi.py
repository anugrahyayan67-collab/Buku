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

# ---------- penggambar bola-batang 2D dengan urutan kedalaman (tanpa cacat tumpang-tindih) ----------
from matplotlib.patches import Circle as _Circle, Polygon as _Poly, PathPatch as _PathPatch
from matplotlib.path import Path as _Path
def _gelap(c, f): c = np.array(to_rgb(c)); return tuple(np.clip(c * f, 0, 1))
def _terang(c, f): c = np.array(to_rgb(c)); return tuple(np.clip(c + (1 - c) * f, 0, 1))
_GRAD = None
def _gradien_bola():
    global _GRAD
    if _GRAD is None:
        n = 160; y, x = np.mgrid[-1:1:n * 1j, -1:1:n * 1j]
        d = np.sqrt((x + 0.35) ** 2 + (y - 0.35) ** 2)        # sorot di kiri atas
        _GRAD = np.clip(1 - d / 1.6, 0, 1)
    return _GRAD
def matriks_pandang(elev=15, azim=-60):
    e, a = np.radians(elev), np.radians(azim)
    Rz = np.array([[np.cos(a), np.sin(a), 0], [-np.sin(a), np.cos(a), 0], [0, 0, 1]])
    Rx = np.array([[1, 0, 0], [0, np.cos(e), np.sin(e)], [0, -np.sin(e), np.cos(e)]])
    # setelah rotasi: sumbu x layar, y kedalaman (positif menjauh), z layar atas
    return Rx @ Rz
def bola2d(ax, x, y, r, warna, z=0):
    c = _Circle((x, y), r, transform=ax.transData)
    rgb = np.array(to_rgb(warna)); g = _gradien_bola()[..., None]
    img = np.clip(rgb * (0.55 + 0.6 * g) + (1 - rgb) * np.clip(g - 0.75, 0, 1) * 1.6, 0, 1)
    im = ax.imshow(img, extent=[x - r, x + r, y - r, y + r], origin='lower', zorder=z, interpolation='bilinear')
    im.set_clip_path(c); ax.add_patch(_Circle((x, y), r, fc='none', ec=_gelap(warna, 0.55), lw=0.6, zorder=z + 0.01))
def batang2d(ax, p, q, w, warna='#a7adb5', z=0):
    p, q = np.array(p), np.array(q); d = q - p; L = np.hypot(*d)
    if L < 1e-6: return
    n = np.array([-d[1], d[0]]) / L * w / 2
    ax.add_patch(_Poly([p + n, q + n, q - n, p - n], closed=True, fc=_gelap(warna, 0.85), ec=_gelap(warna, 0.55), lw=0.5, zorder=z))
    ax.add_patch(_Poly([p + n * 0.75, q + n * 0.75, q - n * 0.05, p - n * 0.05], closed=True, fc=warna, ec='none', zorder=z + 0.01))
    ax.add_patch(_Poly([p + n * 0.55, q + n * 0.55, q + n * 0.25, p + n * 0.25], closed=True, fc=_terang(warna, 0.55), ec='none', zorder=z + 0.02))
def cuping2d(ax, p, arah2, L, w, warna, z=0, alpha=0.85):
    """Cuping tetes 2D dari titik p ke arah arah2 (vektor 2D, panjang terproyeksi L)."""
    d = np.array(arah2, float); n_ = np.hypot(*d)
    if n_ < 1e-6: d = np.array([0, 1.0]); n_ = 1
    d /= n_; nn = np.array([-d[1], d[0]]); t = np.linspace(0, 1, 50)
    rho = w * 1.45 * t ** 0.7 * np.sqrt(np.clip(1 - t ** 2, 0, None))
    kiri = [p + d * L * ti + nn * ri for ti, ri in zip(t, rho)]; kanan = [p + d * L * ti - nn * ri for ti, ri in zip(t[::-1], rho[::-1])]
    poly = _Poly(kiri + kanan, closed=True, transform=ax.transData)
    rgb = np.array(to_rgb(warna)); xs = np.array(kiri + kanan); x0, x1, y0, y1 = xs[:, 0].min(), xs[:, 0].max(), xs[:, 1].min(), xs[:, 1].max()
    gy, gx = np.mgrid[0:1:80j, 0:1:80j]; cx, cy = (p + d * L * 0.65 - [x0, y0]) / [max(x1 - x0, 1e-6), max(y1 - y0, 1e-6)]
    g = np.clip(1 - np.sqrt((gx - cx + 0.15) ** 2 + (gy - cy - 0.15) ** 2) / 0.9, 0, 1)[..., None]
    img = np.concatenate([np.clip(rgb * (0.6 + 0.55 * g), 0, 1), np.full(g.shape, alpha)], -1)
    im = ax.imshow(img, extent=[x0, x1, y0, y1], origin='lower', zorder=z, interpolation='bilinear'); im.set_clip_path(poly)
    ax.add_patch(_Poly(kiri + kanan, closed=True, fc='none', ec=_gelap(warna, 0.6), lw=0.5, zorder=z + 0.01))
def bolabatang(ax, atom, ikatan, elev=15, azim=-60, skala=1.0, pusat=(0, 0), cuping=(), w_batang=0.14, ganda=()):
    """atom: [(el, xyz)], ikatan: [(i, j)], cuping: [(i_atom, arah_xyz, warna)]. Mengembalikan koordinat 2D."""
    M = matriks_pandang(elev, azim); P3 = np.array([p for _, p in atom], float) @ M.T
    xy = P3[:, [0, 2]] * skala + np.array(pusat); dep = P3[:, 1]
    obj = []
    for i, j in ikatan:
        for a, b in [(i, j), (j, i)]:
            mid = (xy[a] + xy[b]) / 2; obj.append((-(dep[a] + 0.02), 'b', (xy[a], mid)))
    for k, (el, _) in enumerate(atom): obj.append((-dep[k], 'a', k))
    for i, v, c in cuping:
        v3 = np.array(v, float) @ M.T; v2 = v3[[0, 2]]; L = 0.95 * skala * max(np.hypot(*v2) / (np.linalg.norm(v3) + 1e-9), 0.35)
        obj.append((-(dep[i] + 0.6 * v3[1] / (np.linalg.norm(v3) + 1e-9)), 'c', (xy[i], v2, L, c)))
    obj.sort(key=lambda o: o[0])
    for z, (dz, jenis, data) in enumerate(obj):
        if jenis == 'b': batang2d(ax, data[0], data[1], w_batang * skala, z=z + 1)
        elif jenis == 'a':
            k = data; el = atom[k][0]; bola2d(ax, *xy[k], RAD[el] * skala, CPK[el], z=z + 1)
        else: cuping2d(ax, data[0], data[1], data[2], 0.36 * skala, data[3], z=z + 1)
    return xy, dep

def hadap(P, kanan=None, atas=None, elev=15, azim=-60):
    """Putar koordinat dunia P sehingga vektor 'kanan' tampak mendatar ke kanan dan 'atas' tampak tegak ke atas."""
    M = matriks_pandang(elev, azim); C = np.stack([M[0], M[1], M[2]], 1)
    if kanan is None: kanan = np.cross(atas, [0.3, 0.7, 0.1])
    u = np.array(kanan, float); u /= np.linalg.norm(u)
    if atas is None: atas = np.cross([0.2, 0.9, 0.3], u)
    v = np.array(atas, float); v = v - np.dot(v, u) * u; v /= np.linalg.norm(v)
    for sg in (1, -1):
        d = sg * np.cross(v, u); B = np.stack([u, d, v], 1); R = C @ B.T
        if np.linalg.det(R) > 0: return P @ R.T
