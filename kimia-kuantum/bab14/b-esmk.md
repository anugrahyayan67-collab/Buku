## 14.4 Energi stabilisasi medan kristal dan sifat termodinamika

### Tabel ESMK

Persamaan (14.ea9) memberi ESMK untuk setiap konfigurasi. Tabel 14.2 merangkumnya untuk kompleks oktahedral spin tinggi dan spin rendah serta kompleks tetrahedral (selalu spin tinggi), dengan $\Delta_t = \tfrac49\Delta_o$ agar kedua geometri dapat dibandingkan. Kolom "pasangan tambahan" mencatat berapa pasangan elektron yang harus dibentuk melebihi keadaan spin tinggi; biayanya dibahas di subbab 14.5.

| $d^n$ | Okt. spin tinggi | ESMK ($Dq$) | Okt. spin rendah | ESMK ($Dq$) | Pasangan tambahan | Tetrahedral ESMK ($Dq_o$) |
|---|---|---|---|---|---|---|
| d⁰ | — | 0 | — | 0 | 0 | 0 |
| d¹ | $t_{2g}^1$ | −4 | sama | −4 | 0 | −2,67 |
| d² | $t_{2g}^2$ | −8 | sama | −8 | 0 | −5,33 |
| d³ | $t_{2g}^3$ | −12 | sama | −12 | 0 | −3,56 |
| d⁴ | $t_{2g}^3e_g^1$ | −6 | $t_{2g}^4$ | −16 | 1 | −1,78 |
| d⁵ | $t_{2g}^3e_g^2$ | 0 | $t_{2g}^5$ | −20 | 2 | 0 |
| d⁶ | $t_{2g}^4e_g^2$ | −4 | $t_{2g}^6$ | −24 | 2 | −2,67 |
| d⁷ | $t_{2g}^5e_g^2$ | −8 | $t_{2g}^6e_g^1$ | −18 | 1 | −5,33 |
| d⁸ | $t_{2g}^6e_g^2$ | −12 | sama | −12 | 0 | −3,56 |
| d⁹ | $t_{2g}^6e_g^3$ | −6 | sama | −6 | 0 | −1,78 |
| d¹⁰ | $t_{2g}^6e_g^4$ | 0 | sama | 0 | 0 | 0 |

: Tabel 14.2 Energi stabilisasi medan kristal. Kolom terakhir dinyatakan dalam $Dq$ oktahedral dengan $\Delta_t = \tfrac49\Delta_o$.

Pola spin tinggi berbentuk "dua punuk": ESMK naik dari nol di d⁰ ke maksimum di d³, turun ke nol di d⁵, naik lagi ke maksimum di d⁸, dan turun ke nol di d¹⁰. Pola ini muncul karena kulit setengah penuh dan kulit penuh mempunyai satu elektron di setiap orbital (atau dua), sehingga rapat elektronnya bersetangkup bola dan tidak merasakan pemecahan.

::: {.contoh}
**Contoh 14.b1 · ESMK dalam kJ/mol**

Hitung ESMK (tanpa energi pemasangan) untuk [Cr(H₂O)₆]³⁺, [Fe(H₂O)₆]²⁺, [Ni(H₂O)₆]²⁺, [Co(NH₃)₆]³⁺ (spin rendah), dan [Fe(CN)₆]⁴⁻ (spin rendah), memakai Tabel 14.1.

**Penyelesaian.** Dengan 1 cm⁻¹ = 0,011 963 kJ/mol:

- [Cr(H₂O)₆]³⁺, d³: $-1{,}2 \times 17\,400 = -20\,880$ cm⁻¹ $= -250$ kJ/mol.
- [Fe(H₂O)₆]²⁺, d⁶ spin tinggi: $-0{,}4 \times 10\,400 = -4160$ cm⁻¹ $= -49{,}8$ kJ/mol.
- [Ni(H₂O)₆]²⁺, d⁸: $-1{,}2 \times 8500 = -10\,200$ cm⁻¹ $= -122$ kJ/mol.
- [Co(NH₃)₆]³⁺, d⁶ spin rendah: $-2{,}4 \times 22\,900 = -54\,960$ cm⁻¹ $= -658$ kJ/mol.
- [Fe(CN)₆]⁴⁻, d⁶ spin rendah: $-2{,}4 \times 33\,800 = -81\,120$ cm⁻¹ $= -970$ kJ/mol.

**Memahami hasil.** ESMK spin tinggi berukuran puluhan sampai ratusan kJ/mol, sebesar energi ikatan hidrogen sampai energi ikatan kovalen lemah. Itu sebabnya ia tampak dalam data termodinamika. Angka spin rendah yang sangat besar menyesatkan bila dibaca sendiri: dari angka itu harus dikurangkan energi pemasangan dua pasangan tambahan (sekitar 2 × 20 000 cm⁻¹), dan juga harus diingat bahwa ESMK diukur terhadap pusat berat orbital d yang sendiri sudah dinaikkan oleh ligan. ESMK adalah koreksi kecil pada energi total kompleks yang ribuan kJ/mol, tetapi koreksi kecil itulah yang berbeda dari satu unsur ke unsur berikutnya.
:::

### Entalpi hidrasi dan jari-jari ion

Entalpi hidrasi ion M²⁺, yaitu perubahan entalpi ketika ion gas masuk ke dalam air, seharusnya makin negatif secara teratur dari Ca²⁺ ke Zn²⁺, karena jari-jari ion menyusut ketika muatan inti bertambah dan elektron d menyaringnya tidak sempurna. Data menunjukkan pola lain. Nilainya memang makin negatif secara umum, tetapi berbentuk dua punuk: V²⁺ dan Ni²⁺ terlalu negatif, sedangkan Mn²⁺ jatuh kembali ke garis lurus yang menghubungkan Ca²⁺ dan Zn²⁺ (Gambar 14.g2).

Teori medan kristal menjelaskan pola ini dengan sederhana. Ion gas tidak mempunyai ESMK, sedangkan ion terhidrasi [M(H₂O)₆]²⁺ mempunyai ESMK oktahedral. Jadi entalpi hidrasi terukur mengandung ESMK sebagai suku tambahan:

$$
\Delta H_\text{hid} = \Delta H_\text{hid}^\text{bola} + \text{ESMK} . \qquad \text{(14.eb1)}
$$

Jika ESMK yang dihitung dari spektrum dikurangkan dari data, titik-titiknya jatuh hampir pada garis lurus. Untuk Ca²⁺, Mn²⁺, dan Zn²⁺ (d⁰, d⁵ spin tinggi, d¹⁰) koreksi itu nol; ketiga ion inilah yang menentukan garis dasar.

![Gambar 14.g2 (a) Entalpi hidrasi ion M²⁺ periode 4 (lingkaran biru) dan nilainya setelah ESMK dikurangkan (segitiga jingga). Garis putus-putus menghubungkan Ca²⁺, Mn²⁺, dan Zn²⁺, yang ESMK-nya nol. (b) Jari-jari ion M²⁺ oktahedral spin tinggi menurut Shannon. Kedua sifat memperlihatkan pola dua punuk yang sama.](fig/c_hidrasi.png){width=92%}

Jari-jari ion memperlihatkan pola yang serupa tetapi terbalik. Untuk d¹–d³, elektron tambahan masuk $t_{2g}$, yang cupingnya di antara ligan, sehingga tidak menghalangi ligan mendekat: ion menyusut lebih cepat daripada garis dasar. Untuk d⁴–d⁵, elektron masuk $e_g$ yang menunjuk ke ligan dan mendorongnya menjauh: jari-jari naik kembali. Pola ini berulang untuk d⁶–d¹⁰. Ion spin rendah lebih kecil daripada pasangan spin tingginya; Fe²⁺ spin rendah, misalnya, sekitar 0,17 Å lebih kecil.

::: {.contoh}
**Contoh 14.b2 · Mengoreksi entalpi hidrasi**

Entalpi hidrasi ion M²⁺ (kJ/mol, dibulatkan; konvensi $\Delta H_\text{hid}(\text{H}^+) = -1091$ kJ/mol): Ca −1580, V −1920, Cr −1905, Mn −1840, Fe −1945, Co −2000, Ni −2105, Cu −2100, Zn −2045. Dengan $\Delta_o$ ion heksaakua dari Tabel 14.1 (Cr²⁺: 13 900 cm⁻¹), kurangkan ESMK dan bandingkan dengan garis lurus Ca–Mn–Zn.

**Penyelesaian.** ESMK (kJ/mol): V²⁺ (d³) $-1{,}2 \times 12\,400 \times 0{,}011\,963 = -178$; Cr²⁺ (d⁴) $-0{,}6 \times 13\,900 \times 0{,}011\,963 = -99{,}8$; Fe²⁺ $-49{,}8$; Co²⁺ (d⁷) $-0{,}8 \times 9300 \times 0{,}011\,963 = -89{,}0$; Ni²⁺ $-122$; Cu²⁺ (d⁹) $-0{,}6 \times 12\,600 \times 0{,}011\,963 = -90{,}4$. Nilai terkoreksi dan garis dasar (interpolasi linear Ca → Mn untuk d¹–d⁴, Mn → Zn untuk d⁶–d⁹):

| Ion | Terukur | Terkoreksi | Garis dasar | Sisa |
|---|---|---|---|---|
| V²⁺ | −1920 | −1742 | −1736 | −6 |
| Cr²⁺ | −1905 | −1805 | −1788 | −17 |
| Fe²⁺ | −1945 | −1895 | −1881 | −14 |
| Co²⁺ | −2000 | −1911 | −1922 | +11 |
| Ni²⁺ | −2105 | −1983 | −1963 | −20 |
| Cu²⁺ | −2100 | −2010 | −2004 | −6 |

**Memahami hasil.** Penyimpangan sebesar 50–180 kJ/mol menyusut menjadi kurang dari 20 kJ/mol, sekitar 1% dari entalpi hidrasi. Sisa sekecil itu wajar, karena data termokimia mempunyai ketidakpastian seukuran itu dan karena Cr²⁺ dan Cu²⁺ masih memperoleh energi Jahn–Teller tambahan (subbab 14.6). Inilah salah satu bukti termodinamika terkuat bahwa pemecahan orbital d yang diukur dari **warna** kompleks benar-benar menyimpan energi yang tampak dalam **kalorimetri**.
:::

::: {.contoh}
**Contoh 14.b3 · Jari-jari ion**

Jari-jari ion M²⁺ oktahedral spin tinggi (Å): Ca 1,00; Ti 0,86; V 0,79; Cr 0,80; Mn 0,83; Fe 0,78; Co 0,745; Ni 0,69; Cu 0,73; Zn 0,74. (a) Bandingkan dengan garis lurus Ca–Zn. (b) Jelaskan minimum di V²⁺ dan Ni²⁺.

**Penyelesaian.** (a) Garis Ca–Zn menurun 0,026 Å per elektron d. Nilainya untuk V (d³) 0,922, Mn (d⁵) 0,870, Ni (d⁸) 0,792. Jari-jari terukur V²⁺ 0,13 Å dan Ni²⁺ 0,10 Å di bawah garis, sedangkan Mn²⁺ hanya 0,04 Å di bawahnya.

(b) Pada V²⁺ ($t_{2g}^3$) dan Ni²⁺ ($t_{2g}^6e_g^2$), orbital $t_{2g}$ terisi sebanyak mungkin relatif terhadap $e_g$. Rapat elektron di arah ligan paling kecil, sehingga ligan dapat mendekat. Setiap elektron $e_g$ (d⁴, d⁵, d⁹, d¹⁰) menambah tolakan tepat di arah ikatan.

**Memahami hasil.** Garis Ca–Zn sendiri tidak melewati Mn²⁺ dengan tepat karena penyaringan muatan inti oleh elektron d juga tidak seragam. Namun, pola dua punuk jelas sekali. Ukuran ion menentukan banyak sifat lain: Ni²⁺ yang kecil membentuk ikatan lebih kuat dengan air dan ligan lain, salah satu penyebab deret Irving–Williams di bawah.
:::

### Spinel: memilih lubang oktahedral atau tetrahedral

**Spinel** adalah oksida AB₂O₄ dengan anion oksida tersusun kubus mampat. Dari setiap delapan satuan rumus, kation menempati 8 lubang tetrahedral dan 16 lubang oktahedral. Dalam **spinel normal**, ion A²⁺ menempati lubang tetrahedral dan B³⁺ lubang oktahedral: A[B₂]O₄ (kurung siku menandai lubang oktahedral). Dalam **spinel terbalik**, separuh ion B³⁺ menempati lubang tetrahedral dan ion A²⁺ pindah ke lubang oktahedral: B[AB]O₄.

Untuk ion tanpa ESMK (d⁰, d⁵ spin tinggi, d¹⁰), pilihan lubang ditentukan oleh ukuran dan energi Madelung, yang umumnya memihak spinel normal. Untuk ion lain, ESMK menambah preferensi. Selisih ESMK oktahedral dan tetrahedral disebut **energi preferensi lubang oktahedral** (EPLO):

$$
\text{EPLO} = \text{ESMK}_\text{okt} - \text{ESMK}_\text{tet} . \qquad \text{(14.eb2)}
$$

Dari Tabel 14.2, EPLO (spin tinggi) bernilai 0; −1,33; −2,67; −8,44; −4,22; 0; −1,33; −2,67; −8,44; −4,22; 0 $Dq$ untuk d⁰ sampai d¹⁰. Ion d³ dan d⁸ paling kuat menuntut lubang oktahedral.

::: {.contoh}
**Contoh 14.b4 · Magnetit adalah spinel terbalik**

Magnetit, Fe₃O₄ = Fe²⁺Fe³⁺₂O₄, adalah spinel terbalik, sedangkan Mn₃O₄ dan Co₃O₄ adalah spinel normal. Jelaskan dengan EPLO. Pakai $\Delta_o$ dalam oksida kira-kira sama dengan ion heksaakua: Fe²⁺ 10 400; Fe³⁺ 14 000; Mn³⁺ 21 000; Co³⁺ 18 200 cm⁻¹.

**Penyelesaian.**

- Fe₃O₄: Fe²⁺ (d⁶ spin tinggi) mempunyai EPLO $-1{,}33Dq = -0{,}133 \times 10\,400 \times 0{,}011\,963 = -16{,}5$ kJ/mol. Fe³⁺ (d⁵ spin tinggi) EPLO nol. Hanya Fe²⁺ yang "menuntut" lubang oktahedral, sehingga Fe²⁺ masuk lubang oktahedral dan separuh Fe³⁺ terdesak ke lubang tetrahedral: Fe³⁺[Fe²⁺Fe³⁺]O₄, spinel terbalik.
- Mn₃O₄: Mn²⁺ (d⁵) EPLO nol, sedangkan Mn³⁺ (d⁴ spin tinggi) EPLO $-0{,}422 \times 21\,000 \times 0{,}011\,963 = -106$ kJ/mol. Mn³⁺ tetap di lubang oktahedral: Mn²⁺[Mn³⁺₂]O₄, spinel normal.
- Co₃O₄: Co³⁺ (d⁶) dalam oksida berspin rendah dengan ESMK oktahedral $-24Dq$, sedangkan di lubang tetrahedral ia harus berspin tinggi ($-2{,}67Dq$). EPLO sekitar $-21Dq \approx -460$ kJ/mol (sebelum dikurangi energi pemasangan): spinel normal.

**Memahami hasil.** Selisih 16,5 kJ/mol pada Fe²⁺ tampak kecil, tetapi cukup untuk membalik struktur ketika ion pesaingnya tidak mempunyai preferensi sama sekali. Struktur terbalik magnetit menempatkan Fe²⁺ dan Fe³⁺ berdampingan di lubang oktahedral, sehingga elektron dapat melompat di antara keduanya. Itulah sebabnya magnetit menghantarkan listrik jauh lebih baik daripada kebanyakan oksida, dan susunan momen magnet Fe³⁺ tetrahedral yang antiparalel dengan ion oktahedral menghasilkan ferimagnetisme, magnet alami tertua yang dikenal manusia.
:::

::: {.contoh}
**Contoh 14.b5 · Ferit dan kromit**

Ramalkan apakah NiFe₂O₄, ZnFe₂O₄, dan NiCr₂O₄ normal atau terbalik. Pakai EPLO Ni²⁺ $-86$ kJ/mol, Cr³⁺ $-176$ kJ/mol, Zn²⁺ dan Fe³⁺ nol.

**Penyelesaian.** NiFe₂O₄: Ni²⁺ menuntut lubang oktahedral, Fe³⁺ tidak peduli: terbalik, Fe³⁺[Ni²⁺Fe³⁺]O₄. ZnFe₂O₄: tidak ada ion yang menuntut; faktor ukuran dan Madelung memihak normal, Zn²⁺[Fe³⁺₂]O₄. NiCr₂O₄: keduanya menuntut lubang oktahedral, tetapi Cr³⁺ lebih kuat dan lebih banyak; Ni²⁺ terpaksa tetrahedral: normal, Ni²⁺[Cr³⁺₂]O₄.

**Memahami hasil.** Ketiga ramalan sesuai dengan struktur teramati. NiCr₂O₄ menarik karena Ni²⁺ tetrahedral (d⁸, keadaan dasar $^3T_1$ berdegenerasi orbital) mengalami distorsi Jahn–Teller yang membuat kisi kubusnya menjadi tetragonal di bawah sekitar 310 K. Ferit nikel dan seng adalah bahan magnet lunak untuk inti transformator frekuensi tinggi; sifat magnetnya dapat diatur dengan mencampur keduanya, karena Zn²⁺ yang memaksa Fe³⁺ pindah lubang mengubah keseimbangan momen antara kedua jenis lubang.
:::

### Deret Irving–Williams

Tetapan kestabilan kompleks M²⁺ periode 4 dengan hampir semua ligan nitrogen dan oksigen mengikuti urutan

$$
\text{Mn}^{2+} < \text{Fe}^{2+} < \text{Co}^{2+} < \text{Ni}^{2+} < \text{Cu}^{2+} > \text{Zn}^{2+} , \qquad \text{(14.eb3)}
$$

yang ditemukan Irving dan Williams pada 1953. Kenaikan dari Mn²⁺ ke Ni²⁺ mengikuti mengecilnya jari-jari ion dan naiknya ESMK (ligan nitrogen lebih kuat daripada air, sehingga penggantian air oleh ligan menambah ESMK). Puncak di Cu²⁺, padahal ESMK d⁹ lebih kecil daripada d⁸, berasal dari efek Jahn–Teller: tembaga(II) membentuk empat ikatan ekuator yang sangat pendek dan kuat (subbab 14.6). Zn²⁺ tanpa ESMK turun kembali.

::: {.contoh}
**Contoh 14.b6 · Kestabilan kompleks etilenadiamina**

Nilai $\log K_1$ untuk [M(en)]²⁺ adalah Mn 2,73; Fe 4,28; Co 5,89; Ni 7,52; Cu 10,55; Zn 5,71. Hitung $\Delta G°$ pembentukannya pada 298 K dan selisih Ni–Zn serta Cu–Zn.

**Penyelesaian.** $\Delta G° = -RT\ln10\cdot\log K = -5{,}708\log K$ kJ/mol. Hasilnya: Mn −15,6; Fe −24,4; Co −33,6; Ni −42,9; Cu −60,2; Zn −32,6 kJ/mol. Selisih Ni − Zn = −10,3 kJ/mol; Cu − Zn = −27,6 kJ/mol.

**Memahami hasil.** Untuk satu ligan en yang menggantikan dua molekul air, $\Delta_o$ naik dari $f = 1{,}00$ ke $f = 1{,}28$ untuk dua dari enam posisi, sehingga ESMK Ni²⁺ bertambah kira-kira $1{,}2 \times (0{,}28 \times \tfrac26) \times 8500 \times 0{,}011\,963 = 11$ kJ/mol. Angka ini hampir persis selisih Ni − Zn. Deret Irving–Williams sangat penting dalam biokimia: ia menjelaskan mengapa protein harus memakai mekanisme khusus (tempat pengikatan dengan geometri tertentu, kompartemen sel) agar enzim yang memerlukan Mn²⁺ atau Fe²⁺ tidak "dicuri" oleh Cu²⁺ atau Zn²⁺.
:::

### Kelembaman kinetik

ESMK juga memengaruhi **laju** reaksi substitusi ligan. Dalam mekanisme disosiatif, kompleks oktahedral melepas satu ligan dan melewati keadaan transisi piramida bujur sangkar berkoordinasi lima. Jika ESMK piramida bujur sangkar lebih kecil daripada ESMK oktahedral, selisihnya, yang disebut **energi aktivasi medan ligan** (EAML), menambah tinggi penghalang reaksi. Dengan energi orbital piramida bujur sangkar dari model muatan titik ($d_{x^2-y^2}$ 9,14; $d_{z^2}$ 0,86; $d_{xy}$ −0,86; $d_{xz}$, $d_{yz}$ −4,57, dalam $Dq$), dan dengan menjaga banyaknya elektron tak berpasangan, diperoleh EAML (dalam $Dq$):

| $d^n$ | d¹ | d² | d³ | d⁴ ST | d⁴ SR | d⁵ ST | d⁵ SR | d⁶ ST | d⁶ SR | d⁷ ST | d⁸ | d⁹ | d¹⁰ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EAML | −0,57 | −1,14 | **2,00** | −3,14 | 1,43 | 0 | 0,86 | −0,57 | **4,00** | −1,14 | **2,00** | −3,14 | 0 |

: Tabel 14.3 Energi aktivasi medan ligan untuk jalur disosiatif oktahedral → piramida bujur sangkar (ST = spin tinggi, SR = spin rendah). Nilai positif memperlambat reaksi.

Konfigurasi d³ dan d⁶ spin rendah kehilangan ESMK paling banyak. Untuk Cr³⁺ dengan $Dq \approx 1740$ cm⁻¹, EAML sekitar 3500 cm⁻¹ = 42 kJ/mol; untuk Co³⁺ spin rendah sekitar 9000 cm⁻¹ = 110 kJ/mol. Kompleks Cr(III) dan Co(III) memang terkenal **lembam**: substitusinya berlangsung dalam jam sampai hari, sehingga Werner dapat memisahkan isomer-isomernya dan membuktikan geometri oktahedral seabad yang lalu.

::: {.contoh}
**Contoh 14.b7 · Laju pertukaran air**

Tetapan laju pertukaran molekul air dalam [M(H₂O)₆]ⁿ⁺ pada 298 K kira-kira: V²⁺ 9 × 10¹ s⁻¹; Cr³⁺ 2 × 10⁻⁶ s⁻¹; Mn²⁺ 2 × 10⁷ s⁻¹; Fe²⁺ 4 × 10⁶ s⁻¹; Co²⁺ 3 × 10⁶ s⁻¹; Ni²⁺ 3 × 10⁴ s⁻¹; Cu²⁺ 4 × 10⁹ s⁻¹. (a) Hitung waktu paruh pertukaran untuk Cr³⁺ dan Ni²⁺. (b) Jelaskan urutannya dengan Tabel 14.3.

**Penyelesaian.** (a) $t_{1/2} = \ln2/k$. Cr³⁺: $0{,}693/(2 \times 10^{-6}) = 3{,}5 \times 10^5$ s, sekitar 4 hari. Ni²⁺: $0{,}693/(3 \times 10^4) = 2{,}3 \times 10^{-5}$ s = 23 µs.

(b) Ion dengan EAML positif (V²⁺ d³, Ni²⁺ d⁸, Cr³⁺ d³) paling lambat; ion dengan EAML nol atau negatif (Mn²⁺, Fe²⁺, Co²⁺) cepat. Untuk Cr³⁺ dan V²⁺ yang sama-sama d³, muatan +3 dan $\Delta_o$ yang lebih besar membuat Cr³⁺ jauh lebih lambat. Cu²⁺ paling cepat karena dua ligan aksialnya yang terikat lemah (efek Jahn–Teller) mudah lepas.

**Memahami hasil.** Rentang lajunya enam belas orde besaran untuk ion-ion yang ukuran dan muatannya hampir sama. EAML tidak menjelaskan seluruhnya (muatan dan jari-jari juga penting), tetapi ia menangkap pola yang paling mencolok, yaitu "kelembaman d³ dan d⁶ spin rendah". Pengetahuan ini dipakai merancang obat logam: cisplatin dan kompleks Ru(II) atau Co(III) dirancang lembam supaya sampai ke sasarannya utuh, sedangkan zat kontras MRI berbasis Gd³⁺ memerlukan pertukaran air yang cepat agar efektif.
:::

::: {.kuis}
**Kuis cepat 14.4**

Mengapa entalpi hidrasi Mn²⁺ terletak pada garis lurus Ca²⁺–Zn²⁺, sedangkan entalpi hidrasi Mn³⁺ (d⁴) tidak akan terletak pada garis serupa untuk ion M³⁺?
:::

## 14.5 Spin tinggi dan spin rendah; magnetisme

### Energi pemasangan

Untuk d⁴ sampai d⁷ oktahedral, elektron dapat memilih antara menaikkan diri ke $e_g$ atau berpasangan di $t_{2g}$. Biaya pilihan kedua disebut **energi pemasangan** $P$. Asal-usulnya ada dua, keduanya dari tolakan elektron (subbab 9.10 dan 9.12):

1. **Tolakan Coulomb.** Dua elektron dalam satu orbital rata-rata lebih dekat satu sama lain daripada dua elektron dalam orbital berbeda, sehingga tolakannya lebih besar.
2. **Hilangnya energi pertukaran.** Elektron-elektron dengan spin sejajar saling menghindar karena asas Pauli (lubang Fermi), sehingga setiap pasangan elektron berspin sejajar memperoleh stabilisasi pertukaran $K$. Memasangkan elektron mengurangi banyaknya pasangan berspin sejajar.

Bagian kedua dapat dihitung dengan menghitung pasangan. Untuk $n_\uparrow$ elektron berspin atas dan $n_\downarrow$ berspin bawah, banyaknya pasangan sejajar adalah

$$
N_\parallel = \tfrac12n_\uparrow(n_\uparrow - 1) + \tfrac12n_\downarrow(n_\downarrow - 1) . \qquad \text{(14.eb4)}
$$

d⁵ spin tinggi (5↑) mempunyai 10 pasangan sejajar; d⁵ spin rendah (3↑ 2↓) hanya 3 + 1 = 4. Berpindah ke spin rendah mengorbankan 6 pasangan, kira-kira $6K$. Untuk d⁶ (5↑1↓ dibanding 3↑3↓) hilang 10 − 6 = 4 pasangan; untuk d⁴ (4↑ dibanding 3↑1↓) hilang 3; untuk d⁷ (5↑2↓ dibanding 4↑3↓) hilang 11 − 9 = 2. Perhitungan kasar ini sudah meramalkan bahwa d⁵ paling enggan berspin rendah dan d⁶ serta d⁷ paling mudah.

Perhitungan yang tepat memerlukan teori atom berelektron banyak dengan parameter Racah $B$ dan $C$ (subbab 14.9). Griffith menurunkan energi pemasangan rata-rata per pasangan untuk ion bebas:

$$
P(\text{d}^4) = 6B + 5C, \quad P(\text{d}^5) = 7{,}5B + 5C, \quad P(\text{d}^6) = 2{,}5B + 4C, \quad P(\text{d}^7) = 4B + 4C . \qquad \text{(14.eb5)}
$$

Kompleks berspin rendah bila $\Delta_o > P$. Karena $C \approx 4B$ sampai $5B$, $P(\text{d}^6)$ dan $P(\text{d}^7)$ jauh lebih kecil daripada $P(\text{d}^4)$ dan $P(\text{d}^5)$, cocok dengan hitungan pasangan di atas. Untuk memeriksa (14.eb5) secara mandiri, kita dapat mendiagonalkan Hamiltonian lengkap kulit $d^n$ dalam medan oktahedral (program di subbab 14.10) dan mencari $\Delta_o$ ketika keadaan dasar berganti spin. Dengan $C/B = 4{,}8$, persilangannya terjadi pada $\Delta_o/B$ = 28,3 (d⁴), 29,9 (d⁵), 20,0 (d⁶), dan 22,3 (d⁷), sedangkan (14.eb5) memberi 30,0; 31,5; 21,7; dan 23,2. Rumus Griffith menaksir 3–8% terlalu tinggi karena mengabaikan pencampuran konfigurasi, tetapi urutannya tepat.

| Ion | $d^n$ | $P$ ion bebas (cm⁻¹) | Kompleks | $\Delta_o$ (cm⁻¹) | Ramalan | Teramati |
|---|---|---|---|---|---|---|
| Cr²⁺ | d⁴ | 23 500 | [Cr(H₂O)₆]²⁺ | 13 900 | ST | ST |
| Mn³⁺ | d⁴ | 28 000 | [Mn(H₂O)₆]³⁺ | 21 000 | ST | ST |
| Mn²⁺ | d⁵ | 25 500 | [Mn(H₂O)₆]²⁺ | 8 500 | ST | ST |
| Fe³⁺ | d⁵ | 30 000 | [Fe(H₂O)₆]³⁺ | 14 000 | ST | ST |
| Fe³⁺ | d⁵ | 30 000 | [Fe(CN)₆]³⁻ | 35 000 | SR | SR |
| Fe²⁺ | d⁶ | 17 600 | [Fe(H₂O)₆]²⁺ | 10 400 | ST | ST |
| Fe²⁺ | d⁶ | 17 600 | [Fe(CN)₆]⁴⁻ | 33 800 | SR | SR |
| Co³⁺ | d⁶ | 21 000 | [CoF₆]³⁻ | 13 000 | ST | ST |
| Co³⁺ | d⁶ | 21 000 | [Co(NH₃)₆]³⁺ | 22 900 | SR | SR |
| Co²⁺ | d⁷ | 22 500 | [Co(H₂O)₆]²⁺ | 9 300 | ST | ST |

: Tabel 14.4 Energi pemasangan ion bebas (taksiran dari spektrum atom) dan keadaan spin kompleks (ST = spin tinggi, SR = spin rendah).

::: {.contoh}
**Contoh 14.b8 · Kasus perbatasan: [Co(H₂O)₆]³⁺**

[Co(H₂O)₆]³⁺ dengan $\Delta_o = 18\,200$ cm⁻¹ ternyata diamagnetik (spin rendah), padahal $P$ ion bebas Co³⁺ 21 000 cm⁻¹. (a) Jelaskan dengan efek nefelauksetik: dalam kompleks, parameter tolakan elektron hanya sekitar 70–80% nilai ion bebas. (b) Berapa batas $P$ dalam kompleks agar ramalannya benar?

**Penyelesaian.** (a) $P$ sebanding dengan $B$ dan $C$. Bila keduanya menyusut menjadi 80% nilai ion bebas, $P \approx 0{,}80 \times 21\,000 = 16\,800$ cm⁻¹ < 18 200 cm⁻¹: spin rendah. (b) Diperlukan $P < 18\,200$, yaitu penyusutan paling sedikit $1 - 18\,200/21\,000 = 13\%$.

**Memahami hasil.** Orbital $e_g$ dan $t_{2g}$ dalam kompleks adalah orbital molekul yang sebagian berada pada ligan (subbab 14.7). Elektron d yang "tersebar" ke ligan saling menolak lebih lemah, sehingga $B$, $C$, dan $P$ mengecil. Untuk kompleks di dekat perbatasan, penyusutan ini menentukan hasil. [CoF₆]³⁻ ($\Delta_o \approx 13\,000$ cm⁻¹) jelas spin tinggi dan merupakan satu-satunya kompleks Co(III) sederhana yang paramagnetik. Perhitungan $P$ ion bebas yang "persis" pun tidak menolong untuk kasus perbatasan: keputusannya bergantung pada selisih dua besaran yang masing-masing sekitar 20 000 cm⁻¹.
:::

::: {.contoh}
**Contoh 14.b9 · Selisih energi spin tinggi–spin rendah**

Untuk [Fe(H₂O)₆]²⁺ dan [Fe(CN)₆]⁴⁻, hitung selisih energi keadaan spin rendah dan spin tinggi menurut model ESMK + pemasangan, memakai $P = 0{,}80 \times 17\,600$ cm⁻¹ dalam kompleks.

**Penyelesaian.** d⁶ spin rendah: ESMK $-24Dq = -2{,}4\Delta_o$, dengan dua pasangan tambahan. Spin tinggi: $-0{,}4\Delta_o$. Selisih $E_\text{SR} - E_\text{ST} = -2\Delta_o + 2P$, dengan $P = 14\,080$ cm⁻¹.

- [Fe(H₂O)₆]²⁺: $-2(10\,400) + 2(14\,080) = +7360$ cm⁻¹ (= +88 kJ/mol). Spin tinggi lebih stabil.
- [Fe(CN)₆]⁴⁻: $-2(33\,800) + 2(14\,080) = -39\,440$ cm⁻¹ (= −472 kJ/mol). Spin rendah jauh lebih stabil.

**Memahami hasil.** Selisih untuk kedua kompleks jauh dari nol, sehingga keadaan spinnya tidak berubah dengan suhu. Untuk mendapat **transisi spin**, $\Delta_o$ harus sangat dekat dengan $P$, dengan selisih energi elektronik hanya beberapa ratus cm⁻¹, seukuran $kT$ (208 cm⁻¹ pada 298 K). Ligan nitrogen heterosiklik seperti fenantrolina, bipiridina, atau triazol sering memberi $\Delta_o$ di wilayah sempit itu untuk Fe(II).
:::

### Momen magnet

Elektron tak berpasangan membuat kompleks **paramagnetik**: tertarik ke daerah medan magnet kuat. Momen magnet satu atom atau ion dengan bilangan kuantum spin total $S$ dan momentum sudut orbital yang "terpadamkan" (penjelasannya di bawah) adalah

$$
\mu_\text{eff} = g_e\sqrt{S(S + 1)}\,\mu_B \approx \sqrt{n(n + 2)}\,\mu_B , \qquad \text{(14.eb6)}
$$

dengan $n = 2S$ banyaknya elektron tak berpasangan, $g_e = 2{,}0023 \approx 2$, dan $\mu_B = 9{,}274 \times 10^{-24}$ J/T magneton Bohr. Rumus **spin saja** ini memberi 1,73; 2,83; 3,87; 4,90; dan 5,92 µ_B untuk $n = 1$ sampai 5.

Yang diukur di laboratorium adalah kerentanan magnet molar $\chi_M$. Untuk zat paramagnetik ideal berlaku **hukum Curie**, yang diturunkan dengan merata-ratakan orientasi momen menurut distribusi Boltzmann dalam medan lemah:

$$
\chi_M = \frac{N_A\mu_0\mu_\text{eff}^2}{3kT}, \qquad \mu_\text{eff} = \sqrt{\frac{3k}{N_A\mu_0}}\,\sqrt{\chi_MT} = 797{,}7\sqrt{\chi_MT}\ \mu_B , \qquad \text{(14.eb7)}
$$

dengan $\chi_M$ dalam m³ mol⁻¹. Dalam satuan cgs yang masih banyak dipakai kimiawan, $\mu_\text{eff} = 2{,}828\sqrt{\chi_MT}$ dengan $\chi_MT$ dalam cm³ K mol⁻¹. Kerentanan diukur dengan neraca Gouy (perubahan berat sampel dalam medan magnet), metode Evans (geseran sinyal NMR pelarut, Bab 16), atau magnetometer SQUID.

::: {.contoh}
**Contoh 14.b10 · Dari $\chi_MT$ ke banyaknya elektron tak berpasangan**

Hasil pengukuran $\chi_MT$ (cm³ K mol⁻¹) pada suhu kamar: (a) garam Mohr, (NH₄)₂Fe(SO₄)₂·6H₂O, 3,4; (b) K₃[Fe(CN)₆], 0,66; (c) [Cr(NH₃)₆]Cl₃, 1,85. Tentukan $\mu_\text{eff}$ dan banyaknya elektron tak berpasangan.

**Penyelesaian.** $\mu_\text{eff} = 2{,}828\sqrt{\chi_MT}$. (a) $2{,}828\sqrt{3{,}4} = 5{,}21$ µ_B. Nilai terdekat rumus spin saja 4,90 ($n = 4$): Fe²⁺ spin tinggi. (b) $2{,}828\sqrt{0{,}66} = 2{,}30$ µ_B. Terdekat 1,73 ($n = 1$): Fe³⁺ spin rendah $t_{2g}^5$. (c) $2{,}828\sqrt{1{,}85} = 3{,}85$ µ_B, sangat dekat dengan 3,87 ($n = 3$): Cr³⁺ $t_{2g}^3$.

**Memahami hasil.** Kecocokan dengan rumus spin saja sangat baik untuk Cr³⁺, tetapi untuk Fe²⁺ dan [Fe(CN)₆]³⁻ nilai terukur jelas di atas nilai spin saja. Selisih ini bukan galat percobaan; ia mencerminkan sumbangan momentum sudut orbital yang tidak padam sepenuhnya. Walaupun demikian, $n$ selalu dapat ditentukan tanpa keraguan, karena selisih antara nilai-nilai spin saja yang berurutan (sekitar 1 µ_B) lebih besar daripada sumbangan orbital.
:::

### Pemadaman momentum sudut orbital

Mengapa sumbangan orbital biasanya kecil? Dalam ion bebas, elektron dapat beredar mengelilingi inti dalam orbital kompleks $d_{\pm1}$ atau $d_{\pm2}$ yang membawa momentum sudut $m_\ell\hbar$. Agar momentum sudut terhadap suatu sumbu tetap ada dalam kompleks, harus ada orbital-orbital yang **berdegenerasi** dan dapat diubah satu sama lain dengan rotasi di sekitar sumbu itu. Dalam medan oktahedral, $d_{xz}$ dan $d_{yz}$ berubah satu ke yang lain dengan rotasi 90° di sekitar sumbu $z$, dan keduanya berdegenerasi; demikian pula $d_{xy}$ dan $d_{xz}$ terhadap sumbu $x$. Jadi elektron dalam $t_{2g}$ dapat membawa momentum sudut orbital. Sebaliknya, $d_{z^2}$ dan $d_{x^2-y^2}$ tidak dapat diubah satu ke yang lain dengan rotasi apa pun yang mempertahankan bentuknya; orbital $e_g$ tidak membawa momentum sudut. Secara formal, unsur matriks $\hat L_z$ di antara kedua fungsi $e_g$ nol.

Akibatnya, momentum sudut orbital hanya "selamat" dalam keadaan dasar berlambang $T$, yaitu ketika ada lubang atau elektron yang dapat berpindah di antara orbital $t_{2g}$ yang tidak terisi seragam: $t_{2g}^1$, $t_{2g}^2$, $t_{2g}^4$, $t_{2g}^5$ dan versi spin tingginya. Keadaan dasar $A$ dan $E$ (misalnya $t_{2g}^3$, $t_{2g}^3e_g^2$, $t_{2g}^6e_g^2$) momentum sudut orbitalnya **padam**. Bahkan untuk keadaan $A$ dan $E$, kopling spin–orbit mencampurkan sedikit keadaan tereksitasi $T$, dan momen magnet menjadi

$$
\mu_\text{eff} = \mu_\text{spin saja}\left(1 - \frac{\alpha\lambda}{\Delta_o}\right), \qquad \alpha = 4\ (A_2),\ 2\ (E) , \qquad \text{(14.eb8)}
$$

dengan $\lambda$ tetapan kopling spin–orbit ion bebas (positif untuk kulit kurang dari setengah penuh, negatif untuk lebih dari setengah penuh; subbab 9.13).

::: {.contoh}
**Contoh 14.b11 · Momen magnet nikel(II)**

Untuk [Ni(H₂O)₆]²⁺, keadaan dasar $^3A_{2g}$ ($t_{2g}^6e_g^2$), $\lambda = -315$ cm⁻¹ dan $\Delta_o = 8500$ cm⁻¹. Hitung $\mu_\text{eff}$ dengan (14.eb8) dan bandingkan dengan nilai terukur, sekitar 3,2 µ_B. Lakukan hal yang sama untuk [Cr(H₂O)₆]³⁺ ($^4A_{2g}$, $\lambda = +91$ cm⁻¹, $\Delta_o = 17\,400$ cm⁻¹; terukur 3,8 µ_B).

**Penyelesaian.** Ni²⁺: $2{,}828 \times (1 + 4 \times 315/8500) = 2{,}828 \times 1{,}148 = 3{,}25$ µ_B. Cr³⁺: $3{,}873 \times (1 - 4 \times 91/17\,400) = 3{,}873 \times 0{,}979 = 3{,}79$ µ_B.

**Memahami hasil.** Kedua ramalan cocok dengan percobaan dalam 0,05 µ_B. Tanda $\lambda$ menentukan arah koreksi: untuk kulit lebih dari setengah penuh (Ni²⁺, Cu²⁺, Co²⁺), $\mu_\text{eff}$ di atas nilai spin saja; untuk kulit kurang dari setengah penuh (Cr³⁺, V²⁺), sedikit di bawahnya. Faktor $g$ yang terukur dalam spektroskopi resonansi spin elektron (Bab 16) memberi informasi yang sama secara lebih langsung: untuk Ni²⁺ oktahedral, $g \approx 2{,}25$.
:::

### Transisi spin

Bila $\Delta_o \approx P$, kedua keadaan spin dapat berada dalam kesetimbangan termal:

$$
\text{SR} \rightleftharpoons \text{ST}, \qquad K = \frac{\gamma_\text{ST}}{1 - \gamma_\text{ST}} = \exp\left(-\frac{\Delta H - T\Delta S}{RT}\right) , \qquad \text{(14.eb9)}
$$

dengan $\gamma_\text{ST}$ fraksi molekul spin tinggi. Perubahan entalpi $\Delta H$ positif (spin rendah lebih stabil pada energi) dan perubahan entropi $\Delta S$ juga positif. Entropinya berasal dari dua sumber: degenerasi spin (keadaan $^5T_{2g}$ mempunyai $2S + 1 = 5$ kali lebih banyak keadaan daripada $^1A_{1g}$, memberi $R\ln5 = 13{,}4$ J K⁻¹ mol⁻¹, ditambah degenerasi orbital) dan, yang lebih besar, getaran: ikatan Fe–N dalam keadaan spin tinggi lebih panjang dan lebih lemah, sehingga frekuensi getarannya lebih rendah dan tingkat-tingkat getarannya lebih rapat (subbab 5.4). Pada suhu rendah $\Delta H$ menang dan kompleks berspin rendah; pada suhu tinggi $T\Delta S$ menang. Suhu tengah, ketika $\gamma_\text{ST} = \tfrac12$, adalah $T_{1/2} = \Delta H/\Delta S$.

![Gambar 14.g3 (a) Energi keadaan $^5T_{2g}$ (spin tinggi) dan $^1A_{1g}$ (spin rendah) kompleks d⁶ oktahedral relatif terhadap keadaan dasar, dihitung dengan diagonalisasi lengkap kulit d⁶ ($C/B = 4{,}8$). Kedua keadaan bersilangan pada $\Delta_o/B = 20{,}0$. (b) Fraksi spin tinggi terhadap suhu untuk [Fe(phen)₂(NCS)₂] menurut model kesetimbangan sederhana (biru) dan, sebagai ilustrasi, bentuk transisi tajam yang teramati dalam padatan akibat kooperativitas (jingga).](fig/c_spin.png){width=92%}

::: {.contoh}
**Contoh 14.b12 · Kompleks transisi spin klasik**

Untuk padatan [Fe(phen)₂(NCS)₂], $\Delta H = 8{,}6$ kJ/mol dan $\Delta S = 48{,}8$ J K⁻¹ mol⁻¹. (a) Hitung $T_{1/2}$. (b) Hitung $\gamma_\text{ST}$ menurut (14.eb9) pada 150, 200, dan 300 K. (c) Berapa bagian $\Delta S$ yang berasal dari degenerasi spin?

**Penyelesaian.** (a) $T_{1/2} = 8600/48{,}8 = 176$ K.

(b) $\gamma_\text{ST} = K/(1 + K)$ dengan $K = \exp[-(8600 - 48{,}8T)/8{,}314T]$: pada 150 K, 0,26; pada 200 K, 0,67; pada 300 K, 0,92.

(c) $R\ln5 = 13{,}4$ J K⁻¹ mol⁻¹, sekitar 27% dari $\Delta S$. Sisanya terutama dari getaran.

**Memahami hasil.** Model kesetimbangan molekul-molekul bebas meramalkan transisi landai selebar lebih dari 100 K. Dalam kristal [Fe(phen)₂(NCS)₂] yang sebenarnya, transisi terjadi dalam rentang hanya beberapa kelvin di sekitar 176 K (Gambar 14.g3b). Penyebabnya **kooperativitas**: molekul spin tinggi lebih besar (ikatan Fe–N 0,2 Å lebih panjang), sehingga molekul yang berganti spin menekan atau melonggarkan tetangganya dan memaksa mereka mengikuti. Dalam beberapa senyawa, kooperativitas cukup kuat untuk menimbulkan histeresis: suhu transisi saat pemanasan dan pendinginan berbeda, sehingga materialnya "mengingat" riwayatnya. Senyawa seperti ini dikaji untuk sensor suhu, penyimpanan data, dan tampilan, karena perubahan spin disertai perubahan warna yang mencolok.
:::

::: {.terapan}
**Hemoglobin: transisi spin yang menghidupi kita**

Dalam deoksihemoglobin, Fe²⁺ berkoordinasi lima (empat N porfirin dan satu N histidina) dan berspin tinggi ($S = 2$). Ion spin tinggi ini terlalu besar untuk masuk ke rongga porfirin dan duduk sekitar 0,4 Å di atas bidangnya. Ketika O₂ terikat sebagai ligan keenam, medan ligan menguat dan besi menjadi diamagnetik secara keseluruhan (keadaan dasarnya sering dijelaskan sebagai Fe(III) spin rendah yang terkopel dengan superoksida). Ion yang menyusut masuk ke bidang porfirin dan menarik histidina, gerakan yang diteruskan ke antarmuka subunit protein dan memicu perubahan konformasi. Kooperativitas pengikatan oksigen dalam darah, yaitu kurva sigmoid yang membuat hemoglobin efektif melepas O₂ di jaringan, berawal dari perubahan jari-jari ion akibat perubahan keadaan spin.
:::

::: {.kuis}
**Kuis cepat 14.5**

Mengapa kompleks tetrahedral d⁴–d⁷ praktis selalu berspin tinggi? Mengapa momen magnet [Co(H₂O)₆]²⁺ (keadaan dasar $^4T_{1g}$) jauh di atas nilai spin saja, sedangkan [Ni(H₂O)₆]²⁺ hanya sedikit di atasnya?
:::

## 14.6 Efek Jahn–Teller

### Teorema

Pada 1937 Jahn dan Teller membuktikan teorema yang bunyinya singkat tetapi akibatnya luas: **molekul taklinear dalam keadaan elektronik yang berdegenerasi orbital tidak stabil terhadap distorsi tertentu yang menurunkan kesetangkupannya dan menghapus degenerasi itu.** Molekul "memilih" bentuk dengan kesetangkupan lebih rendah karena dengan demikian salah satu tingkat yang semula berdegenerasi turun energinya.

Alasannya dapat dilihat dari teori perturbasi. Misalkan $Q$ koordinat distorsi (perubahan geometri yang diukur dari bentuk setangkup), dengan $Q = 0$ geometri setangkup. Energi elektronik bergantung pada $Q$. Untuk keadaan tak berdegenerasi, $E(Q)$ hanya mengandung suku genap terendah $Q^2$ di sekitar bentuk setangkup, kecuali bila $Q$ bersetangkup penuh. Untuk keadaan berdegenerasi, perturbasi orde pertama tingkat terdegenerasi (subbab 8.9) memecah tingkat itu dengan pergeseran **sebanding dengan $Q$**, satu naik dan satu turun. Teori grup menjamin bahwa selalu ada distorsi tak setangkup penuh yang memberi pemecahan linear seperti itu bagi setiap molekul taklinear berdegenerasi. Energi elastik untuk mendistorsi kerangka sebanding dengan $Q^2$. Jumlah suku linear yang menurun dan suku kuadrat yang naik selalu mempunyai minimum di $Q \ne 0$:

$$
E_\pm(Q) = \tfrac12kQ^2 \pm AQ , \qquad \text{(14.ec1)}
$$

dengan $k$ tetapan gaya distorsi dan $A$ tetapan kopling Jahn–Teller. Cabang bawah mempunyai minimum di

$$
Q_0 = \frac{A}{k}, \qquad E_\text{JT} = -\frac{A^2}{2k} , \qquad \text{(14.ec2)}
$$

dan pada $Q_0$ kedua cabang terpisah sejauh $2AQ_0 = 4|E_\text{JT}|$. Bagian linear yang tidak pernah dapat dihilangkan menjamin bahwa minimum selalu ada; yang dapat dibantah hanyalah **besarnya**. Bila $E_\text{JT}$ lebih kecil daripada energi getaran titik nol, distorsi tidak teramati sebagai struktur statis.

### Konfigurasi yang terkena

Dalam kompleks oktahedral, degenerasi orbital ada bila $e_g$ atau $t_{2g}$ terisi tidak seragam. Distorsi yang berpasangan dengan degenerasi $e_g$ adalah ulur tetragonal (dua ikatan aksial memanjang, empat ekuator memendek, atau sebaliknya). Pemanjangan menurunkan $d_{z^2}$ sebesar $\tfrac12\delta_1$ dan menaikkan $d_{x^2-y^2}$ sebesar $\tfrac12\delta_1$, dengan $\delta_1$ sebanding dengan $Q$.

| Kekuatan | Konfigurasi | Contoh ion |
|---|---|---|
| Kuat ($e_g$ tak seragam) | $t_{2g}^3e_g^1$ (d⁴ ST), $t_{2g}^6e_g^1$ (d⁷ SR), $t_{2g}^6e_g^3$ (d⁹) | Cr²⁺, Mn³⁺; Co²⁺ SR, Ni³⁺; Cu²⁺, Ag²⁺ |
| Lemah ($t_{2g}$ tak seragam) | $t_{2g}^1$, $t_{2g}^2$, $t_{2g}^4$, $t_{2g}^5$ (SR), $t_{2g}^4e_g^2$ (d⁶ ST), $t_{2g}^5e_g^2$ (d⁷ ST) | Ti³⁺, V³⁺, Fe²⁺, Co²⁺ |
| Tidak ada | $t_{2g}^3$, $t_{2g}^3e_g^2$, $t_{2g}^6$, $t_{2g}^6e_g^2$, $t_{2g}^6e_g^4$ | Cr³⁺, Mn²⁺, Fe³⁺, Co³⁺ SR, Ni²⁺, Zn²⁺ |

: Tabel 14.5 Kecenderungan Jahn–Teller kompleks oktahedral.

Orbital $e_g$ menunjuk ke ligan, sehingga pengisiannya yang tidak seragam sangat peka terhadap panjang ikatan: efeknya kuat dan tampak dalam struktur kristal. Orbital $t_{2g}$ menunjuk di antara ligan, sehingga kopling dengan distorsi lemah, dan efeknya biasanya hanya tampak dalam spektroskopi.

Untuk d⁹, mengapa hampir selalu pemanjangan, bukan pemampatan? Hingga orde linear, kedua arah setara: pemampatan menempatkan lubang di $d_{z^2}$ dan memberi stabilisasi yang sama besar. Pemilihan arah datang dari suku orde lebih tinggi (anharmonisitas dan pencampuran $d_{z^2}$ dengan 4s), yang secara konsisten memihak pemanjangan. Pada permukaan energi yang lengkap, minimum $E_\text{JT}$ membentuk lembah melingkar yang disebut "topi Meksiko"; suku orde tinggi menimbulkan tiga lekukan setara pada lembah itu, masing-masing pemanjangan sepanjang salah satu dari ketiga sumbu.

![Gambar 14.g4 (a) Pemecahan orbital $e_g$ dan $t_{2g}$ akibat pemanjangan tetragonal; untuk d⁹, dua elektron turun dan satu naik. (b) Energi $E_\pm(Q) = \tfrac12kQ^2 \pm AQ$ untuk Cu²⁺ dengan $E_\text{JT} = 2000$ cm⁻¹ dan $Q_0 = 0{,}39$ Å. Minimum terletak di $\pm Q_0$, dan pada $Q_0$ kedua cabang terpisah $4E_\text{JT}$.](fig/c_jt.png){width=92%}

::: {.contoh}
**Contoh 14.c1 · Stabilisasi Jahn–Teller untuk d⁹**

Tunjukkan bahwa untuk konfigurasi $(d_{z^2})^2(d_{x^2-y^2})^1$ dengan pemecahan $E(d_{z^2}) = -AQ$ dan $E(d_{x^2-y^2}) = +AQ$, energi elektronik total adalah $-AQ$, lalu turunkan $Q_0$ dan $E_\text{JT}$. Mengapa d⁸, $(d_{z^2})^1(d_{x^2-y^2})^1$, tidak terdistorsi?

**Penyelesaian.** $E_\text{el} = 2(-AQ) + 1(+AQ) = -AQ$. Ditambah energi elastik: $E(Q) = \tfrac12kQ^2 - AQ$. Turunan nol: $kQ - A = 0$, sehingga $Q_0 = A/k$ dan $E(Q_0) = \tfrac12A^2/k - A^2/k = -A^2/2k$.

Untuk d⁸ spin tinggi, satu elektron di setiap orbital $e_g$: $E_\text{el} = -AQ + AQ = 0$. Tidak ada suku linear, dan geometri setangkup tetap minimum.

**Memahami hasil.** Pusat berat pemecahan tetap, sehingga stabilisasi hanya muncul bila elektron terbagi tidak seragam. Hal yang sama berlaku untuk d⁴ spin tinggi ($t_{2g}^3e_g^1$: satu elektron $e_g$ turun ke $d_{z^2}$) dan d⁷ spin rendah. Argumen sederhana ini juga menjelaskan mengapa Ni²⁺ (d⁸) oktahedral teratur sempurna sementara tetangganya Cu²⁺ (d⁹) hampir tidak pernah.
:::

::: {.contoh}
**Contoh 14.c2 · Mengukur distorsi dari struktur kristal**

Dalam CuF₂, setiap Cu²⁺ dikelilingi empat F⁻ pada 1,93 Å dan dua F⁻ pada 2,27 Å. Dalam CrF₂, jaraknya 2,00 Å (empat) dan 2,43 Å (dua). Koordinat distorsi tetragonal didefinisikan $Q_\theta = (2\delta_{z+} + 2\delta_{z-} - \delta_{x+} - \delta_{x-} - \delta_{y+} - \delta_{y-})/\sqrt{12}$, dengan $\delta$ simpangan setiap ikatan dari panjang rata-rata. (a) Hitung $Q_\theta$ untuk keduanya. (b) Dengan $E_\text{JT} \approx 2000$ cm⁻¹ untuk Cu²⁺, taksir $A$ dan $k$.

**Penyelesaian.** (a) CuF₂: rata-rata $(4 \times 1{,}93 + 2 \times 2{,}27)/6 = 2{,}043$ Å; $\delta_z = 0{,}227$, $\delta_x = \delta_y = -0{,}113$ Å. $Q_\theta = [4(0{,}227) + 4(0{,}113)]/\sqrt{12} = 0{,}393$ Å. CrF₂: rata-rata 2,143 Å, $\delta_z = 0{,}287$, $\delta_x = -0{,}143$ Å, $Q_\theta = 0{,}497$ Å.

(b) Dari (14.ec2): $A = 2E_\text{JT}/Q_0 = 2(2000)/0{,}393 = 1{,}0 \times 10^4$ cm⁻¹/Å, dan $k = A/Q_0 = 2{,}6 \times 10^4$ cm⁻¹/Å². Dengan 1 cm⁻¹ = 1,986 × 10⁻²³ J dan 1 Å² = 10⁻²⁰ m², $k \approx 52$ N/m.

**Memahami hasil.** Distorsi 0,4–0,5 Å sangat besar: ikatan aksial 17–22% lebih panjang daripada ikatan ekuator. Tetapan gaya 52 N/m adalah tetapan gaya untuk gerakan kolektif enam ligan, jauh lebih lunak daripada ulur satu ikatan Cu–F, sehingga distorsi besar dapat "dibayar" dengan energi elastik kecil. Stabilisasi 2000 cm⁻¹ = 24 kJ/mol cukup untuk menentukan struktur hampir semua senyawa Cu(II): oktahedron memanjang, piramida bujur sangkar, atau bujur sangkar.
:::

### Akibat kimia

Efek Jahn–Teller tampak di mana-mana dalam kimia tembaga(II):

1. **Tetapan pembentukan bertahap.** Empat molekul amonia pertama terikat kuat di posisi ekuator, tetapi yang kelima harus menempati posisi aksial yang panjang dan lemah. Untuk [Cu(NH₃)ₙ]²⁺, $\log K_1$ sampai $\log K_5$ adalah 4,31; 3,67; 3,04; 2,30; −0,46: penurunan tajam 2,76 satuan log dari $K_4$ ke $K_5$. Untuk Ni²⁺ (tanpa Jahn–Teller), $\log K_n$ menurun perlahan: 2,80; 2,24; 1,73; 1,19; 0,75; 0,03.
2. **Puncak Irving–Williams di Cu²⁺** (subbab 14.4): empat ikatan ekuator yang pendek memberikan ikatan yang lebih kuat daripada yang diramalkan ESMK oktahedral.
3. **Kelabilan ekstrem.** [Cu(H₂O)₆]²⁺ menukar airnya sekitar $4 \times 10^9$ kali per detik, karena distorsinya **dinamis**: sumbu panjang melompat di antara ketiga arah, sehingga setiap molekul air secara bergantian berada di posisi aksial yang lemah.
4. **Spektrum.** Pita d–d tembaga(II) lebar dan asimetris karena keadaan dasar dan tereksitasi terpecah; pita tunggal [Ti(H₂O)₆]³⁺ mempunyai bahu (puncak di sekitar 17 400 dan 20 300 cm⁻¹) karena keadaan **tereksitasi** $e_g^1$ mengalami efek Jahn–Teller kuat walaupun keadaan dasarnya hanya lemah.
5. **Bahan.** Dalam LaMnO₃, ion Mn³⁺ (d⁴ spin tinggi) terdistorsi secara teratur dan menghasilkan "susunan orbital" yang menentukan sifat magnetnya; turunannya menunjukkan magnetoresistansi raksasa. Dalam superkonduktor kuprat, bidang CuO₂ dengan ion Cu²⁺ bujur sangkar adalah tempat superkonduksi terjadi.

::: {.contoh}
**Contoh 14.c3 · Mengapa amonia kelima sulit masuk**

Dari data di atas, hitung $\Delta G°$ untuk langkah kelima pengikatan amonia pada Cu²⁺ dan Ni²⁺ pada 298 K, dan selisih $\log K_4 - \log K_5$ untuk keduanya.

**Penyelesaian.** $\Delta G_5° = -5{,}708\log K_5$ kJ/mol. Cu²⁺: $-5{,}708 \times (-0{,}46) = +2{,}6$ kJ/mol. Ni²⁺: $-5{,}708 \times 0{,}75 = -4{,}3$ kJ/mol. Selisih $\log K_4 - \log K_5$: Cu²⁺ 2,76; Ni²⁺ 0,44.

**Memahami hasil.** Untuk Cu²⁺ langkah kelima tidak spontan pada keadaan standar; [Cu(NH₃)₅]²⁺ hanya terbentuk dalam amonia cair atau larutan amonia sangat pekat, dan [Cu(NH₃)₆]²⁺ hampir tidak pernah. Penurunan $\log K$ pada Ni²⁺ (0,44 per langkah) mencerminkan faktor statistik dan tolakan ligan yang wajar. Lompatan pada Cu²⁺ enam kali lebih besar: itulah tanda kimia larutan dari efek Jahn–Teller. Itu sebabnya larutan tembaga dalam amonia yang biru tua sering ditulis [Cu(NH₃)₄(H₂O)₂]²⁺, dengan dua molekul air aksial yang terikat longgar.
:::

::: {.contoh}
**Contoh 14.c4 · Meramalkan distorsi**

Manakah dari ion berikut yang diramalkan mengalami distorsi Jahn–Teller kuat dalam kompleks oktahedral: (a) [Mn(H₂O)₆]³⁺, (b) [Fe(H₂O)₆]³⁺, (c) [Co(NH₃)₆]²⁺ (spin tinggi), (d) [Ni(bpy)₃]³⁺ (spin rendah), (e) [Cr(H₂O)₆]²⁺?

**Penyelesaian.** (a) Mn³⁺ d⁴ spin tinggi, $t_{2g}^3e_g^1$: kuat. (b) Fe³⁺ d⁵ spin tinggi, $t_{2g}^3e_g^2$: tidak ada. (c) Co²⁺ d⁷ spin tinggi, $t_{2g}^5e_g^2$: lemah (hanya $t_{2g}$). (d) Ni³⁺ d⁷ spin rendah, $t_{2g}^6e_g^1$: kuat. (e) Cr²⁺ d⁴ spin tinggi: kuat.

**Memahami hasil.** Ion dengan satu atau tiga elektron di $e_g$ selalu terdistorsi kuat. Mn³⁺ dalam air mudah berdisproporsionasi menjadi Mn²⁺ dan MnO₂; salah satu penyebabnya adalah ketidakstabilan lingkungan oktahedral Mn³⁺. Senyawa Cr²⁺, seperti krom(II) asetat, membentuk struktur dengan ikatan aksial panjang atau ikatan Cr–Cr. Jika keadaan dasar dapat dipindah dari $t_{2g}^5e_g^2$ ke $t_{2g}^6e_g^1$ oleh ligan medan kuat, seperti pada Co²⁺, kompleksnya berubah dari hampir teratur menjadi sangat terdistorsi.
:::

::: {.awas}
**Teorema Jahn–Teller tidak meramalkan besar dan arah distorsi**

Teorema hanya menyatakan bahwa geometri setangkup bukan minimum energi. Besar distorsi bergantung pada perbandingan $A$ dan $k$; bila $E_\text{JT}$ kecil dibanding energi titik nol getaran yang bersangkutan, molekul "bergetar melewati" semua bentuk terdistorsi dan rata-ratanya tampak setangkup (efek Jahn–Teller dinamis). Arah distorsi (pemanjangan atau pemampatan) ditentukan oleh suku orde tinggi. Dan teorema tidak berlaku untuk molekul linear; di sana degenerasi keadaan Π dipecah oleh mekanisme lain yang lebih lemah, efek Renner–Teller. Akhirnya, degenerasi spin (Kramers) tidak pernah dapat dihapus oleh distorsi apa pun, sehingga teorema hanya berbicara tentang degenerasi orbital.
:::

::: {.kuis}
**Kuis cepat 14.6**

Kompleks tetrahedral [CuCl₄]²⁻ ternyata bukan tetrahedron teratur melainkan "tetrahedron pipih". Jelaskan dengan konfigurasi $e^4t_2^5$.
:::
