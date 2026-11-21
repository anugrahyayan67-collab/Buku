# Jembatan Python → render WebGL (three.js di Chromium lewat Playwright)
import json, os, subprocess, tempfile, numpy as np
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
CPK = {'C': '#3b4049', 'H': '#f4f4f4', 'O': '#e04a3c', 'N': '#3f72d6', 'Cl': '#3dbb6c', 'F': '#93d46c', 'Br': '#a8462a', 'S': '#e8c22a', 'B': '#f0b27a'}
RAD = {'C': 0.34, 'H': 0.23, 'O': 0.32, 'N': 0.32, 'Cl': 0.42, 'F': 0.29, 'Br': 0.46, 'S': 0.42, 'B': 0.32}
def hx(c): return int(c.lstrip('#'), 16)
def spek_molekul(atom, ikatan, skala_atom=1.0, r_ikatan=0.085, warna_ikatan='#b9bfc7', ganda=None):
    sp = {'atoms': [{'p': list(map(float, p)), 'r': RAD[e] * skala_atom, 'c': hx(CPK[e])} for e, p in atom], 'bonds': []}
    for i, j, *o in ikatan:
        n = o[0] if o else 1; p, q = np.array(atom[i][1], float), np.array(atom[j][1], float)
        if n == 1: sp['bonds'].append({'p': list(p), 'q': list(q), 'r': r_ikatan, 'c': hx(warna_ikatan)})
        else:
            d = q - p; u = np.cross(d, ganda if ganda is not None else [0, 0, 1]);
            if np.linalg.norm(u) < 1e-6: u = np.cross(d, [0, 1, 0])
            u = u / np.linalg.norm(u) * 0.09
            offs = [-1, 1] if n == 2 else [-1.6, 0, 1.6]
            for k in offs: sp['bonds'].append({'p': list(p + u * k), 'q': list(q + u * k), 'r': r_ikatan * 0.7, 'c': hx(warna_ikatan)})
    return sp
def render(jobs):
    """jobs: list (spec, out_png). Mengembalikan dict out → proyeksi label."""
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, dir=D) as f:
        json.dump([{'spec': s, 'out': o} for s, o in jobs], f); fn = f.name
    subprocess.run(['node', os.path.join(D, 'render.js'), fn], check=True)
    meta = json.load(open(fn.replace('.json', '.meta.json'))); os.remove(fn); os.remove(fn.replace('.json', '.meta.json'))
    return meta
def koord(smi, seed=7):
    from rdkit import Chem
    from rdkit.Chem import AllChem
    m = Chem.AddHs(Chem.MolFromSmiles(smi)); AllChem.EmbedMolecule(m, randomSeed=seed); AllChem.MMFFOptimizeMolecule(m)
    P = m.GetConformer().GetPositions(); c = [a.GetIdx() for a in m.GetAtoms() if a.GetSymbol() != 'H'][0]; P = P - P[c]
    atom = [(a.GetSymbol(), P[a.GetIdx()]) for a in m.GetAtoms()]
    ik = [(b.GetBeginAtomIdx(), b.GetEndAtomIdx(), int(b.GetBondTypeAsDouble())) for b in m.GetBonds()]
    return m, P, atom, ik
def potong(png, pad=6):
    im = Image.open(png); bb = im.getbbox()
    if bb: im = im.crop((max(bb[0] - pad, 0), max(bb[1] - pad, 0), min(bb[2] + pad, im.width), min(bb[3] + pad, im.height)))
    return im

def tampil(ax, png, labels=(), proj=None, fs=9, c='#0e2748', **kw):
    im = Image.open(png); W, H = im.size
    ax.imshow(im, extent=[0, W, H, 0]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.set_aspect('equal'); ax.axis('off')
    for (t, k), xy in zip(labels, proj or []):
        ax.text(xy[0], xy[1], t, ha='center', va='center', fontsize=fs, color=c, **kw)
def tetra(L=1.0):
    v = np.array([[0, 0, 1], [0.943, 0, -0.333], [-0.471, 0.816, -0.333], [-0.471, -0.816, -0.333]]); return v * L

def kamera_terbaik(titik, elev=(8, 40), skor_extra=None):
    """Pilih arah kamera (ortografik, sumbu z ke atas) yang memaksimalkan jarak terproyeksi terkecil antartitik."""
    titik = np.array(titik, float); best = None
    for e in np.radians(np.arange(elev[0], elev[1] + 1, 2)):
        for a in np.radians(np.arange(0, 360, 3)):
            c = np.array([np.cos(e) * np.cos(a), np.cos(e) * np.sin(a), np.sin(e)])
            x = np.cross([0, 0, 1], c); x /= np.linalg.norm(x); y = np.cross(c, x)
            Q = np.stack([titik @ x, titik @ y], 1); d = np.sqrt(((Q[:, None] - Q[None]) ** 2).sum(-1)); np.fill_diagonal(d, 9)
            s = d.min()
            if best is None or s > best[0] + 1e-6: best = (s, c)
    return list(best[1])
