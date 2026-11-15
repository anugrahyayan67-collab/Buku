## 15.10 Laser

### Penguatan cahaya

**Laser** (*light amplification by stimulated emission of radiation*) memanfaatkan emisi terangsang (subbab 15.1). Foton yang melewati medium dengan $N_2$ molekul di tingkat atas dan $N_1$ di tingkat bawah akan diserap dengan laju sebanding dengan $N_1$ dan memicu emisi terangsang dengan laju sebanding dengan $N_2$ (untuk $g_1 = g_2$). Hukum Beer–Lambert (15.5) dengan serapan bersih menjadi

$$
I(x) = I_0e^{\sigma(N_2 - N_1)x} . \qquad \text{(15.35)}
$$

Bila $N_2 > N_1$, eksponennya positif: cahaya **diperkuat** saat melewati medium. Keadaan ini, **inversi populasi**, tidak pernah terjadi dalam kesetimbangan termal, karena berarti suhu "negatif" dalam sebaran Boltzmann. Ia harus diciptakan dengan memompa energi ke medium. Foton-foton yang dihasilkan emisi terangsang adalah salinan foton pemicunya: frekuensi, arah, fase, dan polarisasinya sama. Itulah asal sifat-sifat istimewa cahaya laser.

### Tiga tingkat dan empat tingkat

Contoh 15.4 menunjukkan bahwa sistem dua tingkat tidak dapat dibalik populasinya dengan pemompaan optis. Laser memerlukan lebih banyak tingkat (Gambar 15.8):

- **Laser tiga tingkat** (rubi, laser pertama, Maiman 1960). Cr³⁺ dipompa dengan lampu kilat dari keadaan dasar $^4A_2$ ke pita lebar $^4T_2$ dan $^4T_1$, lalu dalam beberapa pikodetik meluruh tanpa radiasi ke $^2E$ yang berumur sekitar 3 ms (subbab 14.11). Laser bekerja pada transisi $^2E \to {}^4A_2$ (694,3 nm). Karena tingkat bawah laser adalah keadaan dasar, lebih dari separuh ion Cr³⁺ harus dipindahkan ke $^2E$ sebelum ada penguatan. Pemompaannya berat, dan rubi biasanya bekerja dalam pulsa.
- **Laser empat tingkat** (Nd:YAG, He–Ne, zat warna, titanium-safir). Transisi laser berakhir pada tingkat yang berada cukup jauh di atas keadaan dasar dan cepat dikosongkan. Tingkat bawah laser hampir kosong, sehingga sedikit saja populasi di tingkat atas sudah memberi inversi. Ambang lasernya jauh lebih rendah.

![Gambar 15.8 (a) Skema laser tiga tingkat (rubi) dan (b) empat tingkat (Nd:YAG). Panah tebal: pemompaan; panah bergelombang: peluruhan tanpa radiasi yang cepat; panah merah: transisi laser. (c) Mode longitudinal rongga ($\Delta\nu = c/2L$) di bawah kurva penguatan medium; hanya mode yang penguatannya melebihi kerugian (garis putus-putus) yang berosilasi.](fig/c_laser.png){width=94%}

### Rongga resonator dan syarat ambang

Penguatan dalam sekali lewat biasanya kecil, sehingga medium ditempatkan di antara dua cermin: satu memantulkan hampir 100%, yang lain sedikit tembus untuk mengeluarkan berkas. Cahaya bolak-balik berkali-kali dan diperkuat setiap kali lewat. Laser mulai berosilasi bila penguatan satu putaran melebihi kerugian. Untuk medium sepanjang $L$ dengan cermin berpantulan $R_1$ dan $R_2$:

$$
R_1R_2e^{2\sigma\Delta NL} \ge 1 \quad\Longrightarrow\quad \Delta N_\text{ambang} = -\frac{\ln(R_1R_2)}{2\sigma L} . \qquad \text{(15.36)}
$$

Rongga juga memilih frekuensi. Hanya gelombang yang membentuk gelombang berdiri di antara cermin, dengan panjang rongga sama dengan kelipatan setengah panjang gelombang, yang dapat bertahan. Frekuensi **mode longitudinal** ini berjarak

$$
\Delta\nu_\text{mode} = \frac{c}{2L} . \qquad \text{(15.37)}
$$

Banyaknya mode yang berosilasi bergantung pada lebar kurva penguatan medium, yang pada laser gas ditentukan oleh lebar Doppler (subbab 15.3).

::: {.contoh}
**Contoh 15.40 · Ambang laser Nd:YAG**

Penampang lintang emisi terangsang Nd³⁺ dalam YAG pada 1064 nm adalah $2{,}8 \times 10^{-19}$ cm². Batang sepanjang 10 cm ditempatkan di antara cermin $R_1 = 1{,}00$ dan $R_2 = 0{,}95$. (a) Hitung inversi ambang. (b) Bandingkan dengan konsentrasi Nd³⁺ ($1{,}38 \times 10^{20}$ cm⁻³ untuk doping 1%). (c) Berapa yang diperlukan rubi tiga tingkat dengan $1{,}6 \times 10^{19}$ ion Cr³⁺ per cm³?

**Penyelesaian.** (a) $\Delta N = -\ln(0{,}95)/(2 \times 2{,}8 \times 10^{-19} \times 10) = 0{,}0513/5{,}6 \times 10^{-18} = 9{,}2 \times 10^{15}$ cm⁻³. (b) Fraksi $9{,}2 \times 10^{15}/1{,}38 \times 10^{20} = 6{,}6 \times 10^{-5}$. (c) Lebih dari separuh: lebih dari $8 \times 10^{18}$ ion per cm³ harus dieksitasi.

**Memahami hasil.** Laser empat tingkat cukup mengeksitasi satu dari lima belas ribu ion Nd³⁺; laser tiga tingkat harus mengeksitasi setengah dari seluruh ion Cr³⁺, hampir sepuluh ribu kali lebih banyak per ion. Itulah sebabnya hampir semua laser kontinu adalah sistem empat tingkat, dan laser Nd:YAG (sering dengan penggandaan frekuensi ke 532 nm, cahaya hijau penunjuk laser) menjadi kuda kerja laboratorium dan industri.
:::

::: {.contoh}
**Contoh 15.41 · Mode laser He–Ne**

Laser He–Ne (632,8 nm) mempunyai rongga sepanjang 30 cm. Gas neon (massa 20,18 u) di dalamnya bersuhu sekitar 400 K. (a) Hitung jarak antarmode. (b) Hitung lebar Doppler garis penguatan. (c) Berapa banyak mode yang dapat berosilasi?

**Penyelesaian.** (a) $c/2L = 3{,}00 \times 10^8/0{,}60 = 500$ MHz. (b) Dengan (15.11): $\Delta\nu_D = 1{,}51$ GHz. (c) Sekitar $1510/500 \approx 3$ mode.

**Memahami hasil.** Laser He–Ne biasa memancarkan dua atau tiga frekuensi sekaligus yang berjarak 500 MHz. Untuk mendapatkan satu frekuensi saja, rongga dibuat lebih pendek (agar hanya satu mode berada di bawah kurva penguatan) atau dipasang etalon pemilih mode. Laser frekuensi tunggal dengan lebar garis beberapa kilohertz memungkinkan spektroskopi yang ketelitiannya jauh melampaui lebar Doppler.
:::

### Sifat cahaya laser

Cahaya laser berbeda dari cahaya lampu dalam empat hal yang semuanya berasal dari emisi terangsang dan rongga resonator:

1. **Monokromatis.** Lebar garis dapat mencapai beberapa kilohertz, jauh lebih sempit daripada lebar Doppler.
2. **Koheren.** Fasenya teratur dalam ruang dan waktu. Panjang koherensi $l_c = c/\Delta\nu$ mencapai ratusan meter untuk laser frekuensi tunggal, dibanding beberapa mikrometer untuk LED.
3. **Terarah.** Berkas menyebar dengan sudut sekitar $\lambda/\pi w_0$, dengan $w_0$ jari-jari pinggang berkas; berkas He–Ne berjari-jari 0,5 mm hanya menyebar 0,4 mrad.
4. **Intens.** Seluruh daya terkumpul dalam rentang frekuensi dan sudut yang sangat kecil. Pulsa dapat dipadatkan sampai femtodetik, dengan daya puncak terawatt.

Laser pulsa ultrasingkat dibuat dengan **penguncian mode**: bila banyak mode longitudinal berosilasi dengan fase yang terkunci satu sama lain, interferensinya menghasilkan satu pulsa yang bolak-balik di dalam rongga, dan berkas keluar sebagai deretan pulsa berjarak $2L/c$. Makin banyak mode yang terkunci, makin singkat pulsanya. Hubungan transformasi Fourier menetapkan batas bawah: untuk pulsa berbentuk Gauss,

$$
\Delta\nu\,\Delta t \ge 0{,}441 . \qquad \text{(15.38)}
$$

::: {.contoh}
**Contoh 15.42 · Lebar spektrum pulsa femtodetik**

Laser titanium-safir menghasilkan pulsa 10 fs di sekitar 800 nm. Hitung lebar spektrum minimumnya dalam THz, cm⁻¹, dan nm. Berapa lebar spektrum pulsa 100 fs?

**Penyelesaian.** $\Delta\nu = 0{,}441/10^{-14}\ \text{s} = 44{,}1$ THz $= 1470$ cm⁻¹. Dalam panjang gelombang, $\Delta\lambda = \lambda^2\Delta\nu/c = (800\ \text{nm})^2(4{,}41 \times 10^{13})/(3{,}00 \times 10^{17}\ \text{nm/s}) = 94$ nm. Untuk 100 fs: 147 cm⁻¹.

**Memahami hasil.** Pulsa 10 fs bukan "satu warna": ia membentang hampir 100 nm. Lebarnya, 1470 cm⁻¹, mencakup banyak tingkat getaran molekul sekaligus, sehingga pulsa ini tidak mengeksitasi satu tingkat getaran melainkan superposisi koheren banyak tingkat, sebuah paket gelombang (subbab 15.12). Inilah kompromi mendasar spektroskopi: resolusi waktu yang tinggi harus dibayar dengan resolusi energi yang rendah, sesuai hubungan ketidakpastian energi–waktu.
:::

### Ragam laser dan kimia

| Laser | Medium | Panjang gelombang | Transisi |
|---|---|---|---|
| He–Ne | gas Ne (dipompa He) | 632,8 nm | elektronik atom Ne |
| Ion argon | Ar⁺ | 488,0; 514,5 nm | elektronik ion Ar⁺ |
| CO₂ | gas CO₂ | sekitar 10,6 µm | rotasi–getaran $00^01 \to 10^00$ |
| Excimer ArF, KrF | dimer tereksitasi | 193, 248 nm | dari keadaan terikat ke keadaan tolak |
| Nd:YAG | Nd³⁺ dalam Y₃Al₅O₁₂ | 1064 nm | 4f–4f |
| Titanium-safir | Ti³⁺ dalam Al₂O₃ | 650–1100 nm | d–d vibronik, dapat ditala |
| Zat warna | rodamin dan lain-lain dalam larutan | dapat ditala | $S_1 \to S_0$ |
| Dioda | semikonduktor (GaN, GaAs) | 405 nm sampai inframerah | pita konduksi → pita valensi |

: Tabel 15.3 Beberapa laser penting dan asal transisinya.

Hampir setiap tangga energi dalam buku ini muncul dalam tabel itu. Laser CO₂ memakai garis-garis rotasi–getaran (subbab 6.12); garis P(20) yang paling kuat berada di 944,19 cm⁻¹ (10,59 µm). Laser excimer memanfaatkan molekul yang hanya terikat dalam keadaan tereksitasi; keadaan dasarnya tolak-menolak, sehingga tingkat bawah laser otomatis kosong dan inversi mudah. Laser titanium-safir dapat ditala karena transisi d–d Ti³⁺ (seperti [Ti(H₂O)₆]³⁺, subbab 14.2) sangat lebar akibat kopling vibronik; lebar inilah yang memungkinkan pulsa femtodetik. Optika taklinear memperluas jangkauan: kristal penggandaan frekuensi mengubah 1064 nm menjadi 532, 355, dan 266 nm.

::: {.contoh}
**Contoh 15.43 · Foton dari penunjuk laser dan dari laser excimer**

(a) Berapa foton per detik yang dipancarkan laser He–Ne 5,0 mW? (b) Berapa energi foton ArF (193 nm) dalam eV dan kJ/mol, dan mengapa laser ini dapat mengukir polimer dan kornea mata tanpa membakarnya?

**Penyelesaian.** (a) $N = P\lambda/hc = (5{,}0 \times 10^{-3})(632{,}8 \times 10^{-9})/(1{,}986 \times 10^{-25}) = 1{,}6 \times 10^{16}$ foton/s. (b) $E = 1239{,}84/193 = 6{,}42$ eV $= 620$ kJ/mol.

**Memahami hasil.** Satu foton 193 nm membawa energi lebih besar daripada energi ikatan C–C (348 kJ/mol) dan C–H (413 kJ/mol). Penyerapannya oleh ikatan C=O dan C=C memutus ikatan secara langsung (fotoablasi) dalam lapisan setebal kurang dari satu mikrometer, sebelum panas sempat menyebar. Inilah dasar bedah refraktif mata (LASIK) dan fotolitografi chip silikon. Sebaliknya, laser CO₂ dengan foton 0,12 eV bekerja dengan memanaskan, karena setiap foton hanya mengeksitasi getaran.
:::

::: {.kuis}
**Kuis cepat 15.10**

Mengapa laser sinar-X jauh lebih sulit dibuat daripada laser inframerah? (Petunjuk: subbab 15.1.) Mengapa rongga yang lebih panjang menghasilkan mode yang lebih rapat?
:::

## 15.11 Spektroskopi fotoelektron

### Prinsip

Bila foton berenergi $h\nu$ mengionkan molekul, kelebihan energinya dibawa oleh elektron yang terlepas. Menurut kekekalan energi, persamaan Einstein untuk efek fotolistrik (subbab 1.4) yang diterapkan pada molekul,

$$
E_k = h\nu - I_i , \qquad \text{(15.39)}
$$

dengan $I_i$ energi ionisasi ke keadaan ion ke-$i$. Spektrometer fotoelektron menyinari gas dengan foton monokromatik dan mengukur sebaran energi kinetik elektron yang terlepas. Setiap pita dalam spektrum bersesuaian dengan satu keadaan ion, yaitu, dalam gambaran orbital, pengambilan elektron dari satu orbital molekul. Spektroskopi fotoelektron ultraviolet (UPS) memakai lampu helium (He I, 21,22 eV; He II, 40,81 eV) untuk orbital valensi. Spektroskopi fotoelektron sinar-X (XPS) memakai sinar-X Al K$\alpha$ (1486,6 eV) atau Mg K$\alpha$ (1253,6 eV) untuk orbital inti.

### Teorema Koopmans

Dalam teori Hartree–Fock (subbab 9.8 dan 17.2), energi orbital $\varepsilon_i$ adalah energi satu elektron di orbital itu dalam medan semua elektron lain. Bila elektron diambil dari orbital $i$ dan orbital-orbital lain dianggap tidak berubah ("beku"), energi ionisasinya adalah

$$
I_i \approx -\varepsilon_i . \qquad \text{(15.40)}
$$

Inilah **teorema Koopmans**, yang menjadikan spektrum fotoelektron "foto" langsung diagram energi orbital molekul. Hampiran ini mengabaikan dua efek yang berlawanan arah: **relaksasi** (orbital-orbital lain menyesuaikan diri dengan berkurangnya satu elektron, menurunkan energi ion, sehingga $I$ lebih kecil daripada $-\varepsilon$) dan **korelasi** (yang biasanya bekerja ke arah sebaliknya). Untuk orbital valensi, keduanya sering saling menghapus sebagian dan teorema Koopmans meleset sekitar 1 eV; untuk orbital inti, relaksasi mendominasi dan selisihnya belasan eV.

::: {.contoh}
**Contoh 15.44 · Spektrum fotoelektron air**

Energi ionisasi vertikal H₂O: 12,62 eV ($1b_1$), 14,74 eV ($3a_1$), 18,55 eV ($1b_2$), dan 32,2 eV ($2a_1$, diukur dengan He II). Energi orbital Hartree–Fock air dekat batas basis lengkap adalah $-0{,}507$, $-0{,}579$, $-0{,}716$, dan $-1{,}352$ hartree. Bandingkan, dan jelaskan mengapa pita $2a_1$ tidak tampak dalam spektrum He I.

**Penyelesaian.** Dengan 1 hartree = 27,211 eV, $-\varepsilon_i$ = 13,80; 15,76; 19,48; 36,79 eV. Selisih terhadap pengamatan: +1,18; +1,02; +0,93; +4,59 eV.

**Memahami hasil.** Urutan keempat orbital diramalkan dengan benar, dan untuk tiga orbital valensi luar teorema Koopmans meleset sekitar 1 eV, selalu terlalu besar karena relaksasi diabaikan. Orbital $2a_1$ (sebagian besar 2s oksigen) lebih dalam dan relaksasinya lebih besar. Foton He I (21,22 eV) tidak cukup energinya untuk mengionkan dari orbital 32 eV, sehingga diperlukan He II. Spektrum air dengan empat pita adalah bukti langsung bahwa kedua "pasangan bebas" oksigen tidak setara, seperti yang diramalkan teori orbital molekul ($1b_1$ dan $3a_1$ berbeda energi lebih dari 2 eV), bukan dua pasangan sp³ yang identik.
:::

### Struktur getaran dan sifat ikatan orbital

Ionisasi juga merupakan transisi elektronik, sehingga prinsip Franck–Condon berlaku. Struktur getaran setiap pita mengungkap **sifat ikatan** orbital yang dikosongkan:

- Elektron dari orbital **tak berikatan**: geometri ion hampir sama dengan molekul netral. Pita tajam, didominasi komponen 0–0, dan frekuensi getaran ion hampir sama dengan molekul netral.
- Elektron dari orbital **ikatan**: ikatan ion lebih lemah dan lebih panjang. Pita lebar dengan progresi getaran panjang, dan frekuensi getaran ion lebih rendah.
- Elektron dari orbital **antiikatan**: ikatan ion lebih kuat dan lebih pendek. Frekuensi getaran ion lebih tinggi.

Spektrum fotoelektron N₂ adalah contoh baku (Gambar 15.9). Tiga pita pertama berasal dari pengambilan elektron $3\sigma_g$, $1\pi_u$, dan $2\sigma_u$ (subbab 11.7–11.8).

![Gambar 15.9 Spektrum fotoelektron He I N₂ yang dihitung dari faktor Franck–Condon osilator harmonik dengan tetapan molekul N₂ dan ketiga keadaan N₂⁺. Pita $X\,^2\Sigma_g^+$ (15,58 eV) dan $B\,^2\Sigma_u^+$ (18,75 eV) didominasi komponen 0–0; pita $A\,^2\Pi_u$ (16,69 eV) memperlihatkan progresi panjang.](fig/c_pes.png){width=90%}

::: {.contoh}
**Contoh 15.45 · Membaca spektrum fotoelektron N₂**

Pisahan getaran ($\Delta G_{1/2}$) N₂ netral adalah 2330 cm⁻¹. Untuk ketiga keadaan ion N₂⁺: $X$ 2175 cm⁻¹ ($r_e = 1{,}116$ Å), $A$ 1874 cm⁻¹ ($r_e = 1{,}175$ Å), $B$ 2373 cm⁻¹ ($r_e = 1{,}074$ Å); $r_e$(N₂) = 1,098 Å. Faktor Franck–Condon yang dihitung untuk komponen $v' = 0, 1, 2, \ldots$: $X$ 0,92; 0,08; 0,00; $A$ 0,27; 0,39; 0,24; 0,08; 0,02; $B$ 0,87; 0,12; 0,01. Simpulkan sifat ikatan ketiga orbital. Berapa energi kinetik fotoelektron pita $X$ dengan He I?

**Penyelesaian.** $3\sigma_g$: frekuensi turun 7% dan ikatan memanjang 0,019 Å; pita didominasi 0–0: orbital ikatan lemah, hampir tak berikatan. $1\pi_u$: frekuensi turun 20% dan ikatan memanjang 0,077 Å; progresi panjang berpuncak di $v' = 1$: orbital ikatan kuat. $2\sigma_u$: frekuensi **naik** 2% dan ikatan **memendek** 0,024 Å: orbital sedikit antiikatan. $E_k = 21{,}22 - 15{,}58 = 5{,}64$ eV.

**Memahami hasil.** Spektrum fotoelektron N₂ mengonfirmasi diagram orbital molekul dengan pencampuran s–p (subbab 11.8): orbital $3\sigma_g$ berada di **atas** $1\pi_u$ dan hampir tak berikatan karena bercampur dengan $2\sigma_g$. Menariknya, teorema Koopmans dengan fungsi gelombang Hartree–Fock meramalkan urutan sebaliknya ($1\pi_u$ lebih mudah diionkan); urutan yang benar baru diperoleh bila relaksasi dan korelasi diperhitungkan. Spektroskopi fotoelektron di sini menjadi hakim bagi teori.
:::

::: {.contoh}
**Contoh 15.46 · Dua pita metana**

Spektrum fotoelektron metana memperlihatkan dua pita: satu pita lebar di sekitar 14 eV dan satu pita di sekitar 23 eV, dengan perbandingan luas sekitar 3 : 1. Model ikatan valensi dengan empat ikatan C–H sp³ yang setara (subbab 12.5) seolah-olah meramalkan satu pita saja. Jelaskan.

**Penyelesaian.** Delapan elektron valensi metana menempati orbital molekul $1t_2$ (enam elektron, tiga orbital berdegenerasi, sekitar 14 eV) dan $2a_1$ (dua elektron, sekitar 23 eV). Perbandingan luas pita mengikuti banyaknya elektron, 6 : 2 = 3 : 1. Pita $1t_2$ lebar dan terpecah karena ion CH₄⁺ dalam keadaan $^2T_2$ berdegenerasi dan mengalami distorsi Jahn–Teller yang kuat (subbab 14.6).

**Memahami hasil.** Spektrum ini sering dikutip sebagai bukti "kemenangan" teori orbital molekul atas ikatan valensi. Tafsir yang lebih teliti (subbab 12.13) menunjukkan bahwa kedua gambaran setara untuk keadaan dasar: orbital lokal sp³ dan orbital kanonik $a_1 + t_2$ saling berhubungan melalui transformasi uniter yang tidak mengubah energi total. Yang tidak setara adalah **keadaan ion**: lubang yang terbentuk menempati orbital kanonik, yang merupakan fungsi eigen operator Fock, bukan orbital lokal. Fotoionisasi mengukur energi keadaan, bukan energi ikatan.
:::

### XPS dan geseran kimia

Elektron inti (1s karbon, nitrogen, oksigen) tidak ikut berikatan, tetapi energi ikatnya bergantung sedikit pada lingkungan kimia atom. Atom yang kehilangan rapat elektron karena terikat pada atom elektronegatif mengikat elektron intinya lebih kuat, sehingga energi ikat naik. **Geseran kimia** ini, beberapa eV, sebanding kira-kira dengan muatan parsial atom. Untuk karbon 1s dalam polimer, nilai khasnya sekitar 285,0 eV (C–C, C–H), 286,5 eV (C–O), 288,0 eV (C=O), 289,0 eV (O–C=O), dan 292–293 eV (CF₂, CF₃). Karena elektron dengan energi kinetik sekitar 1 keV hanya dapat keluar dari kedalaman beberapa nanometer tanpa kehilangan energi, XPS adalah teknik permukaan: ia dipakai untuk menganalisis lapisan tipis, katalis, korosi, dan permukaan biomaterial.

::: {.contoh}
**Contoh 15.47 · Energi kinetik fotoelektron XPS**

Dengan sinar-X Al K$\alpha$ (1486,6 eV) dan fungsi kerja spektrometer 4,5 eV, berapa energi kinetik fotoelektron C 1s dari gugus C–C (energi ikat 285,0 eV) dan CF₃ (293,0 eV)? Dalam spektrum polimer yang mengandung kedua gugus dengan perbandingan atom 3 : 1, bagaimana pita C 1s tampak?

**Penyelesaian.** $E_k = 1486{,}6 - 285{,}0 - 4{,}5 = 1197{,}1$ eV untuk C–C dan $1189{,}1$ eV untuk CF₃. Pita C 1s terpecah menjadi dua puncak berjarak 8 eV dengan perbandingan luas 3 : 1.

**Memahami hasil.** Karena luas puncak sebanding dengan banyaknya atom (setelah dikoreksi faktor kepekaan), XPS memberi komposisi kuantitatif permukaan dan sekaligus keadaan kimia setiap unsur. Geseran 8 eV untuk karbon yang diikat tiga atom fluor dapat dipahami dengan teorema Koopmans dan elektrostatika: tiga atom fluor yang menarik elektron membuat karbon bermuatan parsial positif, dan potensial listrik positif itu mengikat elektron 1s lebih kuat.
:::

::: {.kuis}
**Kuis cepat 15.11**

Mengapa pita fotoelektron dari orbital tak berikatan tajam? Dalam spektrum fotoelektron HCl, pita pertama (dari orbital 3p klorin yang tegak lurus ikatan) memperlihatkan pisahan getaran 2670 cm⁻¹, dibanding 2886 cm⁻¹ pada HCl netral. Apa sifat ikatan orbital itu?
:::

## 15.12 Spektroskopi resolusi waktu

### Memotret molekul yang bergerak

Semua spektroskopi yang telah dibahas mengukur tingkat energi, yaitu keadaan **stasioner**. Reaksi kimia, sebaliknya, adalah peristiwa yang berlangsung dalam waktu: ikatan meregang, atom bergerak, dan dalam sekitar 100 fs sebuah molekul berubah menjadi molekul lain. Untuk melihat peristiwa itu secara langsung diperlukan "kilat" yang lebih singkat daripada gerak inti. Laser pulsa femtodetik (subbab 15.10) menyediakannya. Teknik dasarnya adalah **pompa–probe**: pulsa pertama (pompa) memulai proses, misalnya mengeksitasi molekul; pulsa kedua (probe), yang tiba setelah selang waktu $\Delta t$ yang dapat diatur, mengukur keadaan sistem melalui serapan, pendaran, atau ionisasi. Selang waktu diatur dengan memperpanjang lintasan optis salah satu pulsa: 1 µm lintasan tambahan sama dengan 3,34 fs.

### Paket gelombang

Pulsa yang sangat singkat mempunyai spektrum lebar (Contoh 15.42) dan karena itu mengeksitasi banyak tingkat getaran keadaan tereksitasi secara serentak dan koheren. Keadaan yang terbentuk adalah superposisi

$$
\Psi(t) = \sum_vc_v\chi_v e^{-iE_vt/\hbar} , \qquad \text{(15.41)}
$$

dengan koefisien $c_v$ yang sebanding dengan amplitudo Franck–Condon $\langle v|0''\rangle$ dikalikan amplitudo spektrum pulsa pada energi $E_v$. Superposisi seperti ini bukan keadaan stasioner; rapat peluangnya berupa **paket gelombang** yang terlokalisasi dan bergerak bolak-balik di dalam sumur potensial seperti partikel klasik (subbab 3.5). Untuk osilator harmonik, semua selisih energi kelipatan $\hbar\omega$, sehingga paket kembali tepat ke bentuk awalnya setiap periode $T = 2\pi/\omega$. Untuk potensial anharmonik, selisih energinya tidak sama persis: paket perlahan **menyebar** (dephasing), lalu pada waktu yang jauh lebih lama **bangkit kembali** (revival). Untuk tingkat Morse $E_v = hc[\omega_e(v + \tfrac12) - \omega_ex_e(v + \tfrac12)^2]$, periode klasik di sekitar $\bar v$ dan waktu kebangkitan adalah

$$
T_\text{kl} = \frac{1}{c[\omega_e - 2\omega_ex_e(\bar v + 1)]}, \qquad T_\text{bangkit} = \frac{1}{c\,\omega_ex_e} , \qquad \text{(15.42)}
$$

dengan penyebut $T_\text{kl}$ sama dengan selisih $G(\bar v + 1) - G(\bar v)$. Pada separuh waktu kebangkitan, paket juga terbentuk kembali, tetapi di sisi seberang sumur (bergeser setengah periode klasik).

![Gambar 15.10 Paket gelombang getaran dalam keadaan B I₂ yang dieksitasi pulsa singkat (tingkat $v'$ sekitar 10, sebaran Gauss dengan lebar 3 tingkat). (a) Fungsi autokorelasi $|\langle\Psi(0)|\Psi(t)\rangle|^2$ selama 3 ps: osilasi dengan periode sekitar 0,3 ps yang perlahan meredup. (b) Selama 100 ps: paket menyebar, lalu bangkit kembali di sekitar 22 ps (di sisi seberang sumur) dan 44 ps.](fig/c_paket.png){width=94%}

::: {.contoh}
**Contoh 15.48 · Getaran I₂ yang terlihat**

Untuk keadaan B I₂ ($\omega_e = 125{,}69$ cm⁻¹, $\omega_ex_e = 0{,}764$ cm⁻¹), hitung periode klasik paket gelombang di sekitar $\bar v = 5$, 10, dan 15, serta waktu kebangkitannya. Berapa banyak tingkat getaran yang dieksitasi oleh pulsa 10 fs?

**Penyelesaian.** $G(\bar v + 1) - G(\bar v) = \omega_e - 2\omega_ex_e(\bar v + 1)$: 116,5; 108,9; 101,2 cm⁻¹, sehingga $T_\text{kl}$ = 286, 306, dan 329 fs. $T_\text{bangkit} = 1/(2{,}998 \times 10^{10} \times 0{,}764)$ s $= 43{,}7$ ps. Pulsa 10 fs selebar 1470 cm⁻¹ mencakup sekitar $1470/110 \approx 13$ tingkat.

**Memahami hasil.** Dengan pulsa probe yang mengionkan molekul hanya ketika paket berada di dekat titik balik luar, sinyal ion berosilasi dengan periode sekitar 300 fs: getaran satu ikatan kimia terlihat secara langsung dalam domain waktu. Periode bertambah panjang dengan energi, sesuai pelunakan potensial Morse, dan dari periode ini bentuk potensial keadaan tereksitasi dapat direkonstruksi. Bahwa paket bangkit kembali setelah puluhan pikodetik adalah gejala kuantum murni yang tidak mempunyai padanan klasik.
:::

::: {.contoh}
**Contoh 15.49 · Fungsi autokorelasi dengan Python**

Hitung $|\langle\Psi(0)|\Psi(t)\rangle|^2 = |\sum_v|c_v|^2e^{-iE_vt/\hbar}|^2$ untuk paket gelombang dalam keadaan B I₂ yang terdiri atas tingkat $v = 0$–30 dengan bobot Gauss berpusat di $v = 10$ dan lebar 3, lalu tentukan waktu puncak pertama dan puncak-puncak kebangkitan.

**Penyelesaian.**

```python
import numpy as np
c = 2.99792458e10                       # cm/s
we, wexe = 125.69, 0.764                # cm^-1
v = np.arange(31)
E = we*(v + 0.5) - wexe*(v + 0.5)**2    # cm^-1
w = np.exp(-(v - 10)**2 / (2*3**2)); w /= w.sum()      # |c_v|^2
t = np.linspace(0, 100e-12, 200001)     # s
A = np.abs((w[:, None] * np.exp(-2j*np.pi*c*E[:, None]*t)).sum(0))**2
def puncak(t1, t2):                    # waktu A maksimum dalam selang (t1, t2)
    m = (t > t1) & (t < t2)
    return t[m][np.argmax(A[m])], A[m].max()
print(puncak(0.1e-12, 0.5e-12))         # puncak pertama
print(puncak(1e-12, 15e-12))            # setelah paket menyebar
print(puncak(15e-12, 30e-12), puncak(35e-12, 50e-12))   # kebangkitan
```

Puncak pertama muncul di 304 fs (tinggi 0,79), sesuai periode klasik untuk $\bar v = 10$. Antara 1 dan 15 ps tidak ada puncak yang lebih tinggi dari 0,50: paket telah menyebar. Puncak kebangkitan muncul di 21,75 ps (0,98) dan 43,8 ps (0,94).

**Memahami hasil.** Kode singkat ini memperlihatkan bahwa seluruh dinamika paket gelombang, baik gerak klasik maupun kebangkitan kuantum, terkandung dalam tingkat energi dan bobot awalnya. Dalam percobaan nyata, bobot $|c_v|^2$ ditentukan oleh faktor Franck–Condon dan spektrum pulsa pompa, dan sinyal yang terukur bergantung pula pada cara probe membaca posisi paket.
:::

### Kimia femtodetik

Zewail dan rekan-rekannya (Hadiah Nobel Kimia 1999) memakai teknik pompa–probe untuk mengamati reaksi kimia pada skala waktu gerak atom. Pada disosiasi ICN → I + CN, fragmen CN muncul sekitar 200 fs setelah eksitasi. Pada natrium iodida, pulsa pompa memindahkan molekul ke keadaan kovalen Na–I yang bersilangan dengan keadaan ionik Na⁺I⁻; paket gelombang berosilasi dengan periode sekitar satu pikodetik, dan setiap kali melewati daerah persilangan sebagian kecil "bocor" menjadi atom Na dan I yang terpisah. Pengamatan ini adalah gambaran langsung keadaan transisi dan persilangan permukaan potensial yang sebelumnya hanya dapat disimpulkan dari teori.

Di luar fase gas, spektroskopi resolusi waktu mengungkap proses yang menjadi dasar kehidupan dan teknologi: isomerisasi cis–trans retinal dalam rodopsin, langkah pertama penglihatan, terjadi dalam sekitar 200 fs dengan hasil kuantum 0,65; pemisahan muatan di pusat reaksi fotosintesis terjadi dalam beberapa pikodetik dengan efisiensi hampir 100%; dan injeksi elektron dari zat warna MLCT ke TiO₂ dalam sel surya peka-pewarna (subbab 14.12) terjadi dalam kurang dari 100 fs.

### Teknik pengukuran

Beberapa teknik resolusi waktu yang paling banyak dipakai kimiawan:

- **Serapan transien.** Probe berupa cahaya putih yang diukur spektrumnya pada setiap $\Delta t$. Perubahan serapan memperlihatkan pengosongan keadaan dasar (bleach, serapan berkurang), emisi terangsang dari keadaan tereksitasi, dan serapan oleh keadaan tereksitasi atau zat antara (serapan bertambah).
- **Penghitungan foton tunggal berkorelasi waktu** (TCSPC). Sampel dieksitasi berulang-ulang dengan pulsa laser lemah, dan waktu tiba setiap foton pendaran dicatat. Histogramnya adalah kurva peluruhan fluoresensi dengan resolusi puluhan pikodetik; inilah cara $\tau_f$ di subbab 15.8 diukur.
- **Inframerah dan Raman resolusi waktu.** Probe inframerah memperlihatkan perubahan ikatan secara langsung, misalnya ulur CO dalam karbonil logam yang kehilangan satu ligan setelah fotolisis.
- **Spektroskopi dua dimensi.** Generalisasi pompa–probe dengan beberapa pulsa yang menghasilkan peta korelasi antara frekuensi eksitasi dan deteksi, mirip NMR dua dimensi (subbab 16.10), yang memperlihatkan bagaimana energi mengalir di antara getaran atau kromofor.

::: {.contoh}
**Contoh 15.50 · Merancang garis tunda**

Dalam percobaan pompa–probe, cermin pada panggung bergerak memantulkan berkas probe bolak-balik, sehingga setiap 1 µm gerakan panggung memperpanjang lintasan 2 µm. (a) Berapa langkah panggung yang diperlukan untuk resolusi 10 fs? (b) Berapa panjang gerak panggung untuk mengamati kebangkitan paket I₂ di 44 ps?

**Penyelesaian.** (a) 10 fs setara $10 \times 0{,}2998 = 3{,}0$ µm lintasan cahaya, yaitu langkah panggung 1,5 µm. (b) 44 ps setara $44 \times 10^{-12} \times 2{,}998 \times 10^8 = 13{,}2$ mm lintasan, yaitu 6,6 mm gerak panggung.

**Memahami hasil.** Cahaya menempuh 0,3 µm dalam satu femtodetik; dalam kimia femtodetik, waktu diukur dengan penggaris. Panggung presisi yang ketelitiannya di bawah satu mikrometer mudah didapat, sehingga resolusi waktu sebenarnya dibatasi oleh lebar pulsa, bukan oleh garis tunda.
:::

::: {.kuis}
**Kuis cepat 15.12**

Mengapa pulsa 1 ps tidak dapat menghasilkan paket gelombang yang berosilasi dalam keadaan B I₂, padahal pulsa 50 fs dapat? Apa yang terlihat bila molekul dieksitasi ke keadaan yang sepenuhnya tolak-menolak?
:::
