## 17.5 Fungsi basis: STO, GTO, split-valence, polarisasi, difus

### Orbital Slater dan orbital Gauss

Pilihan fungsi basis menentukan ketelitian dan biaya perhitungan sekaligus. Pilihan yang paling alami adalah fungsi yang bentuknya meniru orbital atom hidrogen, yaitu **orbital jenis Slater** (STO):

$$
\phi^\text{STO}_{n\ell m}(r, \theta, \varphi) = N\,r^{n-1}e^{-\zeta r}\,Y_\ell^m(\theta, \varphi) , \qquad \text{(17.19)}
$$

dengan eksponen $\zeta$ yang menyatakan "muatan inti efektif" dibagi $n$ (aturan Slater, subbab 9.9). STO mempunyai dua sifat yang benar secara fisis: **taring** (*cusp*) di inti, yaitu turunan yang tidak malar di $r = 0$ sebagaimana dituntut oleh potensial $-Z/r$, dan peluruhan eksponensial $e^{-\zeta r}$ pada jarak jauh. Sayangnya, integral dua elektron yang melibatkan STO pada tiga atau empat pusat berbeda tidak mempunyai bentuk tertutup dan sangat lambat dihitung.

Pada tahun 1950 S. F. Boys mengusulkan **orbital jenis Gauss** (GTO), dalam bentuk Kartesius

$$
\phi^\text{GTO}(\mathbf r) = N\,x^ly^mz^ne^{-\alpha r^2} , \qquad \text{(17.20)}
$$

dengan $L = l + m + n$ menentukan jenis fungsi: $L = 0$ fungsi s, $L = 1$ fungsi p ($x$, $y$, $z$), $L = 2$ fungsi d. Ada enam fungsi d Kartesius ($x^2$, $y^2$, $z^2$, $xy$, $xz$, $yz$), satu kombinasi di antaranya, $x^2 + y^2 + z^2$, sebenarnya berbentuk s; sebagian program memakai lima fungsi d "sferis" yang murni (subbab 7.8). Keunggulan GTO adalah teorema hasil kali Gauss (subbab 2.2): semua integral, sampai integral empat pusat, dapat direduksi menjadi integral satu pusat dan fungsi Boys (subbab 17.3). Kelemahannya juga jelas: fungsi Gauss mulus di inti (tidak bertaring) dan meluruh terlalu cepat ($e^{-\alpha r^2}$ alih-alih $e^{-\zeta r}$).

### Kontraksi dan basis STO-nG

Jalan tengahnya adalah memakai kombinasi linear beberapa fungsi Gauss **primitif** dengan koefisien tetap, yang disebut fungsi Gauss **terkontraksi**:

$$
\phi_\mu(\mathbf r) = \sum_{k=1}^{n}d_{k\mu}\,g_k(\alpha_{k\mu}, \mathbf r) . \qquad \text{(17.21)}
$$

Dalam basis **STO-nG** (Hehre, Stewart, dan Pople, 1969), setiap STO dihampiri dengan $n$ fungsi Gauss yang eksponen dan koefisiennya dipilih agar tumpang tindihnya dengan STO sebesar mungkin. Koefisien dan eksponen itu kemudian dibekukan, sehingga setiap fungsi terkontraksi dihitung sebagai satu fungsi basis dalam persamaan Roothaan, meskipun integralnya dibangun dari $n^4$ integral primitif. Gambar 17.4 memperlihatkan bagaimana tiga fungsi Gauss sudah meniru orbital 1s Slater dengan baik, kecuali di dekat inti (taring) dan di ekor yang jauh.

![Gambar 17.4 Pendekatan orbital Slater 1s (ζ = 1, garis hitam) dengan satu, dua, dan tiga fungsi Gauss (STO-1G, STO-2G, STO-3G). Kiri: fungsi radial; sisipan memperbesar daerah dekat inti, tempat fungsi Gauss tidak dapat meniru taring. Kanan: fungsi distribusi radial r²ψ², yang menunjukkan bahwa di daerah yang penting secara energi pendekatannya sudah sangat baik.](fig/c_basis.png){width=94%}

### Basis minimal, split-valence, polarisasi, difus

Basis dikelompokkan menurut banyaknya fungsi untuk tiap orbital atom:

- **Basis minimal** (STO-3G): satu fungsi untuk setiap orbital yang terisi dalam atom bebas. Untuk H dan He satu fungsi (1s); untuk Li–Ne lima fungsi (1s, 2s, 2p$_x$, 2p$_y$, 2p$_z$). Murah, tetapi tidak dapat menyesuaikan ukuran orbital dengan lingkungan molekul.
- **Basis *split-valence*** (3-21G, 6-31G): orbital inti tetap satu fungsi, tetapi setiap orbital valensi diberi dua fungsi (bagian "dalam" yang terkontraksi dan bagian "luar" yang lebih menyebar). Orbital molekul dapat mencampur keduanya dengan perbandingan berbeda, sehingga orbital dapat "mengembang" atau "menyusut". Notasi 6-31G berarti: orbital inti dari enam primitif; valensi dibagi menjadi bagian dalam dari tiga primitif dan bagian luar dari satu primitif. Basis dengan tiga fungsi per orbital valensi (6-311G) disebut *triple-zeta*.
- **Fungsi polarisasi**: fungsi dengan momentum sudut lebih tinggi daripada yang terisi dalam atom, misalnya fungsi d pada C, N, O dan fungsi p pada H. Fungsi ini memungkinkan awan elektron bergeser dan "membengkok" ke arah ikatan, seperti orbital hibrida yang mencampur s dan p (subbab 12.2). Notasi Pople: 6-31G* atau 6-31G(d) menambah fungsi d pada atom berat; 6-31G** atau 6-31G(d,p) juga menambah fungsi p pada H. Polarisasi sangat penting untuk sudut ikatan, penghalang inversi NH₃, dan molekul dengan atom periode ketiga.
- **Fungsi difus**: fungsi s dan p dengan eksponen kecil yang menyebar jauh (subbab 3.9). Diperlukan untuk anion, keadaan tereksitasi Rydberg, afinitas elektron, ikatan hidrogen, dan interaksi lemah. Notasi: 6-31+G* (difus pada atom berat), 6-31++G* (juga pada H), atau awalan "aug-" pada basis Dunning.

**Basis berkorelasi konsisten** cc-pVXZ (Thom Dunning, 1989), dengan X = D, T, Q, 5, 6 (*double* sampai *sextuple zeta*), dirancang agar setiap peningkatan X menambah fungsi-fungsi yang menyumbang energi korelasi dalam jumlah yang setara. Akibatnya energi korelasi berkonvergensi secara teratur, kira-kira sebagai $X^{-3}$:

$$
E^\text{kor}_X \approx E^\text{kor}_\text{CBS} + AX^{-3} . \qquad \text{(17.22)}
$$

Dengan dua nilai X, kedua tetapan dapat dihilangkan dan diperoleh taksiran **batas basis lengkap** (CBS):

$$
E^\text{kor}_\text{CBS} \approx \frac{X^3E^\text{kor}_X - Y^3E^\text{kor}_Y}{X^3 - Y^3} . \qquad \text{(17.23)}
$$

Energi HF berkonvergensi jauh lebih cepat (kira-kira eksponensial dalam X). Perlunya basis besar untuk korelasi berasal dari **taring antarelektron**: fungsi gelombang tepat mempunyai lekukan tajam ketika dua elektron bertemu ($r_{12} \to 0$), dan perkalian orbital yang mulus sangat lambat meniru lekukan ini. Metode **F12** memasukkan $r_{12}$ secara eksplisit ke dalam fungsi gelombang dan mencapai kualitas CBS dengan basis triple-zeta.

| Basis | H | C, N, O | H₂O | Benzena |
|---|---|---|---|---|
| STO-3G | 1 | 5 | 7 | 36 |
| 6-31G | 2 | 9 | 13 | 66 |
| 6-31G* (6d) | 2 | 15 | 19 | 102 |
| 6-31G** (6d) | 5 | 15 | 25 | 120 |
| cc-pVDZ | 5 | 14 | 24 | 114 |
| aug-cc-pVDZ | 9 | 23 | 41 | 192 |
| cc-pVTZ | 14 | 30 | 58 | 264 |

### Galat superposisi basis

Bila dua molekul mendekat, misalnya dalam dimer berikatan hidrogen, masing-masing dapat "meminjam" fungsi basis tetangganya untuk memperbaiki deskripsi elektronnya sendiri. Penurunan energi semu ini, yang tidak ada bila basisnya lengkap, disebut **galat superposisi basis** (BSSE). Ia membuat interaksi tampak lebih kuat daripada sebenarnya. Koreksi **counterpoise** Boys–Bernardi menghitung energi setiap monomer dalam basis dimer lengkap (fungsi basis pasangan ditempatkan pada posisinya tanpa inti dan elektron, sebagai "atom hantu"):

$$
\Delta E^\text{CP} = E_{AB}(AB) - E_A(AB) - E_B(AB) , \qquad \text{(17.24)}
$$

dengan tanda kurung menyatakan basis yang dipakai. BSSE sangat besar untuk basis kecil dan mengecil bila basis membesar.

Untuk atom berat (dari periode keempat ke bawah), elektron inti sering diganti dengan **potensial inti efektif** (ECP, pseudopotensial) yang meniru pengaruh elektron inti pada elektron valensi. ECP menghemat fungsi basis dan sekaligus dapat memasukkan efek relativistik elektron inti (subbab 17.15).

::: {.contoh}
**Contoh 17.16 · Berapa Gauss untuk satu Slater?**

Untuk atom hidrogen dengan orbital Slater $\zeta = 1$ (energi tepat $-0{,}5\ E_h$), energi dengan pendekatan STO-nG adalah: STO-1G $-0{,}4242$; STO-2G $-0{,}4812$; STO-3G $-0{,}4949$; STO-6G $-0{,}4998\ E_h$. Tumpang tindih dengan orbital Slater berturut-turut 0,9784; 0,9984; 0,99983; 0,9999994, dan rapat elektron di inti $|\psi(0)|^2$ berturut-turut 0,072; 0,152; 0,207; 0,281, dibandingkan nilai tepat $1/\pi = 0{,}318$. Apa polanya?

**Penyelesaian.** Galat energi: 0,0758; 0,0188; 0,0051; 0,0002 $E_h$, berkurang kira-kira empat kali untuk setiap Gauss tambahan pada awalnya. Tumpang tindih sudah 99,98% dengan tiga Gauss, tetapi rapat di inti masih 35% terlalu rendah, dan dengan enam Gauss pun masih 12% terlalu rendah.

**Memahami hasil.** Energi dan tumpang tindih ditentukan oleh daerah tempat elektron sering berada, yang mudah ditiru. Rapat di inti ditentukan oleh taring, yang tidak dapat ditiru oleh jumlah berhingga fungsi Gauss. Itulah sebabnya sifat yang bergantung pada $|\psi(0)|^2$, seperti kopling hiperhalus ESR dan kopling $J$ NMR (subbab 16.5 dan 16.11), memerlukan basis khusus dengan fungsi s yang sangat curam.
:::

::: {.contoh}
**Contoh 17.17 · Menghitung fungsi basis**

Hitung banyaknya fungsi basis untuk metanol CH₃OH dengan STO-3G, 6-31G*, dan cc-pVDZ.

**Penyelesaian.** Dari tabel: STO-3G: $2 \times 5 + 4 \times 1 = 14$. 6-31G* (6d): $2 \times 15 + 4 \times 2 = 38$. cc-pVDZ: $2 \times 14 + 4 \times 5 = 48$.

**Memahami hasil.** Dari STO-3G ke cc-pVDZ, banyaknya fungsi naik 3,4 kali; menurut hukum $N^4$, biaya HF naik sekitar 140 kali, dan biaya CCSD(T) ($N^7$) lebih dari 5000 kali. Menghitung banyaknya fungsi basis sebelum memulai perhitungan adalah kebiasaan yang baik untuk menaksir apakah perhitungan akan selesai dalam waktu wajar.
:::

::: {.contoh}
**Contoh 17.18 · Konvergensi energi HF terhadap basis**

Energi HF H₂O pada geometri percobaan: STO-3G $-74{,}9629$; 6-31G $-75{,}9840$; 6-31G* $-76{,}0105$; 6-31G** $-76{,}0232\ E_h$; batas HF (dari perhitungan dengan basis sangat besar) sekitar $-76{,}0675\ E_h$. Hitung galat basis setiap himpunan dalam kJ/mol.

**Penyelesaian.** Galat terhadap batas HF: STO-3G $1{,}1046\ E_h = 2900$ kJ/mol; 6-31G $0{,}0835\ E_h = 219$ kJ/mol; 6-31G* $0{,}0570\ E_h = 150$ kJ/mol; 6-31G** $0{,}0443\ E_h = 116$ kJ/mol.

**Memahami hasil.** Lompatan terbesar adalah dari basis minimal ke split-valence: STO-3G kehilangan lebih dari satu hartree, terutama karena orbital 1s dan 2s oksigen tidak dapat menyesuaikan diri. Galat 100 kJ/mol yang masih tersisa pada 6-31G** tampak besar, tetapi sebagian besar berasal dari elektron inti dan hampir sama untuk molekul-molekul yang mengandung atom yang sama, sehingga meniadakan diri dalam energi reaksi.
:::

::: {.contoh}
**Contoh 17.19 · Ekstrapolasi ke basis lengkap**

Energi korelasi MP2 (elektron valensi) H₂O dengan basis Dunning kira-kira: cc-pVTZ $-0{,}2613$ dan cc-pVQZ $-0{,}2811\ E_h$. Taksir batas CBS dengan (17.23). Berapa galat cc-pVQZ terhadap taksiran itu?

**Penyelesaian.** Dengan $X = 4$, $Y = 3$:

$$
E_\text{CBS} \approx \frac{64(-0{,}2811) - 27(-0{,}2613)}{64 - 27} = \frac{-17{,}990 + 7{,}055}{37} = -0{,}2956\ E_h .
$$

Galat cc-pVQZ: $0{,}0145\ E_h = 38$ kJ/mol.

**Memahami hasil.** Bahkan basis quadruple-zeta dengan 115 fungsi untuk H₂O kehilangan hampir 40 kJ/mol energi korelasi. Untuk energi reaksi, galat ini sebagian meniadakan diri, tetapi untuk ketelitian di bawah 4 kJ/mol ekstrapolasi CBS atau metode F12 hampir selalu diperlukan. Metode komposit (subbab 17.12) memanfaatkan pola $X^{-3}$ ini secara sistematis.
:::

::: {.contoh}
**Contoh 17.20 · Galat superposisi basis pada dimer air**

Untuk dimer air dengan jarak O···O 2,98 Å, program pendamping memberi energi interaksi HF tanpa koreksi dan dengan koreksi counterpoise: STO-3G $-5{,}13$ dan $-1{,}73$ kkal/mol; 6-31G $-7{,}35$ dan $-6{,}36$ kkal/mol. Hitung BSSE dan komentari.

**Penyelesaian.** BSSE = selisih keduanya: STO-3G 3,40 kkal/mol (66% dari interaksi tanpa koreksi); 6-31G 0,99 kkal/mol (13%).

**Memahami hasil.** Dengan basis minimal, dua pertiga "ikatan hidrogen" adalah artefak peminjaman basis. Dengan basis yang lebih besar, BSSE mengecil, tetapi interaksi HF/6-31G (sekitar −6,4 kkal/mol) masih lebih kuat daripada nilai terbaik untuk dimer air (sekitar −5,0 kkal/mol), karena basis 6-31G tanpa polarisasi melebih-lebihkan momen dipol air (Contoh 17.27). Untuk interaksi lemah, basis dengan fungsi difus dan polarisasi serta koreksi counterpoise adalah standar minimum.
:::

::: {.contoh}
**Contoh 17.21 · Potensial inti efektif untuk emas**

Basis keluarga def2 memakai potensial inti efektif (ECP) yang menggantikan 60 elektron inti emas ($Z = 79$). Berapa elektron emas yang diperlakukan secara eksplisit? Kulit mana yang termasuk? Untuk kompleks [AuCl₂]⁻, berapa elektron yang masuk perhitungan dengan ECP ini (Cl dengan semua elektron)?

**Penyelesaian.** $79 - 60 = 19$ elektron: kulit 5s²5p⁶5d¹⁰6s¹. Dalam [AuCl₂]⁻: $19 + 2 \times 17 + 1 = 54$ elektron, dibandingkan $79 + 34 + 1 = 114$ tanpa ECP.

**Memahami hasil.** Banyaknya elektron dan fungsi basis turun lebih dari separuh, dan fungsi basis yang sangat curam untuk kulit dalam tidak diperlukan lagi. Lebih penting, ECP untuk emas dicocokkan dengan perhitungan atom relativistik, sehingga penyusutan 6s dan pengembangan 5d (subbab 17.15) sudah termasuk tanpa biaya tambahan. Kulit 5s5p "semi-inti" tetap eksplisit karena tumpang tindihnya dengan 5d besar; ECP yang hanya menyisakan 11 elektron (5d¹⁰6s¹) lebih murah tetapi kurang teliti.
:::

::: {.kuis}
**Kuis cepat 17.5**

Apa arti setiap angka dan tanda dalam "6-311++G(2d,p)"? Mengapa fungsi Gauss tidak dapat meniru taring di inti, berapa pun banyaknya?
:::

## 17.6 SCF untuk H₂O

### Menyiapkan perhitungan

Sekarang kita ikuti satu perhitungan nyata dari awal sampai akhir: H₂O pada geometri percobaan ($r_\text{OH} = 0{,}9572$ Å, $\angle\text{HOH} = 104{,}52°$) dengan basis STO-3G, memakai program pendamping. Molekul diletakkan di bidang $yz$ dengan sumbu $C_2$ sepanjang $z$ dan oksigen di titik asal; kedua hidrogen berada di $(0, \pm1{,}4304, 1{,}1072)$ bohr. Ada 10 elektron, sehingga 5 orbital terisi, dan 7 fungsi basis: O 1s, O 2s, O 2p$_x$, O 2p$_y$, O 2p$_z$, H$_a$ 1s, H$_b$ 1s. Tolakan antarinti $V_{NN} = 9{,}1950\ E_h$.

Grup titik molekul adalah $C_{2v}$ (subbab 10.2). Fungsi basis dapat dikelompokkan menurut simetri: O 1s, O 2s, O 2p$_z$, dan kombinasi $\text{H}_a + \text{H}_b$ bersimetri $a_1$; O 2p$_y$ dan $\text{H}_a - \text{H}_b$ bersimetri $b_2$ (dalam bidang); O 2p$_x$, yang tegak lurus bidang molekul, bersimetri $b_1$. Karena orbital molekul harus berupa representasi tak tereduksi, matriks Fock terpecah menjadi blok $4 \times 4$ ($a_1$), $2 \times 2$ ($b_2$), dan $1 \times 1$ ($b_1$). Program memanfaatkan simetri semacam ini untuk menghemat waktu; tanpa memakainya pun, simetri muncul dengan sendirinya dalam hasil.

### Matriks tumpang tindih dan Hcore

Matriks tumpang tindih (hanya unsur yang tidak nol di luar diagonal):

| Pasangan | $S_{\mu\nu}$ | Pasangan | $S_{\mu\nu}$ |
|---|---|---|---|
| O 1s, O 2s | 0,2367 | O 2p$_y$, H$_a$ | +0,3111 |
| O 1s, H | 0,0540 | O 2p$_z$, H | 0,2408 |
| O 2s, H | 0,4748 | H$_a$, H$_b$ | 0,2517 |

Fungsi O 2p$_x$ tidak bertumpang tindih dengan fungsi lain mana pun: bidang molekul adalah bidang simpulnya. Unsur diagonal $\mathbf H^\text{inti}$ (energi kinetik ditambah tarikan ketiga inti untuk satu elektron di fungsi itu) adalah $-32{,}72$ untuk O 1s, $-9{,}33$ untuk O 2s, sekitar $-7{,}5$ untuk O 2p, dan $-5{,}08\ E_h$ untuk H 1s.

### Hasil SCF

Setelah delapan siklus dengan DIIS, energi total $-74{,}962928\ E_h$. Koefisien orbital molekul (kolom) dan energinya:

| Fungsi basis | $1a_1$ | $2a_1$ | $1b_2$ | $3a_1$ | $1b_1$ | $4a_1$ | $2b_2$ |
|---|---|---|---|---|---|---|---|
| O 1s | $-0{,}994$ | $-0{,}233$ | 0 | $-0{,}103$ | 0 | 0,132 | 0 |
| O 2s | $-0{,}027$ | 0,834 | 0 | 0,537 | 0 | $-0{,}885$ | 0 |
| O 2p$_x$ | 0 | 0 | 0 | 0 | 1,000 | 0 | 0 |
| O 2p$_y$ | 0 | 0 | $-0{,}606$ | 0 | 0 | 0 | 0,991 |
| O 2p$_z$ | $-0{,}004$ | 0,130 | 0 | $-0{,}777$ | 0 | $-0{,}742$ | 0 |
| H$_a$ 1s | 0,006 | 0,159 | $-0{,}445$ | $-0{,}278$ | 0 | 0,797 | $-0{,}839$ |
| H$_b$ 1s | 0,006 | 0,159 | 0,445 | $-0{,}278$ | 0 | 0,797 | 0,839 |
| $\varepsilon$ ($E_h$) | $-20{,}242$ | $-1{,}268$ | $-0{,}618$ | $-0{,}453$ | $-0{,}391$ | 0,606 | 0,742 |

Tafsiran setiap orbital sejalan dengan gambaran kualitatif dari simetri (subbab 13.2):

- $1a_1$: praktis orbital O 1s murni, jauh di bawah yang lain; orbital inti ini tidak ikut berikatan.
- $2a_1$: terutama O 2s yang bercampur sefase dengan kedua H 1s: orbital ikatan yang paling dalam.
- $1b_2$: O 2p$_y$ dengan kombinasi $\text{H}_a - \text{H}_b$: orbital ikatan O–H dalam bidang molekul.
- $3a_1$: campuran O 2s, O 2p$_z$, dan H 1s; sebagian besar mengarah menjauhi hidrogen, sehingga bersifat sebagian ikatan dan sebagian pasangan bebas.
- $1b_1$ (HOMO): O 2p$_x$ murni, tegak lurus bidang molekul: pasangan elektron bebas sejati, tanpa sumbangan hidrogen dalam basis ini.
- $4a_1$ dan $2b_2$ (virtual): orbital antiikatan O–H. LUMO $4a_1$ terletak 27,1 eV di atas HOMO.

![Gambar 17.5 Kontur orbital molekul kanonik H₂O (HF/STO-3G, geometri percobaan). Orbital 2a₁, 1b₂, 3a₁, dan 4a₁ digambar di bidang molekul (yz); orbital 1b₁ digambar di bidang xz yang tegak lurus bidang molekul. Kontur biru dan jingga menandai fase berlawanan; titik hitam menandai inti.](fig/c_orbital.png){width=96%}

### Keluaran program yang khas

Hampir semua program kimia kuantum mencetak blok-blok serupa. Berikut contoh keluaran program pendamping (diringkas):

```
Molekul: H2O     Muatan: 0   Multiplisitas: 1   Basis: STO-3G (7 fungsi)
Energi tolakan inti              9.194964854 Eh
 Siklus        E total (Eh)        Delta E       max|FPS-SPF|
    1        -73.232478897     -7.32e+01        2.6e-01
    2        -74.945897757     -1.71e+00        3.6e-02
    3        -74.962079924     -1.62e-02        7.7e-03
    4        -74.962870766     -7.91e-04        1.4e-03
    5        -74.962923297     -5.25e-05        5.0e-04
    6        -74.962928230     -4.93e-06        3.5e-05
    7        -74.962928246     -1.69e-08        2.5e-07
    8        -74.962928246     -7.25e-13        1.0e-09
SCF KONVERGEN dalam 8 siklus
Energi elektronik   -84.157893100  Eh
Energi total        -74.962928246  Eh
 Komponen: kinetik 74.588911  tarikan e-inti -196.960054
           tolakan e-e 38.213250  tolakan inti 9.194965   -V/T 2.0050
Energi orbital (Eh):
   1 a1 -20.2417   2 a1 -1.2684   3 b2 -0.6179   4 a1 -0.4530   5 b1 -0.3912
   6 a1   0.6057   7 b2  0.7424
Momen dipol (debye):  X 0.000  Y 0.000  Z 1.726   Total 1.726
Muatan Mulliken:  O -0.366   H 0.183   H 0.183
```

Membaca keluaran seperti ini dengan kritis adalah keterampilan pokok (subbab 17.18): periksa bahwa SCF benar-benar konvergen, bahwa simetri dan banyaknya elektron benar, bahwa energi orbital terisi semuanya negatif, dan bahwa rasio virial dekat 2.

::: {.contoh}
**Contoh 17.22 · Membaca matriks tumpang tindih**

Mengapa $S(\text{O 1s}, \text{H}) = 0{,}054$ jauh lebih kecil daripada $S(\text{O 2s}, \text{H}) = 0{,}475$? Mengapa $S(\text{O 2p}_y, \text{H}_a)$ dan $S(\text{O 2p}_y, \text{H}_b)$ berlawanan tanda?

**Penyelesaian.** Orbital O 1s sangat kompak (eksponen efektif besar, jari-jari sekitar $1/7{,}7$ bohr), sedangkan hidrogen berjarak 1,81 bohr; kedua fungsi hampir tidak bertemu di ruang. Orbital O 2s jauh lebih menyebar dan meluas sampai ke hidrogen. Fungsi 2p$_y$ positif di $y > 0$ dan negatif di $y < 0$; H$_a$ terletak di $y > 0$ dan H$_b$ di $y < 0$, sehingga tumpang tindihnya berlawanan tanda dengan besar sama.

**Memahami hasil.** Tumpang tindih kecil berarti O 1s tidak berpartisipasi dalam ikatan: orbital $1a_1$ adalah 99% O 1s. Pola tanda $S(\text{2p}_y, \text{H})$ adalah pola simetri $b_2$; hanya kombinasi $\text{H}_a - \text{H}_b$ yang dapat bergabung dengan 2p$_y$.
:::

::: {.contoh}
**Contoh 17.23 · Memberi label simetri dari koefisien**

Dengan tabel karakter $C_{2v}$ (operasi $E$, $C_2$, $\sigma_v(xz)$, $\sigma_v'(yz)$), tentukan label simetri orbital ketiga (energi $-0{,}618$) dan kelima ($-0{,}391$) dari koefisiennya.

**Penyelesaian.** Orbital ketiga: $-0{,}606\,\text{2p}_y - 0{,}445\,\text{H}_a + 0{,}445\,\text{H}_b$. Rotasi $C_2$ (terhadap $z$) membawa $y \to -y$ dan menukar H$_a$ dengan H$_b$: orbital berubah tanda, karakter $-1$. Pencerminan $\sigma_v(xz)$ juga membawa $y \to -y$ dan menukar kedua H: karakter $-1$. Pencerminan $\sigma_v'(yz)$ membiarkan semuanya: $+1$. Pola $(1, -1, -1, 1)$ adalah $b_2$. Orbital kelima, 2p$_x$ murni: $C_2$ membalik tanda ($-1$), $\sigma_v(xz)$ membiarkan ($+1$), $\sigma_v'(yz)$ membalik ($-1$): pola $(1, -1, 1, -1)$, yaitu $b_1$.

**Memahami hasil.** Label simetri tidak bergantung pada basis atau metode: orbital $1b_1$ air tetap $1b_1$ dalam perhitungan apa pun. Label ini dipakai untuk membandingkan hasil perhitungan dengan pita spektrum fotoelektron (Contoh 17.12) dan untuk aturan seleksi transisi elektronik (subbab 10.10). Perhatikan bahwa label $b_1$ dan $b_2$ tertukar bila molekul diletakkan di bidang $xz$; selalu periksa konvensi orientasi program.
:::

::: {.contoh}
**Contoh 17.24 · Teorema virial sebagai pemeriksaan**

Untuk fungsi gelombang yang dioptimasi penuh terhadap semua parameter skala, teorema virial menuntut $\langle V\rangle = -2\langle T\rangle$, yaitu $-V/T = 2$ (subbab 7.9), dan untuk molekul hanya pada geometri setimbang. Program memberi, untuk H₂O/STO-3G pada geometri percobaan, $T = 74{,}5889$, $V_{ne} = -196{,}9601$, $V_{ee} = 38{,}2133$, $V_{NN} = 9{,}1950\ E_h$. Hitung $-V/T$ dan energi total.

**Penyelesaian.** $V = -196{,}9601 + 38{,}2133 + 9{,}1950 = -149{,}5518\ E_h$; $-V/T = 149{,}5518/74{,}5889 = 2{,}0050$. Energi total $T + V = -74{,}9629\ E_h$.

**Memahami hasil.** Penyimpangan 0,25% berasal dari dua sumber: eksponen basis STO-3G tidak dioptimasi untuk molekul ini, dan geometri percobaan bukan minimum STO-3G. Dengan 6-31G*, $-V/T = 2{,}0025$. Rasio virial yang jauh dari 2 adalah tanda bahaya: basis yang buruk, atau geometri yang jauh dari setimbang.
:::

::: {.contoh}
**Contoh 17.25 · Celah HOMO–LUMO bukan energi eksitasi**

Selisih energi LUMO dan HOMO H₂O/STO-3G adalah $0{,}6057 - (-0{,}3912) = 0{,}9969\ E_h = 27{,}1$ eV. Pita serapan pertama air dalam fase gas berada di sekitar 7,4 eV (167 nm). Mengapa jauh berbeda?

**Penyelesaian.** Energi orbital virtual dihitung dalam medan $N$ elektron yang lain, sehingga ia menggambarkan elektron **tambahan** (pembentukan anion), bukan elektron yang dipindahkan dari HOMO. Dalam eksitasi, elektron tereksitasi masih tertarik oleh lubang yang ditinggalkannya; tarikan ini, ditambah pertukaran, menurunkan energi eksitasi jauh di bawah selisih energi orbital. Selain itu, orbital virtual dengan basis minimal sangat tidak teliti, dan keadaan tereksitasi pertama air berkarakter Rydberg (3s), yang tidak dapat digambarkan sama sekali tanpa fungsi difus.

**Memahami hasil.** Untuk energi eksitasi diperlukan metode khusus: CIS, TD-DFT, EOM-CCSD, atau CASPT2. Dalam DFT, celah HOMO–LUMO Kohn–Sham justru sering terlalu kecil (subbab 17.14). Celah HOMO–LUMO tetap berguna sebagai ukuran kualitatif kestabilan dan kekerasan kimia, tetapi tidak boleh dibaca sebagai energi foton.
:::

::: {.kuis}
**Kuis cepat 17.6**

Ada berapa orbital molekul bersimetri $a_1$ dalam perhitungan H₂O/STO-3G, dan mengapa? Bila basis diganti 6-31G*, apakah orbital $1b_1$ tetap merupakan orbital 2p$_x$ oksigen murni?
:::
