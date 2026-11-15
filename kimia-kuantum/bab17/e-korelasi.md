## 17.10 Energi korelasi dan interaksi konfigurasi

### Apa yang hilang dalam Hartree–Fock

Dalam Hartree–Fock setiap elektron bergerak dalam medan **rata-rata** elektron lain. Elektron sebenarnya saling menghindar secara sesaat: bila satu elektron berada di sisi kiri molekul, peluang elektron lain berada di dekatnya berkurang. Pertukaran HF sudah memisahkan elektron berspin **sama** (lubang Fermi), tetapi elektron berspin berlawanan dalam HF bergerak sama sekali tanpa saling memperhatikan. Penurunan energi yang hilang karena itu didefinisikan (Per-Olov Löwdin, 1955) sebagai **energi korelasi**:

$$
E_\text{kor} = E_\text{tepat} - E_\text{HF}^\text{batas} , \qquad \text{(17.e30)}
$$

dengan $E_\text{tepat}$ energi tepat nonrelativistik dan $E_\text{HF}^\text{batas}$ energi HF dengan basis lengkap. Energi korelasi selalu negatif (teorema variasi) dan besarnya sekitar 0,04 $E_h$ per pasangan elektron dalam orbital yang sama, kira-kira 1% energi total. Untuk H₂O, batas HF sekitar $-76{,}068$ dan energi tepat sekitar $-76{,}438\ E_h$, sehingga $E_\text{kor} \approx -0{,}37\ E_h$, hampir 1000 kJ/mol. Sebagian besar berasal dari elektron yang tidak berubah selama reaksi, tetapi perubahan korelasi saat ikatan terbentuk atau putus mudah mencapai 100 kJ/mol. Energi disosiasi ikatan F₂, misalnya, bernilai negatif dalam HF: tanpa korelasi, F₂ tidak terikat.

Ada dua jenis korelasi yang berbeda sifat. **Korelasi dinamik** adalah saling menghindarnya elektron dalam jarak pendek: penyebab "lubang Coulomb" di sekitar setiap elektron dan taring antarelektron (subbab 17.5). Ia terdistribusi atas banyak sekali konfigurasi tereksitasi dengan koefisien kecil. **Korelasi statik** (nondinamik) muncul bila beberapa konfigurasi berenergi hampir sama sehingga satu determinan tidak lagi memadai: ikatan yang putus (Contoh 17.c06), diradikal, keadaan transisi reaksi terlarang simetri, dan banyak senyawa logam transisi. Metode yang baik untuk satu jenis tidak selalu baik untuk jenis lain.

### Interaksi konfigurasi

Determinan HF $\Phi_0$ adalah satu dari banyak determinan yang dapat dibentuk dari $K$ spin-orbital. Dengan memindahkan elektron dari orbital terisi $i, j, \ldots$ ke orbital virtual $a, b, \ldots$, kita memperoleh determinan tereksitasi tunggal $\Phi_i^a$, ganda $\Phi_{ij}^{ab}$, dan seterusnya. Kumpulan semua determinan ini membentuk basis lengkap untuk fungsi gelombang $N$ elektron dalam basis orbital yang dipilih. **Interaksi konfigurasi** (CI) menulis

$$
\Psi = c_0\Phi_0 + \sum_{ia}c_i^a\Phi_i^a + \sum_{i<j,\,a<b}c_{ij}^{ab}\Phi_{ij}^{ab} + \sum_{i<j<k,\,a<b<c}c_{ijk}^{abc}\Phi_{ijk}^{abc} + \cdots \qquad \text{(17.e31)}
$$

dan menentukan koefisien dengan metode variasi linear (subbab 8.4): diagonalisasi matriks Hamiltonian $H_{IJ} = \langle\Phi_I|\hat H|\Phi_J\rangle$ yang unsur-unsurnya diberikan oleh aturan Condon–Slater (subbab 9.14). Dua sifat menyederhanakan matriks itu:

1. Aturan Condon–Slater: unsur matriks antara determinan yang berbeda lebih dari dua spin-orbital adalah nol, karena $\hat H$ hanya memuat operator satu dan dua elektron. Jadi $\Phi_0$ hanya berinteraksi langsung dengan eksitasi tunggal dan ganda.
2. **Teorema Brillouin**: untuk orbital HF, $\langle\Phi_0|\hat H|\Phi_i^a\rangle = f_{ia} = 0$, karena operator Fock diagonal dalam basis orbital kanonik. Eksitasi tunggal tidak berinteraksi langsung dengan $\Phi_0$; mereka hanya masuk secara tidak langsung, melalui eksitasi ganda.

Akibatnya eksitasi **ganda** adalah sumbangan korelasi yang paling penting. Bila semua determinan dimasukkan, diperoleh **CI penuh** (FCI), jawaban tepat dalam basis yang dipakai. Karena banyaknya determinan tumbuh secara eksponensial (Contoh 17.c03), FCI hanya mungkin untuk sistem sangat kecil dan berperan sebagai patokan. CI terpotong pada eksitasi tunggal dan ganda (**CISD**) praktis untuk molekul kecil, tetapi mempunyai cacat mendasar.

### Konsistensi ukuran

Metode disebut **konsisten ukuran** (*size-consistent*) bila energi dua molekul yang terpisah jauh sama dengan jumlah energi masing-masing. HF, MP2, CCSD, dan FCI konsisten ukuran; CISD tidak. Alasannya sederhana: untuk dua molekul H₂ yang terpisah jauh, fungsi gelombang tepat adalah hasil kali $\Psi_A\Psi_B$, dan bila masing-masing memuat eksitasi ganda, hasil kalinya memuat eksitasi **kuadrupel** (ganda pada A sekaligus ganda pada B). CISD membuang kuadrupel itu, sehingga untuk sistem gabungan ia memulihkan pecahan energi korelasi yang lebih kecil daripada untuk masing-masing. Galatnya tumbuh dengan ukuran sistem: untuk $n$ molekul yang tidak berinteraksi, pecahan korelasi yang dipulihkan CISD menurun kira-kira sebagai $1/\sqrt n$. Koreksi Davidson, $\Delta E_Q \approx (1 - c_0^2)E^\text{kor}_\text{CISD}$, menaksir sumbangan kuadrupel yang hilang.

### Fungsi gelombang multikonfigurasi

Untuk korelasi statik, pendekatan yang tepat adalah memasukkan sejak awal beberapa konfigurasi yang penting dan mengoptimasi orbitalnya bersama koefisien CI. **CASSCF** (*complete active space SCF*) memilih "ruang aktif" berisi beberapa elektron dan orbital (misalnya orbital ikatan dan antiikatan dari ikatan yang putus) dan melakukan CI penuh di dalam ruang itu, sambil mengoptimasi semua orbital. Korelasi dinamik kemudian ditambahkan dengan teori perturbasi (CASPT2, NEVPT2) atau dengan CI multireferensi (MRCI). Metode-metode ini adalah alat utama fotokimia dan kimia logam transisi, tetapi pemilihan ruang aktif memerlukan pemahaman kimia dan tidak dapat diserahkan sepenuhnya kepada program.

::: {.contoh}
**Contoh 17.c30 · CI penuh H₂ dalam basis minimal**

Untuk H₂ dalam basis STO-3G ($R = 1{,}4$ bohr) ada dua orbital ruang, $\sigma_g$ dan $\sigma_u$. Konfigurasi singlet $^1\Sigma_g^+$ yang mungkin hanya $\Phi_0 = |\sigma_g\bar\sigma_g|$ dan $\Phi_D = |\sigma_u\bar\sigma_u|$ (eksitasi tunggal bersimetri $\Sigma_u$, sehingga tidak bercampur). Dengan integral orbital molekul $h_{11} = -1{,}2528$, $h_{22} = -0{,}4756$, $J_{11} = 0{,}6746$, $J_{22} = 0{,}6975$, dan $K_{12} = 0{,}1813\ E_h$, susun matriks CI 2 × 2 dan hitung energi dasar.

**Penyelesaian.** $H_{00} = 2h_{11} + J_{11} = -1{,}8310$; $H_{DD} = 2h_{22} + J_{22} = -0{,}2537$; $H_{0D} = \langle\sigma_g\bar\sigma_g|\hat H|\sigma_u\bar\sigma_u\rangle = K_{12} = 0{,}1813\ E_h$. Nilai eigen terendah:

$$
E = \frac{H_{00} + H_{DD}}{2} - \sqrt{\left(\frac{H_{DD} - H_{00}}{2}\right)^2 + K_{12}^2} = -1{,}0424 - 0{,}8092 = -1{,}8516\ E_h .
$$

Ditambah $1/R$: $E_\text{FCI} = -1{,}1373\ E_h$. Koefisiennya $c_0 = 0{,}9936$, $c_D = -0{,}1127$. Energi korelasi $-1{,}1373 - (-1{,}1167) = -0{,}0206\ E_h$.

**Memahami hasil.** Konfigurasi $\sigma_u^2$ hanya bercampur 1,3%, tetapi menurunkan energi 54 kJ/mol. Tanda negatif $c_D$ penting: $c_0\sigma_g^2 - |c_D|\sigma_u^2$ mengurangi bobot bagian ionik H⁺H⁻ dalam fungsi gelombang (subbab 11.12). Pada jarak besar, $c_D \to -c_0$, dan fungsi gelombang menjadi kovalen murni: CI penuh memperbaiki kegagalan disosiasi RHF (Gambar 17.g02).
:::

::: {.contoh}
**Contoh 17.c31 · Tangga metode untuk H₂O dalam basis minimal**

Untuk H₂O/STO-3G pada geometri percobaan, energi korelasi dari program pendamping: MP2 $-0{,}035493$; CISD $-0{,}048773$; CISD+Q (koreksi Davidson) $-0{,}050013$; CCSD $-0{,}049359$; CCSD(T) $-0{,}049426$; CI penuh $-0{,}049475\ E_h$ (441 determinan). Hitung persentase korelasi FCI yang dipulihkan setiap metode dan galatnya dalam kJ/mol.

**Penyelesaian.** MP2 71,7% (galat 36,7 kJ/mol); CISD 98,6% (1,8 kJ/mol); CISD+Q 101,1% (−1,4 kJ/mol, terlampaui); CCSD 99,77% (0,30 kJ/mol); CCSD(T) 99,90% (0,13 kJ/mol).

**Memahami hasil.** Dalam basis minimal, MP2 relatif buruk karena celah energi orbital yang besar membuat penyebut teori perturbasi besar. CCSD(T) praktis menyamai CI penuh dengan biaya polinomial. CISD tampak baik untuk satu molekul kecil, tetapi masalahnya muncul ketika molekul-molekul dibandingkan (Contoh 17.c32). Dalam basis yang lebih besar urutannya serupa, dan CCSD(T) tetap paling dekat dengan FCI (Gambar 17.g07).
:::

![Gambar 17.g07 Kiri: persentase energi korelasi CI penuh yang dipulihkan berbagai metode untuk H₂O/STO-3G. Kanan: energi korelasi H₂O (geometri percobaan) untuk MP2, CCSD, dan CCSD(T) dengan basis STO-3G, 6-31G, dan 6-31G*, menunjukkan bahwa perluasan basis jauh lebih berpengaruh daripada perbedaan antarmetode.](fig/c_korelasi.png){width=94%}

::: {.contoh}
**Contoh 17.c32 · CISD tidak konsisten ukuran**

Dua molekul H₂ ($R = 1{,}4$ bohr) diletakkan berjauhan (50 bohr) dan dihitung bersama dengan basis STO-3G. Energi CISD sistem gabungan $-2{,}274042\ E_h$, sedangkan dua kali energi FCI satu molekul (yang untuk H₂ sama dengan CISD) adalah $-2{,}274552\ E_h$. Energi korelasi satu molekul $-0{,}020562\ E_h$. Hitung galat CISD dan pecahan korelasi yang dipulihkan. Bagaimana dengan CCSD?

**Penyelesaian.** Galat $-2{,}274042 - (-2{,}274552) = 0{,}000510\ E_h = 1{,}34$ kJ/mol. Korelasi yang dipulihkan $(0{,}041124 - 0{,}000510)/0{,}041124 = 98{,}8\%$. Program memberi energi korelasi CCSD gabungan $-0{,}041123\ E_h$, tepat dua kali korelasi satu molekul.

**Memahami hasil.** Untuk satu molekul H₂, CISD tepat (100%); untuk dua molekul yang tidak berinteraksi, hanya 98,8%. Untuk sepuluh molekul air atau protein kecil, galat ini menjadi puluhan kJ/mol dan merusak energi interaksi dan energi reaksi. Konsistensi ukuran adalah alasan utama CISD hampir tidak dipakai lagi, digantikan oleh *coupled-cluster*.
:::

::: {.contoh}
**Contoh 17.c33 · Koreksi Davidson**

Untuk H₂O/STO-3G, koefisien determinan HF dalam fungsi CISD ternormalisasi adalah $c_0 = 0{,}98720$ dan $E^\text{kor}_\text{CISD} = -0{,}048773\ E_h$. Hitung koreksi Davidson dan bandingkan dengan selisih FCI − CISD.

**Penyelesaian.** $1 - c_0^2 = 0{,}02543$; $\Delta E_Q = 0{,}02543 \times (-0{,}048773) = -0{,}001240\ E_h$. Selisih FCI − CISD $= -0{,}049475 - (-0{,}048773) = -0{,}000702\ E_h$.

**Memahami hasil.** Koreksi Davidson menaksir arah dengan benar tetapi melampaui sekitar 75% untuk sistem kecil ini; untuk molekul yang lebih besar dan basis yang lebih baik, taksirannya lebih seimbang. Rumus ini masih banyak dipakai bersama MRCI ("MRCI+Q"), tempat koreksi konsistensi ukuran tetap diperlukan.
:::

::: {.kuis}
**Kuis cepat 17.10**

Mengapa eksitasi tunggal tidak bercampur langsung dengan determinan HF, tetapi tetap muncul dalam fungsi gelombang CISD? Sebutkan satu sistem yang memerlukan korelasi statik.
:::

## 17.11 Teori perturbasi Møller–Plesset

### Membagi Hamiltonian

Christian Møller dan Milton Plesset (1934) menerapkan teori perturbasi Rayleigh–Schrödinger (subbab 8.6–8.7) dengan pembagian yang cerdik: Hamiltonian orde nol adalah jumlah operator Fock,

$$
\hat H^{(0)} = \sum_{i=1}^N\hat f(i), \qquad \hat V = \hat H - \hat H^{(0)} . \qquad \text{(17.e32)}
$$

Determinan HF adalah fungsi eigen $\hat H^{(0)}$ dengan nilai eigen $E^{(0)} = \sum_i\varepsilon_i$, dan setiap determinan tereksitasi juga fungsi eigen, dengan nilai eigen yang berbeda hanya pada energi orbital yang dipindah. Koreksi orde pertama $E^{(1)} = \langle\Phi_0|\hat V|\Phi_0\rangle$, dan dengan (17.e08) terlihat bahwa

$$
E^{(0)} + E^{(1)} = E_\text{HF} . \qquad \text{(17.e33)}
$$

Korelasi baru muncul pada orde kedua. Menurut rumus orde kedua, $E^{(2)} = \sum_I|\langle\Phi_I|\hat V|\Phi_0\rangle|^2/(E^{(0)} - E_I^{(0)})$. Eksitasi tunggal tidak menyumbang (teorema Brillouin), dan eksitasi rangkap tiga ke atas tidak terhubung dengan $\Phi_0$ (Condon–Slater); yang tersisa hanya eksitasi ganda. Hasilnya, dalam spin-orbital,

$$
E^{(2)}_\text{MP2} = \sum_{i<j}\sum_{a<b}\frac{|\langle ij||ab\rangle|^2}{\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b} , \qquad \text{(17.e34)}
$$

dengan $\langle ij||ab\rangle = \langle ij|ab\rangle - \langle ij|ba\rangle$ integral dua elektron terantisimetrikan. Untuk molekul kulit tertutup dalam orbital ruang,

$$
E^{(2)}_\text{MP2} = \sum_{ij}^\text{terisi}\sum_{ab}^\text{virtual}\frac{(ia|jb)\left[2(ia|jb) - (ib|ja)\right]}{\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b} . \qquad \text{(17.e35)}
$$

Penyebut selalu negatif, sehingga $E^{(2)} < 0$. MP2 memerlukan integral dalam basis orbital molekul, yang diperoleh dengan transformasi empat indeks berbiaya $N^5$; itulah skala MP2.

### Sifat dan keterbatasan

MP2 konsisten ukuran, relatif murah, dan biasanya memulihkan 80–95% energi korelasi dinamik dengan basis yang memadai. Ia memperbaiki geometri dan frekuensi HF secara nyata, dan cukup baik untuk ikatan hidrogen. Kelemahannya: (1) deret MP**n** (MP3, MP4, …) tidak selalu konvergen, dan bisa berosilasi atau menyimpang, terutama dengan basis berfungsi difus; (2) MP2 gagal bila celah HOMO–LUMO kecil, karena penyebut (17.e35) mendekati nol (korelasi statik); (3) MP2 melebih-lebihkan interaksi dispersi antarsistem π, misalnya pada dimer benzena.

Varian praktis yang populer: **RI-MP2** (atau DF-MP2) menghampiri integral empat pusat dengan basis bantu sehingga jauh lebih cepat; **SCS-MP2** (Stefan Grimme, 2003) memberi bobot berbeda pada sumbangan pasangan elektron berspin berlawanan dan berspin sama, $E = 1{,}2\,E_\text{os} + \tfrac13E_\text{ss}$, berdasarkan pengamatan bahwa MP2 menaksir kedua bagian dengan galat yang berbeda. Gagasan "MP2 dicampurkan ke dalam fungsional" melahirkan fungsional hibrida ganda (subbab 17.14).

::: {.contoh}
**Contoh 17.c34 · MP2 untuk H₂ dengan tangan**

Dalam basis minimal hanya ada satu eksitasi ganda, $\sigma_g^2 \to \sigma_u^2$. Dengan (17.e35) untuk satu orbital terisi (1) dan satu virtual (2): $E^{(2)} = (12|12)^2/[2(\varepsilon_1 - \varepsilon_2)]$, dengan $(12|12) = K_{12}$. Hitung untuk $K_{12} = 0{,}1813$, $\varepsilon_1 = -0{,}5782$, $\varepsilon_2 = 0{,}6703\ E_h$, dan bandingkan dengan energi korelasi CI penuh ($-0{,}0206\ E_h$).

**Penyelesaian.** $(ia|jb) = (12|12) = 0{,}1813$; pembilang $(12|12)[2(12|12) - (12|12)] = K_{12}^2 = 0{,}03286$. Penyebut $2(-0{,}5782) - 2(0{,}6703) = -2{,}4970$. $E^{(2)} = -0{,}01316\ E_h$, yaitu 64% korelasi FCI.

**Memahami hasil.** Untuk sistem dua tingkat ini, CI penuh adalah $\tfrac12\Delta - \sqrt{\tfrac14\Delta^2 + K^2}$ dengan $\Delta = H_{DD} - H_{00}$, dan uraian untuk $K$ kecil memberi $-K^2/\Delta$, dengan $\Delta = 1{,}577$, bukan $2(\varepsilon_2 - \varepsilon_1) = 2{,}497$. Penyebut MP2 memakai selisih energi orbital, yang melebih-lebihkan energi konfigurasi tereksitasi karena mengabaikan tarikan antara elektron tereksitasi dan lubangnya. Teori perturbasi berbasis Hartree–Fock karena itu konservatif.
:::

::: {.contoh}
**Contoh 17.c35 · MP2 dan basis**

Energi korelasi MP2 H₂O (semua elektron, geometri percobaan): STO-3G $-0{,}0355$; 6-31G $-0{,}1288$; 6-31G* $-0{,}1885\ E_h$. Taksiran batas basis lengkap sekitar $-0{,}36\ E_h$ untuk semua elektron. Berapa persen yang diperoleh setiap basis? Mengapa fungsi d begitu penting?

**Penyelesaian.** Dengan acuan $-0{,}36$: STO-3G 10%; 6-31G 36%; 6-31G* 52%.

**Memahami hasil.** Energi korelasi jauh lebih lambat konvergen terhadap basis daripada energi HF: untuk elektron saling menghindar secara sudut (satu di atas, satu di bawah), fungsi gelombang memerlukan fungsi dengan momentum sudut lebih tinggi daripada orbital terisi. Fungsi d pada oksigen membuka "korelasi sudut" pertama, menambah 0,06 $E_h$ sekaligus. Itulah sebabnya basis untuk perhitungan korelasi selalu memuat polarisasi, dan mengapa basis cc-pVXZ menambah fungsi d, f, g secara bertahap.
:::

::: {.contoh}
**Contoh 17.c36 · Spin sejajar dan spin berlawanan**

Untuk H₂O/6-31G*, energi MP2 terpecah menjadi sumbangan pasangan berspin berlawanan $E_\text{os} = -0{,}14018$ dan berspin sama $E_\text{ss} = -0{,}04830\ E_h$. Hitung energi SCS-MP2 dan bandingkan dengan MP2 dan CCSD(T) ($-0{,}19915\ E_h$).

**Penyelesaian.** MP2: $-0{,}18847$. SCS-MP2: $1{,}2(-0{,}14018) + \tfrac13(-0{,}04830) = -0{,}16822 - 0{,}01610 = -0{,}18431\ E_h$.

**Memahami hasil.** Pasangan berspin berlawanan menyumbang 74% korelasi MP2: elektron berspin sama sudah dijauhkan oleh lubang Fermi, sehingga masih sedikit yang tersisa untuk dikorelasikan. Untuk molekul tunggal ini, SCS-MP2 justru sedikit lebih jauh dari CCSD(T); keunggulan SCS-MP2 tampak pada energi reaksi dan interaksi antarmolekul, tempat galat sistematis MP2 berbeda untuk kedua komponen. Ini mengingatkan bahwa perbaikan empiris dinilai secara statistik atas banyak sistem, bukan dari satu molekul.
:::

::: {.kuis}
**Kuis cepat 17.11**

Mengapa energi MP1 tidak memberi korelasi apa pun? Apa yang terjadi pada MP2 bila celah HOMO–LUMO mendekati nol?
:::

## 17.12 Metode coupled-cluster dan metode komposit

### Ansatz eksponensial

Metode *coupled-cluster* (CC), yang diperkenalkan ke kimia kuantum oleh Jiří Čížek dan Josef Paldus pada tahun 1960-an, menulis fungsi gelombang sebagai

$$
\Psi_\text{CC} = e^{\hat T}\Phi_0 = \left(1 + \hat T + \tfrac12\hat T^2 + \tfrac16\hat T^3 + \cdots\right)\Phi_0, \qquad \hat T = \hat T_1 + \hat T_2 + \hat T_3 + \cdots , \qquad \text{(17.e36)}
$$

dengan operator eksitasi $\hat T_1\Phi_0 = \sum_{ia}t_i^a\Phi_i^a$ dan $\hat T_2\Phi_0 = \sum_{i<j,a<b}t_{ij}^{ab}\Phi_{ij}^{ab}$. Koefisien $t$ disebut **amplitudo**. Bila $\hat T$ dipotong pada $\hat T_1 + \hat T_2$ (**CCSD**), eksponensialnya tetap memuat suku $\tfrac12\hat T_2^2$, yaitu eksitasi kuadrupel yang tersusun dari dua eksitasi ganda yang independen. Suku-suku "tak terhubung" inilah yang dibuang CISD, dan inilah yang membuat CC konsisten ukuran: untuk dua sistem yang tidak berinteraksi, $\hat T = \hat T_A + \hat T_B$, sehingga $e^{\hat T} = e^{\hat T_A}e^{\hat T_B}$ dan fungsi gelombang menjadi hasil kali.

Amplitudo tidak ditentukan dengan metode variasi (yang akan memerlukan semua suku deret), melainkan dengan memproyeksikan persamaan Schrödinger:

$$
\langle\Phi_0|\bar H|\Phi_0\rangle = E_\text{CC}, \qquad \langle\Phi_i^a|\bar H|\Phi_0\rangle = 0, \qquad \langle\Phi_{ij}^{ab}|\bar H|\Phi_0\rangle = 0, \qquad \bar H = e^{-\hat T}\hat He^{\hat T} . \qquad \text{(17.e37)}
$$

Karena $\hat H$ hanya memuat operator dua elektron, uraian $\bar H$ berhenti setelah empat komutator, sehingga persamaannya tertutup. Persamaan amplitudo tak linear dan diselesaikan secara iteratif, mirip SCF. Energinya hanya bergantung pada amplitudo tunggal dan ganda:

$$
E_\text{CC} = E_\text{HF} + \sum_{ia}f_{ia}t_i^a + \tfrac14\sum_{ijab}\langle ij||ab\rangle\left(t_{ij}^{ab} + 2t_i^at_j^b\right) . \qquad \text{(17.e38)}
$$

CC tidak variasional, sehingga energinya dapat sedikit di bawah energi tepat, tetapi dalam praktik hal ini jarang menjadi masalah untuk molekul dekat geometri setimbang.

### CCSD(T): standar emas

CCSD berbiaya $N^6$. Menambahkan $\hat T_3$ penuh (CCSDT, $N^8$) terlalu mahal untuk pemakaian rutin. Raghavachari, Trucks, Pople, dan Head-Gordon (1989) mengusulkan **CCSD(T)**: sumbangan eksitasi rangkap tiga ditaksir dengan teori perturbasi memakai amplitudo CCSD, dengan biaya $N^7$ satu kali (tanpa iterasi). Dengan basis besar dan ekstrapolasi CBS, CCSD(T) memberi energi reaksi dan penghalang dengan galat sekitar 1–4 kJ/mol untuk molekul yang didominasi satu determinan. Ia disebut **standar emas** kimia kuantum dan menjadi patokan untuk menilai DFT dan metode lain. Untuk mengetahui apakah satu determinan cukup, program mencetak **diagnostik T1** (norma amplitudo tunggal); nilai di atas sekitar 0,02 untuk molekul organik menandakan korelasi statik yang berarti, dan CCSD(T) mulai tidak dapat dipercaya.

### Metode komposit

Perhitungan CCSD(T) dengan basis sangat besar tetap mahal. **Metode komposit** memanfaatkan aditivitas: koreksi basis dihitung dengan metode murah, koreksi korelasi tingkat tinggi dengan basis kecil, lalu dijumlahkan. Gagasan intinya:

$$
E[\text{CCSD(T)/basis besar}] \approx E[\text{CCSD(T)/basis kecil}] + E[\text{MP2/basis besar}] - E[\text{MP2/basis kecil}] . \qquad \text{(17.e39)}
$$

Resep baku seperti **Gaussian-n** (G3, G4), **CBS-QB3**, dan **Weizmann-n** (W1, W2, W4) menambahkan geometri dan frekuensi dari DFT, koreksi elektron inti, koreksi relativistik, kopling spin–orbit, dan (untuk G-n) koreksi empiris kecil. G4 memberi galat rata-rata sekitar 3–4 kJ/mol pada himpunan uji ratusan entalpi pembentukan; W1 dan W4 mencapai di bawah 2 kJ/mol untuk molekul kecil, sebanding dengan ketidakpastian banyak data termokimia percobaan. Metode-metode ini menjadikan komputasi sumber termokimia yang setara dengan kalorimetri untuk molekul kecil.

::: {.contoh}
**Contoh 17.c37 · CCSD konsisten ukuran, CISD tidak**

Untuk dua molekul H₂ yang berjauhan (Contoh 17.c32), tuliskan suku-suku $e^{\hat T}$ dengan $\hat T = \hat T_2^A + \hat T_2^B$ sampai orde kedua dan tunjukkan suku yang memuat eksitasi kuadrupel.

**Penyelesaian.** $e^{\hat T}\Phi_0 = [1 + \hat T_2^A + \hat T_2^B + \tfrac12(\hat T_2^A + \hat T_2^B)^2 + \cdots]\Phi_0$. Suku $\tfrac12(\hat T_2^A)^2$ dan $\tfrac12(\hat T_2^B)^2$ nol, karena dalam basis minimal tiap molekul hanya mempunyai satu eksitasi ganda dan tidak dapat dieksitasi dua kali. Suku silang $\tfrac12 \cdot 2\,\hat T_2^A\hat T_2^B\Phi_0 = t^At^B\,\Phi^{AB}_\text{ganda+ganda}$ adalah eksitasi kuadrupel dengan koefisien hasil kali amplitudo masing-masing.

**Memahami hasil.** Koefisien kuadrupel CC bukan parameter baru; ia ditentukan oleh amplitudo ganda. Itulah sebabnya CC memulihkan $2 \times$ korelasi satu molekul secara tepat (program: $-0{,}041123\ E_h$), sedangkan CISD tidak dapat memuat konfigurasi itu sama sekali. Dalam molekul nyata, kuadrupel tak terhubung $\tfrac12\hat T_2^2$ menyumbang sebagian besar efek kuadrupel, dan kuadrupel "terhubung" $\hat T_4$ sangat kecil.
:::

::: {.contoh}
**Contoh 17.c38 · Aditivitas ala metode komposit**

Untuk H₂O (geometri percobaan), program pendamping memberi energi korelasi: CCSD(T)/6-31G $-0{,}136316$; MP2/6-31G $-0{,}128796$; MP2/6-31G* $-0{,}188472$; CCSD(T)/6-31G* $-0{,}199154\ E_h$. Taksir CCSD(T)/6-31G* dengan (17.e39) dan hitung galatnya.

**Penyelesaian.** $-0{,}136316 + (-0{,}188472 + 0{,}128796) = -0{,}195992\ E_h$. Galat terhadap nilai sebenarnya: $0{,}003162\ E_h = 8{,}3$ kJ/mol.

**Memahami hasil.** Galat 8 kJ/mol pada energi korelasi **total** tampak besar, tetapi metode komposit dipakai untuk **selisih** energi (energi atomisasi, reaksi), tempat sebagian besar galat aditivitas meniadakan diri. Juga, basis 6-31G dan 6-31G* terlalu kecil; aditivitas jauh lebih baik antara pasangan basis yang lebih besar, misalnya cc-pVTZ dan cc-pVQZ, karena di sana kedua metode sudah "melihat" bentuk korelasi yang serupa.
:::

::: {.contoh}
**Contoh 17.c39 · Memilih metode dengan anggaran tetap**

Seorang mahasiswa ingin menghitung energi reaksi isomerisasi molekul organik C₆ (sekitar 150 fungsi basis cc-pVTZ) dengan ketelitian 4 kJ/mol. CCSD(T)/cc-pVTZ untuk molekul ini memakan 20 jam per struktur pada komputernya. Bila ia hanya mempunyai satu malam, strategi apa yang masuk akal?

**Penyelesaian.** Optimasi geometri dan frekuensi dengan DFT (subbab 17.14) untuk kedua isomer, lalu energi titik tunggal dengan DLPNO-CCSD(T)/cc-pVTZ (berskala hampir linear, biasanya 1–2% dari biaya CCSD(T) kanonik untuk ukuran ini) atau, bila tidak tersedia, CCSD(T)/cc-pVDZ ditambah koreksi basis MP2 cc-pVDZ → cc-pVTZ menurut (17.e39). Biaya CCSD(T)/cc-pVDZ (sekitar 70 fungsi) kira-kira $(70/150)^7 \approx 0{,}5\%$ dari cc-pVTZ, yaitu beberapa menit.

**Memahami hasil.** Kimia komputasi praktis adalah seni membagi pekerjaan: geometri dari metode murah (yang galatnya pada geometri kecil), energi dari metode mahal pada geometri itu, dan koreksi basis dari metode murah. Notasi untuk strategi pertama adalah DLPNO-CCSD(T)/cc-pVTZ//B3LYP-D3/def2-TZVP, dan resep semacam ini kini rutin dalam studi mekanisme reaksi.
:::

::: {.kuis}
**Kuis cepat 17.12**

Apa yang membuat CCSD memuat eksitasi kuadrupel meskipun $\hat T$ hanya berisi $\hat T_1$ dan $\hat T_2$? Mengapa (T) dalam CCSD(T) ditulis dalam kurung?
:::
