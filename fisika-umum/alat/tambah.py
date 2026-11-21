#!/usr/bin/env python3
# Pakai: tambah.py babNN berkas  (Bab 4-15). Blok: @@RINGKASAN (baris tabel), @@KUIS (teks sebaris), @@PERTANYAAN (satu per baris),
# @@SOAL (diteruskan ke akhir _soal.txt), @@PEMBAHASAN (ditambahkan di akhir _akhir.md)
import re,sys,os
d,src=sys.argv[1],sys.argv[2]; D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..',d)
B={m.group(1):m.group(2).strip() for m in re.finditer(r'@@(\w+)\n(.*?)(?=\n@@|\Z)',open(src).read(),re.S)}
a=open(f'{D}/_akhir.md').read()
if 'RINGKASAN' in B:
    i=a.index('|---|---|---|\n')+14; j=i
    while a[j:j+1]=='|': j=a.index('\n',j)+1
    a=a[:j]+B['RINGKASAN']+'\n'+a[j:]
if 'KUIS' in B:
    i=a.index('**Jawaban kuis cepat.**'); j=a.index('\n',i); a=a[:j].rstrip()+' '+B['KUIS']+a[j:]
if 'PERTANYAAN' in B:
    i=a.index('# Pertanyaan'); j=a.index('\n# ',i+5); n=len(re.findall(r'^\d+\. ',a[i:j],re.M))
    it=[x for x in B['PERTANYAAN'].split('\n') if x.strip()]
    a=a[:j].rstrip('\n')+'\n'+''.join(f'{n+k+1}. {x}\n' for k,x in enumerate(it))+a[j:]
if 'PEMBAHASAN' in B: a=a.rstrip('\n')+'\n\n'+B['PEMBAHASAN']+'\n'
open(f'{D}/_akhir.md','w').write(a)
if 'SOAL' in B:
    s=open(f'{D}/_soal.txt').read().rstrip('\n')+'\n\n'+B['SOAL']+'\n'; open(f'{D}/_soal.txt','w').write(s)
print(d,'ok')
