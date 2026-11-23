## 17.7 Analisis populasi, muatan atom, potensial elektrostatik

### Membagi elektron di antara atom

Kimiawan berpikir dengan muatan parsial: karbon karbonil bermuatan positif, oksigennya negatif. Tetapi "muatan atom" bukan besaran yang dapat diamati; yang dapat diamati adalah rapat elektron $\rho(\mathbf r)$ dan besaran turunannya seperti momen dipol. Membagi elektron di antara atom selalu memerlukan aturan yang sedikit sembarang, dan aturan yang berbeda memberi angka yang berbeda. Meski begitu, muatan atom sangat berguna untuk membandingkan molekul-molekul yang dihitung dengan cara sama, dan untuk membangun medan gaya mekanika molekul (subbab 17.17).

Jumlah elektron dapat ditulis dengan matriks kerapatan (17.11):

$$
N = \int\rho\,d\mathbf r = \sum_{\mu\nu}P_{\mu\nu}S_{\nu\mu} = \sum_\mu(\mathbf P\mathbf S)_{\mu\mu} . \qquad \text{(17.25)}
$$

**Analisis populasi Mulliken** (1955) memberikan $(\mathbf P\mathbf S)_{\mu\mu}$ kepada atom tempat fungsi $\phi_\mu$ berpusat. Ini sama dengan memberikan populasi "bersih" $P_{\mu\mu}$ fungsi itu sendiri, ditambah separuh **populasi tumpang tindih** $P_{\mu\nu}S_{\mu\nu}$ dengan setiap fungsi lain. Muatan Mulliken atom A:

$$
q_A = Z_A - \sum_{\mu \in A}(\mathbf P\mathbf S)_{\mu\mu} . \qquad \text{(17.26)}
$$

Pembagian tumpang tindih secara sama rata adalah titik lemahnya: dalam ikatan polar, awan tumpang tindih sebenarnya lebih dekat ke atom yang elektronegatif. Kelemahan kedua lebih serius: fungsi basis difus yang berpusat di satu atom dapat meluas jauh ke atom lain, tetapi elektronnya tetap dihitung milik atom pusatnya. Akibatnya muatan Mulliken sangat peka terhadap basis dan dapat menjadi tidak masuk akal (populasi orbital negatif atau lebih dari 2) dengan basis besar.

**Analisis Löwdin** mengubah dahulu basis menjadi ortonormal dengan $\mathbf S^{1/2}$, lalu membaca populasi dari diagonal $\mathbf S^{1/2}\mathbf P\mathbf S^{1/2}$; tidak ada populasi tumpang tindih yang perlu dibagi. Metode lain mendefinisikan atom di ruang nyata, bukan di ruang basis: **analisis populasi alami** (NPA, dari teori orbital ikatan alami NBO), **Hirshfeld** (membagi $\rho$ menurut perbandingan rapat atom bebas), dan **QTAIM** Bader (membagi ruang dengan permukaan yang fluks gradien $\rho$-nya nol). Metode-metode ini jauh lebih stabil terhadap pergantian basis.

### Momen dipol: besaran yang teramati

Momen dipol molekul netral tidak bergantung pada pilihan titik asal dan merupakan nilai harap operator yang jelas:

$$
\boldsymbol\mu = \sum_AZ_A\mathbf R_A - \int\mathbf r\,\rho(\mathbf r)\,d\mathbf r = \sum_AZ_A\mathbf R_A - \sum_{\mu\nu}P_{\mu\nu}\langle\phi_\nu|\mathbf r|\phi_\mu\rangle . \qquad \text{(17.27)}
$$

Dalam satuan atom, 1 $ea_0 = 2{,}5417$ debye. Karena teramati, momen dipol berkonvergensi ke nilai tertentu bila basis diperbesar, tidak seperti muatan Mulliken. Hartree–Fock dengan basis besar biasanya melebih-lebihkan momen dipol sekitar 10%, karena tanpa korelasi elektron terlalu "ionik": ia tidak cukup bebas berpindah kembali ke atom yang kurang elektronegatif.

### Potensial elektrostatik

Potensial yang dirasakan muatan uji positif di titik $\mathbf r$ adalah

$$
V(\mathbf r) = \sum_A\frac{Z_A}{|\mathbf r - \mathbf R_A|} - \int\frac{\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}\,d\mathbf r' . \qquad \text{(17.28)}
$$

Peta potensial elektrostatik pada permukaan rapat elektron (biasanya $\rho = 0{,}001$ e/bohr³) menunjukkan daerah yang menarik elektrofil (merah, $V < 0$: pasangan elektron bebas, ikatan π) dan nukleofil (biru, $V > 0$: proton asam). Muatan **ESP** (CHELPG, Merz–Kollman, RESP) dipilih agar muatan titik di inti meniru $V(\mathbf r)$ sebaik mungkin di luar molekul. Karena menirukan besaran yang teramati dan secara langsung menentukan interaksi antarmolekul, muatan ESP adalah pilihan baku untuk medan gaya biomolekul.

::: {.contoh}
**Contoh 17.26 · Muatan oksigen dalam air bergantung pada basis**

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
**Contoh 17.27 · Momen dipol air**

Momen dipol H₂O dari program pendamping: STO-3G 1,73 D; 6-31G 2,63 D; 6-31G* 2,23 D; 6-31G** 2,18 D. Nilai percobaan 1,85 D, dan batas HF sekitar 1,98 D. Jelaskan polanya.

**Penyelesaian.** STO-3G terlalu kecil karena basis minimal tidak dapat mengalirkan cukup elektron ke oksigen. Basis 6-31G, tanpa polarisasi, terlalu besar karena fungsi valensi luar yang menyebar membuat oksigen terlalu ionik dan pasangan elektron bebas tidak dapat "membengkok" ke belakang. Fungsi polarisasi memperbaikinya, dan hasilnya mendekati batas HF. Sisa selisih dengan percobaan (sekitar 0,13 D) adalah efek korelasi.

**Memahami hasil.** Basis 6-31G tanpa polarisasi melebih-lebihkan momen dipol hampir 45%, yang menerangkan mengapa basis ini memberi ikatan hidrogen terlalu kuat (Contoh 17.20). Untuk sifat listrik molekul (dipol, polarisabilitas), polarisasi dan fungsi difus jauh lebih penting daripada untuk energi.
:::

::: {.contoh}
**Contoh 17.28 · Muatan titik tidak cukup untuk menerangkan dipol**

Dengan muatan Mulliken STO-3G ($q_\text{H} = +0{,}183$) dan koordinat hidrogen ($z_\text{H} = 1{,}1072$ bohr di atas oksigen), hitung momen dipol model muatan titik. Ulangi dengan muatan 6-31G* ($q_\text{H} = +0{,}433$). Bandingkan dengan momen dipol yang sebenarnya dihitung (1,73 D dan 2,23 D).

**Penyelesaian.** $\mu_z = 2q_\text{H}z_\text{H}$ (muatan oksigen di titik asal tidak menyumbang). STO-3G: $2(0{,}183)(1{,}1072) = 0{,}405\ ea_0 = 1{,}03$ D. 6-31G*: $2(0{,}433)(1{,}1072) = 0{,}959\ ea_0 = 2{,}44$ D.

**Memahami hasil.** Model muatan Mulliken memberi dipol 40% terlalu kecil untuk STO-3G dan 9% terlalu besar untuk 6-31G*. Rapat elektron di sekitar setiap atom tidak bersimetri bola: pasangan elektron bebas oksigen menonjol ke belakang dan membentuk **dipol atom** sendiri. Muatan Mulliken mengabaikan dipol atom ini, sedangkan muatan ESP justru memilih muatan yang meniru potensial luar, sehingga menyerap sebagian pengaruhnya.
:::

::: {.contoh}
**Contoh 17.29 · Amonia: dipol HF terlalu besar**

HF/6-31G* untuk NH₃ ($r = 1{,}012$ Å, $\angle = 106{,}67°$) memberi momen dipol 1,95 D dan muatan Mulliken nitrogen $-0{,}99$. Nilai percobaan momen dipol 1,47 D. Hitung galat relatifnya. Mengapa NH₃, yang nitrogennya kurang elektronegatif daripada oksigen, mempunyai muatan Mulliken lebih negatif daripada oksigen dalam air (6-31G*: $-0{,}87$)?

**Penyelesaian.** Galat $(1{,}95 - 1{,}47)/1{,}47 = 33\%$. Nitrogen mengikat tiga hidrogen, masing-masing menyumbang sekitar $+0{,}33$, sehingga nitrogen menampung muatan negatif dari tiga ikatan; oksigen dalam air hanya dari dua.

**Memahami hasil.** Galat dipol NH₃ dengan HF/6-31G* jauh lebih besar daripada untuk air, sebagian karena basis tanpa fungsi difus tidak menggambarkan pasangan elektron bebas nitrogen yang menyebar. Pelajaran umum: muatan atom menjumlahkan sumbangan ikatan, bukan hanya mencerminkan keelektronegatifan, dan dipol molekul adalah hasil penjumlahan vektor yang peka terhadap geometri (sudut piramidal) dan pasangan elektron bebas.
:::

::: {.contoh}
**Contoh 17.30 · Potensial elektrostatik di sekitar air**

Dengan (17.28), program pendamping menghitung potensial elektrostatik H₂O (geometri percobaan) di tiga titik: 1,5 Å di belakang oksigen pada sumbu $C_2$; 1,5 Å di luar salah satu hidrogen, pada perpanjangan ikatan O–H; dan 1,5 Å di atas oksigen, tegak lurus bidang molekul. Hasilnya (dalam satuan atom, $E_h/e$): STO-3G $-0{,}072$; $+0{,}033$; $-0{,}036$; 6-31G* $-0{,}085$; $+0{,}048$; $-0{,}056$. Nyatakan energi interaksi muatan $+e$ di titik-titik itu dalam kJ/mol dan tafsirkan.

**Penyelesaian.** Kalikan dengan 2625,5 kJ/mol: STO-3G $-188$; $+86$; $-95$ kJ/mol; 6-31G* $-222$; $+125$; $-147$ kJ/mol.

**Memahami hasil.** Daerah di belakang oksigen, tempat kedua pasangan elektron bebas, sangat menarik muatan positif (proton atau kation logam), sedangkan daerah di luar hidrogen menolaknya, dan karena itu menarik anion dan pasangan elektron bebas molekul lain. Inilah peta ikatan hidrogen dalam bentuk angka: air adalah donor melalui hidrogennya dan akseptor melalui oksigennya. Potensial di atas bidang juga negatif, sesuai gambaran pasangan bebas yang menonjol ke luar bidang (Contoh 17.32). Dengan 6-31G* semua nilai lebih besar sekitar 20–45%, sejalan dengan momen dipol yang lebih besar (Contoh 17.27).
:::

::: {.kuis}
**Kuis cepat 17.7**

Mengapa momen dipol berkonvergensi ketika basis diperbesar, sedangkan muatan Mulliken tidak? Dalam peta potensial elektrostatik molekul air, di mana daerah paling negatif?
:::

## 17.8 OM terlokalisasi

### Kebebasan memutar orbital terisi

Orbital kanonik HF menyebar ke seluruh molekul dan mencerminkan simetrinya. Tetapi determinan Slater mempunyai sifat yang telah kita singgung di subbab 17.2: bila orbital-orbital terisi dicampur dengan transformasi uniter apa pun,

$$
\psi_i' = \sum_{j\,\text{terisi}}U_{ji}\psi_j, \qquad \mathbf U^\dagger\mathbf U = \mathbf 1 , \qquad \text{(17.29)}
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

![Gambar 17.6 Orbital terlokalisasi Boys H₂O (HF/STO-3G). Kiri: salah satu orbital ikatan O–H di bidang molekul (yz). Kanan: kedua orbital pasangan bebas di bidang xz yang tegak lurus bidang molekul, membentuk "telinga kelinci" dengan sudut sekitar 120° di antara pusatnya. Bandingkan dengan orbital kanonik pada Gambar 17.5.](fig/c_lokal.png){width=90%}

::: {.contoh}
**Contoh 17.31 · Memutar dua orbital: dari s dan p ke hibrida**

Misalkan dua orbital terisi ortonormal adalah orbital s dan p$_z$ pada satu atom. Putar keduanya dengan sudut 45°: $h_\pm = (s \pm p_z)/\sqrt2$. Tunjukkan bahwa jumlah rapat kedua orbital tidak berubah, dan tentukan ke mana pusat muatan $h_\pm$ bergeser.

**Penyelesaian.** $|h_+|^2 + |h_-|^2 = \tfrac12[(s + p_z)^2 + (s - p_z)^2] = s^2 + p_z^2$: rapat total sama. Pusat muatan $\langle h_\pm|z|h_\pm\rangle = \tfrac12[\langle s|z|s\rangle + \langle p_z|z|p_z\rangle \pm 2\langle s|z|p_z\rangle] = \pm\langle s|z|p_z\rangle$, karena $\langle s|z|s\rangle = \langle p_z|z|p_z\rangle = 0$ oleh paritas. Kedua hibrida bergeser ke arah $+z$ dan $-z$ sejauh $|\langle s|z|p_z\rangle|$.

**Memahami hasil.** Inilah hibridisasi sp (subbab 12.3) dilihat sebagai lokalisasi: rotasi memusatkan setiap orbital ke satu arah tanpa mengubah fisika apa pun. Kriteria Boys memilih sudut rotasi yang menjauhkan pusat-pusat muatan sejauh mungkin, sehingga untuk dua orbital ini ia memilih tepat 45°.
:::

::: {.contoh}
**Contoh 17.32 · Orbital terlokalisasi air**

Lokalisasi Boys orbital terisi H₂O/STO-3G (program pendamping) memberi: satu orbital inti O 1s; dua orbital ikatan dengan pusat muatan di $(0, \pm0{,}453, 0{,}357)$ Å; dua orbital pasangan bebas dengan pusat di $(\pm0{,}264, 0, -0{,}154)$ Å, yaitu di bidang tegak lurus bidang molekul, di belakang oksigen. Hitung (a) jarak pusat ikatan dari O sebagai pecahan panjang ikatan, (b) sudut antara kedua pusat pasangan bebas, (c) sudut antara kedua pusat ikatan.

**Penyelesaian.** (a) $\sqrt{0{,}453^2 + 0{,}357^2} = 0{,}577$ Å, yaitu 60% dari 0,957 Å. (b) Setengah sudutnya $\arctan(0{,}264/0{,}154) = 59{,}7°$, sehingga sudutnya 119,5°. (c) $2\arctan(0{,}453/0{,}357) = 103{,}6°$.

**Memahami hasil.** Pusat ikatan terletak lebih dekat ke hidrogen daripada ke titik tengah ikatan? Tidak: 60% dari O berarti 40% dari H, sehingga orbital ikatan sedikit condong ke arah hidrogen dalam basis minimal ini. Dengan 6-31G, pusatnya bergeser ke 0,524 Å (55%) dan populasinya pada O naik dari 0,58 ke 0,68: ikatan menjadi lebih polar ke arah oksigen, sesuai keelektronegatifan. Pasangan bebas membentuk sudut sekitar 120°, lebih besar daripada sudut ikatan, sesuai dengan aturan VSEPR bahwa pasangan bebas menempati ruang lebih besar (subbab 12.11). Gambaran "dua pasangan bebas setara" adalah lokalisasi; gambaran kanonik ($1b_1$ dan $3a_1$, berbeda energi 1,7 eV) adalah yang teramati dalam spektrum fotoelektron. Keduanya benar untuk pertanyaan yang berbeda.
:::

::: {.contoh}
**Contoh 17.33 · Metana: satu energi, dua gambaran**

Untuk CH₄/STO-3G, orbital kanonik valensi adalah satu $2a_1$ ($-0{,}910\ E_h$) dan tiga $1t_2$ ($-0{,}519\ E_h$). Lokalisasi Boys memberi empat orbital setara, masing-masing berpusat pada garis C–H, 0,743 Å dari karbon (panjang ikatan 1,087 Å). Hitung jumlah energi orbital valensi untuk kedua set, dengan memakai unsur diagonal matriks Fock untuk orbital terlokalisasi. Apakah energi total berubah?

**Penyelesaian.** Kanonik: $2(-0{,}910) + 6(-0{,}519) = -4{,}934\ E_h$. Jejak matriks Fock dalam subruang orbital terisi tidak berubah oleh rotasi uniter, sehingga keempat LMO masing-masing mempunyai $\langle\psi_i'|\hat f|\psi_i'\rangle = \tfrac14(-0{,}910 - 3 \times 0{,}519) = -0{,}617\ E_h$, dan jumlahnya tetap $-4{,}934\ E_h$. Energi total tidak berubah ($-39{,}7268\ E_h$).

**Memahami hasil.** Keempat LMO mempunyai "energi" sama, $-0{,}617\ E_h$ (16,8 eV), tetapi itu bukan energi ionisasi, karena LMO bukan fungsi eigen operator Fock: matriks Fock dalam basis LMO mempunyai unsur di luar diagonal sebesar sekitar $0{,}1\ E_h$ yang mengopel ikatan-ikatan. Kopling inilah yang memecah empat ionisasi "ikatan C–H" menjadi pita $t_2$ dan $a_1$ yang teramati. Pusat LMO terletak 68% dari karbon, sedikit condong ke hidrogen dalam basis minimal, mirip dengan air.
:::

::: {.kuis}
**Kuis cepat 17.8**

Bila orbital terisi diganti dengan orbital terlokalisasi, apa yang terjadi pada energi total, momen dipol, dan energi orbital? Mengapa metode korelasi lokal dapat mengabaikan pasangan LMO yang berjauhan?
:::

## 17.9 Optimasi geometri, frekuensi getaran, sifat termodinamika

### Mencari minimum

Geometri molekul adalah minimum permukaan energi potensial $E(\mathbf q)$. Untuk menemukannya, program memerlukan **gradien** $\mathbf g = \partial E/\partial\mathbf q$, yang untuk HF, DFT, MP2, dan CCSD dapat dihitung secara analitis dengan biaya sebanding dengan satu perhitungan energi (Pulay, 1969). Gradien analitis adalah salah satu kemajuan terpenting kimia komputasi: tanpanya, setiap komponen gradien memerlukan dua perhitungan energi tambahan (beda hingga), dan molekul dengan $3N$ koordinat memerlukan $6N$ perhitungan per langkah.

Di dekat minimum, energi dapat diuraikan sampai orde kedua: $E(\mathbf q + \Delta\mathbf q) \approx E + \mathbf g^\text{T}\Delta\mathbf q + \tfrac12\Delta\mathbf q^\text{T}\mathbf H\Delta\mathbf q$, dengan $\mathbf H$ matriks Hessian (turunan kedua). Gradien uraian ini nol bila

$$
\Delta\mathbf q = -\mathbf H^{-1}\mathbf g . \qquad \text{(17.30)}
$$

Inilah **langkah Newton–Raphson**: untuk permukaan kuadratik ia langsung mencapai minimum, dan untuk permukaan nyata ia berkonvergensi kuadratik bila sudah dekat. Menghitung Hessian tepat pada setiap langkah mahal, sehingga program memakai metode **kuasi-Newton** (BFGS): Hessian awal ditebak (misalnya dari medan gaya sederhana), lalu diperbarui pada setiap langkah memakai perubahan gradien. Optimasi dilakukan dalam **koordinat internal** (panjang ikatan, sudut, torsi) yang jauh lebih "tidak terkopel" daripada koordinat Kartesius, sehingga biasanya selesai dalam 5–20 langkah. Kriteria konvergensi yang lazim adalah gaya maksimum di bawah sekitar $4{,}5 \times 10^{-4}\ E_h$/bohr dan perpindahan maksimum di bawah sekitar $1{,}8 \times 10^{-3}$ bohr.

Hartree–Fock dengan basis yang memadai memberi panjang ikatan yang sedikit terlalu pendek (sekitar 0,01–0,02 Å untuk ikatan dengan atom elektronegatif), karena tanpa korelasi, pencampuran konfigurasi antiikatan yang melemahkan ikatan hilang. MP2 dan DFT hibrida memberi panjang ikatan dengan galat sekitar 0,01 Å, dan sudut ikatan dalam 1–2°.

### Frekuensi harmonik

Di minimum, $\mathbf g = 0$ dan energi kuadratik dalam perpindahan. Gerak inti menjadi kumpulan osilator harmonik (subbab 5.11): Hessian dalam koordinat Kartesius berbobot massa, $\tilde H_{ij} = H_{ij}/\sqrt{m_im_j}$, didiagonalkan, dan setiap nilai eigen $\lambda_k$ memberi frekuensi sudut $\omega_k = \sqrt{\lambda_k}$, dengan vektor eigen sebagai **mode normal**. Dari $3N$ nilai eigen, enam (lima untuk molekul linear) bersesuaian dengan translasi dan rotasi dan seharusnya nol; dalam praktik nilainya kecil tetapi tidak nol karena geometri tidak tepat di minimum dan karena galat numerik, dan program memproyeksikannya keluar sebelum diagonalisasi. Bilangan gelombang

$$
\tilde\nu_k = \frac{1}{2\pi c}\sqrt{\lambda_k} . \qquad \text{(17.31)}
$$

Bila gradien analitis tidak tersedia, Hessian dapat dihitung dari energi saja dengan beda hingga, $H_{ij} \approx [E(+i, +j) - E(+i, -j) - E(-i, +j) + E(-i, -j)]/4h^2$, dengan $h$ sekitar 0,005 bohr. Untuk H₂O (9 koordinat) itu berarti 162 perhitungan energi; program pendamping memakai cara ini. Langkah terakhirnya, dari Hessian ke bilangan gelombang, hanya beberapa baris:

```python
import numpy as np
def frekuensi(hess, massa):        # hess: 3N x 3N dalam E_h/bohr^2; massa dalam u
    m = np.repeat(massa, 3)
    lam = np.linalg.eigvalsh(hess / np.sqrt(np.outer(m, m)))
    konv = 4.3597447e-18 / (5.29177211e-11**2 * 1.66053907e-27)    # ke s^-2
    return np.sign(lam) * np.sqrt(np.abs(lam) * konv) / (2 * np.pi * 2.99792458e10)
```

Nilai eigen negatif dikembalikan sebagai bilangan negatif, cara lazim program mencetak frekuensi imajiner.

Intensitas inframerah setiap mode sebanding dengan kuadrat turunan momen dipol terhadap koordinat normalnya (subbab 5.8 dan 15.5), dan aktivitas Raman dengan turunan polarisabilitas; keduanya dihitung bersama frekuensi.

Frekuensi harmonik hasil hitungan berbeda dari pita yang teramati karena dua alasan: (1) pita teramati adalah transisi **fundamental** $0 \to 1$ yang diturunkan oleh anharmonisitas (subbab 5.9), dan (2) metode elektronik mempunyai galat sistematis dalam kelengkungan permukaan. HF melebih-lebihkan frekuensi sekitar 10% (kurva potensial HF terlalu curam karena ikatan terlalu kuat). Keduanya cukup sistematis sehingga dapat dikoreksi dengan **faktor skala** empiris: sekitar 0,895 untuk HF/6-31G*, 0,96 untuk B3LYP/6-31G*, dan 0,95 untuk MP2. Faktor skala untuk ZPE sedikit berbeda dari faktor untuk fundamental.

### Dari frekuensi ke termodinamika

Dengan geometri dan frekuensi, besaran termodinamika gas ideal dihitung dari fungsi partisi molekul, yang dalam pendekatan **gas ideal–rotor tegar–osilator harmonik** adalah hasil kali bagian translasi, rotasi, getaran, dan elektronik (Fisika Umum dan subbab 6.11). Bagian-bagian terpenting:

- **Energi titik nol**: $E_\text{ZPE} = \tfrac12\sum_kh\nu_k$.
- **Getaran termal**: $E_\text{vib}(T) = R\sum_k\frac{\theta_k}{e^{\theta_k/T} - 1}$ dengan $\theta_k = h\nu_k/k_B$, dan $S_\text{vib} = R\sum_k\left[\frac{\theta_k/T}{e^{\theta_k/T} - 1} - \ln(1 - e^{-\theta_k/T})\right]$.
- **Translasi dan rotasi**: masing-masing $\tfrac32RT$ untuk molekul tak linear; entropi translasi dari persamaan Sackur–Tetrode, entropi rotasi dari momen inersia dan bilangan simetri $\sigma$.
- **Entalpi dan energi bebas**: $H = E_\text{el} + E_\text{ZPE} + E_\text{vib} + E_\text{rot} + E_\text{trans} + RT$ dan $G = H - TS$.

Program mencetak semua suku ini. Getaran berfrekuensi rendah (di bawah sekitar 100 cm⁻¹, misalnya rotasi gugus metil atau gerak antarmolekul dalam kompleks lemah) adalah titik lemah pendekatan harmonik: entropinya terlalu besar. Koreksi "kuasi-RRHO" memperlakukan mode semacam itu seperti rotor bebas.

![Gambar 17.7 Tiga mode normal H₂O dari Hessian HF/6-31G* (program pendamping): tekuk (1826 cm⁻¹), ulur simetris (4071 cm⁻¹), dan ulur antisimetris (4190 cm⁻¹). Panah menunjukkan arah perpindahan atom (diperbesar); pergeseran oksigen kecil karena massanya besar.](fig/c_frek.png){width=88%}

::: {.contoh}
**Contoh 17.34 · Satu langkah Newton untuk H₂**

Dengan HF/STO-3G pada $R = 1{,}4$ bohr, beda hingga memberi $dE/dR = 0{,}02845\ E_h$/bohr dan $d^2E/dR^2 = 0{,}4820\ E_h$/bohr². Lakukan satu langkah Newton dan bandingkan dengan minimum sebenarnya ($R_e = 1{,}3459$ bohr, $E = -1{,}117506\ E_h$).

**Penyelesaian.** $\Delta R = -0{,}02845/0{,}4820 = -0{,}0590$ bohr, sehingga $R = 1{,}3410$ bohr. Energi di sana $-1{,}117499\ E_h$, hanya $7 \times 10^{-6}\ E_h$ (0,02 kJ/mol) di atas minimum.

**Memahami hasil.** Satu langkah dari titik yang berjarak 0,054 bohr sudah menghasilkan energi yang praktis minimum; sisa galat posisi 0,005 bohr berasal dari anharmonisitas (kelengkungan di 1,4 bohr lebih kecil daripada di minimum, 0,573). Langkah kedua akan memberi $R$ yang benar sampai empat desimal. Inilah konvergensi kuadratik.
:::

::: {.contoh}
**Contoh 17.35 · Geometri air dari berbagai metode**

Optimasi H₂O memberi: HF/STO-3G $r = 0{,}989$ Å, $\angle = 100{,}0°$; HF/6-31G* $r = 0{,}947$ Å, $\angle = 105{,}5°$. Geometri percobaan (setimbang, $r_e$): 0,9572 Å dan 104,52°. Hitung galatnya dan jelaskan arah galat masing-masing.

**Penyelesaian.** STO-3G: $+0{,}032$ Å, $-4{,}5°$. 6-31G*: $-0{,}010$ Å, $+1{,}0°$.

**Memahami hasil.** Basis minimal membuat ikatan terlalu panjang dan sudut terlalu sempit: tanpa fungsi d, oksigen tidak dapat "membengkokkan" pasangan elektron bebasnya ke belakang, sehingga tolakan pasangan bebas mendorong ikatan O–H berdekatan. Dengan polarisasi, galat HF menjadi pola khasnya: ikatan sedikit terlalu pendek. Perbandingan yang adil memakai $r_e$ (dasar kurva potensial), bukan $r_0$ dari spektroskopi rotasi keadaan dasar (subbab 6.12).
:::

::: {.contoh}
**Contoh 17.36 · Frekuensi air dan faktor skala**

HF/6-31G* memberi frekuensi harmonik H₂O 1826, 4071, dan 4190 cm⁻¹ (Hessian beda hingga dari program pendamping). Frekuensi harmonik percobaan 1648, 3832, 3943 cm⁻¹; fundamental teramati 1595, 3657, 3756 cm⁻¹. Hitung perbandingan dengan harmonik percobaan, lalu kalikan frekuensi hitungan dengan faktor skala 0,8953 dan bandingkan dengan fundamental.

**Penyelesaian.** Perbandingan dengan harmonik percobaan: 1,108; 1,062; 1,063. Setelah diskalakan: 1635, 3645, 3751 cm⁻¹, dengan selisih $+40$, $-12$, $-5$ cm⁻¹ terhadap fundamental.

**Memahami hasil.** HF melebih-lebihkan frekuensi harmonik 6–11%; faktor skala tunggal menyerap galat elektronik dan anharmonisitas sekaligus, sehingga frekuensi ulur jatuh dalam beberapa cm⁻¹ dari pita teramati. Mode tekuk meleset lebih banyak karena galat HF untuk sudut berbeda dari galat untuk ikatan. Untuk penetapan spektrum, ketelitian puluhan cm⁻¹ ini sudah sangat berguna: ia cukup untuk membedakan pita C=O, C=C, dan C–H dalam spektrum IR molekul organik.
:::

::: {.contoh}
**Contoh 17.37 · Termokimia air dari perhitungan**

Dari geometri dan frekuensi HF/6-31G* H₂O, program termokimia pendamping (gas ideal–rotor tegar–osilator harmonik, 298,15 K, 1 bar) memberi: $E_\text{ZPE} = 60{,}3$ kJ/mol tanpa skala (55,1 kJ/mol dengan faktor skala ZPE 0,9135), $H(298) - H(0) = 9{,}92$ kJ/mol, $S^\circ = 188{,}3$ J mol⁻¹ K⁻¹ (translasi 144,9; rotasi 43,4; getaran hampir nol), $C_p = 33{,}4$ J mol⁻¹ K⁻¹. Data percobaan: $S^\circ = 188{,}8$ J mol⁻¹ K⁻¹, $H(298) - H(0) = 9{,}905$ kJ/mol, $C_p = 33{,}6$ J mol⁻¹ K⁻¹, ZPE harmonik dari frekuensi percobaan 56,4 kJ/mol. Mengapa entropi dan entalpi termal begitu teliti, sedangkan ZPE meleset 4 kJ/mol tanpa skala?

**Penyelesaian.** Entropi dan entalpi termal air didominasi translasi dan rotasi, yang hanya bergantung pada massa dan momen inersia (yaitu geometri), sedangkan getaran air terlalu tinggi untuk tereksitasi pada 298 K ($\theta_\text{vib} > 2600$ K), sehingga galat frekuensi hampir tidak berpengaruh. ZPE sebanding langsung dengan frekuensi, sehingga mewarisi galat 7% HF.

**Memahami hasil.** Untuk molekul kecil dan kaku, termokimia statistik hampir tepat; galat terbesar ada di energi elektronik dan ZPE. Untuk molekul besar dan lentur, situasinya terbalik: banyak getaran berfrekuensi rendah menyumbang entropi besar dan peka terhadap pendekatan harmonik, dan banyaknya konformer menambah entropi konformasi. Di sana termokimia statistik menjadi sumber galat utama dalam energi bebas.
:::

::: {.kuis}
**Kuis cepat 17.9**

Mengapa enam frekuensi seharusnya nol dalam perhitungan frekuensi molekul tak linear? Mengapa frekuensi HF dikalikan faktor sekitar 0,9 sebelum dibandingkan dengan spektrum IR?
:::
