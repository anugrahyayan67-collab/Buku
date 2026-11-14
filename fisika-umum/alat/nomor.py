#!/usr/bin/env python3
# Pakai: nomor.py babNN N  -> menomori ulang Contoh/Gambar/persamaan bab N menurut urutan muncul.
# Rujukan "Contoh N.k" / "Gambar N.k" / "persamaan (N.k)" di bab-bab lain ikut diperbarui.
import re,sys,os,glob
d,N=sys.argv[1],sys.argv[2]; root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'); os.chdir(os.path.join(root,d))
fs=sorted(f for f in glob.glob('[a-z]-*.md') if not f.startswith('c-akhir'))
fs+=[f for f in ('_akhir.md','_soal.txt') if os.path.exists(f)]
if not os.path.exists('_akhir.md'): fs.append('c-akhir.md')
txt=[open(f).read() for f in fs]; full='\n@@SPLIT@@\n'.join(txt)
maps={}
for typ,pat in [('C',r'\*\*Contoh %s\.(\w+) ·'%N),('G',r'!\[Gambar %s\.(\w+) '%N),('E',r'\\text\{\(%s\.(\w+)\)\}'%N)]:
    ids=[]
    for m in re.finditer(pat,full):
        if m.group(1) not in ids: ids.append(m.group(1))
    maps[typ]={o:str(i+1) for i,o in enumerate(ids)}
def lst(typ):
    return lambda m: re.sub(r'%s\.(\w+)'%N,lambda k:N+'.§'+maps[typ].get(k.group(1),'??'+k.group(1)),m.group(0))
def ganti(full,luar=False):
    full=re.sub(r'Contoh %s\.\w+(?:(?: dan |, | sampai )%s\.\w+)*'%(N,N),lst('C'),full)
    full=re.sub(r'Gambar %s\.\w+(?:(?: dan |, | sampai )%s\.\w+)*'%(N,N),lst('G'),full)
    pe=r'(?<=persamaan )\(%s\.(\w+)\)' if luar else r'\(%s\.(\w+)\)'
    full=re.sub(pe%N,lambda m:'('+N+'.§'+maps['E'].get(m.group(1),'??'+m.group(1))+')',full)
    return full
full=ganti(full)
bad=re.findall(r'\?\?\w+',full); assert not bad,bad
full=full.replace('§','')
for f,t in zip(fs,full.split('\n@@SPLIT@@\n')): open(f,'w').write(t)
for g in glob.glob(os.path.join(root,'bab[0-9][0-9]','*')):
    if os.path.basename(os.path.dirname(g))==d: continue
    b=os.path.basename(g)
    if not (re.match(r'[a-z]-.*\.md$',b) or b in ('_akhir.md','_soal.txt')): continue
    if b=='c-akhir.md' and os.path.exists(os.path.join(os.path.dirname(g),'_akhir.md')): continue
    t=open(g).read(); u=ganti(t,True)
    if '??' in u: print('?? rujukan tak dikenal di',g,re.findall(r'\?\?\w+',u)); continue
    u=u.replace('§','')
    if u!=t: open(g,'w').write(u); print('diperbarui',g)
print({k:len(v) for k,v in maps.items()})
