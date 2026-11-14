## 14.11 Spektrum elektronik dan warna kompleks

### Intensitas dan aturan seleksi

Kuat lemahnya suatu pita serapan ditentukan oleh momen dipol transisi $\boldsymbol\mu_{fi} = \langle\Psi_f|\hat{\boldsymbol\mu}|\Psi_i\rangle$ (subbab 8.12), dengan $\hat{\boldsymbol\mu} = -e\sum_k\mathbf r_k$ operator momen dipol listrik. Kekuatan osilator $f$ sebanding dengan $|\boldsymbol\mu_{fi}|^2$, dan koefisien ekstingsi molar maksimum $\varepsilon_\text{maks}$ yang terukur sebanding dengan $f$ dibagi lebar pita (hubungan tepatnya diturunkan di subbab 15.2). Dua aturan seleksi menentukan apakah $\boldsymbol\mu_{fi}$ nol:

1. **Aturan spin**, $\Delta S = 0$. Operator $\hat{\boldsymbol\mu}$ hanya bekerja pada koordinat ruang, sehingga integral faktor spin $\langle\chi_f|\chi_i\rangle$ nol bila keadaan spinnya berbeda. Kopling spin–orbit mencampurkan sedikit keadaan berspin lain dan melonggarkan aturan ini, lebih banyak untuk logam berat.
2. **Aturan Laporte.** Dalam molekul berpusat inversi, $\hat{\boldsymbol\mu}$ ganjil ($u$) terhadap inversi, sehingga integral $\langle g|u|g\rangle$ nol. Transisi d–d adalah $g \to g$ (kedua keadaan berasal dari orbital d yang genap), jadi **terlarang Laporte** dalam kompleks oktahedral. Transisi diizinkan hanya bila paritasnya berubah: $g \leftrightarrow u$.

Jika kedua aturan itu mutlak, kompleks oktahedral tidak akan berwarna. Kenyataannya mereka berwarna lemah karena dua mekanisme pelonggaran:

- **Kopling vibronik** (mekanisme Herzberg–Teller). Selama getaran yang berparitas $u$, misalnya ulur asimetris yang menggeser logam dari pusat, pusat inversi hilang sesaat dan orbital d bercampur sedikit dengan orbital p. Transisi "meminjam" intensitas dari transisi $d \to p$ yang diizinkan. Karena memerlukan getaran $u$, intensitasnya naik dengan suhu.
- **Tidak adanya pusat inversi.** Dalam kompleks tetrahedral, label $g$ dan $u$ tidak ada; orbital $t_2$ logam bercampur langsung dengan orbital 4p (yang juga $t_2$ dalam $T_d$). Transisi d–d tetrahedral meminjam intensitas secara permanen dan 10–100 kali lebih kuat.

| Jenis transisi | $\varepsilon_\text{maks}$ (L mol⁻¹ cm⁻¹) | Contoh |
|---|---|---|
| Terlarang spin dan Laporte | 0,01–1 | [Mn(H₂O)₆]²⁺, [Fe(H₂O)₆]³⁺ |
| Diizinkan spin, terlarang Laporte (oktahedral) | 1–20 | [Ti(H₂O)₆]³⁺, [Ni(H₂O)₆]²⁺, [Co(H₂O)₆]²⁺ |
| Diizinkan spin, tanpa pusat inversi | 100–1000 | [CoCl₄]²⁻, [NiCl₄]²⁻ |
| Transfer muatan | 10³–10⁵ | MnO₄⁻, [Ru(bpy)₃]²⁺, [Fe(phen)₃]²⁺ |

: Tabel 14.8 Intensitas khas pita serapan senyawa koordinasi.

::: {.contoh}
**Contoh 14.48 · Merah muda dan biru kobalt(II)**

Larutan 0,010 M kobalt(II) dalam air ([Co(H₂O)₆]²⁺, $\varepsilon \approx 5$ pada 515 nm) dan dalam HCl pekat ([CoCl₄]²⁻, $\varepsilon \approx 600$ pada sekitar 690 nm) diukur dalam kuvet 1,00 cm. Hitung absorbansi dan fraksi cahaya yang diteruskan pada panjang gelombang maksimum.

**Penyelesaian.** $A = \varepsilon cl$. [Co(H₂O)₆]²⁺: $A = 5 \times 0{,}010 \times 1 = 0{,}05$, transmitans $10^{-0{,}05} = 0{,}89$. [CoCl₄]²⁻: $A = 600 \times 0{,}010 = 6{,}0$, transmitans $10^{-6} = 10^{-6}$.

**Memahami hasil.** Larutan akua meneruskan 89% cahaya hijau yang paling diserapnya: warnanya merah muda pucat. Larutan klorida praktis tidak meneruskan cahaya merah-jingga sama sekali, sehingga tampak biru pekat. Perubahan warna ini adalah dasar "kertas kobalt klorida" untuk mendeteksi air dan indikator kelembapan dalam silika gel: kobalt tetrahedral (kering) biru, kobalt oktahedral terhidrasi merah muda. Perbedaan intensitasnya adalah perbedaan aturan Laporte.
:::

::: {.contoh}
**Contoh 14.49 · Ketergantungan suhu intensitas vibronik**

Untuk transisi yang diizinkan secara vibronik melalui getaran berparitas $u$ dengan bilangan gelombang $\tilde\nu_u$, kekuatan osilatornya berbanding dengan $\coth(hc\tilde\nu_u/2kT)$. Untuk $\tilde\nu_u = 300$ cm⁻¹, hitung perbandingan intensitas pada 298 K dan 77 K.

**Penyelesaian.** $hc/k = 1{,}4388$ cm K. Pada 298 K: $x = 1{,}4388 \times 300/(2 \times 298) = 0{,}724$, $\coth x = 1{,}614$. Pada 77 K: $x = 2{,}803$, $\coth x = 1{,}007$. Perbandingannya 1,60.

**Memahami hasil.** Pada suhu rendah hanya getaran titik nol yang menyumbang; pada suhu kamar, keadaan getaran tereksitasi menambah amplitudo distorsi dan pinjaman intensitas. Penurunan intensitas d–d sekitar 40% ketika larutan beku didinginkan dari suhu kamar ke nitrogen cair adalah bukti percobaan mekanisme vibronik. Pita transfer muatan yang diizinkan langsung hampir tidak bergantung pada suhu.
:::

### Lebar pita

Pita d–d dalam larutan lebar, 2000–5000 cm⁻¹, jauh lebih lebar daripada garis spektrum atom. Penyebab utamanya adalah prinsip Franck–Condon (subbab 15.7). Transisi $t_{2g} \to e_g$ memindahkan elektron ke orbital antiikatan, sehingga panjang ikatan setimbang keadaan tereksitasi lebih besar daripada keadaan dasar. Transisi elektronik terjadi pada geometri keadaan dasar dan berakhir pada banyak tingkat getaran keadaan tereksitasi, yang menyatu menjadi pita lebar. Dalam bahasa diagram Tanabe–Sugano: ketika getaran mengubah panjang ikatan, $\Delta_o$ berfluktuasi, dan energi transisi berfluktuasi sebanding dengan **kemiringan** garis keadaan tereksitasi terhadap keadaan dasar.

Kesimpulannya, transisi yang memindahkan elektron antara $t_{2g}$ dan $e_g$ menghasilkan pita lebar, sedangkan transisi yang hanya membalik spin **di dalam** konfigurasi yang sama (garis sejajar keadaan dasar pada diagram) menghasilkan garis tajam. Contoh terkenal adalah garis R rubi dan pita 25 000 cm⁻¹ [Mn(H₂O)₆]²⁺ (Contoh 14.47). Efek Jahn–Teller pada keadaan dasar atau tereksitasi menambah pelebaran dan dapat memecah pita (subbab 14.6).

![Gambar 14.11 Spektrum serapan model (jumlah pita Gauss dengan posisi, lebar, dan $\varepsilon$ khas). (a) [Ti(H₂O)₆]³⁺: satu transisi $^2T_{2g} \to {}^2E_g$ yang terpecah Jahn–Teller. (b) [Ni(H₂O)₆]²⁺: tiga pita spin diizinkan. (c) [Cr(H₂O)₆]³⁺: dua pita spin diizinkan dan garis tajam $^2E_g$ yang sangat lemah. Pita latar menunjukkan warna cahaya tampak pada panjang gelombang tersebut.](fig/c_spektrum.png){width=94%}

### Warna

Warna yang kita lihat adalah sisa spektrum cahaya putih setelah sebagian diserap. Bila serapan berupa satu pita di daerah tampak, warna yang terlihat kira-kira **warna komplementer** warna yang diserap.

| Diserap (nm) | Warna diserap | Warna terlihat |
|---|---|---|
| 400–435 | ungu | kuning kehijauan |
| 435–480 | biru | kuning |
| 480–490 | biru kehijauan | jingga |
| 490–500 | hijau kebiruan | merah |
| 500–560 | hijau | ungu kemerahan (magenta) |
| 560–580 | kuning kehijauan | ungu |
| 580–595 | kuning | biru |
| 595–650 | jingga | biru kehijauan |
| 650–750 | merah | hijau kebiruan |

: Tabel 14.9 Warna komplementer (pembagian kasar).

Untuk kompleks dengan lebih dari satu pita, warnanya ditentukan oleh "jendela" tempat cahaya lolos di antara pita-pita itu.

::: {.contoh}
**Contoh 14.50 · Membaca warna dari pita**

Jelaskan warna (a) [Ni(H₂O)₆]²⁺ (pita 8500, 13 800, 25 300 cm⁻¹), (b) [Cu(H₂O)₆]²⁺ (pita lebar berpuncak 12 600 cm⁻¹), (c) [Cr(NH₃)₆]³⁺ (21 550 dan 28 500 cm⁻¹).

**Penyelesaian.** Ubah ke panjang gelombang, $\lambda = 10^7/\tilde\nu$ nm.

(a) 1176, 725, dan 395 nm. Pita pertama di inframerah; pita kedua menyerap merah; pita ketiga menyerap ungu. Jendela di antara keduanya, sekitar 450–600 nm, meneruskan hijau: larutan nikel(II) hijau.

(b) 794 nm, pita lebar yang ekornya meluas sampai sekitar 600 nm: merah dan jingga diserap, biru diteruskan.

(c) 464 nm (biru) dan 351 nm (ultraviolet dekat). Biru diserap, kuning–jingga diteruskan: garam [Cr(NH₃)₆]³⁺ kuning jingga.

**Memahami hasil.** Penggantian air dengan amonia pada Cr³⁺ ($\Delta_o$ dari 17 400 ke 21 550 cm⁻¹) menggeser pita pertama dari 575 nm (kuning) ke 464 nm (biru), dan warnanya bergeser dari ungu kelabu ke kuning. Untuk Cu²⁺, penggantian air dengan amonia juga menggeser pita ke energi lebih tinggi (sekitar 600 nm), menghasilkan biru tua yang khas: pita kini menyerap jingga–kuning dan meneruskan biru dan ungu. Perubahan warna semacam ini adalah cara tercepat membaca deret spektrokimia dengan mata.
:::

### Jawaban teka-teki rubi dan zamrud

Dalam rubi (Cr³⁺:Al₂O₃), pita spin diizinkan $^4A_{2g} \to {}^4T_{2g}$ berada di sekitar 18 000 cm⁻¹ (556 nm, kuning-hijau) dan $^4A_{2g} \to {}^4T_{1g}$ di sekitar 24 600 cm⁻¹ (407 nm, ungu). Cahaya merah lolos dengan bebas, ditambah sedikit biru: merah tua keunguan. Dalam zamrud (Cr³⁺ dalam beril), kisi beril memberi Cr³⁺ ruang sedikit lebih longgar dan atom oksigen yang muatan efektifnya lebih kecil; $\Delta_o$ turun ke sekitar 16 100 cm⁻¹ (621 nm) dan pita kedua ke sekitar 23 800 cm⁻¹. Kini merah–jingga yang diserap dan hijau yang lolos. Perbedaan $\Delta_o$ hanya 11%. Pada alexandrite (Cr³⁺ dalam krisoberil, BeAl₂O₄), $\Delta_o$ berada tepat di antara keduanya, sehingga warnanya bergantung pada sumber cahaya: hijau di bawah sinar matahari yang kaya biru-hijau, merah di bawah lampu pijar yang kaya merah.

Rubi juga menjelaskan sumber garis laser pertama (1960). Keadaan $^2E_g$ berasal dari konfigurasi $t_{2g}^3$, sama dengan keadaan dasar; transisi $^2E_g \to {}^4A_{2g}$ hanya membalik satu spin. Garisnya tajam (garis R di 694,3 nm) dan, karena terlarang spin, umurnya panjang (sekitar 3 ms). Elektron yang dipompa ke pita lebar $^4T_{2g}$ dan $^4T_{1g}$ cepat meluruh tanpa radiasi ke $^2E_g$ dan menumpuk di sana: syarat inversi populasi yang dibahas di subbab 15.10.

::: {.contoh}
**Contoh 14.51 · Berapa jauh oksigen menjauh dalam zamrud?**

Jika perbedaan $\Delta_o$ rubi (18 000 cm⁻¹) dan zamrud (16 100 cm⁻¹) seluruhnya disebabkan perbedaan jarak Cr–O dengan $\Delta_o \propto a^{-5}$, berapa persen jarak Cr–O dalam zamrud lebih panjang?

**Penyelesaian.** $a_\text{zamrud}/a_\text{rubi} = (18\,000/16\,100)^{1/5} = 1{,}118^{0{,}2} = 1{,}023$. Jarak lebih panjang 2,3%, sekitar 0,04–0,05 Å untuk ikatan Cr–O sepanjang 1,9–2,0 Å.

**Memahami hasil.** Perbedaan struktur sekecil itu, setara dengan seperduapuluh jari-jari atom, mengubah merah menjadi hijau. Dalam kenyataan, perbedaan muatan efektif dan kovalensi ikatan Cr–O juga ikut berperan, sehingga perubahan jarak yang sebenarnya lebih kecil daripada taksiran ini. Pelajaran umumnya tetap: karena $\Delta_o$ sangat peka terhadap lingkungan, warna ion logam transisi adalah sensor struktur yang sangat halus, dan geolog memakainya untuk mengenali asal batu permata.
:::

::: {.contoh}
**Contoh 14.52 · Mengapa garis R rubi tajam**

Dengan parameter rubi $B = 643$ cm⁻¹ dan $C = 3195$ cm⁻¹ (dicocokkan dengan pita 18 000 dan 24 600 cm⁻¹ serta garis R di 14 400 cm⁻¹), program Contoh 14.45 memberi energi $^2E_g$ 14 387 cm⁻¹ pada $Dq = 1750$ dan 14 413 cm⁻¹ pada $Dq = 1850$ cm⁻¹, sedangkan $^4T_{2g}$ tepat $10Dq$. Bandingkan kepekaan kedua energi terhadap $Dq$ dan taksir perbandingan lebar pitanya.

**Penyelesaian.** $dE(^2E_g)/dDq = (14\,413 - 14\,387)/100 = 0{,}26$, sedangkan $dE(^4T_{2g})/dDq = 10$. Jika fluktuasi $Dq$ akibat getaran sama untuk kedua transisi, lebar pita sebanding dengan kemiringan, sehingga pita $^4T_{2g}$ sekitar $10/0{,}26 \approx 38$ kali lebih lebar.

**Memahami hasil.** Pita $^4T_{2g}$ rubi selebar sekitar 2000 cm⁻¹; garis R pada suhu kamar hanya sekitar 10 cm⁻¹ (pada suhu rendah lebih sempit lagi, karena pelebaran yang tersisa berasal dari proses lain). Taksiran kemiringan memberi arah yang tepat: garis yang sejajar keadaan dasar pada diagram Tanabe–Sugano menghasilkan garis tajam. Karena garis R hampir tidak bergantung pada $\Delta_o$ tetapi tetap sedikit bergeser dengan tekanan, garis ini menjadi manometer optik yang sangat teliti (Contoh 14.8).
:::

::: {.awas}
**Warna bukan selalu d–d**

Banyak senyawa logam transisi yang berwarna pekat tidak berwarna karena transisi d–d. Permanganat, kromat, dikromat, [Fe(SCN)]²⁺, ferroin, dan biru Prusia berwarna karena transfer muatan (subbab 14.12), yang seratus sampai sepuluh ribu kali lebih kuat. Ukuran $\varepsilon$ biasanya cukup untuk membedakannya: pita dengan $\varepsilon > 1000$ dalam kompleks oktahedral hampir pasti bukan d–d.
:::

::: {.kuis}
**Kuis cepat 14.11**

Mengapa larutan [Fe(H₂O)₆]³⁺ murni (dalam asam perklorat pekat) hampir tidak berwarna, padahal larutan besi(III) biasa kuning kecokelatan?
:::

## 14.12 Transfer muatan

### Tiga jenis transfer muatan

Pada **transisi transfer muatan** (TM), elektron berpindah dari orbital yang terutama milik satu bagian kompleks ke orbital yang terutama milik bagian lain. Karena orbital asal dan tujuan berbeda paritas (misalnya orbital π ligan yang $u$ ke orbital $t_{2g}$ logam yang $g$) dan perpindahan elektron sejauh ikatan memberi momen dipol transisi yang besar, pita TM diizinkan dan sangat kuat: $\varepsilon$ 10³–10⁵ L mol⁻¹ cm⁻¹. Ada tiga jenis utama:

1. **Ligan ke logam (LMCT).** Elektron berpindah dari orbital ligan terisi (biasanya pasangan bebas atau orbital π) ke orbital d logam yang kosong atau setengah terisi. Disukai bila ligan mudah dioksidasi (I⁻, Br⁻, S²⁻, O²⁻) dan logam mudah direduksi (bilangan oksidasi tinggi). Contoh: MnO₄⁻, CrO₄²⁻, [Fe(SCN)(H₂O)₅]²⁺, [IrCl₆]²⁻.
2. **Logam ke ligan (MLCT).** Elektron berpindah dari orbital $t_{2g}$ logam yang terisi ke orbital π* ligan yang kosong. Disukai bila logam mudah dioksidasi (bilangan oksidasi rendah, d⁶ spin rendah) dan ligan mempunyai π* rendah (bipiridina, fenantrolina, CO). Contoh: [Ru(bpy)₃]²⁺, [Fe(phen)₃]²⁺.
3. **Logam ke logam (MMCT) atau antarvalensi (IVCT).** Dalam senyawa valensi campuran, elektron berpindah dari logam bervalensi rendah ke logam yang sama bervalensi tinggi, misalnya Fe(II) → Fe(III) dalam biru Prusia.

Dalam diagram orbital molekul (Gambar 14.6), LMCT berasal dari orbital ikatan atau orbital π ligan tak berikatan ke $t_{2g}$ atau $e_g^*$; MLCT berasal dari $t_{2g}$ ke orbital π* ligan di atas $e_g^*$.

### Transfer muatan ligan ke logam

Ion okso d⁰ isoelektronik menunjukkan pola yang jelas. Semuanya tidak mempunyai elektron d, sehingga tidak mungkin ada transisi d–d; warna mereka sepenuhnya LMCT dari orbital oksigen ke orbital d logam yang kosong.

| Ion | VO₄³⁻ | CrO₄²⁻ | MnO₄⁻ | TcO₄⁻ | ReO₄⁻ |
|---|---|---|---|---|---|
| $\lambda_\text{maks}$ (nm) | ≈ 270 | 373 | 528 | 287 | 227 |
| $\tilde\nu$ (cm⁻¹) | ≈ 37 000 | 26 800 | 18 900 | 34 800 | 44 100 |
| Warna | tak berwarna | kuning | ungu | tak berwarna | tak berwarna |

: Tabel 14.10 Pita LMCT pertama ion okso tetrahedral d⁰ (dibulatkan).

Sepanjang V(V) → Cr(VI) → Mn(VII), muatan inti dan bilangan oksidasi naik, orbital d logam turun energinya, dan pita TM bergeser dari ultraviolet ke hijau. Sepanjang Mn → Tc → Re dalam satu golongan, orbital 4d dan 5d **lebih tinggi** daripada 3d dan lebih kovalen, sehingga pita kembali ke ultraviolet. Itu sebabnya permanganat adalah oksidator kuat yang berwarna pekat, sedangkan perrenat tak berwarna dan jauh kurang oksidatif. Warna dan potensial redoks bercerita hal yang sama: energi orbital penerima.

Jørgensen merangkum energi LMCT dengan **elektronegativitas optis**:

$$
\tilde\nu_\text{LMCT} \approx 30\,000\ \text{cm}^{-1} \times \left[\chi_\text{opt}(\text{L}) - \chi_\text{opt}(\text{M})\right] , \qquad \text{(14.41)}
$$

dengan $\chi_\text{opt}$ ligan F 3,9; Cl 3,0; Br 2,8; I 2,5 (hampir sama dengan skala Pauling), dan $\chi_\text{opt}$ logam yang ditentukan dari satu spektrum lalu dipakai untuk meramalkan yang lain.

::: {.contoh}
**Contoh 14.53 · Heksahaloiridat(IV)**

Pita LMCT pertama [IrCl₆]²⁻ berada di sekitar 20 400 cm⁻¹. (a) Tentukan $\chi_\text{opt}(\text{Ir}^{4+})$. (b) Ramalkan pita yang sama untuk [IrBr₆]²⁻ dan [IrI₆]²⁻.

**Penyelesaian.** (a) $\chi_\text{opt}(\text{Ir}) = 3{,}0 - 20\,400/30\,000 = 2{,}32$. (b) [IrBr₆]²⁻: $30\,000(2{,}8 - 2{,}32) = 14\,400$ cm⁻¹ (694 nm). [IrI₆]²⁻: $30\,000(2{,}5 - 2{,}32) = 5400$ cm⁻¹, di inframerah dekat.

**Memahami hasil.** Penggantian Cl⁻ oleh Br⁻ menurunkan pita TM sekitar 6000 cm⁻¹, karena elektron Br 4p lebih mudah "diambil" logam. [IrI₆]²⁻ tidak stabil: bila energi transfer muatan mendekati nol, elektron benar-benar pindah, Ir(IV) direduksi menjadi Ir(III) dan iodida dioksidasi. Dengan cara yang sama, elektronegativitas optis meramalkan bahwa CuI₂ dan FeI₃ tidak dapat dibuat: pasangan logam pengoksidasi dan ligan pereduksi bereaksi sendiri. Rumus sederhana (14.41) dengan demikian menghubungkan spektroskopi dan kimia redoks.
:::

### Transfer muatan logam ke ligan

Kompleks d⁶ spin rendah dengan ligan diimina aromatik adalah contoh MLCT yang paling banyak dipelajari. [Ru(bpy)₃]²⁺ menyerap kuat di 452 nm ($\varepsilon = 14\,600$), sehingga larutannya jingga. Keadaan tereksitasi yang mula-mula terbentuk adalah singlet, $^1$MLCT, yang dalam kurang dari satu pikodetik berpindah ke triplet $^3$MLCT melalui kopling spin–orbit rutenium yang kuat. Triplet itu berumur sekitar satu mikrodetik dan berpendar jingga-merah di sekitar 610 nm. Dalam keadaan tereksitasi, satu elektron berada pada orbital π* sebuah ligan bipiridina dan satu lubang pada logam: secara formal [Ru³⁺(bpy)₂(bpy⁻)]²⁺. Molekul ini sekaligus pereduksi yang lebih kuat (elektron di π*) dan pengoksidasi yang lebih kuat (lubang di $t_{2g}$) daripada keadaan dasarnya.

::: {.contoh}
**Contoh 14.54 · Potensial redoks keadaan tereksitasi**

Untuk [Ru(bpy)₃]²⁺: $E°(\text{Ru}^{3+}/\text{Ru}^{2+}) = +1{,}26$ V, $E°(\text{Ru}^{2+}/\text{Ru}^{+}) = -1{,}28$ V (keduanya terhadap elektrode hidrogen standar), dan energi keadaan tereksitasi $^3$MLCT di atas keadaan dasar $E_{00} = 2{,}12$ eV. Hitung $E°(\text{Ru}^{3+}/\text{Ru}^{2+*})$ dan $E°(\text{Ru}^{2+*}/\text{Ru}^{+})$.

**Penyelesaian.** Keadaan tereksitasi menyimpan 2,12 eV tambahan. Untuk oksidasi: $E°(\text{Ru}^{3+}/\text{Ru}^{2+*}) = 1{,}26 - 2{,}12 = -0{,}86$ V. Untuk reduksi: $E°(\text{Ru}^{2+*}/\text{Ru}^{+}) = -1{,}28 + 2{,}12 = +0{,}84$ V.

**Memahami hasil.** Satu foton biru mengubah oksidator lemah ($+1{,}26$ V untuk mengambil elektron dari keadaan dasar memerlukan oksidator kuat) menjadi molekul yang dapat memberikan elektron dengan potensial $-0{,}86$ V **dan** menerima elektron dengan potensial $+0{,}84$ V. Inilah dasar fotokatalisis redoks yang kini banyak dipakai dalam sintesis organik dan sel surya peka-pewarna, tempat kompleks rutenium polipiridina menyuntikkan elektron dari keadaan MLCT ke pita konduksi TiO₂.
:::

::: {.contoh}
**Contoh 14.55 · Ferroin dalam analisis besi**

Besi dalam air minum ditentukan dengan mereduksinya menjadi Fe²⁺ dan menambahkan 1,10-fenantrolina berlebih. Kompleks [Fe(phen)₃]²⁺ (ferroin) menyerap di 510 nm dengan $\varepsilon = 11\,100$ L mol⁻¹ cm⁻¹. Absorbansi sampel dalam kuvet 1,00 cm adalah 0,500. Hitung kadar besi dalam mg/L.

**Penyelesaian.** $c = A/\varepsilon l = 0{,}500/11\,100 = 4{,}50 \times 10^{-5}$ M. Dengan $M(\text{Fe}) = 55{,}845$ g/mol: $4{,}50 \times 10^{-5} \times 55{,}845 \times 1000 = 2{,}52$ mg/L.

**Memahami hasil.** Pita MLCT yang sangat kuat memungkinkan pengukuran besi sampai beberapa puluh mikrogram per liter. Fe²⁺ dengan ligan medan kuat ini berspin rendah ($t_{2g}^6$), dan elektron $t_{2g}$ yang tinggi energinya mudah dipindahkan ke orbital π* fenantrolina. Fe³⁺ dengan fenantrolina tidak menunjukkan pita ini (berwarna biru pucat), sehingga zat pereduksi seperti hidroksilamina harus ditambahkan lebih dulu. Ferroin juga indikator redoks: perubahan merah ↔ biru pucat terjadi pada +1,06 V.
:::

### Transfer muatan antarvalensi

Dalam senyawa **valensi campuran** dengan dua pusat logam yang sama tetapi bilangan oksidasinya berbeda, seperti Fe(II)–Fe(III), ada transisi yang memindahkan elektron dari satu pusat ke pusat lain. Robin dan Day mengelompokkan senyawa semacam ini menjadi tiga kelas: kelas I, kedua pusat tidak berinteraksi dan tidak ada pita antarvalensi; kelas II, interaksi lemah, elektron masih terlokalisasi pada satu pusat, dan ada pita antarvalensi yang lebar; kelas III, elektron terdelokalisasi penuh dan kedua pusat setara ("valensi rata-rata").

Untuk sistem kelas II setangkup, Hush menurunkan bahwa energi pita sama dengan energi reorganisasi $\lambda$ (energi yang diperlukan untuk menata ulang ikatan dan pelarut sehingga cocok dengan muatan yang sudah berpindah), dan lebar pita pada suhu $T$

$$
\tilde\nu_\text{maks} = \lambda, \qquad \Delta\tilde\nu_{1/2} = \sqrt{16\ln2\,kT\,\tilde\nu_\text{maks}} \approx \sqrt{2310\,\tilde\nu_\text{maks}}\ \text{cm}^{-1}\ (298\ \text{K}) . \qquad \text{(14.42)}
$$

Dari intensitas pita, besar kopling elektronik antara kedua pusat dapat ditaksir:

$$
H_{ab} \approx \frac{2{,}06 \times 10^{-2}}{r}\sqrt{\tilde\nu_\text{maks}\,\varepsilon_\text{maks}\,\Delta\tilde\nu_{1/2}} , \qquad \text{(14.43)}
$$

dengan semua energi dalam cm⁻¹, $\varepsilon$ dalam L mol⁻¹ cm⁻¹, dan $r$ jarak antarpusat dalam Å. Parameter $\lambda$ dan $H_{ab}$ yang sama menentukan laju transfer elektron termal menurut teori Marcus; spektroskopi antarvalensi dengan demikian mengukur langsung besaran kunci reaksi redoks.

::: {.contoh}
**Contoh 14.56 · Kelas II atau kelas III?**

(a) Suatu kompleks dinuklear Ru(II)–Ru(III) mempunyai pita antarvalensi di 8000 cm⁻¹ dengan $\varepsilon_\text{maks} = 500$ dan $\Delta\tilde\nu_{1/2} = 4300$ cm⁻¹, dengan jarak Ru–Ru 6,8 Å. Periksa kecocokan dengan (14.42) dan hitung $H_{ab}$. (b) Ion Creutz–Taube, [(NH₃)₅Ru(pz)Ru(NH₃)₅]⁵⁺ (pz = pirazina), menyerap di 1570 nm dengan lebar sekitar 1500 cm⁻¹. Termasuk kelas apa?

**Penyelesaian.** (a) Ramalan Hush: $\sqrt{2310 \times 8000} = 4300$ cm⁻¹, sama dengan teramati: kelas II. $H_{ab} = (2{,}06 \times 10^{-2}/6{,}8)\sqrt{8000 \times 500 \times 4300} = 3{,}03 \times 10^{-3} \times 1{,}31 \times 10^5 = 397$ cm⁻¹.

(b) $\tilde\nu = 10^7/1570 = 6370$ cm⁻¹. Ramalan kelas II: $\sqrt{2310 \times 6370} = 3840$ cm⁻¹. Lebar teramati hanya sekitar 40% dari itu. Pita yang jauh lebih sempit dari ramalan Hush menandakan bahwa model elektron terlokalisasi tidak berlaku: ion Creutz–Taube termasuk kelas III (atau di perbatasan II–III), dengan kedua rutenium berbilangan oksidasi efektif +2,5.

**Memahami hasil.** Kopling 400 cm⁻¹ pada kasus (a) kecil dibanding $\lambda/2 = 4000$ cm⁻¹, syarat lokalisasi kelas II. Pada ion Creutz–Taube, kopling melalui jembatan pirazina cukup kuat untuk mendelokalisasi elektron. Pertanyaan "di mana elektron berada" dalam senyawa ini adalah pertanyaan kuantum yang sama dengan pertanyaan resonansi pada benzena (subbab 12.10) dan dijawab oleh perbandingan antara kopling dan energi reorganisasi.
:::

::: {.terapan}
**Biru Prusia**

Biru Prusia, Fe₄[Fe(CN)₆]₃, adalah pigmen sintetis modern pertama (Berlin, sekitar 1706). Kisinya terdiri atas Fe(II) spin rendah yang dikelilingi enam atom C sianida dan Fe(III) spin tinggi yang dikelilingi enam atom N, dengan jembatan Fe(II)–C≡N–Fe(III). Kedua komponen terpisah, K₄[Fe(CN)₆] dan garam Fe³⁺, hanya berwarna kuning pucat. Warna biru tua berasal dari pita antarvalensi Fe(II) → Fe(III) di sekitar 700 nm (14 000 cm⁻¹) dengan $\varepsilon$ sekitar 10⁴ per satuan Fe(II)–Fe(III). Elektron yang berpindah melewati jembatan sianida sejauh 5,1 Å. Biru Prusia kini juga dipakai sebagai obat penawar keracunan talium dan cesium radioaktif, dan analog-analognya diteliti sebagai elektrode baterai ion natrium.
:::

::: {.kuis}
**Kuis cepat 14.12**

Mengapa [Fe(phen)₃]²⁺ merah tua tetapi [Zn(phen)₃]²⁺ tak berwarna, padahal ligannya sama?
:::

## 14.13 Aturan 18 elektron dan senyawa organologam

### Dari diagram OM ke aturan 18 elektron

Logam transisi mempunyai sembilan orbital valensi: lima (n−1)d, satu ns, dan tiga np. Analog dengan aturan oktet untuk unsur golongan utama (empat orbital valensi, delapan elektron), kompleks yang mengisi tepat semua orbital ikatan dan tak berikatan dengan 18 elektron, tanpa menempatkan elektron di orbital antiikatan, diharapkan stabil. Diagram OM subbab 14.7 menunjukkan kapan harapan itu terpenuhi.

Dalam kompleks oktahedral dengan ligan donor σ, sembilan orbital rendah adalah enam orbital ikatan ($a_{1g}$, $t_{1u}$, $e_g$) ditambah tiga $t_{2g}$ tak berikatan; 18 elektron mengisi tepat semuanya. Namun $t_{2g}$ tak berikatan sehingga tidak ada keharusan untuk mengisinya, dan $e_g^*$ hanya sedikit antiikatan bila $\Delta_o$ kecil. Akibatnya kompleks Werner klasik mempunyai 12 sampai 22 elektron: [Cr(H₂O)₆]³⁺ 15, [Ni(H₂O)₆]²⁺ 20, [Cu(H₂O)₆]²⁺ 21. Aturan 18 elektron **tidak berlaku** untuk mereka.

Situasinya berubah bila ligan adalah akseptor π kuat seperti CO. Kini $t_{2g}$ menjadi orbital **ikatan** (subbab 14.8), sehingga mengisinya menguntungkan; sementara $e_g^*$ sangat antiikatan karena CO juga donor σ yang kuat. Celah energi antara sembilan orbital terisi dan orbital kosong terendah besar, dan kompleks dengan tepat 18 elektron jauh lebih stabil daripada dengan 17 atau 19. Aturan 18 elektron karena itu sangat andal untuk **senyawa organologam dan karbonil logam**, yaitu kompleks logam bervalensi rendah dengan ligan akseptor π.

### Menghitung elektron

Ada dua cara menghitung yang memberi jawaban sama bila dipakai konsisten.

- **Cara netral (kovalen).** Logam dihitung sebagai atom netral dengan banyaknya elektron valensi sama dengan nomor golongannya (Cr 6, Fe 8, Ni 10). Ligan dihitung sebagai spesi netral: CO, PR₃, NH₃, η²-alkena menyumbang 2; H, Cl, CH₃ (radikal) 1; η³-alil 3; η⁵-C₅H₅ (siklopentadienil, Cp) 5; η⁶-C₆H₆ 6; NO linear 3. Setiap ikatan logam–logam menambah 1. Muatan kompleks dikurangkan (anion menambah).
- **Cara ionik.** Ligan anionik dihitung dengan pasangan elektronnya (H⁻, Cl⁻, CH₃⁻ 2; Cp⁻ 6; alil⁻ 4), dan logam dihitung dengan bilangan oksidasinya ($d^n$).

::: {.contoh}
**Contoh 14.57 · Menghitung elektron valensi**

Hitung elektron valensi logam dalam (a) Cr(CO)₆, (b) Fe(CO)₅, (c) Ni(CO)₄, (d) HMn(CO)₅, (e) Fe(η⁵-C₅H₅)₂ (ferosena), (f) Cr(η⁶-C₆H₆)₂, (g) [Co(CO)₄]⁻, (h) CpMn(CO)₃.

**Penyelesaian.** Cara netral:

| Senyawa | Logam | Ligan | Muatan | Total |
|---|---|---|---|---|
| Cr(CO)₆ | 6 | 6 × 2 = 12 | 0 | 18 |
| Fe(CO)₅ | 8 | 5 × 2 = 10 | 0 | 18 |
| Ni(CO)₄ | 10 | 4 × 2 = 8 | 0 | 18 |
| HMn(CO)₅ | 7 | 1 + 10 = 11 | 0 | 18 |
| Fe(C₅H₅)₂ | 8 | 2 × 5 = 10 | 0 | 18 |
| Cr(C₆H₆)₂ | 6 | 2 × 6 = 12 | 0 | 18 |
| [Co(CO)₄]⁻ | 9 | 8 | +1 | 18 |
| CpMn(CO)₃ | 7 | 5 + 6 = 11 | 0 | 18 |

Dengan cara ionik, ferosena: Fe²⁺ (d⁶) + 2 Cp⁻ (2 × 6) = 18; hasilnya sama.

**Memahami hasil.** Semua senyawa ini stabil, dapat disimpan, dan banyak di antaranya dapat didistilasi atau disublimasi tanpa terurai. Karbonil sederhana memperlihatkan pola stoikiometri yang menarik: banyaknya CO berkurang dua untuk setiap kenaikan golongan dua tingkat, karena setiap pasangan elektron tambahan pada logam menggantikan satu ligan pemberi dua elektron. Geometrinya mengikuti banyaknya ligan: oktahedron, bipiramida trigonal, tetrahedron.
:::

::: {.contoh}
**Contoh 14.58 · Logam bernomor ganjil**

(a) Mengapa mangan dan kobalt tidak membentuk karbonil monomer netral yang stabil seperti Mn(CO)₆ atau Co(CO)₄, tetapi membentuk Mn₂(CO)₁₀ dan Co₂(CO)₈? (b) V(CO)₆ ada sebagai monomer. Berapa elektronnya dan bagaimana sifatnya?

**Penyelesaian.** (a) Mn (7) + 5 CO (10) = 17; satu elektron kurang. Dua fragmen Mn(CO)₅ membentuk ikatan Mn–Mn, dan setiap Mn menghitung satu elektron tambahan: 18. Dalam Mn₂(CO)₁₀, ikatan Mn–Mn tidak didukung jembatan, panjangnya sekitar 2,9 Å. Untuk Co: 9 + 8 = 17, dan Co₂(CO)₈ juga mempunyai ikatan Co–Co (dengan atau tanpa dua CO jembatan). (b) V (5) + 12 = 17 elektron. Enam CO tidak dapat ditambah satu lagi karena tidak ada ruang di sekitar vanadium untuk dimerisasi; V(CO)₆ tetap monomer paramagnetik ($S = \tfrac12$), mudah direduksi menjadi [V(CO)₆]⁻ (18 elektron) yang lebih stabil.

**Memahami hasil.** Spesies 17 elektron bersifat radikal: mereka membentuk dimer, mengambil satu elektron, atau mengambil satu atom hidrogen (HMn(CO)₅, HCo(CO)₄). HCo(CO)₄ adalah katalis industri pertama untuk hidroformilasi alkena. Dengan menghitung elektron, kita dapat meramalkan rumus dan reaktivitas tanpa satu perhitungan kuantum pun; justru di sinilah nilai suatu aturan yang dasar kuantumnya dipahami.
:::

### Ferosena dan metalosena

Ferosena, Fe(C₅H₅)₂, ditemukan pada 1951 dan strukturnya yang seperti roti lapis (sandwich) dijelaskan oleh Wilkinson dan Fischer, yang membuka kimia organologam modern. Setiap cincin Cp⁻ yang aromatik (enam elektron π, subbab 13.7) mempunyai lima orbital π: satu $a$ (tanpa simpul), dua $e_1$ (satu simpul), dan dua $e_2$ (dua simpul). Kedua cincin membentuk kombinasi genap dan ganjil yang berpasangan dengan orbital logam berkesetangkupan sama ($D_{5d}$): $a_{1g}$ dengan 4s dan $d_{z^2}$, $e_{1g}$ dengan $d_{xz}$ dan $d_{yz}$, $e_{2g}$ dengan $d_{xy}$ dan $d_{x^2-y^2}$, $e_{1u}$ dengan 4p$_x$ dan 4p$_y$, dan $a_{2u}$ dengan 4p$_z$.

Ikatan terkuat adalah $e_{1g}$: orbital $d_{xz}$ dan $d_{yz}$ yang miring mengarah ke cincin bertumpang tindih baik dengan $e_1$ Cp. Delapan belas elektron mengisi enam orbital ikatan terutama ligan, lalu tiga orbital hampir tak berikatan terutama logam ($e_{2g}$ dan $a_{1g}$, yaitu $d_{xy}$, $d_{x^2-y^2}$, $d_{z^2}$); orbital kosong terendah adalah $e_{1g}^*$ yang antiikatan. Ini persis pola "sembilan orbital rendah, 18 elektron". Ferosena sangat stabil (tahan sampai 400 °C), mudah dioksidasi satu elektron menjadi ion ferosenium biru (17 elektron), dan pasangan Fc⁺/Fc menjadi acuan potensial baku dalam elektrokimia pelarut organik.

::: {.contoh}
**Contoh 14.59 · Kobaltosena dan nikelosena**

Hitung elektron valensi kobaltosena (Cp₂Co) dan nikelosena (Cp₂Ni). Dengan diagram OM ferosena, ramalkan banyaknya elektron tak berpasangan dan reaktivitas keduanya.

**Penyelesaian.** Cp₂Co: 9 + 10 = 19 elektron; elektron ke-19 masuk orbital antiikatan $e_{1g}^*$: satu elektron tak berpasangan. Cp₂Ni: 10 + 10 = 20 elektron; dua elektron masuk pasangan $e_{1g}^*$ yang berdegenerasi dan, menurut aturan Hund, berspin sejajar: dua elektron tak berpasangan.

**Memahami hasil.** Kobaltosena adalah pereduksi kuat yang dengan mudah melepas elektron antiikatannya menjadi kation kobaltosenium (18 elektron) yang sangat stabil; potensial Cp₂Co⁺/Cp₂Co sekitar 1,3 V lebih negatif daripada ferosena. Nikelosena paramagnetik dengan momen sekitar 2,9 µ_B, sesuai dua elektron tak berpasangan, dan ikatan Ni–C-nya lebih panjang daripada Fe–C di ferosena karena elektron antiikatan. Ketiga metalosena memperlihatkan seluruh teori dalam satu baris: 18 elektron stabil, 19 mudah melepas satu, 20 melemah dan paramagnetik.
:::

### Kompleks 16 elektron dan katalisis

Kompleks bujur sangkar d⁸ (Rh(I), Ir(I), Pd(II), Pt(II)) umumnya mempunyai 16 elektron dan tetap stabil. Dalam geometri bujur sangkar, orbital $p_z$ logam tidak berinteraksi dengan ligan σ di bidang dan energinya tinggi, sedangkan $d_{x^2-y^2}$ sangat antiikatan (subbab 14.3). Hanya delapan orbital yang rendah, sehingga 16 elektron sudah mengisi semua orbital ikatan dan tak berikatan. Kompleks 16 elektron ini mempunyai "tempat kosong" yang dapat menerima ligan atau molekul substrat. Tolman merumuskan aturan katalisis organologam: reaksi berlangsung melalui langkah-langkah yang masing-masing melibatkan zat antara 16 atau 18 elektron, dan setiap langkah mengubah hitungan sebanyak dua.

::: {.contoh}
**Contoh 14.60 · Hitungan elektron dalam siklus katalis Wilkinson**

Katalis Wilkinson, RhCl(PPh₃)₃, menghidrogenasi alkena. Hitung elektron untuk setiap zat antara berikut: (1) RhCl(PPh₃)₃; (2) RhCl(PPh₃)₂ setelah satu fosfina lepas; (3) RhH₂Cl(PPh₃)₂ setelah adisi oksidatif H₂; (4) RhH₂Cl(PPh₃)₂(η²-C₂H₄); (5) RhH(C₂H₅)Cl(PPh₃)₂ setelah penyisipan migrasi; (6) RhCl(PPh₃)₂ setelah eliminasi reduktif etana.

**Penyelesaian.** Cara netral, Rh = 9. (1) 9 + 1 + 6 = 16. (2) 9 + 1 + 4 = 14. (3) 9 + 2 + 1 + 4 = 16. (4) 16 + 2 = 18. (5) 9 + 1 + 1 + 1 + 4 = 16. (6) 14.

**Memahami hasil.** Siklus ini bergantian antara 14, 16, dan 18 elektron, dengan zat antara 14 elektron yang sangat reaktif hanya berumur singkat. Adisi oksidatif menaikkan bilangan oksidasi dari +1 ke +3 dan menambah dua ligan pemberi satu elektron (hitungan +2); eliminasi reduktif kebalikannya. Hitungan elektron menjadi peta jalan siklus katalitik: langkah yang akan menghasilkan 20 elektron tidak terjadi, dan langkah yang menghasilkan 12 elektron sangat lambat. Pemahaman ini, bersama perhitungan kuantum zat antara dan keadaan transisi (subbab 17.16), dipakai merancang katalis untuk farmasi dan industri petrokimia.
:::

### Analogi isolobal

Hoffmann menunjukkan bahwa fragmen organologam dan fragmen organik dapat mempunyai orbital perbatasan yang "mirip": banyaknya, kesetangkupannya, energinya, dan banyaknya elektron yang ditempatinya. Fragmen seperti itu disebut **isolobal**. Fragmen Mn(CO)₅ (17 elektron) mempunyai satu orbital hibrida $d_{z^2}$–$p_z$–$s$ yang menunjuk ke posisi oktahedral yang kosong dan berisi satu elektron, persis seperti radikal metil CH₃ (7 elektron valensi) dengan satu orbital sp³ setengah terisi. Maka

$$
\text{CH}_3 \longleftrightarrow \text{Mn(CO)}_5, \qquad \text{CH}_2 \longleftrightarrow \text{Fe(CO)}_4, \qquad \text{CH} \longleftrightarrow \text{Co(CO)}_3 . \qquad \text{(14.44)}
$$

Setiap fragmen kekurangan sebanyak elektron yang sama dari "kulit penuh"-nya (oktet untuk karbon, 18 untuk logam). Mn₂(CO)₁₀ adalah analog isolobal etana; Fe₂(CO)₈ analog etilena; dan Co₃(CO)₉CH, yang memang ada dan stabil, adalah analog tetrahedrana dengan satu titik CH dan tiga titik Co(CO)₃.

::: {.contoh}
**Contoh 14.61 · Gugus isolobal**

(a) Periksa bahwa Co₃(CO)₉(μ₃-CH) memenuhi aturan 18 elektron pada setiap kobalt dan aturan oktet pada karbon. (b) Fragmen organologam apa yang isolobal dengan CH₂ dan dapat dipakai untuk membuat "analog siklopropana" Fe₃(CO)₁₂?

**Penyelesaian.** (a) Setiap Co: 9 (atom) + 6 (tiga CO) + 2 (dua ikatan Co–Co) + 1 (ikatan Co–C ke CH) = 18. Karbon CH: 4 + 1 (H) + 3 (tiga ikatan C–Co) = 8. (b) Fe(CO)₄ isolobal dengan CH₂; tiga Fe(CO)₄ yang saling berikatan membentuk segitiga Fe₃ analog siklopropana. Hitungan setiap Fe: 8 + 8 + 2 (dua ikatan Fe–Fe) = 18.

**Memahami hasil.** Fe₃(CO)₁₂ yang sebenarnya mempunyai dua CO jembatan, tetapi segitiga logam dengan tiga ikatan Fe–Fe dan 18 elektron per besi sesuai ramalan. Analogi isolobal memungkinkan kimiawan "menerjemahkan" struktur organik yang dikenal ke kimia gugus logam, dan sebaliknya. Ia dihargai dengan Hadiah Nobel Kimia 1981 bagi Hoffmann (bersama Fukui, untuk teori orbital perbatasan, subbab 13.10): dua pengakuan bahwa pemahaman kualitatif orbital molekul adalah alat kimia yang sangat ampuh.
:::

![Gambar 14.12 (a) Frekuensi ulur CO dalam deret heksakarbonil isoelektronik [M(CO)₆]ⁿ terhadap muatan kompleks; garis putus-putus: CO bebas. (b) Tetapan gaya C–O yang dihitung dari frekuensi tersebut. Makin negatif muatan, makin kuat ikatan balik dan makin lemah ikatan C–O.](fig/c_karbonil.png){width=88%}

::: {.awas}
**Aturan 18 elektron bukan hukum alam**

Aturan ini hampiran yang berguna untuk logam bervalensi rendah dengan ligan akseptor π, terutama logam golongan 6–9. Ia sering dilanggar oleh logam di awal deret (Ti, Zr, V: banyak kompleks 12–16 elektron yang stabil karena ligannya besar), logam di akhir deret (Pd, Pt, Au: 16 dan 14 elektron), dan kompleks Werner dengan ligan donor σ atau π. Aturan ini juga tidak berbicara tentang kinetika: kompleks 18 elektron dapat bereaksi cepat bila ada jalur disosiatif yang mudah.
:::

::: {.kuis}
**Kuis cepat 14.13**

Berapa banyak CO yang diperlukan agar kromium, besi, dan nikel masing-masing mencapai 18 elektron? Apakah [Fe(CO)₄]²⁻ mengikuti aturan 18 elektron?
:::
