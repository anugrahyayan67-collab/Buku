# Bab 1 Gas Ideal dan Teori Kinetik

Buka sebotol parfum di sudut kamar. Molekul-molekul wangi itu, seperti molekul nitrogen dan oksigen di sekitarnya, melesat dengan kelajuan sekitar 500 meter per detik, lebih cepat daripada peluru pistol dan lebih cepat daripada bunyi. Dengan kelajuan seperti itu, wangi parfum semestinya sampai ke hidung orang di seberang kamar dalam seperseratus detik. Kenyataannya, kita perlu menunggu beberapa menit, dan tanpa embusan angin wangi itu bahkan tidak pernah sampai sejauh itu. Ke mana perginya semua kelajuan tadi?

Jawabannya tersembunyi di dalam gambaran yang akan kita bangun di bab ini: gas adalah kumpulan molekul yang bergerak acak, terus-menerus bertumbukan satu sama lain dan dengan dinding wadahnya. Dari gambaran sederhana itu kita akan menurunkan hampir semua sifat gas yang dapat diukur: tekanan, hubungan antara tekanan, volume, dan suhu, kelajuan molekul, laju gas merembes melalui lubang kecil, dan seberapa jauh sebuah molekul dapat bergerak sebelum menabrak molekul lain.

Gas adalah titik awal yang wajar untuk termodinamika kimia. Di antara ketiga wujud zat, gaslah yang paling sederhana, karena molekul-molekulnya berjauhan dan hampir tidak saling memengaruhi. Kesederhanaan itu membuat kita dapat menghubungkan secara langsung dunia molekul yang tidak terlihat dengan besaran yang kita baca di manometer dan termometer. Hubungan itulah yang akan terus kita pakai di seluruh buku ini.

::: {.strategi}
**Pertanyaan pembuka**

1. Apa sebenarnya yang diukur sebuah termometer, dan mengapa suhu mempunyai titik nol mutlak?
2. Mengapa satu mol gas apa pun, dari hidrogen sampai uap iodin, menempati volume yang hampir sama pada suhu dan tekanan yang sama?
3. Dari mana datangnya tekanan gas, padahal setiap molekul hanya menumbuk dinding sesaat?
4. Mengapa hidrogen bocor lebih cepat daripada oksigen dari balon yang sama?
5. Mengapa wangi parfum menyebar begitu lambat, padahal molekulnya bergerak begitu cepat?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Membedakan sistem terbuka, tertutup, dan terisolasi, serta variabel keadaan intensif dan ekstensif.
2. Menjelaskan hukum ke-nol termodinamika dan arti suhu termodinamika.
3. Mengubah satuan tekanan dan membaca barometer serta manometer.
4. Memakai hukum Boyle, Charles, Avogadro, dan persamaan gas ideal untuk menghitung jumlah zat, massa molar, dan massa jenis gas.
5. Menghitung tekanan parsial dan fraksi mol dalam campuran gas.
6. Menurunkan tekanan gas dari teori kinetik dan menghubungkan suhu dengan energi kinetik molekul.
7. Menghitung kelajuan paling mungkin, rata-rata, dan akar rata-rata kuadrat dari sebaran Maxwell–Boltzmann.
8. Memakai hukum Graham untuk efusi dan menghitung jalan bebas rata-rata serta frekuensi tumbukan.
:::

::: {.mat}
**Prasyarat**

Konsep mol dan massa molar dari Kimia Dasar. Dari *Fisika Umum*: suhu dan gas ideal (subbab 10.1 dan 10.3), teori kinetik gas (subbab 10.7), dan sebaran kelajuan Maxwell–Boltzmann (subbab 10.8). Bab ini mengulang bagian-bagian itu dari sudut pandang kimia, jadi kamu boleh mulai di sini.
:::

## 1.1 Sistem, lingkungan, dan variabel keadaan

Termodinamika selalu dimulai dengan satu keputusan: bagian mana dari alam yang sedang kita pelajari? Bagian itu disebut **sistem**. Isinya bisa berupa gas di dalam silinder, larutan di dalam gelas kimia, atau sel hidup. Semua yang berada di luar sistem dan dapat bertukar sesuatu dengannya disebut **lingkungan**. Batas di antara keduanya bisa nyata, seperti dinding labu, atau hanya bayangan, seperti permukaan khayal yang mengurung sejumlah udara tertentu.

Mengapa pembagian ini penting? Karena hampir semua pertanyaan termodinamika berbunyi "apa yang berpindah melintasi batas itu?" Ada dua hal yang dapat berpindah: **materi** dan **energi**. Dari situ muncul tiga jenis sistem:

* **Sistem terbuka** dapat bertukar materi dan energi dengan lingkungan. Contohnya air mendidih di panci tanpa tutup: uap keluar, kalor masuk.
* **Sistem tertutup** dapat bertukar energi tetapi tidak materi. Contohnya reaksi di dalam ampul kaca yang tersegel: kalornya dapat merambat ke luar, tetapi tidak ada molekul yang lolos.
* **Sistem terisolasi** tidak bertukar apa pun. Termos yang ideal mendekati keadaan ini.

Begitu sistem ditentukan, kita perlu cara untuk menyatakan **keadaannya**. Untuk sejumlah gas murni, ternyata cukup empat besaran: jumlah zat *n*, volume *V*, tekanan *p*, dan suhu *T*. Besaran-besaran ini disebut **variabel keadaan**, karena nilainya hanya bergantung pada keadaan sistem saat ini, bukan pada cara sistem itu sampai ke keadaan tersebut. Gas bersuhu 25 °C tetap bersuhu 25 °C, entah ia baru saja dipanaskan dari 0 °C atau didinginkan dari 100 °C.

Variabel keadaan terbagi dua menurut perilakunya ketika sistem dibagi. Bayangkan sebuah labu gas dipisahkan menjadi dua bagian sama besar oleh sekat. Volume dan jumlah zat masing-masing bagian menjadi separuhnya; besaran seperti ini disebut **ekstensif**, karena bergantung pada ukuran sistem. Tekanan dan suhu di kedua bagian tetap sama; besaran seperti ini disebut **intensif**. Hasil bagi dua besaran ekstensif selalu intensif. Itulah sebabnya massa jenis (*m*/*V*) dan **volume molar** $V_\text{m} = V/n$ adalah sifat zat, bukan sifat sampel tertentu.

::: {.contoh}
**Contoh 1.1 · Mengenali jenis sistem dan variabel**

(a) Tentukan jenis sistem untuk: kopi panas di dalam cangkir terbuka; kantong infus yang tersegel; tabung reaksi di dalam bom kalorimeter yang dianggap sempurna. (b) Manakah besaran intensif: massa, massa jenis, suhu titik didih, volume molar, kapasitas kalor?

**Penyelesaian.** (a) Kopi dalam cangkir terbuka adalah sistem terbuka: uap air keluar dan kalor mengalir ke udara. Kantong infus tersegel adalah sistem tertutup: isinya tetap, tetapi suhunya dapat berubah. Isi bom kalorimeter yang sempurna diperlakukan sebagai sistem terisolasi bila kalorimeter dan isinya dipandang bersama.

(b) Massa jenis, suhu titik didih, dan volume molar intensif. Massa dan kapasitas kalor ekstensif: dua kali lebih banyak zat memerlukan dua kali lebih banyak kalor untuk kenaikan suhu yang sama.

**Memahami hasil.** Pembagian ini bukan sekadar istilah. Dalam rumus termodinamika, besaran intensif seperti *p* dan *T* menentukan **arah** perpindahan (kalor mengalir dari *T* tinggi ke *T* rendah), sedangkan besaran ekstensif menentukan **berapa banyak** yang berpindah.
:::

::: {.kuis}
**Kuis cepat 1.1** Sebuah balon karet berisi helium dibiarkan di bawah terik matahari. Apakah balon itu sistem terbuka, tertutup, atau terisolasi bila kita mengabaikan helium yang merembes melalui karet? Bagaimana jika rembesan itu tidak diabaikan?
:::

## 1.2 Kesetimbangan termal, hukum ke-nol, dan suhu

Kita memakai kata "panas" dan "dingin" setiap hari, tetapi termodinamika memerlukan pengertian suhu yang lebih tajam. Pengertian itu lahir dari pengamatan sederhana: bila dua benda bersentuhan cukup lama, perubahan pada keduanya akhirnya berhenti. Keadaan ketika tidak ada lagi perubahan, walaupun benda-benda itu dapat bertukar energi, disebut **kesetimbangan termal**.

Pertanyaan berikutnya muncul dengan sendirinya: bagaimana kita tahu dua benda berada dalam kesetimbangan termal tanpa menempelkan keduanya? Pengalaman menjawabnya dengan pernyataan yang tampak terlalu jelas untuk dijadikan hukum:

::: {.inti}
**Hukum ke-nol termodinamika.** Jika benda A berada dalam kesetimbangan termal dengan benda B, dan B berada dalam kesetimbangan termal dengan benda C, maka A juga berada dalam kesetimbangan termal dengan C.
:::

Hukum ini diberi nomor nol karena baru dirumuskan setelah hukum pertama dan kedua, padahal ia mendasari keduanya. Isinya penting: hukum ke-nol menjamin adanya satu besaran yang sama nilainya bagi semua benda yang setimbang termal satu sama lain. Besaran itulah **suhu**. Benda B dalam pernyataan hukum di atas tidak lain adalah termometer. Kita tidak perlu menempelkan A dan C; cukup bandingkan bacaan termometer pada keduanya.

Termometer apa yang dipakai? Hampir semua sifat zat berubah dengan suhu: panjang batang logam, volume raksa, hambatan kawat platina. Masalahnya, skala yang dibuat dari sifat-sifat itu tidak selalu sepakat di antara titik-titik kalibrasinya. Termometer gas memberi jalan keluar. Bila tekanan sejumlah gas diukur pada volume tetap, makin rendah tekanannya, makin seragam perilaku semua gas, apa pun jenisnya. Pada batas tekanan sangat rendah, tekanan gas bervolume tetap sebanding dengan suhu, dan perbandingan itu dipakai untuk **mendefinisikan** suhu termodinamika:

$$
T = 273{,}16\ \text{K} \times \frac{p}{p_3} \qquad \text{(1.1)}
$$

dengan $p_3$ tekanan gas yang sama ketika termometer dicelupkan ke dalam air pada **titik tripelnya**, keadaan tunggal tempat es, air, dan uap air hidup berdampingan. Satuan suhu termodinamika adalah **kelvin** (K). Skala Celsius hanyalah skala kelvin yang digeser:

$$
\theta/{}^\circ\text{C} = T/\text{K} - 273{,}15 . \qquad \text{(1.2)}
$$

Perhatikan dua angka yang mirip: 273,16 di (1.1) dan 273,15 di (1.2). Keduanya bukan salah ketik. Titik acuan skala kelvin adalah titik tripel air, yang ditetapkan 273,16 K. Titik nol skala Celsius adalah titik beku air pada tekanan 1 atm, yang sedikit lebih rendah, yaitu 273,15 K. Jadi titik tripel air terletak pada 0,01 °C. (Sejak 2019, kelvin didefinisikan melalui nilai tetap tetapan Boltzmann, tetapi kedua angka ini tetap berlaku dalam ketelitian laboratorium biasa.)

Persamaan (1.1) juga menjelaskan mengapa ada **nol mutlak**. Tekanan gas tidak mungkin negatif, sehingga suhu termodinamika tidak mungkin di bawah nol. Gambaran molekul yang akan kita turunkan di subbab 1.7 memberi alasannya: suhu mengukur energi kinetik rata-rata molekul, dan energi kinetik tidak dapat lebih kecil dari nol.

::: {.contoh}
**Contoh 1.2 · Termometer gas bervolume tetap**

Sebuah termometer gas bervolume tetap menunjukkan tekanan 26,66 kPa ketika dicelupkan ke dalam sel titik tripel air. Di sebuah laboratorium di Bandung, termometer itu dicelupkan ke dalam air yang sedang mendidih, dan tekanannya menjadi 36,17 kPa. Berapa suhu air mendidih itu dalam kelvin dan derajat Celsius?

**Penyelesaian.** Dari persamaan (1.1):
$$
T = 273{,}16\ \text{K} \times \frac{36{,}17\ \text{kPa}}{26{,}66\ \text{kPa}} = 370{,}6\ \text{K} .
$$
Dalam Celsius: $370{,}6 - 273{,}15 = 97{,}5$ °C.

**Memahami hasil.** Air mendidih pada 100 °C hanya bila tekanan di atasnya 1 atm. Bandung terletak sekitar 770 m di atas permukaan laut, dan tekanan udaranya hanya sekitar 92 kPa, sehingga air sudah mendidih pada sekitar 97,5 °C. Subbab 8.4 akan menghitung pergeseran titik didih ini. Gas di dalam termometer juga tidak sepenuhnya ideal, tetapi pada tekanan serendah 27 kPa koreksinya hanya beberapa perseratus kelvin. Untuk ketelitian tertinggi, ahli termometri mengulang pengukuran pada tekanan awal yang makin kecil, lalu mengekstrapolasi hasilnya ke tekanan nol. Penyimpangan gas dari perilaku ideal inilah pokok bahasan Bab 2.
:::

::: {.kuis}
**Kuis cepat 1.2** Suhu sebuah ruangan naik dari 20 °C menjadi 30 °C. Apakah suhunya naik "50%"? Berapa kenaikan relatifnya dalam kelvin?
:::

## 1.3 Tekanan dan cara mengukurnya

Variabel keadaan berikutnya, tekanan, didefinisikan sebagai gaya per satuan luas:

$$
p = \frac{F}{A} . \qquad \text{(1.3)}
$$

Satuan SI-nya adalah **pascal**, 1 Pa = 1 N m⁻². Satu pascal sangat kecil, kira-kira tekanan selembar kertas yang diletakkan di atas meja. Karena itu kimiawan lebih sering memakai satuan yang lebih besar:

| Satuan | Nilai dalam Pa | Keterangan |
|---|---|---|
| bar | $10^5$ Pa (tepat) | tekanan standar $p^\circ = 1$ bar |
| atmosfer standar (atm) | 101 325 Pa (tepat) | kira-kira tekanan udara di permukaan laut |
| torr | 101 325/760 Pa ≈ 133,32 Pa | 760 torr = 1 atm |
| mmHg | ≈ 133,322 Pa | praktis sama dengan torr |

Sejak 1982, IUPAC menetapkan **tekanan standar** untuk data termodinamika sebesar 1 bar, bukan 1 atm. Perbedaannya hanya 1,3%, tetapi cukup untuk menimbulkan kebingungan bila tabel yang berbeda dicampur. Di buku ini, setiap data standar mengacu pada 1 bar.

Bagaimana tekanan diukur? Cara tertua memanfaatkan cairan. Pada **barometer** Torricelli, tabung kaca berisi raksa dibalik ke dalam bak raksa. Raksa di dalam tabung turun sampai berat kolomnya diimbangi oleh tekanan udara pada permukaan bak. Kolom setinggi *h* dari cairan bermassa jenis ρ menekan dasarnya dengan

$$
p = \rho gh , \qquad \text{(1.4)}
$$

karena berat kolom itu $\rho Ahg$ dibagi luas alasnya *A*. Persamaan (1.4) menjelaskan mengapa Torricelli memakai raksa: raksa 13,6 kali lebih berat daripada air, sehingga tekanan 1 atm cukup ditopang kolom setinggi 760 mm. Dengan air, kolomnya akan setinggi 10,3 m.

Untuk mengukur tekanan gas di dalam wadah, kimiawan memakai **manometer**: tabung berbentuk U berisi cairan, dengan satu ujung tersambung ke gas. Bila ujung yang lain terbuka ke udara, selisih tinggi cairan di kedua kaki menyatakan selisih tekanan gas terhadap tekanan atmosfer.

Kedua alat itu digambarkan berdampingan pada Gambar 1.1. Perhatikan bahwa barometer mengukur tekanan **mutlak**, karena di atas kolom raksanya hampa, sedangkan manometer ujung terbuka hanya mengukur **selisih** tekanan terhadap udara luar. Karena itu bacaan manometer selalu harus dijumlahkan dengan bacaan barometer.

![Gambar 1.1 Barometer (kiri) dan manometer ujung terbuka (kanan). Pada barometer, berat kolom raksa setinggi *h* diimbangi tekanan udara pada permukaan bak. Pada manometer, raksa di kaki terbuka berdiri lebih tinggi bila tekanan gas lebih besar daripada tekanan udara; selisih tinggi Δ*h* sebanding dengan selisih tekanan.](fig/manometer.png){width=84%}

::: {.contoh}
**Contoh 1.3 · Manometer ujung terbuka**

Sebuah labu gas disambungkan ke manometer raksa yang ujung lainnya terbuka ke udara. Raksa di kaki yang terbuka berdiri 125 mm lebih tinggi daripada di kaki yang tersambung ke labu. Barometer di laboratorium menunjukkan 755 mmHg. Berapa tekanan gas dalam mmHg dan kPa?

**Rencana.** Raksa didorong ke arah kaki yang terbuka, jadi gas menekan **lebih kuat** daripada udara luar. Tekanan gas = tekanan atmosfer + tekanan kolom raksa setinggi selisih itu.

**Penyelesaian.** $p = 755 + 125 = 880$ mmHg. Dalam kPa: $880 \times 0{,}133\,32 = 117{,}3$ kPa.

**Memahami hasil.** Bila kaki yang tersambung ke labu justru lebih tinggi, tekanan gas lebih **rendah** daripada tekanan atmosfer, dan selisih itu dikurangkan. Cara paling aman untuk tidak salah tanda: tanyakan sisi mana yang mendorong raksa lebih kuat.
:::

::: {.awas}
**Tekanan, bukan gaya.** Gas dalam labu kecil dan gas dalam tangki besar dapat bertekanan sama, walaupun gaya total pada dinding tangki jauh lebih besar. Tekanan adalah besaran intensif; gaya total pada dinding adalah tekanan dikali luas.
:::

::: {.kuis}
**Kuis cepat 1.3** Mengapa tekanan udara di puncak gunung lebih rendah daripada di pantai? Pakai gagasan persamaan (1.4).
:::
