#!/usr/bin/env python3
# Pemeriksaan otomatis naskah Kimia Anorganik 1.
# python3 alat/periksa.py          -> semua bab
# python3 alat/periksa.py 3 4      -> bab tertentu
# Memeriksa: rujukan silang, kelengkapan contoh/kuis, sebaran tingkat soal,
# ejaan tidak baku, sapaan, angka desimal bertitik, dan statistik isi.
import re, glob, os, sys
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BAB = [int(a) for a in sys.argv[1:]] or list(range(1, 14))
def teks(n, akhir=True):
    s = ''.join(open(f).read() for f in sorted(glob.glob(f'{R}/bab{n:02d}/[a-c]-*.md')))
    if akhir:
        for f in ('_akhir.md', '_soal.txt'):
            p = f'{R}/bab{n:02d}/{f}'
            if os.path.exists(p): s += open(p).read()
    return s
semua = {n: teks(n) for n in range(1, 14) if glob.glob(f'{R}/bab{n:02d}/a-*.md')}
ada = {k: set() for k in ('Contoh', 'Gambar', 'Tabel', 'subbab', 'pers')}
for n, s in semua.items():
    ada['Contoh'] |= {(n, int(k)) for k in re.findall(rf'\*\*Contoh {n}\.(\d+)', s)}
    ada['Gambar'] |= {(n, int(k)) for k in re.findall(rf'!\[Gambar {n}\.(\d+)', s)}
    ada['Tabel'] |= {(n, int(k)) for k in re.findall(rf'^Tabel {n}\.(\d+)', s, re.M)}
    ada['subbab'] |= {(n, int(k)) for k in re.findall(rf'^## {n}\.(\d+) ', s, re.M)}
    ada['pers'] |= {(n, int(k)) for k in re.findall(rf'\\text{{\({n}\.(\d+)\)}}', s)}
POLA = {'Contoh': r'Contoh (\d+)\.(\d+)', 'Gambar': r'Gambar (\d+)\.(\d+)', 'Tabel': r'Tabel (\d+)\.(\d+)',
        'subbab': r'subbab (\d+)\.(\d+)', 'pers': r'(?<![\\\w])\((\d+)\.(\d+)\)'}
TIDAKBAKU = r'\b(milyar\w*|praktek|analisa|resiko|nampak|merubah|dirubah|sekedar|jaman|aktifitas|obyek|sistim|ijin|silahkan|antar molekul|tsb)\b'
for n in BAB:
    if n not in semua: continue
    s, isi = semua[n], teks(n, False)
    print(f'== Bab {n}')
    for k, pola in POLA.items():
        for baris in s.splitlines():
          if 'Fisika Umum' in baris or 'Kimia Kuantum' in baris: continue   # rujukan ke buku lain
          for a, b in re.findall(pola, baris):
            a, b = int(a), int(b)
            if a in semua and (a, b) not in ada[k]: print(f'  rujukan {k} {a}.{b} tidak ada')
    for x in re.findall(r'\d+\.t\d+|\{\{\w+\}\}|%%\w+%%', isi): print('  label sementara tersisa:', x)
    blok = re.findall(r'::: \{\.contoh\}(.*?)\n:::', isi, re.S)
    for b in blok:
        if 'Memahami hasil' not in b: print('  contoh tanpa Memahami hasil:', b.strip()[:50])
    for sb in re.split(r'^## ', isi, flags=re.M)[1:]:
        j = sb.split('\n')[0]
        if re.match(r'\d+\.\d+', j):
            if '{.kuis}' not in sb: print('  subbab tanpa kuis:', j)
            if '{.contoh}' not in sb: print('  subbab tanpa contoh:', j)
    for m in re.finditer(TIDAKBAKU, isi, re.I): print('  ejaan tidak baku:', m.group(0))
    for m in re.finditer(r'\bAnda\b', isi): print('  sapaan "Anda" (pakai "kamu"/"kita"):', isi[max(0, m.start()-30):m.end()+20].replace('\n', ' '))
    for m in re.finditer(r'(?<![\d.\\{])\d+\.\d+(?![\d.])', re.sub(r'```.*?```|\$[^$]*\$|\(\d+\.\d+\)|Gambar \d+\.\d+|Tabel \d+\.\d+|Contoh \d+\.\d+|subbab \d+\.\d+|Kuis cepat \d+\.\d+|## \d+\.\d+|Bab \d+\.\d+|\d+\.\d+ [A-Z]', '', isi, flags=re.S)):
        a, b = m.group(0).split('.')
        if int(a) <= 13 and len(b) <= 2 and int(b) <= 25: continue   # hampir pasti nomor subbab/persamaan
        print('  kemungkinan desimal bertitik:', m.group(0))
    so = open(f'{R}/bab{n:02d}/_soal.txt').read()
    tk = [len(re.findall(rf'^\*\*{k}', so, re.M)) for k in ('Dasar', 'Menengah', 'Tantangan')]
    w = len(re.sub(r'\$\$.*?\$\$|\$[^$]*\$', '', isi, flags=re.S).split())
    print(f'  statistik: {w} kata, {isi.count("**Contoh ")} contoh, {so.count("|||")} soal ({so.count("★ ")} tantangan), '
          f'{isi.count("![Gambar")} gambar, kotak inti/dalam/terapan/awas = '
          + '/'.join(str(isi.count("{." + k + "}")) for k in ("inti", "dalam", "terapan", "awas")))
