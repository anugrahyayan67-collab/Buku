#!/usr/bin/env python3
# Pakai: sisip.py babNN  -> menyisipkan blok dari _tambahan.txt. Blok: "@@ berkas | penanda" lalu isi.
# Isi disisipkan sebelum kotak kuis terakhir sebelum penanda; penanda "AKHIR" = akhir berkas.
# Untuk _soal.txt: disisipkan tepat sebelum penanda.
import re,sys,os
d=sys.argv[1]; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..',d))
for m in re.finditer(r'@@ (\S+) \| (.*?)\n(.*?)(?=\n@@ |\Z)',open('_tambahan.txt').read(),re.S):
    f,mark,body=m.group(1),m.group(2).strip(),m.group(3).strip()+'\n\n'
    t=open(f).read(); i=len(t) if mark=='AKHIR' else t.index(mark)
    if f!='_soal.txt':
        k=t.rfind('::: {.kuis}',0,i)
        if mark=='AKHIR' or k>t.rfind('\n## ',0,i): i=k
        if mark=='AKHIR' and not t.endswith('\n\n'): pass
    t=t[:i]+body+t[i:]
    open(f,'w').write(t)
print('sisip selesai')
