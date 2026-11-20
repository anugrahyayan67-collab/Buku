# Bab 11 Kesetimbangan Fasa Dua dan Tiga Komponen

Di kilang minyak, menara setinggi gedung sepuluh lantai memisahkan minyak mentah menjadi gas, bensin, minyak tanah, solar, dan aspal, tanpa satu pun reaksi kimia. Di laboratorium, etanol hasil fermentasi dapat dipekatkan dengan distilasi sampai 95,6%, tetapi tidak setetes pun lebih; distilasi berikutnya, berapa kali pun diulang, berhenti di angka yang sama. Di Jawa dan Sumatra, daun nilam dan serai wangi disuling dengan uap air untuk menghasilkan minyak atsiri, padahal minyak itu mendidih jauh di atas 100 °C. Dan solder elektronik meleleh pada 183 °C, lebih rendah daripada timah maupun timbal yang menyusunnya.

Keempat gejala ini adalah bagian dari satu cerita: kesetimbangan fasa campuran. Bab 8 menggambarkan kesetimbangan fasa zat murni pada bidang tekanan–suhu. Bab 10 memberi rumus potensial kimia zat dalam larutan. Bab ini menggabungkan keduanya. Untuk campuran dua komponen, komposisi menjadi variabel ketiga, dan diagram fasa harus memperlihatkannya. Kita akan membaca **diagram tekanan–komposisi** dan **diagram suhu–komposisi** untuk campuran cair–uap, memahami distilasi fraksional dan batasnya pada **azeotrop**, lalu beralih ke cairan yang bercampur sebagian, campuran padat–cair dengan **titik eutektik**, dan akhirnya diagram **segitiga** untuk tiga komponen, dasar ekstraksi pelarut.

Satu alat dipakai di seluruh bab: **aturan tuas**, yang memberi tahu berapa banyak setiap fasa terbentuk ketika campuran terpisah menjadi dua fasa. Dengan aturan fasa Gibbs dan aturan tuas, setiap diagram fasa dapat dibaca seperti peta.

::: {.strategi}
**Pertanyaan pembuka**

1. Berapa banyak variabel yang dapat diubah bebas dalam campuran dua fasa dua komponen?
2. Mengapa campuran dua cairan mendidih dalam rentang suhu, bukan pada satu suhu?
3. Bagaimana kolom distilasi memisahkan dua cairan yang titik didihnya berdekatan?
4. Mengapa etanol tidak dapat dimurnikan melewati 95,6% dengan distilasi biasa?
5. Mengapa minyak atsiri dapat disuling dengan uap air di bawah 100 °C?
6. Mengapa campuran dua padatan dapat meleleh pada suhu yang lebih rendah daripada keduanya?
7. Mengapa ekstraksi berulang dengan sedikit pelarut lebih baik daripada sekali dengan banyak pelarut?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menurunkan aturan fasa Gibbs dan menghitung banyaknya komponen dan derajat kebebasan.
2. Membaca diagram tekanan–komposisi dan suhu–komposisi serta memakai aturan tuas.
3. Menjelaskan distilasi fraksional dengan langkah-langkah kesetimbangan pada diagram suhu–komposisi.
4. Menjelaskan azeotrop dan hubungannya dengan penyimpangan dari hukum Raoult.
5. Memakai model larutan reguler untuk menjelaskan cairan yang bercampur sebagian dan menghitung suhu kritis kelarutannya.
6. Menghitung kelarutan ideal dan titik eutektik dari entalpi peleburan, serta membaca kurva pendinginan.
7. Membaca diagram segitiga dan menghitung hasil ekstraksi pelarut.
:::

::: {.mat}
**Prasyarat**

Dari Bab 8: aturan fasa untuk satu komponen, diagram fasa zat murni. Dari Bab 10: hukum Raoult, potensial kimia larutan ideal, aktivitas, dan model larutan reguler (subbab 10.7). Dari Bab 9: Gibbs–Duhem. Dari matematika: menyelesaikan persamaan tak linear secara numerik (bisa dengan kalkulator atau beberapa kali coba-coba).
:::

## 11.1 Aturan fasa Gibbs

Di subbab 8.8 kita menurunkan aturan fasa untuk zat murni dengan menghitung variabel dan persamaan pengikat. Kini kita melakukan hal yang sama untuk campuran.

Lebih dulu, apa yang dimaksud **komponen**? Banyaknya komponen *C* adalah banyaknya **minimum** zat yang diperlukan untuk menyusun semua fasa dalam sistem, dengan memperhitungkan reaksi yang setimbang di dalamnya. Ini berbeda dari banyaknya zat (spesies) yang ada. Air murni berisi H₂O, H₃O⁺, dan OH⁻, tetapi hanya satu komponen, karena semua spesies itu dibentuk dari H₂O dan jumlahnya ditentukan oleh kesetimbangan autoionisasi. Aturannya: *C* = banyaknya spesies dikurangi banyaknya reaksi yang setimbang dan banyaknya syarat tambahan (seperti netralitas listrik atau perbandingan tetap yang dipaksakan cara pembuatan sistem).

Sekarang hitung variabel. Dalam setiap fasa, komposisi ditentukan oleh *C* − 1 fraksi mol (yang terakhir ditentukan karena jumlahnya satu). Dengan *P* fasa, ada $P(C - 1)$ variabel komposisi, ditambah suhu dan tekanan yang sama di semua fasa: total $P(C - 1) + 2$ variabel intensif.

Persamaan pengikatnya berasal dari kesetimbangan: potensial kimia setiap komponen harus sama di semua fasa. Untuk satu komponen di *P* fasa, ada *P* − 1 persamaan ($\mu_\text{J}(\alpha) = \mu_\text{J}(\beta) = \cdots$). Untuk *C* komponen, ada $C(P - 1)$ persamaan. Derajat kebebasan adalah selisihnya:

$$
F = P(C - 1) + 2 - C(P - 1) = C - P + 2 .
$$

::: {.inti}
$$
F = C - P + 2 . \qquad \text{(11.1)}
$$
**Aturan fasa Gibbs.** Untuk dua komponen, $F = 4 - P$: paling banyak empat fasa dapat setimbang bersama, dan diagram fasa lengkapnya memerlukan tiga sumbu (*p*, *T*, dan komposisi). Bila tekanan atau suhu ditetapkan, satu derajat kebebasan terpakai, dan $F' = 3 - P$.
:::

Karena diagram tiga dimensi sukar digambar di atas kertas, diagram fasa dua komponen biasanya digambar dengan salah satu variabel ditetapkan. Bila suhu tetap, diperoleh **diagram tekanan–komposisi** (subbab 11.2). Bila tekanan tetap, biasanya 1 atm, diperoleh **diagram suhu–komposisi** (subbab 11.3), yang paling berguna di laboratorium karena kebanyakan proses berlangsung pada tekanan udara.

::: {.contoh}
**Contoh 11.1 · Menghitung derajat kebebasan**

Tentukan *C*, *P*, dan *F* untuk: (a) larutan garam dapur dalam air yang setimbang dengan uap air; (b) larutan garam jenuh dengan endapan NaCl dan uap air; (c) campuran es, NaCl padat, larutan garam, dan uap air.

**Penyelesaian.** (a) *C* = 2 (NaCl, H₂O), *P* = 2 (larutan, uap): *F* = 2. Misalnya suhu dan konsentrasi dapat dipilih bebas, lalu tekanan uap sudah tertentu.

(b) *C* = 2, *P* = 3 (larutan, padatan, uap): *F* = 1. Bila suhu dipilih, konsentrasi larutan jenuh dan tekanan uapnya sudah tertentu. Kelarutan adalah fungsi suhu saja.

(c) *C* = 2, *P* = 4: *F* = 0. Keempat fasa hanya dapat setimbang pada satu suhu dan satu tekanan, yaitu titik eutektik NaCl–air (−21,1 °C) dengan tekanan uapnya.

**Memahami hasil.** Setiap tambahan fasa mengurangi satu kebebasan. Pada (b), "jenuh" bukan pilihan kita tetapi akibat hadirnya fasa padat: begitu endapan ada, konsentrasi tidak bebas lagi. Pada (c), sistem menjadi "termometer alami" yang suhunya tetap selama keempat fasa ada, seperti campuran es–air pada 0 °C.
:::

::: {.contoh}
**Contoh 11.2 · Komponen bila ada reaksi**

Tentukan banyaknya komponen dalam: (a) CaCO₃(s) yang dipanaskan dalam wadah tertutup sampai setimbang dengan CaO(s) dan CO₂(g); (b) NH₄Cl(s) yang dipanaskan sampai setimbang dengan NH₃(g) dan HCl(g); (c) seperti (b), tetapi ke dalam wadah ditambahkan NH₃ berlebih.

**Penyelesaian.** (a) Tiga spesies, satu reaksi setimbang ($\text{CaCO}_3 \rightleftharpoons \text{CaO} + \text{CO}_2$): *C* = 2. Dengan *P* = 3 (dua padatan dan gas), *F* = 1: tekanan CO₂ hanya bergantung pada suhu.

(b) Tiga spesies, satu reaksi, ditambah satu syarat: NH₃ dan HCl terbentuk dalam jumlah sama, sehingga komposisi gas tertentu. *C* = 3 − 1 − 1 = 1. Dengan *P* = 2, *F* = 1.

(c) Syarat perbandingan sama hilang: *C* = 2, *P* = 2, *F* = 2.

**Memahami hasil.** Pada (a) dan (b), sistem berperilaku seperti zat murni yang "menyublim": tekanan gas di atas padatan tertentu oleh suhu. Itulah sebabnya kapur tohor dibuat dalam tanur yang tekanan CO₂-nya dijaga di bawah tekanan penguraian. Hasil (c) menunjukkan bahwa cara menyiapkan sistem ikut menentukan banyaknya komponen.
:::

::: {.kuis}
**Kuis cepat 11.1** Berapa paling banyak fasa yang dapat setimbang bersama dalam sistem tiga komponen?
:::

## 11.2 Diagram tekanan uap–komposisi

Kembali ke campuran benzena–toluena dari Bab 10, kini pada suhu tetap 25 °C. Untuk setiap komposisi cairan, hukum Raoult memberi tekanan uap total (persamaan (10.5)), yaitu garis lurus. Tetapi uap yang setimbang dengan cairan itu mempunyai komposisi lain, $y_\text{A} = x_\text{A}p_\text{A}^*/p$. Bila *p* dinyatakan sebagai fungsi komposisi uap, hasilnya adalah

$$
p = \frac{p_\text{A}^*p_\text{B}^*}{p_\text{A}^* + (p_\text{B}^* - p_\text{A}^*)y_\text{A}} , \qquad \text{(11.2)}
$$

kurva yang melengkung di bawah garis cair (lihat Pembahasan soal terpilih di akhir bab). Gambar 11.1 memperlihatkan kedua garis itu sekaligus.

![Gambar 11.1 Diagram tekanan–komposisi benzena–toluena pada 25 °C. Di atas garis cair hanya ada cairan; di bawah garis uap hanya ada uap. Di antara keduanya, sistem terpisah menjadi cairan dan uap. Garis datar melalui titik a (garis hubung) menghubungkan komposisi cairan $x_\text{B}$ dan uap $y_\text{B}$ yang setimbang.](fig/pxy.png){width=72%}

Diagram ini dibaca dengan memakai **komposisi keseluruhan** *z*, yaitu fraksi mol benzena dalam seluruh sistem (cairan dan uap bersama), sebagai sumbu mendatar. Pada tekanan tinggi, semua zat berada dalam cairan. Pada tekanan rendah, semua menguap. Di antara keduanya, titik (*z*, *p*) jatuh di daerah dua fasa, dan sistem terpisah menjadi cairan dengan komposisi $x_\text{B}$ (dibaca pada garis cair) dan uap dengan komposisi $y_\text{B}$ (dibaca pada garis uap), keduanya pada tekanan yang sama. Garis mendatar yang menghubungkan keduanya disebut **garis hubung**.

Bayangkan cairan dengan *z* = 0,40 di dalam silinder berpiston, dan tekanan diturunkan perlahan pada suhu tetap. Pada 7,35 kPa (garis cair), gelembung uap pertama muncul; tekanan ini disebut **tekanan gelembung**. Ketika tekanan terus turun, makin banyak cairan menguap, dan komposisi kedua fasa bergeser sepanjang garis masing-masing. Pada tekanan di garis uap, tetes cairan terakhir menguap; tekanan ini disebut **tekanan embun**. Di bawahnya hanya ada uap.

Berapa banyak cairan dan uap di titik a? Banyaknya total benzena harus sama dengan jumlah benzena di kedua fasa: $nz = n_\text{l}x + n_\text{v}y$, dengan $n = n_\text{l} + n_\text{v}$. Menyusun ulang:

::: {.inti}
$$
n_\text{l}(z - x) = n_\text{v}(y - z) \qquad\text{atau}\qquad \frac{n_\text{l}}{n_\text{v}} = \frac{y - z}{z - x} . \qquad \text{(11.3)}
$$
**Aturan tuas.** Banyaknya setiap fasa berbanding terbalik dengan jarak titik keseluruhan ke garis fasa itu, seperti dua beban pada tuas yang setimbang di titik tumpu *z*. Aturan ini berlaku untuk setiap daerah dua fasa pada diagram fasa apa pun.
:::

::: {.contoh}
**Contoh 11.3 · Tekanan gelembung dan tekanan embun**

Untuk campuran benzena–toluena dengan *z* = 0,400 pada 25 °C ($p_\text{benzena}^* = 12{,}7$ kPa, $p_\text{toluena}^* = 3{,}79$ kPa), hitung tekanan gelembung dan tekanan embun, serta komposisi tetes cairan terakhir.

**Penyelesaian.** Tekanan gelembung: seluruh sistem masih cair dengan *x* = 0,400; dari Raoult, $p = (0{,}400)(12{,}7) + (0{,}600)(3{,}79) = 7{,}35$ kPa.

Tekanan embun: seluruh sistem sudah uap dengan *y* = 0,400. Dari (11.2), atau dari $1/p = y_\text{A}/p_\text{A}^* + y_\text{B}/p_\text{B}^*$:
$$
\frac{1}{p} = \frac{0{,}400}{12{,}7} + \frac{0{,}600}{3{,}79} = 0{,}1898\ \text{kPa}^{-1} , \qquad p = 5{,}27\ \text{kPa} .
$$
Tetes cairan terakhir: $x_\text{benzena} = y\,p/p^*_\text{benzena} = (0{,}400)(5{,}27)/12{,}7 = 0{,}166$.

**Memahami hasil.** Campuran menguap dalam rentang tekanan 7,35 sampai 5,27 kPa, bukan pada satu tekanan seperti zat murni. Tetes terakhir hanya berisi 17% benzena: toluena, yang kurang mudah menguap, tertinggal sampai akhir.
:::

::: {.contoh}
**Contoh 11.4 · Aturan tuas**

Campuran yang sama (*z* = 0,400) ditaruh pada 6,00 kPa dan 25 °C. Hitung komposisi cairan dan uap, serta fraksi sistem yang berupa cairan.

**Penyelesaian.** Garis cair: $6{,}00 = 3{,}79 + (12{,}7 - 3{,}79)x$, sehingga *x* = 0,248. Uap: $y = (0{,}248)(12{,}7)/6{,}00 = 0{,}525$. Aturan tuas:
$$
\frac{n_\text{l}}{n} = \frac{y - z}{y - x} = \frac{0{,}525 - 0{,}400}{0{,}525 - 0{,}248} = 0{,}451 .
$$
Jadi 45% sistem berupa cairan dan 55% uap.

**Memahami hasil.** Titik *z* = 0,400 sedikit lebih dekat ke garis uap (jarak 0,125) daripada ke garis cair (jarak 0,152), sehingga uapnya sedikit lebih banyak. Aturan tuas berlaku dalam satuan mol bila sumbunya fraksi mol, dan dalam satuan massa bila sumbunya fraksi massa.
:::

::: {.kuis}
**Kuis cepat 11.2** Pada diagram tekanan–komposisi, mengapa garis uap selalu berada di bawah garis cair?
:::

## 11.3 Diagram suhu–komposisi dan distilasi

Di laboratorium dan industri, distilasi biasanya dilakukan pada tekanan tetap. Diagram yang sesuai adalah **diagram suhu–komposisi**: untuk setiap komposisi, suhu tempat cairan mulai mendidih (**titik gelembung**) dan suhu tempat uap mulai mengembun (**titik embun**). Karena komponen yang mudah menguap mempunyai titik didih rendah, diagram ini kira-kira bayangan cermin diagram tekanan–komposisi: cairan di bawah, uap di atas.

Garis-garisnya dihitung dengan cara yang sama, tetapi kini tekanan uap murni setiap komponen bergantung pada suhu (Bab 8), sehingga setiap titik memerlukan penyelesaian numerik: cari suhu *T* tempat $x_\text{A}p_\text{A}^*(T) + x_\text{B}p_\text{B}^*(T) = 101{,}3$ kPa. Gambar 11.2 dibuat dengan cara ini dari data tekanan uap benzena dan toluena.

![Gambar 11.2 Diagram suhu–komposisi benzena–toluena pada 1 atm. Garis bawah (titik gelembung) adalah suhu mulai mendidih; garis atas (titik embun) adalah suhu mulai mengembun. Tangga menunjukkan lima langkah penguapan–pengembunan yang memperkaya benzena dari 20% menjadi lebih dari 95%.](fig/txy.png){width=72%}

::: {.contoh}
**Contoh 11.5 · Titik gelembung dan titik embun**

Pada 1 atm, (a) pada suhu berapa cairan benzena–toluena dengan $x_\text{benzena} = 0{,}500$ mulai mendidih, dan apa komposisi uap pertamanya? (b) Pada suhu berapa uap dengan $y_\text{benzena} = 0{,}500$ mulai mengembun?

**Rencana.** Tekanan uap murni dihitung dengan persamaan Antoine dari tabel. Suhu dicari dengan mencoba beberapa nilai sampai syaratnya terpenuhi.

**Penyelesaian.** (a) Pada 92,1 °C, $p_\text{benzena}^* = 144{,}6$ kPa dan $p_\text{toluena}^* = 58{,}0$ kPa, sehingga $(0{,}5)(144{,}6) + (0{,}5)(58{,}0) = 101{,}3$ kPa. Titik gelembung 92,1 °C. Uap pertama: $y = (0{,}5)(144{,}6)/101{,}3 = 0{,}714$.

(b) Syaratnya $1/101{,}3 = 0{,}5/p_\text{benzena}^* + 0{,}5/p_\text{toluena}^*$, dipenuhi pada 98,8 °C. Tetes embun pertama mempunyai $x_\text{benzena} = 0{,}291$.

**Memahami hasil.** Campuran 50:50 mendidih pada 92,1 °C, di antara titik didih benzena (80,1 °C) dan toluena (110,6 °C), dan uap pertamanya berisi 71% benzena. Bila uap itu diembunkan dan dididihkan lagi, uap berikutnya lebih kaya lagi.
:::

Itulah prinsip **distilasi fraksional**. Pada Gambar 11.2, mulai dari cairan dengan 20% benzena. Ia mendidih pada 102,1 °C dan menghasilkan uap dengan 37,6% benzena (langkah 1, garis mendatar ke garis embun). Uap itu diembunkan (garis tegak ke garis gelembung), menjadi cairan dengan 37,6% benzena, yang mendidih pada 95,9 °C dan menghasilkan uap dengan 59,7% benzena (langkah 2). Setiap langkah adalah satu kesetimbangan cair–uap, disebut satu **pelat teoretis**. Lima pelat membawa komposisi dari 20% ke 96%.

::: {.contoh}
**Contoh 11.6 · Berapa pelat yang diperlukan?**

Dengan langkah-langkah pada Gambar 11.2, berapa pelat teoretis yang diperlukan untuk memperoleh benzena 99% dari campuran berisi 20% benzena?

**Penyelesaian.** Mengikuti tangga dengan perhitungan yang sama seperti Contoh 11.5: 0,200 → 0,376 → 0,597 → 0,789 → 0,905 → 0,961 → 0,985 → 0,994. Komposisi 99% dilampaui pada langkah ke-7.

**Memahami hasil.** Langkah-langkah awal memberi kemajuan besar; langkah-langkah akhir makin kecil, karena di dekat benzena murni kedua garis saling mendekat. Di kolom distilasi nyata, cairan yang turun dan uap yang naik bertukar zat terus-menerus pada setiap pelat atau di sepanjang bahan isian, sehingga satu kolom melakukan banyak langkah tanpa perlu diembunkan dan didihkan ulang secara terpisah. Kolom laboratorium yang baik setara 10–30 pelat teoretis; kolom industri dapat lebih dari seratus. Makin dekat titik didih kedua komponen, makin rapat kedua garis, dan makin banyak pelat yang diperlukan.
:::

::: {.terapan}
**Kilang minyak.** Minyak mentah adalah campuran ribuan hidrokarbon. Di kilang, minyak dipanaskan sampai sekitar 350–400 °C dan dimasukkan ke bagian bawah menara distilasi. Uap naik melewati puluhan pelat, makin ke atas makin dingin; setiap pelat setimbang pada suhunya sendiri, dan cairan yang terkumpul di setiap ketinggian diambil sebagai fraksi: gas (C₁–C₄) di puncak, nafta dan bensin (C₅–C₁₀), kerosin (C₁₀–C₁₆), solar (C₁₄–C₂₀), lalu minyak berat dan residu di dasar. Prinsipnya tepat seperti Gambar 11.2, diperluas ke banyak komponen. Residu yang terlalu berat untuk diuapkan pada 1 atm tanpa terurai disuling lagi pada tekanan rendah (distilasi vakum), memanfaatkan turunnya titik didih bersama tekanan yang kita pelajari di Bab 8.
:::

::: {.kuis}
**Kuis cepat 11.3** Ketika campuran benzena–toluena didistilasi sederhana (tanpa kolom), mengapa suhu di labu terus naik selama distilasi?
:::
