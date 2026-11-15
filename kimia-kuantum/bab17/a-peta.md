# Bab 17 Kimia Komputasi

Pada tahun 1929 Paul Dirac menulis bahwa hukum-hukum fisika yang mendasari sebagian besar fisika dan seluruh kimia sudah diketahui sepenuhnya; kesulitannya hanyalah bahwa penerapan hukum-hukum itu menghasilkan persamaan yang terlalu rumit untuk diselesaikan. Kita sudah merasakan kesulitan itu di Contoh 1.2: fungsi gelombang benzena pada kisi yang sangat kasar memerlukan lebih banyak angka daripada jumlah atom di alam semesta. Namun hari ini seorang mahasiswa dapat mengetik beberapa baris berisi koordinat atom, menekan tombol, dan dalam beberapa menit memperoleh geometri molekul obat dengan ketelitian seperseratus angstrom, spektrum inframerahnya, muatan atom-atomnya, dan energi reaksinya dengan galat beberapa kilojoule per mol. Energi total molekul air sekitar $-76{,}4$ hartree, sedangkan ketelitian yang diperlukan kimia sekitar satu milihartree, yaitu satu bagian dalam seratus ribu. Bagaimana sebuah program menembus jurang antara persamaan yang mustahil diselesaikan dan angka yang cukup teliti untuk merancang katalis?

Jawabannya adalah rangkaian hampiran yang tersusun rapi, masing-masing dapat diperbaiki secara sistematis. Elektron pertama-tama dianggap bergerak dalam medan rata-rata elektron lain (**Hartree–Fock**), orbital-orbitalnya diuraikan atas sejumlah berhingga fungsi Gauss (**himpunan basis**), lalu gerak elektron yang saling menghindar (**korelasi**) ditambahkan dengan interaksi konfigurasi, teori perturbasi, atau metode *coupled-cluster*. Jalan lain, yang kini paling banyak dipakai, melepaskan fungsi gelombang sama sekali dan bekerja dengan kerapatan elektron yang hanya bergantung pada tiga koordinat (**teori fungsional kerapatan**, DFT). Untuk molekul yang sangat besar, metode semiempiris dan mekanika molekul mengorbankan ketelitian demi kecepatan.

Bab ini adalah puncak buku. Hampir setiap bab sebelumnya menyumbang bahannya: teorema variasi dan teori perturbasi (Bab 8), determinan Slater dan aturan Condon–Slater (Bab 9), hampiran Born–Oppenheimer dan LCAO (Bab 11), simetri (Bab 10), getaran (Bab 5), dan spektroskopi (Bab 15 dan 16). Kita akan menurunkan persamaan Hartree–Fock dan Roothaan, menulis sendiri program SCF kecil dengan Python, mengikuti perhitungan molekul air dari integral sampai muatan atom, lalu menapaki tangga metode korelasi dan fungsional kerapatan. Bab ditutup dengan apa yang paling diperlukan pemakai: cara memilih metode, membaca keluaran program, dan menghindari jebakan yang lazim.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa hampir semua metode kimia kuantum dimulai dari gambaran "satu elektron dalam medan rata-rata"?
2. Mengapa orbital molekul diuraikan atas fungsi Gauss, padahal orbital atom hidrogen berbentuk eksponensial?
3. Apa arti energi orbital yang dicetak program, dan mengapa ia dapat dipakai untuk menaksir energi ionisasi?
4. Mengapa muatan atom hasil perhitungan berubah-ubah bila himpunan basisnya diganti, sedangkan momen dipolnya tidak?
5. Apa yang hilang dalam Hartree–Fock, dan berapa harganya dalam kilojoule per mol?
6. Bagaimana teori fungsional kerapatan dapat bekerja hanya dengan kerapatan elektron, dan mengapa ada begitu banyak fungsional?
7. Bagaimana komputer menemukan geometri molekul, keadaan transisi, dan frekuensi getarannya?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menempatkan metode ab initio, DFT, semiempiris, dan mekanika molekul pada peta biaya–ketelitian.
2. Menurunkan ungkapan energi Hartree–Fock dan persamaan Fock, serta membedakan RHF, UHF, dan ROHF.
3. Menurunkan persamaan Roothaan, menjalankan prosedur SCF, dan menulis program SCF minimal untuk H₂ dan HeH⁺.
4. Memakai teorema Koopmans untuk menaksir energi ionisasi dan menilai keterbatasannya.
5. Memilih himpunan basis (STO-3G, split-valence, polarisasi, difus, berkorelasi konsisten) dan memahami ekstrapolasi basis serta galat superposisi basis.
6. Mengikuti dan menafsirkan perhitungan SCF lengkap untuk molekul air.
7. Menghitung muatan Mulliken dan Löwdin serta momen dipol, dan menilai kebergantungannya pada basis.
8. Menjelaskan orbital terlokalisasi dan hubungannya dengan gambaran ikatan klasik.
9. Menjelaskan optimasi geometri, analisis frekuensi, dan perhitungan besaran termodinamika dari hasil komputasi.
10. Mendefinisikan energi korelasi dan menghitungnya dengan interaksi konfigurasi, MP2, dan *coupled-cluster*.
11. Menjelaskan teorema Hohenberg–Kohn, persamaan Kohn–Sham, dan tangga fungsional LDA, GGA, meta-GGA, hibrida.
12. Menangani interaksi nonkovalen, efek pelarut, dan efek relativistik dalam perhitungan.
13. Menentukan keadaan transisi dan menghitung laju reaksi dengan teori keadaan transisi.
14. Memahami dasar metode semiempiris dan medan gaya mekanika molekul.
15. Merancang alur kerja perhitungan dan membaca keluaran program kimia kuantum.
:::

::: {.mat}
**Prasyarat**

Dari Bab 1: skala energi dan ketelitian kimia (subbab 1.10, Contoh 1.52). Dari Bab 2: integral Gauss dan hasil kali fungsi Gauss (subbab 2.2), matriks, nilai eigen, dan diagonalisasi (2.7–2.8), satuan atom (2.11). Dari Bab 5: osilator harmonik dan mode normal (5.4, 5.11). Dari Bab 8: teorema variasi dan persamaan sekuler (subbab 8.2–8.5), teori perturbasi (8.6–8.7). Dari Bab 9: determinan Slater (subbab 9.6), Hartree–Fock untuk atom (9.8), korelasi elektron (9.10), aturan Condon–Slater (9.14). Dari Bab 10: tabel karakter dan label simetri orbital. Dari Bab 11: hampiran Born–Oppenheimer (subbab 11.1), LCAO (11.4), molekul H₂ dan interaksi konfigurasi (11.10–11.12). Dari Bab 13: metode Hückel (subbab 13.4).
:::

## 17.1 Peta metode: ab initio, DFT, semiempiris, mekanika molekul

### Satu persamaan, banyak hampiran

Dalam hampiran Born–Oppenheimer (subbab 11.1), inti dianggap diam pada posisi $\{\mathbf R_A\}$, dan elektron mematuhi persamaan Schrödinger elektronik dengan Hamiltonian (dalam satuan atom)

$$
\hat H_\text{el} = -\sum_{i=1}^N\frac12\nabla_i^2 - \sum_{i=1}^N\sum_A\frac{Z_A}{r_{iA}} + \sum_{i<j}\frac1{r_{ij}} , \qquad \text{(17.1)}
$$

ditambah tolakan antarinti $V_{NN} = \sum_{A<B}Z_AZ_B/R_{AB}$ yang tetap untuk geometri tertentu. Penyelesaian $\hat H_\text{el}\Psi = E_\text{el}\Psi$ untuk banyak geometri memberi **permukaan energi potensial** $E(\{\mathbf R_A\}) = E_\text{el} + V_{NN}$, yang menentukan seluruh kimia molekul itu: geometri setimbang (minimum), frekuensi getaran (kelengkungan di minimum), energi reaksi (selisih minimum), dan penghalang reaksi (titik pelana). Kesulitannya ada pada suku terakhir (17.1): tolakan $1/r_{ij}$ mengikat gerak semua elektron sehingga persamaan tidak terpisah menjadi persamaan satu elektron.

Kimia komputasi menawarkan sederet metode yang menangani kesulitan itu dengan cara dan harga yang berbeda:

- **Metode ab initio** ("dari awal") hanya memakai tetapan fisika dasar. Hartree–Fock (HF) mengganti tolakan sesaat dengan medan rata-rata; metode **pasca-HF** (interaksi konfigurasi, teori perturbasi Møller–Plesset, *coupled-cluster*) menambahkan korelasi dan dapat diperbaiki secara sistematis menuju jawaban tepat.
- **Teori fungsional kerapatan** (DFT) menghitung energi sebagai fungsional kerapatan elektron. Secara prinsip tepat, tetapi bentuk fungsional pertukaran–korelasi tidak diketahui dan harus dihampiri; dalam praktik ketelitiannya mendekati metode korelasi dengan biaya mendekati HF.
- **Metode semiempiris** (AM1, PM7, GFN-xTB) memakai kerangka HF atau DFT tetapi mengabaikan sebagian besar integral dan menggantinya dengan parameter yang dicocokkan dengan data percobaan.
- **Mekanika molekul** (medan gaya AMBER, CHARMM, OPLS) meninggalkan elektron sama sekali: energi dihitung dari pegas ikatan, sudut, torsi, dan interaksi van der Waals serta Coulomb antaratom.

### Biaya: hukum pangkat

Waktu perhitungan tumbuh menurut pangkat ukuran sistem, yang diukur dengan banyaknya fungsi basis $N$. Untuk HF, pekerjaan terbesar adalah integral tolakan dua elektron, yang banyaknya sebanding dengan $N^4$; teknik modern menurunkannya mendekati $N^2$–$N^3$ untuk molekul besar. MP2 berskala $N^5$, CCSD $N^6$, CCSD(T) $N^7$, dan interaksi konfigurasi penuh tumbuh secara eksponensial. DFT dengan fungsional lokal berskala sekitar $N^3$–$N^4$, semiempiris sekitar $N^2$–$N^3$, dan mekanika molekul hampir linear. Hukum pangkat ini lebih menentukan daripada kecepatan komputer: melipatduakan ukuran molekul membuat perhitungan CCSD(T) $2^7 = 128$ kali lebih lama, dan komputer yang seratus kali lebih cepat hanya memperbesar molekul yang dapat dihitung sekitar dua kali.

| Metode | Skala biaya | Galat khas energi reaksi | Ukuran sistem praktis |
|---|---|---|---|
| Mekanika molekul | $N$–$N^2$ | tidak berlaku untuk reaksi | $10^5$–$10^6$ atom |
| Semiempiris | $N^2$–$N^3$ | 20–40 kJ/mol | $10^3$–$10^4$ atom |
| Hartree–Fock | $N^3$–$N^4$ | 20–100 kJ/mol | $10^2$–$10^3$ atom |
| DFT (GGA, hibrida) | $N^3$–$N^4$ | 8–20 kJ/mol | $10^2$–$10^3$ atom |
| MP2 | $N^5$ | 10–20 kJ/mol | 50–200 atom |
| CCSD(T) | $N^7$ | sekitar 4 kJ/mol (dengan basis besar) | 10–30 atom |
| CI penuh | eksponensial | tepat dalam basis | 2–6 atom kecil |

Angka-angka dalam tabel hanyalah kisaran kasar, tetapi polanya penting: setiap langkah naik dalam ketelitian dibayar dengan pangkat yang lebih tinggi.

### Dua sumbu ketelitian

John Pople, yang bersama Walter Kohn menerima Hadiah Nobel Kimia 1998, menggambarkan kualitas perhitungan ab initio dengan diagram dua sumbu (Gambar 17.1). Sumbu pertama adalah **himpunan basis**: makin banyak fungsi basis, makin dekat orbital ke bentuk sebenarnya. Sumbu kedua adalah **perlakuan korelasi**: HF, MP2, CCSD, CCSD(T), sampai CI penuh. Jawaban tepat persamaan Schrödinger (nonrelativistik, dalam hampiran Born–Oppenheimer) terletak di pojok basis tak berhingga dan CI penuh. Setiap perhitungan nyata adalah satu titik di bidang ini, dan notasinya menyebut kedua koordinat, dipisah garis miring: "MP2/6-31G*" berarti teori MP2 dengan basis 6-31G*, dan "CCSD(T)/cc-pVTZ//B3LYP/6-31G*" berarti energi CCSD(T)/cc-pVTZ dihitung pada geometri yang dioptimasi dengan B3LYP/6-31G*.

![Gambar 17.1 Diagram Pople. Sumbu mendatar: tingkat perlakuan korelasi; sumbu tegak: ukuran himpunan basis. Jawaban tepat terletak di pojok kanan atas. Angka di setiap kotak adalah energi korelasi atau energi total H₂O (geometri percobaan) yang dihitung dengan program pendamping bab ini; tanda panah menunjukkan arah perbaikan sistematis.](fig/c_pople.png){width=86%}

Untuk DFT, Perdew mengusulkan gambaran serupa yang disebut **tangga Yakub**: anak tangga LDA, GGA, meta-GGA, hibrida, dan fungsional dengan orbital tak terisi, masing-masing menambah bahan baru ke dalam fungsional (subbab 17.14). Berbeda dengan diagram Pople, menaiki tangga Yakub tidak menjamin hasil yang lebih baik untuk setiap sifat, karena fungsional-fungsional itu adalah hampiran yang tidak dapat diperbaiki secara sistematis.

### Ketelitian kimia

Sasaran yang lazim adalah **ketelitian kimia**, sekitar 1 kkal/mol (4,2 kJ/mol), cukup untuk meramalkan tetapan kesetimbangan dalam faktor lima dan laju reaksi dalam faktor yang sama (subbab 17.16). Dalam satuan atom, 1 kkal/mol sama dengan 1,59 m$E_h$ (Contoh 1.52). Yang membuat sasaran ini sulit adalah bahwa ia harus dicapai pada **selisih** energi total yang sangat besar. Untunglah galat metode sering sistematis dan saling meniadakan bila dua struktur yang mirip dibandingkan; seluruh seni kimia komputasi terapan adalah memanfaatkan peniadaan galat ini sambil mengetahui kapan ia gagal.

::: {.inti}
**Inti subbab 17.1**

- Permukaan energi potensial, yang diperoleh dari persamaan Schrödinger elektronik pada banyak geometri, menentukan struktur, getaran, dan reaktivitas.
- Metode kimia komputasi membentuk hierarki biaya–ketelitian: mekanika molekul, semiempiris, HF, DFT, MP2, CCSD(T), CI penuh.
- Kualitas perhitungan ab initio ditentukan oleh dua sumbu: himpunan basis dan perlakuan korelasi.
- Biaya tumbuh menurut pangkat ukuran sistem, sehingga pilihan metode adalah kompromi.
:::

::: {.contoh}
**Contoh 17.1 · Harga melipatduakan molekul**

Perhitungan MP2 untuk molekul berukuran 20 atom berat selesai dalam 10 menit, dan CCSD(T) untuk molekul yang sama dalam 10 jam. Taksir waktu keduanya untuk molekul serupa berukuran 40 atom berat dengan basis yang setara.

**Penyelesaian.** Banyaknya fungsi basis berlipat dua. MP2 ($N^5$): $10 \times 2^5 = 320$ menit, sekitar 5,3 jam. CCSD(T) ($N^7$): $10 \times 2^7 = 1280$ jam, sekitar 53 hari.

**Memahami hasil.** Molekul dua kali lebih besar membuat CCSD(T) praktis tidak terjangkau tanpa trik tambahan. Inilah sebabnya CCSD(T) "kanonik" dipakai untuk molekul kecil sebagai patokan, sedangkan molekul besar dihitung dengan DFT atau dengan varian CCSD(T) terlokalisasi (misalnya DLPNO-CCSD(T)) yang memanfaatkan kenyataan bahwa korelasi elektron sebagian besar bersifat lokal.
:::

::: {.contoh}
**Contoh 17.2 · Ketelitian relatif yang diperlukan**

Energi total H₂O sekitar $-76{,}4\ E_h$. Nyatakan ketelitian kimia (1 kkal/mol) sebagai pecahan energi total. Bandingkan dengan menimbang kapten kapal beserta kapalnya (50 000 ton) untuk mengetahui berat topinya.

**Penyelesaian.** 1 kkal/mol $= 1/627{,}51\ E_h = 1{,}594 \times 10^{-3}\ E_h$. Pecahannya $1{,}594 \times 10^{-3}/76{,}4 = 2{,}1 \times 10^{-5}$. Dengan pecahan yang sama, kapal 50 000 ton memerlukan ketelitian sekitar 1 ton.

**Memahami hasil.** Untuk molekul yang lebih besar, misalnya obat dengan 50 atom, energi totalnya ribuan hartree, dan ketelitian relatif yang diperlukan menjadi $10^{-6}$ atau lebih kecil. Tidak ada metode hampiran yang mencapai ketelitian mutlak ini; yang dimanfaatkan adalah peniadaan galat antara reaktan dan produk, karena elektron-elektron inti dan sebagian besar elektron valensi hampir tidak berubah selama reaksi.
:::

::: {.contoh}
**Contoh 17.3 · Berapa determinan dalam CI penuh?**

Fungsi gelombang CI penuh adalah kombinasi semua determinan Slater yang dapat dibentuk dari $n$ orbital ruang dengan $N_\alpha$ elektron spin α dan $N_\beta$ elektron spin β; banyaknya $\binom{n}{N_\alpha}\binom{n}{N_\beta}$. Hitung untuk H₂O (5 elektron α, 5 elektron β) dengan basis STO-3G (7 orbital), 6-31G (13), dan cc-pVDZ (24).

**Penyelesaian.** STO-3G: $\binom75^2 = 21^2 = 441$. 6-31G: $\binom{13}{5}^2 = 1287^2 = 1{,}66 \times 10^6$. cc-pVDZ: $\binom{24}{5}^2 = 42\,504^2 = 1{,}81 \times 10^9$.

**Memahami hasil.** CI penuh H₂O dengan basis STO-3G dapat dihitung dalam sekejap dengan program kecil (subbab 17.10), tetapi dengan basis yang masih sederhana seperti cc-pVDZ diperlukan hampir dua miliar koefisien. Untuk benzena dengan cc-pVDZ, banyaknya determinan sekitar $10^{45}$. Pertumbuhan eksponensial inilah yang memaksa kita mencari metode korelasi yang biayanya hanya polinomial.
:::

::: {.kuis}
**Kuis cepat 17.1**

Apa arti notasi "B3LYP/6-31G*" dan "CCSD(T)/cc-pVTZ//MP2/cc-pVDZ"? Mengapa komputer yang seribu kali lebih cepat hanya memungkinkan perhitungan CCSD(T) pada molekul sekitar 2,7 kali lebih besar?
:::

## 17.2 Hartree–Fock untuk molekul

### Determinan Slater dan energinya

Hampiran Hartree–Fock menulis fungsi gelombang $N$ elektron sebagai satu **determinan Slater** (subbab 9.6) yang tersusun dari spin-orbital $\chi_i(\mathbf x) = \psi_i(\mathbf r)\sigma(s)$, dengan $\sigma = \alpha$ atau $\beta$:

$$
\Psi_0 = \frac{1}{\sqrt{N!}}\begin{vmatrix}\chi_1(\mathbf x_1) & \chi_2(\mathbf x_1) & \cdots & \chi_N(\mathbf x_1)\\ \chi_1(\mathbf x_2) & \chi_2(\mathbf x_2) & \cdots & \chi_N(\mathbf x_2)\\ \vdots & & & \vdots\\ \chi_1(\mathbf x_N) & \chi_2(\mathbf x_N) & \cdots & \chi_N(\mathbf x_N)\end{vmatrix} \equiv |\chi_1\chi_2\cdots\chi_N| . \qquad \text{(17.2)}
$$

Determinan otomatis antisimetris terhadap pertukaran dua elektron dan memenuhi asas Pauli. Spin-orbital dipilih ortonormal. Nilai harap Hamiltonian (17.1) untuk determinan ini diberikan oleh aturan Condon–Slater (subbab 9.14):

$$
E_0 = \langle\Psi_0|\hat H_\text{el}|\Psi_0\rangle = \sum_{i=1}^N h_{ii} + \frac12\sum_{i=1}^N\sum_{j=1}^N\left(J_{ij} - K_{ij}\right) , \qquad \text{(17.3)}
$$

dengan integral satu elektron (energi kinetik ditambah tarikan semua inti)

$$
h_{ii} = \int\chi_i^*(\mathbf x_1)\left[-\tfrac12\nabla_1^2 - \sum_A\frac{Z_A}{r_{1A}}\right]\chi_i(\mathbf x_1)\,d\mathbf x_1 ,
$$

**integral Coulomb**

$$
J_{ij} = \iint\frac{|\chi_i(\mathbf x_1)|^2\,|\chi_j(\mathbf x_2)|^2}{r_{12}}\,d\mathbf x_1d\mathbf x_2 ,
$$

dan **integral pertukaran**

$$
K_{ij} = \iint\frac{\chi_i^*(\mathbf x_1)\chi_j(\mathbf x_1)\,\chi_j^*(\mathbf x_2)\chi_i(\mathbf x_2)}{r_{12}}\,d\mathbf x_1d\mathbf x_2 .
$$

$J_{ij}$ adalah tolakan klasik antara awan muatan elektron $i$ dan $j$. $K_{ij}$ tidak mempunyai padanan klasik; ia muncul dari antisimetri dan hanya tidak nol bila $\chi_i$ dan $\chi_j$ berspin sama. Perhatikan bahwa suku $i = j$ dalam jumlah ganda aman, karena $J_{ii} = K_{ii}$: **Hartree–Fock bebas dari interaksi diri**, sifat yang akan menjadi penting ketika kita membandingkannya dengan DFT (subbab 17.14).

Untuk molekul **kulit tertutup** dengan $N/2$ orbital ruang yang masing-masing diisi dua elektron berspin berlawanan, integrasi atas spin memberi

$$
E_0 = 2\sum_{a=1}^{N/2}h_{aa} + \sum_{a=1}^{N/2}\sum_{b=1}^{N/2}\left(2J_{ab} - K_{ab}\right) , \qquad \text{(17.4)}
$$

kini dengan integral atas orbital ruang. Faktor 2 pada $J$ berasal dari kenyataan bahwa setiap elektron di orbital $a$ ditolak oleh kedua elektron di orbital $b$, sedangkan pertukaran hanya terjadi antarelektron berspin sama.

### Persamaan Hartree–Fock

Orbital terbaik adalah orbital yang meminimumkan $E_0$ dengan syarat tetap ortonormal (teorema variasi, subbab 8.2). Hasilnya, yang diturunkan di kotak berikut, adalah **persamaan Hartree–Fock**:

$$
\hat f\,\chi_i = \varepsilon_i\,\chi_i, \qquad \hat f(1) = \hat h(1) + \sum_{j=1}^N\left[\hat J_j(1) - \hat K_j(1)\right] , \qquad \text{(17.5)}
$$

dengan $\hat f$ **operator Fock**, $\hat h$ operator satu elektron, dan operator Coulomb serta pertukaran didefinisikan oleh kerjanya pada fungsi sembarang $\chi$:

$$
\hat J_j(1)\chi(1) = \left[\int\frac{|\chi_j(2)|^2}{r_{12}}d\mathbf x_2\right]\chi(1), \qquad \hat K_j(1)\chi(1) = \left[\int\frac{\chi_j^*(2)\chi(2)}{r_{12}}d\mathbf x_2\right]\chi_j(1) . \qquad \text{(17.6)}
$$

$\hat J_j$ adalah operator lokal biasa: perkalian dengan potensial listrik yang ditimbulkan awan elektron $j$. $\hat K_j$ **nonlokal**: nilai $\hat K_j\chi$ di titik 1 bergantung pada nilai $\chi$ di seluruh ruang, karena $\chi$ "dipertukarkan" dengan $\chi_j$. Persamaan (17.5) tampak seperti persamaan nilai eigen satu elektron, tetapi operator Fock bergantung pada orbital-orbital yang dicari, sehingga harus diselesaikan secara iteratif sampai **swakonsisten**: orbital yang dihasilkan sama dengan orbital yang dipakai membangun $\hat f$. Inilah asal nama **medan swakonsisten** (*self-consistent field*, SCF), yang sudah kita jumpai untuk atom di subbab 9.8.

::: {.dalam}
**Menurunkan persamaan Hartree–Fock**

Bentuk Lagrangian $\mathcal L = E_0[\{\chi\}] - \sum_{ij}\lambda_{ji}\left(\langle\chi_i|\chi_j\rangle - \delta_{ij}\right)$, dengan pengali Lagrange $\lambda_{ji}$ yang menjaga ortonormalitas. Ubah setiap orbital sedikit, $\chi_k \to \chi_k + \delta\chi_k$. Dari (17.3), perubahan orde pertama adalah

$$
\delta E_0 = \sum_k\langle\delta\chi_k|\hat h|\chi_k\rangle + \sum_k\sum_j\left(\langle\delta\chi_k|\hat J_j|\chi_k\rangle - \langle\delta\chi_k|\hat K_j|\chi_k\rangle\right) + \text{k.k.}
$$

Faktor $\tfrac12$ dalam (17.3) hilang karena setiap pasangan $(i, j)$ muncul dua kali dalam jumlah ganda, sekali dengan $\delta\chi$ pada indeks pertama dan sekali pada indeks kedua, dan $J_{ij} = J_{ji}$, $K_{ij} = K_{ji}$. Perubahan syarat ortonormalitas adalah $\sum_{kj}\lambda_{jk}\langle\delta\chi_k|\chi_j\rangle + \text{k.k.}$ Syarat $\delta\mathcal L = 0$ untuk $\delta\chi_k$ sembarang menuntut

$$
\left[\hat h + \sum_j(\hat J_j - \hat K_j)\right]\chi_k = \sum_j\lambda_{jk}\chi_j , \quad\text{yaitu}\quad \hat f\chi_k = \sum_j\lambda_{jk}\chi_j .
$$

Matriks $\boldsymbol\lambda$ Hermitian. Operator $\hat f$ tidak berubah bila orbital-orbital yang terisi dicampur dengan transformasi uniter $\chi_i' = \sum_jU_{ji}\chi_j$, karena determinan hanya berubah dengan faktor fase $\det\mathbf U$ (subbab 17.8). Kita dapat memilih $\mathbf U$ yang mendiagonalkan $\boldsymbol\lambda$; dalam basis itu $\lambda_{jk} = \varepsilon_k\delta_{jk}$, dan diperoleh bentuk kanonik (17.5). Orbital-orbital yang mendiagonalkan $\boldsymbol\lambda$ disebut **orbital kanonik**.
:::

### Energi orbital dan energi total

Kalikan (17.5) dari kiri dengan $\chi_i^*$ dan integrasikan:

$$
\varepsilon_i = h_{ii} + \sum_{j=1}^N\left(J_{ij} - K_{ij}\right) . \qquad \text{(17.7)}
$$

Energi orbital $\varepsilon_i$ adalah energi kinetik dan tarikan inti elektron di $\chi_i$ ditambah tolakan bersihnya dengan **semua** elektron lain. Jumlahkan atas orbital terisi dan bandingkan dengan (17.3):

$$
E_0 = \sum_{i=1}^N\varepsilon_i - \frac12\sum_{i,j}\left(J_{ij} - K_{ij}\right) = \frac12\sum_{i=1}^N\left(\varepsilon_i + h_{ii}\right) . \qquad \text{(17.8)}
$$

Energi total **bukan** jumlah energi orbital: menjumlahkan $\varepsilon_i$ menghitung setiap tolakan antarelektron dua kali, sekali untuk $i$ dan sekali untuk $j$. Kesalahan ini, mengira energi molekul sama dengan jumlah energi orbitalnya, sangat lazim dan perlu diwaspadai; ia benar hanya dalam teori Hückel, yang tidak memperlakukan tolakan elektron secara eksplisit (subbab 13.4).

### RHF, UHF, dan ROHF

Untuk molekul kulit tertutup, pasangan elektron α dan β memakai orbital ruang yang sama: **Hartree–Fock terbatas** (*restricted*, RHF). Untuk molekul kulit terbuka (radikal, triplet) ada dua pilihan. **Hartree–Fock tak terbatas** (UHF) memberi elektron α dan β orbital ruang yang berbeda, sehingga ada dua operator Fock, $\hat f^\alpha$ dan $\hat f^\beta$, yang saling terkopel melalui suku Coulomb. Kebebasan tambahan ini menurunkan energi, tetapi determinan UHF umumnya bukan fungsi eigen $\hat S^2$: ia tercampur dengan keadaan spin yang lebih tinggi (**kontaminasi spin**). Program mencetak $\langle\hat S^2\rangle$; untuk doblet nilai tepatnya $S(S+1) = 0{,}75$, dan nilai yang jauh lebih besar menandakan hasil yang perlu dicurigai. **Hartree–Fock terbatas kulit terbuka** (ROHF) memaksa elektron berpasangan berbagi orbital ruang dan menempatkan elektron tak berpasangan di orbital tunggal; ia bebas kontaminasi tetapi energinya sedikit lebih tinggi daripada UHF.

Perbedaan RHF dan UHF tampak dramatis pada pemutusan ikatan. Determinan RHF untuk H₂, $|\sigma_g\alpha\,\sigma_g\beta|$ dengan $\sigma_g \propto 1s_A + 1s_B$, bila diuraikan memuat bagian kovalen $1s_A1s_B$ dan bagian ionik $1s_A^2 + 1s_B^2$ dengan bobot sama, tidak peduli seberapa jauh kedua atom dipisahkan (subbab 11.10). Pada jarak besar, bagian ionik H⁺H⁻ itu sama sekali tidak fisis, dan energi RHF naik jauh di atas energi dua atom hidrogen. UHF dapat melokalisasi elektron α di satu atom dan elektron β di atom lain, sehingga berdisosiasi dengan benar ke dua atom, tetapi dengan harga kontaminasi spin: pada jarak besar fungsi UHF adalah campuran setara singlet dan triplet ($\langle\hat S^2\rangle \to 1$). Penyelesaian yang benar memerlukan lebih dari satu determinan (subbab 17.10).

![Gambar 17.2 Kurva energi potensial H₂ dengan basis STO-3G: RHF (naik terlalu tinggi pada jarak besar), UHF (berimpit dengan RHF sampai titik ketidakstabilan Coulson–Fischer di sekitar 2,2 bohr, lalu berdisosiasi dengan benar), dan CI penuh. Garis putus-putus: energi dua atom H dalam basis yang sama.](fig/c_h2kurva.png){width=78%}

::: {.contoh}
**Contoh 17.4 · Energi H₂ dari integral orbital molekul**

Untuk H₂ dengan basis STO-3G pada $R = 1{,}4$ bohr, program memberi integral orbital molekul $h_{11} = -1{,}2528\ E_h$ dan $J_{11} = 0{,}6746\ E_h$ untuk orbital $\sigma_g$. Hitung energi orbital, energi elektronik, dan energi total. Periksa (17.8).

**Penyelesaian.** Dari (17.7) untuk kulit tertutup dengan satu orbital terisi: $\varepsilon_1 = h_{11} + 2J_{11} - K_{11} = h_{11} + J_{11} = -0{,}5782\ E_h$ (karena $K_{11} = J_{11}$). Dari (17.4): $E_\text{el} = 2h_{11} + J_{11} = -1{,}8310\ E_h$. Tambahkan $V_{NN} = 1/1{,}4 = 0{,}7143$: $E = -1{,}1167\ E_h$. Pemeriksaan: $\tfrac12\sum_i(\varepsilon_i + h_{ii}) = \varepsilon_1 + h_{11} = -1{,}8310\ E_h$.

**Memahami hasil.** Jumlah energi orbital, $2\varepsilon_1 = -1{,}1564\ E_h$, berbeda $0{,}67\ E_h$ dari energi elektronik: tepat sebesar $J_{11}$ yang terhitung dua kali. Energi total HF $-1{,}1167\ E_h$ adalah $0{,}0206\ E_h$ di atas hasil CI penuh dalam basis yang sama (subbab 17.10); selisih ini adalah energi korelasi.
:::

::: {.contoh}
**Contoh 17.5 · Helium dan batas Hartree–Fock**

Energi He: STO-3G $-2{,}8078\ E_h$; batas Hartree–Fock (basis tak berhingga) $-2{,}8617\ E_h$; energi tepat nonrelativistik $-2{,}9037\ E_h$. Hitung galat basis STO-3G, energi korelasi, dan nyatakan keduanya dalam kJ/mol.

**Penyelesaian.** Galat basis: $-2{,}8078 - (-2{,}8617) = 0{,}0539\ E_h = 142$ kJ/mol. Energi korelasi: $-2{,}9037 - (-2{,}8617) = -0{,}0420\ E_h = -110$ kJ/mol.

**Memahami hasil.** Dalam basis minimal, galat basis lebih besar daripada seluruh energi korelasi. Energi korelasi sepasang elektron dalam satu orbital sekitar 0,04 $E_h$, sekitar 1% energi total tetapi sebanding dengan energi ikatan kimia (H₂: 0,17 $E_h$). Untuk molekul dengan puluhan pasangan elektron, energi korelasi mencapai beberapa hartree, dan perubahannya selama reaksi mudah mencapai puluhan kJ/mol.
:::

::: {.contoh}
**Contoh 17.6 · RHF dan UHF pada ikatan yang meregang**

Dengan basis STO-3G pada $R = 4{,}0$ bohr, H₂ memberi: RHF $-0{,}7611\ E_h$; UHF $-0{,}9358\ E_h$ dengan $\langle\hat S^2\rangle = 0{,}964$; CI penuh $-0{,}9438\ E_h$. Energi dua atom H terpisah dalam basis yang sama $-0{,}9332\ E_h$. Tafsirkan.

**Penyelesaian.** RHF berada $0{,}172\ E_h$ (452 kJ/mol) di atas energi dua atom terpisah dan $0{,}356\ E_h$ di atas minimumnya sendiri ($-1{,}1175\ E_h$): menurut RHF, meregangkan ikatan sampai 2,1 Å menghabiskan hampir dua kali energi yang diperlukan untuk memutusnya menjadi dua atom. UHF hanya $0{,}008\ E_h$ di atas CI penuh dan sudah di bawah energi dua atom. Tetapi $\langle\hat S^2\rangle = 0{,}96$ jauh dari nol: fungsinya hampir separuh triplet.

**Memahami hasil.** Pada geometri setimbang, RHF dan UHF berimpit; perbedaan muncul setelah suatu titik kritis (ketidakstabilan Coulson–Fischer, di sekitar 2,2 bohr untuk basis ini). Pelajaran praktisnya: untuk pemutusan ikatan dan diradikal, satu determinan tidak cukup. UHF memberi energi yang masuk akal tetapi fungsi gelombang yang salah spin; metode multikonfigurasi (subbab 17.10) memberi keduanya dengan benar.
:::

::: {.contoh}
**Contoh 17.7 · Kontaminasi spin pada radikal**

Program pendamping memberi $\langle\hat S^2\rangle$ UHF untuk radikal metil datar (C–H 1,079 Å): 0,765 (STO-3G) dan 0,762 (6-31G*); untuk radikal alil (C–C 1,388 Å, $\angle$CCC = 124°, STO-3G): 1,074. Nilai tepat untuk doblet adalah 0,750. Bila fungsi UHF dianggap campuran doblet dan kuartet ($\langle\hat S^2\rangle = 3{,}75$) saja, berapa bobot kuartet pada masing-masing?

**Penyelesaian.** Dengan bobot kuartet $w$: $0{,}75(1 - w) + 3{,}75w = \langle\hat S^2\rangle$, sehingga $w = (\langle\hat S^2\rangle - 0{,}75)/3$. Metil: $w = 0{,}005$ (STO-3G) dan 0,004 (6-31G*). Alil: $w = 0{,}108$.

**Memahami hasil.** Radikal metil, dengan elektron tak berpasangan terlokalisasi pada satu orbital p karbon, hampir bebas kontaminasi, dan UHF dapat dipercaya. Pada radikal alil yang terkonjugasi, elektron tak berpasangan tersebar pada dua karbon ujung dan pasangan elektron π terpolarisasi kuat oleh spinnya; UHF memanfaatkan kebebasannya dengan mencampurkan keadaan kuartet sekitar 11%. Kontaminasi sebesar ini merusak energi, kerapatan spin, dan terutama hasil MP2 berbasis UHF. Untuk radikal terkonjugasi, ROHF, DFT (yang kontaminasinya biasanya jauh lebih kecil), atau metode multikonfigurasi lebih aman.
:::

::: {.kuis}
**Kuis cepat 17.2**

Mengapa $J_{ii} = K_{ii}$, dan apa akibatnya bagi interaksi elektron dengan dirinya sendiri? Bila energi orbital terisi H₂O dijumlahkan dan dikalikan dua, apakah hasilnya energi elektronik molekul?
:::
