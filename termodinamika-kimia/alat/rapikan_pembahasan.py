#!/usr/bin/env python3
# Memindahkan blok "**Soal {{kunci}}.**" yang tertempel sesudah "# Bacaan lanjut"
# ke bagian "# Pembahasan soal terpilih", lalu mengurutkan semua blok menurut urutan soal.
# Pakai: python3 alat/rapikan_pembahasan.py babNN
import re, sys, os
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', sys.argv[1])
A = open(f'{d}/_akhir.md').read()
urut = re.findall(r'^@(\w+) ', open(f'{d}/_soal.txt').read(), re.M)
kepala, sisa = A.split('# Pembahasan soal terpilih', 1)
pemb, bacaan = sisa.split('# Bacaan lanjut', 1)
m = re.search(r'^\*\*Soal \{\{', bacaan, re.M)
if m: pemb, bacaan = pemb.rstrip() + '\n\n' + bacaan[m.start():], bacaan[:m.start()]
m = re.search(r'^\*\*Soal \{\{', pemb, re.M)
awal, isi = pemb[:m.start()], pemb[m.start():]
blok = re.split(r'(?m)^(?=\*\*Soal \{\{)', isi)
blok = [b.strip() for b in blok if b.strip()]
blok.sort(key=lambda b: urut.index(re.match(r'\*\*Soal \{\{(\w+)', b).group(1)))
A = kepala + '# Pembahasan soal terpilih' + awal + '\n\n'.join(blok) + '\n\n# Bacaan lanjut' + bacaan.rstrip() + '\n'
open(f'{d}/_akhir.md', 'w').write(A)
print(sys.argv[1], [re.match(r'\*\*Soal \{\{(\w+)', b).group(1) for b in blok])
