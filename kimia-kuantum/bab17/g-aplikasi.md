## 17.15 Interaksi nonkovalen, efek pelarut, efek relativistik

### Interaksi antarmolekul

Ikatan hidrogen, tumpukan π, interaksi van der Waals, dan pengikatan obat pada protein melibatkan energi 1–50 kJ/mol, jauh lebih kecil daripada ikatan kovalen, tetapi menentukan sifat cairan, struktur DNA, dan pengenalan molekul. Energi interaksi dapat diuraikan (misalnya dengan teori perturbasi teradaptasi simetri, SAPT) menjadi empat bagian: **elektrostatik** (interaksi muatan, dipol, dan multipol permanen), **induksi** (polarisasi satu molekul oleh medan molekul lain), **tolakan pertukaran** (asas Pauli ketika awan elektron bertumpang tindih), dan **dispersi** (tarikan antara fluktuasi sesaat awan elektron). Tiga bagian pertama sudah ada dalam HF; dispersi murni efek korelasi.

Dispersi London sebanding dengan $-C_6/R^6$ pada jarak jauh. Dengan model osilator Drude, London (1930) menaksir

$$
C_6 \approx \frac32\,\frac{I_AI_B}{I_A + I_B}\,\alpha_A\alpha_B , \qquad \text{(17.e52)}
$$

dengan $I$ energi ionisasi dan $\alpha$ polarisabilitas (satuan atom). Karena dispersi berasal dari korelasi elektron yang berjauhan, ia tidak ada dalam HF dan tidak ada dalam fungsional LDA, GGA, maupun hibrida biasa, yang hanya "melihat" kerapatan di sekitar setiap titik. Akibatnya DFT tanpa koreksi meramalkan bahwa dimer benzena bertumpuk dan dimer gas mulia hampir tidak terikat, dan meremehkan pengikatan ligan pada protein secara sistematis. Jalan keluar yang paling banyak dipakai adalah koreksi empiris **DFT-D** (Grimme):

$$
E_\text{disp} = -\sum_{A<B}\sum_{n = 6, 8}s_n\frac{C_n^{AB}}{R_{AB}^n}\,f_\text{redam}(R_{AB}) , \qquad \text{(17.e53)}
$$

dengan koefisien $C_6$ yang bergantung pada lingkungan atom (D3, D4) dan fungsi peredam yang mematikan koreksi pada jarak pendek, tempat fungsional sudah memuat korelasi. Alternatif lain adalah fungsional nonlokal (VV10) atau metode korelasi eksplisit. Untuk interaksi nonkovalen, CCSD(T)/CBS adalah acuan baku, dan himpunan uji seperti S22 dan S66 dipakai untuk menilai metode murah. Dua hal teknis wajib diperhatikan: basis dengan fungsi difus dan koreksi BSSE (subbab 17.5).

### Efek pelarut

Sebagian besar kimia terjadi dalam larutan, sedangkan perhitungan baku menggambarkan molekul terisolasi dalam fase gas. Ada dua pendekatan.

**Pelarut eksplisit**: molekul pelarut dimasukkan sebagai atom-atom, biasanya ribuan, dengan mekanika molekul atau QM/MM (subbab 17.17), lalu dirata-ratakan atas banyak konfigurasi dengan dinamika molekul atau Monte Carlo. Teliti tetapi mahal.

**Pelarut implisit** (kontinum): pelarut diganti dengan dielektrik kontinu berpermitivitas $\varepsilon_r$ yang mengelilingi rongga berbentuk molekul. Rapat muatan zat terlarut mempolarisasi dielektrik, yang dinyatakan sebagai muatan permukaan pada dinding rongga; muatan itu kemudian dimasukkan ke dalam Hamiltonian zat terlarut, dan semuanya diselesaikan secara swakonsisten (**medan reaksi swakonsisten**, SCRF). Model populer: PCM, COSMO, dan SMD (yang menambahkan suku nonelektrostatik untuk kavitasi, dispersi, dan struktur pelarut). Bentuk paling sederhana model kontinum adalah **persamaan Born** untuk ion bola bermuatan $ze$ berjari-jari $a$:

$$
\Delta G_\text{solv} = -\frac{N_Az^2e^2}{8\pi\varepsilon_0a}\left(1 - \frac1{\varepsilon_r}\right) . \qquad \text{(17.e54)}
$$

Model kontinum menangkap sebagian besar energi solvasi elektrostatik dengan biaya hampir nol, tetapi tidak menangkap interaksi spesifik seperti ikatan hidrogen terarah. Untuk ion dan anion kecil, praktik yang baik adalah model **kluster–kontinum**: beberapa molekul pelarut di kulit pertama diperlakukan eksplisit, sisanya kontinum.

### Efek relativistik

Persamaan Schrödinger bersifat nonrelativistik. Untuk elektron 1s dengan muatan inti $Z$, kecepatan rata-ratanya dalam satuan atom sekitar $Z$, sehingga $v/c \approx Z/137$ (subbab 7.10). Untuk emas ($Z = 79$), $v/c \approx 0{,}58$, dan massa relativistik elektron naik dengan faktor $\gamma = 1/\sqrt{1 - v^2/c^2}$. Karena jari-jari orbit berbanding terbalik dengan massa ($a_0 = \hbar^2/me^2$), orbital 1s menyusut. Orbital s dan p$_{1/2}$ yang lebih luar juga menyusut, karena harus tetap ortogonal terhadap orbital dalam dan karena mempunyai rapat di dekat inti. Sebaliknya, orbital d dan f mengembang dan naik energinya, karena lebih terperisai oleh orbital s dan p yang menyusut. Ditambah kopling spin–orbit (subbab 9.13), akibat-akibat ini menerangkan sejumlah keanehan kimia unsur berat:

- **Warna emas**: penyusutan 6s dan pengembangan 5d mempersempit celah 5d → 6s sehingga serapan bergeser dari ultraungu (seperti perak) ke biru; emas memantulkan kuning.
- **Raksa cair**: pasangan 6s² raksa sangat stabil dan enggan berikatan, sehingga ikatan logam Hg–Hg lemah.
- **Aki timbal**: sekitar 80% tegangan aki timbal–asam berasal dari efek relativistik pada stabilitas PbO₂.
- **Efek pasangan inert** pada Tl, Pb, Bi dan kecenderungan bilangan oksidasi rendahnya.
- **Aurofilisitas**: interaksi Au(I)···Au(I) yang kuat dalam senyawa emas.

Dalam praktik, efek relativistik skalar dimasukkan dengan potensial inti efektif (ECP) yang dicocokkan dengan perhitungan atom relativistik, atau dengan Hamiltonian Douglas–Kroll–Hess (DKH) dan ZORA. Untuk spin–orbit diperlukan perlakuan dua komponen atau empat komponen (persamaan Dirac).

::: {.contoh}
**Contoh 17.c47 · Koefisien dispersi argon**

Taksir $C_6$ untuk Ar–Ar dengan (17.e52), memakai $\alpha = 11{,}08$ satuan atom dan $I = 15{,}76$ eV. Hitung energi dispersi pada $R = 3{,}76$ Å dalam cm⁻¹ dan bandingkan dengan nilai teliti $C_6 = 64{,}3$ satuan atom serta kedalaman sumur dimer Ar₂ (99,5 cm⁻¹).

**Penyelesaian.** Untuk atom sejenis $C_6 = \tfrac34I\alpha^2$. $I = 15{,}76/27{,}211 = 0{,}5792\ E_h$; $C_6 = 0{,}75(0{,}5792)(11{,}08)^2 = 53{,}3$ satuan atom. $R = 3{,}76$ Å $= 7{,}105$ bohr; $R^6 = 1{,}288 \times 10^5$; $E = -53{,}3/1{,}288 \times 10^5 = -4{,}14 \times 10^{-4}\ E_h = -91$ cm⁻¹.

**Memahami hasil.** Rumus London meremehkan $C_6$ sekitar 17%, galat yang lazim karena satu energi eksitasi rata-rata mewakili seluruh spektrum. Energi dispersi pada jarak setimbang sebanding dengan kedalaman sumur; pada jarak itu tolakan pertukaran dan suku $C_8$, $C_{10}$ saling mengimbangi secara kasar. HF meramalkan bahwa dimer Ar tidak terikat sama sekali; seluruh ikatannya adalah korelasi.
:::

::: {.contoh}
**Contoh 17.c48 · Persamaan Born untuk ion natrium**

Hitung energi bebas hidrasi Na⁺ dengan persamaan Born, memakai jari-jari Born 1,68 Å (jari-jari ion ditambah koreksi empiris) dan $\varepsilon_r = 78{,}4$. Bandingkan dengan jari-jari ion Pauling 1,02 Å.

**Penyelesaian.** $\dfrac{N_Ae^2}{8\pi\varepsilon_0} = \dfrac{(6{,}022 \times 10^{23})(1{,}602 \times 10^{-19})^2}{8\pi(8{,}854 \times 10^{-12})} = 6{,}946 \times 10^{-5}$ J m/mol. Dengan $a = 1{,}68 \times 10^{-10}$ m: $\Delta G = -(6{,}946 \times 10^{-5}/1{,}68 \times 10^{-10})(1 - 1/78{,}4) = -408$ kJ/mol. Dengan $a = 1{,}02$ Å: $-672$ kJ/mol.

**Memahami hasil.** Nilai percobaan sekitar $-365$ sampai $-410$ kJ/mol, bergantung pada skala acuan yang dipakai untuk energi hidrasi proton. Hasilnya sangat peka terhadap jari-jari rongga; itulah sebabnya model kontinum modern menentukan rongga dari jari-jari atom yang dikalibrasi terhadap data percobaan. Energi hidrasi ratusan kJ/mol jauh melebihi energi kebanyakan reaksi, sehingga untuk reaksi yang melibatkan ion dalam air, perlakuan pelarut sama pentingnya dengan metode elektronik.
:::

::: {.contoh}
**Contoh 17.c49 · Ketelitian pKa**

pKa dihitung dari siklus termodinamika: $\text{p}K_a = \Delta G_\text{deprot}/(RT\ln10)$, dengan $\Delta G_\text{deprot}$ energi bebas deprotonasi dalam larutan. Berapa galat $\Delta G$ yang setara dengan galat 1 satuan pKa pada 298 K? Bila energi solvasi anion meleset 10 kJ/mol, berapa galat pKa?

**Penyelesaian.** $RT\ln10 = (8{,}314)(298{,}15)(2{,}3026) = 5{,}71$ kJ/mol per satuan pKa. Galat 10 kJ/mol setara dengan $10/5{,}71 = 1{,}8$ satuan pKa.

**Memahami hasil.** Meramalkan pKa dalam batas satu satuan memerlukan ketelitian energi bebas sekitar 6 kJ/mol, lebih ketat daripada ketelitian kimia biasa, padahal energi solvasi anion sendiri ratusan kJ/mol dan galat model kontinum untuk anion sering 10–20 kJ/mol. Itulah sebabnya perhitungan pKa mutlak sulit, dan dalam praktik orang menghitung pKa relatif terhadap asam acuan yang strukturnya mirip, agar galat solvasi meniadakan diri.
:::

::: {.contoh}
**Contoh 17.c50 · Seberapa besar efek relativistik?**

Taksir $v/c$, faktor $\gamma$, dan penyusutan relatif jari-jari orbital 1s ($1 - 1/\gamma$) untuk Cu ($Z = 29$), Ag (47), Au (79), dan Hg (80), dengan $v/c \approx Z/137{,}036$.

**Penyelesaian.**

| Unsur | $v/c$ | $\gamma$ | Penyusutan 1s |
|---|---|---|---|
| Cu | 0,212 | 1,023 | 2,3% |
| Ag | 0,343 | 1,065 | 6,1% |
| Au | 0,576 | 1,224 | 18,3% |
| Hg | 0,584 | 1,232 | 18,8% |

**Memahami hasil.** Efek relativistik tumbuh jauh lebih cepat daripada linear dengan $Z$, sehingga lompatan dari perak ke emas sangat besar. Penyusutan orbital 6s emas yang sebenarnya, dari perhitungan Dirac–Fock, sekitar 17%, sebanding dengan taksiran kasar ini, dan merupakan yang terbesar di antara semua unsur sampai periode keenam; Pyykkö menyebut daerah sekitar emas sebagai "maksimum relativistik" tabel periodik. Itulah sebabnya kimia emas sangat berbeda dari kimia perak, meskipun keduanya segolongan.
:::

::: {.kuis}
**Kuis cepat 17.15**

Mengapa fungsional B3LYP tanpa koreksi tidak dapat menggambarkan ikatan dalam dimer argon? Menurut persamaan Born, mengapa ion kecil lebih kuat terhidrasi daripada ion besar?
:::

## 17.16 Reaksi kimia dan keadaan transisi

### Titik stasioner pada permukaan energi

Pada permukaan energi potensial $E(\mathbf q)$, dengan $\mathbf q$ koordinat inti, titik **stasioner** adalah titik dengan gradien nol, $\partial E/\partial q_i = 0$. Jenisnya ditentukan oleh nilai eigen matriks Hessian $\mathbf H_{ij} = \partial^2E/\partial q_i\partial q_j$ (setelah gerak translasi dan rotasi dibuang):

- semua nilai eigen positif: **minimum** (reaktan, produk, zat antara);
- tepat satu nilai eigen negatif: **titik pelana orde pertama**, yaitu **keadaan transisi** (TS);
- dua atau lebih nilai eigen negatif: titik pelana orde lebih tinggi, yang secara kimia tidak bermakna sebagai keadaan transisi.

Keadaan transisi adalah titik tertinggi pada jalur energi terendah antara dua minimum: maksimum sepanjang satu arah (koordinat reaksi) dan minimum ke semua arah lain. Nilai eigen negatif bersesuaian dengan **frekuensi imajiner** $i\nu^\ddagger$ (subbab 3.12), dan vektor eigennya menunjukkan gerak atom yang membawa sistem dari reaktan ke produk.

Menemukan minimum mudah: ikuti gradien turun. Menemukan titik pelana lebih sulit, karena kita harus naik di satu arah sambil turun di arah lain. Metode yang dipakai antara lain **mengikuti vektor eigen** (*eigenvector following*, langkah Newton yang dimodifikasi agar naik sepanjang vektor eigen terendah), metode **interpolasi** (QST2/QST3) yang memulai dari struktur reaktan dan produk, dan metode **pita elastis bertakik** (NEB) yang mengoptimasi seluruh rangkaian struktur di sepanjang jalur. Setelah TS ditemukan, dua pemeriksaan wajib: (1) analisis frekuensi harus menunjukkan tepat satu frekuensi imajiner, dan (2) perhitungan **koordinat reaksi intrinsik** (IRC), yang menuruni lereng dari TS ke kedua arah dalam koordinat berbobot massa, harus berakhir di reaktan dan produk yang dimaksud.

![Gambar 17.g09 Permukaan model Müller–Brown, permukaan uji baku untuk algoritme pencarian titik stasioner. Tiga minimum (lingkaran) dihubungkan oleh dua titik pelana (segitiga); garis jingga adalah jalur energi minimum yang diperoleh dengan menuruni gradien dari setiap titik pelana ke kedua arah.](fig/c_pes.png){width=74%}

### Teori keadaan transisi

Dari energi TS dan reaktan, laju reaksi dihitung dengan **teori keadaan transisi** (Eyring, Evans, Polanyi, 1935):

$$
k = \kappa\,\frac{k_BT}{h}\,e^{-\Delta G^\ddagger/RT} , \qquad \text{(17.e55)}
$$

dengan $\Delta G^\ddagger$ energi bebas pengaktifan (dihitung dari energi elektronik, ZPE, dan suku termal seperti di subbab 17.9, dengan frekuensi imajiner dikeluarkan dari fungsi partisi getaran TS) dan $\kappa$ koefisien transmisi yang memuat penerobosan dan penyeberangan balik. Untuk penerobosan, koreksi Wigner orde terendah (subbab 3.12) adalah

$$
\kappa_\text{W} = 1 + \frac{1}{24}\left(\frac{h|\nu^\ddagger|}{k_BT}\right)^2 , \qquad \text{(17.e56)}
$$

yang hanya berlaku bila koreksinya kecil; untuk transfer atom hidrogen dengan frekuensi imajiner besar diperlukan model Eckart atau penerobosan semiklasik multidimensi.

Ketergantungan eksponensial (17.e55) menetapkan tuntutan ketelitian: galat 4,2 kJ/mol (1 kkal/mol) pada penghalang mengubah laju dengan faktor $e^{4184/RT} = 5{,}4$ pada 298 K. Penghalang reaksi juga merupakan besaran yang paling sulit bagi banyak metode, karena keadaan transisi sering mempunyai ikatan yang setengah putus dan setengah terbentuk, tempat korelasi statik dan galat delokalisasi DFT paling berpengaruh. HF umumnya melebih-lebihkan penghalang (korelasi lebih penting di TS daripada di reaktan), sedangkan fungsional GGA sering meremehkannya.

::: {.contoh}
**Contoh 17.c51 · Titik stasioner permukaan Müller–Brown**

Permukaan Müller–Brown $V(x, y) = \sum_{k=1}^4A_k\exp[a_k(x - x_k)^2 + b_k(x - x_k)(y - y_k) + c_k(y - y_k)^2]$ dengan parameter baku mempunyai lima titik stasioner. Penyelesaian numerik $\nabla V = 0$ (dengan `scipy.optimize.root`) dan diagonalisasi Hessian memberi:

| Titik | $(x, y)$ | $V$ | Nilai eigen Hessian |
|---|---|---|---|
| A | $(-0{,}558;\ 1{,}442)$ | $-146{,}70$ | 410; 4068 |
| B | $(0{,}623;\ 0{,}028)$ | $-108{,}17$ | 544; 3005 |
| C | $(-0{,}050;\ 0{,}467)$ | $-80{,}77$ | 221; 1479 |
| S1 | $(-0{,}822;\ 0{,}624)$ | $-40{,}66$ | $-751$; 490 |
| S2 | $(0{,}212;\ 0{,}293)$ | $-72{,}25$ | $-735$; 511 |

Golongkan setiap titik dan hitung penghalang untuk A → C dan C → B.

**Penyelesaian.** A, B, C mempunyai dua nilai eigen positif: minimum. S1 dan S2 masing-masing satu nilai eigen negatif: titik pelana orde pertama. Jalur A → C melewati S1: penghalang $-40{,}66 - (-146{,}70) = 106{,}0$. Jalur C → B melewati S2: penghalang $-72{,}25 - (-80{,}77) = 8{,}5$ (satuan permukaan model).

**Memahami hasil.** Zat antara C berada dalam sumur dangkal: penghalang keluarnya ke B hanya 8,5, jauh lebih kecil daripada penghalang masuk dari A. Pola semacam ini (zat antara reaktif yang berumur pendek) lazim dalam mekanisme reaksi nyata. Perhatikan juga bahwa jalur energi minimum melengkung tajam (Gambar 17.g09): koordinat reaksi bukan garis lurus antara reaktan dan produk, sehingga interpolasi linear antara struktur reaktan dan produk tidak cukup untuk menemukan TS.
:::

::: {.contoh}
**Contoh 17.c52 · Dari penghalang ke waktu paruh**

Dengan (17.e55) dan $\kappa = 1$, hitung tetapan laju orde pertama dan waktu paruh pada 298 K untuk $\Delta G^\ddagger$ = 40, 60, 80, dan 100 kJ/mol.

**Penyelesaian.** $k_BT/h = 6{,}21 \times 10^{12}$ s⁻¹. Hasilnya:

| $\Delta G^\ddagger$ (kJ/mol) | $k$ (s⁻¹) | $t_{1/2}$ |
|---|---|---|
| 40 | $6{,}1 \times 10^5$ | 1,1 μs |
| 60 | 191 | 3,6 ms |
| 80 | 0,060 | 12 s |
| 100 | $1{,}9 \times 10^{-5}$ | 10 jam |

**Memahami hasil.** Setiap tambahan 20 kJ/mol memperlambat reaksi sekitar 3000 kali. Reaksi yang "berjalan pada suhu kamar dalam waktu wajar" mempunyai penghalang sekitar 80–100 kJ/mol. Galat DFT khas sebesar 10 kJ/mol berarti galat laju sekitar 50 kali, cukup untuk membedakan reaksi cepat dan lambat, tetapi tidak cukup untuk meramalkan perbandingan produk yang halus. Perbandingan produk ditentukan oleh **selisih** penghalang dua jalur yang mirip, tempat galat jauh lebih kecil karena saling meniadakan.
:::

::: {.contoh}
**Contoh 17.c53 · Penghalang H + H₂ dengan Hartree–Fock**

Untuk reaksi H + H₂ → H₂ + H, program pendamping (UHF/6-31G**) memberi: H₂ setimbang ($r = 0{,}7326$ Å) $-1{,}131334\ E_h$; atom H $-0{,}498233\ E_h$; keadaan transisi linear simetris ($r = 0{,}9332$ Å) $-1{,}601072\ E_h$. Hitung penghalang dan bandingkan dengan nilai teliti 40,2 kJ/mol (dari permukaan CI sangat besar). Hitung juga perbandingan laju menurut kedua penghalang pada 300 K.

**Penyelesaian.** $\Delta E^\ddagger = -1{,}601072 - (-1{,}131334 - 0{,}498233) = 0{,}028495\ E_h = 74{,}8$ kJ/mol. Perbandingan laju $e^{(74{,}8 - 40{,}2) \times 1000/(8{,}314 \times 300)} = e^{13{,}9} \approx 10^6$.

**Memahami hasil.** HF melebih-lebihkan penghalang hampir dua kali, dan meramalkan reaksi sejuta kali lebih lambat. Di keadaan transisi, tiga elektron tersebar pada tiga pusat dan saling berdekatan; korelasi yang hilang di sana jauh lebih besar daripada dalam H₂ + H yang terpisah. Fungsional GGA justru meremehkan penghalang ini karena galat delokalisasi, sering hanya sepertiga sampai separuh nilai sebenarnya. Reaksi H + H₂, yang permukaannya diketahui sangat teliti, adalah batu uji klasik untuk metode baru.
:::

::: {.contoh}
**Contoh 17.c54 · Koreksi penerobosan Wigner**

Hitung $\kappa_\text{W}$ pada 298 K untuk frekuensi imajiner 500i, 1000i, dan 1500i cm⁻¹. Untuk transfer proton dengan $|\nu^\ddagger| = 1500$ cm⁻¹, mengapa koreksi Wigner tidak dapat dipercaya?

**Penyelesaian.** $h|\nu^\ddagger|/k_BT = hc\tilde\nu/k_BT$ dengan $hc/k_B = 1{,}4388$ cm K: 2,41; 4,83; 7,24. Maka $\kappa_\text{W} = 1 + u^2/24$: 1,24; 1,97; 3,18.

**Memahami hasil.** Untuk 500i cm⁻¹ (penghalang lebar, misalnya rotasi atau gerak atom berat), penerobosan menambah laju 24%. Untuk 1500i cm⁻¹ (penghalang sempit transfer H), koreksinya lebih dari tiga kali lipat, padahal rumus Wigner diturunkan dengan menganggap koreksi kecil; suku orde lebih tinggi sama besarnya, dan model yang lebih lengkap (Eckart, penerobosan sudut kecil) sering memberi faktor 10 atau lebih. Efek isotop kinetik H/D yang sangat besar (subbab 5.10) adalah tanda percobaan bahwa penerobosan dominan.
:::

::: {.kuis}
**Kuis cepat 17.16**

Bagaimana kita membedakan minimum dan keadaan transisi dari hasil perhitungan frekuensi? Mengapa satu frekuensi imajiner saja belum cukup untuk memastikan bahwa TS yang ditemukan adalah TS reaksi yang dimaksud?
:::
