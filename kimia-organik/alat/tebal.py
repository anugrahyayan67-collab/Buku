#!/usr/bin/env python3
# Menyisipkan blok tambahan ke akhir subbab (sebelum kuis subbab itu) dan soal tambahan ke _soal.txt.
# Pakai dari skrip lain: from tebal import sisip, soal
import re, glob, os
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
def sisip(n, k, teks, tanda):
    for f in sorted(glob.glob(f'{R}/bab{n:02d}/[a-y]-*.md')):
        s = open(f).read(); m = re.search(rf'^## {re.escape(k)} .*$', s, re.M)
        if not m: continue
        if tanda in s: return 'sudah'
        nxt = re.search(r'^## \d+\.\d+ ', s[m.end():], re.M); end = m.end() + nxt.start() if nxt else len(s)
        blok = s[m.end():end]; q = blok.rfind('::: {.kuis}')
        pos = m.end() + q if q >= 0 else end
        s = s[:pos] + teks.strip('\n') + '\n\n' + s[pos:]; open(f, 'w').write(s); return 'ok'
    raise SystemExit(f'subbab {k} tidak ditemukan')
def soal(n, k, baris):
    f = f'{R}/bab{n:02d}/_soal.txt'; s = open(f).read()
    m = re.search(rf'^## Subbab {re.escape(k)}:.*$', s, re.M)
    nxt = re.search(r'^## Subbab ', s[m.end():], re.M); end = m.end() + nxt.start() if nxt else len(s)
    blok = s[m.end():end]
    if baris[0][:40] in blok: return 'sudah'
    t = blok.find('**Tantangan'); pos = m.end() + t if t >= 0 else end
    ins = '\n'.join(baris) + '\n\n'
    if t < 0: ins = '\n' + ins
    s = s[:pos] + ins + s[pos:]; open(f, 'w').write(s); return 'ok'
