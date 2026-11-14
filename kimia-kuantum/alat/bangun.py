#!/usr/bin/env python3
# Membangun PDF satu bab Kimia Kuantum dengan gaya Edisi 4 Fisika Umum.
# Pakai: python3 alat/bangun.py babNN ["Bab N"]   -> kimia-kuantum/babNN.pdf
# Tahap: pandoc (MathML) -> gaya.py + penyesuaian -> halaman pembuka -> Playwright (alat/render.cjs)
#        -> judul berjalan dan nomor halaman (reportlab, ditumpuk sebagai stream) -> penanda subbab.
import re, os, sys, glob, json, subprocess
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, ArrayObject, DecodedStreamObject, DictionaryObject
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
d = sys.argv[1]; n = int(d[-2:]); D = f'{R}/{d}'; K = f'{R}/_kerja'; os.makedirs(K, exist_ok=True)
fs = sorted(glob.glob(f'{D}/[a-z]-*.md'))
JUDUL = re.match(r'# Bab \d+ (.*)', open(fs[0]).readline()).group(1).strip()
# nama bagian dari RENCANA.md
bag, BAG = '', {}
for line in open(f'{R}/RENCANA.md'):
    m = re.match(r'## (Bagian [IVX]+) · (.*)', line)
    if m: bag = m.group(2).strip()
    m = re.match(r'### \S+ Bab (\d+) ', line)
    if m: BAG[int(m.group(1))] = bag
# ---------- 1. Markdown -> HTML
md = '\n\n'.join(open(f).read() for f in fs)
src = f'{D}/_bab.md'; out = f'{D}/_bab.html'; open(src, 'w').write(md)
css = ['../buku.css', '../buku2.css', '../buku3.css', '../pembuka.css']
subprocess.run(['pandoc', src, '-s', '--mathml', '--metadata', 'pagetitle=Kimia Kuantum', '-o', out] + sum([['-c', c] for c in css], []),
               check=True, cwd=D, stderr=subprocess.DEVNULL)
s = open(out).read()
s = re.sub(r'<mn>(\d+)</mn><mo>,</mo><mn>(\d+)</mn>', r'<mn>\1,\2</mn>', s)
s = re.sub(r'<mn>(\d+)</mn><mo>,</mo><msup><mn>(\d+)</mn>', r'<msup><mn>\1,\2</mn>', s)
open(out, 'w').write(s)
subprocess.run(['python3', f'{R}/gaya.py', out], check=True)
s = open(out).read()
s = re.sub(r'(<h2 id="[^"]*" class="sub">)\s*(\d+\.\d+) ', r'\1<span class="nsub">\2</span>', s)
s = re.sub(r'<strong>(Contoh \d+\.\d+) · ', r'<strong><span class="cno">\1</span>', s)
s = s.replace('<strong class="lk">Memahami hasil.</strong>', '<strong class="lk periksa">Memahami hasil.</strong>')
P = f'{K}/pembuka'
if not os.path.exists(f'{P}/orb{n:02d}.png'): subprocess.run(['python3', f'{R}/alat/pembuka.py', str(n)], check=True)
orb, sub = open(f'{P}/orb{n:02d}.txt').read().split('|')
def ganti(m):
    return (f'<section class="pembuka"><img class="orb" src="file://{P}/orb{n:02d}.png"><div class="bag">{BAG.get(n, "")}</div><div class="kb">BAB</div>'
            f'<div class="nb">{n}</div><h1{m.group(1)}>{m.group(2)}</h1><div class="cap">Latar: awan elektron orbital {orb}<sub>{sub}</sub> atom hidrogen</div></section>')
s = re.sub(r'<h1( id="[^"]*") class="bab"><span class="pita">.*?</span></span><span class="judul">(.*?)</span></h1>', ganti, s, count=1, flags=re.S)
assert 'class="pembuka"' in s, 'judul bab tidak ditemukan'
open(out, 'w').write(s)
bad = re.findall(r'class="math[^"]*"', s) + re.findall(r'\$[^$\s][^$]{0,40}\$', re.sub(r'<math.*?</math>', '', s, flags=re.S))
if bad: print('PERINGATAN: sisa TeX/MathML mentah:', bad[:8])
# ---------- 2. render
mentah = f'{K}/{d}-mentah.pdf'
json.dump([{'html': out, 'pdf': mentah}], open(f'{K}/jobs.json', 'w'))
subprocess.run(['node', f'{R}/alat/render.cjs', f'{K}/jobs.json'], check=True, cwd=R, stdout=subprocess.DEVNULL)
# ---------- 3. judul berjalan dan nomor halaman
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
SRC = PdfReader(mentah); NP = len(SRC.pages); W_, H_ = 595.28, 841.89
cv = canvas.Canvas(f'{K}/lapis.pdf', pagesize=(W_, H_))
TUA, GARIS = HexColor('#0e2748'), HexColor('#b9d6ef')
def badge(x, y, t, kanan):
    wd = max(cv.stringWidth(t, 'Helvetica-Bold', 8.5) + 4 * mm, 7 * mm); x0 = x - wd if kanan else x
    cv.setFillColor(TUA); cv.roundRect(x0, y - 1.5 * mm, wd, 5.0 * mm, 1.2 * mm, stroke=0, fill=1)
    cv.setFillColor(HexColor('#ffffff')); cv.setFont('Helvetica-Bold', 8.5); cv.drawCentredString(x0 + wd / 2, y, t)
    return wd
for p in range(1, NP + 1):
    if p > 1:
        Y = H_ - 13 * mm; L, Rr = 18 * mm, W_ - 18 * mm; kanan = p % 2 == 1
        tx = (f'Bab {n}  {JUDUL}' if kanan else 'Kimia Kuantum').upper()
        wd = badge(Rr if kanan else L, Y, str(p), kanan)
        cv.setFillColor(TUA); cv.setFont('Helvetica-Bold', 7)
        if kanan: cv.drawRightString(Rr - wd - 3 * mm, Y + .2 * mm, tx)
        else: cv.drawString(L + wd + 3 * mm, Y + .2 * mm, tx)
        cv.setStrokeColor(GARIS); cv.setLineWidth(.5); cv.line(L, Y - 2.6 * mm, Rr, Y - 2.6 * mm)
    cv.showPage()
cv.save()
LAP = PdfReader(f'{K}/lapis.pdf'); w = PdfWriter(); LFONT = {}
def tumpuk(pg, lp):
    fd = lp['/Resources']['/Font'].get_object()
    for nm, ref in fd.items():
        if nm not in LFONT:
            o = ref.get_object(); LFONT[nm] = w._add_object(DictionaryObject({NameObject(k): v for k, v in o.items()}))
    data = lp.get_contents().get_data()
    for nm in LFONT: data = data.replace(nm.encode() + b' ', b'/Ov' + nm[1:].encode() + b' ')
    def st(b):
        x = DecodedStreamObject(); x.set_data(b); return w._add_object(x)
    c = pg['/Contents'].get_object()
    lama = list(c) if isinstance(c, ArrayObject) else [pg.raw_get('/Contents')]
    pg[NameObject('/Contents')] = ArrayObject([st(b'q\n')] + lama + [st(b'\nQ\n'), st(data)])
    res = pg['/Resources'].get_object()
    if '/Font' not in res: res[NameObject('/Font')] = DictionaryObject()
    f = res['/Font'].get_object()
    for nm, ref in LFONT.items(): f[NameObject('/Ov' + nm[1:])] = ref
for i in range(NP):
    pg = w.add_page(SRC.pages[i])
    if i > 0: tumpuk(pg, LAP.pages[i])
# ---------- 4. penanda subbab
def norm(t): return re.sub(r'\s+', '', re.sub(r'-\n', '', t)).lower()
def plain(t): return re.sub(r'\$[^$]*\$|\*', '', t).strip()
TX = [norm(p.extract_text() or '') for p in SRC.pages]
def cari(t, mulai=0):
    t = norm(t)[:40]
    return next((i for i in range(mulai, NP) if t in TX[i]), None)
w.add_outline_item(f'Bab {n}  {JUDUL}', 0); last = 0
for line in md.split('\n'):
    m = re.match(r'^# (Ringkasan|Pertanyaan|Soal|Jawaban|Pembahasan|Bacaan)(.*)$', line) or re.match(r'^## (\d+\.\d+) (.*)$', line)
    if not m: continue
    i = cari(m.group(1) + plain(m.group(2)), last)
    if i is None: print('?? penanda tidak ketemu:', line); continue
    w.add_outline_item(f'{m.group(1)} {plain(m.group(2))}'.strip(), i); last = i
w.add_metadata({'/Title': f'Kimia Kuantum · Bab {n} {JUDUL}'}); w.page_mode = '/UseOutlines'
w.write(f'{R}/{d}.pdf'); print(f'{d}.pdf', NP, 'halaman')
