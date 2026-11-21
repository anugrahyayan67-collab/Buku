# Pemotong dan penempat gambar RDKit: buang tepi kosong, batasi pembesaran, tempel tanpa distorsi
import numpy as np
from PIL import Image

def rapat(img, maks=1.7, pad=8):
    """Potong tepi kosong; bila molekul kecil, sisakan kanvas minimal (ukuran asli / maks) agar tidak membengkak."""
    a = np.asarray(img.convert('RGBA')).astype(int); bg = a[1, 1]
    m = (np.abs(a - bg).sum(2) > 24) & (a[..., 3] > 10) if bg[3] > 10 else a[..., 3] > 10
    ys, xs = np.nonzero(m)
    if not len(xs): return img
    c = img.convert('RGBA').crop((max(xs.min() - pad, 0), max(ys.min() - pad, 0), min(xs.max() + pad + 1, a.shape[1]), min(ys.max() + pad + 1, a.shape[0])))
    W, H = max(c.width, int(img.width / maks)), max(c.height, int(img.height / maks))
    if (W, H) == c.size: return putih_ke_alfa(c)
    kan = Image.new('RGBA', (W, H), (255, 255, 255, 0) if bg[3] < 10 else tuple(bg)); kan.paste(c, ((W - c.width) // 2, (H - c.height) // 2)); return putih_ke_alfa(kan)

def putih_ke_alfa(im):
    """Latar putih pekat -> transparan (warna dipulihkan dari campuran dengan putih), agar panah/teks di bawah gambar tetap terlihat."""
    a = np.asarray(im.convert('RGBA')).astype(float)
    if a[1, 1, 3] < 250 or a[1, 1, :3].min() < 250: return im
    rgb = a[..., :3] / 255; al = np.clip((1 - rgb).max(2), 0, 1); al = np.maximum(al, 1e-6)
    col = 1 - (1 - rgb) / al[..., None]; out = np.dstack([np.clip(col, 0, 1) * 255, al * a[..., 3]])
    out[al < 0.004, 3] = 0; return Image.fromarray(out.astype(np.uint8), 'RGBA')

def pasang(ax, img, x0, x1, y0, y1, zorder=2, maks=None, **k):
    """Tempel img di kotak data [x0,x1]x[y0,y1], rasio dijaga, di tengah kotak."""
    try: ax.apply_aspect()
    except Exception: pass
    p0, p1 = ax.transData.transform((x0, y0)), ax.transData.transform((x1, y1)); bw, bh = abs(p1[0] - p0[0]), abs(p1[1] - p0[1])
    s = min(bw / img.width, bh / img.height, maks or 1e9); fx, fy = img.width * s / bw, img.height * s / bh
    cx, cy, dx, dy = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) * fx / 2, (y1 - y0) * fy / 2
    return ax.imshow(img, extent=[cx - dx, cx + dx, cy - dy, cy + dy], zorder=zorder, aspect=ax.get_aspect(), **k)

def ukuran_px(ax, x0, x1, y0, y1):
    """Ukuran kotak data dalam piksel figur (untuk merender RDKit pada resolusi asli, huruf seragam)."""
    try: ax.apply_aspect()
    except Exception: pass
    p0, p1 = ax.transData.transform((x0, y0)), ax.transData.transform((x1, y1)); return int(abs(p1[0] - p0[0])), int(abs(p1[1] - p0[1]))
