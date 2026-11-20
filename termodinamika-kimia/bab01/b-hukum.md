## 1.4 Hukum-hukum gas: Boyle, Charles, Avogadro

Sekarang kita punya empat variabel keadaan, *p*, *V*, *T*, dan *n*. Pertanyaan alamiahnya: apakah keempatnya bebas, atau saling terikat? Jawaban pertama datang tiga setengah abad yang lalu, dari percobaan yang mengubah satu variabel sambil menahan yang lain tetap.

**Hukum Boyle (1662).** Robert Boyle mengurung udara di ujung tertutup tabung berbentuk J, lalu menuangkan raksa ke ujung yang terbuka untuk menekannya. Ia menemukan bahwa pada suhu tetap, makin besar tekanan, makin kecil volume udara itu, dan hasil kali keduanya tetap:

$$
pV = \text{tetap} \qquad (n, T\ \text{tetap}) . \qquad \text{(1.5)}
$$

Mengapa begitu? Bayangkan volume gas dibuat separuhnya. Molekul yang sama kini berdesakan dalam ruang yang lebih sempit, sehingga setiap bagian dinding dihantam dua kali lebih sering, dan tekanan menjadi dua kali. Kurva *p* terhadap *V* pada suhu tetap berbentuk hiperbola dan disebut **isoterm**.

**Hukum Charles (1787) dan Gay-Lussac (1802).** Bila tekanan dibuat tetap dan gas dipanaskan, volumenya bertambah secara linear dengan suhu. Hal yang mengejutkan muncul ketika garis volume–suhu untuk berbagai gas diperpanjang ke arah suhu rendah: semuanya memotong volume nol pada titik yang sama, sekitar −273 °C. Titik itulah nol mutlak, dan bila suhu diukur dalam kelvin, hubungannya menjadi kesebandingan sederhana:

$$
V \propto T \qquad (n, p\ \text{tetap}) . \qquad \text{(1.6)}
$$

Tentu saja, tidak ada gas yang benar-benar menyusut sampai volume nol; semua gas mencair lebih dulu. Ekstrapolasi itu hanya menunjukkan bahwa suhu kelvin adalah ukuran yang "alami" bagi gas. Garis-garis pada tekanan tetap ini disebut **isobar**.

**Asas Avogadro (1811).** Gay-Lussac juga menemukan bahwa gas-gas bereaksi dalam perbandingan volume yang sederhana. Dua volume hidrogen bereaksi dengan satu volume oksigen menghasilkan dua volume uap air. Amedeo Avogadro menafsirkannya dengan gagasan yang berani untuk zamannya: pada suhu dan tekanan yang sama, volume yang sama dari gas apa pun mengandung jumlah molekul yang sama. Dengan kata lain,

$$
V \propto n \qquad (p, T\ \text{tetap}) . \qquad \text{(1.7)}
$$

Kini perbandingan volume 2 : 1 : 2 langsung terbaca sebagai perbandingan molekul dalam persamaan reaksi $2\text{H}_2 + \text{O}_2 \to 2\text{H}_2\text{O}$.

::: {.contoh}
**Contoh 1.4 · Boyle dan Charles dalam praktik**

(a) Udara 2,50 L pada 1,00 atm di dalam alat suntik ditekan perlahan sampai volumenya 0,80 L tanpa perubahan suhu. Berapa tekanannya sekarang? (b) Sebuah balon berisi 1,20 L udara pada 25 °C dicelupkan ke dalam campuran es kering dan aseton bersuhu −78 °C. Berapa volumenya bila tekanan tetap?

**Penyelesaian.** (a) Dari hukum Boyle, $p_1V_1 = p_2V_2$:
$$
p_2 = \frac{(1{,}00\ \text{atm})(2{,}50\ \text{L})}{0{,}80\ \text{L}} = 3{,}1\ \text{atm} .
$$
(b) Suhu harus dalam kelvin: $T_1 = 298{,}15$ K, $T_2 = 195{,}15$ K. Dari hukum Charles, $V_1/T_1 = V_2/T_2$:
$$
V_2 = (1{,}20\ \text{L}) \times \frac{195{,}15\ \text{K}}{298{,}15\ \text{K}} = 0{,}785\ \text{L} .
$$

**Memahami hasil.** Pada (b), suhu Celsius turun dari 25 menjadi −78, tetapi volume tidak menjadi negatif. Hanya perbandingan suhu **kelvin** yang bermakna: balon menyusut sepertiganya karena suhu kelvinnya turun sepertiga.
:::

::: {.awas}
**Selalu pakai kelvin.** Kesalahan paling sering dalam soal gas adalah memasukkan suhu Celsius ke dalam perbandingan. Pemanasan dari 10 °C ke 20 °C tidak melipatduakan volume gas; volumenya hanya naik dari 283 menjadi 293 bagian, sekitar 3,5%.
:::

::: {.kuis}
**Kuis cepat 1.4** Gelembung udara naik dari dasar danau sedalam 20 m ke permukaan. Kira-kira berapa kali volumenya bertambah bila suhunya tidak berubah? (Petunjuk: setiap 10,3 m air setara dengan 1 atm.)
:::

## 1.5 Persamaan gas ideal dan pemakaiannya

Ketiga hukum di atas berbicara tentang gas yang sama dari tiga arah. Boyle mengatakan $V \propto 1/p$, Charles mengatakan $V \propto T$, dan Avogadro mengatakan $V \propto n$. Satu-satunya cara agar ketiganya benar sekaligus adalah $V \propto nT/p$. Menamai tetapan kesebandingannya *R*, kita memperoleh

::: {.inti}
$$
pV = nRT \qquad \text{(1.8)}
$$
**Persamaan gas ideal.** *R* adalah **tetapan gas**: $R = 8{,}314$ J K⁻¹ mol⁻¹ $= 0{,}082\,06$ L atm K⁻¹ mol⁻¹ $= 0{,}083\,14$ L bar K⁻¹ mol⁻¹.
:::

Gas yang memenuhi persamaan (1.8) secara tepat pada semua kondisi disebut **gas ideal**. Gas ideal tidak ada, tetapi gas nyata mendekatinya makin baik bila tekanannya makin rendah dan suhunya makin tinggi, yakni bila molekul-molekulnya berjauhan dan bergerak cepat. Pada suhu kamar dan tekanan sekitar 1 atm, kebanyakan gas sederhana (N₂, O₂, He, Ar, CH₄) menyimpang dari persamaan (1.8) kurang dari satu persen, sehingga persamaan ini sangat berguna dalam praktik.

Persamaan gas ideal juga memberi arti yang jelas pada **volume molar**. Membagi (1.8) dengan *n* menghasilkan $V_\text{m} = RT/p$, yang sama untuk semua gas ideal. Dua kondisi acuan yang sering dipakai:

| Kondisi | *T* | *p* | $V_\text{m}$ |
|---|---|---|---|
| STP (lama) | 273,15 K | 1 atm | 22,414 L mol⁻¹ |
| SATP (suhu dan tekanan standar ambien) | 298,15 K | 1 bar | 24,790 L mol⁻¹ |

Bila jumlah zat tetap, persamaan (1.8) dapat ditulis sebagai $pV/T = nR = \text{tetap}$, sehingga untuk dua keadaan dari gas yang sama

$$
\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2} . \qquad \text{(1.9)}
$$

Bentuk ini praktis karena satuan tidak perlu diubah, asalkan satuan yang sama dipakai di kedua ruas dan suhu dinyatakan dalam kelvin.

Pemakaian yang paling penting bagi kimiawan adalah menghubungkan sifat gas dengan **massa molar**. Jumlah zat sama dengan massa dibagi massa molar, $n = m/M$. Memasukkannya ke dalam (1.8) dan menyusun ulang menghasilkan

$$
M = \frac{\rho RT}{p} , \qquad \rho = \frac{m}{V} . \qquad \text{(1.10)}
$$

Jadi, cukup dengan menimbang sejumlah gas dalam labu bervolume tertentu pada suhu dan tekanan yang diketahui, kita dapat menentukan massa molar zat itu. Cara inilah yang dipakai pada abad ke-19 untuk menentukan massa atom banyak unsur.

::: {.contoh}
**Contoh 1.5 · Berapa mol gas di dalam tabung?**

Sebuah tabung 10,0 L berisi oksigen pada 2,00 atm dan 25 °C. Berapa mol dan berapa gram oksigen di dalamnya?

**Penyelesaian.** Dari (1.8), dengan *R* dalam L atm K⁻¹ mol⁻¹ supaya satuan cocok:
$$
n = \frac{pV}{RT} = \frac{(2{,}00\ \text{atm})(10{,}0\ \text{L})}{(0{,}082\,06\ \text{L atm K}^{-1}\text{mol}^{-1})(298{,}15\ \text{K})} = 0{,}817\ \text{mol} .
$$
Massanya $0{,}817 \times 32{,}00 = 26{,}2$ g.

**Memahami hasil.** Pilihan nilai *R* menentukan satuan yang harus dipakai untuk *p* dan *V*. Dengan $R = 8{,}314$ J K⁻¹ mol⁻¹, tekanan harus dalam Pa dan volume dalam m³: $p = 2{,}026 \times 10^5$ Pa, $V = 0{,}0100$ m³, hasilnya sama.
:::

::: {.contoh}
**Contoh 1.6 · Mengenali gas dari massa jenisnya**

Suatu gas murni mempunyai massa jenis 1,25 g L⁻¹ pada 0 °C dan 1,00 atm. Berapa massa molarnya, dan gas apa kemungkinan besar?

**Penyelesaian.** Dari (1.10):
$$
M = \frac{(1{,}25\ \text{g L}^{-1})(0{,}082\,06\ \text{L atm K}^{-1}\text{mol}^{-1})(273{,}15\ \text{K})}{1{,}00\ \text{atm}} = 28{,}0\ \text{g mol}^{-1} .
$$

**Memahami hasil.** Massa molar 28,0 g mol⁻¹ cocok dengan N₂ (28,01) dan CO (28,01). Massa jenis saja tidak dapat membedakan keduanya; kita perlu sifat lain, misalnya bahwa CO terbakar dengan nyala biru dan N₂ tidak. Massa jenis gas juga menjelaskan mengapa CO₂ (44 g mol⁻¹) mengumpul di dasar gua dan sumur, sementara helium (4 g mol⁻¹) membuat balon melayang.
:::

::: {.contoh}
**Contoh 1.7 · Kantong udara mobil**

Kantong udara mobil mengembang karena natrium azida terurai dengan cepat: $2\text{NaN}_3(s) \to 2\text{Na}(s) + 3\text{N}_2(g)$. Berapa volume nitrogen yang dihasilkan oleh 65,0 g NaN₃ ($M = 65{,}01$ g mol⁻¹) pada 25 °C dan 1,00 atm?

**Penyelesaian.** Jumlah NaN₃: $65{,}0/65{,}01 = 1{,}000$ mol. Menurut persamaan reaksi, setiap 2 mol NaN₃ menghasilkan 3 mol N₂, jadi $n(\text{N}_2) = 1{,}500$ mol. Volumenya:
$$
V = \frac{nRT}{p} = \frac{(1{,}500)(0{,}082\,06)(298{,}15)}{1{,}00}\ \text{L} = 36{,}7\ \text{L} .
$$

**Memahami hasil.** Enam puluh lima gram padatan, kira-kira sesendok makan, menghasilkan hampir 37 liter gas dalam beberapa puluh milidetik. Itulah kekuatan reaksi yang menghasilkan gas: volume molar gas sekitar seribu kali volume molar padatan.
:::

::: {.contoh}
**Contoh 1.8 · Tekanan ban setelah perjalanan**

Pagi hari pada 25 °C, pengukur tekanan menunjukkan ban mobil bertekanan 220 kPa. Pengukur ini membaca **tekanan lebih** di atas tekanan udara (101,3 kPa). Setelah perjalanan jauh, suhu udara di dalam ban naik menjadi 50 °C. Bila volume ban dianggap tetap, berapa bacaan pengukur sekarang?

**Rencana.** Hukum gas hanya berlaku untuk tekanan **mutlak**. Ubah dulu bacaan pengukur ke tekanan mutlak, pakai (1.9) dengan $V_1 = V_2$, lalu kembalikan ke bacaan pengukur.

**Penyelesaian.** Tekanan mutlak awal $220 + 101{,}3 = 321{,}3$ kPa. Tekanan mutlak akhir:
$$
p_2 = (321{,}3\ \text{kPa}) \times \frac{323{,}15\ \text{K}}{298{,}15\ \text{K}} = 348{,}2\ \text{kPa} .
$$
Bacaan pengukur: $348{,}2 - 101{,}3 = 247$ kPa.

**Memahami hasil.** Bacaan naik 27 kPa, sekitar 12%, walaupun suhu kelvin hanya naik 8%. Kenaikan relatif bacaan pengukur lebih besar karena 101,3 kPa tekanan udara luar tidak ikut naik. Karena itu pabrik ban selalu menganjurkan pengukuran tekanan saat ban masih dingin.
:::

::: {.kuis}
**Kuis cepat 1.5** Dua labu bervolume sama pada suhu dan tekanan sama berisi H₂ dan CO₂. Labu mana yang mengandung lebih banyak molekul? Labu mana yang lebih berat?
:::

## 1.6 Campuran gas: hukum Dalton dan fraksi mol

Udara yang kita hirup bukan gas murni, tetapi campuran nitrogen, oksigen, argon, dan sedikit gas lain. Bagaimana persamaan gas ideal berlaku untuk campuran? John Dalton menjawabnya pada 1801 dengan pengamatan yang sesuai dengan gambaran molekul: dalam campuran gas ideal, setiap komponen berperilaku seolah-olah ia sendirian mengisi seluruh wadah.

Tekanan yang akan diberikan komponen *J* bila ia sendirian menempati wadah itu disebut **tekanan parsial** $p_J$:

$$
p_J = \frac{n_JRT}{V} . \qquad \text{(1.11)}
$$

Menjumlahkan semua komponen menghasilkan **hukum Dalton**:

$$
p = p_A + p_B + \cdots = (n_A + n_B + \cdots)\frac{RT}{V} . \qquad \text{(1.12)}
$$

Mengapa hukum ini masuk akal? Karena dalam gas ideal molekul-molekul tidak saling memengaruhi. Molekul oksigen yang menumbuk dinding tidak "tahu" bahwa ada molekul nitrogen di dekatnya, sehingga sumbangannya pada tekanan sama seperti bila ia sendirian.

Membagi (1.11) dengan (1.12) menghilangkan *R*, *T*, dan *V* sekaligus, dan menghasilkan hubungan yang sangat praktis:

::: {.inti}
$$
p_J = x_Jp , \qquad x_J = \frac{n_J}{n} \qquad \text{(1.13)}
$$
Tekanan parsial suatu komponen sama dengan **fraksi molnya** $x_J$ dikali tekanan total. Jumlah semua fraksi mol sama dengan 1.
:::

::: {.contoh}
**Contoh 1.9 · Tekanan parsial udara**

Udara kering mengandung fraksi mol N₂ 0,7808, O₂ 0,2095, dan Ar 0,0093. Hitung tekanan parsial masing-masing pada tekanan total 1,00 atm.

**Penyelesaian.** Dari (1.13): $p(\text{N}_2) = 0{,}7808$ atm $= 593$ mmHg $= 79{,}1$ kPa; $p(\text{O}_2) = 0{,}2095$ atm $= 159$ mmHg $= 21{,}2$ kPa; $p(\text{Ar}) = 0{,}0093$ atm $= 7{,}1$ mmHg $= 0{,}94$ kPa.

**Memahami hasil.** Tubuh kita merespons tekanan parsial oksigen, bukan fraksi molnya. Di puncak gunung setinggi 5000 m, fraksi mol O₂ tetap 0,21, tetapi tekanan totalnya hanya sekitar setengah atmosfer, sehingga tekanan parsial oksigennya juga tinggal setengah. Itulah penyebab sesak napas di tempat tinggi.
:::

::: {.contoh}
**Contoh 1.10 · Penyelam dan keracunan oksigen**

Penyelam menghirup udara bertekanan sama dengan tekanan air di sekelilingnya. (a) Berapa tekanan parsial oksigen yang dihirup pada kedalaman 30 m di laut ($\rho = 1025$ kg m⁻³)? (b) Tekanan parsial oksigen di atas sekitar 1,4 atm dapat menyebabkan kejang. Sampai kedalaman berapa udara biasa masih aman dari sisi ini?

**Penyelesaian.** (a) Tekanan total = tekanan udara + tekanan kolom air (persamaan 1.4):
$$
p = 101\,325\ \text{Pa} + (1025)(9{,}807)(30)\ \text{Pa} = 4{,}03 \times 10^5\ \text{Pa} = 3{,}98\ \text{atm} .
$$
Tekanan parsial oksigen $0{,}2095 \times 3{,}98 = 0{,}83$ atm.

(b) Batas tercapai bila $p = 1{,}4/0{,}2095 = 6{,}68$ atm $= 6{,}77 \times 10^5$ Pa. Kolom airnya harus menyumbang $6{,}77 \times 10^5 - 1{,}01 \times 10^5 = 5{,}76 \times 10^5$ Pa, setara dengan kedalaman $5{,}76 \times 10^5/(1025 \times 9{,}807) = 57$ m.

**Memahami hasil.** Penyelaman yang lebih dalam memerlukan campuran gas dengan fraksi mol oksigen lebih kecil, misalnya campuran helium–oksigen. Prinsipnya sama dengan hukum Dalton: yang dijaga adalah tekanan parsial, bukan persentase.
:::

::: {.contoh}
**Contoh 1.11 · Gas yang ditampung di atas air**

Oksigen hasil penguraian KClO₃ ditampung dengan menggeser air dalam gelas ukur terbalik pada 25 °C. Volume gas yang terkumpul 250 mL dan tekanan total di dalam gelas sama dengan tekanan udara, 755 mmHg. Tekanan uap air pada 25 °C adalah 23,76 mmHg. Berapa massa oksigen yang terkumpul?

**Rencana.** Gas di dalam gelas bukan oksigen murni: ia jenuh dengan uap air. Menurut hukum Dalton, tekanan total = tekanan parsial O₂ + tekanan uap air.

**Penyelesaian.** $p(\text{O}_2) = 755 - 23{,}76 = 731{,}2$ mmHg $= 9{,}749 \times 10^4$ Pa. Maka
$$
n = \frac{pV}{RT} = \frac{(9{,}749 \times 10^4\ \text{Pa})(2{,}50 \times 10^{-4}\ \text{m}^3)}{(8{,}314\ \text{J K}^{-1}\text{mol}^{-1})(298{,}15\ \text{K})} = 9{,}83 \times 10^{-3}\ \text{mol} ,
$$
dan massanya $9{,}83 \times 10^{-3} \times 32{,}00 = 0{,}315$ g.

**Memahami hasil.** Bila tekanan uap air diabaikan, hasilnya 3% terlalu besar. Kesalahan sistematis sebesar itu cukup untuk membuat percobaan stoikiometri gagal mencapai ketelitian yang diharapkan.
:::

::: {.kuis}
**Kuis cepat 1.6** Sebuah wadah berisi 2,0 g H₂ dan 32 g O₂ dengan tekanan total 3,0 atm. Berapa tekanan parsial masing-masing gas?
:::
