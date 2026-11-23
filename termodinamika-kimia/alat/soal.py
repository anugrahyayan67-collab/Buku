#!/usr/bin/env python3
# Pakai: soal.py babNN  -> membaca _soal.txt dan _akhir.md, menulis z-akhir.md
import re,sys,os
d=sys.argv[1]; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..',d))
out=[];rows=[];keys={};n=0
for line in open('_soal.txt').read().split('\n'):
    if not line.strip(): continue
    if line.startswith('## '): out.append(line+'\n'); continue
    if line.startswith('> '): out.append(line[2:]+'\n'); continue
    k=None; m=re.match(r'@(\w+) (.*)',line)
    if m: k,line=m.group(1),m.group(2)
    
    if "|||" not in line: out.append(line+"\n"); continue
    t,a=[x.strip() for x in line.split('|||')]
    n+=1
    if k: keys[k]=n
    out.append(f'**{n}.** {t}\n'); rows.append((n,a))
half=(len(rows)+1)//2; tb='::: {.panjang}\n| No. | Jawaban | No. | Jawaban |\n|---|---|---|---|\n'
for i in range(half):
    l=rows[i]; r=rows[i+half] if i+half<len(rows) else ('','')
    tb+=f'| {l[0]} | {l[1]} | {r[0]} | {r[1]} |\n'
tb+=':::\n'
s='\n'.join(out)
A=open('_akhir.md').read()
sub=lambda x: re.sub(r'\{\{(\w+)\}\}',lambda m:str(keys[m.group(1)]),x)
A=A.replace('%%SOAL%%',sub(s)).replace('%%JAWABAN%%',tb); A=sub(A)
open('z-akhir.md','w').write(A); print(d,'soal:',n)
