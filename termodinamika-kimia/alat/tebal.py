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
    if not m:
        judul = None
        for g in sorted(glob.glob(f'{R}/bab{n:02d}/[a-y]-*.md')):
            mm = re.search(rf'^## {re.escape(k)} (.*)$', open(g).read(), re.M)
            if mm: judul = mm.group(1); break
        s = s.rstrip('\n') + f'\n\n## Subbab {k}: {judul}\n'; open(f, 'w').write(s)
        m = re.search(rf'^## Subbab {re.escape(k)}:.*$', s, re.M)
    nxt = re.search(r'^## Subbab ', s[m.end():], re.M); end = m.end() + nxt.start() if nxt else len(s)
    blok = s[m.end():end]
    if baris[0][:40] in blok: return 'sudah'
    t = blok.find('**Tantangan'); pos = m.end() + t if t >= 0 else end
    ins = '\n'.join(baris) + '\n\n'
    if t < 0: ins = '\n' + ins
    s = s[:pos] + ins + s[pos:]; open(f, 'w').write(s); return 'ok'

def tanya(n, k, daftar):
    """Sisipkan pertanyaan konsep ke _akhir.md di bawah '## Subbab k: ...' (dibuat bila belum ada, urut), lalu nomori ulang."""
    f = f'{R}/bab{n:02d}/_akhir.md'; s = open(f).read()
    a = s.index('# Pertanyaan'); b = s.index('\n# Soal', a); blok = s[a:b]
    if daftar[0][:40] in blok: return 'sudah'
    m = re.search(rf'^## Subbab {re.escape(k)}:.*$', blok, re.M)
    if not m:
        judul = None
        for g in sorted(glob.glob(f'{R}/bab{n:02d}/[a-y]-*.md')):
            mm = re.search(rf'^## {re.escape(k)} (.*)$', open(g).read(), re.M)
            if mm: judul = mm.group(1); break
        kk = tuple(int(x) for x in k.split('.'))
        heads = [(tuple(int(x) for x in h.group(1).split('.')), h.start()) for h in re.finditer(r'^## Subbab (\d+\.\d+):', blok, re.M)]
        pos = next((p for t, p in heads if t > kk), len(blok))
        blok = blok[:pos].rstrip('\n') + f'\n\n## Subbab {k}: {judul}\n\n' + '\n'.join(f'1. {q}' for q in daftar) + '\n\n' + blok[pos:].lstrip('\n')
    else:
        nxt = re.search(r'^## Subbab ', blok[m.end():], re.M); end = m.end() + nxt.start() if nxt else len(blok)
        blok = blok[:end].rstrip('\n') + '\n' + '\n'.join(f'1. {q}' for q in daftar) + '\n\n' + blok[end:]
    c = [0]
    def num(mo): c[0] += 1; return f'{c[0]}. '
    blok = re.sub(r'^\d+\. ', num, blok, flags=re.M)
    s = s[:a] + blok.rstrip('\n') + '\n' + s[b:]; open(f, 'w').write(s); return f'ok ({c[0]})'

def bahas(n, teks):
    """Tambahkan pembahasan soal sebelum '# Bacaan lanjut'."""
    f = f'{R}/bab{n:02d}/_akhir.md'; s = open(f).read()
    if teks.strip()[:50] in s: return 'sudah'
    i = s.index('# Bacaan lanjut'); s = s[:i] + teks.strip() + '\n\n' + s[i:]; open(f, 'w').write(s); return 'ok'

def ringkas(n, baris, kuis=None):
    """Tambah baris tabel Ringkasan (sebelum baris kosong setelah tabel) dan jawaban kuis cepat."""
    f = f'{R}/bab{n:02d}/_akhir.md'; s = open(f).read()
    a = s.index('| Gagasan'); e = s.index('\n\n', a)
    tambah = [b for b in baris if b.split('|')[1].strip() not in s[a:e]]
    if tambah: s = s[:e] + '\n' + '\n'.join(tambah) + s[e:]
    if kuis:
        k, t = kuis
        if f'**{k}**' not in s:
            i = s.index('**Jawaban kuis cepat.**'); j = s.index('\n', i); s = s[:j] + f' **{k}** {t}' + s[j:]
    open(f, 'w').write(s); return 'ok'
