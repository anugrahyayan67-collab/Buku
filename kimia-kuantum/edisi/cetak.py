#!/usr/bin/env python3
# Mencetak Kimia Kuantum Edisi 1 sebagai satu buku utuh.
# Pakai: python3 kimia-kuantum/edisi/cetak.py [--lewati-bab]   (--lewati-bab: pakai PDF bab hasil render sebelumnya)
import re, os, sys, glob, json, subprocess, html
from pypdf import PdfReader, PdfWriter
E = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(E); K = f'{E}/_kerja'
os.makedirs(K, exist_ok=True)
LEWATI = '--lewati-bab' in sys.argv
BAB = sorted(int(d[-2:]) for d in glob.glob(f'{R}/bab[0-9][0-9]'))
BAG = {}; _b = ''
for _l in open(f'{R}/RENCANA.md'):
    _m = re.match(r'## Bagian ([IVX]+) · (.*)', _l)
    if _m: _b = (_m.group(1), _m.group(2).strip())
    _m = re.match(r'### \S+ Bab (\d+) ', _l)
    if _m: BAG[int(_m.group(1))] = _b
JUDUL = {n: re.match(r'# Bab \d+ (.*)', open(sorted(glob.glob(f'{R}/bab{n:02d}/[a-z]-*.md'))[0]).readline()).group(1).strip() for n in BAB}

def koma(s):
    s = re.sub(r'<mn>(\d+)</mn><mo>,</mo><mn>(\d+)</mn>', r'<mn>\1,\2</mn>', s)
    return re.sub(r'<mn>(\d+)</mn><mo>,</mo><msup><mn>(\d+)</mn>', r'<msup><mn>\1,\2</mn>', s)
def md2html(md, out, css):
    src = out[:-5] + '.md'; open(src, 'w').write(md)
    cmd = ['pandoc', src, '-s', '--mathml', '--metadata', 'pagetitle=Kimia Kuantum', '-o', out] + sum([['-c', c] for c in css], [])
    subprocess.run(cmd, check=True, cwd=os.path.dirname(out), stderr=subprocess.DEVNULL)
    s = koma(open(out).read()); open(out, 'w').write(s)
    s = open(out).read().replace('<h1\n', '<h1 ').replace('<h2\n', '<h2 ').replace('<h3\n', '<h3 ')
    s = re.sub(r'(<h[1-3][^>]*>)(.*?)(</h[1-3]>)', lambda m: m.group(1) + m.group(2).replace('\n', ' ') + m.group(3), s, flags=re.S); open(out, 'w').write(s)
    subprocess.run(['python3', f'{R}/gaya.py', out], check=True)
    s = open(out).read()
    s = re.sub(r'<h1 id="[^"]*" class="(?:lampiran|pita1)">Lampiran (\w) (.*?)</h1>',
               r'<h1 class="bab"><span class="pita"><span class="kata">Lampiran</span><span class="no">\1</span></span><span class="judul">\2</span></h1>', s)
    s = re.sub(r'<h2 id="([^"]*)">([A-E]\.\d+ )', r'<h2 id="\1" class="sub">\2', s)
    s = re.sub(r'(<h2 id="[^"]*" class="sub">)\s*([A-E0-9]+\.\d+) ', r'\1<span class="nsub">\2</span>', s)
    s = re.sub(r'<strong>(Contoh \d+\.\d+) · ', r'<strong><span class="cno">\1</span>', s)
    s = s.replace('<strong class="lk">Memahami hasil.</strong>', '<strong class="lk periksa">Memahami hasil.</strong>')
    open(out, 'w').write(s)
def pembuka(n, out):
    s = open(out).read(); P = f'{E}/_kerja/pembuka'
    cap = open(f'{P}/b{n:02d}.txt').read().strip()
    subs = [m for f_ in sorted(glob.glob(f'{R}/bab{n:02d}/[a-y]-*.md')) for m in re.findall(r'^## (\d+\.\d+) (.*)$', open(f_).read(), re.M)]
    garis = ''.join(f'<li><b>{k}</b>{html.escape(re.sub(r"[$*]", "", t))}</li>' for k, t in subs)
    outline = f'<div class="outline"><div class="oh">Isi bab</div><ul>{garis}</ul></div>'
    bag = f'Bagian {BAG[n][0]} · {BAG[n][1]}'
    def ganti(m):
        return (f'<section class="pembuka"><img class="orb" src="file://{P}/b{n:02d}.png"><div class="bag">{bag}</div><div class="kb">BAB</div>'
                f'<div class="nb">{n}</div><h1{m.group(1)}>{m.group(2)}</h1><div class="cap">{cap}</div>{outline}</section>')
    s = re.sub(r'<h1( id="[^"]*") class="bab"><span class="pita">.*?</span></span><span class="judul">(.*?)</span></h1>', ganti, s, count=1, flags=re.S)
    # bagian Soal: bungkus agar tata letaknya rapi (nomor menggantung, label tingkat)
    m1 = re.search(r'<h1 id="[^"]*" class="pita1">Soal</h1>', s); m2 = re.search(r'<h1 id="[^"]*" class="pita1">Jawaban</h1>', s)
    if m1 and m2:
        blok = s[m1.end():m2.start()]
        blok = re.sub(r'<p><strong>(Dasar|Menengah|Tantangan[^<]*)</strong></p>', r'<p class="tk">\1</p>', blok)
        blok = re.sub(r'<p>(<strong>\d+\.</strong>)', r'<p class="si">\1', blok)
        mb = re.search(r'<blockquote>.*?</blockquote>', blok, re.S)   # catatan data di atas, selebar halaman
        if mb: blok = mb.group(0) + blok[:mb.start()] + blok[mb.end():]
        s = s[:m1.end()] + '<div class="soal2">' + blok + '</div>' + s[m2.start():]
    # bagian Pertanyaan: dikelompokkan per subbab, dua kolom seperti Soal
    m1 = re.search(r'<h1 id="[^"]*" class="pita1">Pertanyaan</h1>', s); m2 = re.search(r'<h1 id="[^"]*" class="pita1">Soal</h1>', s)
    if m1 and m2 and m1.end() < m2.start():
        s = s[:m1.end()] + '<div class="soal2 tanya">' + s[m1.end():m2.start()] + '</div>' + s[m2.start():]
    balik = f'https://hal/d/{n}'
    s = re.sub(r'(<h2 id="[^"]*" class="sub">)(.*?)</h2>', lambda m: f'{m.group(1)}<a class="tl" href="{balik}">{m.group(2)}</a></h2>', s, flags=re.S)
    s = re.sub(r'(<h1 id="[^"]*" class="pita1">)(.*?)</h1>', lambda m: f'{m.group(1)}<a class="tl" href="{balik}">{m.group(2)}</a></h1>', s, flags=re.S)
    s = re.sub(r'(<section class="pembuka">.*?<h1[^>]*>)(.*?)</h1>', lambda m: f'{m.group(1)}<a class="tl" href="{balik}">{m.group(2)}</a></h1>', s, count=1, flags=re.S)
    open(out, 'w').write(s)
def render(jobs):
    p = f'{K}/jobs.json'; json.dump(jobs, open(p, 'w'))
    subprocess.run(['node', f'{E}/render.cjs', p], check=True, cwd=R)
CSS_BAB = ['../buku.css', '../buku2.css', '../buku3.css', '../pembuka.css', '../edisi/kk.css']; CSS_E = ['../../buku.css', '../../buku2.css', '../../buku3.css', '../kk.css']

# ---------- 1. bab-bab dan lampiran
jobs = []
for n in BAB:
    d = f'{R}/bab{n:02d}'
    md = '\n\n'.join(open(f).read() for f in sorted(glob.glob(f'{d}/[a-z]-*.md')))
    md2html(md, f'{d}/_e2.html', CSS_BAB); pembuka(n, f'{d}/_e2.html'); jobs.append({'html': f'{d}/_e2.html', 'pdf': f'{K}/bab{n:02d}.pdf'})
md2html('\n\n'.join(open(f).read() for f in sorted(glob.glob(f'{R}/lampiran/[a-z]-*.md'))), f'{K}/lampiran.html', CSS_E); jobs.append({'html': f'{K}/lampiran.html', 'pdf': f'{K}/lampiran.pdf'})
md2html(open(f'{E}/depan.md').read(), f'{K}/depan.html', CSS_E); jobs.append({'html': f'{K}/depan.html', 'pdf': f'{K}/depan.pdf'})
if not LEWATI: render(jobs)
else: render([j for j in jobs if j['pdf'].endswith('lampiran.pdf')])   # lampiran selalu dirender ulang

# ---------- 2. teks per halaman, letak judul
def norm(s): return re.sub(r'\s+', '', re.sub(r'-\n', '', s)).lower()
def plain(t): return re.sub(r'\$[^$]*\$|\*', '', t).strip()
TEKS = {}; NHAL = {}
for n in BAB + ['lampiran']:
    key = f'bab{n:02d}' if n != 'lampiran' else n
    r = PdfReader(f'{K}/{key}.pdf'); NHAL[n] = len(r.pages); TEKS[n] = [norm(p.extract_text() or '') for p in r.pages]
def cari(n, s, mulai=0, akhir=None):
    s = norm(s)[:40]
    for i in range(mulai, akhir if akhir is not None else NHAL[n]):
        if s in TEKS[n][i]: return i
    return None
SUB = {}; AKHIR = {}
for n in BAB:
    subs = []; last = 1
    for f in sorted(glob.glob(f'{R}/bab{n:02d}/[a-z]-*.md')):
        for m in re.finditer(r'^## (\d+\.\d+) (.*)$', open(f).read(), re.M):
            i = cari(n, m.group(1) + plain(m.group(2)), last)
            if i is None: print('?? tidak ketemu', n, m.group(0)); i = last
            subs.append((m.group(1), plain(m.group(2)), i)); last = i
    SUB[n] = subs
    rk = cari(n, f'Ringkasan Bab {n}', last); jw = cari(n, 'Jawaban No. Jawaban No. Jawaban', rk or last)
    AKHIR[n] = (rk if rk is not None else last, jw if jw is not None else last)

# ---------- 3. penomoran arab
CETAK = '--cetak' in sys.argv   # versi cetak: halaman kosong agar bab mulai di halaman kanan
hal = 1; MULAI = {}; URUT = []        # URUT: (berkas/None, idx, jenis, info)
def tambah(key, n, jenis):
    global hal
    if CETAK and hal % 2 == 0: URUT.append((None, 0, 'kosong', None)); hal += 1
    MULAI[key] = hal
    for i in range(n):
        URUT.append((key, i, 'awal' if i == 0 else 'isi', None)); hal += 1
for n in BAB: tambah(f'bab{n:02d}', NHAL[n], 'bab')
tambah('lampiran', NHAL['lampiran'], 'lampiran')
LJ = {}
for _f in sorted(glob.glob(f'{R}/lampiran/[a-z]-*.md')):
    _m = re.match(r'# Lampiran (\w) (.*)', open(_f).readline()); LJ[_m.group(1)] = (_m.group(2).strip(), cari('lampiran', 'LAMPIRAN' + _m.group(1) + _m.group(2)) or cari('lampiran', _m.group(1) + 'LAMPIRAN' + _m.group(2)) or cari('lampiran', _m.group(2)) or 0)
LAMP_B = LJ['B'][1]
def hal_bab(n, i): return MULAI[f'bab{n:02d}'] + i

# ---------- 4. indeks
STOP = set(open(f'{E}/indeks_buang.txt').read().split('\n')) if os.path.exists(f'{E}/indeks_buang.txt') else set()
cue = re.compile(r'disebut|dinamai|dinamakan|yaitu|didefinisikan|adalah|artinya|dikenal')
ISTILAH = {}
for n in BAB:
    for f in sorted(glob.glob(f'{R}/bab{n:02d}/[a-y]-*.md')):
        for para in open(f).read().split('\n\n'):
            if para.startswith(('|', '#')): continue
            for sent in re.split(r'(?<=[.!?])\s+', para):
                if not cue.search(sent): continue
                for m in re.finditer(r'\*\*([^*$\n]{3,45}?)\*\*', sent):
                    x = m.group(1).strip()
                    if not re.match(r"^[a-zA-Z][\w\s\-–'()/]*$", x) or len(x.split()) > 5: continue
                    if x[0].isupper() and not re.match(r'(Hukum|Persamaan|Asas|Teorema|Prinsip|Efek|Kaidah|Kesetaraan)', x): continue
                    if x.lower() in STOP: continue
                    ISTILAH.setdefault(x[0].lower() + x[1:], [n])
for line in open(f'{E}/indeks_tambah.txt').read().strip().split('\n'):
    ISTILAH.setdefault(line.strip(), None)
ENTRI = {}
BOLD = {}
for n in BAB:
    for f in sorted(glob.glob(f'{R}/bab{n:02d}/[a-y]-*.md')):
        for m in re.finditer(r'\*\*([^*$\n]{3,60}?)\*\*', open(f).read()): BOLD.setdefault(m.group(1).strip().lower(), n)
for t, bab in ISTILAH.items():
    tl = t.lower(); hs = []
    if bab:
        i = cari(bab[0], t, 0, AKHIR[bab[0]][0])
        if i is not None: hs = [hal_bab(bab[0], i)]
    else:
        sub = [(n, i) for n in BAB for k, judul, i in SUB[n] if tl in judul.lower()]
        if sub: hs = [hal_bab(n, i) for n, i in sub[:2]]
        else:
            nb = BOLD.get(tl) or next((BOLD[b] for b in BOLD if tl in b), None)
            for n in ([nb] if nb else BAB):
                i = cari(n, t, 1, AKHIR[n][0])
                if i is not None: hs = [hal_bab(n, i)]; break
    if hs: ENTRI[t] = sorted(set(hs))
def kunci(t): return re.sub(r'[^a-z0-9 ]', '', t.lower().replace('–', ' '))
huruf = None; baris = []
for t in sorted(ENTRI, key=kunci):
    h0 = kunci(t)[:1].upper()
    if h0 != huruf: huruf = h0; baris.append(f'<p><span class="huruf">{h0}</span></p>')
    baris.append(f'<p><b>{html.escape(t)}</b>, {", ".join(f'<a class="tl" href="https://hal/a/{h}">{h}</a>' for h in ENTRI[t])}</p>')
open(f'{K}/indeks.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../buku.css"><link rel="stylesheet" href="../../buku2.css"><link rel="stylesheet" href="../../buku3.css"><link rel="stylesheet" href="../kk.css"></head>
<body><div class="indeks"><h1 style="page-break-before:avoid">Indeks</h1><p class="catatan">Nomor menunjuk halaman tempat istilah itu diperkenalkan atau dibahas pertama kali.</p><div class="kol">{''.join(baris)}</div></div></body></html>''')
render([{'html': f'{K}/indeks.html', 'pdf': f'{K}/indeks.pdf'}])
tambah('indeks', len(PdfReader(f'{K}/indeks.pdf').pages), 'indeks')
print('istilah indeks:', len(ENTRI))

# ---------- 5. bagian depan: judul, keterangan, isi ringkas, daftar isi
def tuju(p): return f'https://hal/{"a" if str(p).isdigit() else "r"}/{p}'
def r(t, p, cls='r'): return f'<a class="tl" href="{tuju(p)}"><div class="{cls}"><span class="t">{t}</span><span class="d"></span><span class="p">{p}</span></div></a>'
ring = ['<div class="ringkas3">']
for n in BAB:
    if n == 1 or BAG[n] != BAG[n - 1]: ring.append(f'<div class="bagianbuku">Bagian {BAG[n][0]} · {BAG[n][1]}</div>')
    ring.append(f'<div class="bab">{r(f"<span class=no>{n}</span>{JUDUL[n]}", MULAI[f"bab{n:02d}"])}</div>')
ring.append('<div class="bagianbuku">Bagian akhir</div>')
ring += [f'<div class="bab">{r(f"<span class=no>{x}</span>{t}", p)}</div>' for x, t, p in [(x, LJ[x][0], MULAI['lampiran'] + LJ[x][1]) for x in sorted(LJ)] + [('', 'Indeks', MULAI['indeks'])]]
ring.append('</div>')
isi = []
for n in BAB:
    isi.append(f'<div class="bab">{r(f"<span class=no>{n}</span>{JUDUL[n]}", MULAI[f"bab{n:02d}"])}</div>')
    for k, t, i in SUB[n]: isi.append(r(f'<b>{k}</b>{html.escape(t)}', hal_bab(n, i), 'r sub'))
    isi.append(r('Ringkasan, pertanyaan, dan soal', hal_bab(n, AKHIR[n][0]), 'r akhir'))
    isi.append(r('Jawaban dan pembahasan', hal_bab(n, AKHIR[n][1]), 'r akhir'))
for x in sorted(LJ): isi.append(f'<div class="bab">{r(f"Lampiran {x} · {LJ[x][0]}", MULAI["lampiran"] + LJ[x][1])}</div>')
isi.append(f'<div class="bab">{r("Indeks", MULAI["indeks"])}</div>')
nbab = len(BAB); ncontoh = sum(len(re.findall(r'::: \{\.contoh\}', open(f).read())) for f in glob.glob(f'{R}/bab*/[a-y]-*.md'))
nsoal = sum(len(re.findall(r'^\*\*\d+\.\*\*', open(f'{R}/bab{n:02d}/z-akhir.md').read(), re.M)) for n in BAB)
open(f'{K}/judul.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../buku.css"><link rel="stylesheet" href="../../buku2.css"><link rel="stylesheet" href="../../buku3.css"><link rel="stylesheet" href="../kk.css"></head><body>
<div class="judul-hal halaman"><div class="atas"><div class="j">KIMIA<br>KUANTUM</div><div class="s">dari persamaan Schrödinger sampai kimia komputasi</div><div class="pen">Septian Anugrah Dwi Putra</div><div class="e">EDISI PERTAMA</div></div>
<div class="bawah"></div></div>
<div class="ket halaman"><p><b>Kimia Kuantum</b><br>Edisi Pertama, 2026<br>Penyusun: Septian Anugrah Dwi Putra</p>
<p>Isi: {nbab} bab dalam lima bagian, Lampiran A–E, serta indeks. Buku ini merupakan lanjutan dari <i>Fisika Umum</i> karya penyusun yang sama.</p>
<p>Naskah disusun oleh penyusun dengan bantuan Claude (Anthropic). Semua angka dalam contoh dan jawaban dihitung ulang dengan komputer. Gambar dibuat dengan Matplotlib; huruf isi Caladea, huruf judul Inter.</p>
<p>Tanda desimal mengikuti kaidah bahasa Indonesia (koma). Satuan mengikuti Sistem Internasional.</p></div>
</body></html>''')
open(f'{K}/isi.html', 'w').write(f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../../buku.css"><link rel="stylesheet" href="../../buku2.css"><link rel="stylesheet" href="../../buku3.css"><link rel="stylesheet" href="../kk.css"></head><body>
<div class="toc halaman"><h1 style="page-break-before:avoid">Isi Ringkas</h1>{''.join(ring)}</div>
<div class="toc"><h1 style="page-break-before:avoid">Daftar Isi</h1>{r("Kata Pengantar", "@KP")}{r("Cara Memakai Buku Ini", "@CM")}{''.join(isi)}</div></body></html>''')
render([{'html': f'{K}/judul.html', 'pdf': f'{K}/judul.pdf'}, {'html': f'{K}/isi.html', 'pdf': f'{K}/isi.pdf'}])
def roman(x):
    out = ''
    for v, s in [(10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]:
        while x >= v: out += s; x -= v
    return out
# halaman depan: judul(i) ket(ii) isi ringkas(iii) [kosong] daftar isi(...) kata pengantar(ganjil) ...
isi_r = PdfReader(f'{K}/isi.pdf'); n_ringkas = 1
n_isi = len(isi_r.pages) - n_ringkas
dep_r = PdfReader(f'{K}/depan.pdf'); dteks = [norm(p.extract_text() or '') for p in dep_r.pages]
cm_i = next(i for i, t in enumerate(dteks) if 'caramemakaibukuini' in t)
DEP = [('judul', 0), ('judul', 1), ('isi', 0)]
if CETAK and len(DEP) % 2 == 1: DEP.append((None, 0))
DEP += [('isi', 1 + i) for i in range(n_isi)]
if CETAK and len(DEP) % 2 == 1: DEP.append((None, 0))
kp = len(DEP) + 1
DEP += [('depan', i) for i in range(len(dep_r.pages))]
s = open(f'{K}/isi.html').read().replace('@KP', roman(kp)).replace('@CM', roman(kp + cm_i)); open(f'{K}/isi.html', 'w').write(s)
render([{'html': f'{K}/isi.html', 'pdf': f'{K}/isi.pdf'}])
if CETAK and len(DEP) % 2 == 1: DEP.append((None, 0))

# ---------- 6. sampul, judul berjalan, rakit
subprocess.run(['python3', f'{E}/sampul.py', str(nbab), str(ncontoh), str(nsoal), str(hal - 1 + len(DEP))], check=True)
render([{'html': f'{K}/sampul.html', 'pdf': f'{K}/sampul.pdf', 'margin': ['0', '0', '0', '0']}])
SRC = {k: PdfReader(f'{K}/{k}.pdf') for k in ['judul', 'isi', 'depan', 'lampiran', 'indeks', 'sampul'] + [f'bab{n:02d}' for n in BAB]}
halaman = []   # (reader-key/None, idx, overlay dict)
for i, (k, j) in enumerate(DEP):
    no = roman(i + 1)
    ov = {} if (k in (None, 'judul')) or (k == 'isi' and j == 0 and False) else {'bawah': no}
    halaman.append((k, j, ov))
BABNYA = {}
for k, j, jenis, _ in URUT:
    p = len(halaman) - len(DEP) + 1
    if jenis == 'kosong': halaman.append((None, 0, {})); continue
    if k.startswith('bab'):
        n = int(k[3:]); kanan = f'Bab {n} · {JUDUL[n]}'
    elif k == 'lampiran':
        x = max((x for x in LJ if LJ[x][1] <= j), default='A'); kanan = f'Lampiran {x} · {LJ[x][0]}'
    else: kanan = 'Indeks'
    if jenis == 'awal': ov = {}
    elif p % 2: ov = {'kanan': kanan, 'no': str(p)}
    else: ov = {'kiri': 'Kimia Kuantum', 'no': str(p)}
    halaman.append((k, j, ov))
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
cv = canvas.Canvas(f'{K}/lapis.pdf', pagesize=(595.28, 841.89))
BIRU, TUA, GARIS = HexColor('#4a3ab0'), HexColor('#1e1548'), HexColor('#d6cdf3')
def badge(x, y, t, kanan):
    wd = max(cv.stringWidth(t, 'Helvetica-Bold', 8.5) + 4 * mm, 7 * mm)
    x0 = x - wd if kanan else x
    cv.setFillColor(TUA); cv.roundRect(x0, y - 1.5 * mm, wd, 5.0 * mm, 1.2 * mm, stroke=0, fill=1)
    cv.setFillColor(HexColor('#ffffff')); cv.setFont('Helvetica-Bold', 8.5); cv.drawCentredString(x0 + wd / 2, y, t)
    return wd
for k, j, ov in halaman:
    Y = 841.89 - 13 * mm; L, Rr = 18 * mm, 595.28 - 18 * mm
    if 'bawah' in ov:
        cv.setFillColor(TUA); cv.setFont('Helvetica-Bold', 8.5); cv.drawCentredString(595.28 / 2, 9 * mm, ov['bawah'])
    elif 'kanan' in ov or 'kiri' in ov:
        kanan = 'kanan' in ov; tx = (ov.get('kanan') or ov.get('kiri')).upper()
        wd = badge(Rr if kanan else L, Y, ov['no'], kanan)
        cv.setFillColor(TUA); cv.setFont('Helvetica-Bold', 7)
        if kanan: cv.drawRightString(Rr - wd - 3 * mm, Y + .2 * mm, tx)
        else: cv.drawString(L + wd + 3 * mm, Y + .2 * mm, tx)
        cv.setStrokeColor(GARIS); cv.setLineWidth(.5); cv.line(L, Y - 2.6 * mm, Rr, Y - 2.6 * mm)
    cv.showPage()
cv.save()
LAP = PdfReader(f'{K}/lapis.pdf')
w = PdfWriter(); W_, H_ = 595.28, 841.89
from pypdf.generic import NameObject, ArrayObject, DecodedStreamObject, DictionaryObject
LFONT = {}
def tumpuk(pg, lp):
    fd = lp['/Resources']['/Font'].get_object()
    for nm, ref in fd.items():
        if nm not in LFONT:
            o = ref.get_object(); d = DictionaryObject({NameObject(k): v for k, v in o.items()}); LFONT[nm] = w._add_object(d)
    data = lp.get_contents().get_data()
    for nm in LFONT: data = data.replace(nm.encode() + b' ', b'/Ov' + nm[1:].encode() + b' ')
    def st(b):
        x = DecodedStreamObject(); x.set_data(b); return w._add_object(x)
    c = pg['/Contents']; c = c.get_object()
    lama = list(c) if isinstance(c, ArrayObject) else [pg.raw_get('/Contents')]
    pg[NameObject('/Contents')] = ArrayObject([st(b'q\n')] + lama + [st(b'\nQ\n'), st(data)])
    res = pg['/Resources'].get_object()
    if '/Font' not in res: res[NameObject('/Font')] = DictionaryObject()
    f = res['/Font'].get_object()
    for nm, ref in LFONT.items(): f[NameObject('/Ov' + nm[1:])] = ref

w.add_page(SRC['sampul'].pages[0])
if CETAK: w.add_blank_page(W_, H_)
for idx, (k, j, ov) in enumerate(halaman):
    if k is None: pg = w.add_blank_page(W_, H_)
    else: pg = w.add_page(SRC[k].pages[j])
    if ov: tumpuk(pg, LAP.pages[idx])
if CETAK and (len(w.pages)) % 2 == 0: w.add_blank_page(W_, H_)
w.add_page(SRC['sampul'].pages[1])
# tautan daftar isi / indeks -> lompat ke halaman
from pypdf.generic import NumberObject
S0_ = 2 if CETAK else 1; OFF_ = S0_ + len(DEP) - 1
ROM = {roman(i + 1): S0_ + i for i in range(len(DEP))}
ISI_T = [norm(p.extract_text() or '') for p in PdfReader(f'{K}/isi.pdf').pages]
DI = {}
for n in BAB:
    j = next((j for j in range(1, len(ISI_T)) if norm(f'{n}{JUDUL[n]}') in ISI_T[j]), 1)
    DI[str(n)] = S0_ + DEP.index(('isi', j))
nlink = 0
for pg in w.pages:
    for ref in (pg.get('/Annots') or []):
        a = ref.get_object(); A = a.get('/A')
        if not A or not str(A.get_object().get('/URI', '')).startswith('https://hal/'): continue
        _, jenis, v = str(A.get_object()['/URI']).rsplit('/', 2)
        idx = OFF_ + int(v) if jenis == 'a' else DI.get(v) if jenis == 'd' else ROM.get(v)
        if idx is None or idx >= len(w.pages): continue
        a[NameObject('/A')] = DictionaryObject({NameObject('/S'): NameObject('/GoTo'), NameObject('/D'): ArrayObject([w.pages[idx].indirect_reference, NameObject('/Fit')])})
        nlink += 1
print('tautan:', nlink)
# ---------- 7. penanda (bookmark)
S0 = 2 if CETAK else 1
off = S0 + len(DEP) - 1   # indeks halaman PDF untuk halaman arab p adalah off + p
w.add_outline_item('Sampul', 0)
w.add_outline_item('Daftar Isi', S0 + DEP.index(('isi', 1)))
w.add_outline_item('Kata Pengantar', S0 + kp - 1)
for n in BAB:
    par = w.add_outline_item(f'Bab {n}  {JUDUL[n]}', off + MULAI[f'bab{n:02d}'])
    for k, t, i in SUB[n]: w.add_outline_item(f'{k} {t}', off + hal_bab(n, i), parent=par)
    w.add_outline_item('Ringkasan, pertanyaan, dan soal', off + hal_bab(n, AKHIR[n][0]), parent=par)
    w.add_outline_item('Jawaban dan pembahasan', off + hal_bab(n, AKHIR[n][1]), parent=par)
for x in sorted(LJ): w.add_outline_item(f'Lampiran {x}  {LJ[x][0]}', off + MULAI['lampiran'] + LJ[x][1])
w.add_outline_item('Indeks', off + MULAI['indeks'])
w.add_metadata({'/Title': 'Kimia Kuantum, Edisi Pertama', '/Author': 'Septian Anugrah Dwi Putra', '/Subject': 'Kimia kuantum untuk mahasiswa kimia'})
w.page_mode = '/UseOutlines'
out = f'{R}/Kimia-Kuantum-Edisi-1' + ('-cetak' if CETAK else '') + '.pdf'; w.write(out)
print('selesai:', out, len(w.pages), 'halaman; isi arab', hal - 1)
