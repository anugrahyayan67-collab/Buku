import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from tebal import soal, tanya, bahas
N = 2
S = {
'2.1': ['Satu mol CO₂ dalam wadah 0,500 L pada 300 K bertekanan 40,0 bar. Hitung *Z* dan katakan gaya mana yang dominan. ||| 0,80; tarikan',
        'Helium 1,00 mol dalam 0,100 L pada 300 K bertekanan 32,4 bar. Hitung *Z*, lalu jelaskan mengapa nilainya lebih besar dari 1. ||| 1,30; volume molekul (tolakan) dominan, tarikan He sangat lemah',
        'Mengapa pada tekanan mendekati nol semua gas mempunyai *Z* = 1, apa pun jenisnya? ||| molekul sangat berjauhan; volume dan tarikan antarmolekul tidak berarti'],
'2.2': ['Untuk argon, σ = 0,3405 nm dan ε/*k* = 120 K. Hitung jarak kesetimbangan $r_\\text{min} = 2^{1/6}σ$ dan kedalaman sumur dalam J mol⁻¹. ||| 0,382 nm; 998 J mol⁻¹',
        'Bandingkan kedalaman sumur argon (≈ 1 kJ mol⁻¹) dengan *RT* pada 25 °C. Apa artinya bagi keadaan argon pada suhu kamar? ||| *RT* = 2,48 kJ mol⁻¹ > ε; tarikan tidak cukup untuk mengikat atom, argon gas',
        'Mengapa suku tolakan pada potensial Lennard-Jones dipilih berpangkat 12, sedangkan suku tarikan berpangkat 6? ||| tarikan dispersi memang ∝ $r^{-6}$; pangkat 12 pilihan praktis untuk tolakan yang sangat curam',
        'Urutkan kekuatan tarikan antarmolekul He, N₂, CO₂, dan jelaskan hubungannya dengan tetapan *a* van der Waals. ||| He < N₂ < CO₂; sama dengan urutan *a*'],
'2.3': ['Hitung tekanan 2,00 mol CH₄ dalam 1,00 L pada 300 K menurut van der Waals dan menurut gas ideal. ||| 45,4 bar; 49,9 bar',
        'Hitung tekanan 1,00 mol H₂ dalam 0,0500 L pada 300 K menurut van der Waals dan gas ideal. Mengapa van der Waals lebih besar? ||| 967 bar; 499 bar; volume molekul (*b*) menempati sebagian besar wadah',
        'Dari *b* argon (0,0320 L mol⁻¹) dan anggapan $b = 4N_\\text{A}\\cdot\\tfrac43\\pi(d/2)^3$, perkirakan diameter atom argon. ||| 0,29 nm',
        'Untuk N₂ pada 25 °C, berapa perbandingan *b*/$V_\\text{m}$ pada 1 bar dan pada 300 bar? Apa artinya? ||| 0,0016; 0,47; pada 300 bar hampir separuh ruang "terisi" molekul',
        'Hitung "tekanan dalam" $a/V_\\text{m}^2$ untuk CO₂ pada 1 bar dan 25 °C, dan bandingkan dengan tekanan gasnya. ||| 0,0059 bar; 0,6% dari tekanan'],
'2.4': ['Apa yang terjadi bila gas di bawah suhu kritisnya dimampatkan pada suhu tetap? Gambarkan bentuk isotermnya. ||| tekanan naik, lalu tetap selama gas mencair (garis datar), lalu naik tajam pada cairan',
        'Mengapa bagian isoterm van der Waals dengan $(\\partial p/\\partial V)_T > 0$ tidak dapat diwujudkan? ||| tekanan naik saat volume bertambah: tidak stabil mekanis',
        'Apa yang ditentukan oleh konstruksi Maxwell pada isoterm van der Waals? ||| tekanan uap: garis datar dengan dua luas sama'],
'2.5': ['Hitung $T_\\text{c}$, $p_\\text{c}$, dan $V_\\text{c}$ N₂ menurut van der Waals, lalu bandingkan dengan Tabel 2.2. ||| 126,2 K; 33,9 bar; 116 cm³ mol⁻¹ (terukur 126,2; 34,0; 90)',
        'Hitung $T_\\text{c}$ dan $p_\\text{c}$ He menurut van der Waals. ||| 5,18 K; 2,26 bar',
        'Faktor kompresi kritis $Z_\\text{c} = p_\\text{c}V_\\text{c}/RT_\\text{c}$ menurut van der Waals selalu 3/8. Hitung $Z_\\text{c}$ terukur N₂ dan CO₂ dari Tabel 2.2. ||| 0,292; 0,274 (van der Waals 0,375)',
        'Mengapa oksigen tidak dapat dicairkan pada suhu kamar berapa pun tekanannya? ||| suhu kamar di atas $T_\\text{c}$ O₂ (154,6 K)'],
'2.6': ['Argon pada 300 K dan 100 bar. Pada suhu dan tekanan berapa CO₂ berada dalam keadaan sehubungan? ||| 605 K; 152 bar',
        'Dari Gambar 2.6, perkirakan *Z* gas pada $T_r$ = 1,5 dan $p_r$ = 3. ||| ≈ 0,75',
        'Mengapa hukum keadaan sehubungan bekerja baik untuk Ar, N₂, dan CH₄ tetapi buruk untuk H₂O dan NH₃? ||| molekul polar dan berikatan hidrogen mempunyai bentuk potensial antarmolekul yang berbeda'],
'2.7': ['Hitung *Z* argon pada 273 K dan 50 bar dengan $B = -21{,}7$ cm³ mol⁻¹. ||| 0,952',
        'Hitung *Z* helium pada 273 K dan 100 bar dengan $B = +11{,}9$ cm³ mol⁻¹. ||| 1,052',
        'Hitung *Z* CO₂ pada 273 K dan 10 bar dari Tabel 2.3. ||| 0,934',
        'Hitung suhu Boyle Ar dan O₂ menurut van der Waals dan bandingkan dengan Tabel 2.3. ||| Ar 509 K (terukur 412); O₂ 521 K (terukur 406)',
        'Menurut van der Waals, perbandingan $T_\\text{B}/T_\\text{c}$ sama untuk semua gas. Berapa nilainya? ||| 27/8 = 3,375'],
'2.8': ['Hitung volume molar dan *Z* metana pada 250 K dan 92,0 bar dengan persamaan Redlich–Kwong ($a = 0{,}427\\,48\\,R^2T_\\text{c}^{2{,}5}/p_\\text{c}$, $b = 0{,}086\\,64\\,RT_\\text{c}/p_\\text{c}$; $T_\\text{c}$ = 190,6 K, $p_\\text{c}$ = 46,0 bar). ||| 0,161 L mol⁻¹; *Z* = 0,71',
        'Apa keunggulan persamaan kubik seperti Peng–Robinson dibanding persamaan virial untuk perhitungan teknik? ||| berlaku sampai cairan dan dekat titik kritis; cukup dua tetapan dari $T_\\text{c}$, $p_\\text{c}$ (dan ω)',
        'Mengapa semua persamaan kubik dapat mempunyai tiga akar *V* untuk satu pasang (*T*, *p*)? Akar mana yang dipakai untuk gas? ||| persamaan pangkat tiga dalam *V*; akar terbesar untuk gas, terkecil untuk cair'],
'2.9': ['CO₂ pada 25 °C dimuaikan dari 50 atm ke 1 atm melalui katup. Perkirakan perubahan suhunya dengan μ$_\\text{JT}$ = 1,11 K atm⁻¹. ||| ≈ −54 K (cukup untuk membentuk "salju" CO₂)',
        'Mengapa helium yang dimuaikan melalui katup pada suhu kamar justru memanas? ||| suhu kamar di atas suhu inversi He (40 K)',
        'Mengapa proses Joule–Thomson berlangsung pada entalpi tetap, bukan pada energi dalam tetap? ||| kerja dorong *pV* di kedua sisi katup ikut dihitung; $\\Delta U + \\Delta(pV) = 0$',
        'Hitung suhu inversi atas He menurut van der Waals, $2a/Rb$, dan bandingkan dengan Tabel 2.4. ||| 35 K (terukur 40 K)'],
'2.10': ['Dengan persamaan Peng–Robinson (ω = 0,225), massa jenis CO₂ pada 40 °C dan 100 bar adalah 563 g L⁻¹. Bandingkan dengan gas ideal dan jelaskan perbedaannya. ||| ideal 169 g L⁻¹; fluida superkritis serapat cairan',
        '@super [P] Mengapa CO₂ superkritis dipakai untuk menghilangkan kafein dari biji kopi, padahal pelarut organik seperti diklorometana juga melarutkan kafein? Sebutkan tiga alasan termodinamika dan praktisnya. ||| daya larut dapat disetel dengan *p*; dilepas cukup dengan menurunkan tekanan tanpa sisa; tidak beracun dan suhu kritis rendah (31 °C)',
        'Mengapa air superkritis (di atas 374 °C dan 221 bar) dapat melarutkan minyak, padahal air biasa tidak? ||| ikatan hidrogen melemah, tetapan dielektrik turun tajam; air menjadi "pelarut nonpolar"'],
}
for k, b in S.items(): print(k, soal(N, k, b))
print(tanya(N, '2.1', ['Apakah *Z* < 1 berarti molekul gas lebih kecil daripada yang dibayangkan? Jelaskan arti fisis *Z* < 1 dan *Z* > 1.']))
print(tanya(N, '2.3', ['Mengapa koreksi tarikan van der Waals berbentuk $a(n/V)^2$, yaitu sebanding dengan kuadrat konsentrasi, bukan dengan konsentrasi biasa?']))
print(tanya(N, '2.6', ['Apa yang "sama" dari dua gas yang berada dalam keadaan sehubungan, dan mengapa kesamaan itu masuk akal dari bentuk potensial antarmolekulnya?']))
print(tanya(N, '2.9', ['Pemuaian bebas ke ruang hampa dan pemuaian melalui katup sama-sama tanpa kalor. Apa beda keduanya, dan mengapa gas ideal tidak berubah suhu pada keduanya?']))
print(tanya(N, '2.10', ['Bagaimana mungkin berpindah dari gas ke cair tanpa pernah melihat pendidihan atau pengembunan? Gambarkan jalurnya pada diagram fasa.']))
print(bahas(N, r'''**Soal {{super}}.** (1) *Daya larut dapat disetel.* Sedikit di atas titik kritis, massa jenis CO₂ superkritis berubah besar dengan perubahan kecil tekanan (bandingkan Contoh 2.12 dan Gambar 2.7). Daya larut zat terlarut naik bersama massa jenis pelarut, sehingga operator dapat memilih tekanan yang melarutkan kafein tetapi hampir tidak melarutkan senyawa aroma. (2) *Pemisahan mudah.* Setelah ekstraksi, tekanan diturunkan; CO₂ kembali menjadi gas, dan kafein mengendap tanpa sisa pelarut. Pelarut organik harus diuapkan dan selalu meninggalkan jejak. (3) *Aman dan lembut.* Suhu kritis CO₂ hanya 31 °C, sehingga ekstraksi berlangsung pada suhu yang tidak merusak biji kopi; CO₂ tidak beracun, tidak mudah terbakar, dan murah.

*Cara berpikir:* pertanyaan "mengapa memakai pelarut X" dijawab dengan membandingkan **sifat yang dapat diatur** dan **biaya memisahkan pelarut** setelahnya. Fluida superkritis istimewa karena satu variabel, tekanan, mengatur daya larut secara kontinu. Gagasan yang sama muncul lagi di Bab 10 dan 11: sifat larutan bergantung pada interaksi zat terlarut dengan pelarut, dan interaksi itu bergantung pada kerapatan pelarut.'''))
