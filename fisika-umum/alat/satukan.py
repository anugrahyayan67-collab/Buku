#!/usr/bin/env python3
# Edisi 2: menyatukan Bab 1-3 (Bagian A/B) menjadi pola bab biasa seperti Bab 4-15.
# Pakai: satukan.py N   (membaca dari _ed1/babNN, menulis babNN/a-isi.md, b-isi.md, c-akhir.md)
import re, sys, os, glob, math
N = int(sys.argv[1]); R = os.path.expanduser('~/fisika-umum'); S = f'{R}/_ed1/bab{N:02d}'; D = f'{R}/bab{N:02d}'

def cat(pat): return '\n\n'.join(open(f).read().strip() for f in sorted(glob.glob(f'{S}/{pat}')))
def blocks(t):
    out = []; cur = None
    for line in t.split('\n'):
        if line.startswith('# '):
            cur = [line[2:].strip(), []]; out.append(cur)
        elif cur is not None: cur[1].append(line)
    return [(h, '\n'.join(b).strip()) for h, b in out]
def kind(h):
    for k in ['Bab', 'Bagian', 'Ringkasan', 'Soal', 'Proyek', 'Jawaban']:
        if h.startswith(k): return k
    raise SystemExit('?? ' + h)
def secs(t):  # preamble, [(judul, isi)]
    parts = re.split(r'^## (.*)$', t, flags=re.M)
    return parts[0].strip(), [(parts[i].strip(), parts[i+1].strip()) for i in range(1, len(parts), 2)]

A = blocks(cat('a-*.md')); B = blocks(cat('b-*.md'))
gA = {kind(h): (h, b) for h, b in A}; gB = {kind(h): (h, b) for h, b in B}
judul = gA['Bab'][0]

# ---- pembuka bab
intro = [p for p in gA['Bab'][1].split('\n\n') if not p.lstrip().startswith('|') and 'bagian' not in p.lower()]
isiA = gA['Bagian'][1]; isiB = gB['Bagian'][1]
isiA = re.sub(r'^## Peta bab\n.*?(?=^## )', '', isiA, flags=re.M | re.S)
isiA = re.sub(r'::: \{\.tujuan\}\n\*\*Prasyarat\*\*', '::: {.mat}\n**Prasyarat**', isiA)
# tujuan B digabung ke tujuan A
tb = re.search(r'::: \{\.tujuan\}\n\*\*Tujuan belajar\*\*.*?\n:::\n?', isiB, re.S)
itemB = re.findall(r'^\d+\. (.*)$', tb.group(0), re.M) if tb else []
isiB = isiB.replace(tb.group(0), '') if tb else isiB
isiB = re.sub(r'::: \{\.(?:tujuan|mat)\}\n\*\*Prasyarat\*\*.*?\n:::\n?', '', isiB, flags=re.S)
def addtuj(m):
    box = m.group(0); n = len(re.findall(r'^\d+\. ', box, re.M))
    add = ''.join(f'{n+i+1}. {x}\n' for i, x in enumerate(itemB))
    return re.sub(r'(\n:::\n?)$', '\n' + add.rstrip('\n') + r'\1', box.rstrip('\n') + '\n:::\n') if False else box[:box.rstrip().rfind(':::')].rstrip('\n') + '\n' + add + ':::\n'
isiA = re.sub(r'::: \{\.tujuan\}\n\*\*Tujuan belajar\*\*.*?\n:::\n?', addtuj, isiA, count=1, flags=re.S)
# kait B dipindah ke bawah judul subbab pertama B
i = isiB.find('\n## ')
kaitB, restB = isiB[:i].strip(), isiB[i+1:]
j = restB.find('\n'); h1B = restB[:j]; restB = restB[j+1:]
k1 = re.match(r'## (\d+\.\d+)', h1B).group(1)
kaitB = kaitB.replace('**Pertanyaan pembuka**', f'**Pertanyaan pembuka subbab {k1}**')
isiB = h1B + '\n\n' + kaitB + '\n\n' + restB

# ---- akhir bab
def ringk(t):
    pre, ss = secs(t); per = [b for h, b in ss if h.startswith('Pertanyaan konsep')]
    return pre, [(h, b) for h, b in ss if not h.startswith('Pertanyaan konsep')], per
preA, sA, pA = ringk(gA['Ringkasan'][1]); preB, sB, pB = ringk(gB['Ringkasan'][1])
preB = preB.replace('**Jawaban pertanyaan pembuka.**', f'**Jawaban pertanyaan pembuka subbab {k1}.**')
merged = []; dB = dict(sB); used = set()
for h, b in sA:
    if h in dB:
        b2 = dB[h]; used.add(h)
        if b.startswith('|') and b2.startswith('|') and b.split('\n')[0] == b2.split('\n')[0]:
            tA = b.split('\n\n')[0]; tB = b2.split('\n\n')[0]
            b = tA + '\n' + '\n'.join(tB.split('\n')[2:]) + b[len(tA):] + b2[len(tB):]
        else: b = b + '\n\n' + b2
    merged.append((h, b))
merged += [(h, b) for h, b in sB if h not in used]
ring = f'# Ringkasan Bab {N}\n\n' + '\n\n'.join(x for x in [preA, preB] if x) + '\n\n' + '\n\n'.join(f'## {h}\n\n{b}' for h, b in merged)
items = re.findall(r'^\*\*P\d+\.\*\*\s*(.*)$', '\n'.join(pA + pB), re.M)
pert = '# Pertanyaan\n\n' + '\n'.join(f'{i+1}. {x}' for i, x in enumerate(items))

def soal(t, off):
    pre, ss = secs(t)
    pre = re.sub(r'Tingkat kesulitan:[^.]*\.\s*', '', pre)
    body = '\n\n'.join(f'## {h}\n\n{b}' for h, b in ss)
    body = re.sub(r'^\*\*(\d+)\.\*\*\s*(?:•+\s*)?', lambda m: f'**{int(m.group(1))+off}.** ', body, flags=re.M)
    if off: body = re.sub(r'\b([Ss]oal) (\d+)\b', lambda m: f'{m.group(1)} {int(m.group(2))+off}', body)
    return pre, body
nA = max(int(x) for x in re.findall(r'^\*\*(\d+)\.\*\*', gA['Soal'][1], re.M))
preSA, bodyA = soal(gA['Soal'][1], 0); preSB, bodyB = soal(gB['Soal'][1], nA)
preSB = re.sub(r'Soal bertanda \*\*\[P\]\*\* dibahas lengkap\.\s*', '', preSB).strip()
if preSB: bodyB = re.sub(r'^(## .*\n)', lambda m: m.group(1) + '\n> ' + preSB + '\n', bodyB, count=1)
soalT = '# Soal\n\n' + preSA + '\n\n' + bodyA + '\n\n' + bodyB

def jaw(t, off):
    pre, ss = secs(t); d = dict(ss); rows = []
    for line in d['Jawaban akhir'].split('\n'):
        m = re.match(r'^\|\s*(\d+)\s*\|(.*?)\|\s*(\d+|)\s*\|(.*)\|\s*$', line)
        if m:
            rows.append((int(m.group(1)) + off, m.group(2).strip()))
            if m.group(3): rows.append((int(m.group(3)) + off, m.group(4).strip()))
    pb = d.get('Pembahasan soal terpilih', '')
    if off: pb = re.sub(r'\b([Ss]oal) (\d+)\b', lambda m: f'{m.group(1)} {int(m.group(2))+off}', pb)
    return rows, pb
rA, pbA = jaw(gA['Jawaban'][1], 0); rB, pbB = jaw(gB['Jawaban'][1], nA)
rows = sorted(rA + rB); h = math.ceil(len(rows) / 2)
tab = ['| No. | Jawaban | No. | Jawaban |', '|---|---|---|---|']
for i in range(h):
    a = rows[i]; b = rows[i+h] if i+h < len(rows) else ('', '')
    tab.append(f'| {a[0]} | {a[1]} | {b[0]} | {b[1]} |')
jawT = '# Jawaban\n\n::: {.panjang}\n' + '\n'.join(tab) + '\n:::\n\n## Pembahasan soal terpilih\n\n' + pbA + '\n\n' + pbB

FIX = [(' (lihat Proyek 2.2)', ''), ('Program lengkapnya ada di Proyek 2.3. ', ''), (' Proyek 2.5 mengajakmu menghitungnya sendiri.', ''),
       (' (Proyek 3.3)', '')]
def fx(t):
    for a, b in FIX: t = t.replace(a, b)
    return re.sub(r'\n{3,}', '\n\n', t).strip() + '\n'
for f in glob.glob(f'{D}/[a-z]-*.md'): os.remove(f)
open(f'{D}/a-isi.md', 'w').write(fx(f'# {judul}\n\n' + '\n\n'.join(intro) + '\n\n' + isiA))
open(f'{D}/b-isi.md', 'w').write(fx(isiB))
open(f'{D}/c-akhir.md', 'w').write(fx(ring + '\n\n' + pert + '\n\n' + soalT + '\n\n' + jawT))
print(N, 'soal', len(rows), 'pertanyaan', len(items), 'tujuanB', len(itemB))
