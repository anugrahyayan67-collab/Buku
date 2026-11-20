#!/usr/bin/env python3
# Mengelompokkan "Pertanyaan" akhir bab per subbab (seperti bagian Soal).
# Pakai:  python3 kelompok_tanya.py DIR_BUKU NN            -> tampilkan usulan
#         python3 kelompok_tanya.py DIR_BUKU NN tulis      -> tulis ke babNN/_akhir.md
#         python3 kelompok_tanya.py DIR_BUKU NN tulis 1:1,2:1,3:2,...   -> tulis dengan penempatan manual (nomor:subbab)
# Penempatan otomatis: kemiripan kata (TF-IDF) dengan teks tiap subbab, dengan urutan tak menurun.
import re, sys, glob, math, os
from collections import Counter
D, N = sys.argv[1], int(sys.argv[2]); TULIS = len(sys.argv) > 3 and sys.argv[3] == 'tulis'
MANUAL = dict(map(int, p.split(':')) for p in sys.argv[4].split(',')) if len(sys.argv) > 4 else {}
bab = f'{D}/bab{N:02d}'
src = ''.join(open(f).read() for f in sorted(glob.glob(f'{bab}/[a-y]-*.md')) if 'akhir' not in f)
subs = [(int(k), j.strip(), t) for k, j, t in re.findall(r'^## \d+\.(\d+) (.*?)\n(.*?)(?=^## |\Z)', src, re.M | re.S)]
fa = f'{bab}/_akhir.md' if os.path.exists(f'{bab}/_akhir.md') else f'{bab}/c-akhir.md'; A = open(fa).read()
m = re.search(r'^# Pertanyaan\n(.*?)(?=^# )', A, re.M | re.S)
blok = m.group(1)
if '## Subbab' in blok: sys.exit('sudah dikelompokkan')
qs = re.findall(r'^(\d+)\. (.*)$', blok, re.M)
tok = lambda s: [w for w in re.findall(r'[a-zà-ÿ]{4,}', re.sub(r'\$[^$]*\$', ' ', s.lower()))]
docs = [Counter(tok(j + ' ' + j + ' ' + t)) for _, j, t in subs]
df = Counter(w for d in docs for w in d)
idf = {w: math.log((len(docs) + 1) / (c + 0.5)) for w, c in df.items()}
def sim(q, d):
    return sum(min(c, 3) * idf.get(w, 0) * math.log(1 + d[w]) for w, c in Counter(tok(q)).items())
S = [[sim(q, d) for d in docs] for _, q in qs]
# DP urutan tak menurun
nq, ns = len(qs), len(subs); best = [[-1e9] * ns for _ in range(nq)]; back = [[0] * ns for _ in range(nq)]
for j in range(ns): best[0][j] = S[0][j]
for i in range(1, nq):
    run, arg = -1e9, 0
    for j in range(ns):
        if best[i - 1][j] > run: run, arg = best[i - 1][j], j
        best[i][j] = run + S[i][j]; back[i][j] = arg
j = max(range(ns), key=lambda k: best[-1][k]); asg = [0] * nq
for i in range(nq - 1, -1, -1): asg[i] = j; j = back[i][j]
asg = [subs[a][0] for a in asg]
for i, (no, q) in enumerate(qs):
    if int(no) in MANUAL: asg[i] = MANUAL[int(no)]
if not TULIS:
    for (no, q), a in zip(qs, asg): print(f'{no:>3} -> {N}.{a}  {q[:95]}')
    sys.exit()
judul = {k: j for k, j, _ in subs}
out, cur = [], None
for (no, q), a in sorted(zip(qs, asg), key=lambda x: (x[1], int(x[0][0]))):
    if a != cur: out.append(f'\n## Subbab {N}.{a}: {judul[a]}\n'); cur = a
    out.append(f'{no}. {q}')
baru = '\n'.join(out).strip('\n') + '\n\n'
# nomor ulang berurutan setelah pengelompokan
k = [0]
def nomor(mm): k[0] += 1; return f'{k[0]}. '
baru = re.sub(r'^\d+\. ', nomor, baru, flags=re.M)
A = A[:m.start(1)] + '\n' + baru + A[m.end(1):]
open(fa, 'w').write(A); print('ditulis', fa)
