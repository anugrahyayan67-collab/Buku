#!/usr/bin/env python3
# Membangun PDF Lampiran A-E Kimia Kuantum: python3 lampiran/_bangun.py  -> kimia-kuantum/lampiran.pdf
# Salinan ringkas alat/bangun.py tanpa halaman pembuka bab (alat bersama sengaja tidak diubah).
import re, os, glob, json, subprocess
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, ArrayObject, DecodedStreamObject, DictionaryObject
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
D = f'{R}/lampiran'; K = f'{R}/_kerja'; os.makedirs(K, exist_ok=True)
fs = sorted(glob.glob(f'{D}/[a-z]-*.md'))
md = '\n\n'.join(open(f).read() for f in fs)
md = re.sub(r'^\(([a-h])\) ', r'\\(\1) ', md, flags=re.M)
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
# nama grup + tabel karakternya jangan terpisah halaman
s = re.sub(r'(<p><strong>(?:(?!</p>).)*?</strong> \(contoh:(?:(?!</p>).)*</p>\s*<table.*?</table>)',
           r'<div style="break-inside: avoid;">\1</div>', s, flags=re.S)
# setiap lampiran mulai di halaman baru
s = re.sub(r'(<h1 id="[^"]*" class="pita1")', r'\1 style="break-before: page;"', s)
s = s.replace(' style="break-before: page;"', '', 1)
open(out, 'w').write(s)
bad = re.findall(r'class="math[^"]*"', s) + re.findall(r'\$[^$\s][^$]{0,40}\$', re.sub(r'<math.*?</math>', '', s, flags=re.S))
if bad: print('PERINGATAN: sisa TeX/MathML mentah:', bad[:8])
mentah = f'{K}/lampiran-mentah.pdf'
json.dump([{'html': out, 'pdf': mentah}], open(f'{K}/jobs.json', 'w'))
subprocess.run(['node', f'{R}/alat/render.cjs', f'{K}/jobs.json'], check=True, cwd=R, stdout=subprocess.DEVNULL)
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
SRC = PdfReader(mentah); NP = len(SRC.pages); W_, H_ = 595.28, 841.89
cv = canvas.Canvas(f'{K}/lapis.pdf', pagesize=(W_, H_)); TUA, GARIS = HexColor('#0e2748'), HexColor('#b9d6ef')
for p in range(1, NP + 1):
    Y = H_ - 13 * mm; L, Rr = 18 * mm, W_ - 18 * mm; kanan = p % 2 == 1
    tx = 'LAMPIRAN' if kanan else 'KIMIA KUANTUM'; t = str(p)
    wd = max(cv.stringWidth(t, 'Helvetica-Bold', 8.5) + 4 * mm, 7 * mm); x0 = Rr - wd if kanan else L
    cv.setFillColor(TUA); cv.roundRect(x0, Y - 1.5 * mm, wd, 5.0 * mm, 1.2 * mm, stroke=0, fill=1)
    cv.setFillColor(HexColor('#ffffff')); cv.setFont('Helvetica-Bold', 8.5); cv.drawCentredString(x0 + wd / 2, Y, t)
    cv.setFillColor(TUA); cv.setFont('Helvetica-Bold', 7)
    if kanan: cv.drawRightString(Rr - wd - 3 * mm, Y + .2 * mm, tx)
    else: cv.drawString(L + wd + 3 * mm, Y + .2 * mm, tx)
    cv.setStrokeColor(GARIS); cv.setLineWidth(.5); cv.line(L, Y - 2.6 * mm, Rr, Y - 2.6 * mm); cv.showPage()
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
    pg = w.add_page(SRC.pages[i]); tumpuk(pg, LAP.pages[i])
def norm(t): return re.sub(r'\s+', '', re.sub(r'-\n', '', t)).lower()
TX = [norm(p.extract_text() or '') for p in SRC.pages]; last = 0; induk = None
for line in md.split('\n'):
    m = re.match(r'^# (Lampiran [A-E]) (.*)$', line) or re.match(r'^## ([A-E]\.\d+) (.*)$', line)
    if not m: continue
    key = norm(m.group(1) + m.group(2))[:30]
    i = next((k for k in range(last, NP) if key in TX[k]), None)
    if i is None: print('?? penanda tidak ketemu:', line); continue
    if line.startswith('# '): induk = w.add_outline_item(f'{m.group(1)} {m.group(2)}', i)
    else: w.add_outline_item(f'{m.group(1)} {m.group(2)}', i, parent=induk)
    last = i
w.add_metadata({'/Title': 'Kimia Kuantum · Lampiran A–E'}); w.page_mode = '/UseOutlines'
w.write(f'{R}/lampiran.pdf'); print('lampiran.pdf', NP, 'halaman')
