# Bab 12 Hibridisasi dan Teori Ikatan Valensi Molekul Poliatom

Atom karbon dalam keadaan dasar mempunyai konfigurasi $1s^2 2s^2 2p^2$, dengan dua elektron tak berpasangan di orbital $2p$. Menurut gagasan paling sederhana tentang ikatan kovalen (satu ikatan untuk setiap elektron tak berpasangan), karbon seharusnya bervalensi dua dan hidrida paling stabilnya adalah CH₂, dengan sudut H–C–H 90° karena kedua orbital $p$ saling tegak lurus. Kenyataannya, hidrida karbon yang stabil adalah metana, CH₄, dengan empat ikatan C–H yang tidak dapat dibedakan satu sama lain, masing-masing membentuk sudut 109,47° dengan yang lain. Air, yang oksigennya juga hanya mempunyai dua elektron $p$ tak berpasangan, ternyata tidak bersudut 90° melainkan 104,5°; tetapi H₂S, satu periode di bawahnya, bersudut 92,1°, hampir tepat 90°. Dari mana karbon memperoleh empat ikatan yang setara, mengapa sudutnya tepat arccos$(-\tfrac13)$, dan mengapa oksigen "menyimpang" dari 90° sedangkan belerang hampir tidak?

Bab ini menjawab pertanyaan-pertanyaan itu dengan **teori ikatan valensi** (IV) untuk molekul poliatom. Teori ini memperluas gambaran Heitler–London tentang molekul H₂ (subbab 11.11): ikatan adalah sepasang elektron berspin berlawanan dalam dua orbital yang saling tumpang tindih. Untuk molekul poliatom, orbital-orbital atom harus terlebih dahulu "diarahkan" ke atom tetangga. Caranya adalah membentuk kombinasi linear orbital $s$ dan $p$ (kadang $d$) pada atom yang sama, yaitu **orbital hibrida**. Kita akan melihat bahwa sudut antarhibrida bukan sesuatu yang dihafal, melainkan akibat langsung syarat **ortogonalitas**: sudut tetrahedral 109,47° keluar dari satu baris aljabar. Dari sana kita sampai ke hibridisasi tak setara (air, amonia, aturan Bent), kaitan hibridisasi dengan sifat yang dapat diukur (panjang ikatan, keasaman C–H, kopling NMR), molekul "hipervalen" dan ikatan tiga pusat, resonansi, VSEPR, teori ikatan valensi modern, dan akhirnya uji yang menentukan: spektrum fotoelektron metana.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa karbon bervalensi empat, padahal atom karbon dalam keadaan dasar hanya mempunyai dua elektron tak berpasangan?
2. Mengapa sudut ikatan metana tepat 109,47°, dan mengapa sudut itu dapat diturunkan hanya dari syarat bahwa orbital-orbital hibrida harus saling ortogonal?
3. Mengapa sudut H–O–H air 104,5°, tetapi sudut H–S–H hanya 92,1°? Apa artinya bagi kebasaan NH₃ dan PH₃?
4. Mengapa ikatan C–H pada asetilena lebih pendek, lebih kuat, dan jauh lebih asam daripada pada etana?
5. Bagaimana SF₆ dan XeF₂ dapat terbentuk tanpa "oktet yang diperluas", dan bagaimana diborana dapat stabil dengan elektron yang "tidak cukup" untuk semua ikatannya?
6. Jika keempat ikatan C–H metana setara, mengapa spektrum fotoelektron metana menunjukkan dua pita, bukan satu?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menuliskan fungsi gelombang ikatan valensi pasangan sempurna untuk molekul poliatom dan memakai aturan energi pasangan spin.
2. Menyusun orbital hibrida sebagai kombinasi linear ortonormal orbital $s$ dan $p$, dan menghitung karakter $s$ serta arahnya.
3. Menurunkan sudut 180°, 120°, dan 109,47° dari syarat normalisasi, ortogonalitas, dan kesetaraan hibrida.
4. Memakai teorema Coulson, $1 + \lambda_i\lambda_j\cos\theta_{ij} = 0$, untuk menghitung karakter $s$ hibrida dari sudut ikatan, termasuk pada molekul dengan pasangan elektron bebas.
5. Menjelaskan aturan Bent dan memakainya untuk meramalkan sudut ikatan dan panjang ikatan dalam molekul bersubstituen.
6. Mengaitkan karakter $s$ dengan panjang ikatan, kekuatan ikatan, keasaman C–H, elektronegativitas orbital, dan tetapan kopling $^1J(^{13}\text{C–H})$.
7. Menjelaskan ikatan dalam molekul hipervalen dengan model ikatan tiga pusat empat elektron, dan menilai peran orbital $d$.
8. Menjelaskan ikatan tiga pusat dua elektron dalam diborana dan senyawa kekurangan elektron lainnya.
9. Menyusun fungsi gelombang resonansi dari struktur-struktur ikatan valensi, menghitung energi resonansi benzena, dan menaksir orde ikatan.
10. Meramalkan bentuk molekul dengan VSEPR dan menjelaskan dasar kuantumnya pada asas Pauli.
11. Menjelaskan gagasan teori ikatan valensi modern (GVB dan spin-coupled) dan menghitung fungsi gelombang GVB untuk H₂.
12. Menjelaskan mengapa spektrum fotoelektron metana tidak bertentangan dengan gambaran hibrida sp³, dan menilai kapan memakai teori ikatan valensi atau orbital molekul.
13. Memakai hibrida $d^2sp^3$, $dsp^2$, dan hibrida $sd^n$ untuk senyawa logam transisi, beserta keterbatasannya.
:::

::: {.mat}
**Prasyarat**

Dari Bab 2: vektor dan hasil kali dalam fungsi (subbab 2.6), matriks dan determinan (2.7), nilai eigen (2.8). Dari Bab 4: ortogonalitas fungsi eigen, notasi Dirac (4.8, 4.14). Dari Bab 6 dan 7: harmonik bola, orbital riil $s$, $p$, $d$ dan bentuknya (7.7, 7.8). Dari Bab 8 dan 9: metode variasi linear (8.4), spin dan determinan Slater (9.2, 9.6). Dari Bab 10: grup titik dan SALC (10.2, 10.7). Dari Bab 11: integral tumpang tindih, Coulomb, dan pertukaran (11.4), teori orbital molekul dan teori Heitler–London untuk H₂ (11.10–11.12).
:::

## 12.1 Dari ikatan valensi H₂ ke molekul poliatom

### Pelajaran dari Heitler–London

Pada tahun 1916 G. N. Lewis mengusulkan bahwa ikatan kovalen adalah **sepasang elektron** yang dimiliki bersama oleh dua atom. Sebelas tahun kemudian W. Heitler dan F. London memberi gagasan itu dasar kuantum (subbab 11.11). Untuk molekul H₂ dengan orbital $1s$ atom A dan B, yang kita tulis $a$ dan $b$, fungsi gelombang Heitler–London adalah

$$
\Psi_\text{HL} = \frac{a(1)b(2) + b(1)a(2)}{\sqrt{2(1 + S^2)}}\cdot\frac{\alpha(1)\beta(2) - \beta(1)\alpha(2)}{\sqrt2} , \qquad \text{(12.1)}
$$

dengan $S = \langle a|b\rangle$ integral tumpang tindih. Bagian ruangnya simetris dan bagian spinnya singlet (antisimetris), sehingga fungsi total antisimetris seperti yang dituntut asas Pauli. Energinya

$$
E_\text{HL} = \frac{Q + K}{1 + S^2} , \qquad \text{(12.2)}
$$

dengan $Q$ integral Coulomb (energi interaksi elektrostatik dua atom yang tidak terganggu) dan $K$ integral pertukaran. Pada jarak ikatan, $K$ bernilai negatif dan jauh lebih besar daripada $Q$; hampir seluruh energi ikatan berasal dari suku pertukaran, yang ada karena elektron tidak dapat dibedakan.

Tiga pelajaran dari H₂ akan kita bawa ke molekul poliatom:

1. **Ikatan terbentuk antara dua orbital yang masing-masing berisi satu elektron**, dan kedua spin itu berpasangan menjadi singlet.
2. **Kekuatan ikatan bertambah dengan tumpang tindih** kedua orbital. Integral pertukaran $K$ melibatkan hasil kali $a(1)b(1)$, yang hanya besar di daerah tempat kedua orbital sama-sama besar.
3. **Spin yang tidak berpasangan dengan pasangan ikatannya menolak.** Keadaan triplet H₂ mempunyai energi $(Q - K)/(1 - S^2)$, yang bersifat tolak-menolak pada semua jarak.

### Fungsi gelombang pasangan sempurna

Untuk molekul dengan banyak ikatan, misalnya CH₄, gagasan Heitler–London diperluas dengan memasangkan elektron-elektron menurut struktur Lewis. Setiap ikatan A–B mendapat satu orbital $\phi_A$ pada atom A dan satu orbital $\phi_B$ pada atom B, masing-masing berisi satu elektron, dan kedua elektron itu dipasangkan menjadi singlet. Fungsi gelombangnya

$$
\Psi_\text{PP} = \hat{\mathcal A}\left[\Phi_\text{inti}\prod_{\text{ikatan } k}\left(\phi_{A_k}\phi_{B_k} + \phi_{B_k}\phi_{A_k}\right)(\alpha\beta - \beta\alpha)\right] , \qquad \text{(12.3)}
$$

dengan $\hat{\mathcal A}$ operator antisimetrisasi (subbab 9.6) yang menjamin asas Pauli untuk seluruh elektron, dan $\Phi_\text{inti}$ fungsi elektron-elektron yang tidak ikut berikatan (elektron inti dan pasangan bebas). Fungsi ini disebut fungsi **pasangan sempurna** (*perfect pairing*). Inilah terjemahan kuantum yang langsung dari struktur Lewis: satu garis ikatan sama dengan satu pasangan singlet Heitler–London.

Bila kita mengabaikan tumpang tindih antarorbital dari ikatan yang berbeda dan hanya menyimpan integral pertukaran antara orbital-orbital yang bertetangga, energi fungsi pasangan sempurna mempunyai bentuk yang sangat sederhana:

$$
E_\text{PP} = Q + \sum_{\text{pasangan berikatan}}J_{ij} - \frac12\sum_{\text{pasangan tak berikatan}}J_{ij} , \qquad \text{(12.4)}
$$

dengan $Q$ jumlah semua integral Coulomb dan $J_{ij}$ integral pertukaran antara orbital $i$ dan $j$ (negatif bila keduanya tumpang tindih). Pasangan yang spinnya dipasangkan menjadi singlet menyumbang $+J_{ij}$ (menurunkan energi); pasangan orbital yang berada dalam ikatan berbeda, sehingga spinnya tidak berkorelasi, menyumbang $-\tfrac12J_{ij}$ (menaikkan energi). Rumus (12.4) diturunkan dalam kotak berikut; kita akan memakainya lagi untuk resonansi benzena di subbab 12.10.

::: {.dalam}
**Hamiltonian spin Dirac dan aturan pasangan**

Untuk dua elektron dalam orbital $a$ dan $b$, energi singlet dan triplet (dengan tumpang tindih diabaikan) adalah $Q + J$ dan $Q - J$. Keduanya dapat ditulis sebagai satu operator yang bekerja pada spin saja. Operator pertukaran spin $\hat P^\sigma_{12}$, yang menukar spin elektron 1 dan 2, bernilai $+1$ pada triplet (simetris) dan $-1$ pada singlet (antisimetris). Dari $\hat{\mathbf S}^2 = (\hat{\mathbf s}_1 + \hat{\mathbf s}_2)^2$ diperoleh $\hat{\mathbf s}_1\cdot\hat{\mathbf s}_2 = \tfrac12[S(S+1) - \tfrac32]$ (dalam satuan $\hbar^2$), yaitu $-\tfrac34$ untuk singlet dan $+\tfrac14$ untuk triplet. Maka $\hat P^\sigma_{12} = \tfrac12 + 2\hat{\mathbf s}_1\cdot\hat{\mathbf s}_2$, dan energi kedua keadaan sama dengan nilai eigen

$$
\hat H_\text{spin} = Q - J\left(\tfrac12 + 2\hat{\mathbf s}_1\cdot\hat{\mathbf s}_2\right) .
$$

Dirac menunjukkan bahwa untuk banyak elektron dalam orbital-orbital yang hampir ortogonal, satu elektron per orbital, energinya dapat dirumuskan dengan cara yang sama: $\hat H_\text{spin} = Q - \sum_{i<j}J_{ij}\left(\tfrac12 + 2\hat{\mathbf s}_i\cdot\hat{\mathbf s}_j\right)$. Dalam fungsi pasangan sempurna, pasangan yang berikatan adalah singlet, $\langle\hat{\mathbf s}_i\cdot\hat{\mathbf s}_j\rangle = -\tfrac34$, sehingga sumbangannya $-J_{ij}(\tfrac12 - \tfrac32) = +J_{ij}$. Untuk dua elektron dari pasangan yang berbeda, spin-spinnya tidak berkorelasi: $\langle\hat{\mathbf s}_i\cdot\hat{\mathbf s}_j\rangle = 0$, dan sumbangannya $-\tfrac12J_{ij}$. Itulah (12.4). Hamiltonian ini adalah model Heisenberg yang juga dipakai untuk magnetisme; di sini ia menjadi "mesin hitung" teori ikatan valensi.
:::

### Valensi dan elektron tak berpasangan

Menurut fungsi pasangan sempurna, sebuah atom dapat membentuk ikatan sebanyak elektron tak berpasangannya. Hidrogen ($1s^1$) bervalensi satu. Fluor ($2s^2 2p^5$) mempunyai satu elektron $p$ tak berpasangan dan bervalensi satu. Oksigen ($2p^4$, suku $^3P$) mempunyai dua, nitrogen ($2p^3$, $^4S$) tiga. Sampai di sini teori bekerja baik: HF, H₂O, dan NH₃.

Untuk karbon teori ini tersandung. Keadaan dasar $2s^2 2p^2$ ($^3P$) hanya mempunyai dua elektron tak berpasangan. Agar bervalensi empat, satu elektron $2s$ harus dipindahkan ke orbital $2p$ yang kosong:

$$
\text{C}\ (2s^2 2p^2,\ ^3P) \longrightarrow \text{C}\ (2s^1 2p^3,\ ^5S) , \qquad \Delta E = 4{,}18\ \text{eV} = 404\ \text{kJ/mol} . \qquad \text{(12.5)}
$$

Langkah ini disebut **promosi**. Promosi mahal, tetapi ia membuka dua ikatan tambahan, dan setiap ikatan C–H melepaskan sekitar 400 kJ/mol. Neraca energinya jelas menguntungkan (Contoh 12.1). Gagasan yang sama menjelaskan valensi berilium (dua, padahal $2s^2$ tidak mempunyai elektron tak berpasangan) dan boron (tiga, padahal $2s^2 2p^1$ hanya satu).

::: {.awas}
**Awas · Promosi adalah pembukuan, bukan peristiwa**

Molekul metana tidak terbentuk dengan cara atom karbon mula-mula tereksitasi ke $^5S$ lalu "menunggu" empat atom hidrogen. Promosi adalah cara menghitung energi: kita membayangkan jalan yang memudahkan perhitungan antara dua keadaan yang nyata (atom-atom terpisah dan molekul). Karena energi adalah fungsi keadaan, jalan khayalan itu sah untuk neraca energi. Lagi pula, "keadaan valensi" karbon dalam metana bukanlah keadaan $^5S$ (yang keempat spinnya sejajar), melainkan campuran spin yang lebih tinggi lagi energinya. Angka 404 kJ/mol adalah batas bawah biaya promosi.
:::

### Masalah arah

Promosi menyelesaikan masalah jumlah ikatan, tetapi menimbulkan masalah baru. Jika keempat elektron karbon berada dalam $2s$, $2p_x$, $2p_y$, dan $2p_z$, maka tiga ikatan C–H dibentuk oleh orbital $p$ yang saling tegak lurus, dan satu ikatan dibentuk oleh orbital $s$ yang tidak berarah. Ramalannya: tiga ikatan setara pada sudut 90° dan satu ikatan yang berbeda. Percobaan menunjukkan empat ikatan yang setara dengan sudut 109,47°, dan spektrum NMR, IR, dan Raman metana tidak memperlihatkan tanda sedikit pun bahwa satu ikatan berbeda dari yang lain.

Masalah yang sama tampak pada air. Bila oksigen memakai dua orbital $2p$ untuk berikatan dengan dua atom H, sudut H–O–H seharusnya 90°. Percobaan memberikan 104,5°. Pada H₂S (92,1°), H₂Se (90,6°), dan H₂Te (90,3°) ramalan 90° hampir tepat. Mengapa atom-atom periode 2 "menyimpang" dan atom-atom yang lebih berat tidak? Jawaban atas kedua teka-teki ini adalah **hibridisasi**, yang dibahas mulai subbab 12.2; perbedaan antara O dan S dibahas di subbab 12.6.

::: {.contoh}
**Contoh 12.1 · Apakah promosi karbon menguntungkan?**

Gunakan entalpi pembentukan gas pada 298 K: $\Delta_fH^\circ$(C) $= 716{,}68$ kJ/mol, $\Delta_fH^\circ$(H) $= 218{,}00$ kJ/mol, $\Delta_fH^\circ$(CH₄) $= -74{,}87$ kJ/mol, dan $\Delta_fH^\circ$(CH₂, triplet) $\approx 390{,}4$ kJ/mol. (a) Hitung entalpi atomisasi CH₄ dan CH₂. (b) Berapa energi yang dilepaskan bila CH₂ mengikat dua atom H lagi? Bandingkan dengan biaya promosi.

**Penyelesaian.** (a) $\Delta H_\text{at}(\text{CH}_4) = 716{,}68 + 4(218{,}00) - (-74{,}87) = 1663{,}5$ kJ/mol, atau 415,9 kJ/mol per ikatan. $\Delta H_\text{at}(\text{CH}_2) = 716{,}68 + 2(218{,}00) - 390{,}4 = 762{,}3$ kJ/mol, atau 381,1 kJ/mol per ikatan.

\(b) CH₂ + 2H → CH₄ melepaskan $1663{,}5 - 762{,}3 = 901{,}2$ kJ/mol. Biaya promosi $^3P \to {}^5S$ hanya 403,6 kJ/mol.

**Memahami hasil.** Dua ikatan tambahan melepaskan lebih dari dua kali biaya promosi, sehingga karbon bervalensi empat jauh lebih stabil. Perhatikan bahwa CH₂ (metilena) memang ada, tetapi hanya sebagai zat antara yang sangat reaktif. Di subbab 12.12 kita akan melihat mengapa keadaan dasar metilena adalah triplet, persis seperti yang diramalkan oleh dua elektron tak berpasangan karbon yang tersisa.
:::

::: {.contoh}
**Contoh 12.2 · Valensi atom periode 2**

Tentukan konfigurasi dan banyaknya elektron tak berpasangan dalam keadaan dasar Be, B, C, N, O, F, lalu ramalkan valensinya. Atom mana yang memerlukan promosi agar sesuai dengan valensi yang teramati (BeH₂, BF₃, CH₄)? Hitung biaya promosi Be ($2s^2 \to 2s2p$, $^3P$, 21 978 cm⁻¹) dan B ($2s^2 2p \to 2s2p^2$, $^4P$, sekitar 28 800 cm⁻¹) dalam eV dan kJ/mol.

**Penyelesaian.** Be $2s^2$: 0; B $2s^2 2p$: 1; C $2s^2 2p^2$: 2; N $2s^2 2p^3$: 3; O $2s^2 2p^4$: 2; F $2s^2 2p^5$: 1. Valensi teramati Be 2, B 3, C 4: ketiganya memerlukan promosi satu elektron $2s$ ke $2p$. Untuk Be, $21\,978 \times 1{,}2398 \times 10^{-4} = 2{,}72$ eV $= 263$ kJ/mol. Untuk B, $28\,800 \times 1{,}2398 \times 10^{-4} = 3{,}57$ eV $= 345$ kJ/mol.

**Memahami hasil.** Promosi hanya diperlukan oleh atom-atom di sebelah kiri karbon (dan karbon sendiri), yang orbital $2p$-nya masih kosong atau setengah kosong. Atom di sebelah kanan (N, O, F) sudah mempunyai cukup elektron tak berpasangan; pasangan $2s^2$ mereka tetap menjadi pasangan bebas. Pola ini sesuai dengan aturan oktet: setelah promosi dan pembentukan ikatan, Be, B, dan C mencapai 4, 6, dan 8 elektron valensi. Be dan B tetap kekurangan elektron, dan inilah akar sifat asam Lewis BeCl₂ dan BF₃.
:::

::: {.contoh}
**Contoh 12.3 · Energi pasangan sempurna air dengan orbital p murni**

Dalam model paling sederhana, oksigen memakai $2p_x$ dan $2p_y$ untuk berikatan dengan H₁ dan H₂. Tuliskan energi pasangan sempurna menurut (12.4), dengan menyimpan pertukaran O–H dan H···H. Mengapa model ini meramalkan sudut sedikit lebih besar dari 90°?

**Penyelesaian.** Pasangan berikatan: $(p_x, 1s_1)$ dan $(p_y, 1s_2)$. Pasangan tak berikatan yang bertetangga: $(p_x, 1s_2)$, $(p_y, 1s_1)$, dan $(1s_1, 1s_2)$. Maka

$$
E = Q + J_{x1} + J_{y2} - \tfrac12\left(J_{x2} + J_{y1} + J_{12}\right) .
$$

Pada sudut 90°, H₂ terletak di bidang simpul $p_x$ sehingga $J_{x2} = 0$, dan begitu pula $J_{y1} = 0$; pertukaran berikatan $J_{x1}$, $J_{y2}$ maksimum karena setiap H berada tepat pada sumbu orbital $p$-nya. Suku $-\tfrac12J_{12}$ bernilai positif (karena $J_{12} < 0$): dua atom H yang spinnya tidak berpasangan saling menolak.

**Memahami hasil.** Memperbesar sudut sedikit dari 90° mengurangi tolakan H···H (suku terakhir), dengan biaya kecil pada pertukaran berikatan. Sudut optimum model ini hanya beberapa derajat di atas 90°, jadi tolakan H···H saja tidak cukup untuk menjelaskan 104,5° pada H₂O. Untuk H₂S, ikatannya lebih panjang (134 pm, dibanding 96 pm pada H₂O) sehingga atom-atom H lebih berjauhan dan tolakannya lebih kecil: sudutnya mendekati 90°. Selisih yang besar pada air memerlukan pencampuran $2s$ ke dalam orbital ikatan, yaitu hibridisasi.
:::

::: {.contoh}
**Contoh 12.4 · Berapa banyak cara memasangkan elektron?**

Untuk $n$ elektron (satu per orbital) dengan spin total $S$, banyaknya fungsi spin yang bebas linear adalah

$$
f(n, S) = \frac{n!\,(2S + 1)}{\left(\tfrac n2 + S + 1\right)!\left(\tfrac n2 - S\right)!} .
$$

Hitung $f$ untuk singlet dengan $n = 2, 4, 6, 8$, dan triplet dengan $n = 6$. Apa artinya bagi benzena (enam elektron $\pi$) dan metana (delapan elektron valensi)?

**Penyelesaian.** Singlet: $f(2, 0) = 1$, $f(4, 0) = 2$, $f(6, 0) = 5$, $f(8, 0) = 14$. Triplet: $f(6, 1) = 6!\cdot3/(5!\,2!) = 9$.

**Memahami hasil.** Untuk H₂ hanya ada satu cara memasangkan dua elektron. Untuk enam elektron $\pi$ benzena ada lima struktur kovalen yang bebas: dua struktur Kekulé dan tiga struktur Dewar (subbab 12.10). Untuk delapan elektron valensi metana ada 14 cara, tetapi satu di antaranya, yaitu pasangan sempurna dengan setiap hibrida karbon dipasangkan dengan orbital $1s$ hidrogen di depannya, jauh lebih penting daripada yang lain. Teori ikatan valensi yang lengkap memakai semua struktur; struktur Lewis memilih yang paling penting.
:::

::: {.kuis}
**Kuis cepat 12.1**

Menurut fungsi pasangan sempurna, apakah tanda sumbangan pertukaran antara dua atom H yang tidak saling berikatan dalam CH₄ menaikkan atau menurunkan energi? Apakah valensi nitrogen memerlukan promosi?
:::

## 12.2 Orbital terarah dan gagasan hibridisasi

### Kombinasi linear orbital pada satu atom

Pada atom hidrogen, orbital $2s$, $2p_x$, $2p_y$, dan $2p_z$ berdegenerasi, sehingga sembarang kombinasi linearnya juga fungsi eigen dengan energi yang sama (subbab 4.2). Pada atom berelektron banyak, $2s$ lebih rendah daripada $2p$, tetapi di dalam molekul atom tidak lagi bebas: medan atom-atom tetangga mencampurkan $s$ dan $p$. Pertanyaan yang tepat bukan "apakah boleh mencampur $s$ dan $p$", melainkan "kombinasi mana yang paling cocok untuk melukiskan ikatan dalam molekul tertentu". Kombinasi linear orbital-orbital valensi **pada atom yang sama** itulah yang disebut **orbital hibrida** (L. Pauling dan J. C. Slater, 1931).

Untuk atom dengan orbital $s$ dan tiga orbital $p$ yang ortonormal, hibrida yang paling umum adalah

$$
h = c_s\,s + c_x\,p_x + c_y\,p_y + c_z\,p_z , \qquad c_s^2 + c_x^2 + c_y^2 + c_z^2 = 1 . \qquad \text{(12.6)}
$$

Syarat kedua adalah normalisasi: karena keempat orbital atom ortonormal, $\langle h|h\rangle = \sum c^2$.

### Orbital p dalam arah sembarang

Orbital $p$ riil berbentuk $p_x = x\,f(r)$, $p_y = y\,f(r)$, $p_z = z\,f(r)$, dengan $f(r)$ fungsi radial yang sama untuk ketiganya (subbab 7.7). Ambil vektor satuan $\mathbf n = (n_x, n_y, n_z)$. Kombinasi

$$
p_\mathbf n = n_xp_x + n_yp_y + n_zp_z = (\mathbf n\cdot\mathbf r)\,f(r) \qquad \text{(12.7)}
$$

adalah orbital $p$ yang persis sama bentuknya dengan $p_z$, hanya sumbunya menunjuk ke arah $\mathbf n$: $\mathbf n\cdot\mathbf r = r\cos\gamma$, dengan $\gamma$ sudut antara $\mathbf r$ dan $\mathbf n$. Tumpang tindih dua orbital $p$ berarah adalah

$$
\langle p_\mathbf n|p_\mathbf m\rangle = n_xm_x + n_ym_y + n_zm_z = \mathbf n\cdot\mathbf m = \cos\theta_{\mathbf{nm}} , \qquad \text{(12.8)}
$$

karena $\langle p_x|p_y\rangle = 0$ dan seterusnya. Hasil kecil ini adalah kunci seluruh bab: **tumpang tindih dua orbital $p$ pada atom yang sama sama dengan kosinus sudut antara sumbunya.**

Dengan (12.7), setiap hibrida (12.6) dapat ditulis ulang sebagai campuran satu orbital $s$ dan satu orbital $p$ yang menunjuk ke arah tertentu:

$$
h = \sqrt\alpha\,s + \sqrt{1 - \alpha}\,p_\mathbf n , \qquad \alpha = c_s^2 , \qquad \mathbf n = \frac{(c_x, c_y, c_z)}{\sqrt{1 - \alpha}} . \qquad \text{(12.9)}
$$

Bilangan $\alpha$ disebut **karakter $s$** (fraksi $s$) hibrida, dan $1 - \alpha$ karakter $p$-nya. Notasi kimia yang lazim adalah sp$^{\lambda^2}$, dengan

$$
h = \frac{s + \lambda\,p_\mathbf n}{\sqrt{1 + \lambda^2}} , \qquad \alpha = \frac{1}{1 + \lambda^2} , \qquad \lambda^2 = \frac{1 - \alpha}{\alpha} . \qquad \text{(12.10)}
$$

Jadi sp berarti $\lambda^2 = 1$ ($\alpha = \tfrac12$, 50% $s$), sp² berarti $\lambda^2 = 2$ (33,3% $s$), sp³ berarti $\lambda^2 = 3$ (25% $s$). Pangkat tidak harus bulat: hibrida dengan 20% $s$ adalah sp⁴, dengan 30% $s$ adalah sp$^{2,33}$.

### Mengapa hibrida lebih terarah

Bagian sudut orbital $s$ adalah $1/\sqrt{4\pi}$ ke semua arah; bagian sudut orbital $p_\mathbf n$ adalah $\sqrt{3/4\pi}\cos\gamma$. Dalam hibrida (12.9), kedua bagian itu saling menguatkan di sisi $\gamma = 0$ (tempat $\cos\gamma > 0$) dan saling melemahkan di sisi $\gamma = 180°$. Hasilnya adalah orbital dengan satu cuping besar yang menunjuk ke arah $\mathbf n$ dan cuping kecil di belakang (Gambar 12.1). Cuping besar itulah yang diarahkan ke atom tetangga.

![Gambar 12.1 Penampang orbital $2s$, $2p_z$, dan orbital hibrida dengan karakter $s$ berbeda pada bidang $xz$ (fungsi hidrogenik dengan $Z = 3{,}25$, sesuai muatan efektif karbon). Biru: positif; jingga: negatif; garis putus-putus: permukaan simpul. Makin besar karakter $s$, makin besar cuping depan relatif terhadap cuping belakang, dan makin terbuka permukaan simpulnya.](fig/c_hibrida.png){width=88%}

Pauling mengusulkan ukuran sederhana untuk "daya ikat" sebuah orbital: besar bagian sudutnya ke arah ikatan, dinormalisasi sehingga orbital $s$ bernilai 1. Dengan satuan ini, orbital $p$ bernilai $\sqrt3$ ke arah sumbunya, dan hibrida (12.9) bernilai

$$
f(\alpha) = \sqrt\alpha + \sqrt{3(1 - \alpha)} . \qquad \text{(12.11)}
$$

Turunannya terhadap $\alpha$ adalah $\dfrac{1}{2\sqrt\alpha} - \dfrac{\sqrt3}{2\sqrt{1 - \alpha}}$; nol bila $(1 - \alpha)/\alpha = 3$, yaitu $\alpha = \tfrac14$. Pada titik itu $f = \tfrac12 + \tfrac32 = 2$. **Hibrida sp³ adalah hibrida $s$–$p$ yang paling terarah.** Nilai-nilai lainnya: $s$ 1, $p$ 1,732, sp 1,932, sp² 1,992, sp³ 2,000.

### Tumpang tindih yang sebenarnya

Ukuran Pauling hanya melihat bagian sudut. Yang benar-benar menentukan kekuatan ikatan adalah integral tumpang tindih dengan orbital atom tetangga, yang bergantung juga pada bagian radial dan jarak antarinti. Karena tumpang tindih bersifat linear dalam orbital, tumpang tindih hibrida (12.9) dengan orbital $1s$ hidrogen yang terletak pada sumbu $\mathbf n$ adalah

$$
S(\alpha) = \sqrt\alpha\,S_s + \sqrt{1 - \alpha}\,S_{p\sigma} , \qquad \text{(12.12)}
$$

dengan $S_s = \langle s|1s_\text{H}\rangle$ dan $S_{p\sigma} = \langle p_\mathbf n|1s_\text{H}\rangle$. Dengan cara yang sama seperti pada $f(\alpha)$, maksimum $S(\alpha)$ terletak pada

$$
\alpha^* = \frac{S_s^2}{S_s^2 + S_{p\sigma}^2} , \qquad S_\text{maks} = \sqrt{S_s^2 + S_{p\sigma}^2} . \qquad \text{(12.13)}
$$

Untuk ikatan C–H, nilai $S_s$ dan $S_{p\sigma}$ dapat dihitung dengan orbital Slater (Contoh 12.6). Gambar 12.2 menunjukkan $S$ sebagai fungsi karakter $s$ untuk ikatan C–H dan C–C. Semua kurva berbentuk kubah: tumpang tindih naik tajam ketika sedikit $s$ dicampurkan ke $p$, mencapai maksimum di sekitar 50–60% $s$, lalu turun lagi.

![Gambar 12.2 Integral tumpang tindih hibrida karbon dengan orbital $1s$ hidrogen (C–H, 109 pm) dan antara dua hibrida karbon yang setara pada tiga jarak C–C, sebagai fungsi karakter $s$ (orbital Slater, $\zeta_\text{C} = 1{,}625$, $\zeta_\text{H} = 1{,}0$). Titik menandai maksimum. Makin pendek ikatan C–C, makin besar karakter $s$ yang memaksimumkan tumpang tindih.](fig/c_tumpang.png){width=78%}

### Karakter s adalah sumber daya yang terbatas

Jika satu ikatan C–H sendirian "menginginkan" sekitar 60% $s$, mengapa ikatan C–H metana hanya mendapat 25%? Karena atom karbon hanya mempunyai **satu** orbital $s$. Bila empat hibrida $h_i = \sqrt{\alpha_i}\,s + \sqrt{1 - \alpha_i}\,p_i$ dibentuk dari satu $s$ dan tiga $p$, transformasi dari $\{s, p_x, p_y, p_z\}$ ke $\{h_1, h_2, h_3, h_4\}$ harus mempertahankan ortonormalitas, sehingga matriks koefisiennya ortogonal (subbab 2.7). Kolom-kolom matriks ortogonal juga ternormalisasi; kolom $s$ memberikan

$$
\sum_i\alpha_i = 1 , \qquad \sum_i(1 - \alpha_i) = 3 . \qquad \text{(12.14)}
$$

Satu orbital $s$ dibagi habis di antara keempat hibrida; demikian pula ketiga orbital $p$. Ini adalah **kekekalan orbital**: hibridisasi tidak menciptakan atau menghilangkan orbital, hanya membagi ulang.

Sekarang kita dapat bertanya: bagaimana karakter $s$ harus dibagi agar **jumlah** tumpang tindih keempat ikatan C–H maksimum? Kita memaksimumkan $\sum_i S(\alpha_i)$ dengan kendala $\sum_i\alpha_i = 1$. Dengan pengali Lagrange $\mu$:

$$
\frac{\partial}{\partial\alpha_i}\left[\sum_k S(\alpha_k) - \mu\sum_k\alpha_k\right] = \frac{S_s}{2\sqrt{\alpha_i}} - \frac{S_{p\sigma}}{2\sqrt{1 - \alpha_i}} - \mu = 0 .
$$

Persamaan ini sama untuk setiap $i$, dan ruas kirinya fungsi monoton dari $\alpha_i$; jadi semua $\alpha_i$ sama, $\alpha_i = \tfrac14$. **Untuk empat ikatan yang sejenis, tumpang tindih total maksimum dicapai oleh empat hibrida sp³ yang setara.** Kesetaraan ikatan metana bukan asumsi, melainkan hasil optimasi.

### Syarat ortogonalitas dan sudut antarhibrida

Hibrida-hibrida pada atom yang sama harus saling ortogonal. Alasannya fisis, bukan sekadar kerapian matematika. Bila dua hibrida pada atom yang sama tumpang tindih, dua pasangan elektron dalam ikatan yang berbeda akan menempati daerah ruang yang sama; asas Pauli kemudian memaksa fungsi gelombang menaikkan energi kinetiknya (tolakan Pauli). Hibrida yang ortogonal adalah cara paling murah untuk menempatkan beberapa pasangan elektron di sekitar satu atom.

Ambil dua hibrida $h_i = \sqrt{\alpha_i}\,s + \sqrt{1 - \alpha_i}\,p_{\mathbf n_i}$ dan $h_j$ dengan arah $\mathbf n_j$. Dengan (12.8),

$$
\langle h_i|h_j\rangle = \sqrt{\alpha_i\alpha_j} + \sqrt{(1 - \alpha_i)(1 - \alpha_j)}\cos\theta_{ij} = 0 , \qquad \text{(12.15)}
$$

dengan $\theta_{ij}$ sudut antara $\mathbf n_i$ dan $\mathbf n_j$. Maka

$$
\boxed{\ \cos\theta_{ij} = -\left[\frac{\alpha_i\alpha_j}{(1 - \alpha_i)(1 - \alpha_j)}\right]^{1/2} = -\frac{1}{\lambda_i\lambda_j}\ } \qquad \text{(12.16)}
$$

Bentuk kedua, $1 + \lambda_i\lambda_j\cos\theta_{ij} = 0$, dikenal sebagai **teorema Coulson**. Untuk dua hibrida yang setara ($\alpha_i = \alpha_j = \alpha$):

$$
\cos\theta = -\frac{\alpha}{1 - \alpha} = -\frac{1}{\lambda^2} . \qquad \text{(12.17)}
$$

Persamaan sederhana ini memuat seluruh geometri hibridisasi $s$–$p$. Gambar 12.3 melukiskannya.

![Gambar 12.3 Sudut antara dua hibrida setara terhadap karakter $s$-nya, menurut (12.17). Titik bulat: hibrida baku sp³, sp², sp. Titik persegi: karakter $s$ hibrida ikatan yang dibaca dari sudut ikatan teramati H₂O, NH₃, PH₃, dan H₂S. Hibrida yang hanya memuat $s$ dan $p$ tidak pernah membentuk sudut kurang dari 90°.](fig/c_sudut.png){width=72%}

Tiga akibat langsung dari (12.16):

1. **Sudut antarhibrida $s$–$p$ selalu ≥ 90°.** Ruas kanan (12.16) tidak pernah positif. Hibrida yang membentuk sudut lancip mustahil; inilah sebabnya cincin beranggota tiga dan empat mempunyai "ikatan bengkok" (subbab 12.5).
2. **Makin besar karakter $s$, makin besar sudutnya.** 25% → 109,47°, 33,3% → 120°, 50% → 180°.
3. **Sudut dapat dibaca menjadi karakter $s$**, dan sebaliknya. Dari sudut H–X–H yang terukur, kita dapat menghitung susunan hibrida (subbab 12.6).

::: {.inti}
**Tiga syarat hibridisasi $s$–$p$**

1. Normalisasi: $\alpha_i + (1 - \alpha_i) = 1$ untuk setiap hibrida.
2. Kekekalan orbital: $\sum_i\alpha_i = 1$ (satu orbital $s$), $\sum_i(1 - \alpha_i) =$ banyaknya orbital $p$ yang dipakai.
3. Ortogonalitas: $1 + \lambda_i\lambda_j\cos\theta_{ij} = 0$ untuk setiap pasangan.

Dari ketiga syarat ini sudut-sudut 180°, 120°, dan 109,47° keluar tanpa asumsi tambahan.
:::

::: {.awas}
**Awas · Hibridisasi tidak menyebabkan geometri**

Kalimat "metana tetrahedral karena karbonnya terhibridisasi sp³" membalik sebab dan akibat. Geometri molekul ditentukan oleh energi total yang dihitung dari persamaan Schrödinger untuk seluruh elektron dan inti. Hibrida adalah cara **melukiskan** distribusi elektron pada geometri itu dengan orbital-orbital lokal. Kalimat yang tepat: "karena metana tetrahedral, orbital lokal karbon yang paling sesuai adalah empat hibrida sp³". Di subbab 12.11 kita akan melihat argumen yang benar-benar meramalkan geometri (VSEPR dan dasar kuantumnya), dan di subbab 12.13 kita akan melihat bahwa deskripsi hibrida bukan satu-satunya deskripsi yang sah.
:::

::: {.contoh}
**Contoh 12.5 · "Kekuatan ikatan" Pauling**

Hitung $f(\alpha) = \sqrt\alpha + \sqrt{3(1 - \alpha)}$ untuk $s$, sp, sp², sp³, dan $p$, dan tunjukkan bahwa maksimumnya terjadi pada sp³. Berapa perbandingan cuping depan terhadap cuping belakang (dalam bagian sudut) untuk sp, sp², dan sp³?

**Penyelesaian.** $s$: 1. sp: $0{,}7071 + 1{,}2247 = 1{,}932$. sp²: $0{,}5774 + 1{,}4142 = 1{,}992$. sp³: $0{,}5 + 1{,}5 = 2{,}000$. $p$: $\sqrt3 = 1{,}732$. Maksimum terjadi pada $\alpha = \tfrac14$, seperti diturunkan di atas.

Ke arah belakang ($\gamma = 180°$) amplitudo sudutnya $|\sqrt\alpha - \sqrt{3(1 - \alpha)}|$. Perbandingan depan/belakang: sp $1{,}932/0{,}518 = 3{,}73$; sp² $1{,}992/0{,}837 = 2{,}38$; sp³ $2{,}000/1{,}000 = 2{,}00$.

**Memahami hasil.** Perbedaan "kekuatan" sp, sp², dan sp³ menurut ukuran sudut sangat kecil (kurang dari 4%), jauh lebih kecil daripada perbedaan kekuatan ikatan C–H yang teramati (subbab 12.7). Ukuran Pauling hanya kasar; yang menentukan adalah tumpang tindih sebenarnya dan energi orbital $s$ yang lebih rendah. Menariknya, hibrida sp justru paling "berat sebelah": cuping depannya hampir empat kali cuping belakang.
:::

::: {.contoh}
**Contoh 12.6 · Tumpang tindih C–H dengan orbital Slater**

Dengan orbital Slater $2s$ dan $2p$ karbon ($\zeta = 1{,}625$) dan $1s$ hidrogen ($\zeta = 1{,}0$) pada jarak 109 pm, integral numeriknya $S_s = 0{,}570$ dan $S_{p\sigma} = 0{,}466$. (a) Hitung tumpang tindih hibrida sp³, sp², sp, dan $p$ dengan $1s_\text{H}$. (b) Pada karakter $s$ berapa tumpang tindih maksimum, dan berapa nilainya?

**Penyelesaian.** (a) Dengan (12.12): $p$: 0,466. sp³: $0{,}5(0{,}570) + 0{,}866(0{,}466) = 0{,}689$. sp²: $0{,}577(0{,}570) + 0{,}816(0{,}466) = 0{,}710$. sp: $0{,}707(0{,}570) + 0{,}707(0{,}466) = 0{,}733$.

\(b) Dengan (12.13): $\alpha^* = 0{,}570^2/(0{,}570^2 + 0{,}466^2) = 0{,}600$ dan $S_\text{maks} = 0{,}736$.

**Memahami hasil.** Mencampurkan 25% $s$ ke dalam orbital $p$ menaikkan tumpang tindih dari 0,47 menjadi 0,69, hampir 50%. Inilah keuntungan utama hibridisasi. Bila satu ikatan C–H boleh memilih sendiri, ia akan mengambil 60% $s$; dalam metana empat ikatan harus berbagi satu orbital $s$, dan pembagian yang memaksimumkan jumlah tumpang tindih adalah pembagian rata. Perhatikan juga bahwa orbital Slater $2s$ tidak mempunyai simpul radial, sehingga angka-angka ini hanya ilustrasi; perhitungan dengan orbital yang lebih baik memberikan pola yang sama.
:::

::: {.contoh}
**Contoh 12.7 · Membaca sebuah hibrida**

Sebuah hibrida karbon adalah $h = 0{,}55\,s + 0{,}48\,p_x + 0{,}48\,p_y + 0{,}48\,p_z$. (a) Apakah ia ternormalisasi? (b) Tentukan karakter $s$, notasi sp$^{\lambda^2}$, dan arah cuping besarnya. (c) Berapa sudut antara $h$ dan hibrida setara yang menunjuk ke arah $(1, -1, -1)$?

**Penyelesaian.** (a) $0{,}55^2 + 3(0{,}48)^2 = 0{,}3025 + 0{,}6912 = 0{,}9937$. Hampir, tetapi tidak tepat ternormalisasi; bagi dengan $\sqrt{0{,}9937} = 0{,}9968$: $c_s = 0{,}552$, $c_p = 0{,}482$.

\(b) $\alpha = 0{,}552^2 = 0{,}304$, sehingga $\lambda^2 = 0{,}696/0{,}304 = 2{,}29$: hibrida sp$^{2,3}$ dengan 30% $s$. Arahnya $(1, 1, 1)/\sqrt3$.

\(c) Sudut antara $(1, 1, 1)$ dan $(1, -1, -1)$ adalah $\arccos(-\tfrac13) = 109{,}47°$. Tumpang tindih kedua hibrida: $\alpha + (1 - \alpha)\cos\theta = 0{,}304 + 0{,}696(-\tfrac13) = 0{,}072 \ne 0$.

**Memahami hasil.** Dua hibrida dengan 30% $s$ tidak dapat saling ortogonal pada sudut tetrahedral; menurut (12.17) mereka memerlukan $\cos\theta = -0{,}304/0{,}696$, yaitu 116,0°. Lagi pula, empat hibrida dengan 30% $s$ akan memerlukan $4 \times 0{,}304 = 1{,}22$ orbital $s$, lebih dari yang tersedia. Hibrida seperti ini hanya dapat muncul bila hibrida-hibrida lainnya pada atom yang sama mempunyai karakter $s$ lebih kecil (subbab 12.6).
:::

::: {.contoh}
**Contoh 12.8 · Kekekalan orbital**

(a) Dapatkah karbon membentuk empat hibrida yang masing-masing 30% $s$? (b) Sebuah atom membentuk dua hibrida ikatan setara dengan sudut 104,5° di antara keduanya. Berapa karakter $s$ yang tersisa untuk orbital-orbital lain? (c) Bila sisa itu dibagi rata ke dua pasangan bebas setara, berapa sudut di antara keduanya?

**Penyelesaian.** (a) Tidak: $\sum\alpha_i = 1{,}2 > 1$. (b) Dari (12.17), $\alpha = -\cos\theta/(1 - \cos\theta) = 0{,}2504/1{,}2504 = 0{,}200$. Kedua ikatan memakai 0,400; sisanya 0,600. (c) Setiap pasangan bebas mendapat 0,300, dan sudutnya $\arccos(-0{,}300/0{,}700) = 115{,}4°$.

**Memahami hasil.** Inilah air (subbab 12.6): ikatan O–H mendapat sedikit karakter $s$, dan pasangan bebas mendapat banyak. Sudut 115,4° antara kedua pasangan bebas lebih besar daripada sudut 104,5° antara kedua ikatan, sesuai dengan gagasan VSEPR bahwa pasangan bebas "lebih gemuk" (subbab 12.11). Perlu dicatat bahwa pembagian rata ini bukan satu-satunya pilihan; subbab 12.6 dan 12.13 membahas alternatifnya.
:::

::: {.kuis}
**Kuis cepat 12.2**

Dua hibrida $s$–$p$ setara pada atom yang sama membentuk sudut 100°. Berapa karakter $s$-nya? Mungkinkah dua hibrida $s$–$p$ membentuk sudut 80°?
:::
