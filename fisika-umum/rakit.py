import re,os,glob,shutil,sys
SRC=os.path.expanduser('~/fisika-dasar'); DST=os.path.expanduser('~/fisika-umum')
NEW={1:(1,'A'),3:(1,'B'),2:(2,'A'),4:(2,'B'),5:(3,'A'),6:(3,'B')}
TITLES={1:'Pengukuran dan Vektor',2:'Kinematika',3:'Hukum Newton dan Penerapannya'}
KW=r'(Gambar|Contoh|Kuis cepat|Proyek|[Ss]ubbab|Terapan)'
NUM=re.compile(r'(?<![\d,.{}\w/])([1-6])\.(\d{1,2})(?![\d\w])')
def typ(s,m):
    pre=s[max(0,m.start()-60):m.start()]
    k=None
    for km in re.finditer(KW,pre):
        mid=pre[km.end():]
        if re.fullmatch(r'[\s\d.,()–\-]*((dan|sampai|atau|dan\s)[\s\d.,()–\-]*)*',mid): k=km.group(1)
    if k:
        k=k.lower()
        return {'gambar':'G','contoh':'C','kuis cepat':'K','proyek':'P'}.get(k,'S')
    if pre.endswith('(') and s[m.end():m.end()+1]==')': return 'E'
    return 'S'
def segs(text):
    # yield (is_code, chunk)
    out=[];code=False
    for line in text.split('\n'):
        if line.startswith('```'): code=not code; out.append((True,line)); continue
        if code: out.append((True,line)); continue
        parts=re.split(r'(`[^`]*`)',line)
        out.append((False,parts))
    return out
def scan(text,ch,mx):
    for c,p in segs(text):
        if c: continue
        for i,part in enumerate(p):
            if i%2: continue
            for m in NUM.finditer(part):
                if m.group(2).startswith('0') or int(m.group(1))!=ch: continue
                t=typ(part,m); mx[t]=max(mx.get(t,0),int(m.group(2)))
def read(ch): return [(f,open(f).read()) for f in sorted(glob.glob(f'{SRC}/bab{ch:02d}/[a-z]-*.md'))]
MAX={}
for ch in NEW:
    mx={}
    for f,t in read(ch): scan(t,ch,mx)
    MAX[ch]=mx
first={1:1,2:2,3:5}
def conv(text,log):
    res=[]
    for c,p in segs(text):
        if c: res.append(p); continue
        for i,part in enumerate(p):
            if i%2: continue
            def rep(m):
                if m.group(2).startswith('0'): return m.group(0)
                c0=int(m.group(1)); n,ab=NEW[c0]; t=typ(part,m); k=int(m.group(2))
                if ab=='B': k+=MAX[first[n]].get(t,0)
                return f'{n}.{k}'
            q=NUM.sub(rep,part)
            def bab(m):
                c0=int(m.group(1))
                if c0 in NEW: return 'Bagian %d%s'%NEW[c0]
                log.add(c0); return m.group(0)
            p[i]=re.sub(r'\bBab (\d+)\b',bab,q)
        res.append(''.join(p))
    return '\n'.join(res)
log=set()
for ch,(n,ab) in NEW.items():
    d=f'{DST}/bab{n:02d}'; os.makedirs(d+'/fig',exist_ok=True)
    for g in glob.glob(f'{SRC}/bab{ch:02d}/fig/*'):
        shutil.copy(g,f'{d}/fig/{ab.lower()}_{os.path.basename(g)}')
    for f,t in read(ch):
        t=re.sub(r'\n# Menuju Bab.*\Z','\n',t,flags=re.S)
        t=conv(t,log).replace('](fig/',f'](fig/{ab.lower()}_')
        open(f'{d}/{ab.lower()}-{os.path.basename(f)}','w').write(t)
print(MAX); print('rujukan luar:',sorted(log))
