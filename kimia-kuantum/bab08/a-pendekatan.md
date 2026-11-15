# Bab 8 Metode Pendekatan: Variasi dan Perturbasi

Atom helium hanya mempunyai dua elektron. Energi yang diperlukan untuk mencabut keduanya, satu demi satu, telah diukur dengan sangat teliti: 24,59 eV untuk elektron pertama dan 54,42 eV untuk elektron kedua, sehingga energi total atom itu $-79{,}0$ eV. Persamaan Schrödinger helium hanya berbeda dari persamaan dua ion He⁺ yang terpisah oleh satu suku kecil, tolakan $1/r_{12}$ antara kedua elektron. Namun sampai hari ini tidak seorang pun dapat menyelesaikan persamaan itu secara eksak, dan para matematikawan yakin bahwa penyelesaian dalam bentuk rumus tertutup memang tidak ada. Anehnya, energi helium telah *dihitung* sampai lebih dari dua puluh angka penting, jauh lebih teliti daripada kemampuan alat ukur mana pun. Bagaimana kita dapat menghitung sesuatu setepat itu tanpa pernah menyelesaikan persamaannya?

Jawabannya terletak pada dua gagasan yang menjadi tulang punggung seluruh kimia kuantum modern. Yang pertama adalah **metode variasi**: tebak bentuk fungsi gelombang, sisakan beberapa parameter yang dapat diatur, lalu cari nilai parameter yang membuat energi serendah mungkin. Sebuah teorema yang sederhana tetapi sangat kuat menjamin bahwa energi hasil tebakan tidak pernah jatuh di bawah energi yang sebenarnya, sehingga "makin rendah, makin baik". Yang kedua adalah **teori perturbasi**: mulai dari masalah yang dapat diselesaikan, lalu tambahkan pengaruh suku kecil yang diabaikan sebagai deret koreksi, orde demi orde.

Kedua gagasan ini jauh melampaui atom helium. Metode Hartree–Fock dan interaksi konfigurasi yang dipakai setiap program kimia komputasi adalah metode variasi; teori Møller–Plesset (MP2) adalah teori perturbasi. Polarisabilitas molekul, gaya dispersi London yang membuat gas mulia dapat dicairkan, efek substituen pada warna zat warna, kekuatan pita serapan dalam spektrum UV-Vis, dan aturan seleksi spektroskopi, semuanya adalah hasil teori perturbasi. Bab ini membangun kedua alat itu dari dasar, menerapkannya pada atom helium sebagai batu uji, dan menutupnya dengan perturbasi bergantung waktu yang menjelaskan bagaimana cahaya menyebabkan transisi antartingkat energi.

::: {.strategi}
**Pertanyaan pembuka**

1. Bagaimana kita tahu bahwa energi yang dihitung dari fungsi gelombang tebakan tidak pernah lebih rendah daripada energi keadaan dasar yang sebenarnya?
2. Mengapa setiap elektron helium "merasakan" muatan inti yang lebih kecil daripada 2, dan berapa tepatnya?
3. Mengapa program kimia komputasi, betapa pun rumitnya, pada intinya hanya membangun dan mendiagonalkan matriks?
4. Mengapa dua atom argon yang netral dan bersimetri bola tetap saling tarik, sehingga argon dapat dicairkan?
5. Mengapa sebagian transisi spektroskopi menghasilkan pita yang sangat kuat, sebagian lemah, dan sebagian lagi sama sekali tidak muncul?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menjelaskan mengapa hampir semua masalah kimia memerlukan metode pendekatan, dan kapan variasi atau perturbasi lebih cocok.
2. Membuktikan teorema variasi dan memakainya untuk memperoleh batas atas energi keadaan dasar dan keadaan tereksitasi.
3. Memilih fungsi uji yang masuk akal, menghitung integral variasi, dan mengoptimumkan parameternya.
4. Menghitung energi atom helium dan ion mirip helium dengan muatan inti efektif, serta menafsirkan tetapan perisai.
5. Menurunkan persamaan sekuler metode variasi linear dan menyelesaikannya untuk dua sampai enam fungsi basis.
6. Menulis masalah variasi linear sebagai masalah nilai eigen matriks dan menyelesaikannya dengan Python.
7. Menurunkan koreksi energi dan fungsi gelombang orde pertama teori perturbasi tak terdegenerasi.
8. Menghitung koreksi energi orde kedua dan menafsirkan "tolakan tingkat" dalam bahasa kimia.
9. Membandingkan hasil perturbasi dan variasi untuk helium, termasuk deret $1/Z$ ion mirip helium.
10. Menerapkan perturbasi tingkat terdegenerasi pada keadaan tereksitasi helium dan pada molekul bersimetri tinggi, serta menjelaskan integral pertukaran.
11. Menghitung efek Stark linear dan kuadratik, polarisabilitas, dan tetapan dispersi London.
12. Menurunkan amplitudo transisi teori perturbasi bergantung waktu, aturan seleksi dari momen dipol transisi, dan aturan emas Fermi.
:::

::: {.mat}
**Prasyarat**

Dari Bab 2: matriks, determinan, dan sistem persamaan homogen (subbab 2.7), nilai eigen dan vektor eigen matriks (subbab 2.8), deret Taylor (subbab 2.9), dan satuan atom (subbab 2.11). Dari Bab 3: partikel dalam kotak dan model elektron bebas (subbab 3.6–3.8). Dari Bab 4: operator Hermitian, ekspansi dalam fungsi eigen, dan notasi Dirac (subbab 4.8, 4.9, dan 4.14). Dari Bab 5: osilator harmonik, operator tangga, dan anharmonisitas (subbab 5.4, 5.6, dan 5.9). Dari Bab 6: harmonik bola dan rotor tegar (subbab 6.5 dan 6.9). Dari Bab 7: fungsi gelombang atom hidrogen dan atom mirip hidrogen (subbab 7.4–7.10). Sepanjang bab ini kita memakai **satuan atom**: panjang dalam bohr ($a_0 = 52{,}918$ pm) dan energi dalam hartree ($E_h = 27{,}211$ eV). Dari Bab 7: aturan seleksi atom hidrogen sebagai pratinjau (subbab 7.11).
:::

## 8.1 Mengapa perlu pendekatan

### Sedikit sekali masalah yang dapat diselesaikan eksak

Sejauh ini kita telah menyelesaikan persamaan Schrödinger secara eksak untuk segelintir sistem: partikel dalam kotak, osilator harmonik, rotor tegar, dan atom hidrogen beserta ion mirip hidrogen. Daftar itu dapat diperpanjang sedikit (potensial Morse, beberapa sumur dengan bentuk khusus), tetapi tidak banyak. Semua sistem itu mempunyai satu kesamaan: **Hamiltoniannya dapat dipisahkan** menjadi bagian-bagian yang masing-masing bergantung pada satu koordinat, sehingga persamaan diferensial parsial berubah menjadi beberapa persamaan diferensial biasa.

Begitu sistem mempunyai dua elektron, keadaan berubah total. Hamiltonian atom helium (inti dianggap diam) dalam satuan atom adalah

$$
\hat H = -\tfrac12\nabla_1^2 - \tfrac12\nabla_2^2 - \frac{Z}{r_1} - \frac{Z}{r_2} + \frac{1}{r_{12}} , \qquad Z = 2 . \qquad \text{(8.1)}
$$

Empat suku pertama adalah dua Hamiltonian ion mirip hidrogen, satu untuk tiap elektron. Seandainya hanya ada keempat suku itu, $\hat H = \hat h_1 + \hat h_2$, dan fungsi gelombangnya adalah hasil kali dua orbital mirip hidrogen (subbab 4.4). Suku terakhir, $1/r_{12} = 1/|\mathbf r_1 - \mathbf r_2|$, merusak pemisahan itu: ia bergantung pada koordinat kedua elektron sekaligus, dan tidak ada pilihan koordinat yang dapat menguraikannya. Dalam mekanika klasik, gerak tiga benda yang saling tarik (Matahari, Bumi, dan Bulan, atau inti dan dua elektron) juga tidak mempunyai penyelesaian umum dalam rumus tertutup; Poincaré membuktikannya di akhir abad ke-19. Mekanika kuantum tidak membebaskan kita dari kesulitan ini.

Padahal semua sistem yang menarik bagi kimiawan mempunyai banyak elektron. Molekul air mempunyai 10 elektron dan 3 inti; benzena 42 elektron dan 12 inti. Bila helium saja tidak dapat diselesaikan eksak, jelas bahwa kimia kuantum harus dibangun di atas **metode pendekatan**. Yang mengejutkan adalah betapa baiknya pendekatan itu dapat dibuat.

### Tiga jalan keluar

**Jalan pertama: hitung langsung pada kisi.** Di subbab 5.12 kita menyelesaikan persamaan Schrödinger satu dimensi secara numerik dengan metode Numerov. Mengapa tidak melakukan hal yang sama untuk helium? Masalahnya adalah jumlah dimensi. Fungsi gelombang helium bergantung pada enam koordinat. Kisi yang sangat kasar, 100 titik per koordinat, sudah memerlukan $100^6 = 10^{12}$ nilai. Untuk litium (sembilan koordinat) diperlukan $10^{18}$ nilai, dan untuk benzena $10^{252}$. Pertumbuhan eksponensial ini disebut **kutukan dimensi**, dan inilah alasan mengapa pendekatan "hitung semua titik" hanya dipakai untuk sistem dengan sangat sedikit derajat kebebasan.

**Jalan kedua: metode variasi.** Daripada mencari fungsi gelombang di setiap titik ruang, kita menebak *bentuknya*, misalnya hasil kali dua orbital 1s dengan eksponen yang dapat diatur, lalu memilih parameter yang memberikan energi terendah. Teorema variasi (subbab 8.2) menjamin bahwa energi yang diperoleh selalu batas atas energi sebenarnya. Bila tebakan berupa kombinasi linear fungsi-fungsi tetap, masalahnya menjadi masalah nilai eigen matriks (subbab 8.4 dan 8.5), dan inilah bentuk yang dipakai di hampir semua program kimia komputasi.

**Jalan ketiga: teori perturbasi.** Bila Hamiltonian dapat ditulis sebagai $\hat H = \hat H^{(0)} + \hat H'$, dengan $\hat H^{(0)}$ dapat diselesaikan eksak dan $\hat H'$ "kecil", maka energi dan fungsi gelombang dapat diuraikan dalam deret: suku orde nol dari $\hat H^{(0)}$, koreksi orde pertama yang sebanding dengan $\hat H'$, koreksi orde kedua yang sebanding dengan $\hat H'^2$, dan seterusnya (subbab 8.6 dan 8.7). Untuk helium, $\hat H^{(0)}$ adalah dua ion He⁺ dan $\hat H' = 1/r_{12}$.

Ketiga jalan ini saling melengkapi. Variasi memberi batas atas dan dapat diperbaiki secara sistematis dengan menambah parameter; perturbasi memberi rumus analitis yang memperlihatkan *mengapa* suatu efek terjadi dan bagaimana ia bergantung pada besaran fisika. Kimia komputasi modern memakai keduanya, sering dalam satu perhitungan.

### Kapan sebuah suku dapat dianggap kecil?

Teori perturbasi memerlukan $\hat H'$ yang "kecil", tetapi kecil dibandingkan dengan apa? Di subbab 8.6 kita akan melihat bahwa ukuran yang tepat adalah perbandingan unsur matriks perturbasi terhadap **selisih tingkat energi** sistem tanpa gangguan:

$$
\left|\frac{H'_{mn}}{E_n^{(0)} - E_m^{(0)}}\right| \ll 1 . \qquad \text{(8.2)}
$$

Banyak gangguan dalam kimia dan spektroskopi memenuhi syarat ini dengan sangat baik. Medan listrik dan magnet laboratorium, interaksi spin–orbit pada atom ringan, efek relativistik pada unsur periode 2, kopling hiperhalus, dan pergantian satu atom C oleh N dalam cincin aromatik semuanya kecil dibandingkan selisih tingkat elektronik. Tolakan antarelektron dalam helium *tidak* kecil, tetapi teori perturbasi tetap bekerja cukup baik karena koreksi-koreksinya mengecil dengan cepat (subbab 8.8).

### Hierarki energi dalam molekul

Molekul mempunyai energi pada skala yang sangat berbeda: energi elektronik orde eV, energi getaran orde 0,1 eV, energi rotasi orde 0,001 eV, struktur halus dan efek medan luar lebih kecil lagi, dan kopling hiperhalus orde $10^{-6}$ eV. Perbedaan skala ini adalah anugerah: setiap tingkat hierarki dapat diperlakukan sebagai perturbasi terhadap tingkat di atasnya. Pendekatan Born–Oppenheimer (Bab 11) memisahkan gerak elektron dari gerak inti; distorsi sentrifugal (subbab 6.12) adalah perturbasi getaran oleh rotasi; efek Zeeman dan Stark adalah perturbasi oleh medan luar. Seluruh spektroskopi molekul disusun menurut hierarki ini.

::: {.inti}
**Inti subbab 8.1**

- Hanya Hamiltonian yang dapat dipisahkan yang dapat diselesaikan eksak. Tolakan $1/r_{12}$ membuat setiap sistem berelektron banyak tidak terpisahkan.
- Perhitungan langsung pada kisi tumbuh eksponensial dengan jumlah elektron (kutukan dimensi).
- Metode variasi menebak bentuk fungsi gelombang dan meminimumkan energi; teori perturbasi menguraikan energi dalam deret koreksi terhadap masalah yang dapat diselesaikan.
- Perturbasi berlaku bila unsur matriks gangguan jauh lebih kecil daripada selisih tingkat energi.
:::

::: {.contoh}
**Contoh 8.1 · Seberapa besar tolakan antarelektron helium?**

Di subbab 4.4 kita menghitung bahwa helium tanpa tolakan antarelektron mempunyai energi $-Z^2 = -4\ E_h$. Nilai rata-rata tolakan $1/r_{12}$ untuk dua elektron 1s dengan $Z = 2$ ternyata $\tfrac54\ E_h$ (akan diturunkan di subbab 8.3). (a) Nyatakan kedua energi itu dalam eV. (b) Bandingkan dengan energi eksperimen $-79{,}0$ eV. (c) Apakah tolakan antarelektron dapat dianggap "kecil"?

**Penyelesaian.** (a) $-4\ E_h = -108{,}8$ eV; $\tfrac54\ E_h = 34{,}0$ eV.

(b) Tanpa tolakan, galatnya $-108{,}8 - (-79{,}0) = -29{,}8$ eV, atau 38%. Dengan menambahkan tolakan rata-rata, $-108{,}8 + 34{,}0 = -74{,}8$ eV, galatnya tinggal 4,2 eV (5,3%).

(c) Tolakan 34,0 eV adalah 31% dari energi orde nol. Ini jelas tidak kecil, tetapi menambahkan nilai rata-ratanya saja sudah memperbaiki galat dari 38% menjadi 5%.

**Memahami hasil.** Menambahkan nilai rata-rata gangguan, dihitung dengan fungsi gelombang tanpa gangguan, adalah persis koreksi perturbasi orde pertama (subbab 8.6). Bahwa langkah sesederhana itu sudah menghasilkan galat 5% memberi harapan: untuk molekul, di mana tolakan antarelektron jauh lebih rumit, gagasan "medan rata-rata" juga merupakan titik awal yang baik. Itulah dasar metode Hartree–Fock (subbab 9.8).
:::

::: {.contoh}
**Contoh 8.2 · Kutukan dimensi**

Sebuah komputer menyimpan setiap nilai fungsi gelombang sebagai bilangan 8 bita. Berapa memori yang diperlukan untuk menyimpan fungsi gelombang pada kisi 100 titik per koordinat (a) untuk satu elektron, (b) untuk helium, (c) untuk litium, (d) untuk benzena?

**Penyelesaian.** (a) Tiga koordinat: $10^6$ nilai, 8 MB. (b) Enam koordinat: $10^{12}$ nilai, $8 \times 10^{12}$ bita = 8 TB. (c) Sembilan koordinat: $10^{18}$ nilai, $8 \times 10^{18}$ bita, sekitar delapan juta terabita. (d) 42 elektron, 126 koordinat: $10^{252}$ nilai.

**Memahami hasil.** Satu elektron mudah, helium sudah memerlukan pusat data, dan litium mustahil. Bilangan $10^{252}$ jauh melampaui jumlah atom di alam semesta teramati (sekitar $10^{80}$). Fungsi gelombang molekul karena itu tidak pernah disimpan "titik demi titik", melainkan disusun dari bagian-bagian sederhana, yaitu orbital satu elektron yang masing-masing hanya memerlukan tiga koordinat. Pendekatan orbital ini, yang dirintis oleh metode variasi untuk helium di subbab 8.3, adalah alasan mengapa kimia kuantum dapat dikerjakan sama sekali.
:::

::: {.contoh}
**Contoh 8.3 · Medan laboratorium sebagai perturbasi kecil**

Medan listrik $1{,}0 \times 10^7$ V/m (100 kV/cm) sudah cukup kuat untuk menembus udara kering. Bandingkan medan itu dengan satuan atom medan listrik, $5{,}142 \times 10^{11}$ V/m (medan proton pada jarak $a_0$), dan bandingkan energi $ea_0F$ dengan selisih energi 1s–2p atom hidrogen, 10,20 eV.

**Penyelesaian.** $F/F_\text{au} = 1{,}0 \times 10^7/5{,}142 \times 10^{11} = 1{,}94 \times 10^{-5}$. Energi $ea_0F = (5{,}292 \times 10^{-11}\ \text{m})(1{,}0 \times 10^7\ \text{V/m}) = 5{,}29 \times 10^{-4}$ eV. Perbandingannya terhadap 10,20 eV adalah $5{,}2 \times 10^{-5}$.

**Memahami hasil.** Medan terkuat yang dapat dibuat di antara dua pelat di laboratorium hanya mengganggu atom pada orde seperseratus ribu. Syarat (8.2) terpenuhi dengan sangat baik, sehingga efek medan listrik pada atom dan molekul (efek Stark, subbab 8.10) dapat dihitung dengan teori perturbasi orde rendah. Situasinya berbeda untuk laser pulsa intens, yang medan puncaknya dapat mendekati $10^{11}$ V/m; di sana teori perturbasi runtuh dan muncul fenomena seperti ionisasi medan kuat.
:::

::: {.contoh}
**Contoh 8.4 · Ketelitian kimia**

Kimiawan sering menyebut galat 1 kkal/mol sebagai "ketelitian kimia", karena pada tingkat itu tetapan laju dan tetapan kesetimbangan dapat diramalkan dalam faktor beberapa kali. (a) Nyatakan 1 kkal/mol dalam hartree dan eV. (b) Energi total molekul air sekitar $-76{,}44\ E_h$. Berapa ketelitian relatif yang diperlukan?

**Penyelesaian.** (a) 1 kkal/mol $= 4{,}184$ kJ/mol. Dengan $1\ E_h = 2625{,}5$ kJ/mol, $4{,}184/2625{,}5 = 1{,}594 \times 10^{-3}\ E_h = 0{,}0434$ eV.

(b) $1{,}594 \times 10^{-3}/76{,}44 = 2{,}1 \times 10^{-5}$, sekitar dua bagian per seratus ribu.

**Memahami hasil.** Kimia ditentukan oleh *selisih* energi yang sangat kecil dibandingkan energi total. Untunglah galat metode pendekatan sebagian besar berasal dari elektron-elektron kulit dalam yang tidak berubah selama reaksi, sehingga galat itu sebagian besar saling menghapus ketika selisih energi dihitung. Pembatalan galat yang sistematis ini adalah salah satu rahasia keberhasilan kimia komputasi (Bab 17).
:::

::: {.kuis}
**Kuis cepat 8.1**

Ion molekul H₂⁺ hanya mempunyai satu elektron. Mengapa persamaan Schrödinger elektronnya (dengan inti diam) tetap tidak dapat diselesaikan dengan pemisahan koordinat bola seperti atom hidrogen? Dan mengapa medan magnet 1 T dapat diperlakukan sebagai perturbasi kecil terhadap atom (bandingkan $\mu_BB$ dengan 10 eV)?
:::

## 8.2 Teorema variasi

### Pernyataan teorema

Misalkan $\hat H$ adalah Hamiltonian sistem dengan energi keadaan dasar $E_1$ (energi terendah yang mungkin). Misalkan pula $\phi$ adalah sembarang fungsi yang berperilaku baik (kontinu, bernilai tunggal, kuadratnya dapat diintegralkan) dan memenuhi syarat batas sistem itu. Maka

$$
W \equiv \frac{\displaystyle\int\phi^*\hat H\phi\,d\tau}{\displaystyle\int\phi^*\phi\,d\tau} \ \ge\ E_1 . \qquad \text{(8.3)}
$$

Besaran $W$ disebut **integral variasi**, dan $\phi$ disebut **fungsi uji** (atau fungsi variasi). Bila $\phi$ sudah dinormalisasi, penyebutnya satu dan $W = \langle\phi|\hat H|\phi\rangle$. Kesamaan berlaku hanya bila $\phi$ adalah fungsi gelombang keadaan dasar yang sebenarnya.

Teorema ini mengatakan sesuatu yang luar biasa: kita boleh menebak fungsi gelombang sesuka hati, dan energi yang dihitung dari tebakan itu **tidak pernah** di bawah energi keadaan dasar sebenarnya. Tebakan buruk memberi energi yang terlalu tinggi; tebakan yang lebih baik memberi energi yang lebih rendah. Energi menjadi kompas yang menunjukkan arah perbaikan.

### Bukti

Fungsi eigen $\psi_k$ dari $\hat H$, dengan $\hat H\psi_k = E_k\psi_k$, membentuk himpunan ortonormal yang lengkap (subbab 4.9). Urutkan nilai eigennya: $E_1 \le E_2 \le E_3 \le \cdots$. Karena lengkap, sembarang fungsi uji dapat diuraikan:

$$
\phi = \sum_k a_k\psi_k , \qquad a_k = \langle\psi_k|\phi\rangle .
$$

Masukkan ke pembilang (8.3). Karena $\hat H$ linear dan $\hat H\psi_k = E_k\psi_k$,

$$
\langle\phi|\hat H|\phi\rangle = \sum_j\sum_ka_j^*a_k\langle\psi_j|\hat H|\psi_k\rangle = \sum_j\sum_ka_j^*a_kE_k\delta_{jk} = \sum_k|a_k|^2E_k .
$$

Dengan cara yang sama, penyebutnya $\langle\phi|\phi\rangle = \sum_k|a_k|^2$. Sekarang gunakan fakta bahwa setiap $E_k \ge E_1$ dan setiap $|a_k|^2 \ge 0$:

$$
\sum_k|a_k|^2E_k \ \ge\ \sum_k|a_k|^2E_1 = E_1\sum_k|a_k|^2 .
$$

Bagi kedua ruas dengan $\sum_k|a_k|^2 > 0$, maka $W \ge E_1$. Kesamaan terjadi hanya bila semua $a_k$ dengan $E_k > E_1$ nol, yaitu bila $\phi$ sebanding dengan $\psi_1$. $\blacksquare$

Bukti ini juga memberi tafsiran yang jelas: $W = \sum_k p_kE_k$ dengan $p_k = |a_k|^2/\sum_j|a_j|^2$ adalah **rata-rata berbobot** energi-energi eigen, dengan bobot berupa peluang menemukan sistem pada keadaan $k$ (postulat pengukuran, subbab 4.12). Rata-rata dari bilangan-bilangan yang semuanya $\ge E_1$ tidak mungkin lebih kecil daripada $E_1$.

::: {.inti}
**Teorema variasi**

Untuk sembarang fungsi uji $\phi$ yang berperilaku baik dan memenuhi syarat batas,

$$
W = \frac{\langle\phi|\hat H|\phi\rangle}{\langle\phi|\phi\rangle} \ \ge\ E_1 .
$$

$W$ adalah rata-rata berbobot energi-energi eigen. Makin rendah $W$, makin baik fungsi ujinya, dan $W = E_1$ hanya bila $\phi = \psi_1$.
:::

### Strategi: parameter variasi

Dalam praktik, fungsi uji diberi satu atau beberapa **parameter variasi** $\alpha, \beta, \ldots$, sehingga $W$ menjadi fungsi parameter-parameter itu. Karena setiap nilai $W$ adalah batas atas, nilai terbaik adalah yang **terendah**, dan diperoleh dari syarat minimum:

$$
\frac{\partial W}{\partial\alpha} = 0, \qquad \frac{\partial W}{\partial\beta} = 0, \qquad \ldots \qquad \text{(8.4)}
$$

Langkah-langkahnya selalu sama: (1) pilih bentuk fungsi uji berdasarkan pengetahuan fisika (simetri, perilaku di dekat inti dan di jauh tak hingga, jumlah simpul); (2) hitung $W$ sebagai fungsi parameter; (3) cari minimumnya; (4) periksa hasilnya, misalnya dengan teorema virial atau dengan membandingkan sifat lain.

::: {.awas}
**Fungsi uji harus memenuhi syarat batas**

Teorema variasi hanya berlaku bila $\phi$ berada dalam "ruang" fungsi yang sama dengan fungsi eigen $\hat H$. Untuk partikel dalam kotak, misalnya, $\phi$ harus nol di kedua dinding. Fungsi tetap $\phi = 1$ di dalam kotak memberi $\langle\phi|\hat T|\phi\rangle = 0$, jauh di bawah $E_1$! Kontradiksi ini hanya tampak: fungsi yang tidak nol di dinding melompat ke nol di luar kotak, dan lompatan itu mempunyai energi kinetik tak hingga yang tidak ikut terhitung bila integral hanya diambil di dalam kotak. Selalu periksa syarat batas sebelum mempercayai batas atas.
:::

### Galat energi adalah orde kedua

Teorema variasi mempunyai satu sifat lagi yang membuatnya sangat berguna. Misalkan fungsi uji berbeda sedikit dari fungsi sebenarnya: $\phi = \psi_1 + \varepsilon\chi$, dengan $\chi$ ternormalisasi, ortogonal pada $\psi_1$, dan $\varepsilon$ kecil. Maka

$$
W = \frac{E_1 + \varepsilon^2\langle\chi|\hat H|\chi\rangle}{1 + \varepsilon^2} , \qquad W - E_1 = \frac{\varepsilon^2\left(\langle\chi|\hat H|\chi\rangle - E_1\right)}{1 + \varepsilon^2} . \qquad \text{(8.5)}
$$

Suku-suku yang linear dalam $\varepsilon$ hilang karena $\langle\psi_1|\hat H|\chi\rangle = E_1\langle\psi_1|\chi\rangle = 0$. Galat fungsi gelombang sebesar $\varepsilon$ hanya menghasilkan galat energi sebesar $\varepsilon^2$. Akibatnya ada dua: fungsi uji yang "lumayan" sudah memberi energi yang "baik", tetapi sifat lain selain energi (momen dipol, kerapatan elektron di inti) yang galatnya orde pertama dalam $\varepsilon$ biasanya **jauh kurang teliti** daripada energinya.

### Batas atas untuk keadaan tereksitasi

Bukti di atas dapat diperluas. Bila fungsi uji **ortogonal** terhadap fungsi keadaan dasar, $a_1 = \langle\psi_1|\phi\rangle = 0$, maka suku $k = 1$ tidak ada dalam jumlah, dan rata-rata berbobot menjadi rata-rata dari $E_2, E_3, \ldots$:

$$
\langle\psi_1|\phi\rangle = 0 \quad\Longrightarrow\quad W \ge E_2 . \qquad \text{(8.6)}
$$

Secara umum, fungsi uji yang ortogonal terhadap $k - 1$ keadaan terendah memberi batas atas untuk $E_k$. Kesulitannya, kita biasanya tidak mengetahui $\psi_1$ yang tepat, sehingga ortogonalitas tidak dapat dijamin. Ada satu jalan keluar yang sangat berguna: **simetri**. Fungsi-fungsi yang termasuk jenis simetri berbeda (misalnya genap dan ganjil terhadap pencerminan, atau momentum sudut berbeda) otomatis ortogonal, apa pun bentuk persisnya. Karena itu, metode variasi selalu memberi batas atas untuk keadaan **terendah dari setiap jenis simetri**. Contohnya: keadaan triplet terendah helium, keadaan $\ell = 1$ terendah atom apa pun, atau keadaan tereksitasi terendah molekul yang simetrinya berbeda dari keadaan dasarnya dapat dihitung secara variasi tanpa takut "runtuh" ke keadaan dasar.

### Penskalaan dan teorema virial

Untuk sistem yang hanya mengandung gaya Coulomb, ada cara cepat mengoptimumkan satu parameter penting: ukuran. Ambil sembarang fungsi uji $\phi(\mathbf r)$ dan ganti setiap koordinat dengan $\zeta\mathbf r$, dengan $\zeta$ **faktor skala**. Energi kinetik mengandung dua turunan terhadap koordinat, sehingga berskala $\zeta^2$; energi potensial Coulomb sebanding dengan $1/r$, sehingga berskala $\zeta$. Bila $T_1$ dan $V_1$ adalah nilai rata-rata untuk $\zeta = 1$, maka

$$
W(\zeta) = \zeta^2T_1 + \zeta V_1 . \qquad \text{(8.7)}
$$

Minimumnya terletak di $dW/d\zeta = 2\zeta T_1 + V_1 = 0$, yaitu $\zeta_\text{opt} = -V_1/2T_1$, dan di sana

$$
\langle T\rangle = \zeta_\text{opt}^2T_1 = -\tfrac12\zeta_\text{opt}V_1 = -\tfrac12\langle V\rangle , \qquad W_\text{min} = -\frac{V_1^2}{4T_1} = -\langle T\rangle . \qquad \text{(8.8)}
$$

Inilah **teorema virial** untuk sistem Coulomb (subbab 7.9), yang ternyata berlaku bukan hanya untuk fungsi eigen eksak, tetapi juga untuk setiap fungsi uji yang ukurannya telah dioptimumkan. Fungsi uji yang gagal memenuhi $\langle V\rangle/\langle T\rangle = -2$ pasti belum optimum, dan perbandingan ini menjadi alat pemeriksa yang murah dalam kimia komputasi.

::: {.contoh}
**Contoh 8.5 · Atom hidrogen dengan fungsi uji Gauss**

Seandainya kita tidak tahu bahwa keadaan dasar hidrogen berbentuk $e^{-r}$, kita mungkin mencoba fungsi Gauss $\phi = (2\alpha/\pi)^{3/4}e^{-\alpha r^2}$ (sudah ternormalisasi). Hitung energi terbaiknya, lalu bandingkan dengan nilai eksak $-\tfrac12\ E_h$.

**Penyelesaian.** Laplasian fungsi berbentuk bola adalah $\nabla^2f = r^{-2}d(r^2df/dr)/dr$. Untuk $f = e^{-\alpha r^2}$: $df/dr = -2\alpha re^{-\alpha r^2}$, dan $\nabla^2f = (4\alpha^2r^2 - 6\alpha)e^{-\alpha r^2}$. Jadi

$$
\langle T\rangle = -\tfrac12\langle\nabla^2\rangle = 3\alpha - 2\alpha^2\langle r^2\rangle .
$$

Dengan integral Gauss (subbab 2.2), $\langle r^2\rangle = 3/4\alpha$, sehingga $\langle T\rangle = 3\alpha - \tfrac32\alpha = \tfrac32\alpha$. Energi potensialnya

$$
\langle V\rangle = -\left(\frac{2\alpha}{\pi}\right)^{3/2}\int_0^\infty\frac1r\,e^{-2\alpha r^2}\,4\pi r^2\,dr = -4\pi\left(\frac{2\alpha}{\pi}\right)^{3/2}\frac{1}{4\alpha} = -2\sqrt{\frac{2\alpha}{\pi}} .
$$

Jadi $W(\alpha) = \tfrac32\alpha - 2\sqrt{2\alpha/\pi}$. Syarat $dW/d\alpha = \tfrac32 - \sqrt{2/\pi\alpha} = 0$ memberi $\alpha = 8/9\pi = 0{,}2829$, dan

$$
W_\text{min} = \frac{4}{3\pi} - \frac{8}{3\pi} = -\frac{4}{3\pi} = -0{,}4244\ E_h = -11{,}55\ \text{eV} .
$$

Galatnya $0{,}0756\ E_h$, atau 15,1%. Periksa virial: $\langle T\rangle = 0{,}4244$ dan $\langle V\rangle = -0{,}8488$, perbandingannya tepat $-2$.

**Memahami hasil.** Fungsi Gauss memberi batas atas, sesuai teorema, tetapi galatnya besar. Penyebabnya terlihat di dua tempat: di inti, fungsi eksak mempunyai "puncak lancip" (*cusp*, turunannya tidak nol di $r = 0$) sedangkan Gauss datar; di jauh, $e^{-\alpha r^2}$ meluruh terlalu cepat dibandingkan $e^{-r}$. Yang mengejutkan, jarak rata-rata $\langle r\rangle = 2/\sqrt{2\pi\alpha} = 1{,}500\ a_0$ tepat sama dengan nilai eksak, sedangkan kerapatan di inti $|\phi(0)|^2 = 0{,}0764$ hanya seperempat nilai eksak $1/\pi = 0{,}318$. Pelajaran ini penting: fungsi Gauss dipakai luas dalam kimia komputasi karena integralnya mudah (subbab 8.5 dan Bab 17), tetapi sifat-sifat yang peka terhadap daerah inti, seperti kopling hiperhalus ESR dan geseran kimia NMR, memerlukan banyak fungsi Gauss yang sangat sempit.
:::

::: {.contoh}
**Contoh 8.6 · Fungsi uji yang buruk untuk osilator harmonik**

Untuk osilator harmonik ($\hbar = m = \omega = 1$, $\hat H = -\tfrac12d^2/dx^2 + \tfrac12x^2$), coba fungsi uji $\phi = \sqrt a\,e^{-a|x|}$. Hitung energi terbaiknya dan bandingkan dengan energi eksak $\tfrac12$.

**Penyelesaian.** Fungsi ini mempunyai "patahan" di $x = 0$. Agar tidak perlu menurunkan dua kali di titik patah, pakai bentuk energi kinetik yang setara (integral parsial): $\langle T\rangle = \tfrac12\int|\phi'|^2dx$. Karena $|\phi'| = a|\phi|$ di mana-mana, $\langle T\rangle = \tfrac12a^2$. Energi potensial: $\langle x^2\rangle = 2a\int_0^\infty x^2e^{-2ax}dx = 2a\cdot\dfrac{2}{(2a)^3} = \dfrac{1}{2a^2}$, sehingga $\langle V\rangle = 1/4a^2$. Jadi $W = \tfrac12a^2 + 1/4a^2$. Minimum: $a - 1/2a^3 = 0$, $a^4 = \tfrac12$, dan

$$
W_\text{min} = \frac{1}{2\sqrt2} + \frac{\sqrt2}{4} = \frac{\sqrt2}{2} = 0{,}707 .
$$

**Memahami hasil.** Batas atas 0,707 terlalu tinggi 41%. Fungsi eksponensial berpatahan sama sekali tidak mirip Gauss eksak: lancip di tengah dan berekor terlalu panjang. Sebaliknya, bila kita memakai keluarga Gauss $e^{-\alpha x^2}$, minimumnya jatuh tepat di $\alpha = \tfrac12$ dengan $W = \tfrac12$, karena fungsi eksak termasuk dalam keluarga itu. Mutu hasil variasi sepenuhnya ditentukan oleh seberapa "lentur" keluarga fungsi uji dan seberapa dekat ia dengan fungsi sebenarnya. Bandingkan dengan Contoh 8.5: di sana Gauss adalah tebakan yang buruk untuk sistem yang fungsinya eksponensial; di sini eksponensial adalah tebakan yang buruk untuk sistem yang fungsinya Gauss.
:::

::: {.contoh}
**Contoh 8.7 · Osilator kuartik dan getaran pengerutan cincin**

Beberapa molekul siklik beranggota empat, misalnya oksetana dan siklobutanon, mempunyai getaran "pengerutan cincin" (*ring puckering*) dengan potensial yang hampir murni kuartik, $V \propto x^4$, karena bentuk datar dan bentuk berkerut hampir sama energinya. Persamaan Schrödinger untuk $V = x^4$ tidak dapat diselesaikan eksak. Dengan $\hbar = m = 1$, $\hat H = -\tfrac12d^2/dx^2 + x^4$, gunakan fungsi uji $e^{-\alpha x^2}$ untuk memperkirakan energi keadaan dasar. Nilai numerik eksaknya 0,6680.

**Penyelesaian.** Untuk Gauss ternormalisasi $(2\alpha/\pi)^{1/4}e^{-\alpha x^2}$: $\langle T\rangle = \alpha/2$, $\langle x^2\rangle = 1/4\alpha$, dan $\langle x^4\rangle = 3\langle x^2\rangle^2 = 3/16\alpha^2$. Jadi

$$
W(\alpha) = \frac{\alpha}{2} + \frac{3}{16\alpha^2} , \qquad \frac{dW}{d\alpha} = \frac12 - \frac{3}{8\alpha^3} = 0 \quad\Rightarrow\quad \alpha = \left(\tfrac34\right)^{1/3} = 0{,}9086 .
$$

Di minimum, $3/16\alpha^2 = \alpha/4$, sehingga $W = \tfrac34\alpha = 0{,}6814$. Galatnya $0{,}0134$, atau 2,0%.

**Memahami hasil.** Satu parameter Gauss sudah memberi galat hanya 2%, karena keadaan dasar kuartik memang menyerupai Gauss (simetris, tanpa simpul, meluruh cepat). Di minimum, $\langle T\rangle = \alpha/2 = 2\langle V\rangle$: teorema virial untuk potensial $x^4$ adalah $2\langle T\rangle = 4\langle V\rangle$, dan penskalaan memenuhinya otomatis. Spektroskopi inframerah jauh dan gelombang mikro mengukur tingkat-tingkat getaran pengerutan cincin, dan dari jaraknya yang tidak sama, kimiawan menyimpulkan apakah cincin itu datar atau berkerut serta berapa tinggi penghalang di antara dua bentuk berkerut.
:::

::: {.contoh}
**Contoh 8.8 · Keluarga fungsi uji untuk partikel dalam kotak**

Di Contoh 3.14 kita menghitung bahwa fungsi parabola $x(L - x)$ memberi energi rata-rata $1{,}0132E_1$. Perumum menjadi keluarga $\phi_p = [x(L - x)]^p$ dengan $p > \tfrac12$. Dengan menghitung $W(p)$ secara numerik, tentukan $p$ terbaik dan energinya.

**Penyelesaian.** Dengan $\hbar = m = L = 1$, $W(p) = \tfrac12\int_0^1(\phi_p')^2dx\big/\int_0^1\phi_p^2dx$. Integrasi numerik memberi:

| $p$ | 0,75 | 0,90 | 1,00 | 1,112 | 1,20 |
|---|---|---|---|---|---|
| $W/E_1$ | 1,2159 | 1,0487 | 1,0132 | 1,0030 | 1,0074 |

Minimumnya di $p = 1{,}112$ dengan $W = 1{,}0030E_1$, galat 0,30%.

**Memahami hasil.** Parabola ($p = 1$) bukan anggota terbaik keluarganya; sedikit "menggembungkan" fungsi di tengah dengan $p$ sedikit di atas 1 menurunkan galat empat kali lipat. Perhatikan pula bahwa semua nilai $W$ di tabel di atas $E_1$, sesuai teorema. Syarat $p > \tfrac12$ diperlukan agar $\phi_p'$ dapat dikuadratkan dan diintegralkan; untuk $p \le \tfrac12$, kemiringan di dinding tak hingga dan energi kinetiknya tak hingga.
:::

::: {.contoh}
**Contoh 8.9 · Batas atas keadaan tereksitasi pertama kotak**

Fungsi $\phi = x(L - x)(L - 2x)$ ganjil terhadap titik tengah kotak. (a) Mengapa fungsi ini pasti ortogonal terhadap keadaan dasar? (b) Hitung $W$ dan bandingkan dengan $E_2 = 4E_1$.

**Penyelesaian.** (a) Terhadap titik tengah, $\psi_1$ genap dan $\phi$ ganjil; hasil kalinya ganjil sehingga integralnya nol (subbab 4.11). Menurut (8.6), $W \ge E_2$.

(b) Dengan $L = 1$: $\phi = x - 3x^2 + 2x^3$ dan $\phi' = 1 - 6x + 6x^2$. Integral elementer memberi $\int_0^1\phi^2dx = 1/210$ dan $\int_0^1\phi'^2dx = 1/5$. Jadi $W = \tfrac12(1/5)(210) = 21\ \hbar^2/mL^2$. Karena $E_1 = \pi^2\hbar^2/2mL^2 = 4{,}935\ \hbar^2/mL^2$, $W = 4{,}255E_1 = 1{,}064E_2$.

**Memahami hasil.** Batas atas untuk $E_2$ terlalu tinggi 6,4%, sedikit lebih buruk daripada parabola untuk $E_1$, karena polinom pangkat tiga dengan satu simpul belum menyerupai $\sin(2\pi x/L)$ sebaik parabola menyerupai $\sin(\pi x/L)$. Yang penting adalah prinsipnya: simetri menjamin ortogonalitas tanpa kita perlu mengetahui $\psi_1$. Dalam atom dan molekul, peran "genap dan ganjil" ini dimainkan oleh momentum sudut, spin, dan unsur-unsur simetri molekul (Bab 10).
:::

::: {.contoh}
**Contoh 8.10 · Penskalaan fungsi 1s untuk ion mirip hidrogen**

Untuk ion mirip hidrogen bermuatan inti $Z$, gunakan fungsi uji $\phi = (\zeta^3/\pi)^{1/2}e^{-\zeta r}$. (a) Tulis $W(\zeta)$ dengan rumus penskalaan (8.7). (b) Tentukan $\zeta$ optimum dan $W$. (c) Periksa teorema virial.

**Penyelesaian.** (a) Untuk $\zeta = 1$, fungsi 1s hidrogen mempunyai $T_1 = \tfrac12$ dan $\langle 1/r\rangle = 1$, sehingga untuk muatan inti $Z$: $V_1 = -Z$. Jadi $W(\zeta) = \tfrac12\zeta^2 - Z\zeta$.

(b) $dW/d\zeta = \zeta - Z = 0$ memberi $\zeta = Z$ dan $W = -\tfrac12Z^2$, tepat energi eksak.

(c) $\langle T\rangle = \tfrac12Z^2$ dan $\langle V\rangle = -Z^2$: perbandingannya $-2$.

**Memahami hasil.** Karena fungsi eksak termasuk dalam keluarga uji, metode variasi menemukannya kembali. Parameter $\zeta$ disebut **eksponen orbital** atau **muatan inti efektif**, karena fungsi $e^{-\zeta r}$ adalah orbital 1s yang "dirasakan" seolah-olah intinya bermuatan $\zeta$. Di subbab berikut, parameter yang sama memperoleh makna kimia yang mendalam: dalam helium, setiap elektron melindungi elektron lain dari sebagian muatan inti, dan nilai optimum $\zeta$ menjadi lebih kecil daripada $Z$.
:::

::: {.terapan}
**Batas atas dalam kimia komputasi**

Energi yang dilaporkan oleh perhitungan Hartree–Fock atau interaksi konfigurasi selalu merupakan batas atas, karena keduanya adalah metode variasi. Ini memberi pedoman praktis yang sangat berguna: bila himpunan basis diperbesar (lebih banyak fungsi, lebih banyak parameter), energi tidak boleh naik. Bila ternyata naik, ada kesalahan dalam masukan atau dalam program. Sebaliknya, metode perturbasi seperti MP2 dan metode fungsional kerapatan tidak bersifat variasi dalam arti ini, sehingga energinya dapat jatuh di bawah energi eksak. Ini bukan cacat, tetapi berarti bahwa "lebih rendah" tidak otomatis "lebih baik" untuk metode-metode itu (Bab 17).
:::

::: {.kuis}
**Kuis cepat 8.2**

(a) Seorang mahasiswa menghitung energi keadaan dasar atom hidrogen dengan fungsi uji tertentu dan memperoleh $-0{,}52\ E_h$. Apa kesimpulanmu? (b) Fungsi uji $xe^{-\alpha x^2}$ untuk osilator harmonik memberi batas atas untuk keadaan mana, dan mengapa? (c) Di titik optimum suatu fungsi uji untuk atom, $\langle T\rangle = 0{,}40\ E_h$ dan $\langle V\rangle = -0{,}84\ E_h$. Apakah ukurannya sudah optimum?
:::

