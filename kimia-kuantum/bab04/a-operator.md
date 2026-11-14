# Bab 4 Operator dan Postulat Mekanika Kuantum

Buka buku kimia dasar mana pun dan kamu akan menemukan tiga orbital p: $p_x$, $p_y$, $p_z$, berbentuk halter yang menunjuk ke tiga arah sumbu. Buka buku fisika atom dan kamu akan menemukan tiga orbital p yang lain: $p_{+1}$, $p_0$, $p_{-1}$, dua di antaranya berbentuk donat dan bernilai kompleks. Mana yang benar? Elektron 2p dalam atom karbon sebenarnya menempati yang mana?

Jawabannya: keduanya benar, dan pertanyaan "yang mana" tidak bermakna sampai kita menyebut **besaran apa yang diukur**. Orbital $p_{+1}$, $p_0$, $p_{-1}$ adalah keadaan dengan komponen-$z$ momentum sudut tertentu ($+\hbar$, $0$, $-\hbar$). Orbital $p_x$ dan $p_y$ tidak mempunyai komponen-$z$ momentum sudut tertentu, tetapi mempunyai arah yang jelas, berguna untuk ikatan. Dalam atom bebas tanpa medan, keenam fungsi itu berenergi sama, dan dua basis itu hanyalah dua cara menuliskan ruang keadaan yang sama, seperti dua pasang sumbu koordinat untuk bidang yang sama. Dalam medan magnet, energinya terpecah menurut $m_\ell$, dan basis kompleks menjadi istimewa. Dalam molekul dengan ikatan di sepanjang sumbu $x$, basis riil yang istimewa.

Bahasa yang membuat pernyataan-pernyataan seperti ini tepat adalah bahasa **operator**, **fungsi eigen**, dan **komutator**. Bab ini membangun bahasa itu, lalu merangkum seluruh mekanika kuantum dalam beberapa **postulat**. Setelah bab ini, setiap perhitungan dalam buku ini, dari osilator harmonik sampai teori fungsional kerapatan, adalah penerapan postulat-postulat yang sama.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa setiap besaran yang dapat diukur dinyatakan oleh sebuah operator, dan mengapa operator itu harus Hermitian?
2. Mengapa hasil pengukuran energi selalu salah satu tingkat energi, tidak pernah nilai di antaranya?
3. Apa arti matematis "dua besaran tidak dapat diukur serempak dengan tajam"?
4. Mengapa sebuah kotak kubus mempunyai tingkat energi yang terdegenerasi, dan mengapa degenerasi itu pecah bila kotaknya sedikit memanjang?
5. Bagaimana persamaan Schrödinger berubah menjadi soal diagonalisasi matriks?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menghitung dengan operator linear: jumlah, hasil kali, pangkat, dan komutator.
2. Menentukan apakah sebuah fungsi merupakan fungsi eigen suatu operator, beserta nilai eigen dan derajat degenerasinya.
3. Membangun operator kuantum dari besaran klasik, termasuk momentum, energi kinetik, dan momentum sudut.
4. Menuliskan persamaan Schrödinger tiga dimensi dan banyak partikel, dan memisahkan variabel untuk partikel yang tidak berinteraksi.
5. Menyelesaikan partikel dalam kotak tiga dimensi dan menganalisis degenerasinya, termasuk gas elektron dalam logam.
6. Menghitung nilai harap dan memakai teorema Ehrenfest.
7. Menyebutkan syarat fungsi gelombang yang dapat diterima.
8. Membuktikan bahwa operator Hermitian mempunyai nilai eigen riil dan fungsi eigen yang ortogonal.
9. Menguraikan fungsi atas fungsi eigen dan menafsirkan koefisiennya sebagai amplitudo peluang.
10. Menurunkan relasi ketidakpastian umum dari komutator dan menerapkannya.
11. Memakai paritas untuk menyederhanakan perhitungan dan menurunkan aturan seleksi.
12. Menyatakan postulat-postulat mekanika kuantum dan menerapkannya pada pengukuran.
13. Memakai notasi Dirac dan menyatakan operator sebagai matriks, termasuk mendiagonalkan Hamiltonian dengan Python.
:::

::: {.mat}
**Prasyarat**

Dari Bab 2: bilangan kompleks (2.1), integral parsial dan paritas (2.2), hasil kali dalam, ortonormalitas, dan ekspansi (2.6), matriks Hermitian dan nilai eigen (2.7 dan 2.8), statistik (2.10). Dari Bab 3: persamaan Schrödinger, tafsir Born, keadaan stasioner, superposisi (3.2–3.4), partikel dalam kotak (3.6 dan 3.7).
:::

## 4.1 Operator dan aljabarnya

### Definisi

**Operator** adalah aturan yang mengubah satu fungsi menjadi fungsi lain. Kita menandainya dengan topi: $\hat Af(x) = g(x)$. Contoh: $\hat D = d/dx$ mengubah $x^3$ menjadi $3x^2$; operator "kali dengan $x$", $\hat x$, mengubah $\sin x$ menjadi $x\sin x$; operator $\hat\Pi$ yang mengganti $x$ dengan $-x$ mengubah $e^x$ menjadi $e^{-x}$.

Sebuah operator disebut **linear** jika untuk sembarang fungsi $f$, $g$ dan tetapan $c$:

$$
\hat A(f + g) = \hat Af + \hat Ag, \qquad \hat A(cf) = c\hat Af . \qquad \text{(4.1)}
$$

Turunan, perkalian dengan fungsi, dan pembalikan $x \to -x$ semuanya linear. Mengambil akar kuadrat atau mengambil konjugat kompleks tidak linear. Semua operator besaran fisis dalam mekanika kuantum linear, karena persamaan Schrödinger linear dan asas superposisi harus berlaku.

### Aljabar operator

- **Jumlah**: $(\hat A + \hat B)f = \hat Af + \hat Bf$.
- **Hasil kali**: $\hat A\hat Bf = \hat A(\hat Bf)$, yaitu kerjakan $\hat B$ dulu, lalu $\hat A$. Urutan dibaca dari kanan ke kiri.
- **Pangkat**: $\hat A^2 = \hat A\hat A$; misalnya $\hat D^2 = d^2/dx^2$.
- **Komutator**: $[\hat A, \hat B] = \hat A\hat B - \hat B\hat A$.

Berbeda dengan perkalian bilangan, perkalian operator pada umumnya **tidak komutatif**. Contoh terpenting adalah $\hat x$ dan $\hat D$. Kerjakan pada fungsi uji $f$:

$$
\hat x\hat Df = x\frac{df}{dx}, \qquad \hat D\hat xf = \frac{d}{dx}(xf) = f + x\frac{df}{dx} .
$$

Selisihnya $-f$, untuk fungsi $f$ apa pun. Jadi $[\hat x, \hat D] = -1$. Untuk mengerjakan komutator dengan benar, **selalu bekerjakan pada fungsi uji** lalu hapus fungsi itu di akhir; tanpa fungsi uji, aturan hasil kali mudah terlupa.

### Identitas komutator

Komutator memenuhi beberapa identitas yang langsung diperiksa dari definisinya:

$$
[\hat A, \hat B] = -[\hat B, \hat A], \qquad [\hat A, \hat B + \hat C] = [\hat A, \hat B] + [\hat A, \hat C], \qquad [\hat A, \hat B\hat C] = [\hat A, \hat B]\hat C + \hat B[\hat A, \hat C] . \qquad \text{(4.2)}
$$

Identitas terakhir, "aturan hasil kali untuk komutator", sangat berguna: misalnya $[\hat x, \hat D^2] = [\hat x, \hat D]\hat D + \hat D[\hat x, \hat D] = -2\hat D$.

::: {.contoh}
**Contoh 4.1 · Linear atau tidak?**

Manakah operator berikut yang linear? (a) $\hat A f = x^2f$; (b) $\hat Bf = f^2$; (c) $\hat Cf = \int_0^xf(t)\,dt$; (d) $\hat Ef = f + 3$; (e) $\hat Ff = f^*$.

**Penyelesaian.** (a) Linear: $x^2(f + g) = x^2f + x^2g$. (b) Tidak: $(f + g)^2 \ne f^2 + g^2$. (c) Linear: integral adalah operasi linear. (d) Tidak: $\hat E(2f) = 2f + 3 \ne 2(f + 3)$. (e) Tidak: $\hat F(if) = -if^* \ne i\hat Ff$ (operator ini "antilinear").

**Memahami hasil.** Operator "tambah tetapan" tampak sederhana, tetapi tidak linear. Pengambilan konjugat kompleks tidak linear karena tidak menghormati perkalian dengan bilangan kompleks; operator semacam ini muncul dalam pembalikan waktu, tetapi tidak sebagai besaran yang diukur.
:::

::: {.contoh}
**Contoh 4.2 · Komutator posisi dan momentum**

Dengan $\hat p_x = -i\hbar\,d/dx$, hitung $[\hat x, \hat p_x]$, $[\hat x^2, \hat p_x]$, dan $[\hat x, \hat p_x^2]$.

**Penyelesaian.** Dari $[\hat x, \hat D] = -1$: $[\hat x, \hat p_x] = -i\hbar[\hat x, \hat D] = i\hbar$.

Dengan (4.2): $[\hat x^2, \hat p_x] = \hat x[\hat x, \hat p_x] + [\hat x, \hat p_x]\hat x = 2i\hbar\hat x$.

$[\hat x, \hat p_x^2] = [\hat x, \hat p_x]\hat p_x + \hat p_x[\hat x, \hat p_x] = 2i\hbar\hat p_x$.

**Memahami hasil.** Hubungan $[\hat x, \hat p_x] = i\hbar$ disebut **komutator kanonik**; seluruh mekanika kuantum satu partikel dapat dibangun darinya. Pola hasil (b) umum: $[f(\hat x), \hat p_x] = i\hbar f'(\hat x)$, sehingga komutator dengan $\hat p_x$ bekerja seperti turunan. Hasil (c) dipakai di subbab 4.10 untuk menurunkan bahwa $\tfrac{d}{dt}\langle x\rangle = \langle p\rangle/m$.
:::

::: {.contoh}
**Contoh 4.3 · Kuadrat operator dan urutan kerja**

Untuk $\hat A = x + d/dx$, hitung $\hat A^2f$ dan bandingkan dengan $(x^2 + d^2/dx^2)f$.

**Penyelesaian.**

$$
\hat A^2f = \left(x + \frac{d}{dx}\right)\left(xf + f'\right) = x^2f + xf' + \frac{d}{dx}(xf) + f'' = x^2f + 2xf' + f + f'' .
$$

Jadi $\hat A^2 = x^2 + 2x\,d/dx + 1 + d^2/dx^2$, yang berbeda dari $x^2 + d^2/dx^2$ sebesar $2x\,d/dx + 1$.

**Memahami hasil.** Rumus $(a + b)^2 = a^2 + 2ab + b^2$ untuk bilangan berubah menjadi $(\hat a + \hat b)^2 = \hat a^2 + \hat a\hat b + \hat b\hat a + \hat b^2$ untuk operator; kedua suku tengah tidak boleh disatukan bila operatornya tidak komut. Kombinasi $x \pm d/dx$ semacam ini, kelak, adalah **operator tangga** osilator harmonik (Bab 5).
:::

::: {.kuis}
**Kuis cepat 4.1**

Hitung $[\hat D, x^3]$ (kerjakan pada fungsi uji). Apakah $\hat D$ dan operator "kali dengan $e^x$" komut?
:::

## 4.2 Fungsi eigen dan nilai eigen

### Persamaan nilai eigen

Jika operator $\hat A$ yang bekerja pada fungsi $f$ menghasilkan fungsi yang sama dikali tetapan,

$$
\boxed{\ \hat Af = af\ } \qquad \text{(4.3)}
$$

maka $f$ disebut **fungsi eigen** $\hat A$ dengan **nilai eigen** $a$. Fungsi nol dikecualikan (ia memenuhi persamaan untuk $a$ berapa pun). Persamaan Schrödinger tak bergantung waktu $\hat H\psi = E\psi$ adalah persamaan nilai eigen untuk operator energi. Ini sama persis dengan persamaan nilai eigen matriks di subbab 2.8; perbedaannya hanya bahwa "vektor"-nya kini fungsi.

Fungsi eigen hanya tertentu sampai faktor pengali: jika $f$ fungsi eigen, $cf$ juga, dengan nilai eigen yang sama. Kebebasan ini dipakai untuk menormalisasi.

### Degenerasi

Jika beberapa fungsi eigen yang **bebas linear** mempunyai nilai eigen yang sama, nilai eigen itu disebut **terdegenerasi**, dan banyaknya fungsi bebas linear itu disebut **derajat degenerasi** $g$. Sifat terpenting: **setiap kombinasi linear fungsi-fungsi eigen yang terdegenerasi juga fungsi eigen dengan nilai eigen yang sama**. Buktinya satu baris: jika $\hat Af_1 = af_1$ dan $\hat Af_2 = af_2$, maka $\hat A(c_1f_1 + c_2f_2) = a(c_1f_1 + c_2f_2)$, karena $\hat A$ linear.

Inilah inti teka-teki pembuka bab. Orbital $p_{+1}$, $p_0$, $p_{-1}$ adalah fungsi eigen Hamiltonian atom hidrogen dengan energi sama. Kombinasi $p_x = (p_{-1} - p_{+1})/\sqrt2$ dan $p_y = i(p_{-1} + p_{+1})/\sqrt2$ karena itu juga fungsi eigen Hamiltonian dengan energi yang sama. Dalam ruang terdegenerasi kita bebas memilih basis; pilihan yang "baik" ditentukan oleh operator lain yang ingin kita buat diagonal (subbab 4.10).

::: {.contoh}
**Contoh 4.4 · Mengenali fungsi eigen**

Manakah yang merupakan fungsi eigen $d/dx$, dan manakah fungsi eigen $d^2/dx^2$? Berikan nilai eigennya. (a) $e^{-3x}$; (b) $\sin 2x$; (c) $x^2$; (d) $e^{ikx}$; (e) $3\cos 5x - \sin 5x$.

**Penyelesaian.** Untuk $d/dx$: (a) ya, $-3$; (d) ya, $ik$; lainnya tidak. Untuk $d^2/dx^2$: (a) ya, $9$; (b) ya, $-4$; (d) ya, $-k^2$; (e) ya, $-25$; (c) tidak ($d^2x^2/dx^2 = 2$).

**Memahami hasil.** Fungsi (e) adalah kombinasi linear $\cos 5x$ dan $\sin 5x$, yang sama-sama fungsi eigen $d^2/dx^2$ dengan nilai eigen $-25$: contoh degenerasi. Ia bukan fungsi eigen $d/dx$. Fungsi eigen $d^2/dx^2$ tidak harus fungsi eigen $d/dx$, tetapi fungsi eigen $d/dx$ selalu fungsi eigen $d^2/dx^2$.
:::

::: {.contoh}
**Contoh 4.5 · Nilai eigen dari syarat batas**

Cari fungsi eigen dan nilai eigen $\hat A = -d^2/dx^2$ pada $[0, \pi]$ dengan syarat $f(0) = f(\pi) = 0$.

**Penyelesaian.** $-f'' = af$. Untuk $a \le 0$ penyelesaiannya eksponen atau linear, yang tidak dapat nol di kedua ujung kecuali $f = 0$. Untuk $a = k^2 > 0$: $f = \sin kx$ dengan $\sin k\pi = 0$, sehingga $k = 1, 2, 3, \ldots$ Fungsi eigen $\sin nx$, nilai eigen $a = n^2$.

**Memahami hasil.** Operator yang sama mempunyai himpunan nilai eigen yang berbeda bergantung pada **ruang fungsi** tempat ia bekerja, termasuk syarat batasnya. Tanpa syarat batas, setiap bilangan adalah nilai eigen $-d^2/dx^2$. Fisika memilih ruang fungsi lewat syarat-syarat yang dibahas di subbab 4.7.
:::

::: {.contoh}
**Contoh 4.6 · Fungsi eigen operator pembalikan**

Operator paritas $\hat\Pi$ didefinisikan oleh $\hat\Pi f(x) = f(-x)$. (a) Tunjukkan bahwa $\hat\Pi^2 = 1$. (b) Simpulkan nilai eigen yang mungkin. (c) Manakah fungsi eigen: $\cos x$, $x^3$, $e^x$, $x^2 + x$?

**Penyelesaian.** (a) $\hat\Pi^2f(x) = \hat\Pi f(-x) = f(x)$. (b) Jika $\hat\Pi f = \lambda f$, maka $f = \hat\Pi^2f = \lambda^2f$, jadi $\lambda = \pm1$. (c) $\cos x$: $+1$; $x^3$: $-1$; $e^x$ dan $x^2 + x$: bukan.

**Memahami hasil.** Fungsi eigen paritas adalah fungsi genap ($+1$) dan ganjil ($-1$). Setiap fungsi dapat diuraikan menjadi bagian genap dan ganjil: $e^x = \cosh x + \sinh x$. Paritas dibahas lebih lanjut di subbab 4.11.
:::

::: {.kuis}
**Kuis cepat 4.2**

Jika $f$ dan $g$ fungsi eigen $\hat A$ dengan nilai eigen **berbeda**, apakah $f + g$ fungsi eigen $\hat A$?
:::

## 4.3 Operator besaran fisika

### Aturan membangun operator

Setiap besaran fisis yang dapat diukur (disebut **teramati**) dinyatakan oleh sebuah operator linear Hermitian. Untuk besaran yang mempunyai padanan klasik, operatornya dibangun dengan aturan berikut:

1. Tuliskan besaran klasiknya sebagai fungsi koordinat Kartesius dan momentum.
2. Ganti koordinat dengan operator perkalian: $\hat x = x$, $\hat y = y$, $\hat z = z$.
3. Ganti komponen momentum dengan operator turunan:

$$
\hat p_x = -i\hbar\frac{\partial}{\partial x}, \qquad \hat p_y = -i\hbar\frac{\partial}{\partial y}, \qquad \hat p_z = -i\hbar\frac{\partial}{\partial z} . \qquad \text{(4.4)}
$$

Bentuk ini sudah kita temui ketika menebak persamaan Schrödinger (subbab 3.2): ia adalah satu-satunya operator yang memberi gelombang de Broglie $e^{ikx}$ momentum tepat $\hbar k$. Aturan ini harus dipakai dalam **koordinat Kartesius**; operator dalam koordinat lain diperoleh dengan mengubah koordinat setelah operator Kartesius dibentuk.

### Operator-operator terpenting

| Besaran | Klasik | Operator |
|---|---|---|
| posisi | $x$ | $x\,\cdot$ |
| momentum | $p_x$ | $-i\hbar\,\partial/\partial x$ |
| energi kinetik | $p^2/2m$ | $-\dfrac{\hbar^2}{2m}\nabla^2$ |
| energi potensial | $V(\mathbf r)$ | $V(\mathbf r)\,\cdot$ |
| energi total | $p^2/2m + V$ | $\hat H = -\dfrac{\hbar^2}{2m}\nabla^2 + V$ |
| momentum sudut-$z$ | $xp_y - yp_x$ | $-i\hbar\left(x\dfrac{\partial}{\partial y} - y\dfrac{\partial}{\partial x}\right) = -i\hbar\dfrac{\partial}{\partial\phi}$ |
| momen dipol listrik | $\sum q_i\mathbf r_i$ | $\sum q_i\mathbf r_i\,\cdot$ |

Perhatikan bahwa energi kinetik dibentuk dari $\hat p_x^2 + \hat p_y^2 + \hat p_z^2 = -\hbar^2\nabla^2$. Beberapa besaran, terutama **spin**, tidak mempunyai padanan klasik; operatornya ditentukan oleh sifat-sifat aljabarnya (Bab 9).

::: {.contoh}
**Contoh 4.7 · Momentum sudut-$z$ dalam koordinat bola**

Tunjukkan bahwa $\hat L_z = -i\hbar(x\,\partial_y - y\,\partial_x)$ sama dengan $-i\hbar\,\partial/\partial\phi$.

**Penyelesaian.** Dalam koordinat bola, $x = r\sin\theta\cos\phi$ dan $y = r\sin\theta\sin\phi$, sedangkan $r$ dan $\theta$ tidak bergantung pada $\phi$. Dengan aturan rantai:

$$
\frac{\partial}{\partial\phi} = \frac{\partial x}{\partial\phi}\frac{\partial}{\partial x} + \frac{\partial y}{\partial\phi}\frac{\partial}{\partial y} + \frac{\partial z}{\partial\phi}\frac{\partial}{\partial z} = -y\frac{\partial}{\partial x} + x\frac{\partial}{\partial y} + 0 .
$$

Kalikan dengan $-i\hbar$: $-i\hbar\,\partial/\partial\phi = -i\hbar(x\,\partial_y - y\,\partial_x) = \hat L_z$.

**Memahami hasil.** Momentum sudut terhadap sumbu $z$ adalah "momentum" untuk sudut $\phi$, persis seperti $\hat p_x$ untuk koordinat $x$. Fungsi eigennya $e^{im\phi}$ dengan nilai eigen $m\hbar$ (Contoh 4.9).
:::

::: {.contoh}
**Contoh 4.8 · Energi kinetik gelombang bidang dan fungsi Gauss**

(a) Hitung $\hat T\psi$ untuk $\psi = e^{i(k_xx + k_yy + k_zz)}$. (b) Untuk $\psi = e^{-ax^2}$ (satu dimensi), apakah $\psi$ fungsi eigen $\hat T$?

**Penyelesaian.** (a) $\nabla^2\psi = -(k_x^2 + k_y^2 + k_z^2)\psi$, sehingga $\hat T\psi = \dfrac{\hbar^2k^2}{2m}\psi$: fungsi eigen dengan nilai eigen $p^2/2m$.

(b) $\psi'' = (4a^2x^2 - 2a)\psi$, sehingga $\hat T\psi = -\dfrac{\hbar^2}{2m}(4a^2x^2 - 2a)\psi$. Faktor bergantung pada $x$: bukan fungsi eigen.

**Memahami hasil.** Fungsi Gauss bukan keadaan dengan energi kinetik tertentu; energi kinetiknya tersebar. Tetapi jika ditambah potensial $V = \tfrac12\kappa x^2$ yang cocok, suku $x^2$ dari energi kinetik dibatalkan oleh energi potensial, dan $e^{-ax^2}$ menjadi fungsi eigen $\hat H$ osilator harmonik (Bab 5), sama seperti $e^{-r}$ untuk atom hidrogen (Contoh 2.53 di Bab 2).
:::

::: {.contoh}
**Contoh 4.9 · Fungsi eigen $\hat L_z$**

(a) Cari fungsi eigen $\hat L_z = -i\hbar\,\partial/\partial\phi$. (b) Syarat apa yang membatasi nilai eigennya? (c) Apakah $\cos\phi$ fungsi eigen $\hat L_z$? Apakah fungsi eigen $\hat L_z^2$?

**Penyelesaian.** (a) $-i\hbar\,d\Phi/d\phi = \ell_z\Phi$ memberikan $\Phi = e^{i\ell_z\phi/\hbar}$.

(b) $\phi$ dan $\phi + 2\pi$ adalah titik yang sama, sehingga fungsi gelombang harus bernilai tunggal: $e^{i\ell_z(\phi + 2\pi)/\hbar} = e^{i\ell_z\phi/\hbar}$, yaitu $e^{2\pi i\ell_z/\hbar} = 1$. Jadi $\ell_z = m\hbar$ dengan $m = 0, \pm1, \pm2, \ldots$

(c) $\hat L_z\cos\phi = i\hbar\sin\phi$: bukan fungsi eigen. $\hat L_z^2\cos\phi = -\hbar^2\,d^2\cos\phi/d\phi^2 = \hbar^2\cos\phi$: fungsi eigen $\hat L_z^2$ dengan nilai eigen $\hbar^2$.

**Memahami hasil.** Kuantisasi momentum sudut di sini tidak datang dari dinding, melainkan dari **kebernilaian tunggal**: setelah satu putaran penuh, fungsi gelombang harus kembali ke nilainya sendiri. Orbital riil $p_x \propto \sin\theta\cos\phi$ mempunyai $L_z^2$ tertentu ($\hbar^2$), tetapi bukan $L_z$ tertentu; ia campuran sama besar $m = +1$ dan $-1$. Itulah jawaban teka-teki pembuka.
:::

::: {.contoh}
**Contoh 4.10 · Operator momen dipol molekul**

Molekul HCl terdiri atas inti H (muatan $+e$) di $\mathbf R_\text{H}$, inti Cl ($+17e$) di $\mathbf R_\text{Cl}$, dan 18 elektron di $\mathbf r_1, \ldots, \mathbf r_{18}$. Tuliskan operator momen dipolnya. Mengapa nilainya tidak bergantung pada pilihan titik asal?

**Penyelesaian.** $\hat{\boldsymbol\mu} = e\mathbf R_\text{H} + 17e\mathbf R_\text{Cl} - e\sum_{i=1}^{18}\mathbf r_i$. Menggeser titik asal sejauh $\mathbf d$ mengubah setiap posisi menjadi $\mathbf r - \mathbf d$, sehingga $\boldsymbol\mu$ berubah sebesar $-\mathbf d\sum q_i = -\mathbf d(1 + 17 - 18)e = 0$.

**Memahami hasil.** Untuk molekul netral, momen dipol tidak bergantung pada titik asal; untuk ion, ia bergantung, sehingga momen dipol ion harus dinyatakan terhadap titik tertentu (biasanya pusat massa). Nilai harap operator ini, $\langle\Psi|\hat{\boldsymbol\mu}|\Psi\rangle$, adalah momen dipol yang diukur dari spektrum gelombang mikro atau tetapan dielektrik (Bab 11).
:::

::: {.kuis}
**Kuis cepat 4.3**

Tuliskan operator untuk $p_x^2 + p_y^2$ dan untuk energi potensial osilator harmonik tiga dimensi isotropik $\tfrac12\kappa r^2$.
:::
