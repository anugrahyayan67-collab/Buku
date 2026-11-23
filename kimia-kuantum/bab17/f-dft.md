## 17.13 Teori fungsional kerapatan: Hohenberg–Kohn dan Kohn–Sham

### Kerapatan sebagai pengganti fungsi gelombang

Fungsi gelombang $N$ elektron bergantung pada $3N$ koordinat ruang (ditambah spin). Untuk benzena, 126 koordinat; untuk protein kecil, puluhan ribu. Padahal Hamiltonian elektronik hanya memuat interaksi satu dan dua elektron, dan "identitas" molekul ditentukan sepenuhnya oleh potensial luar $v(\mathbf r) = -\sum_AZ_A/|\mathbf r - \mathbf R_A|$, yaitu oleh letak dan muatan inti. Apakah besaran yang jauh lebih sederhana, **kerapatan elektron**

$$
\rho(\mathbf r) = N\int|\Psi(\mathbf r, \mathbf x_2, \ldots, \mathbf x_N)|^2\,ds_1\,d\mathbf x_2\cdots d\mathbf x_N , \qquad \text{(17.42)}
$$

yang hanya bergantung pada tiga koordinat, cukup untuk menentukan energi? Kerapatan inilah yang diukur dengan difraksi sinar-X (subbab 3.3).

Gagasan ini lebih tua daripada mekanika kuantum molekul modern. Model **Thomas–Fermi** (1927) menghitung energi kinetik elektron seolah-olah setiap elemen volume berisi gas elektron seragam dengan kerapatan lokal $\rho(\mathbf r)$:

$$
T_\text{TF}[\rho] = C_F\int\rho^{5/3}(\mathbf r)\,d\mathbf r, \qquad C_F = \tfrac{3}{10}(3\pi^2)^{2/3} = 2{,}8712 . \qquad \text{(17.43)}
$$

Dirac (1930) menambahkan energi pertukaran gas seragam:

$$
E_x^\text{LDA}[\rho] = -C_x\int\rho^{4/3}(\mathbf r)\,d\mathbf r, \qquad C_x = \tfrac34\left(\tfrac3\pi\right)^{1/3} = 0{,}7386 . \qquad \text{(17.44)}
$$

Besaran seperti $T_\text{TF}[\rho]$, yang memetakan sebuah fungsi menjadi sebuah bilangan, disebut **fungsional** dan ditulis dengan kurung siku. Model Thomas–Fermi menerangkan beberapa sifat atom secara kasar, tetapi gagal total untuk kimia: menurut teorema Teller (1962), molekul Thomas–Fermi tidak pernah terikat. Penyebabnya adalah energi kinetik, yang terlalu besar untuk ditaksir dengan rumus lokal sederhana; kulit atom dan ikatan kimia lenyap.

::: {.dalam}
**Dari gas elektron seragam ke $\rho^{5/3}$ dan $\rho^{4/3}$**

Dalam kubus bervolume $L^3$ dengan syarat batas periodik, elektron bebas menempati gelombang datar dengan $\mathbf k = (2\pi/L)(n_x, n_y, n_z)$ (subbab 4.5). Setiap titik $\mathbf k$ menempati volume $(2\pi/L)^3$ dan memuat dua elektron. Mengisi bola Fermi berjari-jari $k_F$ dengan $N$ elektron memberi $N = 2\cdot\tfrac43\pi k_F^3/(2\pi/L)^3$, sehingga $\rho = k_F^3/3\pi^2$, atau $k_F = (3\pi^2\rho)^{1/3}$. Energi kinetik rata-rata per elektron adalah $\tfrac35\cdot\tfrac12k_F^2$ (rata-rata $k^2$ dalam bola adalah $\tfrac35k_F^2$), sehingga rapat energi kinetik $t = \tfrac{3}{10}k_F^2\rho = \tfrac{3}{10}(3\pi^2)^{2/3}\rho^{5/3}$. Perhitungan energi pertukaran gelombang datar, yang lebih panjang, memberi energi pertukaran per elektron $-\tfrac{3}{4\pi}k_F = -\tfrac34(3\rho/\pi)^{1/3}$, sehingga rapat energinya $-C_x\rho^{4/3}$. Kedua pangkat juga dapat ditebak dengan analisis dimensi: energi kinetik berdimensi panjang$^{-2}$ dan $\rho^{2/3}$ juga; energi Coulomb berdimensi panjang$^{-1}$, sama dengan $\rho^{1/3}$.
:::

### Teorema Hohenberg–Kohn

Pierre Hohenberg dan Walter Kohn (1964) membuktikan bahwa kerapatan memang cukup.

**Teorema pertama**: potensial luar $v(\mathbf r)$ ditentukan secara unik (sampai tetapan aditif) oleh kerapatan keadaan dasar $\rho_0(\mathbf r)$. Karena $v$ dan $N = \int\rho_0$ menentukan Hamiltonian, maka $\rho_0$ menentukan segalanya: fungsi gelombang, energi, dan semua sifat keadaan dasar.

Buktinya pendek dan memakai kontradiksi. Misalkan dua potensial $v$ dan $v'$ yang berbeda lebih dari tetapan memberi kerapatan keadaan dasar yang sama $\rho$. Keduanya mempunyai Hamiltonian $\hat H$ dan $\hat H'$, keadaan dasar $\Psi$ dan $\Psi'$ yang berbeda, dan energi $E$ dan $E'$. Menurut teorema variasi, dengan $\Psi'$ sebagai fungsi uji untuk $\hat H$:

$$
E < \langle\Psi'|\hat H|\Psi'\rangle = \langle\Psi'|\hat H'|\Psi'\rangle + \langle\Psi'|\hat H - \hat H'|\Psi'\rangle = E' + \int[v(\mathbf r) - v'(\mathbf r)]\rho(\mathbf r)\,d\mathbf r .
$$

Dengan peran yang ditukar, $E' < E + \int[v' - v]\rho\,d\mathbf r$. Jumlahkan kedua ketaksamaan: $E + E' < E' + E$, kontradiksi. Jadi tidak mungkin dua potensial berbeda memberi kerapatan yang sama.

**Teorema kedua** (variasional): ada fungsional universal $F[\rho]$ (energi kinetik ditambah tolakan elektron, sama untuk semua molekul) sehingga fungsional energi

$$
E_v[\rho] = F[\rho] + \int v(\mathbf r)\rho(\mathbf r)\,d\mathbf r \qquad \text{(17.45)}
$$

mencapai minimumnya, yaitu energi keadaan dasar, tepat pada kerapatan keadaan dasar. Teorema ini mengubah masalah $3N$ dimensi menjadi masalah tiga dimensi, tetapi tidak memberi tahu bentuk $F[\rho]$. Seluruh kesulitan persamaan Schrödinger kini tersembunyi di dalam satu fungsional yang tidak diketahui.

### Persamaan Kohn–Sham

Walter Kohn dan Lu Jeu Sham (1965) menemukan cara mengatasi masalah energi kinetik yang menggagalkan Thomas–Fermi. Bayangkan sistem pembanding berisi $N$ elektron **tanpa interaksi** yang bergerak dalam potensial efektif $v_s(\mathbf r)$ yang dipilih sedemikian rupa sehingga kerapatannya sama dengan kerapatan sistem nyata. Fungsi gelombang sistem pembanding adalah satu determinan Slater dari orbital $\phi_i$, dan energi kinetiknya dapat dihitung **tepat**:

$$
T_s[\rho] = \sum_i\langle\phi_i|-\tfrac12\nabla^2|\phi_i\rangle, \qquad \rho = \sum_i|\phi_i|^2 . \qquad \text{(17.46)}
$$

Fungsional energi kemudian ditulis

$$
E[\rho] = T_s[\rho] + \int v\rho\,d\mathbf r + J[\rho] + E_{xc}[\rho], \qquad J[\rho] = \frac12\iint\frac{\rho(\mathbf r)\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}\,d\mathbf r\,d\mathbf r' . \qquad \text{(17.47)}
$$

Suku $J$ adalah energi Hartree (tolakan klasik awan elektron dengan dirinya sendiri), dan **energi pertukaran–korelasi** $E_{xc}$ didefinisikan sebagai sisanya: pertukaran, korelasi, dan selisih kecil antara energi kinetik sebenarnya dan $T_s$. Karena $T_s$ dan $J$, yang merupakan bagian terbesar energi, dihitung tepat, pendekatan pada $E_{xc}$ yang relatif kecil jauh lebih aman daripada pendekatan pada seluruh energi kinetik. Meminimumkan (17.47) terhadap orbital dengan syarat ortonormal (seperti penurunan Hartree–Fock) memberi **persamaan Kohn–Sham**:

$$
\left[-\tfrac12\nabla^2 + v(\mathbf r) + v_H(\mathbf r) + v_{xc}(\mathbf r)\right]\phi_i = \varepsilon_i\phi_i, \qquad v_H = \int\frac{\rho(\mathbf r')}{|\mathbf r - \mathbf r'|}d\mathbf r', \qquad v_{xc} = \frac{\delta E_{xc}}{\delta\rho} . \qquad \text{(17.48)}
$$

Persamaan ini sangat mirip persamaan Hartree–Fock, tetapi pertukaran nonlokal diganti dengan potensial lokal $v_{xc}$, dan potensial itu, secara prinsip, juga memuat korelasi. Prosedur penyelesaiannya sama: basis Gauss, matriks Kohn–Sham, iterasi SCF. Satu-satunya tambahan adalah integral $E_{xc}$ dan $v_{xc}$ yang tidak dapat dihitung secara analitis, sehingga dilakukan secara numerik pada **kisi** titik-titik di sekitar setiap atom. Energi totalnya

$$
E = \sum_i\varepsilon_i - J[\rho] - \int v_{xc}\rho\,d\mathbf r + E_{xc}[\rho] . \qquad \text{(17.49)}
$$

Bila $E_{xc}$ diketahui tepat, Kohn–Sham memberi energi dan kerapatan tepat. Kohn menerima Hadiah Nobel Kimia 1998 untuk teori ini.

### Lubang pertukaran–korelasi

Apa sebenarnya yang harus ditiru oleh $E_{xc}$? Tolakan elektron bergantung pada **rapat pasangan** $\rho_2(\mathbf r, \mathbf r')$, peluang menemukan satu elektron di $\mathbf r$ dan elektron lain di $\mathbf r'$. Tuliskan

$$
\rho_2(\mathbf r, \mathbf r') = \rho(\mathbf r)\left[\rho(\mathbf r') + h_{xc}(\mathbf r, \mathbf r')\right] ,
$$

dengan $h_{xc}$ **lubang pertukaran–korelasi**: berkurangnya peluang menemukan elektron lain di $\mathbf r'$ karena sudah ada satu elektron di $\mathbf r$. Energi tolakan elektron menjadi $J[\rho] + \tfrac12\iint\rho(\mathbf r)h_{xc}(\mathbf r, \mathbf r')/|\mathbf r - \mathbf r'|\,d\mathbf r\,d\mathbf r'$: tolakan klasik ditambah tarikan antara setiap elektron dan lubangnya sendiri. Lubang ini mempunyai sifat-sifat tepat yang sederhana: lubang pertukaran selalu negatif dan berisi tepat satu elektron, $\int h_x(\mathbf r, \mathbf r')\,d\mathbf r' = -1$ (elektron tidak dapat berinteraksi dengan dirinya sendiri), sedangkan lubang korelasi berisi nol elektron, sehingga hanya mengubah bentuk lubang. Energi pertukaran–korelasi hanya bergantung pada **rata-rata bola** lubang di sekitar setiap elektron, bukan bentuk rincinya. Inilah rahasia keberhasilan LDA yang mengejutkan: lubang gas seragam sangat berbeda bentuknya dari lubang dalam molekul, tetapi ia berisi tepat minus satu elektron dan rata-rata bolanya cukup mirip. Banyak fungsional modern dirancang dengan memaksakan sifat-sifat tepat semacam ini.

::: {.contoh}
**Contoh 17.49 · Lubang pertukaran helium**

Untuk keadaan dasar HF helium, kedua elektron menempati orbital ruang yang sama. Tunjukkan bahwa lubang pertukaran adalah $h_x(\mathbf r, \mathbf r') = -\tfrac12\rho(\mathbf r')$ dan bahwa $E_x = -\tfrac12J[\rho]$. Dengan $J[\rho] = 2{,}0516\ E_h$ untuk kerapatan HF, hitung $E_x$ dan bandingkan dengan LDA ($-0{,}862\ E_h$).

**Penyelesaian.** Elektron berspin α hanya "melihat" lubang pertukaran yang dibentuk elektron berspin α lain; dalam He tidak ada. Untuk elektron α, satu-satunya elektron lain adalah elektron β yang tersebar dengan rapat $\tfrac12\rho$, tanpa korelasi dalam HF. Jadi $\rho_2(\mathbf r, \mathbf r') = \tfrac12\rho(\mathbf r)\rho(\mathbf r')$, sehingga $h_x = -\tfrac12\rho(\mathbf r')$, yang terintegrasi menjadi $-1$. Maka $E_x = \tfrac12\iint\rho(\mathbf r)(-\tfrac12\rho(\mathbf r'))/|\mathbf r - \mathbf r'| = -\tfrac12J[\rho] = -1{,}0258\ E_h$, sama dengan $-J_{11}$ (Contoh 17.51).

**Memahami hasil.** Lubang pertukaran helium tidak terpusat di sekitar elektron: ia adalah separuh awan elektron itu sendiri, tidak peduli di mana elektron pertama berada. LDA menganggap lubang terpusat di sekitar setiap elektron seperti dalam gas seragam, sehingga bentuknya salah, tetapi isinya benar ($-1$), dan energi pertukarannya hanya 16% terlalu kecil. Untuk molekul yang direnggangkan, lubang tepat dapat berada di atom lain sama sekali; inilah keadaan ketika fungsional lokal paling gagal (korelasi statik dan galat delokalisasi).
:::

### Arti orbital dan energi Kohn–Sham

Orbital Kohn–Sham adalah orbital sistem pembanding buatan, bukan orbital HF. Meski begitu, bentuknya biasanya sangat mirip orbital HF dan berguna untuk penafsiran kualitatif. Ada satu hasil tepat: untuk fungsional tepat, energi HOMO Kohn–Sham sama dengan minus energi ionisasi pertama, $\varepsilon_\text{HOMO} = -\text{EI}$ (teorema ionisasi). Dengan fungsional pendekatan, hasil ini biasanya jauh meleset (Contoh 17.52): energi HOMO LDA dan GGA terlalu tinggi beberapa eV, karena potensial $v_{xc}$ pendekatan meluruh terlalu cepat jauh dari molekul. Teorema Janak menghubungkan energi orbital dengan turunan energi terhadap okupansi, $\varepsilon_i = \partial E/\partial n_i$.

::: {.contoh}
**Contoh 17.50 · Thomas–Fermi untuk atom hidrogen**

Hitung $T_\text{TF}$ untuk kerapatan tepat atom hidrogen $\rho = e^{-2r}/\pi$ dan bandingkan dengan energi kinetik tepat $\tfrac12\ E_h$.

**Penyelesaian.** $T_\text{TF} = C_F\int_0^\infty4\pi r^2\pi^{-5/3}e^{-10r/3}dr = 4\pi^{-2/3}C_F\cdot\dfrac{2}{(10/3)^3} = 4(0{,}4662)(2{,}8712)(0{,}0540) = 0{,}289\ E_h$.

**Memahami hasil.** Thomas–Fermi meremehkan energi kinetik 42%. Atom hidrogen jauh dari gas elektron seragam: kerapatannya berubah cepat dalam jarak sebanding dengan panjang gelombang elektron. Galat semacam ini, untuk bagian energi yang terbesar, adalah alasan mengapa model berbasis kerapatan murni ("orbital-free DFT") masih jauh dari ketelitian kimia, dan mengapa trik Kohn–Sham, menghitung $T_s$ dari orbital, sangat penting.
:::

::: {.contoh}
**Contoh 17.51 · Atom helium dengan LDA**

Program radial kecil (program pendamping `lda.py`, metode beda hingga pada kisi radial) menyelesaikan persamaan Kohn–Sham untuk He dengan pertukaran Dirac dan korelasi gas seragam (parameterisasi Perdew–Wang 1992). Hasilnya: energi total LDA $-2{,}8345\ E_h$; dengan pertukaran saja $-2{,}7236\ E_h$; $E_x^\text{LDA} = -0{,}862$ dan $E_c^\text{LDA} = -0{,}111\ E_h$. Nilai HF: $E = -2{,}8617$, $E_x = -1{,}026\ E_h$; energi tepat $-2{,}9037$, energi korelasi tepat $-0{,}042\ E_h$. Bandingkan.

**Penyelesaian.** LDA meremehkan besar pertukaran 16% ($0{,}862/1{,}026 = 0{,}84$) dan melebih-lebihkan korelasi 2,6 kali ($0{,}111/0{,}042$). Galat pertukaran ($+0{,}164\ E_h$) dan galat korelasi ($-0{,}069\ E_h$) berlawanan tanda dan sebagian meniadakan diri, sehingga energi total LDA hanya $0{,}069\ E_h$ di atas nilai tepat, lebih buruk daripada HF ($0{,}042$) untuk atom ini.

**Memahami hasil.** Untuk atom dan energi total, LDA tidak unggul. Keunggulannya muncul pada selisih energi dan pada sistem yang mendekati gas seragam (logam). Peniadaan galat pertukaran dan korelasi bukan kebetulan: lubang pertukaran–korelasi LDA, sebagai satu kesatuan, memenuhi syarat-syarat tepat yang penting (misalnya berisi tepat minus satu elektron), meskipun masing-masing bagiannya tidak.
:::

::: {.contoh}
**Contoh 17.52 · Interaksi diri dan energi HOMO**

Untuk atom H dengan LSDA (spin terpolarisasi), program radial memberi $E = -0{,}4787\ E_h$, $J = 0{,}2984$, $E_x = -0{,}2564$, $E_c = -0{,}0217\ E_h$, dan $\varepsilon_\text{HOMO} = -0{,}269\ E_h$. Untuk He (LDA), $\varepsilon_\text{HOMO} = -0{,}570\ E_h$, sedangkan EI He 0,9036 $E_h$. Tafsirkan.

**Penyelesaian.** Untuk satu elektron, tidak ada tolakan elektron–elektron: harus berlaku $J + E_x + E_c = 0$. LSDA memberi $0{,}2984 - 0{,}2564 - 0{,}0217 = +0{,}0203\ E_h$: elektron masih "menolak dirinya sendiri" sebesar 53 kJ/mol. Energi HOMO H seharusnya $-0{,}5\ E_h$, tetapi LSDA memberi $-0{,}269$ (galat 46%); untuk He galatnya 37%.

**Memahami hasil.** Inilah **galat interaksi diri**: dalam HF, $J_{ii} = K_{ii}$ menghapus interaksi diri secara tepat (subbab 17.2), tetapi fungsional lokal tidak dapat melakukannya. Akibatnya potensial Kohn–Sham meluruh seperti $e^{-r}$ alih-alih $-1/r$ jauh dari atom, elektron terluar terikat terlalu lemah, dan energi HOMO terlalu tinggi. Galat ini adalah sumber banyak kegagalan DFT: penghalang reaksi terlalu rendah, celah pita terlalu kecil, dan muatan yang terlalu tersebar pada sistem transfer muatan (subbab 17.14).
:::

::: {.kuis}
**Kuis cepat 17.13**

Apa yang dibuktikan teorema Hohenberg–Kohn, dan apa yang tidak? Mengapa Kohn–Sham menghitung energi kinetik dari orbital alih-alih dari rumus kerapatan seperti Thomas–Fermi?
:::

## 17.14 Fungsional LDA, GGA, hibrida

### Tangga Yakub

Semua fungsional praktis adalah pendekatan bagi $E_{xc}[\rho]$. John Perdew menyusunnya sebagai **tangga Yakub** menuju "surga ketelitian kimia", dengan setiap anak tangga menambah satu bahan:

| Anak tangga | Bahan | Contoh |
|---|---|---|
| 1. LDA | $\rho$ | SVWN, SPW92 |
| 2. GGA | $\rho$, $\nabla\rho$ | BLYP, PBE, BP86 |
| 3. meta-GGA | $\rho$, $\nabla\rho$, $\tau = \tfrac12\sum_i|\nabla\phi_i|^2$ | TPSS, SCAN, M06-L |
| 4. hibrida | + pertukaran tepat (HF) | B3LYP, PBE0, M06-2X, ωB97X |
| 5. hibrida ganda | + orbital virtual (gaya MP2) | B2PLYP, DSD-PBEP86 |

Makin tinggi anak tangga, makin mahal dan umumnya makin teliti, tetapi tidak ada jaminan untuk setiap sifat. Dua filosofi bersaing dalam perancangan fungsional: **nonempiris**, yang memenuhi sebanyak mungkin syarat tepat (PBE, TPSS, SCAN), dan **empiris**, yang mencocokkan parameter dengan himpunan data acuan (B3LYP, keluarga Minnesota M06). Fungsional nonempiris lebih dapat dipercaya di luar daerah pencocokan; fungsional empiris sering lebih teliti untuk jenis senyawa yang dipakai dalam pencocokannya.

### LDA

**Pendekatan kerapatan lokal** (LDA, atau LSDA bila spin dipisahkan) memakai energi pertukaran–korelasi per elektron gas seragam pada kerapatan lokal: $E_{xc}^\text{LDA} = \int\rho\,\varepsilon_{xc}^\text{gas}(\rho)\,d\mathbf r$. Bagian pertukaran adalah (17.44); bagian korelasi diambil dari simulasi Monte Carlo kuantum gas elektron (Ceperley dan Alder, 1980) yang diinterpolasi (VWN, PW92). LDA memberi geometri dan frekuensi yang cukup baik dan sangat berhasil untuk logam dan padatan, tetapi **mengikat terlalu kuat**: energi atomisasi molekul rata-rata terlalu besar lebih dari 100 kJ/mol. Karena itu LDA jarang dipakai dalam kimia molekul.

### GGA

**Pendekatan gradien terumumkan** (GGA) memperhitungkan seberapa cepat kerapatan berubah melalui gradien tereduksi tak berdimensi

$$
s = \frac{|\nabla\rho|}{2(3\pi^2)^{1/3}\rho^{4/3}} , \qquad E_x^\text{GGA} = \int\rho\,\varepsilon_x^\text{LDA}(\rho)\,F_x(s)\,d\mathbf r . \qquad \text{(17.50)}
$$

Faktor peningkatan $F_x(s)$ bernilai 1 untuk gas seragam ($s = 0$) dan naik untuk kerapatan yang tidak seragam. Untuk fungsional PBE (Perdew, Burke, Ernzerhof, 1996),

$$
F_x^\text{PBE}(s) = 1 + \kappa - \frac{\kappa}{1 + \mu s^2/\kappa}, \qquad \kappa = 0{,}804, \quad \mu = 0{,}21951 , \qquad \text{(17.51)}
$$

dengan $\kappa$ dipilih agar memenuhi batas Lieb–Oxford dan $\mu$ dari syarat gas hampir seragam: tidak ada parameter yang dicocokkan dengan data molekul. Fungsional pertukaran B88 (Becke, 1988) memakai satu parameter yang dicocokkan dengan energi pertukaran atom gas mulia dan dirancang agar rapat energi pertukaran meluruh dengan benar seperti $-1/2r$ jauh dari atom. Korelasi LYP (Lee, Yang, Parr, 1988) diturunkan dari rumus korelasi Colle–Salvetti untuk helium. GGA memperbaiki energi atomisasi LDA secara dramatis, menjadi galat rata-rata sekitar 20–40 kJ/mol, dan sangat populer untuk padatan dan dinamika molekul ab initio (PBE).

### Hibrida

Axel Becke (1993) memakai argumen **koneksi adiabatik**: bayangkan tolakan elektron "dinyalakan" perlahan dari nol (sistem Kohn–Sham tanpa interaksi, yang pertukarannya tepat sama dengan pertukaran HF dari orbital KS) sampai penuh (sistem nyata). Energi pertukaran–korelasi adalah rata-rata sepanjang jalan ini, sehingga mencampur sebagian pertukaran tepat dengan fungsional lokal masuk akal. Fungsional hibrida yang paling banyak dipakai dalam sejarah kimia adalah **B3LYP**:

$$
E_{xc}^\text{B3LYP} = (1 - a_0)E_x^\text{LSDA} + a_0E_x^\text{HF} + a_x\Delta E_x^\text{B88} + a_cE_c^\text{LYP} + (1 - a_c)E_c^\text{VWN} , \qquad \text{(17.52)}
$$

dengan $a_0 = 0{,}20$, $a_x = 0{,}72$, dan $a_c = 0{,}81$, tiga parameter yang semula dicocokkan oleh Becke dengan energi atomisasi dan energi ionisasi. **PBE0** mencampur 25% pertukaran HF ke dalam PBE tanpa parameter tambahan, berdasarkan argumen teori perturbasi. Hibrida mengurangi galat interaksi diri, memperbaiki penghalang reaksi dan celah HOMO–LUMO, dan memberi energi atomisasi dengan galat rata-rata sekitar 10 kJ/mol untuk molekul organik kecil (himpunan uji G2).

**Hibrida terpisah jangkauan** memecah tolakan Coulomb menjadi bagian jarak pendek dan jarak jauh,

$$
\frac1{r_{12}} = \frac{1 - \operatorname{erf}(\omega r_{12})}{r_{12}} + \frac{\operatorname{erf}(\omega r_{12})}{r_{12}} , \qquad \text{(17.53)}
$$

dan memakai fungsional DFT untuk bagian pertama serta pertukaran HF penuh untuk bagian kedua (ωB97X, CAM-B3LYP, LC-ωPBE). Dengan cara ini potensial meluruh dengan benar seperti $-1/r$ jauh dari molekul, sehingga eksitasi transfer muatan, polarisabilitas molekul panjang, dan energi HOMO jauh lebih baik.

**Hibrida ganda** (B2PLYP, Grimme 2006) menambahkan korelasi gaya MP2 dari orbital Kohn–Sham: $E_{xc} = (1 - a_x)E_x^\text{GGA} + a_xE_x^\text{HF} + (1 - a_c)E_c^\text{GGA} + a_cE_c^\text{PT2}$, dengan $a_x = 0{,}53$ dan $a_c = 0{,}27$ untuk B2PLYP. Biayanya sebanding dengan MP2, dan ketelitiannya untuk termokimia sering mendekati metode komposit.

### Galat yang khas

Mengetahui di mana DFT gagal sama pentingnya dengan mengetahui di mana ia berhasil:

1. **Galat delokalisasi** (bentuk lain galat interaksi diri): fungsional lokal lebih menyukai muatan yang tersebar. H₂⁺ yang direnggangkan terlalu stabil, penghalang reaksi radikal terlalu rendah, dan kompleks transfer muatan terlalu terikat. Hibrida dengan pertukaran HF lebih besar mengurangi masalah ini.
2. **Korelasi statik**: satu determinan Kohn–Sham tidak dapat menggambarkan diradikal dan ikatan yang putus, meskipun DFT sering lebih toleran daripada HF.
3. **Dispersi**: fungsional lokal dan semilokal tidak memuat interaksi London jarak jauh, yang berasal dari korelasi antara fluktuasi kerapatan di dua tempat yang berjauhan. Koreksi empiris D3 atau D4 kini hampir wajib (subbab 17.15).
4. **Celah pita**: celah HOMO–LUMO Kohn–Sham dengan GGA meremehkan celah pita semikonduktor 30–50%.

### Keadaan tereksitasi

Semua metode di atas dirancang untuk keadaan dasar. Untuk spektrum UV-Vis, fotokimia, dan fluoresensi (subbab 15.7–15.9) diperlukan keadaan tereksitasi. Tiga keluarga metode banyak dipakai:

- **CIS** (*configuration interaction singles*): fungsi gelombang tereksitasi sebagai kombinasi eksitasi tunggal dari determinan HF. Menurut teorema Brillouin, keadaan CIS tidak bercampur dengan keadaan dasar HF, sehingga CIS adalah "Hartree–Fock untuk keadaan tereksitasi". Energinya biasanya terlalu tinggi 1–2 eV karena tidak ada korelasi.
- **TD-DFT** (DFT bergantung waktu, dalam formulasi respons linear Casida): energi eksitasi diperoleh dari kutub respons kerapatan terhadap medan listrik yang berosilasi. Biayanya sebanding dengan DFT keadaan dasar, dan dengan fungsional hibrida, eksitasi valensi molekul organik diramalkan dengan galat sekitar 0,2–0,4 eV. Ia gagal untuk eksitasi transfer muatan (kecuali dengan hibrida terpisah jangkauan), keadaan Rydberg (tanpa fungsi difus dan potensial yang meluruh benar), dan keadaan dengan karakter eksitasi ganda.
- **EOM-CCSD** dan **CC2** (*coupled-cluster* untuk keadaan tereksitasi): lebih mahal, tetapi galatnya sekitar 0,1–0,3 eV dan dapat diandalkan sebagai acuan. Untuk keadaan dengan korelasi statik kuat (misalnya titik persilangan konis dalam fotokimia), diperlukan CASSCF/CASPT2.

Bersama energi eksitasi, metode-metode ini memberi **kekuatan osilator** $f = \tfrac23\Delta E|\langle 0|\boldsymbol\mu|n\rangle|^2$ (subbab 15.2), sehingga seluruh spektrum serapan dapat disimulasikan.

::: {.contoh}
**Contoh 17.53 · CIS untuk air**

Program pendamping, dengan matriks CIS singlet $A_{ia,jb} = (\varepsilon_a - \varepsilon_i)\delta_{ij}\delta_{ab} + 2(ia|jb) - (ij|ab)$, memberi untuk H₂O pada geometri percobaan: dengan STO-3G, eksitasi singlet terendah 13,2 eV dan triplet terendah 11,1 eV; dengan 6-31G*, singlet 9,60 eV dan triplet 8,63 eV, keduanya dari eksitasi $1b_1 \to 4a_1$. Celah HOMO–LUMO 6-31G* adalah 19,3 eV, dan pita serapan pertama air teramati di sekitar 7,4 eV. Tafsirkan.

**Penyelesaian.** Celah HOMO–LUMO 19,3 eV turun menjadi 9,6 eV setelah suku $2(ia|jb) - (ij|ab)$ dimasukkan. Suku $-(ij|ab)$, untuk $i = j$ dan $a = b$, adalah tarikan Coulomb antara elektron tereksitasi dan lubangnya, dan inilah yang menurunkan energi eksitasi paling banyak. Triplet lebih rendah karena tidak memiliki suku pertukaran $2(ia|jb)$ yang menaikkan singlet. Sisa galat 2,2 eV berasal dari tiadanya korelasi dan dari basis tanpa fungsi difus untuk karakter Rydberg (3s) keadaan tereksitasi pertama air.

**Memahami hasil.** Contoh ini menegaskan Contoh 17.25: selisih energi orbital bukan energi eksitasi. Bahkan CIS dengan basis lebih besar tetap terlalu tinggi sekitar 1 eV; TD-DFT dengan fungsional hibrida dan basis berfungsi difus memberi sekitar 7 eV, dan EOM-CCSD dengan basis aug-cc-pVTZ mendekati nilai percobaan dalam 0,1–0,2 eV.
:::

![Gambar 17.9 Kiri: faktor peningkatan pertukaran PBE terhadap gradien tereduksi s; arsiran menunjukkan rentang s yang dominan dalam ikatan kimia (sekitar 0–3). Kanan: hasil program radial LDA untuk He, yaitu rapat elektron radial 4πr²ρ dan potensial pertukaran–korelasi v_xc, dibandingkan potensial −1/r yang seharusnya dirasakan elektron jauh dari atom; v_xc LDA meluruh terlalu cepat.](fig/c_dft.png){width=94%}

::: {.contoh}
**Contoh 17.54 · Faktor peningkatan PBE**

Hitung $F_x^\text{PBE}$ untuk $s = 0$; 0,5; 1; 2; 3; dan 10. Untuk atom hidrogen ($\rho = e^{-2r}/\pi$), berapa $s$ pada $r = 1$ dan $r = 4$ bohr?

**Penyelesaian.** Dari (17.51): $F_x = 1{,}000$; 1,051; 1,172; 1,420; 1,571; 1,776, mendekati batas $1 + \kappa = 1{,}804$. Untuk atom H, $|\nabla\rho| = 2\rho$, sehingga $s = \rho^{-1/3}/(3\pi^2)^{1/3} = (\pi e^{2r})^{1/3}/(3\pi^2)^{1/3}$: $s(1) = 0{,}92$ dan $s(4) = 6{,}8$.

**Memahami hasil.** Di daerah yang paling penting bagi energi ($s \lesssim 2$), GGA menaikkan pertukaran 5–40% dibandingkan LDA, menutup sebagian besar kekurangan pertukaran LDA (Contoh 17.51). Di ekor kerapatan yang jauh ($s$ besar) faktornya jenuh; perilaku fungsional di daerah ini sulit dikendalikan dan menjadi sumber galat untuk sifat yang peka terhadap ekor, seperti afinitas elektron dan polarisabilitas.
:::

::: {.contoh}
**Contoh 17.55 · Membedah B3LYP**

Dari (17.52), berapa bagian pertukaran HF dalam B3LYP? Tulis ulang bagian pertukaran sebagai $\alpha E_x^\text{LSDA} + \beta E_x^\text{B88,total} + a_0E_x^\text{HF}$, dengan $\Delta E_x^\text{B88} = E_x^\text{B88} - E_x^\text{LSDA}$. Berapa persen korelasi yang berasal dari LYP?

**Penyelesaian.** Pertukaran HF 20%. $(1 - a_0)E_x^\text{LSDA} + a_x(E_x^\text{B88} - E_x^\text{LSDA}) = (0{,}80 - 0{,}72)E_x^\text{LSDA} + 0{,}72E_x^\text{B88} = 0{,}08E_x^\text{LSDA} + 0{,}72E_x^\text{B88}$. Jumlah koefisien $0{,}08 + 0{,}72 + 0{,}20 = 1$. Korelasi: 81% LYP, 19% VWN.

**Memahami hasil.** B3LYP adalah campuran dengan resep tetap, bukan fungsional yang diturunkan dari prinsip pertama. Sebagian ketenarannya adalah keberuntungan sejarah: resep ini, yang dirancang sebelum ada himpunan uji besar, ternyata sangat baik untuk geometri, frekuensi, dan termokimia molekul organik. Untuk penghalang reaksi, dispersi, dan logam transisi, fungsional yang lebih baru umumnya lebih unggul.
:::

::: {.contoh}
**Contoh 17.56 · Pemisahan jangkauan**

Dengan $\omega = 0{,}3$ bohr⁻¹ (nilai dalam ωB97X), berapa pecahan $1/r_{12}$ yang diperlakukan dengan pertukaran HF pada $r_{12} = 1$, 3, 5, dan 10 bohr?

**Penyelesaian.** Pecahan jarak jauh $\operatorname{erf}(\omega r_{12})$: $\operatorname{erf}(0{,}3) = 0{,}33$; $\operatorname{erf}(0{,}9) = 0{,}80$; $\operatorname{erf}(1{,}5) = 0{,}97$; $\operatorname{erf}(3{,}0) = 1{,}00$.

**Memahami hasil.** Pada jarak sebanding dengan panjang ikatan (2–3 bohr), sekitar setengah sampai empat perlima pertukaran sudah HF; pada jarak antarmolekul seluruhnya HF. Untuk elektron yang dipindahkan dari donor ke akseptor berjarak 10 bohr, tarikan antara elektron dan lubangnya kini dihitung dengan benar sebagai $-1/R$, sehingga energi eksitasi transfer muatan dalam TD-DFT tidak lagi terlalu rendah beberapa eV seperti pada B3LYP.
:::

::: {.contoh}
**Contoh 17.57 · Memilih fungsional**

Untuk setiap tugas berikut, pilih jenis fungsional dan alasannya: (a) optimasi geometri molekul organik besar; (b) energi penghalang reaksi radikal; (c) energi interaksi kompleks tumpukan π; (d) eksitasi transfer muatan dalam zat warna donor–akseptor; (e) struktur pita logam.

**Penyelesaian.** (a) GGA atau hibrida dengan koreksi dispersi (misalnya PBE-D3 atau B3LYP-D3) dan basis sedang: murah dan geometrinya baik. (b) Hibrida dengan pertukaran HF tinggi atau meta-GGA hibrida (M06-2X, ωB97X-D): mengurangi galat delokalisasi yang merendahkan penghalang. (c) Fungsional apa pun **dengan** koreksi dispersi D3/D4, atau hibrida ganda; tanpa koreksi, tumpukan π hampir tidak terikat. (d) Hibrida terpisah jangkauan (CAM-B3LYP, ωB97X-D). (e) GGA (PBE) atau meta-GGA (SCAN) dalam basis gelombang datar; untuk logam, hibrida mahal dan tidak selalu lebih baik.

**Memahami hasil.** Tidak ada fungsional terbaik untuk semua hal. Praktik yang baik adalah memeriksa beberapa fungsional dari anak tangga berbeda, membandingkan dengan data percobaan atau perhitungan CCSD(T) untuk sistem model, dan melaporkan dengan jujur kepekaan hasil terhadap pilihan fungsional.
:::

::: {.contoh}
**Contoh 17.58 · Pertukaran PBE untuk helium**

Untuk kerapatan helium dengan muatan efektif $\zeta = 1{,}6875$, $\rho = (2\zeta^3/\pi)e^{-2\zeta r}$, energi pertukaran tepat (bentuk HF untuk dua elektron dalam satu orbital) adalah $-\tfrac12J[\rho] = -5\zeta/8 = -1{,}0547\ E_h$. Integrasi numerik dengan (17.44) dan (17.50)–(17.51) memberi $E_x^\text{LDA} = -0{,}9046$ dan $E_x^\text{PBE} = -1{,}0325\ E_h$. Hitung galat relatif keduanya.

**Penyelesaian.** LDA: $(1{,}0547 - 0{,}9046)/1{,}0547 = 14{,}2\%$ terlalu kecil. PBE: $(1{,}0547 - 1{,}0325)/1{,}0547 = 2{,}1\%$ terlalu kecil.

**Memahami hasil.** Faktor peningkatan gradien memulihkan sebagian besar kekurangan pertukaran LDA, dari 14% menjadi 2%. Untuk atom-atom, galat pertukaran GGA biasanya 1–3%; karena energi pertukaran jauh lebih besar daripada energi ikatan, galat persen kecil ini masih berarti puluhan kJ/mol, tetapi sebagian besar meniadakan diri dalam energi reaksi. Menariknya, untuk kerapatan Kohn–Sham LDA helium (yang sedikit lebih menyebar), PBE memberi $-0{,}990\ E_h$: hasil fungsional bergantung pada kerapatan yang dipakai, sehingga fungsional dan kerapatannya harus konsisten.
:::

::: {.kuis}
**Kuis cepat 17.14**

Mengapa menambahkan sebagian pertukaran HF mengurangi galat interaksi diri? Apa bahan baru yang ditambahkan meta-GGA dibandingkan GGA?
:::
