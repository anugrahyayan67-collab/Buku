## 17.7 Analisis populasi, muatan atom, potensial elektrostatik

### Membagi elektron di antara atom

Kimiawan berpikir dengan muatan parsial: karbon karbonil bermuatan positif, oksigennya negatif. Tetapi "muatan atom" bukan besaran yang dapat diamati; yang dapat diamati adalah rapat elektron $\rho(\mathbf r)$ dan besaran turunannya seperti momen dipol. Membagi elektron di antara atom selalu memerlukan aturan yang sedikit sembarang, dan aturan yang berbeda memberi angka yang berbeda. Meski begitu, muatan atom sangat berguna untuk membandingkan molekul-molekul yang dihitung dengan cara sama, dan untuk membangun medan gaya mekanika molekul (subbab 17.17).

Jumlah elektron dapat ditulis dengan matriks kerapatan (17.e11):

$$
N = \int\rho\,d\mathbf r = \sum_{\mu\nu}P_{\mu\nu}S_{\nu\mu} = \sum_\mu(\mathbf P\mathbf S)_{\mu\mu} . \qquad \text{(17.e25)}
$$

**Analisis populasi Mulliken** (1955) memberikan $(\mathbf P\mathbf S)_{\mu\mu}$ kepada atom tempat fungsi $\phi_\mu$ berpusat. Ini sama dengan memberikan populasi "bersih" $P_{\mu\mu}$ fungsi itu sendiri, ditambah separuh **populasi tumpang tindih** $P_{\mu\nu}S_{\mu\nu}$ dengan setiap fungsi lain. Muatan Mulliken atom A:

$$
q_A = Z_A - \sum_{\mu \in A}(\mathbf P\mathbf S)_{\mu\mu} . \qquad \text{(17.e26)}
$$

Pembagian tumpang tindih secara sama rata adalah titik lemahnya: dalam ikatan polar, awan tumpang tindih sebenarnya lebih dekat ke atom yang elektronegatif. Kelemahan kedua lebih serius: fungsi basis difus yang berpusat di satu atom dapat meluas jauh ke atom lain, tetapi elektronnya tetap dihitung milik atom pusatnya. Akibatnya muatan Mulliken sangat peka terhadap basis dan dapat menjadi tidak masuk akal (populasi orbital negatif atau lebih dari 2) dengan basis besar.

**Analisis Löwdin** mengubah dahulu basis menjadi ortonormal dengan $\mathbf S^{1/2}$, lalu membaca populasi dari diagonal $\mathbf S^{1/2}\mathbf P\mathbf S^{1/2}$; tidak ada populasi tumpang tindih yang perlu dibagi. Metode lain mendefinisikan atom di ruang nyata, bukan di ruang basis: **analisis populasi alami** (NPA, dari teori orbital ikatan alami NBO), **Hirshfeld** (membagi $\rho$ menurut perbandingan rapat atom bebas), dan **QTAIM** Bader (membagi ruang dengan permukaan yang fluks gradien $\rho$-nya nol). Metode-metode ini jauh lebih stabil terhadap pergantian basis.

### Momen dipol: besaran yang teramati

Momen dipol molekul netral tidak bergantung pada pilihan titik asal dan merupakan nilai harap operator yang jelas:

$$
\boldsymbol\mu = \sum_AZ_A\mathbf R_A - \int\mathbf r\,\rho(\mathbf r)\,d\mathbf r = \sum_AZ_A\mathbf R_A - \sum_{\mu\nu}P_{\mu\nu}\langle\phi_\nu|\mathbf r|\phi_\mu\rangle . \qquad \text{(17.e27)}
$$

Dalam satuan atom, 1 $ea_0 = 2{,}5417$ debye. Karena teramati, momen dipol berkonvergensi ke nilai tertentu bila basis diperbesar, tidak seperti muatan Mulliken. Hartree–Fock dengan basis besar biasanya melebih-lebihkan momen dipol sekitar 10%, karena tanpa korelasi elektron terlalu "ionik": ia tidak cukup bebas berpindah kembali ke atom yang kurang elektronegatif.

### Potensial elektrostatik

Potensial yang dirasakan muatan uji positif di titik $\mathbf r$ adalah

$$
V(\mathbf r) = \sum_A\frac{Z_A}{|\mathbf r - \mathbf R_A|} - \int\frac{\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}\,d\mathbf r' . \qquad \text{(17.e28)}
$$

Peta potensial elektrostatik pada permukaan rapat elektron (biasanya $\rho = 0{,}001$ e/bohr³) menunjukkan daerah yang menarik elektrofil (merah, $V < 0$: pasangan elektron bebas, ikatan π) dan nukleofil (biru, $V > 0$: proton asam). Muatan **ESP** (CHELPG, Merz–Kollman, RESP) dipilih agar muatan titik di inti meniru $V(\mathbf r)$ sebaik mungkin di luar molekul. Karena menirukan besaran yang teramati dan secara langsung menentukan interaksi antarmolekul, muatan ESP adalah pilihan baku untuk medan gaya biomolekul.

::: {.contoh}
**Contoh 17.c23 · Muatan oksigen dalam air bergantung pada basis**

Muatan oksigen H₂O (geometri percobaan) menurut Mulliken dan Löwdin, dihitung dengan program pendamping:

| Basis | $q_\text{O}$ Mulliken | $q_\text{O}$ Löwdin |
|---|---|---|
| STO-3G | $-0{,}366$ | $-0{,}253$ |
| 6-31G | $-0{,}792$ | $-0{,}581$ |
| 6-31G* | $-0{,}866$ | $-0{,}728$ |
| 6-31G** | $-0{,}674$ | $-0{,}454$ |

Apa yang dapat disimpulkan?

**Penyelesaian.** Muatan Mulliken berubah lebih dari dua kali dari STO-3G ke 6-31G*, lalu turun lagi ketika fungsi p ditambahkan pada H. Muatan Löwdin selalu lebih kecil daripada muatan Mulliken, tetapi sama gelisahnya terhadap basis. Penambahan fungsi p pada H (6-31G**) memindahkan sebagian rapat elektron di daerah ikatan ke "milik" hidrogen, sehingga muatan oksigen tampak berkurang, padahal rapat elektronnya hampir tidak berubah.

**Memahami hasil.** Tidak ada satu angka "muatan oksigen dalam air" yang benar. Perbandingan muatan antarmolekul hanya bermakna bila dihitung dengan metode dan basis yang sama, dan lebih baik dengan skema yang stabil (NPA, Hirshfeld, ESP). Dalam publikasi, skema muatan selalu harus disebut.
:::

::: {.contoh}
**Contoh 17.c24 · Momen dipol air**

Momen dipol H₂O dari program pendamping: STO-3G 1,73 D; 6-31G 2,63 D; 6-31G* 2,23 D; 6-31G** 2,18 D. Nilai percobaan 1,85 D, dan batas HF sekitar 1,98 D. Jelaskan polanya.

**Penyelesaian.** STO-3G terlalu kecil karena basis minimal tidak dapat mengalirkan cukup elektron ke oksigen. Basis 6-31G, tanpa polarisasi, terlalu besar karena fungsi valensi luar yang menyebar membuat oksigen terlalu ionik dan pasangan elektron bebas tidak dapat "membengkok" ke belakang. Fungsi polarisasi memperbaikinya, dan hasilnya mendekati batas HF. Sisa selisih dengan percobaan (sekitar 0,13 D) adalah efek korelasi.

**Memahami hasil.** Basis 6-31G tanpa polarisasi melebih-lebihkan momen dipol hampir 45%, yang menerangkan mengapa basis ini memberi ikatan hidrogen terlalu kuat (Contoh 17.c18). Untuk sifat listrik molekul (dipol, polarisabilitas), polarisasi dan fungsi difus jauh lebih penting daripada untuk energi.
:::

::: {.contoh}
**Contoh 17.c25 · Muatan titik tidak cukup untuk menerangkan dipol**

Dengan muatan Mulliken STO-3G ($q_\text{H} = +0{,}183$) dan koordinat hidrogen ($z_\text{H} = 1{,}1072$ bohr di atas oksigen), hitung momen dipol model muatan titik. Ulangi dengan muatan 6-31G* ($q_\text{H} = +0{,}433$). Bandingkan dengan momen dipol yang sebenarnya dihitung (1,73 D dan 2,23 D).

**Penyelesaian.** $\mu_z = 2q_\text{H}z_\text{H}$ (muatan oksigen di titik asal tidak menyumbang). STO-3G: $2(0{,}183)(1{,}1072) = 0{,}405\ ea_0 = 1{,}03$ D. 6-31G*: $2(0{,}433)(1{,}1072) = 0{,}959\ ea_0 = 2{,}44$ D.

**Memahami hasil.** Model muatan Mulliken memberi dipol 40% terlalu kecil untuk STO-3G dan 9% terlalu besar untuk 6-31G*. Rapat elektron di sekitar setiap atom tidak bersimetri bola: pasangan elektron bebas oksigen menonjol ke belakang dan membentuk **dipol atom** sendiri. Muatan Mulliken mengabaikan dipol atom ini, sedangkan muatan ESP justru memilih muatan yang meniru potensial luar, sehingga menyerap sebagian pengaruhnya.
:::

::: {.contoh}
**Contoh 17.c26 · Amonia: dipol HF terlalu besar**

HF/6-31G* untuk NH₃ ($r = 1{,}012$ Å, $\angle = 106{,}67°$) memberi momen dipol 1,95 D dan muatan Mulliken nitrogen $-0{,}99$. Nilai percobaan momen dipol 1,47 D. Hitung galat relatifnya. Mengapa NH₃, yang nitrogennya kurang elektronegatif daripada oksigen, mempunyai muatan Mulliken lebih negatif daripada oksigen dalam air (6-31G*: $-0{,}87$)?

**Penyelesaian.** Galat $(1{,}95 - 1{,}47)/1{,}47 = 33\%$. Nitrogen mengikat tiga hidrogen, masing-masing menyumbang sekitar $+0{,}33$, sehingga nitrogen menampung muatan negatif dari tiga ikatan; oksigen dalam air hanya dari dua.

**Memahami hasil.** Galat dipol NH₃ dengan HF/6-31G* jauh lebih besar daripada untuk air, sebagian karena basis tanpa fungsi difus tidak menggambarkan pasangan elektron bebas nitrogen yang menyebar. Pelajaran umum: muatan atom menjumlahkan sumbangan ikatan, bukan hanya mencerminkan keelektronegatifan, dan dipol molekul adalah hasil penjumlahan vektor yang peka terhadap geometri (sudut piramidal) dan pasangan elektron bebas.
:::

::: {.kuis}
**Kuis cepat 17.7**

Mengapa momen dipol berkonvergensi ketika basis diperbesar, sedangkan muatan Mulliken tidak? Dalam peta potensial elektrostatik molekul air, di mana daerah paling negatif?
:::

## 17.8 OM terlokalisasi

### Kebebasan memutar orbital terisi

Orbital kanonik HF menyebar ke seluruh molekul dan mencerminkan simetrinya. Tetapi determinan Slater mempunyai sifat yang telah kita singgung di subbab 17.2: bila orbital-orbital terisi dicampur dengan transformasi uniter apa pun,

$$
\psi_i' = \sum_{j\,\text{terisi}}U_{ji}\psi_j, \qquad \mathbf U^\dagger\mathbf U = \mathbf 1 , \qquad \text{(17.e29)}
$$

determinan baru sama dengan determinan lama dikali $\det\mathbf U$, suatu faktor fase. Ini adalah sifat determinan: mengganti kolom-kolom dengan kombinasi linearnya hanya mengalikan determinan dengan determinan matriks kombinasi. Akibatnya **energi total, rapat elektron, momen dipol, dan semua besaran teramati tidak berubah**. Matriks kerapatan $\mathbf P = 2\mathbf C_\text{terisi}\mathbf C_\text{terisi}^\dagger$ juga invarian, karena $\mathbf C'\mathbf C'^\dagger = \mathbf C\mathbf U\mathbf U^\dagger\mathbf C^\dagger = \mathbf C\mathbf C^\dagger$.

Jadi orbital kanonik hanyalah satu pilihan di antara tak terhingga banyak pilihan yang setara. Pilihan itu istimewa untuk ionisasi (teorema Koopmans) dan spektroskopi, karena orbital kanonik adalah fungsi eigen operator Fock. Untuk berpikir tentang ikatan, pilihan lain lebih bermakna: orbital yang dipusatkan sekompak mungkin pada satu atau dua atom, **orbital molekul terlokalisasi** (LMO).

### Kriteria lokalisasi

Ada beberapa resep untuk memilih $\mathbf U$:

- **Boys–Foster**: maksimumkan jumlah kuadrat jarak antara pusat-pusat muatan orbital, $\sum_i|\langle\psi_i|\mathbf r|\psi_i\rangle|^2$, atau setara, minimumkan sebaran ruang setiap orbital. Sederhana karena hanya memerlukan integral dipol.
- **Edmiston–Ruedenberg**: maksimumkan jumlah energi tolakan diri $\sum_i(ii|ii)$. Lebih mahal tetapi dianggap paling "fisis".
- **Pipek–Mezey**: maksimumkan jumlah kuadrat populasi Mulliken orbital pada atom-atom. Menjaga pemisahan ikatan σ dan π.
- **Orbital ikatan alami** (NBO, Weinhold): bukan lokalisasi orbital HF secara langsung, melainkan pencarian orbital satu dan dua pusat dengan okupansi mendekati 2 dari matriks kerapatan; sangat populer karena menerjemahkan hasil perhitungan ke bahasa struktur Lewis, hibridisasi, dan hiperkonjugasi.

Dalam praktik, LMO dari berbagai kriteria sangat mirip untuk molekul dengan struktur Lewis yang jelas: satu orbital inti untuk setiap atom berat, satu orbital dua pusat untuk setiap ikatan, dan satu orbital satu pusat untuk setiap pasangan elektron bebas. Dengan kata lain, LMO menghidupkan kembali struktur Lewis dan hibrida ikatan valensi (Bab 12) dari fungsi gelombang orbital molekul. Ikatan ganda menjadi dua "ikatan pisang" yang setara (lokalisasi Boys) atau satu σ dan satu π (Pipek–Mezey).

Lokalisasi juga punya nilai praktis besar. Korelasi elektron sebagian besar bersifat jarak pendek, sehingga bila dinyatakan dengan LMO, sebagian besar pasangan orbital yang berjauhan dapat diabaikan atau dihampiri. Inilah dasar metode korelasi lokal (LMP2, DLPNO-CCSD(T)) yang membuat perhitungan berkualitas *coupled-cluster* mungkin untuk molekul ratusan atom.

![Gambar 17.g06 Orbital terlokalisasi Boys H₂O (HF/STO-3G). Kiri: salah satu orbital ikatan O–H di bidang molekul (yz). Kanan: kedua orbital pasangan bebas di bidang xz yang tegak lurus bidang molekul, membentuk "telinga kelinci" dengan sudut sekitar 120° di antara pusatnya. Bandingkan dengan orbital kanonik pada Gambar 17.g05.](fig/c_lokal.png){width=90%}

::: {.contoh}
**Contoh 17.c27 · Memutar dua orbital: dari s dan p ke hibrida**

Misalkan dua orbital terisi ortonormal adalah orbital s dan p$_z$ pada satu atom. Putar keduanya dengan sudut 45°: $h_\pm = (s \pm p_z)/\sqrt2$. Tunjukkan bahwa jumlah rapat kedua orbital tidak berubah, dan tentukan ke mana pusat muatan $h_\pm$ bergeser.

**Penyelesaian.** $|h_+|^2 + |h_-|^2 = \tfrac12[(s + p_z)^2 + (s - p_z)^2] = s^2 + p_z^2$: rapat total sama. Pusat muatan $\langle h_\pm|z|h_\pm\rangle = \tfrac12[\langle s|z|s\rangle + \langle p_z|z|p_z\rangle \pm 2\langle s|z|p_z\rangle] = \pm\langle s|z|p_z\rangle$, karena $\langle s|z|s\rangle = \langle p_z|z|p_z\rangle = 0$ oleh paritas. Kedua hibrida bergeser ke arah $+z$ dan $-z$ sejauh $|\langle s|z|p_z\rangle|$.

**Memahami hasil.** Inilah hibridisasi sp (subbab 12.3) dilihat sebagai lokalisasi: rotasi memusatkan setiap orbital ke satu arah tanpa mengubah fisika apa pun. Kriteria Boys memilih sudut rotasi yang menjauhkan pusat-pusat muatan sejauh mungkin, sehingga untuk dua orbital ini ia memilih tepat 45°.
:::

::: {.contoh}
**Contoh 17.c28 · Orbital terlokalisasi air**

Lokalisasi Boys orbital terisi H₂O/STO-3G (program pendamping) memberi: satu orbital inti O 1s; dua orbital ikatan dengan pusat muatan di $(0, \pm0{,}453, 0{,}357)$ Å; dua orbital pasangan bebas dengan pusat di $(\pm0{,}264, 0, -0{,}154)$ Å, yaitu di bidang tegak lurus bidang molekul, di belakang oksigen. Hitung (a) jarak pusat ikatan dari O sebagai pecahan panjang ikatan, (b) sudut antara kedua pusat pasangan bebas, (c) sudut antara kedua pusat ikatan.

**Penyelesaian.** (a) $\sqrt{0{,}453^2 + 0{,}357^2} = 0{,}577$ Å, yaitu 60% dari 0,957 Å. (b) Setengah sudutnya $\arctan(0{,}264/0{,}154) = 59{,}7°$, sehingga sudutnya 119,5°. (c) $2\arctan(0{,}453/0{,}357) = 103{,}6°$.

**Memahami hasil.** Pusat ikatan terletak lebih dekat ke hidrogen daripada ke titik tengah ikatan? Tidak: 60% dari O berarti 40% dari H, sehingga orbital ikatan sedikit condong ke arah hidrogen dalam basis minimal ini. Dengan 6-31G, pusatnya bergeser ke 0,524 Å (55%) dan populasinya pada O naik dari 0,58 ke 0,68: ikatan menjadi lebih polar ke arah oksigen, sesuai keelektronegatifan. Pasangan bebas membentuk sudut sekitar 120°, lebih besar daripada sudut ikatan, sesuai dengan aturan VSEPR bahwa pasangan bebas menempati ruang lebih besar (subbab 12.11). Gambaran "dua pasangan bebas setara" adalah lokalisasi; gambaran kanonik ($1b_1$ dan $3a_1$, berbeda energi 1,7 eV) adalah yang teramati dalam spektrum fotoelektron. Keduanya benar untuk pertanyaan yang berbeda.
:::

::: {.contoh}
**Contoh 17.c29 · Metana: satu energi, dua gambaran**

Untuk CH₄/STO-3G, orbital kanonik valensi adalah satu $2a_1$ ($-0{,}910\ E_h$) dan tiga $1t_2$ ($-0{,}519\ E_h$). Lokalisasi Boys memberi empat orbital setara, masing-masing berpusat pada garis C–H, 0,743 Å dari karbon (panjang ikatan 1,087 Å). Hitung jumlah energi orbital valensi untuk kedua set, dengan memakai unsur diagonal matriks Fock untuk orbital terlokalisasi. Apakah energi total berubah?

**Penyelesaian.** Kanonik: $2(-0{,}910) + 6(-0{,}519) = -4{,}934\ E_h$. Jejak matriks Fock dalam subruang orbital terisi tidak berubah oleh rotasi uniter, sehingga keempat LMO masing-masing mempunyai $\langle\psi_i'|\hat f|\psi_i'\rangle = \tfrac14(-0{,}910 - 3 \times 0{,}519) = -0{,}617\ E_h$, dan jumlahnya tetap $-4{,}934\ E_h$. Energi total tidak berubah ($-39{,}7268\ E_h$).

**Memahami hasil.** Keempat LMO mempunyai "energi" sama, $-0{,}617\ E_h$ (16,8 eV), tetapi itu bukan energi ionisasi, karena LMO bukan fungsi eigen operator Fock: matriks Fock dalam basis LMO mempunyai unsur di luar diagonal sebesar sekitar $0{,}1\ E_h$ yang mengopel ikatan-ikatan. Kopling inilah yang memecah empat ionisasi "ikatan C–H" menjadi pita $t_2$ dan $a_1$ yang teramati. Pusat LMO terletak 68% dari karbon, sedikit condong ke hidrogen dalam basis minimal, mirip dengan air.
:::

::: {.kuis}
**Kuis cepat 17.8**

Bila orbital terisi diganti dengan orbital terlokalisasi, apa yang terjadi pada energi total, momen dipol, dan energi orbital? Mengapa metode korelasi lokal dapat mengabaikan pasangan LMO yang berjauhan?
:::
