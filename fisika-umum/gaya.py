import re,sys
f=sys.argv[1]; s=open(f).read()
def h1(m):
    a,t=m.group(1),re.sub(r'\s+',' ',m.group(2))
    b=re.match(r'Bab (\d+) (.*)',t)
    if b: return f'<h1{a} class="bab"><span class="pita"><span class="kata">Bab</span><span class="no">{b.group(1)}</span></span><span class="judul">{b.group(2)}</span></h1>'
    b=re.match(r'Bagian (\d+[AB]) (.*)',t)
    if b: return f'<h1{a} class="bagian"><span class="pita"><span class="kata">Bagian</span><span class="no">{b.group(1)}</span></span><span class="judul">{b.group(2)}</span></h1>'
    return f'<h1{a} class="pita1">{t}</h1>'
s=re.sub(r'<h1( id="[^"]*")>(.*?)</h1>',h1,s,flags=re.S)
def h2(m):
    a,t=m.group(1),m.group(2)
    c='sub' if re.match(r'\s*\d+\.\d+ ',t) else ('kecil' if re.match(r'\s*(Subbab|Soal gabungan|Proyek)',t) else '')
    return f'<h2{a} class="{c}">{t}</h2>' if c else m.group(0)
s=re.sub(r'<h2( id="[^"]*")>(.*?)</h2>',h2,s,flags=re.S)
s=re.sub(r'<strong>((?:Penyelesaian|Memahami hasil|Memahami soal|Gambaran fisis|Rencana|Kerjakan|Periksa|Pahami|Modelkan|Rencanakan|Langkah|Alat)\.)</strong>',r'<strong class="lk">\1</strong>',s)
s=re.sub(r'(<figcaption[^>]*>)\s*(Gambar\s+\d+\.\d+)',r'\1<span class="gb">\2</span>',s)
s=re.sub(r'<li>(<a href="#bab-\d)',r'<li class="t-bab">\1',s)
s=re.sub(r'<li>(<a href="#bagian-\d)',r'<li class="t-bagian">\1',s)
open(f,'w').write(s)
