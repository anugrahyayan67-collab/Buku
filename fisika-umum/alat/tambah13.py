#!/usr/bin/env python3
# Pakai: tambah13.py babNN berkas  -> menambah ringkasan/kuis/pertanyaan/soal/pembahasan ke c-akhir.md Bab 1-3
# Berkas berisi blok: @@RINGKASAN, @@KUIS, @@PERTANYAAN, @@SOAL (## judul / "teks ||| jawaban" / @kunci teks ||| jawaban), @@PEMBAHASAN ({{kunci}})
import re,sys,os,math
d,src=sys.argv[1],sys.argv[2]; f=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..',d,'c-akhir.md')
t=open(f).read(); B={m.group(1):m.group(2).strip() for m in re.finditer(r'@@(\w+)\n(.*?)(?=\n@@|\Z)',open(src).read(),re.S)}
if 'RINGKASAN' in B:
    head='| Gagasan | Isi | Subbab |\n|---|---|---|\n'; a=t.index(head)+len(head); b=a
    while t[b:b+1]=='|': b=t.index('\n',b)+1
    t=t[:b]+B['RINGKASAN']+'\n'+t[b:]
if 'KUIS' in B:
    i=t.index('## Jawaban kuis cepat'); j=t.index('\n# ',i); t=t[:j].rstrip('\n')+'\n\n'+B['KUIS']+'\n'+t[j:]
if 'PERTANYAAN' in B:
    i=t.index('# Pertanyaan'); j=t.index('\n# ',i+5); n=len(re.findall(r'^\d+\. ',t[i:j],re.M))
    it=[x for x in B['PERTANYAAN'].split('\n') if x.strip()]
    t=t[:j].rstrip('\n')+'\n'+''.join(f'{n+k+1}. {x}\n' for k,x in enumerate(it))+t[j:]
keys={}
if 'SOAL' in B:
    i=t.index('\n# Soal'); j=t.index('\n# Jawaban',i); n=max(int(x) for x in re.findall(r'^\*\*(\d+)\.\*\*',t[i:j],re.M))
    out=[]; rows=[]
    for line in B['SOAL'].split('\n'):
        if not line.strip(): continue
        if line.startswith('## '): out.append(line); continue
        if line.startswith('> '): out.append(line[2:]); continue
        k=None; m=re.match(r'@(\w+) (.*)',line)
        if m: k,line=m.group(1),m.group(2)
        q,a=[x.strip() for x in line.split('|||')]; n+=1
        if k: keys[k]=n
        out.append(f'**{n}.** {q}'); rows.append((n,a))
    t=t[:j].rstrip('\n')+'\n\n'+'\n\n'.join(out)+'\n'+t[j:]
    # tabel jawaban dibangun ulang
    i=t.index('::: {.panjang}'); j=t.index(':::',i+5)
    old=[]
    for line in t[i:j].split('\n'):
        m=re.match(r'^\|\s*(\d+)\s*\|(.*?)\|\s*(\d+|)\s*\|(.*)\|\s*$',line)
        if m:
            old.append((int(m.group(1)),m.group(2).strip()))
            if m.group(3): old.append((int(m.group(3)),m.group(4).strip()))
    rr=sorted(old+rows); h=math.ceil(len(rr)/2); tab=['| No. | Jawaban | No. | Jawaban |','|---|---|---|---|']
    for k in range(h):
        x=rr[k]; y=rr[k+h] if k+h<len(rr) else ('','')
        tab.append(f'| {x[0]} | {x[1]} | {y[0]} | {y[1]} |')
    t=t[:i]+'::: {.panjang}\n'+'\n'.join(tab)+'\n'+t[j:]
if 'PEMBAHASAN' in B:
    p=re.sub(r'\{\{(\w+)\}\}',lambda m:str(keys[m.group(1)]),B['PEMBAHASAN'])
    t=t.rstrip('\n')+'\n\n'+p+'\n'
open(f,'w').write(t); print(d,'soal baru',len(keys) if keys else '', 'ok')
