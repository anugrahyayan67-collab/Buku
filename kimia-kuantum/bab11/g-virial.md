## 11.15 Mengapa ikatan terbentuk: teorema virial

### Pertanyaan yang tampak sederhana

"Ikatan terbentuk karena elektron di antara inti ditarik oleh kedua inti sekaligus" adalah penjelasan yang paling sering dijumpai, dan kita pun memakainya di subbab 11.5. Tetapi penjelasan ini tidak lengkap. Elektron yang ditarik dua inti bergerak dalam potensial yang lebih dalam, tetapi agar dapat menumpuk di daerah antarinti yang sempit, fungsi gelombangnya harus melengkung lebih tajam, yang berarti energi kinetik lebih besar. Komponen energi mana yang sebenarnya turun ketika ikatan terbentuk, kinetik atau potensial? Jawabannya diberikan oleh sebuah teorema yang sangat umum, dan jawaban itu ternyata lebih halus daripada yang diduga.

### Teorema virial untuk atom

Tinjau atom dengan elektron-elektron yang semuanya berinteraksi melalui gaya Coulomb. Bila $\psi$ adalah fungsi gelombang eksak, ubah skalanya: $\psi_\eta(\mathbf r_1, \ldots) = \eta^{3N/2}\psi(\eta\mathbf r_1, \ldots)$, dengan faktor $\eta^{3N/2}$ menjaga normalisasi. Mengganti variabel integrasi menunjukkan bahwa energi kinetik (dua turunan) berubah sebagai $\eta^2$, sedangkan energi potensial Coulomb (berbanding $1/r$) berubah sebagai $\eta$:

$$
E(\eta) = \eta^2\langle\hat T\rangle + \eta\langle\hat V\rangle .
$$

Fungsi eksak memberi energi terendah di antara semua fungsi uji, termasuk semua $\psi_\eta$, sehingga $dE/d\eta = 0$ di $\eta = 1$: $2\langle\hat T\rangle + \langle\hat V\rangle = 0$. Jadi untuk atom

$$
\langle\hat T\rangle = -E, \qquad \langle\hat V\rangle = 2E . \qquad \text{(11.36)}
$$

Untuk atom H, $E = -\tfrac12$, $\langle T\rangle = \tfrac12$, dan $\langle V\rangle = -1$ hartree, sesuai dengan perhitungan langsung (subbab 7.9).

### Teorema virial untuk molekul

Untuk molekul dalam pendekatan Born–Oppenheimer, ada kerumitan: energi bergantung pada $R$, dan penskalaan koordinat elektron dengan $\eta$ juga harus menskala jarak antarinti agar semua suku Coulomb berubah dengan cara yang sama. Energi Hamiltonian elektronik pada jarak $R$ dengan fungsi yang diskala adalah $\eta^2T + \eta V(\eta R)$, dengan $T$ dan $V$ dihitung untuk fungsi tak terskala pada jarak $\eta R$. Syarat minimum dan sedikit aljabar (kotak *Lebih dalam*) memberi teorema virial molekul (Slater, 1933):

$$
2\langle\hat T\rangle + \langle\hat V\rangle = -R\frac{dE}{dR} , \qquad \text{(11.37)}
$$

dengan $\hat V$ mencakup semua energi potensial (termasuk tolakan antarinti) dan $E = \langle\hat T\rangle + \langle\hat V\rangle$ energi total pada jarak $R$. Bila dipecahkan untuk $T$ dan $V$:

$$
\langle\hat T\rangle = -E - R\frac{dE}{dR}, \qquad \langle\hat V\rangle = 2E + R\frac{dE}{dR} . \qquad \text{(11.38)}
$$

Keistimewaan (11.38): dari kurva $E(R)$ saja, kita dapat mengetahui bagaimana energi kinetik dan potensial berubah sepanjang pembentukan ikatan. Di jarak setimbang dan di jarak tak hingga, $dE/dR = 0$, sehingga (11.36) berlaku lagi.

::: {.dalam}
**Lebih dalam · Menurunkan teorema virial molekul**

Tulis $E(R) = T(R) + V(R)$ untuk fungsi gelombang eksak pada jarak $R$. Untuk fungsi yang diskala $\psi_\eta$ pada jarak $R$, ganti variabel $\mathbf r' = \eta\mathbf r$. Energi kinetik menjadi $\eta^2T(\eta R)$. Energi potensial Coulomb, karena semua jarak (elektron–elektron, elektron–inti, inti–inti) dikalikan $\eta$ secara serempak bila $R$ juga dikalikan $\eta$, menjadi $\eta V(\eta R)$. Jadi

$$
W(\eta) = \eta^2T(\eta R) + \eta V(\eta R)
$$

adalah energi fungsi uji $\psi_\eta$ untuk Hamiltonian pada jarak $R$. Fungsi eksak ($\eta = 1$) meminimumkan $W$, sehingga $dW/d\eta|_{\eta = 1} = 0$:

$$
2T + V + R\left(\frac{dT}{dR} + \frac{dV}{dR}\right) = 0 \quad\Longrightarrow\quad 2T + V = -R\frac{dE}{dR} .
$$

Penurunan ini hanya memakai dua hal: semua gaya bersifat Coulomb (sebanding $1/r$), dan fungsi gelombang optimal terhadap penskalaan. Fungsi uji pendekatan yang mempunyai parameter skala bebas (seperti $\zeta$ dalam orbital Slater) yang dioptimalkan juga memenuhi teorema ini secara tepat.
:::

### Apa yang terjadi selama pembentukan ikatan

Dengan kurva eksak H₂⁺ dan (11.38), diperoleh perubahan energi kinetik dan potensial relatif terhadap H + H⁺ ($\Delta T = T - 0{,}5$, $\Delta V = V + 1$) untuk setiap jarak (Gambar 11.13):

| $R$ (bohr) | $\Delta E$ | $\Delta T$ | $\Delta V$ |
|---|---|---|---|
| 8,0 | $-0{,}003$ | $-0{,}013$ | $+0{,}011$ |
| 6,0 | $-0{,}012$ | $-0{,}041$ | $+0{,}029$ |
| 4,0 | $-0{,}046$ | $-0{,}062$ | $+0{,}016$ |
| 3,0 | $-0{,}078$ | $-0{,}025$ | $-0{,}052$ |
| 2,0 | $-0{,}103$ | $+0{,}102$ | $-0{,}205$ |
| 1,0 | $+0{,}048$ | $+0{,}473$ | $-0{,}425$ |

(Semua dalam hartree.) Ketika atom-atom mulai mendekat dari jauh, energi **kinetik** turun sementara energi potensial sedikit naik: elektron yang dapat menyebar ke dua inti mempunyai fungsi gelombang yang lebih landai, persis seperti efek delokalisasi di Contoh 11.24. Penurunan energi kinetik inilah yang pertama-tama membuat atom-atom saling menarik. Di sekitar $R \approx 3$ bohr pola berbalik: awan elektron menyusut ke arah inti (seperti $\zeta$ yang naik di Contoh 11.18), energi potensial turun tajam, dan energi kinetik naik. Di jarak setimbang, hasil akhirnya sesuai (11.36): $\Delta T = -\Delta E = +0{,}103$ dan $\Delta V = 2\Delta E = -0{,}205$ hartree.

![Gambar 11.13 Teorema virial untuk H₂⁺ eksak. Perubahan energi total $\Delta E$, kinetik $\Delta T$, dan potensial $\Delta V$ relatif terhadap H + H⁺, dihitung dari kurva $E(R)$ dengan (11.38). Pada jarak besar ikatan dimulai oleh penurunan energi kinetik; di jarak setimbang energi kinetik justru naik dan energi potensial turun dua kali penurunan energi total.](fig/c_virial.png){width=82%}

Dua cerita yang tampak bertentangan tentang ikatan kimia, "ikatan menurunkan energi potensial" dan "ikatan menurunkan energi kinetik", karena itu sama-sama benar, pada tahap yang berbeda. Analisis Klaus Ruedenberg (1962) menafsirkannya demikian: penyebab utama ikatan kovalen adalah penurunan energi kinetik akibat interferensi konstruktif (delokalisasi) orbital atom; penyusutan orbital yang menyertainya mengubah keuntungan kinetik itu menjadi keuntungan potensial, sehingga di jarak setimbang teorema virial terpenuhi. Kimiawan masih memperdebatkan bobot relatif kedua mekanisme, tetapi teorema virial menjamin bahwa setiap cerita yang hanya menyebut "potensial" atau hanya "kinetik" tidak lengkap.

::: {.contoh}
**Contoh 11.72 · Energi kinetik dan potensial di jarak setimbang**

Energi eksak H₂⁺ di $R_e$ adalah $-0{,}60263$ hartree, dan energi eksak H₂ di $R_e$ adalah $-1{,}17447$ hartree. Hitung $\langle T\rangle$ dan $\langle V\rangle$ untuk keduanya, serta perubahannya relatif terhadap atom-atom terpisah.

**Penyelesaian.** Di $R_e$, $dE/dR = 0$. H₂⁺: $T = 0{,}60263$, $V = -1{,}20527$; relatif terhadap H + H⁺ ($T = 0{,}5$, $V = -1$): $\Delta T = +0{,}1026$, $\Delta V = -0{,}2053$ hartree. H₂: $T = 1{,}17447$, $V = -2{,}34894$; relatif terhadap 2H ($T = 1$, $V = -2$): $\Delta T = +0{,}1745$, $\Delta V = -0{,}3489$ hartree.

**Memahami hasil.** Dalam kedua molekul, di jarak setimbang energi kinetik elektron *lebih besar* daripada di atom terpisah, dan energi potensial turun dua kali lebih banyak daripada energi total. Ini berlaku untuk setiap molekul yang terikat: molekul selalu "lebih rapat dan lebih cepat" daripada atom-atom penyusunnya pada jarak setimbang.
:::

::: {.contoh}
**Contoh 11.73 · Fungsi uji yang melanggar teorema virial**

Untuk LCAO H₂⁺ dengan $\zeta = 1$ di minimumnya ($R = 2{,}493$ bohr), $T = 0{,}3827$ dan $V = -0{,}9475$ hartree. Dengan $\zeta = 1{,}238$ dioptimalkan ($R = 2{,}003$ bohr), $T = 0{,}5865$ dan $V = -1{,}1730$ hartree. Hitung $-V/T$ untuk keduanya.

**Penyelesaian.** $\zeta = 1$: $-V/T = 0{,}9475/0{,}3827 = 2{,}48$. $\zeta$ optimal: $1{,}1730/0{,}5865 = 2{,}000$.

**Memahami hasil.** Fungsi dengan $\zeta = 1$ melanggar teorema virial jauh sekali: energi kinetiknya bahkan *lebih kecil* daripada atom H (0,38 < 0,50), berlawanan dengan Contoh 11.72. Fungsi itu menangkap efek delokalisasi tetapi tidak menangkap penyusutan orbital. Setelah $\zeta$ dioptimalkan, perbandingan $-V/T$ menjadi tepat 2, seperti dijanjikan kotak *Lebih dalam*. Pemeriksaan $-V/T = 2$ adalah uji kualitas sederhana untuk fungsi gelombang pendekatan, dan program kimia kuantum sering mencetak "rasio virial" untuk tujuan ini.
:::

::: {.contoh}
**Contoh 11.74 · Gaya dari energi kinetik dan potensial**

Dari tabel di atas, pada $R = 3{,}0$ bohr: $E = -0{,}57756$, $T = 0{,}47488$, $V = -1{,}05244$ hartree. Gunakan (11.37) untuk menghitung $dE/dR$ dan gaya antarinti. Apakah inti saling menarik atau menolak di jarak ini?

**Penyelesaian.** $2T + V = 0{,}94976 - 1{,}05244 = -0{,}10268$, sehingga $dE/dR = 0{,}10268/3{,}0 = 0{,}0342$ hartree/bohr. Gaya $F = -dE/dR = -0{,}0342$ hartree/bohr (tanda negatif: berlawanan arah pertambahan $R$), yaitu tarikan sebesar $0{,}0342 \times 82{,}39 = 2{,}8$ nN.

**Memahami hasil.** Teorema virial memberi cara lain menghitung gaya dari komponen energi: bila $2T + V < 0$, inti saling menarik; bila $> 0$, menolak; bila $= 0$, setimbang. Gaya 2,8 nN, meskipun kecil secara makroskopis, sangat besar untuk sepasang atom: sebanding dengan gaya yang diukur mikroskop gaya atom ketika menarik satu molekul sampai ikatannya putus.
:::

::: {.dalam}
**Lebih dalam · Tiga tahap pembentukan ikatan menurut Ruedenberg**

Ruedenberg menguraikan pembentukan ikatan H₂⁺ dan H₂ menjadi langkah-langkah yang masing-masing dapat dihitung. (1) **Promosi**: orbital atom menyusut (eksponen $\zeta$ naik), yang sendirian menaikkan energi atom karena orbitalnya tidak lagi optimal; energi kinetik naik, energi potensial turun, tetapi totalnya naik. (2) **Interferensi** (pembagian elektron): orbital-orbital yang sudah menyusut digabungkan; interferensi konstruktif memindahkan kerapatan dari daerah dekat inti ke daerah antarinti dan menurunkan energi kinetik secara besar, sementara energi potensial sedikit naik karena elektron meninggalkan daerah dekat inti yang potensialnya paling dalam. (3) **Kuasi-klasik**: tarikan elektrostatik antara awan atom dan inti tetangga, yang hampir dibatalkan tolakan antarinti (seperti $J + 1/R$ di Contoh 11.16). Menurut analisis ini, keuntungan energi bersih datang terutama dari langkah (2), penurunan energi kinetik oleh interferensi, sedangkan langkah (1) diperlukan agar keuntungan itu dapat dimanfaatkan sepenuhnya dan agar teorema virial terpenuhi. Analisis serupa untuk ikatan antaratom yang lebih berat, seperti dalam B₂ dan C₂, memberi gambaran yang sama, meskipun peran tolakan Pauli kulit dalam membuat neraca lebih rumit.
:::

::: {.contoh}
**Contoh 11.75 · Rasio virial sebagai uji fungsi gelombang H₂**

Untuk keempat fungsi H₂ di subbab 11.12, energi kinetik dan potensial di minimum masing-masing adalah (hartree): OM $\zeta = 1$: $T = 0{,}797$, $V = -1{,}896$; OM $\zeta$ optimal: $T = 1{,}128$, $V = -2{,}256$; Heitler–London $\zeta = 1$: $T = 0{,}838$, $V = -1{,}954$; Wang: $T = 1{,}139$, $V = -2{,}278$. Hitung $-V/T$ dan tafsirkan.

**Penyelesaian.** OM $\zeta = 1$: 2,38; OM optimal: 2,000; Heitler–London: 2,33; Wang: 2,000.

**Memahami hasil.** Fungsi dengan $\zeta = 1$ mempunyai energi kinetik jauh di bawah nilai eksak (1,174 hartree): elektron dalam orbital atom H yang tidak berubah bergerak "terlalu lambat" untuk molekul. Setelah $\zeta$ dioptimalkan, rasio menjadi tepat 2, tetapi itu tidak berarti energinya tepat: fungsi OM dan Wang yang optimal masih meleset 1,3 dan 1,0 eV. Teorema virial adalah syarat perlu, bukan syarat cukup. Perhitungan $\zeta$ optimal H₂⁺ untuk banyak $R$ menunjukkan pola yang sejalan dengan Gambar 11.13: $\zeta = 0{,}995$ pada 6 bohr (orbital sedikit *mengembang*, energi kinetik turun), 1,03 pada 4 bohr, 1,24 pada 2 bohr, dan 1,54 pada 1 bohr (orbital menyusut kuat, energi kinetik naik).
:::

::: {.contoh}
**Contoh 11.76 · Teorema virial dalam perhitungan nyata**

Untuk H₂ dengan RHF/cc-pVTZ (PySCF), energi kinetik dan potensial pada dua jarak adalah: $R = 1{,}4$ bohr: $T = 1{,}12312$, $V = -2{,}25608$ hartree; $R = 2{,}0$ bohr: $T = 0{,}88544$, $V = -1{,}97652$ hartree. Turunan energi yang dihitung secara numerik: $-R\,dE/dR = -0{,}00669$ (pada 1,4 bohr) dan $-0{,}20439$ hartree (pada 2,0 bohr). Periksa (11.37).

**Penyelesaian.** $R = 1{,}4$: $2T + V = 2{,}24624 - 2{,}25608 = -0{,}00984$, dibandingkan $-0{,}00669$. $R = 2{,}0$: $2T + V = 1{,}77088 - 1{,}97652 = -0{,}20564$, dibandingkan $-0{,}20439$.

**Memahami hasil.** Kedua ruas cocok sampai sekitar 0,003 hartree, tetapi tidak tepat. Sebabnya: teorema virial berlaku tepat hanya bila fungsi gelombang optimal terhadap penskalaan, dan basis Gauss yang tetap (eksponennya tidak dioptimalkan untuk setiap molekul) tidak sepenuhnya memiliki kebebasan itu. Dengan basis yang makin lengkap, selisihnya mengecil. Program kimia kuantum mencetak "rasio virial" $-V/T$; pada geometri setimbang yang dioptimalkan dengan basis yang baik nilainya sangat dekat ke 2 (di sini 2,009 pada 1,4 bohr, dekat minimum RHF 1,388 bohr), dan simpangan besar menandakan basis yang tidak seimbang.
:::

::: {.kuis}
**Kuis cepat 11.15**

\(a) Untuk atom He, $E = -2{,}9037$ hartree. Berapa $\langle T\rangle$ dan $\langle V\rangle$? (b) Pada jarak besar ($R > 4$ bohr), komponen energi mana yang menyebabkan tarikan dalam H₂⁺? (c) Mengapa LCAO dengan $\zeta = 1$ tidak memenuhi teorema virial?
:::

## 11.16 Teorema Hellmann–Feynman dan gaya pada inti

### Turunan energi terhadap parameter

Hamiltonian molekul bergantung pada banyak parameter: posisi inti, muatan inti, medan listrik luar. Bagaimana energi berubah bila salah satu parameter $\lambda$ diubah? Bila $\psi$ adalah fungsi eigen ternormalisasi $\hat H(\lambda)$ dengan nilai eigen $E(\lambda)$, maka

$$
\frac{dE}{d\lambda} = \left\langle\psi\left|\frac{\partial\hat H}{\partial\lambda}\right|\psi\right\rangle . \qquad \text{(11.39)}
$$

Inilah **teorema Hellmann–Feynman** (Hans Hellmann, 1937; Richard Feynman, 1939). Buktinya singkat. Turunkan $E = \langle\psi|\hat H|\psi\rangle$:

$$
\frac{dE}{d\lambda} = \left\langle\frac{\partial\psi}{\partial\lambda}\right|\hat H|\psi\rangle + \langle\psi|\frac{\partial\hat H}{\partial\lambda}|\psi\rangle + \langle\psi|\hat H\left|\frac{\partial\psi}{\partial\lambda}\right\rangle .
$$

Karena $\hat H\psi = E\psi$ dan $\hat H$ Hermitian, suku pertama dan ketiga menjadi $E[\langle\partial_\lambda\psi|\psi\rangle + \langle\psi|\partial_\lambda\psi\rangle] = E\,\frac{d}{d\lambda}\langle\psi|\psi\rangle = 0$, karena normalisasi tetap 1. Tersisa suku tengah. Yang luar biasa: perubahan fungsi gelombang tidak perlu dihitung. Turunan energi cukup dihitung sebagai nilai harap turunan operator, dengan fungsi gelombang yang sudah ada.

### Teorema elektrostatik: gaya pada inti

Ambil $\lambda$ sebagai koordinat inti $A$, misalnya $X_A$. Dalam Hamiltonian elektronik, hanya suku tarikan elektron–inti dan tolakan antarinti yang bergantung pada posisi inti. Gaya pada inti, $\mathbf F_A = -\nabla_AE$, menurut (11.39) adalah

$$
\mathbf F_A = Z_A\int\rho(\mathbf r)\frac{\mathbf r - \mathbf R_A}{|\mathbf r - \mathbf R_A|^3}\,d\tau + \sum_{B \ne A}Z_AZ_B\frac{\mathbf R_A - \mathbf R_B}{|\mathbf R_A - \mathbf R_B|^3} \qquad \text{(11.40)}
$$

(dalam satuan atom). Suku pertama adalah tarikan Coulomb klasik oleh awan elektron dengan kerapatan $\rho(\mathbf r)$; suku kedua adalah tolakan Coulomb klasik oleh inti-inti lain. Inilah **teorema elektrostatik** Feynman: setelah kerapatan elektron diketahui dari mekanika kuantum, gaya pada inti dapat dihitung sepenuhnya dengan elektrostatika klasik. Tidak ada "gaya kuantum" khusus, "gaya pertukaran", atau "gaya resonansi" yang bekerja pada inti; semua efek kuantum tersimpan dalam bentuk $\rho(\mathbf r)$.

### Daerah mengikat dan antiikat

Persamaan (11.40) memberi cara yang sangat gamblang untuk memahami ikatan. Setiap unsur kerapatan elektron menarik kedua inti ke arahnya. Bila unsur itu berada di antara inti, tarikannya pada $A$ ke arah $B$ dan pada $B$ ke arah $A$: ia mendekatkan inti. Bila berada di belakang $A$ (di sisi yang jauh dari $B$), ia menarik $A$ menjauhi $B$ lebih kuat daripada menarik $B$ ke arah $A$: ia menjauhkan inti. T. Berlin (1951) membagi ruang menjadi **daerah mengikat** dan **daerah antiikat** dengan batas berupa dua permukaan berbentuk mangkuk yang membuka ke luar, melalui kedua inti (Gambar 11.14). Untuk molekul homonuklir, sebuah titik berada di daerah mengikat bila

$$
\frac{\cos\theta_A}{r_A^2} + \frac{\cos\theta_B}{r_B^2} > 0 , \qquad \text{(11.41)}
$$

dengan $\theta_A$ sudut di inti $A$ antara arah ke titik itu dan arah ke inti $B$ (demikian pula $\theta_B$). Ikatan terbentuk bila cukup banyak kerapatan elektron berpindah ke daerah mengikat untuk mengimbangi tolakan antarinti, dan orbital antiikatan memindahkan kerapatan ke daerah antiikat.

![Gambar 11.14 Daerah mengikat (biru muda) dan antiikat (putih) untuk molekul diatom homonuklir menurut kriteria Berlin (11.41), dengan kontur kerapatan elektron orbital $1\sigma_g$ H₂⁺ ($\zeta = 1{,}24$, $R = 2$ bohr). Kerapatan di daerah mengikat menarik kedua inti satu sama lain; kerapatan di belakang inti menarik keduanya menjauh.](fig/c_berlin.png){width=80%}

::: {.contoh}
**Contoh 11.77 · Gaya yang menahan H₂⁺**

Di jarak setimbang H₂⁺ ($R_e = 1{,}997$ bohr), gaya total pada setiap proton nol. Hitung gaya tolak antarproton dan gaya tarik yang harus diberikan awan elektron, dalam satuan atom dan nanonewton (1 hartree/bohr $= 82{,}39$ nN).

**Penyelesaian.** Tolakan $1/R_e^2 = 1/1{,}997^2 = 0{,}2507$ hartree/bohr $= 20{,}7$ nN. Menurut (11.40), awan elektron harus menarik setiap proton ke arah proton lain dengan gaya yang sama, 20,7 nN.

**Memahami hasil.** Awan satu elektron, yang separuhnya berada "di sisi" proton lain, harus menarik setiap proton seolah-olah ada muatan $-1$ pada jarak $R_e$ di arah proton tetangga. Itu hanya mungkin bila kerapatan elektron sedikit bergeser dari setiap proton ke arah daerah antarinti: awan di sekitar setiap inti terpolarisasi ke arah ikatan. Pergeseran kecil inilah yang ditangkap oleh fungsi polarisasi di Contoh 11.19.
:::

::: {.contoh}
**Contoh 11.78 · Teorema Hellmann–Feynman untuk atom H**

Ambil $\lambda = Z$ dalam Hamiltonian ion mirip hidrogen, $\hat H = -\tfrac12\nabla^2 - Z/r$, dengan $E = -Z^2/2$. Gunakan (11.39) untuk menghitung $\langle 1/r\rangle$.

**Penyelesaian.** $\partial\hat H/\partial Z = -1/r$. Maka $dE/dZ = -Z = \langle -1/r\rangle$, sehingga $\langle 1/r\rangle = Z$ (dalam bohr⁻¹).

**Memahami hasil.** Hasil ini sama dengan perhitungan langsung dengan fungsi gelombang 1s (subbab 7.9), tetapi diperoleh tanpa satu integral pun. Dengan memilih parameter lain (massa, $\hbar$, $\ell$), cara yang sama memberi $\langle T\rangle$, $\langle 1/r^2\rangle$, dan nilai harap lain. Dalam kimia komputasi, teorema ini menghubungkan turunan energi dengan sifat: turunan terhadap medan listrik memberi momen dipol ($\mu = -dE/dF$) dan polarisabilitas, turunan terhadap medan magnet memberi geseran kimia NMR.
:::

::: {.contoh}
**Contoh 11.79 · Gaya Pulay: ketika teorema tampak gagal**

Untuk LCAO H₂⁺ dengan $\zeta = 1$, energi minimum di $R = 2{,}493$ bohr, jadi $dE/dR = 0$ di sana. Namun integrasi numerik ruas kanan (11.39) dengan fungsi LCAO itu memberi tarikan elektron pada setiap proton hanya 0,0994 hartree/bohr, sedangkan tolakan antarproton $1/R^2 = 0{,}1609$ hartree/bohr. Hitung gaya "Hellmann–Feynman" bersih dan jelaskan mengapa tidak nol.

**Penyelesaian.** Gaya bersih $= 0{,}1609 - 0{,}0994 = 0{,}0615$ hartree/bohr, mendorong proton menjauh, padahal energi LCAO tidak berubah terhadap $R$ di titik itu.

**Memahami hasil.** Teorema Hellmann–Feynman berlaku untuk fungsi eigen eksak (dan untuk fungsi variasi yang lengkap terhadap perubahan $\lambda$). Fungsi LCAO tidak memenuhinya karena orbital 1s "ikut berpindah" bersama inti: suku $\partial\psi/\partial R$ yang dalam pembuktian lenyap, di sini tidak lenyap. Selisihnya disebut **gaya Pulay** (Peter Pulay, 1969). Program kimia kuantum yang mengoptimalkan geometri molekul dengan basis yang berpusat di atom harus menghitung gaya Pulay secara eksplisit; tanpanya, gaya yang dihitung salah dan optimasi geometri menuju struktur yang keliru. Contoh ini juga memperlihatkan mengapa kerapatan LCAO sederhana belum cukup baik: ia tidak cukup terpolarisasi ke daerah antarinti untuk menahan proton.
:::

::: {.contoh}
**Contoh 11.80 · Hellmann–Feynman dengan medan listrik**

Dalam medan listrik seragam $F$ sepanjang $z$, Hamiltonian molekul bertambah suku $-\hat\mu_zF$. Menurut (11.39), $dE/dF = -\langle\hat\mu_z\rangle$: momen dipol adalah turunan energi terhadap medan. Perhitungan RHF/aug-cc-pVDZ (PySCF) untuk molekul HF memberi $E(F) - E(0)$ untuk $F = \pm0{,}001$ satuan atom, dan dari selisihnya $\mu = -[E(+F) - E(-F)]/2F = 0{,}75961$ satuan atom. Nilai harap operator dipol yang dihitung langsung dari fungsi gelombang di $F = 0$ juga $0{,}75961$ satuan atom. Nyatakan dalam debye dan jelaskan mengapa kedua angka sama persis, padahal untuk gaya pada inti (Contoh 11.79) teorema ini gagal untuk fungsi pendekatan.

**Penyelesaian.** $0{,}75961 \times 2{,}5417 = 1{,}931$ D (terukur 1,83 D; selisihnya adalah efek korelasi, seperti di Contoh 11.70). Kedua angka sama karena fungsi basis tidak bergantung pada medan listrik: ketika $F$ berubah, hanya koefisien orbital yang berubah, dan koefisien itu optimal secara variasi, sehingga suku $\partial\psi/\partial F$ tidak menyumbang. Untuk koordinat inti, sebaliknya, fungsi basis ikut berpindah.

**Memahami hasil.** Turunan kedua, $-d^2E/dF^2$, memberi polarisabilitas: dari ketiga energi itu, $\alpha_{zz} = 5{,}6$ satuan atom. Cara "medan berhingga" ini adalah resep umum menghitung sifat molekul sebagai turunan energi: dipol, polarisabilitas, dan hiperpolarisabilitas dari medan listrik; geseran kimia NMR dan tetapan kopling dari medan magnet dan momen magnet inti; serta gaya dan tetapan gaya dari posisi inti.
:::

::: {.contoh}
**Contoh 11.81 · Asal gaya dispersi menurut Feynman**

Dua atom gas mulia yang berjauhan saling menarik lemah (gaya van der Waals, sebanding $R^{-7}$). Menurut teorema elektrostatik, gaya pada inti hanyalah tarikan oleh awan elektron dan tolakan oleh inti lain. Bagaimana tarikan muncul bila masing-masing atom netral dan bersimetri bola?

**Penyelesaian.** Fluktuasi korelasi antara elektron kedua atom (dipol sesaat yang saling menginduksi) membuat awan elektron setiap atom sedikit bergeser ke arah atom lain. Awan yang bergeser itu kini sedikit tidak simetris terhadap intinya sendiri, dan menarik intinya sendiri ke arah atom tetangga. Inilah yang Feynman sebut "dipol atom": gaya dispersi bekerja pada setiap inti melalui awan elektronnya sendiri yang terpolarisasi, bukan melalui awan atom lain.

**Memahami hasil.** Penjelasan ini, yang diberikan Feynman dalam makalah sarjananya pada 1939, menunjukkan kekuatan teorema elektrostatik: setiap gaya antarmolekul, dari ikatan kovalen sampai gaya van der Waals, dapat dibaca dari peta kerapatan elektron. Gaya dispersi sangat sulit ditangkap oleh teori fungsional kerapatan yang sederhana, karena pergeseran awan yang diperlukan sangat kecil dan berasal dari korelasi elektron (subbab 17.15).
:::

::: {.contoh}
**Contoh 11.82 · Gaya yang memutus ikatan**

Bila sebuah molekul ditarik dari kedua ujungnya, gaya pemulih $dE/dR$ naik dari nol di $R_e$, mencapai maksimum di titik belok kurva potensial, lalu turun ke nol pada disosiasi. (a) Dari kurva eksak H₂⁺, gaya pemulih maksimum adalah 0,0342 hartree/bohr di $R \approx 3{,}0$ bohr. Nyatakan dalam nN. (b) Untuk potensial Morse, gaya maksimum adalah $aD_e/2$. Hitung untuk H₂ ($a = 1{,}944$ Å⁻¹, $D_e = 4{,}747$ eV).

**Penyelesaian.** (a) $0{,}0342 \times 82{,}39 = 2{,}82$ nN. (b) $aD_e/2 = (1{,}944 \times 10^{10}\ \text{m}^{-1})(4{,}747 \times 1{,}602 \times 10^{-19}\ \text{J})/2 = 7{,}39 \times 10^{-9}$ N $= 7{,}4$ nN.

**Memahami hasil.** Gaya putus ikatan berorde beberapa nanonewton. Ikatan dua elektron H₂ sekitar 2,6 kali lebih "kuat" terhadap tarikan daripada ikatan satu elektron H₂⁺. Percobaan mikroskop gaya atom yang menarik satu rantai polimer yang ditambatkan secara kovalen memperlihatkan putusnya ikatan kovalen tunggal pada gaya sekitar 2 nN, sesuai orde besaran ini. Kimia mekanik (*mechanochemistry*) memanfaatkan gaya sebesar ini untuk mempercepat reaksi tertentu: tarikan mekanis memiringkan permukaan energi potensial, persis seperti medan listrik memiringkan potensial dalam efek Stark.
:::

::: {.terapan}
**Kaitan kimia · Dari gaya ke struktur molekul dan dinamika**

Setiap kali sebuah program kimia kuantum mengoptimalkan geometri molekul, ia menghitung gaya pada setiap inti, yaitu turunan energi terhadap koordinat inti, lalu menggeser inti searah gaya sampai gaya lenyap: itulah minimum permukaan energi potensial Born–Oppenheimer (subbab 17.9). Turunan kedua (matriks Hessian) memberi tetapan gaya dan frekuensi getaran yang dapat dibandingkan dengan spektrum IR. Dalam dinamika molekul *ab initio*, gaya dihitung ulang pada setiap langkah waktu, dan inti digerakkan menurut hukum Newton, sehingga reaksi kimia, difusi proton dalam air, dan pelelehan dapat disimulasikan langsung dari persamaan Schrödinger. Semua ini bertumpu pada dua gagasan bab ini: pemisahan Born–Oppenheimer, yang memberi potensial tempat inti bergerak, dan teorema Hellmann–Feynman, yang memberi gaya dari kerapatan elektron.
:::

::: {.kuis}
**Kuis cepat 11.16**

\(a) Mengapa suku yang memuat $\partial\psi/\partial\lambda$ lenyap dalam bukti teorema Hellmann–Feynman? (b) Di daerah mana kerapatan elektron menarik kedua inti menjauh? (c) Apa yang dimaksud gaya Pulay?
:::

### Menuju bab berikutnya

Teori orbital molekul dan ikatan valensi sudah kita bandingkan untuk molekul diatom. Bab 12 membawa teori ikatan valensi ke molekul poliatom melalui hibridisasi, yang menjelaskan bentuk metana, air, dan etilena.
