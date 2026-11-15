# Bab 13 Orbital Molekul Poliatom dan Sistem π

Benzena, C₆H₆, adalah salah satu zat paling stabil dalam kimia organik: ia tidak mudah mengadisi brom, dapat dipanaskan sampai ratusan derajat tanpa terurai, dan cincinnya bertahan dalam reaksi-reaksi substitusi yang keras. Siklobutadiena, C₄H₄, yang tampak seperti "benzena yang lebih kecil", baru dapat diamati pada tahun 1970-an dalam matriks gas mulia pada suhu sekitar 10 K; pada suhu kamar ia bereaksi dengan dirinya sendiri dalam sekejap. Siklooktatetraena, C₈H₈, tidak datar sama sekali melainkan berbentuk bak, dan bereaksi seperti alkena biasa. Mengapa enam elektron π membuat molekul sangat stabil, empat elektron membuatnya sangat tidak stabil, dan delapan elektron membuatnya "biasa saja"? Mengapa butadiena tak berwarna, β-karotena jingga, dan rantai poliasetilena yang sangat panjang dapat menghantarkan listrik? Mengapa heksatriena menutup cincin dengan stereokimia yang berbeda bila dipanaskan daripada bila disinari?

Jawaban atas semua pertanyaan ini datang dari teori **orbital molekul** (OM) untuk molekul poliatom, khususnya untuk elektron π yang terdelokalisasi di atas kerangka molekul. Di Bab 11 kita membangun OM untuk molekul diatom; di Bab 12 kita melihat bahwa orbital lokal (hibrida, ikatan, pasangan bebas) melukiskan keadaan dasar dengan sama baiknya. Bab ini memakai sudut pandang yang lain: orbital-orbital yang meliputi seluruh molekul, yang energinya dapat diukur dengan spektroskopi fotoelektron dan spektroskopi UV, dan yang bentuknya menentukan reaktivitas. Kita mulai dari OM molekul kecil yang disusun dengan simetri, lalu diagram Walsh yang menjelaskan bentuk molekul. Bagian terbesar bab ini adalah **metode Hückel**, model paling sederhana dan paling berhasil untuk sistem π: dari etilena sampai benzena, aturan aromatisitas $4n + 2$, heteroatom, orbital perbatasan, dan aturan Woodward–Hoffmann. Metode Pariser–Parr–Pople menambahkan tolakan elektron. Akhirnya kita membiarkan rantai Hückel tumbuh sampai tak hingga, dan sampai pada pita energi padatan: logam, semikonduktor, dan grafena.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa orbital molekul kanonik tersebar ke seluruh molekul, padahal ikatan kimia tampak lokal?
2. Mengapa BeH₂ linear tetapi H₂O bengkok, dan mengapa metilena triplet lebih "lurus" daripada metilena singlet?
3. Bagaimana sebuah model dengan dua parameter, $\alpha$ dan $\beta$, dapat meramalkan kestabilan, warna, dan kereaktifan hidrokarbon π?
4. Mengapa sistem siklik dengan $4n + 2$ elektron π stabil dan dengan $4n$ elektron π tidak stabil?
5. Mengapa piridina bersifat basa sedangkan pirola hampir tidak, padahal keduanya mempunyai atom N dalam cincin aromatik?
6. Mengapa reaksi Diels–Alder berjalan dengan pemanasan, sedangkan adisi dua alkena menjadi siklobutana memerlukan cahaya?
7. Bagaimana tingkat-tingkat energi diskret molekul berubah menjadi pita energi padatan, dan mengapa grafena menghantarkan listrik dengan cara yang luar biasa?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menyusun orbital molekul LCAO molekul poliatom, membedakan orbital kanonik dan orbital terlokalisasi, dan menghubungkan keduanya.
2. Membangun diagram OM H₂O, NH₃, dan CH₄ dengan kombinasi linear teradaptasi simetri, dan membandingkannya dengan spektrum fotoelektron.
3. Membaca diagram Walsh dan meramalkan bentuk molekul AH₂, AH₃, dan AB₂ dari banyaknya elektron valensi.
4. Menuliskan dan menyelesaikan persamaan sekuler Hückel, termasuk dengan Python, dan menafsirkan $\alpha$ dan $\beta$.
5. Menghitung tingkat energi, koefisien, energi delokalisasi, muatan, dan orde ikatan untuk etilena, alil, butadiena, dan molekul yang lebih besar.
6. Menurunkan rumus umum tingkat energi poliena linear dan siklik, dan memakai lingkaran Frost.
7. Menjelaskan aromatisitas, antiaromatisitas, dan aturan $4n + 2$, serta peran simetri Möbius.
8. Memasukkan heteroatom ke dalam model Hückel dan meramalkan kebasaan dan momen dipol piridina dan pirola.
9. Memakai orbital perbatasan HOMO dan LUMO untuk meramalkan tempat serangan elektrofil, nukleofil, dan radikal.
10. Menurunkan aturan Woodward–Hoffmann untuk reaksi elektrosiklik, sikloadisi, dan sigmatropik.
11. Menjelaskan metode Pariser–Parr–Pople dan mengapa ia memperbaiki ramalan spektrum UV.
12. Menurunkan pita energi rantai Hückel tak hingga, menjelaskan distorsi Peierls, dan membedakan logam, semikonduktor, dan isolator.
13. Menurunkan struktur pita π grafena dan menjelaskan kerucut Dirac.
:::

::: {.mat}
**Prasyarat**

Dari Bab 2: matriks, determinan, dan nilai eigen (subbab 2.7, 2.8), deret Fourier dan bilangan kompleks (2.1, 2.9). Dari Bab 3: model elektron bebas untuk poliena (3.8). Dari Bab 8: fungsi variasi linear dan persamaan sekuler (8.4, 8.5), perturbasi orde kedua (8.7). Dari Bab 9: determinan Slater dan metode Hartree–Fock (9.6, 9.8). Dari Bab 10: tabel karakter, SALC, OM berdasar simetri, aturan seleksi elektronik (10.5–10.8, 10.10). Dari Bab 11: OM diatom, integral tumpang tindih dan Coulomb (11.4–11.8). Dari Bab 12: orbital terlokalisasi dan spektrum fotoelektron metana (subbab 12.13), resonansi benzena (12.10).
:::

## 13.1 OM delokalisasi vs orbital lokal

### LCAO untuk molekul poliatom

Gagasan LCAO dari Bab 11 berlaku tanpa perubahan untuk molekul berapa pun ukurannya. Kita memilih himpunan orbital atom (fungsi basis) $\{\chi_\mu\}$ pada semua atom, dan menulis setiap orbital molekul sebagai

$$
\psi_i = \sum_{\mu = 1}^{M}c_{\mu i}\,\chi_\mu . \qquad \text{(13.1)}
$$

Untuk H₂O dengan basis minimal (orbital $1s$, $2s$, dan tiga $2p$ oksigen, ditambah $1s$ setiap hidrogen) $M = 7$, sehingga terbentuk tujuh OM. Untuk benzena dengan basis minimal $M = 36$. Banyaknya OM selalu sama dengan banyaknya fungsi basis: orbital tidak diciptakan atau dimusnahkan, hanya dicampur.

Koefisien $c_{\mu i}$ ditentukan dengan metode variasi linear (subbab 8.4). Meminimumkan energi orbital terhadap koefisien menghasilkan persamaan sekuler, yang dalam bentuk matriks adalah **masalah nilai eigen yang diperumum**

$$
\mathbf H\mathbf c_i = \varepsilon_i\,\mathbf S\mathbf c_i , \qquad H_{\mu\nu} = \langle\chi_\mu|\hat h|\chi_\nu\rangle , \quad S_{\mu\nu} = \langle\chi_\mu|\chi_\nu\rangle , \qquad \text{(13.2)}
$$

dengan $\hat h$ operator satu elektron efektif. Dalam metode Hartree–Fock, $\hat h$ adalah operator Fock, yang bergantung pada orbital-orbital itu sendiri sehingga persamaan harus diselesaikan secara iteratif (persamaan Roothaan, subbab 17.3). Dalam metode semiempiris seperti metode Hückel, unsur-unsur $H_{\mu\nu}$ diambil dari parameter empiris, sehingga (13.2) diselesaikan sekali saja. Bagaimanapun caranya, persamaan (13.2) adalah inti teori orbital molekul, dan menyelesaikannya berarti mendiagonalisasi matriks.

### Simetri memecah masalah

Bila molekul mempunyai simetri, kita tidak perlu mendiagonalisasi matriks $M \times M$ sekaligus. Fungsi basis dapat diganti dengan **kombinasi linear teradaptasi simetri** (SALC, subbab 10.7) yang masing-masing termasuk satu representasi tak tereduksi grup titik. Unsur matriks Hamiltonian antara SALC dari representasi yang berbeda selalu nol, sehingga matriks Hamiltonian menjadi diagonal per blok: setiap blok simetri diselesaikan sendiri. Untuk H₂O ($C_{2v}$), matriks $7 \times 7$ pecah menjadi satu blok $4 \times 4$ ($a_1$), satu blok $2 \times 2$ ($b_2$), dan satu blok $1 \times 1$ ($b_1$). Setiap OM yang dihasilkan diberi label simetrinya: $1a_1$, $2a_1$, $1b_2$, dan seterusnya, dengan angka di depan menghitung orbital-orbital dengan simetri yang sama dari energi terendah.

### Orbital kanonik dan orbital terlokalisasi

Orbital-orbital yang diperoleh dengan menyelesaikan (13.2) disebut **orbital kanonik**. Mereka mempunyai dua sifat penting: setiap orbital adalah fungsi eigen operator satu elektron, dengan energi $\varepsilon_i$ yang terdefinisi, dan setiap orbital bersimetri seperti salah satu representasi tak tereduksi. Konsekuensinya, orbital kanonik pada umumnya **tersebar ke seluruh molekul**: misalnya orbital $1t_2$ metana memuat keempat atom H.

Di subbab 12.13 kita telah melihat bahwa orbital-orbital terisi dapat ditransformasi secara uniter tanpa mengubah fungsi gelombang total. Orbital terlokalisasi (ikatan dua pusat, pasangan bebas) yang diperoleh dengan cara itu sama sahnya. Pembagian kerja kedua jenis orbital itu jelas:

| Pertanyaan | Orbital yang lebih alami |
|---|---|
| Ikatan mana yang terbentuk, sudut dan hibridisasi | terlokalisasi |
| Energi ionisasi, spektrum fotoelektron | kanonik |
| Spektrum UV, keadaan tereksitasi | kanonik |
| Reaksi dengan elektrofil dan nukleofil (HOMO, LUMO) | kanonik |
| Transferabilitas sifat ikatan (C–H mirip di banyak molekul) | terlokalisasi |

Bab ini sebagian besar memakai orbital kanonik, karena kita akan banyak membahas spektroskopi dan reaktivitas.

### Tiga aturan pembentukan OM

Dari persamaan sekuler dua orbital (subbab 11.4) kita memperoleh tiga aturan praktis yang berlaku untuk molekul apa pun:

1. **Simetri.** Hanya orbital dengan simetri yang sama yang bercampur.
2. **Tumpang tindih.** Makin besar tumpang tindih, makin besar pemisahan antara kombinasi ikatan dan antiikatan.
3. **Kecocokan energi.** Dua orbital dengan energi yang hampir sama bercampur kuat (koefisien hampir sama); dua orbital yang energinya jauh berbeda bercampur lemah, dan orbital ikatan menyerupai orbital yang lebih rendah, orbital antiikatan menyerupai yang lebih tinggi.

Ada satu akibat dari tumpang tindih yang perlu ditekankan. Untuk dua orbital dengan energi $\alpha$ yang sama, interaksi $\beta$, dan tumpang tindih $S$, persamaan sekulernya memberikan

$$
E_\pm = \frac{\alpha \pm \beta}{1 \pm S} . \qquad \text{(13.3)}
$$

Karena penyebut $1 + S > 1 - S$, orbital antiikatan **lebih tidak stabil** daripada orbital ikatan **stabil** (Contoh 13.3). Bila kedua orbital terisi (empat elektron), totalnya adalah tolakan. Inilah asal tolakan antara dua molekul berkulit tertutup (He···He, tolakan sterik antara dua ikatan C–H) yang sering disebut **tolakan Pauli** atau tolakan tumpang tindih.

![Gambar 13.1 Empat orbital molekul valensi terisi H₂O dari perhitungan Hückel diperluas (Contoh 13.5). Tiga panel pertama: bidang molekul ($yz$); panel terakhir: bidang tegak lurus yang memuat sumbu $C_2$ ($xz$), karena $1b_1$ adalah orbital $2p_x$ oksigen yang tegak lurus bidang molekul. Biru dan jingga: tanda fungsi gelombang; titik: inti.](fig/c_air.png){width=94%}

::: {.contoh}
**Contoh 13.1 · Orbital molekul BeH₂**

Untuk BeH₂ linear (sumbu $z$), (a) susun SALC dari kedua orbital $1s$ hidrogen, $h_a$ dan $h_b$, dan tentukan orbital Be yang dapat bercampur dengan masing-masing. (b) Perhitungan Hückel diperluas (Be–H 133 pm) memberikan dua OM terisi: $2\sigma_g$ ($-15{,}67$ eV) $= 0{,}392\,(2s) + 0{,}490\,(h_a + h_b)$ dan $1\sigma_u$ ($-14{,}02$ eV) $= 0{,}244\,(2p_z) + 0{,}573\,(h_a - h_b)$. Tafsirkan. (c) Apa peran $2p_x$ dan $2p_y$?

**Penyelesaian.** (a) $h_a + h_b$ simetris terhadap inversi ($\sigma_g$) dan bercampur dengan $2s$ Be. $h_a - h_b$ antisimetris ($\sigma_u$) dan bercampur dengan $2p_z$. (b) Kedua OM terisi adalah orbital ikatan tiga pusat: satu dari $2s$, satu dari $2p_z$. Koefisien H lebih besar daripada koefisien Be karena orbital $1s$ H ($-13{,}6$ eV) lebih rendah daripada orbital valensi Be ($-10{,}0$ dan $-6{,}0$ eV): pasangan elektron ikatan lebih banyak berada di H. (c) $2p_x$ dan $2p_y$ ($\pi_u$) tidak mempunyai pasangan simetri di antara orbital H, sehingga tetap murni, nonikatan, dan kosong ($-6{,}0$ eV).

**Memahami hasil.** Empat elektron valensi BeH₂ mengisi dua OM ikatan yang masing-masing meliputi ketiga atom. Tidak ada OM yang terlokalisasi pada satu ikatan Be–H. Orbital $\pi_u$ yang kosong adalah LUMO, dan inilah sifat asam Lewis BeH₂ dalam bahasa orbital molekul.
:::

::: {.contoh}
**Contoh 13.2 · Dari OM kanonik ke ikatan lokal**

Dengan koefisien Contoh 13.1, bentuk $\lambda_\pm = (2\sigma_g \pm 1\sigma_u)/\sqrt2$. (a) Tuliskan $\lambda_+$. (b) Berapa karakter $s$ bagian berilium dari $\lambda_+$? Bandingkan dengan hibrida sp.

**Penyelesaian.** (a) $\lambda_+ = \tfrac{1}{\sqrt2}[0{,}392\,(2s) + 0{,}244\,(2p_z) + (0{,}490 + 0{,}573)h_a + (0{,}490 - 0{,}573)h_b] = 0{,}277\,(2s) + 0{,}172\,(2p_z) + 0{,}752\,h_a - 0{,}059\,h_b$. (b) Bagian Be: $0{,}277^2/(0{,}277^2 + 0{,}172^2) = 0{,}0767/0{,}1063 = 0{,}72$.

**Memahami hasil.** Kombinasi $\lambda_+$ hampir sepenuhnya terlokalisasi pada ikatan Be–H$_a$: koefisien H$_a$ 0,752, H$_b$ hanya $-0{,}059$. Bagian berilium adalah hibrida $s$–$p$ yang menunjuk ke H$_a$, dengan 72% $s$ alih-alih 50%. Perbedaan ini muncul karena $2\sigma_g$ dan $1\sigma_u$ tidak memakai orbital Be dengan bobot yang sama; dengan kata lain, transformasi dari orbital kanonik ke orbital lokal tidak harus menghasilkan hibrida "baku". Gambaran hibrida sp di subbab 12.3 adalah pendekatan yang baik, tetapi bukan hukum.
:::

::: {.contoh}
**Contoh 13.3 · Ikatan dan antiikatan tidak simetris**

Dua orbital karbon $2p$ ($\alpha = -11{,}4$ eV) dengan tumpang tindih $S = 0{,}25$ berinteraksi. Ambil $\beta = 1{,}75\,S\,\alpha$ (rumus Wolfsberg–Helmholz). (a) Hitung $E_+$ dan $E_-$ dengan (13.3). (b) Hitung stabilisasi bila dua elektron mengisi orbital ikatan, dan perubahan energi bila empat elektron mengisi keduanya.

**Penyelesaian.** (a) $\beta = 1{,}75(0{,}25)(-11{,}4) = -4{,}99$ eV. $E_+ = (-11{,}4 - 4{,}99)/1{,}25 = -13{,}11$ eV; $E_- = (-11{,}4 + 4{,}99)/0{,}75 = -8{,}55$ eV. (b) Dua elektron: $2(-13{,}11) - 2(-11{,}4) = -3{,}42$ eV. Empat elektron: $2(-13{,}11) + 2(-8{,}55) - 4(-11{,}4) = +2{,}28$ eV.

**Memahami hasil.** Orbital ikatan turun 1,71 eV, sedangkan orbital antiikatan naik 2,85 eV. Dengan empat elektron, sistem lebih tidak stabil daripada kedua fragmen yang terpisah. Inilah sebabnya He₂ tidak terikat, dan mengapa dua molekul berkulit tertutup saling menolak bila awan elektronnya tumpang tindih. Tolakan sterik dalam kimia organik, misalnya antara gugus-gugus yang berdesakan, pada dasarnya adalah efek ini.
:::

::: {.contoh}
**Contoh 13.4 · Menghitung orbital dan elektron**

Untuk basis minimal (orbital $1s$ untuk H; $1s$, $2s$, $2p$ untuk atom periode 2), tentukan banyaknya OM total, banyaknya elektron, dan banyaknya OM terisi untuk H₂O, NH₃, CH₄, dan C₂H₄. Berapa OM valensi yang terisi?

**Penyelesaian.** H₂O: $5 + 2 = 7$ OM, 10 elektron, 5 terisi (4 valensi). NH₃: $5 + 3 = 8$ OM, 10 elektron, 5 terisi (4 valensi). CH₄: $5 + 4 = 9$ OM, 10 elektron, 5 terisi (4 valensi). C₂H₄: $2(5) + 4 = 14$ OM, 16 elektron, 8 terisi (6 valensi).

**Memahami hasil.** Ketiga molekul isoelektronik H₂O, NH₃, dan CH₄ mempunyai lima OM terisi: satu orbital $1s$ inti dan empat orbital valensi. Perbedaannya terletak pada **berapa banyak** dari keempat orbital valensi itu yang ikatan dan berapa yang pasangan bebas, yang ditentukan oleh simetri dan geometri (subbab 13.2). Etilena mempunyai enam OM valensi terisi: lima σ dan satu π.
:::

::: {.kuis}
**Kuis cepat 13.1**

Benzena dengan basis minimal mempunyai 36 OM. Berapa yang terisi? Berapa di antaranya orbital π?
:::

## 13.2 OM H₂O, NH₃, CH₄ dari simetri

### Air ($C_{2v}$)

Letakkan molekul di bidang $yz$ dengan sumbu $C_2$ sepanjang $z$. Kedua orbital $1s$ hidrogen membentuk dua SALC: $h_+ = (h_a + h_b)/\sqrt{2(1 + S_{ab})}$ bersimetri $a_1$, dan $h_- = (h_a - h_b)/\sqrt{2(1 - S_{ab})}$ bersimetri $b_2$. Orbital oksigen: $2s$ dan $2p_z$ bersimetri $a_1$, $2p_y$ bersimetri $b_2$, dan $2p_x$ (tegak lurus bidang molekul) bersimetri $b_1$. Klasifikasi ini mengikuti langsung dari tabel karakter $C_{2v}$:

| | $E$ | $C_2$ | $\sigma_v(xz)$ | $\sigma_v'(yz)$ | orbital |
|---|---|---|---|---|---|
| $A_1$ | 1 | 1 | 1 | 1 | O $2s$, $2p_z$; $h_+$ |
| $A_2$ | 1 | 1 | $-1$ | $-1$ | — |
| $B_1$ | 1 | $-1$ | 1 | $-1$ | O $2p_x$ |
| $B_2$ | 1 | $-1$ | $-1$ | 1 | O $2p_y$; $h_-$ |

Blok-blok yang dihasilkan:

* **$a_1$** (tiga orbital valensi: $2s$, $2p_z$, $h_+$) memberikan tiga OM: $2a_1$ (terutama $2s$ oksigen, sedikit ikatan), $3a_1$ (campuran $2p_z$ dan $2s$ dengan sedikit $h_+$, sebagian ikatan, sebagian pasangan bebas), dan $4a_1$ (antiikatan, kosong).
* **$b_2$** ($2p_y$, $h_-$) memberikan $1b_2$ (ikatan O–H yang jelas) dan $2b_2$ (antiikatan).
* **$b_1$** ($2p_x$) sendirian: $1b_1$, pasangan bebas murni.

Delapan elektron valensi mengisi $2a_1^2\,1b_2^2\,3a_1^2\,1b_1^2$. HOMO adalah $1b_1$, orbital $2p$ oksigen yang tegak lurus bidang molekul (Gambar 13.1). Perhitungan Hückel diperluas (Contoh 13.5) memberikan energi orbital $-33{,}3$; $-17{,}1$; $-15{,}5$; $-14{,}8$ eV, sejajar dengan energi ionisasi terukur 32,2; 18,5; 14,7; 12,6 eV. Urutan dan pemisahan kasarnya benar; nilai mutlaknya tidak terlalu penting karena metode Hückel diperluas adalah metode semiempiris.

Bandingkan dengan subbab 12.6 dan 12.13: pasangan bebas σ dan π dari bahasa hibridisasi kini muncul sebagai $3a_1$ dan $1b_1$. Pasangan bebas "telinga kelinci" adalah kombinasi $3a_1 \pm 1b_1$ (setelah sebagian $3a_1$ yang bersifat ikatan dipisahkan).

### Amonia ($C_{3v}$)

Ketiga orbital $1s$ hidrogen membentuk SALC $a_1$ ($h_1 + h_2 + h_3$) dan pasangan $e$ ($2h_1 - h_2 - h_3$ dan $h_2 - h_3$, dinormalisasi). Orbital nitrogen: $2s$ dan $2p_z$ ($a_1$, dengan $z$ sepanjang sumbu $C_3$), dan $(2p_x, 2p_y)$ ($e$). Delapan elektron valensi mengisi $2a_1^2\,1e^4\,3a_1^2$. Orbital $1e$ adalah dua orbital ikatan N–H yang berdegenerasi; HOMO $3a_1$ adalah pasangan bebas nitrogen, terutama $2p_z$ dengan sedikit $2s$, menunjuk keluar dari puncak piramida. Spektrum fotoelektron menunjukkan pita $3a_1$ di sekitar 10,9 eV, pita $1e$ di sekitar 16 eV, dan pita $2a_1$ di sekitar 27 eV.

HOMO amonia yang tinggi dan terarah menjelaskan sifat-sifat kimianya: amonia adalah basa Brønsted, nukleofil, dan ligan yang baik. Ketika NH₃ menjadi datar (keadaan transisi inversi, subbab 3.12), $3a_1$ berubah menjadi $2p_z$ murni ($a_2''$ dalam $D_{3h}$), yang energinya lebih tinggi karena kehilangan karakter $2s$ dan sedikit sifat ikatannya.

### Metana ($T_d$)

Keempat orbital $1s$ hidrogen membentuk SALC $a_1$ ($\tfrac12(h_1 + h_2 + h_3 + h_4)$) dan tiga SALC $t_2$, dengan pola tanda yang sama seperti bagian $p$ hibrida sp³ (12.23): $\tfrac12(h_1 + h_2 - h_3 - h_4)$ bersimetri seperti $p_x$, dan seterusnya. Orbital karbon: $2s$ ($a_1$) dan $(2p_x, 2p_y, 2p_z)$ ($t_2$). Diagram OM metana sangat sederhana: $2a_1$ ikatan dari $2s$ + SALC $a_1$, tiga $1t_2$ ikatan dari $2p$ + SALC $t_2$, dan pasangan antiikatannya $3a_1^*$ dan $2t_2^*$. Delapan elektron valensi mengisi $2a_1^2\,1t_2^6$. Inilah asal dua pita dalam spektrum fotoelektron metana, 22,9 eV ($2a_1$) dan 14,4 eV ($1t_2$), yang telah kita bahas dalam bahasa ikatan lokal di subbab 12.13.

Metana tidak mempunyai pasangan bebas; HOMO-nya adalah orbital ikatan C–H. Karena itu metana sangat tidak reaktif terhadap elektrofil biasa, tetapi dalam asam super (misalnya HSO₃F–SbF₅) ia dapat diprotonasi menjadi CH₅⁺, dengan elektron ikatan $1t_2$ yang bertindak sebagai donor ke H⁺ dan membentuk ikatan tiga pusat dua elektron (subbab 12.9).

::: {.inti}
**Pola diagram OM molekul hidrida AH$_n$.** Orbital $1s$ hidrogen digabung dulu menjadi SALC. Setiap SALC bercampur dengan orbital atom pusat yang sesimetri; orbital pusat yang tidak mempunyai pasangan sesimetri menjadi orbital nonikatan (pasangan bebas atau orbital kosong). Delapan elektron valensi mengisi empat OM terendah. Banyaknya pasangan bebas (CH₄ 0, NH₃ 1, H₂O 2) mengikuti dari berapa banyak orbital pusat yang tidak "terpakai" oleh SALC hidrogen.
:::

::: {.contoh}
**Contoh 13.5 · Hückel diperluas untuk air**

Metode Hückel diperluas (R. Hoffmann, 1963) memakai orbital Slater valensi, menghitung semua integral tumpang tindih $S_{\mu\nu}$, mengambil $H_{\mu\mu}$ sama dengan negatif energi ionisasi orbital valensi atom (O $2s$: $-32{,}3$ eV, O $2p$: $-14{,}8$ eV, H $1s$: $-13{,}6$ eV), dan $H_{\mu\nu} = 1{,}75\,S_{\mu\nu}(H_{\mu\mu} + H_{\nu\nu})/2$. Untuk H₂O (O–H 95,8 pm, 104,5°) hasilnya:

| OM | $\varepsilon$ (eV) | komponen utama | IE terukur (eV) |
|---|---|---|---|
| $2a_1$ | $-33{,}3$ | O $2s$ (0,87), sedikit H | 32,2 |
| $1b_2$ | $-17{,}1$ | O $2p_y$ (0,72), $h_a - h_b$ (0,34) | 18,5 |
| $3a_1$ | $-15{,}5$ | O $2p_z$ (0,92), O $2s$, $h_a + h_b$ (0,14) | 14,7 |
| $1b_1$ | $-14{,}8$ | O $2p_x$ (1,00) | 12,6 |

(a) Mengapa $\varepsilon(1b_1)$ tepat sama dengan $H_{2p}$ oksigen? (b) Analisis populasi Mulliken memberikan muatan O $-0{,}88$ dan H $+0{,}44$. Apakah angka ini dapat dipercaya?

**Penyelesaian.** (a) $1b_1$ adalah satu-satunya orbital bersimetri $b_1$; tidak ada orbital lain yang dapat bercampur dengannya, sehingga ia tetap $2p_x$ murni dengan energi $H_{2p}$. (b) Metode Hückel diperluas tidak memperhitungkan tolakan elektron secara eksplisit, sehingga tidak ada yang mencegah muatan menumpuk pada atom elektronegatif. Muatan yang dihasilkan cenderung terlalu besar; arah polaritasnya (O negatif) benar.

**Memahami hasil.** Dengan satu parameter per jenis orbital dan satu tetapan 1,75, metode ini memberi urutan orbital, simetri, dan energi kasar yang benar. Ia dikembangkan untuk molekul organik dan senyawa logam transisi yang terlalu besar bagi perhitungan *ab initio* pada tahun 1960-an, dan memberi dasar orbital bagi aturan Woodward–Hoffmann (Hadiah Nobel Hoffmann, 1981). Kelemahannya tampak di subbab 13.3: ia meramalkan sudut H₂O terlalu besar.
:::

::: {.contoh}
**Contoh 13.6 · SALC dengan operator proyeksi**

Dengan operator proyeksi $\hat P^{(\Gamma)} = \sum_R\chi^{(\Gamma)}(R)\,\hat R$ (subbab 10.7) dan tabel karakter $C_{2v}$, proyeksikan $h_a$ ke $A_1$ dan $B_2$. Operasi pada $h_a$: $\hat E h_a = h_a$, $\hat C_2h_a = h_b$, $\hat\sigma_v(xz)h_a = h_b$, $\hat\sigma_v'(yz)h_a = h_a$.

**Penyelesaian.** $\hat P^{(A_1)}h_a = h_a + h_b + h_b + h_a = 2(h_a + h_b)$. $\hat P^{(B_2)}h_a = h_a - h_b - h_b + h_a = 2(h_a - h_b)$. $\hat P^{(A_2)}h_a = h_a + h_b - h_b - h_a = 0$; $\hat P^{(B_1)}h_a = h_a - h_b + h_b - h_a = 0$.

**Memahami hasil.** Setelah dinormalisasi, SALC-nya $h_\pm$ seperti di atas. Representasi yang dibentuk oleh kedua orbital H adalah $A_1 + B_2$; karena tidak ada SALC $B_1$, orbital $2p_x$ oksigen tidak mempunyai pasangan dan menjadi pasangan bebas murni. Simetri saja, tanpa hitungan energi, sudah memastikan bahwa HOMO air adalah orbital $2p$ oksigen yang tegak lurus bidang molekul.
:::

::: {.contoh}
**Contoh 13.7 · Teorema Koopmans untuk tiga hidrida**

Perhitungan Hückel diperluas memberikan (dalam eV): CH₄ $2a_1$ $-24{,}6$, $1t_2$ $-15{,}5$; NH₃ $2a_1$ $-28{,}0$, $1e$ $-16{,}5$, $3a_1$ $-13{,}8$. Bandingkan dengan energi ionisasi terukur (CH₄: 22,9 dan 14,4; NH₃: sekitar 27, 16, dan 10,9 eV). Orbital mana yang paling buruk diramalkan, dan mengapa?

**Penyelesaian.** Selisih $-\varepsilon$ terhadap IE: CH₄ $2a_1$ +1,7, $1t_2$ +1,1; NH₃ $2a_1$ +1,0, $1e$ +0,5, $3a_1$ +2,9 eV. Pasangan bebas NH₃ ($3a_1$) paling buruk.

**Memahami hasil.** Teorema Koopmans (subbab 17.4) menyamakan energi ionisasi dengan $-\varepsilon_i$ dan mengabaikan relaksasi orbital ion. Pasangan bebas yang terlokalisasi pada satu atom paling banyak mengalami relaksasi ketika elektronnya dilepas, sehingga galatnya paling besar. Dalam metode Hückel diperluas, energi pasangan bebas N juga dipatok dekat $H_{2p}$ nitrogen ($-13{,}4$ eV), yang tidak memperhitungkan bahwa N dalam NH₃ bermuatan negatif dan lebih mudah diionisasi daripada atom N bebas (14,5 eV).
:::

::: {.kuis}
**Kuis cepat 13.2**

Pada H₂S, orbital $1b_1$ masih merupakan HOMO. Dari $3p$ atom apa ia berasal, dan mengapa energinya lebih tinggi daripada $1b_1$ air (energi ionisasi H₂S 10,5 eV)?
:::

## 13.3 Diagram Walsh dan bentuk molekul

### Gagasan Walsh

A. D. Walsh (1953) mengajukan pertanyaan sederhana: bagaimana energi setiap OM berubah bila geometri molekul diubah, misalnya bila sudut ikatan AH₂ dibuka dari bengkok ke linear? Plot energi orbital terhadap sudut disebut **diagram Walsh**. Aturan Walsh: bentuk molekul adalah bentuk yang membuat orbital-orbital **terisi**, terutama yang paling tinggi, paling stabil. Aturan ini kasar (jumlah energi orbital bukan energi total), tetapi kecenderungannya sering benar dan selalu bermakna kimia.

### Diagram Walsh molekul AH₂

Mulailah dari AH₂ linear ($D_{\infty h}$). Orbital valensinya: $2\sigma_g$ ($2s$ A + $h_a + h_b$, ikatan), $1\sigma_u$ ($2p_z$ A + $h_a - h_b$, ikatan), $1\pi_u$ ($2p_x$, $2p_y$ A, nonikatan dan berdegenerasi), lalu $3\sigma_g$ dan $2\sigma_u$ (antiikatan). Bila molekul dibengkokkan (simetri turun ke $C_{2v}$), setiap orbital berubah (Gambar 13.2):

* $2\sigma_g \to 2a_1$: hampir tidak berubah. Kedua H yang saling mendekat menambah sedikit sifat ikatan $h_a$–$h_b$ (dalam perhitungan yang teliti orbital ini sedikit turun), tetapi orbital ini didominasi $2s$ atom pusat yang tidak berarah.
* $1\sigma_u \to 1b_2$: **naik**. Orbital ini memakai $2p$ yang semula mengarah tepat ke kedua H; ketika H keluar dari sumbu $p$, tumpang tindihnya berkurang.
* $1\pi_u \to 3a_1 + 1b_1$: degenerasinya pecah. Komponen di bidang lengkungan ($3a_1$) **turun tajam**: ia kini dapat bertumpang tindih dengan kedua H dan bercampur dengan $2s$ A, sehingga berubah dari orbital nonikatan menjadi sebagian ikatan. Komponen yang tegak lurus bidang ($1b_1$) tidak berubah, karena tetap tidak dapat bertumpang tindih dengan H.

![Gambar 13.2 Diagram Walsh H₂O dari perhitungan Hückel diperluas: energi orbital valensi terhadap sudut H–O–H. Label kiri: simetri $C_{2v}$; label kanan: simetri $D_{\infty h}$. Orbital $3a_1$ turun ketika molekul dibengkokkan, $1b_2$ naik, $1b_1$ tetap. Sumbu tegak dipatahkan; orbital $2a_1$ (sekitar $-33$ eV) tidak ditampilkan.](fig/c_walsh.png){width=72%}

Akibatnya bergantung pada banyaknya elektron valensi:

* **4 elektron** ($2\sigma_g^2\,1\sigma_u^2$): BeH₂, BH₂⁺. Membengkokkan menaikkan $1b_2$ dan hampir tidak menguntungkan $2a_1$. **Linear.**
* **5–6 elektron**: BH₂ ($3a_1^1$), CH₂. Elektron dalam $3a_1$ sangat diuntungkan oleh lengkungan. **Bengkok.** BH₂ 131°. Metilena triplet ($3a_1^1\,1b_1^1$) 134°; metilena singlet ($3a_1^2$) 102°: dua elektron di $3a_1$ memberi dorongan lengkung dua kali lebih besar.
* **7–8 elektron**: NH₂ ($3a_1^2\,1b_1^1$), H₂O ($3a_1^2\,1b_1^2$). Elektron di $1b_1$ tidak peduli pada sudut; yang menentukan masih $3a_1^2$. **Bengkok**, sekitar 103–105°.

Diagram Walsh memberikan cara lain untuk memahami mengapa sudut air jauh dari 180°, tanpa menyebut hibridisasi: orbital $3a_1$ yang terisi, yang dalam bahasa ikatan valensi adalah pasangan bebas σ, menjadi lebih stabil ketika molekul dibengkokkan karena ia dapat mengambil karakter $2s$.

### Keterbatasan kuantitatif

Tabel berikut membandingkan sudut yang meminimumkan jumlah energi orbital terisi dalam perhitungan Hückel diperluas dengan sudut teramati.

| Molekul | Elektron valensi | Hückel diperluas | Teramati |
|---|---|---|---|
| BeH₂ | 4 | 180° | 180° |
| BH₂ | 5 | 132° | 131° |
| CH₂ triplet | 6 | 154° | 134° |
| CH₂ singlet | 6 | 114° | 102° |
| NH₂ | 7 | 126° | 103° |
| H₂O | 8 | 140° | 104,5° |

Ramalan kualitatif (4 elektron linear, lebih banyak elektron bengkok, singlet lebih bengkok daripada triplet) selalu benar. Ramalan kuantitatifnya memburuk bila atom pusat makin elektronegatif. Pada oksigen, selisih energi $2s$–$2p$ sangat besar (17,5 eV dalam parameter Hückel diperluas), sehingga pencampuran $2s$ ke dalam $3a_1$ terlalu lemah: Gambar 13.2 menunjukkan bahwa $3a_1$ hanya turun 0,7 eV dari 180° ke 104,5°, padahal perhitungan Hartree–Fock memberikan penurunan beberapa eV. Selain itu, jumlah energi orbital mengabaikan tolakan inti–inti dan menghitung tolakan elektron secara tidak tepat. Diagram Walsh dari perhitungan *ab initio* (Bab 17) mereproduksi sudut-sudut ini dengan baik.

### Molekul AH₃ dan AB₂

Diagram Walsh untuk AH₃ (datar $D_{3h}$ vs piramida $C_{3v}$) mempunyai satu orbital kunci: orbital $a_2''$ ($p_z$ atom pusat yang tegak lurus bidang) pada bentuk datar menjadi $3a_1$ pada piramida, dan turun ketika molekul menjadi piramida karena dapat mengambil karakter $s$. Dengan 6 elektron valensi (BH₃, CH₃⁺), orbital ini kosong: **datar**. Dengan 7 (radikal CH₃), ia setengah terisi: hampir datar, dengan gerak "payung" yang lunak. Dengan 8 (NH₃, H₃O⁺, CH₃⁻): **piramida**.

Untuk molekul triatomik AB₂ dari atom-atom periode 2, aturan Walsh yang terkenal: **16 elektron valensi linear** (CO₂, N₃⁻, NO₂⁺, OCS), **17 sampai 20 elektron bengkok**, dengan sudut yang mengecil ketika elektron bertambah: NO₂ (17) 134°, O₃ dan NO₂⁻ (18) 117° dan 115°, SO₂ 119,5°, OF₂ (20) 103°. Elektron ke-17 masuk ke orbital ($6a_1$) yang pada molekul linear adalah orbital π* antiikatan, dan yang menjadi lebih stabil ketika molekul dibengkokkan.

::: {.contoh}
**Contoh 13.8 · Bentuk ion dan radikal NO₂**

Tentukan banyaknya elektron valensi dan ramalkan bentuk NO₂⁺, NO₂, dan NO₂⁻. Bandingkan dengan percobaan: NO₂⁺ linear, NO₂ 134,1°, NO₂⁻ 115,4°. Mengapa NO₂ cenderung berdimerisasi menjadi N₂O₄?

**Penyelesaian.** NO₂⁺: $5 + 12 - 1 = 16$, linear. NO₂: 17, bengkok. NO₂⁻: 18, lebih bengkok. Ramalan sesuai. NO₂ mempunyai satu elektron dalam $6a_1$, orbital yang terutama berada pada atom N dan menunjuk ke luar dari sudut molekul. Dua radikal NO₂ memasangkan elektron itu menjadi ikatan N–N.

**Memahami hasil.** Elektron ke-17 cukup untuk membengkokkan molekul, dan elektron ke-18 membengkokkannya lebih jauh. Dalam bahasa ikatan valensi, NO₂⁻ dan O₃ mempunyai satu pasangan bebas pada atom pusat (AX₂E, subbab 12.11), sedangkan NO₂ mempunyai "setengah pasangan bebas". Diagram Walsh dan VSEPR memberikan ramalan yang sama, tetapi Walsh juga menangani radikal dan keadaan tereksitasi.
:::

::: {.contoh}
**Contoh 13.9 · Keadaan tereksitasi yang berubah bentuk**

Asetilena (HCCH) linear dalam keadaan dasar. Pada eksitasi $\pi \to \pi^*$ pertama, satu elektron berpindah ke orbital π*. Diagram Walsh untuk HAAH menunjukkan bahwa salah satu komponen π* turun tajam bila molekul dibengkokkan secara trans. Apa ramalan untuk bentuk keadaan tereksitasi itu? Bandingkan dengan formaldehida, yang datar dalam keadaan dasar tetapi menjadi piramida dalam keadaan tereksitasi $n \to \pi^*$.

**Penyelesaian.** Dengan satu elektron di π* yang distabilkan oleh lengkungan trans, keadaan tereksitasi pertama asetilena **bengkok trans** (teramati: sudut C–C–H sekitar 120°). Pada formaldehida, eksitasi $n \to \pi^*$ menaruh elektron di π* C=O, yang distabilkan bila atom C menjadi piramida (orbital π* mengambil karakter $s$); keadaan tereksitasi formaldehida memang piramidal.

**Memahami hasil.** Perubahan bentuk saat eksitasi menyebabkan deret getaran panjang dalam spektrum elektronik (asas Franck–Condon, subbab 15.7). Spektrum UV asetilena sekitar 240 nm menunjukkan deret panjang getaran tekuk, yang ditafsirkan tepat seperti ramalan Walsh. Diagram Walsh adalah salah satu alat paling awal yang menghubungkan spektroskopi elektronik dengan geometri molekul.
:::

::: {.contoh}
**Contoh 13.10 · Membaca diagram Walsh secara kuantitatif**

Dari perhitungan Hückel diperluas H₂O (Gambar 13.2), energi orbital pada 180° dan 104,5° adalah: $1b_2$ $-17{,}85$ dan $-17{,}11$ eV; $3a_1$ $-14{,}80$ dan $-15{,}46$ eV; $1b_1$ $-14{,}80$ dan $-14{,}80$ eV. (a) Hitung perubahan jumlah energi orbital terisi (dua elektron per orbital) dari 180° ke 104,5°, dengan $2a_1$ $-33{,}27$ dan $-33{,}25$ eV. (b) Mengapa model ini meramalkan minimum di sekitar 140°, bukan 104,5°?

**Penyelesaian.** (a) $1b_2$: $2(-17{,}11 + 17{,}85) = +1{,}48$ eV. $3a_1$: $2(-15{,}46 + 14{,}80) = -1{,}32$ eV. $1b_1$: 0. $2a_1$ ($-33{,}25$ dan $-33{,}27$ eV): $+0{,}04$ eV. Total $+0{,}20$ eV: dalam model ini lengkungan sampai 104,5° justru sedikit merugikan.

\(b) Penurunan $3a_1$ (0,66 eV) terlalu kecil untuk mengimbangi kenaikan $1b_2$. Minimum jumlah energi berada di tempat kedua efek seimbang, sekitar 140°.

**Memahami hasil.** Arah perubahan setiap orbital benar, tetapi besarnya tidak. Diagram Walsh pada dasarnya adalah alat kualitatif: ia menunjukkan **orbital mana** yang mendorong ke arah mana. Untuk sudut yang teliti diperlukan energi total dari metode yang memperhitungkan tolakan elektron secara konsisten. Pelajaran ini berlaku untuk banyak model sederhana: kecenderungan dapat dipercaya, angka mutlak tidak selalu.
:::

::: {.kuis}
**Kuis cepat 13.3**

Ramalkan bentuk BH₂⁺ (4 elektron valensi), CH₂⁺ (5), dan H₃O⁺ (8). Mengapa CH₂ triplet kurang bengkok daripada CH₂ singlet?
:::
