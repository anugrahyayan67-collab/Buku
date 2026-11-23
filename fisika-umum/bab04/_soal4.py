import re
C=open('_c1.md').read()
T={}  # tambahan per judul subbab: (teks, jawaban)
T['## Subbab 4.1']=[
("Seorang pendaki 65 kg naik dari perkemahan ke puncak yang 800 m lebih tinggi melalui jalur sepanjang 6,0 km. Berapa usaha gravitasi padanya?","$-5{,}1 \\times 10^5$ J"),
("Balok 10 kg ditarik naik dengan kelajuan tetap sejauh 4,0 m di bidang miring licin 20° oleh gaya yang sejajar bidang. Berapa gaya itu dan berapa usahanya?","33,5 N; 134 J"),
("Kabin lift 1000 kg yang sedang turun diperlambat $2{,}0\\ \\text{m/s}^2$ sejauh 15 m. Hitung usaha kabel, usaha gravitasi, dan usaha total pada kabin.","$-1{,}77 \\times 10^5$ J; $+1{,}47 \\times 10^5$ J; $-3{,}0 \\times 10^4$ J"),
("Gaya $\\vec F = (2{,}0\\,\\hat\\imath + 3{,}0\\,\\hat\\jmath - 1{,}0\\,\\hat k)$ N bekerja pada benda yang berpindah $\\vec d = (4{,}0\\,\\hat\\imath - 2{,}0\\,\\hat\\jmath + 5{,}0\\,\\hat k)$ m. Berapa usahanya?","$-3{,}0$ J"),
]
T['## Subbab 4.2']=[
("Gaya pada sebuah partikel adalah $F_x = 4{,}0x^3$ (N, dengan $x$ dalam meter). Berapa usahanya dari $x = 0$ sampai $x = 2{,}0$ m?","16 J"),
("Dua pegas, 200 N/m dan 300 N/m, ditarik dengan gaya 12 N. Tentukan konstanta efektif dan pertambahan panjang totalnya jika keduanya dipasang (a) paralel, (b) seri.","(a) 500 N/m; 2,4 cm; (b) 120 N/m; 10 cm"),
("Beban bandul 0,80 kg pada tali 2,0 m ditarik sangat perlahan dengan gaya mendatar sampai tali membentuk sudut 50° terhadap garis tegak. Berapa usaha gaya itu?","5,6 J"),
("Sebuah pegas tak linear memerlukan gaya $F = 100x + 500x^2$ (N, dengan $x$ dalam meter) untuk diregangkan sejauh $x$. Berapa usaha untuk meregangkannya dari 0 sampai 0,30 m?","9,0 J"),
]
T['## Subbab 4.3']=[
("Palu 1,5 kg dengan kelajuan 6,0 m/s memukul paku sehingga paku masuk 1,2 cm ke dalam kayu. Berapa gaya rata-rata pada paku?","$2{,}3 \\times 10^3$ N"),
("Seorang pengemudi memiliki waktu reaksi 0,80 s, dan remnya memberi perlambatan $6{,}5\\ \\text{m/s}^2$. Berapa jarak berhenti total pada kelajuan 72 km/jam?","47 m"),
("Seseorang bermassa 55 kg melompat turun dari ketinggian 0,80 m dan mendarat dengan menekuk lutut sehingga pusat massanya masih turun 0,25 m. Berapa gaya rata-rata lantai pada kakinya?","$2{,}3 \\times 10^3$ N"),
("Energi kinetik sebuah benda dijadikan tiga kali lipat. Berapa persen kelajuannya bertambah?","73%"),
("Proton (massa $1{,}67 \\times 10^{-27}$ kg) memiliki energi kinetik 5,0 MeV. Berapa kelajuannya? (1 MeV = $1{,}602 \\times 10^{-13}$ J.)","$3{,}1 \\times 10^7$ m/s"),
]
T['## Subbab 4.4']=[
("Mesin sebuah mobil 1000 kg memberi daya tetap 50 kW ke roda. Abaikan hambatan. (a) Berapa waktu untuk mencapai 30 m/s dari diam? (b) Berapa percepatannya pada kelajuan 20 m/s?","(a) 9,0 s; (b) $2{,}5\\ \\text{m/s}^2$"),
("Sebuah mobil memerlukan 12 kW untuk melawan hambatan udara pada 90 km/jam. Berapa daya yang diperlukan untuk melawan hambatan udara pada 120 km/jam?","28 kW"),
("Sebuah derek mengangkat beban 350 kg setinggi 20 m dalam 40 s sambil memakai daya listrik 2,4 kW. Berapa efisiensinya?","71%"),
("Saat berolahraga ringan, jantung memompa 6,0 liter darah per menit melawan tekanan rata-rata 16 kPa. Berapa daya mekaniknya?","1,6 W"),
("Sebuah mobil memerlukan 15 kW di roda untuk melaju tetap 25 m/s, dengan efisiensi keseluruhan 22%. Bensin menyimpan 34 MJ per liter. Berapa kilometer yang ditempuh per liter?","12,5 km"),
]
T['## Subbab 4.5 dan 4.6']=[
("Kereta halilintar mulai dari diam di ketinggian 30 m pada lintasan licin dan melewati dasar lembah (ketinggian nol) yang berjari-jari kelengkungan 12 m. Berapa gaya normal pada penumpang 70 kg di sana, dan berapa kali beratnya?","$4{,}1 \\times 10^3$ N; 6,0 kali"),
("**[P]** Kereta halilintar mulai dari diam di ketinggian 20 m pada lintasan licin, lalu melewati puncak bukit setinggi 8,0 m yang berjari-jari kelengkungan 15 m. (a) Apakah kereta tetap menempel di puncak bukit itu? (b) Berapa tinggi bukit paling rendah agar kereta tetap menempel?","(a) tidak; (b) 12,5 m"),
("Beban bandul dengan tali 1,2 m dilepas dari posisi tali mendatar. Sebuah paku dipasang tepat di bawah titik gantung. Berapa jarak paku paling kecil dari titik gantung agar beban dapat berputar satu lingkaran penuh mengelilingi paku?","0,72 m"),
("Peski meluncur dari diam menuruni lereng licin yang ujungnya mendatar, 18 m lebih rendah daripada titik awal dan 4,0 m di atas bidang pendaratan yang datar. Berapa jarak mendatar pendaratannya dari ujung lereng?","17 m"),
("Bola 0,30 kg diletakkan di atas pegas tegak ($k = 600$ N/m) yang ditekan 0,12 m, lalu dilepas. (a) Berapa kelajuan bola saat meninggalkan pegas? (b) Berapa tinggi terbesarnya di atas posisi awal?","(a) 5,1 m/s; (b) 1,5 m"),
("Seorang anak 30 kg di ayunan dilepas dari posisi tali membentuk sudut 50° terhadap garis tegak. Berapa tegangan total tali di titik terendah?","504 N"),
("Seorang anak mulai meluncur dari puncak kubah es licin berjari-jari 5,0 m. Pada ketinggian berapa dari dasar kubah ia lepas dari permukaan, dan berapa kelajuannya saat itu?","3,3 m; 5,7 m/s"),
("Sebuah pegas mengerjakan gaya $F_x = -60x - 400x^3$ (N, dengan $x$ dalam meter). Berapa energi potensialnya pada $x = 0{,}20$ m, jika $U(0) = 0$?","1,36 J"),
]
T['## Subbab 4.7']=[
("Mobil 1500 kg direm dari 30 m/s sampai berhenti. Seluruh energi kinetiknya memanaskan cakram rem besi bermassa total 20 kg (kalor jenis 450 J/(kg·K)). Berapa kenaikan suhu cakram?","75 K"),
("Air jatuh dari air terjun setinggi 100 m. Jika seluruh energi potensialnya menjadi energi termal air (kalor jenis 4186 J/(kg·K)), berapa kenaikan suhunya?","0,23 K"),
("Seorang atlet 70 kg melompat tegak. Selama mendorong lantai pusat massanya naik 0,30 m, dan setelah lepas dari lantai naik 0,45 m lagi. Berapa gaya rata-rata kakinya pada lantai selama mendorong?","$1{,}7 \\times 10^3$ N"),
("Kereta halilintar 400 kg dilepas dari diam di ketinggian 25 m dan tiba di permukaan tanah dengan kelajuan 20 m/s. Berapa energi yang berubah menjadi energi termal?","$1{,}8 \\times 10^4$ J"),
("**[P]** Balok dilepas dari diam dan meluncur turun sejauh 4,0 m di bidang miring 30°, lalu terus meluncur di lantai mendatar. Koefisien gesek kinetis di bidang miring dan di lantai sama, yaitu 0,20. Berapa jauh balok meluncur di lantai sebelum berhenti?","6,5 m"),
]
T['## Subbab 4.8']=[
("Untuk $U(x) = x^4 - 8x^2$ (J, dengan $x$ dalam meter), berapa konstanta pegas efektif untuk getaran kecil di sekitar $x = 2{,}0$ m?","32 N/m"),
("Untuk molekul H₂, parameter potensial Morse adalah $D = 4{,}75$ eV dan $a = 19{,}4\\ \\text{nm}^{-1}$. Berapa konstanta pegas ikatannya?","573 N/m"),
("Sebuah reaksi endoterm memiliki energi aktivasi 75 kJ/mol dan $\\Delta H = +40$ kJ/mol. Berapa energi aktivasi reaksi baliknya? Nyatakan kedua energi aktivasi itu dalam eV per molekul.","35 kJ/mol; 0,78 eV dan 0,36 eV"),
("Untuk potensial Lennard-Jones, gaya pada jarak $r = \\sigma$ adalah $24\\varepsilon/\\sigma$ dan bersifat tolak-menolak. Hitung besarnya untuk dua atom argon ($\\varepsilon = 1{,}65 \\times 10^{-21}$ J, $\\sigma = 0{,}340$ nm).","$1{,}2 \\times 10^{-10}$ N"),
]
BARU='''## Subbab 4.9: Gravitasi jarak jauh dan laju lepas

Gunakan $GM_\\text{Bumi} = 3{,}986 \\times 10^{14}\\ \\text{m}^3/\\text{s}^2$, $R_\\text{Bumi} = 6{,}37 \\times 10^6$ m, dan $G = 6{,}674 \\times 10^{-11}\\ \\text{N·m}^2/\\text{kg}^2$.

'''
T9=[
("Hitung laju lepas dari permukaan Mars ($M = 6{,}42 \\times 10^{23}$ kg, $R = 3{,}39 \\times 10^6$ m).","5,0 km/s"),
("**[P]** Sebuah proyektil ditembakkan tegak ke atas dari permukaan Bumi dengan kelajuan 5,0 km/s. Abaikan udara. Berapa ketinggian terbesarnya di atas permukaan?","1600 km"),
("Berapa energi paling sedikit untuk menempatkan satelit 500 kg dari keadaan diam di permukaan Bumi ke orbit lingkaran 300 km di atas permukaan?","$1{,}6 \\times 10^{10}$ J"),
("Sebuah meteoroid mula-mula hampir diam, sangat jauh dari Bumi, lalu jatuh ke Bumi. Abaikan udara dan benda langit lain. Berapa kelajuannya saat tiba di permukaan?","11,2 km/s"),
]
T10=[
("Berapa energi yang setara dengan massa 1,0 mg? Nyatakan dalam joule dan kWh.","$9{,}0 \\times 10^{10}$ J; 25 000 kWh"),
("Baterai menyimpan 12 Wh. Jika seluruh energinya dipakai untuk mengangkat orang 60 kg, seberapa tinggi orang itu terangkat?","73 m"),
("Pembakaran 1 mol metana melepas 890 kJ. Berapa massa yang hilang?","$9{,}9 \\times 10^{-12}$ kg"),
]
pre,rest=C.split('\n# Soal\n',1); soal,rest2=rest.split('\n# Jawaban\n',1); tab,pemb=rest2.split('\n## Pembahasan soal terpilih\n',1)
ans={}
for row in re.findall(r'^\|(.*)\|\s*$',tab,re.M):
    c=[x.strip() for x in row.split('|')]
    if len(c)==4 and c[0].isdigit():
        ans[int(c[0])]=c[1]
        if c[2].isdigit(): ans[int(c[2])]=c[3]
print(len(ans))
# pecah soal menjadi blok
parts=re.split(r'(?m)^(?=## )',soal); head=parts[0]; out=[head]; items=[]  # items: (old or None, text, answer)
seq=[]
for p in parts[1:]:
    title=p.split('\n',1)[0]; body=p.split('\n',1)[1]
    probs=re.findall(r'(?ms)^\*\*(\d+)\.\*\* (.*?)(?=\n\n|\Z)',body)
    lst=[(int(n),t,ans[int(n)]) for n,t in probs]
    add=[]
    for k,v in T.items():
        if title.startswith(k): add=[(None,t,a) for t,a in v]
    if title.startswith('## Soal gabungan'):
        seq.append((BARU.split('\n')[0],BARU.split('\n',1)[1].strip(),[(None,t,a) for t,a in T9]))
        seq.append(('## Subbab 4.10: Bentuk-bentuk energi','',[(None,t,a) for t,a in T10]))
    seq.append((title,'',lst+add))
n=0; m={}; txt=head; rows=[]
for title,intro,lst in seq:
    txt+=title+'\n\n'+(intro+'\n\n' if intro else '')
    for old,t,a in lst:
        n+=1
        if old: m[old]=n
        txt+=f'**{n}.** {t}\n\n'; rows.append((n,a))
print(n,m[43],m[63])
fix=lambda s: re.sub(r'Soal (\d+)',lambda k:'Soal %d'%m.get(int(k.group(1)),int(k.group(1))),s)
txt=re.sub(r'pada Soal (\d+)',lambda k:'pada Soal %d'%m[int(k.group(1))],txt)
half=(len(rows)+1)//2; tb='::: {.panjang}\n| No. | Jawaban | No. | Jawaban |\n|---|---|---|---|\n'
for i in range(half):
    l=rows[i]; r=rows[i+half] if i+half<len(rows) else ('','')
    tb+=f'| {l[0]} | {l[1]} | {r[0]} | {r[1]} |\n'
tb+=':::\n'
pemb=re.sub(r'\*\*Soal (\d+)\.\*\*',lambda k:'**Soal %d.**'%m[int(k.group(1))],pemb)
def no(snip):
    k=re.search(r'\*\*(\d+)\.\*\* [^\n]*'+re.escape(snip),txt); return int(k.group(1))
nb,ng,ni=no('puncak bukit setinggi 8,0 m'),no('lalu terus meluncur di lantai mendatar'),no('kelajuan 5,0 km/s')
pemb=pemb.rstrip()+f'''

**Soal {nb}.** (a) Kelajuan di puncak bukit: $v^2 = 2g(20 - 8{{,}}0) = 235\\ \\text{{m}}^2/\\text{{s}}^2$. Di puncak bukit, $mg - n = mv^2/R$. Kereta tetap menempel hanya jika $n \\ge 0$, yaitu $v^2 \\le gR = (9{{,}}80)(15) = 147\\ \\text{{m}}^2/\\text{{s}}^2$. Karena $235 > 147$, kereta lepas dari lintasan. (b) Syaratnya $2g(20 - h) \\le 147$, sehingga $h \\ge 20 - 7{{,}}5 = 12{{,}}5$ m.

*Cara berpikir:* di puncak bukit, berat adalah satu-satunya gaya yang dapat menarik kereta ke arah pusat kelengkungan. Jika kereta terlalu cepat, berat tidak cukup untuk membelokkannya, dan kereta terbang lurus. Bukit yang lebih tinggi memperlambat kereta, jadi justru lebih aman.

**Soal {ng}.** Ambil seluruh perjalanan sebagai satu proses: awal diam, akhir diam. Balok turun setinggi $4{{,}}0\\sin 30° = 2{{,}}0$ m. Seluruh energi potensial itu menjadi energi termal, sebagian di bidang miring (dengan $n = mg\\cos 30°$) dan sebagian di lantai (dengan $n = mg$):

$$
mg(2{{,}}0) = \\mu_kmg\\cos 30°\\,(4{{,}}0) + \\mu_kmg\\,D \\quad\\Longrightarrow\\quad D = \\frac{{2{{,}}0 - (0{{,}}20)(0{{,}}866)(4{{,}}0)}}{{0{{,}}20}} = \\frac{{2{{,}}0 - 0{{,}}69}}{{0{{,}}20}} = 6{{,}}5\\ \\text{{m}}.
$$

*Cara berpikir:* kelajuan di kaki bidang miring tidak perlu dihitung. Yang perlu diperhatikan hanyalah gaya normal yang berbeda di dua bagian lintasan, sehingga gaya geseknya juga berbeda.

**Soal {ni}.** Per kilogram: $\\tfrac12v^2 = 1{{,}}25 \\times 10^7$ J/kg dan $GM/R = 6{{,}}26 \\times 10^7$ J/kg. Kekekalan energi sampai titik tertinggi:

$$
\\frac{{GM}}{{r}} = \\frac{{GM}}{{R}} - \\tfrac12v^2 = 5{{,}}01 \\times 10^7\\ \\text{{J/kg}} \\quad\\Longrightarrow\\quad r = \\frac{{3{{,}}986 \\times 10^{{14}}}}{{5{{,}}01 \\times 10^7}} = 7{{,}}96 \\times 10^6\\ \\text{{m}}.
$$

Ketinggian: $h = r - R = 1{{,}}6 \\times 10^6$ m, atau 1600 km.

*Cara berpikir:* rumus $v^2/(2g)$ memberi 1280 km, meleset sekitar 20%. Makin tinggi lintasannya dibandingkan jari-jari Bumi, makin besar kesalahan anggapan $g$ tetap.
'''
pre=pre.replace('| Jembatan satuan kimia | 1 eV per partikel = 96,5 kJ/mol | 4.8 |','''| Jembatan satuan kimia | 1 eV per partikel = 96,5 kJ/mol | 4.8 |
| Pegas gabungan | paralel: $k = k_1 + k_2$; seri: $1/k = 1/k_1 + 1/k_2$ | 4.2 |
| Gaya rata-rata saat berhenti | $F = K/d$ | 4.3 |
| Gerak dengan daya tetap | $v = \\sqrt{2Pt/m}$ | 4.4 |
| Daya melawan hambatan udara | $P = \\tfrac12\\rho C_dAv^3$ | 4.4 |
| Efisiensi | $\\eta$ = keluaran berguna / masukan | 4.4 |
| Tegangan bandul di titik terendah | $T = mg(3 - 2\\cos\\theta_0)$ | 4.6 |
| Kenaikan suhu oleh energi termal | $\\Delta T = Q/(mc)$ | 4.7 |
| Konstanta pegas efektif | $k_\\text{ef} = d^2U/dx^2$ di titik minimum | 4.8 |
| Potensial Morse | $U = D(1 - e^{-a(r - r_0)})^2$, $\\ k_\\text{ef} = 2Da^2$ | 4.8 |
| Energi aktivasi reaksi balik | $E_a(\\text{balik}) = E_a(\\text{maju}) - \\Delta H$ | 4.8 |
| Energi potensial gravitasi umum | $U = -GMm/r$ | 4.9 |
| Laju lepas | $v_\\text{lepas} = \\sqrt{2GM/R}$; Bumi: 11,2 km/s | 4.9 |
| Orbit lingkaran | $v = \\sqrt{GM/r}$, $\\ E = -GMm/(2r)$ | 4.9 |
| Kesetaraan massa dan energi | $E_0 = mc^2$ | 4.10 |''')
assert '4.10 |' in pre
pre=pre.replace('inilah asal pemuaian zat ketika dipanaskan.','inilah asal pemuaian zat ketika dipanaskan. **4.9** Tidak jauh berbeda. Benda pertama tiba dengan $\\sqrt{GM/R} = 7{,}9$ km/s dan benda kedua dengan laju lepas, 11,2 km/s. Itulah kelajuan terbesar yang mungkin bagi benda yang jatuh dari keadaan diam. **4.10** Ya. Pegas yang ditekan menyimpan energi lebih banyak, jadi massanya lebih besar sebesar $\\Delta E/c^2$, sekitar $10^{-17}$ kg untuk energi 1 J. Selisih itu jauh di bawah kemampuan neraca mana pun.')
assert '**4.10** Ya' in pre
open('c-akhir.md','w').write(pre+'\n# Soal\n'+txt.rstrip()+'\n\n# Jawaban\n\n'+tb+'\n## Pembahasan soal terpilih\n'+pemb)
print(nb,ng,ni)
