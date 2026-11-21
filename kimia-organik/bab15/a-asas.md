# Bab 15 Spektroskopi NMR

Dalam Contoh 14.13 kita menjumpai dua cairan yang sulit dibedakan. Keduanya bermassa molekul 88 dan berumus C₄H₈O₂, keduanya ester, dan keduanya memberi pita C=O kuat di sekitar 1740 cm⁻¹ serta pita C–O di daerah 1200 cm⁻¹. Botol pertama berisi **etil asetat**, CH₃COOCH₂CH₃, pelarut yang baunya kita kenal dari penghapus cat kuku. Botol kedua berisi **metil propanoat**, CH₃CH₂COOCH₃, isomer yang baunya mirip buah. Spektrum IR keduanya hampir kembar. Spektrum massanya memang berbeda (etil asetat memberi puncak 43, CH₃CO⁺; metil propanoat memberi 57, C₂H₅CO⁺), tetapi untuk sampai ke kesimpulan itu kita harus menebak lebih dulu jalur fragmentasinya.

Ada cara yang jauh lebih langsung. Kedua molekul ini sama-sama mengandung satu gugus CH₃ "sendirian", satu gugus CH₃ yang bertetangga dengan CH₂, dan satu gugus CH₂. Perbedaannya hanya **di mana** gugus-gugus itu terpasang: pada etil asetat, CH₂ melekat pada oksigen ester; pada metil propanoat, CH₂ melekat pada karbon karbonil, sedangkan CH₃ yang sendirian melekat pada oksigen. Seandainya ada alat yang dapat "mendengar" setiap kelompok atom hidrogen secara terpisah, sekaligus memberi tahu lingkungan elektroniknya, jumlah atomnya, dan siapa tetangganya, kedua isomer ini akan langsung terbedakan. Alat itu ada: **spektroskopi resonansi magnet inti** (*nuclear magnetic resonance*, NMR).

NMR adalah alat paling ampuh dalam penentuan struktur organik. Spektrum IR memberi tahu gugus fungsi, spektrum massa memberi tahu massa dan rumus, tetapi spektrum NMR memberi peta kerangka molekul atom demi atom. Dari satu spektrum ¹H NMR kita memperoleh empat informasi sekaligus: **berapa jenis** hidrogen yang ada (jumlah sinyal), **lingkungan elektronik** masing-masing (geseran kimia), **berapa banyak** hidrogen dari setiap jenis (integrasi), dan **berapa hidrogen tetangga** yang dimilikinya (pola pemecahan). Spektrum ¹³C NMR menambahkan jumlah dan jenis atom karbon. Di bab ini kita mempelajari asal fisika setiap informasi itu dan cara membacanya. Dasar kuantumnya (spin, tingkat energi dalam medan magnet) sudah dibahas di buku *Kimia Kuantum*; di sini kita memakainya sebagai alat.

::: {.kuis}
**Pertanyaan pembuka**

1. Mengapa inti ¹H dan ¹³C dapat diamati dengan NMR, sedangkan inti ¹²C dan ¹⁶O tidak?
2. Mengapa spektrometer NMR yang lebih mahal memakai magnet yang lebih kuat?
3. Mengapa proton gugus CH₃ yang terikat pada oksigen muncul di tempat yang berbeda dengan proton CH₃ yang terikat pada karbon?
4. Mengapa proton benzena muncul jauh di sebelah kiri spektrum, padahal karbon sp² tidak jauh lebih elektronegatif daripada karbon sp³?
5. Mengapa sinyal CH₂ pada etil asetat terpecah menjadi empat garis?
6. Mengapa proton O–H pada etanol sering tampak sebagai satu garis lebar, tidak terpecah oleh CH₂ di sebelahnya?
7. Mengapa spektrum ¹³C biasanya hanya berisi garis-garis tunggal, tanpa pemecahan?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menjelaskan asal sinyal NMR dari spin inti dalam medan magnet dan menghitung frekuensi resonansi serta selisih energi tingkat spin.
2. Menjelaskan perisai dan pengawaperisaian elektron, mendefinisikan geseran kimia δ, dan menghitung δ dari data frekuensi.
3. Meramalkan geseran kimia ¹H dari keelektronegatifan, hibridisasi, dan anisotropi magnet.
4. Menentukan proton-proton yang setara secara kimia dan meramalkan jumlah sinyal, termasuk membedakan proton homotopik, enantiotopik, dan diastereotopik.
5. Memakai kurva integrasi untuk menentukan perbandingan jumlah proton.
6. Menjelaskan pemecahan spin–spin, memakai aturan *n* + 1 dan segitiga Pascal, dan menghubungkan tetapan kopling *J* dengan struktur.
7. Menganalisis pola rumit (doblet dari doblet, kopling dengan dua kelompok tetangga) dengan diagram pohon.
8. Menjelaskan perilaku khas proton O–H dan N–H serta memakai pertukaran D₂O.
9. Membaca spektrum ¹³C NMR dan DEPT untuk menentukan jumlah dan jenis karbon.
10. Menggabungkan rumus molekul, IR, MS, ¹H NMR, dan ¹³C NMR untuk menentukan struktur senyawa yang belum dikenal.
:::

::: {.mat}
**Prasyarat**

Bab 1: derajat ketidakjenuhan (subbab 1.4), hibridisasi (subbab 1.5), keelektronegatifan dan kepolaran ikatan (subbab 1.7). Bab 4: konformasi dan rotasi ikatan (subbab 4.2). Bab 5: kiralitas dan diastereomer. Bab 10: aromatisitas. Bab 14: IR dan MS. *Kimia Kuantum*: spin dan momen magnet; *Fisika Umum*: medan magnet dan induksi.
:::

## 15.1 Asas NMR

### Inti yang berputar adalah magnet kecil

Banyak inti atom mempunyai sifat kuantum yang disebut **spin inti**, dengan bilangan kuantum spin *I*. Inti yang jumlah proton dan jumlah neutronnya sama-sama genap, misalnya ¹²C dan ¹⁶O, mempunyai *I* = 0 dan tidak mempunyai momen magnet; inti seperti ini "tidak terlihat" oleh NMR. Inti ¹H (proton), ¹³C, ¹⁹F, dan ³¹P mempunyai *I* = ½. Inti bermuatan yang berspin berperilaku seperti magnet batang yang sangat kecil: ia mempunyai **momen magnet** μ yang searah dengan spinnya.

Untuk inti dengan *I* = ½, mekanika kuantum hanya mengizinkan dua keadaan orientasi bila inti diletakkan dalam medan magnet luar **B**₀: keadaan **α** (momen magnet sejajar dengan medan, energinya lebih rendah) dan keadaan **β** (momen magnet berlawanan dengan medan, energinya lebih tinggi). Tanpa medan luar kedua keadaan ini berenergi sama. Dalam medan magnet, keduanya terpisah oleh selisih energi yang sebanding dengan kuat medan:

$$
\Delta E = h\nu = \frac{h\gamma B_0}{2\pi} \qquad \text{(15.1)}
$$

dengan γ **rasio giromagnetik**, tetapan khas setiap jenis inti. Untuk ¹H, γ = 2,675 × 10⁸ rad s⁻¹ T⁻¹; untuk ¹³C, γ = 6,728 × 10⁷ rad s⁻¹ T⁻¹, sekitar seperempatnya. Frekuensi ν = γ*B*₀/2π yang memenuhi persamaan ini disebut **frekuensi Larmor** atau frekuensi resonansi.

![Gambar 15.1 Pemisahan tingkat energi spin inti ¹H dalam medan magnet. Tanpa medan (kiri), keadaan α dan β berenergi sama. Selisih energinya bertambah sebanding dengan kuat medan *B*₀; pada 7,05 T selisih itu sesuai dengan foton 300 MHz, dan pada 9,40 T dengan foton 400 MHz.](fig/tingkat.png){width=82%}

### Resonansi: menyerap gelombang radio

Bila sampel yang berada dalam medan magnet disinari dengan gelombang radio yang frekuensinya tepat sama dengan frekuensi Larmor, inti dalam keadaan α dapat menyerap foton dan berpindah ke keadaan β: inti **beresonansi**. Itulah asal nama resonansi magnet inti. Spektrometer modern dinamai menurut frekuensi resonansi proton dalam magnetnya: "spektrometer 400 MHz" mempunyai magnet sekitar 9,4 T, kira-kira dua ratus ribu kali medan magnet Bumi. Magnet sekuat ini dibuat dari kumparan superkonduktor yang direndam dalam helium cair.

Energi foton NMR sangat kecil. Pada 400 MHz, Δ*E* = *h*ν = 2,65 × 10⁻²⁵ J per inti atau hanya 0,160 J mol⁻¹, sekitar dua ratus ribu kali lebih kecil daripada energi foton IR pada 3000 cm⁻¹ (35,9 kJ mol⁻¹). Akibatnya, pada suhu kamar populasi kedua keadaan hampir sama. Menurut distribusi Boltzmann, perbandingan populasinya adalah

$$
\frac{N_\beta}{N_\alpha} = e^{-\Delta E / kT} \qquad \text{(15.2)}
$$

Pada 400 MHz dan 298 K, perbandingan ini 0,999936. Dari setiap sejuta proton, kelebihan populasi di keadaan α hanya sekitar 32 proton. Sinyal NMR berasal dari kelebihan kecil ini saja, sehingga NMR adalah metode yang **kurang peka** dibandingkan IR atau MS: kita memerlukan beberapa miligram sampel, sedangkan MS cukup dengan nanogram. Kepekaan bertambah dengan medan magnet, karena Δ*E* dan kelebihan populasi sebanding dengan *B*₀. Inilah salah satu alasan mengapa kimiawan menginginkan magnet yang makin kuat; alasan lainnya, yang lebih penting, akan kita lihat di subbab 15.6.

::: {.contoh}
**Contoh 15.1 · Frekuensi resonansi dan selisih energi**

Sebuah spektrometer mempunyai magnet 14,1 T. (a) Hitung frekuensi resonansi ¹H dan ¹³C. (b) Hitung Δ*E* untuk ¹H dalam J mol⁻¹. (c) Hitung kelebihan populasi keadaan α per sejuta proton pada 298 K.

**Rencana.** Pakai ν = γ*B*₀/2π, lalu Δ*E* = *h*ν dikali *N*ₐ, lalu perbandingan Boltzmann.

**Penyelesaian.** (a) Untuk ¹H: ν = (2,675 × 10⁸)(14,1)/(2π) = 6,00 × 10⁸ Hz = **600 MHz**. Untuk ¹³C: ν = (6,728 × 10⁷)(14,1)/(2π) = **151 MHz**. (b) Δ*E* = (6,626 × 10⁻³⁴)(6,00 × 10⁸)(6,022 × 10²³) = **0,239 J mol⁻¹**. (c) *N*~β~/*N*~α~ = exp(−Δ*E*/*RT*) = exp(−0,239/(8,314 × 298)) = 0,999903. Selisih relatifnya (*N*~α~ − *N*~β~)/(*N*~α~ + *N*~β~) ≈ Δ*E*/2*RT* = 4,8 × 10⁻⁵, yaitu sekitar **48 proton per sejuta**.

**Memahami hasil.** Spektrometer "600 MHz" disebut demikian karena proton beresonansi pada 600 MHz di dalamnya. Karbon-13 dalam magnet yang sama beresonansi pada frekuensi yang kira-kira empat kali lebih rendah, sehingga spektrum ¹H dan ¹³C diukur pada saluran frekuensi yang berbeda dan tidak saling mengganggu. Kelebihan populasi naik dari 32 menjadi 48 per sejuta bila medan naik dari 9,4 T ke 14,1 T: kepekaan sebanding dengan medan.
:::

### Bagaimana spektrum diukur

Spektrometer generasi awal menyapu frekuensi atau medan secara perlahan dan mencatat penyerapan satu per satu. Spektrometer modern memakai cara yang jauh lebih cepat, **NMR transformasi Fourier (FT-NMR)**. Sampel (biasanya 5–20 mg dalam 0,6 mL pelarut terdeuterasi, misalnya CDCl₃) ditempatkan dalam tabung kaca tipis di tengah magnet. Sebuah **pulsa** gelombang radio yang sangat singkat, beberapa mikrodetik, mengandung semua frekuensi di sekitar frekuensi Larmor sekaligus, sehingga membangkitkan semua inti ¹H bersamaan. Setelah pulsa, magnetisasi inti berpresesi dan perlahan kembali ke keadaan setimbang; gerakan ini menginduksi arus kecil dalam kumparan penerima. Sinyal yang tercatat, **peluruhan induksi bebas** (*free induction decay*, FID), adalah campuran gelombang dari semua jenis proton yang meluruh dalam beberapa detik. Komputer mengubah FID menjadi spektrum (intensitas terhadap frekuensi) dengan operasi matematika **transformasi Fourier**. Karena satu pengukuran hanya beberapa detik, puluhan pengukuran dapat dijumlahkan untuk memperbesar sinyal terhadap derau.

![Gambar 15.2 Prinsip FT-NMR. Pulsa gelombang radio membangkitkan semua proton sekaligus; sinyal yang terekam (FID, kiri) adalah jumlah gelombang yang meluruh. Transformasi Fourier mengubahnya menjadi spektrum (kanan): setiap frekuensi dalam FID menjadi satu puncak. Sinyal skematis dengan dua jenis proton.](fig/fid.png){width=94%}

Mengapa pelarutnya harus terdeuterasi? Pelarut biasa seperti CHCl₃ mengandung proton dalam jumlah yang ribuan kali lebih banyak daripada sampel, sehingga sinyalnya akan menutupi sinyal sampel. Deuterium (²H) beresonansi pada frekuensi yang sangat berbeda dan tidak terlihat dalam spektrum ¹H. Spektrometer juga memakai sinyal deuterium pelarut untuk "mengunci" medan agar tetap stabil selama pengukuran. Pelarut terdeuterasi tidak pernah 100% murni; sisa CHCl₃ dalam CDCl₃ memberi sinyal kecil pada δ 7,26 yang hampir selalu tampak dalam spektrum.

::: {.inti}
**Inti subbab 15.1**

- Inti dengan *I* = ½ (¹H, ¹³C, ¹⁹F, ³¹P) mempunyai dua keadaan spin dalam medan magnet; selisih energinya Δ*E* = *h*γ*B*₀/2π, sebanding dengan medan.
- Resonansi terjadi pada frekuensi radio: ¹H 400 MHz pada 9,4 T; ¹³C sekitar seperempatnya.
- Δ*E* sangat kecil, sehingga kelebihan populasi hanya puluhan per sejuta inti: NMR kurang peka, tetapi kepekaan naik dengan medan.
- FT-NMR membangkitkan semua inti dengan satu pulsa dan mengubah FID menjadi spektrum dengan transformasi Fourier.
:::

::: {.kuis}
**Kuis cepat 15.1** (a) Berapa frekuensi resonansi ¹H dalam magnet 11,74 T? (b) Mengapa ¹²C dan ¹⁶O tidak memberi sinyal NMR? (c) Mengapa sampel NMR dilarutkan dalam CDCl₃, bukan CHCl₃?
:::

## 15.2 Geseran kimia ¹H

### Elektron melindungi inti

Seandainya semua proton dalam molekul merasakan medan magnet yang sama, semuanya akan beresonansi pada frekuensi yang sama dan spektrum NMR hanya berisi satu garis: tidak berguna. Kenyataannya, setiap proton dikelilingi elektron. Dalam medan magnet luar, elektron-elektron itu bersirkulasi dan menghasilkan **medan magnet imbas** kecil yang **berlawanan arah** dengan **B**₀ di tempat inti berada (sama seperti hukum Lenz pada kumparan). Akibatnya, inti merasakan medan efektif yang sedikit lebih kecil daripada medan luar:

$$
B_\text{efektif} = B_0 (1 - \sigma) \qquad \text{(15.3)}
$$

dengan σ **tetapan perisai**, besarnya sekitar sepersejuta sampai beberapa per seratus ribu. Kita katakan inti itu **terperisai** (*shielded*) oleh elektronnya. Makin besar kerapatan elektron di sekitar proton, makin kuat perisainya, makin kecil medan efektifnya, dan makin rendah frekuensi resonansinya. Sebaliknya, bila ada atom elektronegatif yang menarik elektron dari sekitar proton, perisainya melemah, proton **terawaperisai** (*deshielded*), dan beresonansi pada frekuensi yang lebih tinggi.

![Gambar 15.3 Perisai elektron. Kiri: medan luar **B**₀ menyebabkan elektron di sekitar inti bersirkulasi dan menghasilkan medan imbas yang melawan **B**₀, sehingga inti merasakan medan efektif lebih kecil. Kanan: skala spektrum. Proton terawaperisai (kerapatan elektron rendah) muncul di kiri, pada δ besar ("medan bawah"); proton terperisai muncul di kanan, dekat TMS ("medan atas").](fig/perisai.png){width=94%}

### Skala δ dan senyawa rujukan TMS

Perbedaan frekuensi resonansi antara proton dalam lingkungan yang berbeda sangat kecil: hanya beberapa ratus sampai beberapa ribu hertz dari frekuensi ratusan juta hertz. Selain itu, perbedaan dalam hertz sebanding dengan medan magnet, sehingga angka yang sama akan berbeda di spektrometer 300 MHz dan 600 MHz. Untuk mendapatkan angka yang tidak bergantung pada alat, kita mengukur frekuensi relatif terhadap senyawa rujukan dan membaginya dengan frekuensi spektrometer. Hasilnya adalah **geseran kimia** δ, dalam satuan **bagian per sejuta** (*parts per million*, ppm):

$$
\delta = \frac{\nu_\text{sampel} - \nu_\text{TMS}}{\nu_\text{spektrometer}} \times 10^{6} \qquad \text{(15.4)}
$$

Senyawa rujukannya adalah **tetrametilsilana** (TMS), (CH₃)₄Si. Pilihan ini cerdik: (1) kedua belas protonnya setara, sehingga memberi satu sinyal tajam dan kuat; (2) silikon kurang elektronegatif daripada karbon, sehingga proton TMS sangat terperisai dan muncul di sebelah kanan hampir semua proton organik; (3) TMS lembam dan mudah menguap (titik didih 27 °C), sehingga mudah dibuang dari sampel. Menurut definisi, δ(TMS) = 0. Hampir semua proton organik mempunyai δ antara 0 dan 12.

Spektrum NMR digambar dengan δ **bertambah ke kiri**. Sisi kiri disebut **medan bawah** (*downfield*): proton terawaperisai, δ besar. Sisi kanan disebut **medan atas** (*upfield*): proton terperisai, δ kecil. Istilah "medan bawah" dan "medan atas" berasal dari spektrometer lama yang menyapu medan magnet; kita tetap memakainya karena praktis.

::: {.contoh}
**Contoh 15.2 · Menghitung geseran kimia**

Pada spektrometer 300 MHz, sinyal proton CH₃ metanol muncul 1020 Hz di sebelah kiri sinyal TMS. (a) Berapa δ? (b) Pada berapa hertz dari TMS sinyal ini muncul di spektrometer 600 MHz? (c) Sinyal lain dalam spektrum 300 MHz yang sama berada pada δ 7,26. Berapa hertz jaraknya dari TMS?

**Penyelesaian.** (a) δ = 1020 Hz / 300 MHz = 1020/(300 × 10⁶) × 10⁶ = **3,40 ppm**. (b) Geseran kimia tidak bergantung pada alat, sehingga pada 600 MHz jaraknya 3,40 × 600 = **2040 Hz**. (c) 7,26 × 300 = **2178 Hz**.

**Memahami hasil.** Dalam satuan hertz, jarak sinyal dari TMS berlipat dua bila medan berlipat dua, tetapi δ tetap. Itulah sebabnya geseran kimia selalu dilaporkan dalam ppm, sedangkan tetapan kopling (subbab 15.5), yang tidak bergantung pada medan, dilaporkan dalam hertz. Perhatikan juga bahwa "ppm" di sini bukan konsentrasi, melainkan perbandingan dua frekuensi.
:::

### Faktor 1: keelektronegatifan

Faktor paling penting yang menentukan geseran kimia adalah keelektronegatifan atom di sekitar proton. Atom elektronegatif menarik elektron ikatan C–H menjauh dari proton, mengurangi perisai, sehingga proton bergeser ke medan bawah. Perhatikan deret metil halida dan senyawa sejenis:

| Senyawa | CH₄ | CH₃I | CH₃Br | CH₃Cl | CH₃OH | CH₃F |
|---|---|---|---|---|---|---|
| Keelektronegatifan X | 2,2 (H) | 2,7 | 3,0 | 3,2 | 3,4 | 4,0 |
| δ (ppm) | 0,23 | 2,16 | 2,68 | 3,05 | 3,40 | 4,26 |

Makin elektronegatif X, makin besar δ. Efek ini **bertambah** bila ada lebih banyak atom elektronegatif: CH₃Cl 3,05; CH₂Cl₂ 5,30; CHCl₃ 7,26. Efek ini **berkurang cepat dengan jarak**: dalam 1-bromopropana, CH₂Br berada pada δ 3,39, CH₂ di tengah pada 1,89, dan CH₃ di ujung pada 1,03, hampir sama dengan alkana biasa. Efek induktif melemah dengan cepat setiap kali melewati satu ikatan, sehingga pengaruhnya praktis lenyap setelah tiga ikatan.

### Faktor 2: hibridisasi dan anisotropi magnet

Proton pada karbon sp³ alkana muncul pada δ 0,9–1,7. Proton pada alkena (vinil) muncul pada δ 4,5–6,5, proton aromatik pada δ 6,5–8,0, dan proton aldehida pada δ 9,5–10,5. Sebagian pergeseran ini berasal dari hibridisasi: karbon sp² lebih elektronegatif daripada karbon sp³ (subbab 1.5). Tetapi efek itu terlalu kecil untuk menjelaskan selisih yang mencapai beberapa ppm. Penyebab utamanya adalah **anisotropi magnet**: elektron π bersirkulasi dalam medan magnet dan menghasilkan medan imbas yang arahnya **bergantung pada letak** di sekitar molekul.

Contoh paling jelas adalah benzena. Dalam medan **B**₀ yang tegak lurus bidang cincin, keenam elektron π bersirkulasi mengelilingi cincin sebagai **arus cincin** (*ring current*). Arus ini menghasilkan medan imbas yang di tengah cincin berlawanan dengan **B**₀, tetapi di luar cincin, tempat proton-proton benzena berada, garis medannya melengkung kembali dan **searah** dengan **B**₀. Proton aromatik merasakan medan tambahan, sehingga terawaperisai dan muncul pada δ 7,3 untuk benzena. Arus cincin hanya ada bila cincin aromatik (subbab 10.2); karena itu geseran kimia proton sering dipakai sebagai bukti percobaan aromatisitas. Buktinya yang paling meyakinkan berasal dari molekul seperti [18]anulena, cincin aromatik besar yang mempunyai proton di dalam dan di luar cincin: proton di luar muncul pada δ 9,3, sedangkan proton di dalam cincin, yang merasakan medan imbas berlawanan, muncul pada δ −3, di sebelah kanan TMS.

![Gambar 15.4 Anisotropi magnet. (a) Arus cincin benzena: medan imbas melawan **B**₀ di dalam cincin tetapi menambah **B**₀ di luar, tempat proton aromatik berada (terawaperisai, δ 7,3). (b) Ikatan rangkap C=C dan C=O: proton vinil dan proton aldehida berada di daerah terawaperisai. (c) Ikatan rangkap tiga: sirkulasi elektron π di sekitar sumbu ikatan memerisai proton asetilenik di ujung sumbu (δ 2,5). Daerah ⊕ terawaperisai, ⊖ terperisai.](fig/cincin.png){width=96%}

Ikatan rangkap dua C=C dan C=O menghasilkan efek serupa: proton vinil dan terutama proton aldehida (yang juga terikat pada karbon yang ditarik oleh oksigen) berada di daerah terawaperisai. Proton aldehida pada δ 9,5–10,5 hampir tidak pernah tertukar dengan proton lain, sehingga menjadi penanda yang sangat andal.

Ikatan rangkap tiga memberi kejutan. Elektron π alkuna membentuk silinder simetris di sekitar sumbu ikatan. Bila sumbu itu sejajar dengan **B**₀, sirkulasi elektron mengelilingi sumbu menghasilkan medan imbas yang **melawan** **B**₀ tepat di ujung sumbu, tempat proton asetilenik berada. Akibatnya proton ≡C–H terperisai dan muncul pada δ sekitar 2,5, jauh di sebelah kanan proton vinil, meskipun karbon sp lebih elektronegatif daripada karbon sp².

### Faktor 3: ikatan hidrogen

Proton O–H dan N–H mempunyai geseran kimia yang sangat bervariasi (δ 1–5 untuk alkohol dan amina, 4–8 untuk fenol, 10–13 untuk asam karboksilat), bergantung pada konsentrasi, pelarut, dan suhu. Ikatan hidrogen menarik proton ke arah atom elektronegatif kedua dan mengurangi kerapatan elektron di sekitarnya, sehingga proton bergeser ke medan bawah. Makin pekat larutan, makin banyak ikatan hidrogen, makin besar δ. Asam karboksilat membentuk dimer dengan dua ikatan hidrogen kuat (subbab 12.1), sehingga proton COOH-nya muncul sangat jauh di kiri, δ 10–13. Kita kembali ke proton ini di subbab 15.7.

### Tabel geseran kimia

Gabungan ketiga faktor di atas menghasilkan daerah-daerah geseran kimia yang khas untuk setiap jenis proton. Daerah ini perlu dihafal dalam garis besar, seperti daerah gugus fungsi dalam IR.

![Gambar 15.5 Daerah geseran kimia ¹H yang khas. Proton makin terawaperisai (makin ke kiri) bila terikat pada karbon yang membawa atom elektronegatif, bila terikat pada karbon sp² dalam daerah anisotropi yang menguntungkan, atau bila terlibat ikatan hidrogen kuat.](fig/geseran.png){width=96%}

| Jenis proton | δ (ppm) | Jenis proton | δ (ppm) |
|---|---|---|---|
| R–CH₃, R₂CH₂, R₃CH | 0,9; 1,3; 1,5 | H–C–Cl, H–C–Br, H–C–I | 3,0–4,0; 2,5–4,0; 2,0–4,0 |
| C=C–CH₃ (alilik) | 1,6–2,0 | H–C–O (alkohol, eter, ester) | 3,3–4,5 |
| O=C–CH₃ (α karbonil) | 2,0–2,6 | C=C–H (vinil) | 4,5–6,5 |
| Ar–CH₃ (benzilik) | 2,2–2,5 | Ar–H (aromatik) | 6,5–8,5 |
| ≡C–H (asetilenik) | 2,4–3,1 | O=C–H (aldehida) | 9,5–10,5 |
| H–C–N (amina) | 2,2–3,0 | R–COOH | 10–13 |
| R–OH, R–NH₂ | 1–5 (beragam) | Ar–OH (fenol) | 4–8 (beragam) |

Untuk proton CH₂ atau CH yang dipengaruhi lebih dari satu gugus, efeknya kira-kira **menjumlah**. Sebagai pegangan kasar, mulailah dari δ 1,3 untuk CH₂ alkana lalu tambahkan kira-kira 0,8 bila bersebelahan dengan C=O atau cincin benzena, 1,0 untuk C=C, 2,1 untuk Br, 2,2 untuk Cl, 2,1–2,4 untuk O–R atau O–H, dan 2,9 untuk O–C(=O)R. Perkiraan ini tidak tepat, tetapi biasanya cukup untuk membedakan beberapa kemungkinan struktur.

::: {.contoh}
**Contoh 15.3 · Meramalkan geseran kimia**

Ramalkan δ setiap jenis proton dalam (a) etil asetat, CH₃COOCH₂CH₃, dan (b) metil propanoat, CH₃CH₂COOCH₃. Bagaimana geseran kimia membedakan kedua isomer?

**Penyelesaian.** (a) Etil asetat: CH₃ yang terikat pada C=O berada di daerah α karbonil, **δ ≈ 2,0**. CH₂ yang terikat pada oksigen ester: 1,3 + 2,9 ≈ **4,1**. CH₃ ujung gugus etil hanya terpengaruh lemah oleh oksigen yang berjarak dua ikatan: **δ ≈ 1,2**. Nilai terukur: 2,05; 4,12; 1,26. (b) Metil propanoat: CH₃ yang terikat pada oksigen ester (OCH₃): **δ ≈ 3,7**. CH₂ yang terikat pada C=O: 1,3 + 0,8 ≈ **2,2–2,3**. CH₃ ujung: **δ ≈ 1,1**. Nilai terukur: 3,67; 2,32; 1,14.

**Memahami hasil.** Kedua isomer sama-sama memberi tiga sinyal, tetapi letaknya berbeda tajam. Pada etil asetat, sinyal paling kiri (4,1) adalah CH₂, sedangkan pada metil propanoat sinyal paling kiri (3,7) adalah CH₃. Integrasi (subbab 15.4) akan menunjukkan apakah sinyal paling kiri mewakili dua atau tiga proton, dan pola pemecahan (subbab 15.5) akan memastikan siapa tetangganya. Teka-teki pembuka bab sudah setengah terjawab hanya dari geseran kimia.
:::

::: {.awas}
**Hati-hati: medan bawah tidak sama dengan "energi rendah"**

Proton terawaperisai (δ besar, kiri) memerlukan frekuensi **lebih tinggi** untuk beresonansi, karena medan efektif yang dirasakannya lebih besar. Jadi spektrum NMR digambar dengan frekuensi bertambah ke kiri. Jangan terkecoh oleh istilah "medan bawah": istilah itu berasal dari spektrometer lama yang menjaga frekuensi tetap dan menyapu medan; proton terawaperisai sudah beresonansi pada medan luar yang lebih rendah.
:::

::: {.inti}
**Inti subbab 15.2**

- Elektron di sekitar proton menghasilkan medan imbas yang melawan **B**₀ (perisai). Kerapatan elektron rendah berarti terawaperisai, frekuensi lebih tinggi, δ besar (kiri).
- δ = (ν − ν~TMS~)/ν~spektrometer~ × 10⁶ ppm; tidak bergantung pada kuat medan. TMS: δ = 0.
- Penentu δ: keelektronegatifan (menjumlah, melemah cepat dengan jarak), anisotropi elektron π (aromatik 6,5–8,5; vinil 4,5–6,5; aldehida 9,5–10,5; alkuna hanya 2,5), dan ikatan hidrogen (OH, NH beragam; COOH 10–13).
:::

::: {.kuis}
**Kuis cepat 15.2** (a) Pada spektrometer 400 MHz, sebuah sinyal berada 1480 Hz dari TMS. Berapa δ? (b) Urutkan δ proton: CH₃–CH₃, CH₃–O–CH₃, CH₃–C(=O)–CH₃, CH₃–Cl. (c) Mengapa proton asetilena (δ 1,9) lebih terperisai daripada proton etena (δ 5,3)?
:::

## 15.3 Kesetaraan proton dan jumlah sinyal

### Proton setara memberi satu sinyal

Proton-proton yang berada dalam lingkungan kimia yang persis sama mempunyai geseran kimia yang sama dan muncul sebagai **satu sinyal**. Proton seperti ini disebut **setara secara kimia** (*chemically equivalent*). Jumlah sinyal dalam spektrum ¹H NMR sama dengan jumlah jenis proton yang tidak setara.

Kadang kesetaraan mudah dilihat. Keenam proton etana setara; keenam proton benzena setara; kedua belas proton TMS setara. Ketiga proton dalam satu gugus metil selalu setara, karena rotasi ikatan C–C berlangsung sangat cepat (miliaran kali per detik, subbab 4.2) dibandingkan skala waktu NMR, sehingga setiap proton menempati ketiga posisi secara bergantian dan merasakan lingkungan rata-rata yang sama.

### Uji penggantian

Untuk kasus yang kurang jelas, ada uji sederhana yang selalu berhasil: **uji penggantian**. Ganti satu proton dengan atom lain (sebut saja Z) dalam pikiran, lalu ganti proton lain dengan Z, dan bandingkan kedua senyawa hasilnya.

- Bila kedua hasil penggantian adalah **senyawa yang sama** (dapat ditumpuk tepat setelah diputar), kedua proton itu **homotopik**: setara dalam segala keadaan, memberi satu sinyal.
- Bila kedua hasil penggantian adalah **enansiomer**, kedua proton itu **enantiotopik**. Dalam pelarut biasa (akiral), enansiomer mempunyai sifat fisika yang sama, sehingga proton enantiotopik juga setara dan memberi satu sinyal.
- Bila kedua hasil penggantian adalah **diastereomer**, kedua proton itu **diastereotopik**. Diastereomer mempunyai sifat fisika yang berbeda (subbab 5.6), sehingga proton diastereotopik pada prinsipnya **tidak setara** dan dapat memberi sinyal berbeda.
- Bila kedua hasil penggantian adalah **isomer struktur** yang berbeda, kedua proton jelas tidak setara.

![Gambar 15.6 Uji penggantian. (a) Dua proton CH₂ pada propana: mengganti salah satunya memberi 2-Z-propana, dan mengganti yang lain memberi molekul yang sama persis setelah diputar: homotopik. (b) Dua proton CH₂ pada etanol: hasil penggantiannya sepasang enansiomer: enantiotopik, setara dalam pelarut akiral. (c) Dua proton CH₂ pada (*R*)-2-klorobutana: hasilnya sepasang diastereomer: diastereotopik, tidak setara.](fig/topik.png){width=94%}

Proton diastereotopik hampir selalu dijumpai pada gugus CH₂ dalam molekul yang sudah mempunyai pusat kiral, dan juga pada proton =CH₂ alkena yang ujung lainnya membawa dua gugus berbeda. Pada alkena, rotasi ikatan rangkap tidak terjadi, sehingga kedua proton =CH₂ dalam kloroetena, misalnya, berbeda: yang satu *cis* terhadap Cl dan yang lain *trans*. Kloroetena memberi tiga sinyal, bukan dua.

::: {.contoh}
**Contoh 15.4 · Menghitung jumlah sinyal**

Berapa sinyal ¹H NMR yang diberikan oleh: (a) 2-metilpropana; (b) butan-2-on; (c) *p*-xilena (1,4-dimetilbenzena); (d) metilsikloheksana pada suhu kamar (abaikan perbedaan halus sisi aksial/ekuatorial); (e) 1,1-dikloroetena; (f) 1-kloro-2-metilpropana?

**Penyelesaian.** (a) (CH₃)₃CH: sembilan proton CH₃ setara, satu proton CH: **2 sinyal**. (b) CH₃COCH₂CH₃: CH₃ pada C=O, CH₂, CH₃ ujung: **3 sinyal**. (c) Dua CH₃ setara (simetri) dan empat proton cincin setara: **2 sinyal**. (d) Metilsikloheksana: CH₃; CH (C1); C2/C6 setara; C3/C5 setara; C4. Proton dalam CH₂ cincin masing-masing diastereotopik (satu di sisi yang sama dengan CH₃, satu di sisi berlawanan), sehingga hitungan lengkapnya lebih besar, tetapi sinyal-sinyal itu bertumpuk menjadi pita lebar pada δ 0,9–1,7. Hitungan kasar menurut kelompok karbon: **5**. (e) Cl₂C=CH₂: kedua proton =CH₂ setara karena ujung lain membawa dua gugus yang sama: **1 sinyal**. (f) ClCH₂CH(CH₃)₂: CH₂Cl, CH, dua CH₃ setara (enantiotopik, karena tidak ada pusat kiral): **3 sinyal**.

**Memahami hasil.** Cara tercepat adalah mencari unsur simetri molekul (bidang cermin, sumbu putar) lalu mengelompokkan atom yang dipetakan satu sama lain oleh simetri itu. Uji penggantian dipakai bila ragu, terutama untuk CH₂ di dekat pusat kiral.
:::

::: {.contoh}
**Contoh 15.5 · Membedakan isomer dari jumlah sinyal**

Empat isomer C₄H₉Br: 1-bromobutana, 2-bromobutana, 1-bromo-2-metilpropana, dan 2-bromo-2-metilpropana. Berapa sinyal yang diberikan masing-masing (kelompokkan proton diastereotopik sebagai satu sinyal), dan isomer mana yang dapat dikenali hanya dari jumlah sinyal?

**Penyelesaian.** 1-Bromobutana, BrCH₂CH₂CH₂CH₃: **4**. 2-Bromobutana, CH₃CHBrCH₂CH₃: CH₃ pada C1, CH, CH₂, CH₃ pada C4: **4** (proton CH₂ diastereotopik karena C2 kiral, tetapi biasanya bertumpuk). 1-Bromo-2-metilpropana, BrCH₂CH(CH₃)₂: **3**. 2-Bromo-2-metilpropana, (CH₃)₃CBr: **1**.

**Memahami hasil.** Dua isomer langsung dikenali dari jumlah sinyal (1 dan 3). Dua lainnya sama-sama memberi empat sinyal dan harus dibedakan dari geseran kimia (CH₂Br pada δ 3,4 lawan CHBr pada δ 4,1), integrasi (2H lawan 1H), dan pola pemecahan. Inilah alasan kita memerlukan keempat jenis informasi NMR bersama-sama.
:::

::: {.inti}
**Inti subbab 15.3**

- Proton setara secara kimia memberi satu sinyal; jumlah sinyal = jumlah jenis proton yang tidak setara.
- Uji penggantian: hasil identik → homotopik; enansiomer → enantiotopik (setara dalam pelarut akiral); diastereomer → diastereotopik (tidak setara).
- Rotasi cepat menyetarakan proton CH₃; ikatan rangkap dan pusat kiral dapat membuat proton CH₂ tidak setara.
:::

::: {.kuis}
**Kuis cepat 15.3** Berapa sinyal ¹H NMR untuk: (a) aseton; (b) etil benzena (proton cincin dikelompokkan menurut posisi *o*, *m*, *p*); (c) (*E*)-but-2-ena; (d) 2-metilbut-2-ena?
:::

## 15.4 Integrasi

### Luas sinyal sebanding dengan jumlah proton

Setiap proton memberi sumbangan yang sama terhadap sinyal NMR. Karena itu **luas** di bawah sebuah sinyal (bukan tingginya) sebanding dengan jumlah proton yang menghasilkannya. Spektrometer menghitung luas ini dengan **integrasi** dan menampilkannya sebagai kurva bertangga di atas spektrum, atau sebagai angka di bawah setiap sinyal. Tinggi setiap anak tangga sebanding dengan luas sinyal di bawahnya.

Yang diperoleh dari integrasi adalah **perbandingan** jumlah proton, bukan jumlah mutlaknya. Untuk mengubah perbandingan menjadi jumlah, kita perlu tahu jumlah total proton (dari rumus molekul), atau kita membagi semua angka dengan angka terkecil lalu mencari bilangan bulat yang paling sesuai.

![Gambar 15.7 Spektrum ¹H NMR skematis etil asetat (300 MHz, CDCl₃). Tiga sinyal: kuartet CH₂ pada δ 4,12, singlet CH₃ asetil pada δ 2,05, dan triplet CH₃ etil pada δ 1,26. Kurva integrasi (garis bertangga) naik dengan perbandingan 2 : 3 : 3. Sinyal TMS pada δ 0.](fig/etilasetat.png){width=96%}

::: {.contoh}
**Contoh 15.6 · Dari tinggi tangga ke jumlah proton**

Spektrum senyawa C₁₀H₁₄ memberi dua sinyal: δ 7,28 (anak tangga setinggi 31 mm) dan δ 1,32 (anak tangga setinggi 56 mm). Tentukan jumlah proton setiap sinyal dan usulkan struktur.

**Rencana.** Hitung perbandingan, ubah menjadi bilangan bulat yang jumlahnya 14, lalu cocokkan dengan geseran kimia dan derajat ketidakjenuhan.

**Penyelesaian.** Perbandingan 31 : 56 = 1 : 1,81. Jumlah total 31 + 56 = 87 mm untuk 14 proton, atau 6,21 mm per proton. Maka sinyal δ 7,28: 31/6,21 = 5,0 → **5H**; sinyal δ 1,32: 56/6,21 = 9,0 → **9H**. Derajat ketidakjenuhan C₁₀H₁₄: (2·10 + 2 − 14)/2 = 4, cocok dengan cincin benzena. Lima proton aromatik berarti cincin bersubstituen tunggal (C₆H₅–). Sisanya C₄H₉ dengan sembilan proton setara dalam satu singlet: gugus *tert*-butil. Struktur: ***tert*-butilbenzena**, C₆H₅C(CH₃)₃.

**Memahami hasil.** Sembilan proton dalam satu singlet tanpa tetangga adalah tanda khas gugus *tert*-butil, sama seperti singlet 3H pada δ 2,1 adalah tanda khas metil keton atau asetil. Perbandingan yang tidak bulat sempurna (1,81 bukan 1,80) adalah hal biasa: integrasi nyata mempunyai ketelitian beberapa persen.
:::

### Batas integrasi

Integrasi ¹H dapat dipercaya sampai beberapa persen, cukup untuk membedakan 2H dari 3H, tetapi kadang sulit membedakan 9H dari 10H. Sinyal O–H dan N–H yang lebar sering terintegrasi kurang tepat. Sinyal yang tumpang-tindih hanya dapat diintegrasi bersama. Dalam spektrum ¹³C rutin, integrasi **tidak** dapat dipercaya, karena karbon yang berbeda pulih ke keadaan setimbang dengan kecepatan yang sangat berbeda dan intensitasnya juga diperbesar secara tidak merata oleh pemisahan proton (subbab 15.8).

Integrasi juga dipakai di luar penentuan struktur. Perbandingan luas sinyal dua senyawa dalam campuran memberi perbandingan molnya, sehingga NMR dipakai untuk mengukur kemurnian, hasil reaksi, atau perbandingan isomer tanpa memisahkan campuran. Teknik ini, **NMR kuantitatif** (qNMR), sekarang dipakai dalam industri farmasi untuk menetapkan kemurnian bahan baku obat.

::: {.contoh}
**Contoh 15.7 · Perbandingan isomer dalam campuran**

Hasil reaksi berupa campuran etil asetat (CH₃COOC₂H₅) dan metil propanoat (C₂H₅COOCH₃). Dalam spektrum ¹H campuran itu, kuartet OCH₂ etil asetat (δ 4,12) mempunyai integrasi 1,00, dan singlet OCH₃ metil propanoat (δ 3,67) mempunyai integrasi 0,90. Berapa persen mol etil asetat dalam campuran?

**Penyelesaian.** Kuartet 4,12 mewakili 2 proton per molekul etil asetat: jumlah relatif molekul = 1,00/2 = 0,500. Singlet 3,67 mewakili 3 proton per molekul metil propanoat: 0,90/3 = 0,300. Fraksi mol etil asetat = 0,500/(0,500 + 0,300) = 0,625 = **62,5%**.

**Memahami hasil.** Sebelum membandingkan, integrasi selalu dibagi dengan jumlah proton yang diwakili sinyal itu. Kesalahan yang paling sering adalah membandingkan luas sinyal langsung (1,00 lawan 0,90), yang akan memberi 53%. Pilih sinyal yang terpisah jelas dan tidak bertumpuk dengan sinyal senyawa lain.
:::

::: {.inti}
**Inti subbab 15.4**

- Luas sinyal ¹H sebanding dengan jumlah proton; integrasi memberi perbandingan, bukan jumlah mutlak.
- Ubah perbandingan menjadi bilangan bulat dengan memakai jumlah total proton dari rumus molekul.
- Perbandingan mol dalam campuran = (integrasi / jumlah H per molekul) untuk setiap komponen.
- Integrasi ¹³C rutin tidak dapat dipercaya.
:::

::: {.kuis}
**Kuis cepat 15.4** Senyawa C₈H₁₀ memberi sinyal δ 7,05 (integrasi 2,0) dan δ 2,30 (integrasi 3,0). (a) Berapa proton setiap sinyal? (b) Usulkan struktur.
:::
