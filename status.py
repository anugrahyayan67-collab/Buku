#!/usr/bin/env python3
# Ringkasan keadaan seri buku untuk awal sesi: python3 status.py
import re, glob, os, subprocess
R = os.path.dirname(os.path.abspath(__file__)); os.chdir(R)
def sh(c): return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.strip()
print('== Git:', sh('git branch --show-current'), '|', sh('git log --oneline -1'))
d = sh('git status --short | grep -v "_e2\\|\\.pdf$\\|_kerja" | head -5')
if d: print('   perubahan belum di-commit:\n' + d)
print('\n== Buku (RENCANA.md tiap folder)')
for f in sorted(glob.glob('*/RENCANA.md')):
    if f.startswith('kimia-dasar'): continue   # tidak dibuat (RENCANA-SERI.md)
    s = open(f).read(); bab = re.findall(r'^### (\S+) Bab (\d+) (.*)$', s, re.M)
    if not bab: continue
    done = sum(1 for b in bab if b[0] == '☑'); todo = [f'Bab {b[1]} {b[2][:40]}' for b in bab if b[0] != '☑']
    nbab = len(glob.glob(os.path.join(os.path.dirname(f), 'bab[0-9][0-9]')))
    print(f'  {os.path.dirname(f):22s} {done}/{len(bab)} bab ☑, {nbab} folder bab' + (f' | berikutnya: {todo[0]}' if todo else ''))
print('\n== PDF akhir di pdf/:', ', '.join(sorted(os.path.basename(p) for p in glob.glob('pdf/*.pdf'))))
print('\n== Pekerjaan berikutnya (PROMPT-AKUN-LAIN.md bagian 3): tiga butir terbuka pertama')
n = 0
for line in open('PROMPT-AKUN-LAIN.md'):
    m = re.match(r'\d+\. ([☐◐]) \*\*(.+?)\*\*', line)
    if m and n < 3: print(f'  {m.group(1)} {m.group(2)}'); n += 1
