import re
A=open('_a.bak').read(); Bq=open('_b.bak').read(); C=open('_c.bak').read()
blk=dict((m.group(1),m.group(2).strip()+'\n\n') for m in re.finditer(r'@@(\w)\n(.*?)(?=\n@@|\Z)',open('_tambahan.txt').read(),re.S))
def ins(t,head,b):
    assert head in t,head; return t.replace(head,blk[b]+head,1)
A=ins(A,'## 4.2 ','A'); A=ins(A,'## 4.3 ','B'); A=ins(A,'## 4.4 ','C'); A=A.rstrip()+'\n\n'+blk['D']
Bq=ins(Bq,'## 4.6 ','E'); Bq=ins(Bq,'## 4.7 ','F'); Bq=ins(Bq,'## 4.8 ','G')
# H: bagian sebelum "## 4.9" masuk sebelum terapan+kuis 4.8? taruh di akhir 4.8, sebelum kotak terapan
h=blk['H']; h1,h2=h.split('## 4.9 ',1); h2='## 4.9 '+h2
Bq=ins(Bq,'::: {.terapan}\n**Kaitan kimia · Dari joule','_') if False else Bq.replace('::: {.terapan}\n**Kaitan kimia · Dari joule',h1+'::: {.terapan}\n**Kaitan kimia · Dari joule',1)
Bq=Bq.rstrip()+'\n\n'+h2
full=A+'\n@@SPLIT@@\n'+Bq+'\n@@SPLIT@@\n'+C
maps={}
for typ,pat in [('C',r'\*\*Contoh 4\.(\w+) ·'),('G',r'!\[Gambar 4\.(\w+) '),('E',r'\\text\{\(4\.(\w+)\)\}')]:
    ids=[]; 
    for m in re.finditer(pat,full):
        if m.group(1) not in ids: ids.append(m.group(1))
    maps[typ]={o:str(i+1) for i,o in enumerate(ids)}
    print(typ,len(ids))
def rl(typ):
    return lambda m: m.group(1)+'4.§'+maps[typ].get(m.group(2),'??'+m.group(2))+(m.group(3) or '')
def lst(typ,kw):
    def f(m):
        s=m.group(0); return re.sub(r'4\.(\w+)',lambda k:'4.§'+maps[typ].get(k.group(1),'??'+k.group(1)),s)
    return f
full=re.sub(r'Contoh 4\.\w+(?: dan 4\.\w+)?',lst('C','Contoh'),full)
full=re.sub(r'Gambar 4\.\w+(?: dan 4\.\w+)?',lst('G','Gambar'),full)
full=re.sub(r'\(4\.(\w+)\)',lambda m:'(4.§'+maps['E'].get(m.group(1),'??'+m.group(1))+')',full)
assert '??' not in full, re.findall(r'\?\?\w+',full)
full=full.replace('§','')
a,b,c=full.split('\n@@SPLIT@@\n')
open('a-usaha.md','w').write(a); open('b-energi.md','w').write(b); open('_c1.md','w').write(c)
