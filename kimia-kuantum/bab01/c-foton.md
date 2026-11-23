## 1.4 Efek fotolistrik dan foton

Planck sendiri menganggap kuantisasi sebagai sifat osilator dalam dinding rongga, bukan sifat cahaya. Cahaya, bagi Planck dan hampir semua fisikawan tahun 1900, tetap gelombang Maxwell yang malar. Langkah berikutnya, yang jauh lebih radikal, diambil Einstein pada tahun 1905 untuk menjelaskan efek fotolistrik.

### Pengamatan

Heinrich Hertz (1887) memperhatikan bahwa percikan listrik lebih mudah melompat antara dua elektrode jika elektrode disinari ultraviolet. Philipp Lenard (1902) menyelidikinya dengan tabung hampa: cahaya dijatuhkan pada pelat logam (katode), elektron yang terlepas (**fotoelektron**) dikumpulkan pada elektrode lain (anode), dan energi kinetiknya diukur dengan memberi anode potensial negatif yang menolak elektron. Potensial terkecil yang menghentikan elektron tercepat disebut **potensial henti** $V_0$, dan $eV_0 = K_\text{maks}$. Hasilnya:

1. **Ada frekuensi ambang** $\nu_0$ yang khas untuk setiap logam. Di bawah $\nu_0$ tidak ada elektron yang keluar, seterang apa pun cahayanya.
2. **Energi kinetik maksimum fotoelektron bertambah secara linear dengan frekuensi** dan **tidak bergantung pada intensitas** cahaya.
3. **Intensitas hanya menentukan banyaknya** fotoelektron (arus), bukan energinya.
4. **Tidak ada jeda waktu.** Elektron keluar kurang dari $10^{-9}$ s sesudah cahaya dinyalakan, bahkan pada cahaya yang sangat redup.

Teori gelombang klasik meramalkan sebaliknya untuk keempatnya. Energi gelombang sebanding dengan kuadrat amplitudonya, jadi cahaya yang lebih terang seharusnya melepaskan elektron yang lebih cepat; warna seharusnya tidak penting; dan cahaya redup memerlukan waktu untuk "mengisi" elektron sampai cukup energinya untuk lepas.

::: {.contoh}
**Contoh 1.16 · Jeda waktu menurut teori gelombang**

Cahaya ultraviolet berintensitas $1{,}0 \times 10^{-2}$ W/m² jatuh pada permukaan natrium. Fungsi kerja natrium 2,75 eV. Anggap energi gelombang diserap merata oleh setiap atom permukaan yang luas penampangnya $\pi(0{,}10\ \text{nm})^2$. Berapa lama sebuah elektron harus menunggu untuk mengumpulkan energi yang cukup?

**Penyelesaian.** Luas penampang $A = \pi(1{,}0 \times 10^{-10}\ \text{m})^2 = 3{,}1 \times 10^{-20}$ m². Daya yang diterima satu atom $P = IA = 3{,}1 \times 10^{-22}$ W. Energi yang diperlukan $2{,}75 \times 1{,}602 \times 10^{-19} = 4{,}41 \times 10^{-19}$ J. Waktunya

$$
t = \frac{4{,}41 \times 10^{-19}\ \text{J}}{3{,}1 \times 10^{-22}\ \text{W}} = 1{,}4 \times 10^{3}\ \text{s} \approx 23\ \text{menit}.
$$

**Memahami hasil.** Percobaan menunjukkan elektron pertama keluar dalam waktu kurang dari satu nanodetik. Selisih dua belas orde besaran ini tidak dapat diperbaiki dengan menebak luas penampang yang lebih besar. Energi cahaya tidak tersebar merata; ia datang dalam paket yang masing-masing cukup untuk satu elektron.
:::

### Hipotesis foton Einstein

Einstein mengusulkan bahwa cahaya berfrekuensi $\nu$ terdiri atas kuanta energi, kini disebut **foton**, yang masing-masing berenergi

$$
E = h\nu = \frac{hc}{\lambda} . \qquad \text{(1.15)}
$$

Dalam efek fotolistrik, satu foton diserap seluruhnya oleh satu elektron. Elektron memerlukan sedikitnya energi $\phi$, **fungsi kerja** logam, untuk lepas dari permukaan. Sisa energinya menjadi energi kinetik. Elektron yang paling lemah terikat keluar dengan energi kinetik terbesar:

$$
\boxed{\ K_\text{maks} = h\nu - \phi = eV_0\ } \qquad \text{(1.16)}
$$

Keempat pengamatan langsung terjelaskan. Ambang $h\nu_0 = \phi$ ada karena satu foton harus cukup untuk satu elektron; foton tidak dapat "menabung" energi bersama-sama. $K_\text{maks}$ linear terhadap $\nu$ dengan kemiringan $h$ yang sama untuk semua logam. Intensitas menyatakan banyaknya foton, jadi hanya menentukan banyaknya elektron. Dan tidak ada jeda, karena energi tiap foton diserahkan sekaligus.

![Gambar 1.5 Kiri: energi kinetik maksimum fotoelektron terhadap frekuensi untuk tiga logam. Garis-garisnya sejajar dengan kemiringan $h$; perpotongannya dengan sumbu tegak memberikan $-\phi$. Kanan: spektrum fotoelektron N₂ yang disinari foton He I 21,22 eV. Setiap pita bersesuaian dengan pelepasan elektron dari satu orbital molekul; label menunjukkan energi ionisasinya.](fig/c_fotolistrik.png){width=94%}

Ramalan Einstein bahwa kemiringan $V_0$ terhadap $\nu$ adalah $h/e$ diuji dengan teliti oleh Robert Millikan (1916). Millikan sebenarnya berharap membuktikan Einstein salah. Setelah sepuluh tahun percobaan dengan permukaan logam alkali yang disiapkan dalam hampa, ia memperoleh $h$ yang cocok dengan nilai Planck dalam ketelitian sekitar 1%. Einstein menerima Hadiah Nobel 1921 atas penjelasan efek fotolistrik, bukan atas relativitas.

| Logam | Cs | K | Na | Ag | Zn | Cu | Pt |
|---|---|---|---|---|---|---|---|
| $\phi$ (eV) | 2,14 | 2,30 | 2,75 | 4,26 | 4,33 | 4,65 | 5,65 |
| $\lambda_0 = hc/\phi$ (nm) | 579 | 539 | 451 | 291 | 286 | 267 | 219 |

Fungsi kerja logam alkali kecil karena elektron valensinya lemah terikat; itulah sebabnya fotokatode dibuat dari campuran cesium dan antimon. Tetapi perhatikan: fungsi kerja natrium (2,75 eV) jauh lebih kecil daripada energi ionisasi atom natrium dalam fase gas (5,14 eV). Dalam logam, elektron valensi tidak terikat pada satu atom; ia mengisi pita energi yang dibentuk oleh semua atom, dan elektron di puncak pita lebih mudah dikeluarkan. Kita akan memahami pita energi di Bab 13.

### Foton sebagai partikel

Foton adalah partikel tanpa massa diam yang selalu bergerak dengan laju $c$. Dari relativitas, energi dan momentum partikel tak bermassa berhubungan menurut $E = pc$. Jadi foton membawa momentum

$$
p = \frac{E}{c} = \frac{h}{\lambda} . \qquad \text{(1.17)}
$$

Momentum foton cahaya tampak sangat kecil (sekitar $10^{-27}$ kg·m/s), tetapi cukup untuk mendorong atom (subbab 1.5) dan membuat "pinset optik" yang mampu memegang satu sel bakteri.

::: {.contoh}
**Contoh 1.17 · Laser hijau dan laser ungu pada natrium**

\(a) Berapa panjang gelombang ambang natrium? (b) Apakah laser hijau 532 nm dapat melepaskan elektron dari natrium? (c) Berapa energi kinetik maksimum dan kelajuan fotoelektron yang dilepaskan laser ungu 405 nm?

**Penyelesaian.** (a) $\lambda_0 = hc/\phi = (1239{,}8\ \text{eV·nm})/(2{,}75\ \text{eV}) = 451$ nm.

\(b) Energi foton 532 nm adalah $1239{,}8/532 = 2{,}33$ eV, lebih kecil dari 2,75 eV. Tidak ada fotoelektron, seberapa pun daya lasernya.

\(c) $E = 1239{,}8/405 = 3{,}06$ eV, sehingga $K_\text{maks} = 3{,}06 - 2{,}75 = 0{,}31$ eV. Kelajuannya

$$
v = \sqrt{\frac{2K}{m_e}} = \sqrt{\frac{2(0{,}311)(1{,}602 \times 10^{-19})}{9{,}109 \times 10^{-31}}} = 3{,}3 \times 10^5\ \text{m/s}.
$$

**Memahami hasil.** Laser hijau berdaya 1 W pun tidak melepaskan satu elektron pun, sedangkan pointer ungu yang dayanya seperseribu itu langsung melakukannya. Bentuk $hc = 1239{,}8$ eV·nm sangat praktis: energi foton dalam eV sama dengan 1239,8 dibagi panjang gelombang dalam nm.
:::

::: {.contoh}
**Contoh 1.18 · Mengukur h dengan garis-garis raksa**

Seperti Millikan, kita menyinari fotokatode dengan garis-garis spektrum lampu raksa dan mengukur potensial henti:

| $\lambda$ (nm) | 546,1 | 435,8 | 404,7 | 365,0 | 313,2 |
|---|---|---|---|---|---|
| $\nu$ ($10^{14}$ Hz) | 5,49 | 6,88 | 7,41 | 8,21 | 9,57 |
| $V_0$ (V) | 0,14 | 0,68 | 0,93 | 1,25 | 1,84 |

Tentukan $h$, fungsi kerja, dan panjang gelombang ambang katode.

**Rencana.** Menurut (1.16), $V_0 = (h/e)\nu - \phi/e$. Grafik $V_0$ terhadap $\nu$ adalah garis lurus; kemiringannya $h/e$ dan perpotongannya $-\phi/e$. Cocokkan garis dengan kuadrat terkecil.

**Penyelesaian.** Regresi linear memberikan kemiringan $0{,}4177$ V per $10^{14}$ Hz dan perpotongan $-2{,}170$ V. Jadi

$$
h = e \times \text{kemiringan} = (1{,}602 \times 10^{-19})(4{,}177 \times 10^{-15}) = 6{,}69 \times 10^{-34}\ \text{J·s},
$$

$\phi = 2{,}17$ eV, dan $\nu_0 = 2{,}170/0{,}4177 \times 10^{14} = 5{,}19 \times 10^{14}$ Hz, atau $\lambda_0 = c/\nu_0 = 577$ nm.

**Memahami hasil.** Nilai $h$ meleset 1% dari nilai sebenarnya, ketelitian yang wajar untuk percobaan mahasiswa. Fungsi kerja 2,17 eV menunjukkan katode cesium. Perhatikan bahwa yang ditentukan dengan baik adalah kemiringan; perpotongan peka terhadap keadaan permukaan logam, kontaminasi, dan beda potensial kontak antara katode dan anode.
:::

### Foton dalam fotokimia

Bagi kimia, makna terpenting hipotesis foton adalah ini: **cahaya bereaksi dengan molekul satu foton demi satu foton**. Hukum ekuivalensi fotokimia (Stark–Einstein) menyatakan bahwa dalam tahap primer reaksi fotokimia, setiap foton yang diserap mengaktifkan satu molekul. Karena itu energi yang relevan adalah energi **satu mol foton**,

$$
E_\text{mol} = N_A\frac{hc}{\lambda} = \frac{1{,}196 \times 10^5\ \text{kJ/mol}}{\lambda/\text{nm}} . \qquad \text{(1.18)}
$$

Satu mol foton kadang disebut satu **einstein**. Bandingkan nilai (1.18) dengan energi ikatan: foton merah 700 nm membawa 171 kJ/mol, cahaya ungu 400 nm membawa 299 kJ/mol, ultraviolet 254 nm (lampu raksa) membawa 471 kJ/mol. Energi ikatan kovalen tunggal berkisar 150–450 kJ/mol. Inilah sebabnya cahaya tampak dan ultraviolet memicu reaksi kimia, sedangkan inframerah dan gelombang mikro hanya memanaskan.

Efisiensi reaksi fotokimia dinyatakan dengan **hasil kuantum**

$$
\Phi = \frac{\text{banyaknya molekul yang bereaksi}}{\text{banyaknya foton yang diserap}} . \qquad \text{(1.19)}
$$

$\Phi$ kurang dari 1 jika molekul yang tereksitasi kehilangan energinya dengan cara lain (fluoresensi, tumbukan). $\Phi$ dapat jauh lebih besar dari 1 jika foton memicu reaksi berantai; campuran H₂ dan Cl₂ yang disinari dapat mencapai $\Phi \approx 10^5$–$10^6$.

::: {.contoh}
**Contoh 1.19 · Menghitung foton dari laser**

Laser He–Ne 1,00 mW memancarkan cahaya 633 nm. (a) Berapa energi satu foton? (b) Berapa foton dipancarkan tiap detik? (c) Berapa mol foton tiap detik?

**Penyelesaian.** (a) $E = hc/\lambda = (6{,}626 \times 10^{-34})(2{,}998 \times 10^8)/(633 \times 10^{-9}) = 3{,}14 \times 10^{-19}$ J (1,96 eV).

\(b) $N/t = P/E = (1{,}00 \times 10^{-3})/(3{,}14 \times 10^{-19}) = 3{,}19 \times 10^{15}$ foton/s.

\(c) $3{,}19 \times 10^{15}/(6{,}022 \times 10^{23}) = 5{,}29 \times 10^{-9}$ mol/s.

**Memahami hasil.** Tiga ribu triliun foton tiap detik: berkas laser biasa sama sekali tidak tampak "berbutir". Sifat kuantum cahaya baru tampak pada cahaya yang sangat redup atau pada peristiwa satu molekul. Dalam satuan mol, laser 1 mW memerlukan sekitar enam tahun untuk memancarkan satu einstein.
:::

::: {.contoh}
**Contoh 1.20 · Freon dan ultraviolet stratosfer**

Energi ikatan C–Cl dalam CFC sekitar 339 kJ/mol. (a) Berapa panjang gelombang terpanjang yang dapat memutus ikatan itu? (b) Mengapa CFC mantap di troposfer, tetapi terurai di stratosfer?

**Penyelesaian.** (a) Dari (1.18), $\lambda = (1{,}196 \times 10^5\ \text{kJ/mol})/(339\ \text{kJ/mol}) = 353$ nm.

\(b) Secara energi, ultraviolet di bawah 353 nm sudah cukup. Tetapi molekul CFC hampir tidak menyerap cahaya di atas sekitar 230 nm; penyerapannya baru kuat di ultraviolet jauh. Foton sependek itu tidak sampai ke troposfer karena sudah diserap O₂ dan O₃ di lapisan atas. CFC yang naik ke stratosfer (di atas 20–30 km) terkena foton 190–220 nm dan melepaskan atom Cl yang merusak ozon.

**Memahami hasil.** Syarat energi ($h\nu \ge D$) perlu tetapi tidak cukup: molekul juga harus **menyerap** foton itu, yaitu harus ada transisi elektron yang cocok dengan energi foton. Penyerapan dibahas dengan teori perturbasi bergantung waktu di Bab 8 dan spektroskopi elektronik di Bab 15.
:::

::: {.contoh}
**Contoh 1.21 · Hasil kuantum fotolisis**

Larutan sebuah keton disinari ultraviolet 313 nm dengan daya terserap 100 mW selama 10,0 menit. Analisis menunjukkan $2{,}0 \times 10^{-5}$ mol keton terurai. Hitung hasil kuantumnya.

**Penyelesaian.** Energi yang diserap $E = (0{,}100\ \text{W})(600\ \text{s}) = 60{,}0$ J. Energi satu foton $hc/\lambda = 6{,}35 \times 10^{-19}$ J, jadi banyaknya foton $60{,}0/6{,}35 \times 10^{-19} = 9{,}45 \times 10^{19}$, atau $1{,}57 \times 10^{-4}$ einstein. Hasil kuantumnya

$$
\Phi = \frac{2{,}0 \times 10^{-5}}{1{,}57 \times 10^{-4}} = 0{,}13 .
$$

**Memahami hasil.** Hanya sekitar satu dari delapan foton yang terserap menghasilkan penguraian. Sisanya dilepaskan sebagai kalor, fluoresensi, atau kembali ke keadaan dasar lewat jalur lain (Bab 15). Pengukuran hasil kuantum memerlukan **aktinometer**, larutan acuan yang hasil kuantumnya diketahui, misalnya kalium ferioksalat, untuk mengukur banyaknya foton.
:::

::: {.contoh}
**Contoh 1.22 · Efisiensi energi fotosintesis**

Fotosistem tumbuhan menyerap terutama cahaya merah sekitar 680 nm. Untuk melepaskan satu molekul O₂ dari air dan mereduksi satu CO₂ diperlukan sedikitnya delapan foton. Energi bebas yang tersimpan dalam glukosa sekitar 2870 kJ tiap mol glukosa, yaitu sekitar 478 kJ tiap mol O₂. Berapa efisiensi energinya?

**Penyelesaian.** Satu mol foton 680 nm: $1{,}196 \times 10^5/680 = 176$ kJ. Delapan mol: 1407 kJ. Efisiensi $478/1407 = 0{,}34$, atau 34%.

**Memahami hasil.** Satu foton 680 nm (1,82 eV) tidak cukup untuk memecah air sendirian, karena oksidasi air menjadi O₂ memerlukan sekitar 1,23 eV tiap elektron ditambah energi lebih untuk mendorong laju. Alam memecahkannya dengan dua fotosistem berurutan yang masing-masing menyerap satu foton per elektron: empat elektron dikali dua foton sama dengan delapan foton. Batas 34% ini adalah batas termodinamika tahap fotokimia; efisiensi tumbuhan di lapangan jauh lebih rendah (sekitar 1–2%) karena sebagian besar spektrum Matahari tidak terserap atau terbuang.
:::

### Spektroskopi fotoelektron

Persamaan Einstein berlaku juga untuk molekul bebas. Jika molekul dalam fase gas disinari foton berenergi tetap $h\nu$ yang cukup besar, elektron dapat dilepaskan dari berbagai orbital. Elektron dari orbital dengan energi ionisasi $I_i$ keluar dengan energi kinetik

$$
K = h\nu - I_i . \qquad \text{(1.20)}
$$

Dengan mengukur sebaran energi kinetik fotoelektron, kita memperoleh energi ionisasi setiap orbital yang terisi. Teknik ini disebut **spektroskopi fotoelektron** (PES). Sumber yang umum adalah lampu helium (He I, 21,22 eV, panjang gelombang 58,4 nm) untuk elektron valensi dan sinar-X (XPS) untuk elektron kulit dalam. PES adalah bukti paling langsung bahwa elektron dalam molekul menempati **orbital** dengan energi yang berbeda-beda; ia menjadi uji utama teori orbital molekul di Bab 11–13.

::: {.contoh}
**Contoh 1.23 · Spektrum fotoelektron nitrogen**

Spektrum fotoelektron N₂ dengan sumber He I (21,22 eV) menunjukkan tiga pita yang bersesuaian dengan energi ionisasi 15,58, 16,69, dan 18,75 eV. Pada energi kinetik berapa ketiga pita itu teramati?

**Penyelesaian.** Dari (1.20): $21{,}22 - 15{,}58 = 5{,}64$ eV; $21{,}22 - 16{,}69 = 4{,}53$ eV; $21{,}22 - 18{,}75 = 2{,}47$ eV.

**Memahami hasil.** Ketiga pita berasal dari tiga orbital molekul valensi terluar N₂, yang di Bab 11 akan dikenali sebagai $3\sigma_g$, $1\pi_u$, dan $2\sigma_u$. Pita kedua (16,69 eV) memperlihatkan deret puncak yang berjarak sekitar 0,22 eV (Gambar 1.5 kanan): ion N₂⁺ yang terbentuk sedang bergetar. Lebar deret itu memberi tahu seberapa kuat elektron yang dilepaskan ikut mengikat atom. Orbital $1\pi_u$ bersifat mengikat kuat, sehingga melepaskannya mengubah panjang ikatan dan membangkitkan banyak tingkat getaran. Satu spektrum memuat informasi tentang energi orbital dan karakter ikatannya.
:::

::: {.kuis}
**Kuis cepat 1.4**

Sebuah lampu ultraviolet dan sebuah lampu inframerah sama-sama berdaya 10 W. Lampu mana yang memancarkan lebih banyak foton tiap detik? Lampu mana yang dapat memicu reaksi fotokimia?
:::

## 1.5 Efek Compton

Jika foton membawa momentum $h/\lambda$, maka dalam tumbukan dengan elektron, foton seharusnya terpental seperti bola biliar dan kehilangan sebagian energinya. Kehilangan energi berarti frekuensinya turun, atau panjang gelombangnya bertambah. Arthur Compton (1923) mengamati efek ini dengan menghamburkan sinar-X dari blok grafit. Hasilnya adalah bukti paling langsung bahwa foton berperilaku sebagai partikel yang membawa energi **dan** momentum.

### Pengamatan

Sinar-X monokromatik garis Mo Kα ($\lambda = 71{,}07$ pm) dijatuhkan pada grafit, dan sinar yang terhambur pada sudut $\theta$ dianalisis panjang gelombangnya dengan difraksi kristal. Pada setiap sudut, kecuali $\theta = 0$, terlihat dua puncak (Gambar 1.6 kanan): satu pada panjang gelombang semula, dan satu pada panjang gelombang yang lebih panjang $\lambda'$. Pergeseran $\lambda' - \lambda$ bertambah dengan sudut hamburan dan **tidak bergantung pada bahan** penghambur.

Teori gelombang klasik (hamburan Thomson) meramalkan bahwa elektron yang digetarkan oleh gelombang datang memancarkan kembali gelombang dengan **frekuensi yang sama**. Tidak ada pergeseran.

![Gambar 1.6 Kiri: foton berpanjang gelombang $\lambda$ bertumbukan dengan elektron yang diam; foton terhambur pada sudut $\theta$ dengan panjang gelombang $\lambda'$, elektron terpental pada sudut $\varphi$. Kanan: spektrum sinar-X Mo Kα yang dihamburkan grafit pada empat sudut. Puncak yang tidak bergeser berasal dari hamburan oleh elektron yang terikat kuat.](fig/c_compton.png){width=92%}

### Penurunan rumus Compton

Tinjau tumbukan foton dengan elektron bebas yang mula-mula diam (Gambar 1.6 kiri). Karena elektron dapat terpental dengan kelajuan yang mendekati $c$, kita pakai mekanika relativistik: energi elektron $E_e$ dan momentumnya $p_e$ berhubungan menurut $E_e^2 = (p_ec)^2 + (m_ec^2)^2$. Tulis $p = h/\lambda$ dan $p' = h/\lambda'$ untuk momentum foton sebelum dan sesudah tumbukan. Energi foton adalah $pc$ dan $p'c$.

**Kekekalan momentum.** Momentum awal hanya milik foton, jadi $\vec p = \vec p\,' + \vec p_e$, atau $\vec p_e = \vec p - \vec p\,'$. Kuadratkan, dengan $\theta$ sudut antara $\vec p$ dan $\vec p\,'$ (aturan kosinus):

$$
p_e^2 = p^2 + p'^2 - 2pp'\cos\theta . \qquad \text{(i)}
$$

**Kekekalan energi.** Energi awal adalah energi foton ditambah energi diam elektron:

$$
pc + m_ec^2 = p'c + E_e \quad\Longrightarrow\quad E_e = (p - p')c + m_ec^2 . \qquad \text{(ii)}
$$

**Gabungkan.** Kuadratkan (ii) dan samakan dengan $E_e^2 = p_e^2c^2 + m_e^2c^4$:

$$
(p - p')^2c^2 + 2(p - p')m_ec^3 + m_e^2c^4 = p_e^2c^2 + m_e^2c^4 .
$$

Suku $m_e^2c^4$ saling meniadakan. Bagi dengan $c^2$ dan masukkan (i):

$$
p^2 - 2pp' + p'^2 + 2(p - p')m_ec = p^2 + p'^2 - 2pp'\cos\theta .
$$

Suku $p^2$ dan $p'^2$ saling meniadakan, menyisakan

$$
(p - p')\,m_ec = pp'(1 - \cos\theta) .
$$

Bagi kedua ruas dengan $pp'm_ec$: $\dfrac{1}{p'} - \dfrac{1}{p} = \dfrac{1 - \cos\theta}{m_ec}$. Kalikan dengan $h$ dan ingat $h/p = \lambda$:

$$
\boxed{\ \lambda' - \lambda = \frac{h}{m_ec}(1 - \cos\theta)\ } \qquad \text{(1.21)}
$$

Besaran $\lambda_C = h/m_ec = 2{,}426$ pm disebut **panjang gelombang Compton** elektron. Pergeseran terbesar, $2\lambda_C = 4{,}85$ pm, terjadi pada hamburan balik ($\theta = 180°$). Rumus ini cocok sempurna dengan data Compton.

Mengapa ada puncak yang tidak bergeser? Elektron dalam kulit dalam atom karbon terikat kuat, sehingga foton tidak dapat melepaskannya; foton terhambur oleh **seluruh atom**. Massa yang terpental sekarang massa atom, sekitar 22 000 kali massa elektron, sehingga pergeserannya praktis nol.

::: {.inti}
**Foton membawa energi dan momentum.** $E = h\nu = hc/\lambda$, $p = h/\lambda$. Dalam tumbukan dengan elektron, kedua besaran itu kekal, persis seperti tumbukan dua partikel. Pergeseran Compton $\Delta\lambda = \lambda_C(1 - \cos\theta)$ tidak bergantung pada panjang gelombang datang, sehingga hanya berarti bila $\lambda$ sendiri sebanding dengan $\lambda_C$, yaitu untuk sinar-X dan sinar gamma.
:::

::: {.contoh}
**Contoh 1.24 · Hamburan sinar-X molibdenum**

Sinar-X Mo Kα (71,07 pm) dihamburkan elektron bebas dengan sudut 90°. Hitung (a) panjang gelombang terhambur, (b) energi kinetik elektron yang terpental, (c) arah gerak elektron itu.

**Penyelesaian.** (a) $\lambda' = 71{,}07 + 2{,}426(1 - \cos 90°) = 73{,}50$ pm.

\(b) Energi kinetik elektron sama dengan energi yang hilang dari foton:

$$
K = hc\left(\frac{1}{\lambda} - \frac{1}{\lambda'}\right) = (1239{,}8\ \text{eV·nm})\left(\frac{1}{0{,}07107} - \frac{1}{0{,}07350}\right) \text{nm}^{-1} = 576\ \text{eV}.
$$

\(c) Ambil foton datang sepanjang sumbu $x$ dan foton terhambur sepanjang sumbu $+y$. Momentum elektron $\vec p_e = \vec p - \vec p\,'$ mempunyai komponen $p_x = h/\lambda$ dan $p_y = -h/\lambda'$. Sudutnya di bawah sumbu $x$: $\tan\varphi = \lambda/\lambda' = 0{,}967$, jadi $\varphi = 44{,}0°$.

**Memahami hasil.** Foton sinar-X 17,4 keV hanya kehilangan 3,3% energinya. Energi elektron yang terpental (576 eV) jauh lebih kecil daripada energi diamnya (511 keV), jadi untuk kasus ini mekanika Newton sebenarnya sudah cukup bagi elektron; yang mutlak memerlukan relativitas adalah foton.
:::

::: {.contoh}
**Contoh 1.25 · Mengapa efek Compton tidak terlihat pada cahaya tampak**

Berapa perubahan fraksional panjang gelombang cahaya 500 nm yang dihamburkan balik oleh elektron bebas?

**Penyelesaian.** $\Delta\lambda/\lambda = 2\lambda_C/\lambda = 2(2{,}426 \times 10^{-12})/(500 \times 10^{-9}) = 9{,}7 \times 10^{-6}$.

**Memahami hasil.** Pergeseran sepuluh per sejuta jauh di bawah lebar garis spektrum biasa. Lagi pula, elektron dalam bahan terikat dengan energi beberapa eV, sebanding dengan energi foton tampak, sehingga anggapan "elektron bebas" tidak berlaku. Untuk sinar-X dengan $\lambda \approx 0{,}07$ nm, pergeserannya beberapa persen dan energi ikat elektron luar kecil dibandingkan energi foton.
:::

::: {.contoh}
**Contoh 1.26 · Tepi Compton dalam spektroskopi gamma**

Detektor sinar gamma yang mengukur sumber ¹³⁷Cs (foton 661,7 keV) menunjukkan, selain puncak utama, spektrum malar yang berakhir tajam pada suatu energi (tepi Compton), dan puncak kecil di sekitar 184 keV. Jelaskan dan hitung kedua angka itu. Pakai $m_ec^2 = 511{,}0$ keV.

**Penyelesaian.** Dalam bentuk energi, (1.21) menjadi $1/E' - 1/E = (1 - \cos\theta)/m_ec^2$, atau

$$
E' = \frac{E}{1 + (E/m_ec^2)(1 - \cos\theta)} .
$$

Elektron dalam detektor menerima energi terbesar ketika foton terhambur balik ($\theta = 180°$): $E' = 661{,}7/(1 + 2 \times 1{,}2949) = 184{,}3$ keV. Energi elektron terbesar $661{,}7 - 184{,}3 = 477{,}4$ keV: itulah tepi Compton. Foton yang terhambur balik dari bahan di sekitar detektor lalu masuk ke detektor menghasilkan puncak di 184 keV.

**Memahami hasil.** Analis radiokimia memakai rumus ini setiap hari untuk menafsirkan spektrum gamma. Untuk foton berenergi tinggi, energi terhambur balik tidak pernah melebihi sekitar $m_ec^2/2 = 256$ keV, berapa pun energi foton datang.
:::

### Momentum foton dalam kimia

Efek Compton menunjukkan bahwa momentum foton nyata. Akibatnya juga terasa pada atom: setiap kali atom menyerap foton, atom terdorong searah foton dengan perubahan momentum $h/\lambda$. Ketika atom kemudian memancarkan foton secara spontan ke arah acak, dorongan baliknya rata-rata nol. Dengan menembakkan laser yang frekuensinya diatur tepat sedikit di bawah frekuensi resonansi atom, atom yang bergerak menuju laser lebih sering menyerap (efek Doppler) dan diperlambat. Inilah **pendinginan laser** (Hadiah Nobel Fisika 1997), yang kini dipakai untuk menghasilkan gas atom dan molekul pada suhu mikrokelvin dan untuk mempelajari reaksi kimia ultradingin.

::: {.contoh}
**Contoh 1.27 · Dorongan satu foton pada atom natrium**

Atom natrium (massa 22,99 u) menyerap foton 589,0 nm. (a) Berapa perubahan kecepatannya? (b) Berapa foton yang harus diserap berurutan untuk menghentikan atom yang bergerak 300 m/s?

**Penyelesaian.** (a) $\Delta v = h/(m\lambda) = (6{,}626 \times 10^{-34})/[(22{,}99)(1{,}661 \times 10^{-27})(589{,}0 \times 10^{-9})] = 0{,}0295$ m/s, yaitu 2,95 cm/s.

\(b) $N = 300/0{,}0295 = 1{,}0 \times 10^4$ foton.

**Memahami hasil.** Sepuluh ribu foton terdengar banyak, tetapi atom natrium dapat menyerap dan memancarkan kembali sekitar $3 \times 10^7$ foton tiap detik (umur keadaan tereksitasinya 16 ns). Jadi atom dapat dihentikan dalam waktu sekitar satu milidetik, dengan perlambatan sekitar $10^5$ kali percepatan gravitasi.
:::

::: {.kuis}
**Kuis cepat 1.5**

Pada sudut hamburan berapa pergeseran Compton sama dengan nol? Sama dengan $\lambda_C$? Apakah pergeseran itu lebih besar untuk sinar-X 70 pm atau untuk sinar gamma 1 pm?
:::
