# Bab 7 Atom Hidrogen

Foto nebula seperti Nebula Orion selalu didominasi warna merah muda. Warna itu berasal dari satu garis spektrum, H$_\alpha$ pada 656,3 nm, yang dipancarkan atom hidrogen ketika elektronnya turun dari tingkat $n = 3$ ke $n = 2$. Di laboratorium, garis-garis hidrogen diukur dengan ketelitian lebih dari dua belas angka penting, dan tidak ada satu pun yang menyimpang dari ramalan teori kuantum yang lengkap. Tetapi ada keanehan yang tersembunyi dalam keberhasilan itu. Dalam atom hidrogen, orbital 2s dan 2p mempunyai energi yang sama persis, demikian pula 3s, 3p, dan 3d. Dalam atom litium, natrium, atau atom apa pun selain hidrogen, orbital s selalu lebih rendah daripada orbital p dengan $n$ yang sama, dan urutan itulah yang membentuk tabel periodik. Apa yang istimewa dari atom hidrogen, dan apa yang hilang ketika elektron kedua ditambahkan? Jawaban pertanyaan terakhir ini ada di Bab 9 (subbab 9.9).

Atom hidrogen adalah satu-satunya atom yang persamaan Schrödingernya dapat diselesaikan secara tepat. Penyelesaiannya adalah fondasi seluruh kimia: fungsi gelombangnya adalah **orbital** s, p, d, dan f yang dipakai untuk menggambarkan setiap atom dan molekul; bilangan kuantum $n$, $\ell$, dan $m_\ell$ yang muncul darinya menjadi label konfigurasi elektron; dan skala panjang dan energinya, bohr dan hartree, menjadi satuan atom yang dipakai di sisa buku ini.

Bab ini menggabungkan hasil-hasil Bab 6 (harmonik bola, massa tereduksi, potensial efektif) dengan penyelesaian persamaan radial. Kita akan melihat mengapa energi bergantung hanya pada $n$, bagaimana bentuk orbital ditentukan oleh simpul radial dan sudut, mengapa elektron 2s "menembus" lebih dekat ke inti daripada elektron 2p, dan bagaimana spektrum, aturan seleksi, dan efek medan magnet mengikuti dari fungsi-fungsi gelombang ini.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa energi atom hidrogen hanya bergantung pada bilangan kuantum utama $n$?
2. Apa arti fisis simpul radial dan simpul sudut, dan berapa jumlah masing-masing?
3. Mengapa elektron 1s paling mungkin ditemukan pada jarak $a_0$ dari inti, padahal rapat peluangnya terbesar di inti?
4. Mengapa transisi 2s → 1s terlarang, sedangkan 2p → 1s sangat cepat?
5. Bagaimana medan magnet memecah garis spektrum, dan apa yang dapat dipelajari darinya?
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menuliskan Hamiltonian atom hidrogen dalam satuan SI dan satuan atom, serta menjelaskan peran massa tereduksi.
2. Memisahkan persamaan Schrödinger menjadi bagian radial dan sudut.
3. Menyelesaikan persamaan radial dengan deret pangkat dan memperoleh syarat kuantisasi energi.
4. Menghitung tingkat energi, degenerasi, dan energi transisi atom hidrogen.
5. Menuliskan dan menganalisis fungsi radial, termasuk letak simpul radialnya.
6. Menghitung dan menafsirkan fungsi distribusi radial, jarak paling mungkin, dan peluang di dalam bola.
7. Mengubah orbital kompleks menjadi orbital riil dan menjelaskan kapan masing-masing dipakai.
8. Menggambarkan bentuk orbital s, p, d, dan f dan menghitung simpul-simpulnya.
9. Menghitung nilai harap $\langle r\rangle$, $\langle 1/r\rangle$, dan energi kinetik serta potensial, dan memeriksa teorema virial.
10. Menerapkan hasil atom hidrogen pada ion mirip hidrogen dan hukum Moseley.
11. Menurunkan aturan seleksi dipol dan menghitung laju peluruhan radiatif.
12. Menghitung pemecahan Zeeman normal.
13. Menyelesaikan persamaan radial secara numerik dan menerapkannya pada potensial model atom alkali.
:::

::: {.mat}
**Prasyarat**

Dari *Fisika Umum*: Bab 12 (hukum Coulomb, energi potensial listrik) dan Bab 15 (model Bohr). Dari buku ini: model Bohr dan spektrum hidrogen (subbab 1.6), integral $\int_0^\infty x^ne^{-ax}dx$ (persamaan 2.8), koordinat bola (subbab 2.5), deret pangkat (subbab 2.4), satuan atom (subbab 2.11), nilai harap (subbab 4.6) dan pembagian energi kinetik–potensial osilator (subbab 5.5); teorema virial sendiri baru diturunkan di subbab 7.9, harmonik bola, massa tereduksi, dan potensial efektif (Bab 6), metode Numerov (subbab 5.12).
:::

## 7.1 Masalah gaya sentral

### Hamiltonian

Atom hidrogen terdiri atas satu proton dan satu elektron yang saling menarik dengan gaya Coulomb. Setelah gerak pusat massa dipisahkan (subbab 6.8), gerak relatif adalah partikel bermassa tereduksi $\mu = m_em_p/(m_e + m_p)$ dalam potensial

$$
V(r) = -\frac{Ze^2}{4\pi\varepsilon_0r} , \qquad \text{(7.1)}
$$

dengan $Z = 1$ untuk hidrogen. Kita langsung menuliskan $Z$ umum agar hasilnya berlaku untuk ion mirip hidrogen (He⁺, Li²⁺, ...; subbab 7.10). Hamiltoniannya

$$
\hat H = -\frac{\hbar^2}{2\mu}\nabla^2 - \frac{Ze^2}{4\pi\varepsilon_0r} . \qquad \text{(7.2)}
$$

### Satuan atom

Dalam satuan atom (subbab 2.11), $\hbar = m_e = e = 4\pi\varepsilon_0 = 1$, panjang diukur dalam bohr ($a_0 = 52{,}918$ pm) dan energi dalam hartree ($E_h = 27{,}211$ eV). Bila kita juga mengabaikan selisih kecil antara $\mu$ dan $m_e$ (0,05% untuk hidrogen; koreksinya dibahas di subbab 7.4), persamaan Schrödinger menjadi

$$
\left[-\tfrac12\nabla^2 - \frac Zr\right]\psi = E\psi . \qquad \text{(7.3)}
$$

Bentuk ini bebas dari tetapan, sehingga strukturnya terlihat jelas. Mulai bab ini, rumus-rumus ditulis dalam satuan atom kecuali dinyatakan lain; untuk kembali ke SI, kalikan panjang dengan $a_0$ dan energi dengan $E_h$.

### Mengapa masalah ini dapat diselesaikan

Potensial (7.1) bersifat **sentral**: ia hanya bergantung pada $r$. Menurut subbab 6.2, $\hat L^2$ dan $\hat L_z$ komut dengan Hamiltonian (Contoh 6.7), sehingga ada fungsi eigen bersama ketiganya. Bagian sudutnya sudah diketahui: harmonik bola. Yang tersisa hanya persamaan diferensial biasa satu variabel, persamaan radial. Untuk potensial sentral apa pun, langkah ini berlaku; kekhususan potensial Coulomb baru muncul pada penyelesaian persamaan radialnya.

::: {.contoh}
**Contoh 7.1 · Skala energi dan panjang atom**

Hitung energi potensial elektron dan proton pada jarak $a_0$ dan pada jarak 100 pm, dalam eV dan hartree. Hitung juga medan listrik proton di jarak $a_0$.

**Penyelesaian.** $V(a_0) = -e^2/(4\pi\varepsilon_0a_0) = -4{,}360 \times 10^{-18}$ J $= -27{,}21$ eV $= -1$ $E_h$. Pada 100 pm $= 1{,}890\,a_0$: $V = -1/1{,}890 = -0{,}529$ $E_h = -14{,}40$ eV. Medan $e/(4\pi\varepsilon_0a_0^2) = 5{,}14 \times 10^{11}$ V/m.

**Memahami hasil.** Satu hartree adalah energi Coulomb dua muatan elementer pada jarak satu bohr. Medan listrik di dalam atom ($5 \times 10^{11}$ V/m) ribuan kali lebih kuat daripada medan terkuat yang dapat dibuat di laboratorium dengan elektroda; itulah sebabnya efek Stark pada atom dalam medan luar kecil, dan perturbasi (Bab 8) cukup untuk menghitungnya. Hanya laser berdaya sangat tinggi yang mampu menyaingi medan ini dan mengionisasi atom secara langsung.
:::

::: {.contoh}
**Contoh 7.2 · Mengubah persamaan ke satuan atom**

Tunjukkan bahwa dengan $r = a_0\rho$ dan $E = E_h\varepsilon$, persamaan (7.2) dengan $\mu = m_e$ dan $Z = 1$ menjadi (7.3) dalam variabel $\rho$ dan $\varepsilon$.

**Penyelesaian.** $\nabla_r^2 = a_0^{-2}\nabla_\rho^2$. Persamaannya $-\tfrac{\hbar^2}{2m_ea_0^2}\nabla_\rho^2\psi - \tfrac{e^2}{4\pi\varepsilon_0a_0}\tfrac1\rho\psi = E_h\varepsilon\psi$. Dengan $a_0 = 4\pi\varepsilon_0\hbar^2/m_ee^2$: $\tfrac{\hbar^2}{m_ea_0^2} = \tfrac{e^2}{4\pi\varepsilon_0a_0} = E_h$. Bagi seluruhnya dengan $E_h$: $-\tfrac12\nabla_\rho^2\psi - \tfrac1\rho\psi = \varepsilon\psi$.

**Memahami hasil.** Kedua skala energi, kinetik ($\hbar^2/m_ea_0^2$) dan potensial ($e^2/4\pi\varepsilon_0a_0$), sama tepat pada jarak $a_0$. Itulah definisi jari-jari Bohr: jarak tempat energi kinetik "pengurungan" sama besar dengan tarikan Coulomb. Kesamaan ini adalah teorema virial dalam bentuk paling ringkas (subbab 7.9).
:::

::: {.contoh}
**Contoh 7.3 · Mengapa elektron tidak jatuh ke inti**

Perkirakan dengan asas ketidakpastian energi elektron yang terkurung dalam bola berjari-jari $r$: $E(r) \approx \tfrac{1}{2r^2} - \tfrac1r$ (satuan atom). Cari minimumnya.

**Penyelesaian.** $dE/dr = -\tfrac{1}{r^3} + \tfrac{1}{r^2} = 0$ memberi $r = 1$ bohr, dan $E = \tfrac12 - 1 = -\tfrac12$ hartree.

**Memahami hasil.** Taksiran kasar ini kebetulan memberi jawaban tepat. Energi kinetik pengurungan tumbuh seperti $1/r^2$, lebih cepat daripada tarikan Coulomb ($1/r$), sehingga mendekat ke inti tidak menguntungkan di bawah jarak tertentu. Fisika klasik tidak mempunyai suku $1/r^2$ ini, dan karena itu meramalkan keruntuhan atom (subbab 1.6). Stabilitas atom adalah akibat langsung dari asas ketidakpastian.
:::

::: {.kuis}
**Kuis cepat 7.1**

Berapa energi potensial (hartree) elektron pada jarak 2 bohr dari inti He²⁺? Mengapa potensial Coulomb disebut sentral?
:::

## 7.2 Pemisahan variabel

### Bagian sudut dan bagian radial

Dengan Laplasian dalam bentuk (6.8), persamaan (7.3) menjadi

$$
-\frac{1}{2r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\psi}{\partial r}\right) + \frac{\hat L^2}{2r^2}\psi - \frac Zr\psi = E\psi . \qquad \text{(7.4)}
$$

Coba $\psi(r, \theta, \phi) = R(r)\,Y_\ell^m(\theta, \phi)$. Karena $\hat L^2Y_\ell^m = \ell(\ell + 1)Y_\ell^m$ (dalam satuan atom $\hbar = 1$), harmonik bola dapat dicoret dari kedua ruas, dan tersisa **persamaan radial**:

$$
-\frac{1}{2r^2}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) + \left[\frac{\ell(\ell + 1)}{2r^2} - \frac Zr\right]R = ER . \qquad \text{(7.5)}
$$

Persamaan ini bergantung pada $\ell$ tetapi tidak pada $m$. Akibatnya, untuk $\ell$ tertentu, semua $2\ell + 1$ nilai $m$ mempunyai fungsi radial dan energi yang sama: degenerasi "biasa" setiap potensial sentral.

### Fungsi $u = rR$

Persamaan (7.5) menjadi lebih sederhana dengan substitusi $u(r) = rR(r)$. Karena $\tfrac{1}{r^2}\tfrac{d}{dr}(r^2R') = \tfrac1ru''$ (soal di akhir bab), diperoleh

$$
-\tfrac12u'' + V_\text{ef}(r)\,u = Eu, \qquad V_\text{ef}(r) = -\frac Zr + \frac{\ell(\ell + 1)}{2r^2} . \qquad \text{(7.6)}
$$

Ini persamaan Schrödinger **satu dimensi** pada setengah garis $r > 0$ dengan potensial efektif (6.26) (Gambar 7.1). Normalisasinya juga sederhana: $\int_0^\infty R^2r^2dr = \int_0^\infty u^2dr = 1$. Syarat batasnya $u(0) = 0$, agar $R = u/r$ berhingga di inti.

![Gambar 7.1 Potensial efektif atom hidrogen untuk $\ell = 0$, 1, dan 2 (satuan atom). Untuk $\ell > 0$, penghalang sentrifugal menjauhkan elektron dari inti. Garis putus-putus adalah tingkat energi $n = 1$, 2, 3; setiap tingkat $n$ dapat dicapai oleh semua kurva dengan $\ell < n$.](fig/c_veff.png){width=78%}

### Bilangan kuantum

Fungsi gelombang akan diberi label tiga bilangan kuantum:

* $n$, **bilangan kuantum utama**, dari persamaan radial (subbab 7.3), menentukan energi;
* $\ell$, **bilangan kuantum momentum sudut** (azimut), menentukan $L^2 = \ell(\ell + 1)\hbar^2$ dan bentuk orbital (s, p, d, f untuk $\ell = 0$, 1, 2, 3);
* $m_\ell$, **bilangan kuantum magnetik**, menentukan $L_z = m_\ell\hbar$ dan orientasi orbital.

Huruf s, p, d, dan f berasal dari nama deret garis spektrum logam alkali (*sharp*, *principal*, *diffuse*, *fundamental*); setelah f, huruf berlanjut menurut abjad: g, h, ...

::: {.contoh}
**Contoh 7.4 · Memeriksa fungsi 2p$_0$**

Tunjukkan bahwa $\psi = re^{-r/2}\cos\theta$ adalah fungsi eigen (7.3) dengan $Z = 1$, dan tentukan energinya.

**Penyelesaian.** $\psi = R(r)Y$ dengan $R = re^{-r/2}$ dan $Y \propto \cos\theta$ ($\ell = 1$). Dengan $u = rR = r^2e^{-r/2}$: $u' = (2r - \tfrac12r^2)e^{-r/2}$, $u'' = (2 - 2r + \tfrac14r^2)e^{-r/2}$. Ruas kiri (7.6) dengan $\ell = 1$: $-\tfrac12(2 - 2r + \tfrac14r^2)e^{-r/2} + (-\tfrac1r + \tfrac{1}{r^2})r^2e^{-r/2} = (-1 + r - \tfrac18r^2 - r + 1)e^{-r/2} = -\tfrac18r^2e^{-r/2} = -\tfrac18u$.

**Memahami hasil.** $E = -\tfrac18$ hartree $= -3{,}40$ eV, energi $n = 2$ dalam model Bohr. Suku-suku konstan dan suku sebanding $r$ saling meniadakan, persis seperti $1/r$ meniadakan pada $e^{-r}$ (Contoh 2.53). Fungsi ini adalah orbital $2p_z$ yang belum dinormalisasi.
:::

::: {.contoh}
**Contoh 7.5 · Bentuk $u$ di dekat inti**

Tunjukkan bahwa di dekat inti, $u \propto r^{\ell+1}$, sehingga $R \propto r^\ell$. Apa akibatnya bagi kerapatan elektron di inti?

**Penyelesaian.** Untuk $r \to 0$, suku sentrifugal $\ell(\ell+1)/2r^2$ mendominasi (7.6), sehingga $u'' \approx \ell(\ell+1)u/r^2$. Coba $u = r^s$: $s(s - 1) = \ell(\ell + 1)$, jadi $s = \ell + 1$ atau $s = -\ell$. Penyelesaian $r^{-\ell}$ membuat $R$ tak hingga (atau, untuk $\ell = 0$, membuat $\nabla^2\psi$ memuat fungsi delta), sehingga ditolak. Jadi $u \propto r^{\ell+1}$ dan $|\psi|^2 \propto r^{2\ell}$ di dekat inti.

**Memahami hasil.** Hanya orbital s ($\ell = 0$) yang mempunyai rapat peluang tidak nol di inti. Fakta ini sangat penting dalam kimia: interaksi kontak Fermi antara elektron dan spin inti (sumber garis 21 cm hidrogen dan kopling hiperhalus dalam EPR, Bab 16), pergeseran isotop karena ukuran inti, dan penangkapan elektron oleh inti radioaktif semuanya hanya melibatkan elektron s.
:::

::: {.contoh}
**Contoh 7.6 · Bilangan kuantum yang diizinkan**

Daftarkan semua kombinasi $(n, \ell, m_\ell)$ untuk $n = 3$ dan beri nama orbitalnya.

**Penyelesaian.** $\ell = 0$: $m = 0$ (3s). $\ell = 1$: $m = -1, 0, 1$ (tiga orbital 3p). $\ell = 2$: $m = -2, \ldots, 2$ (lima orbital 3d). Total $1 + 3 + 5 = 9 = n^2$.

**Memahami hasil.** Kulit ke-$n$ mempunyai $n^2$ orbital dan, dengan dua keadaan spin, $2n^2$ elektron: 2, 8, 18, 32. Dalam atom hidrogen, kesembilan orbital $n = 3$ berenergi sama (subbab 7.4); dalam atom berelektron banyak, 3s < 3p < 3d, dan 3d bahkan naik di atas 4s untuk kalium dan kalsium (Bab 9).
:::

::: {.kuis}
**Kuis cepat 7.2**

Mengapa persamaan radial tidak bergantung pada $m_\ell$? Berapa banyak orbital dengan $n = 4$?
:::

## 7.3 Persamaan radial dan penyelesaiannya

### Perilaku asimtotik

Untuk keadaan terikat, $E < 0$. Tulis $E = -\kappa^2/2$ dengan $\kappa > 0$. Jauh dari inti, kedua suku potensial dalam (7.6) hilang, dan $u'' \approx \kappa^2u$, dengan penyelesaian $e^{\pm\kappa r}$. Hanya $e^{-\kappa r}$ yang dapat dinormalisasi. Di dekat inti, $u \propto r^{\ell+1}$ (Contoh 7.5). Seperti pada osilator harmonik (subbab 5.2), kita pisahkan kedua perilaku itu:

$$
u(r) = r^{\ell+1}e^{-\kappa r}f(r) , \qquad \text{(7.7)}
$$

dan berharap $f$ adalah fungsi yang lebih sederhana.

### Persamaan untuk $f$ dan rekursi

Turunkan (7.7) dua kali dan masukkan ke (7.6). Setelah membagi dengan $r^\ell e^{-\kappa r}$, semua suku $1/r^2$ saling meniadakan (karena eksponen $\ell + 1$ dipilih tepat), dan tersisa

$$
rf'' + 2(\ell + 1 - \kappa r)f' + 2[Z - \kappa(\ell + 1)]f = 0 . \qquad \text{(7.8)}
$$

Coba deret pangkat $f = \sum_ka_kr^k$. Suku-suku berpangkat $r^k$ memberi

$$
a_{k+1} = \frac{2[\kappa(k + \ell + 1) - Z]}{(k + 1)(k + 2\ell + 2)}\,a_k . \qquad \text{(7.9)}
$$

### Deret harus berhenti

Untuk $k$ besar, $a_{k+1}/a_k \to 2\kappa/k$, sama dengan perbandingan koefisien deret $e^{2\kappa r}$. Bila deret tidak berhenti, $f \sim e^{2\kappa r}$ dan $u \sim e^{+\kappa r}$: fungsi meledak dan tidak dapat dinormalisasi, persis seperti pada osilator harmonik. Jadi deret harus berhenti pada suatu $k = k_\text{maks}$, yaitu pembilang (7.9) harus nol:

$$
\kappa(k_\text{maks} + \ell + 1) = Z .
$$

Definisikan $n = k_\text{maks} + \ell + 1$. Karena $k_\text{maks} = 0, 1, 2, \ldots$ dan $\ell = 0, 1, 2, \ldots$, $n$ adalah bilangan bulat positif dengan $n \ge \ell + 1$. Maka $\kappa = Z/n$ dan

$$
\boxed{\ E_n = -\frac{\kappa^2}{2} = -\frac{Z^2}{2n^2}\ E_h, \qquad n = 1, 2, 3, \ldots, \qquad \ell = 0, 1, \ldots, n - 1\ } \qquad \text{(7.10)}
$$

Inilah rumus Bohr (subbab 1.6), kini diperoleh dari syarat kenormalan, bukan dari postulat orbit. Polinom $f$ berderajat $n - \ell - 1$ dan, dengan normalisasi yang sesuai, adalah polinom **Laguerre terasosiasi** $L_{n-\ell-1}^{2\ell+1}(2Zr/n)$.

### Fungsi radial

Fungsi radial ternormalisasi untuk $n \le 3$ (dengan $\rho = Zr$, dalam satuan atom):

| Orbital | $R_{n\ell}(r)$ |
|---|---|
| 1s | $2Z^{3/2}e^{-\rho}$ |
| 2s | $\dfrac{Z^{3/2}}{2\sqrt2}(2 - \rho)e^{-\rho/2}$ |
| 2p | $\dfrac{Z^{3/2}}{2\sqrt6}\,\rho\,e^{-\rho/2}$ |
| 3s | $\dfrac{2Z^{3/2}}{81\sqrt3}(27 - 18\rho + 2\rho^2)e^{-\rho/3}$ |
| 3p | $\dfrac{4Z^{3/2}}{81\sqrt6}(6 - \rho)\,\rho\,e^{-\rho/3}$ |
| 3d | $\dfrac{4Z^{3/2}}{81\sqrt{30}}\,\rho^2e^{-\rho/3}$ |

Fungsi gelombang lengkap adalah $\psi_{n\ell m} = R_{n\ell}(r)Y_\ell^m(\theta, \phi)$.

::: {.dalam}
**Menurunkan persamaan untuk $f$**

Dari $u = r^{\ell+1}e^{-\kappa r}f$: $u' = r^{\ell+1}e^{-\kappa r}\left[f' + \left(\tfrac{\ell+1}{r} - \kappa\right)f\right]$ dan
$$
u'' = r^{\ell+1}e^{-\kappa r}\left[f'' + 2\left(\tfrac{\ell+1}{r} - \kappa\right)f' + \left(\left(\tfrac{\ell+1}{r} - \kappa\right)^2 - \tfrac{\ell+1}{r^2}\right)f\right] .
$$
Suku dalam kurung terakhir sama dengan $\tfrac{\ell(\ell+1)}{r^2} - \tfrac{2\kappa(\ell+1)}{r} + \kappa^2$. Persamaan (7.6) dikali $-2$ berbunyi $u'' = \left[\tfrac{\ell(\ell+1)}{r^2} - \tfrac{2Z}{r} + \kappa^2\right]u$. Suku $\ell(\ell+1)/r^2$ dan $\kappa^2$ di kedua ruas sama, sehingga tersisa $f'' + 2\left(\tfrac{\ell+1}{r} - \kappa\right)f' + \tfrac{2[Z - \kappa(\ell+1)]}{r}f = 0$. Kalikan dengan $r$: (7.8). Memasukkan $f = \sum a_kr^k$ dan mengumpulkan koefisien $r^k$: $(k+1)k\,a_{k+1} + 2(\ell+1)(k+1)a_{k+1} - 2\kappa k\,a_k + 2[Z - \kappa(\ell+1)]a_k = 0$, yang memberi (7.9).
:::

::: {.contoh}
**Contoh 7.7 · Membangun $R_{20}$ dari rekursi**

Dengan $Z = 1$, $n = 2$, $\ell = 0$ ($\kappa = \tfrac12$), bangun $f$ dari (7.9) mulai $a_0 = 1$, lalu tuliskan $R_{20}$ tanpa normalisasi.

**Penyelesaian.** $a_1 = \tfrac{2[\tfrac12(0 + 1) - 1]}{(1)(2)}a_0 = -\tfrac12$. $a_2 = \tfrac{2[\tfrac12(2) - 1]}{(2)(3)}a_1 = 0$. Jadi $f = 1 - \tfrac r2$, $u = r(1 - \tfrac r2)e^{-r/2}$, $R = u/r = (1 - \tfrac r2)e^{-r/2} = \tfrac12(2 - r)e^{-r/2}$.

**Memahami hasil.** Sebanding dengan $R_{20}$ di tabel. Satu simpul radial di $r = 2$ bohr, sesuai $n - \ell - 1 = 1$. Pembilang rekursi menjadi nol pada $k = 1$, tepat ketika $\kappa(k + \ell + 1) = \tfrac12 \cdot 2 = Z$.
:::

::: {.contoh}
**Contoh 7.8 · Fungsi 3p dari rekursi**

Untuk $n = 3$, $\ell = 1$ ($\kappa = \tfrac13$), bangun $f$ dan bandingkan dengan $R_{31}$.

**Penyelesaian.** $a_1 = \tfrac{2[\tfrac13(2) - 1]}{(1)(4)}a_0 = -\tfrac16a_0$; $a_2 = \tfrac{2[\tfrac13(3) - 1]}{(2)(5)}a_1 = 0$. Jadi $f = 1 - \tfrac r6$, $u = r^2(1 - \tfrac r6)e^{-r/3}$, $R = r(1 - \tfrac r6)e^{-r/3} = \tfrac16r(6 - r)e^{-r/3}$.

**Memahami hasil.** Sebanding dengan $R_{31} \propto (6 - \rho)\rho e^{-\rho/3}$. Simpul radial di $r = 6$ bohr, ditambah "simpul" di inti yang berasal dari faktor $r^\ell$ (bukan simpul radial dalam hitungan, karena ada pada setiap orbital dengan $\ell > 0$).
:::

::: {.contoh}
**Contoh 7.9 · Bagaimana bila $E$ bukan nilai eigen?**

Misalkan $Z = 1$, $\ell = 0$, dan $\kappa = 0{,}9$ (bukan $1/n$). Hitung lima koefisien pertama dan perhatikan perbandingan $a_{k+1}/a_k$.

**Penyelesaian.** Dengan (7.9): $a_{k+1}/a_k = \tfrac{2[0{,}9(k + 1) - 1]}{(k + 1)(k + 2)}$. $k = 0$: $-0{,}1$; $k = 1$: $0{,}267$; $k = 2$: $0{,}283$; $k = 3$: $0{,}26$; $k = 4$: $0{,}233$. Untuk $k$ besar, perbandingannya mendekati $1{,}8/k$, yaitu $2\kappa/k$.

**Memahami hasil.** Koefisien tidak pernah menjadi nol, dan deretnya tumbuh seperti $e^{1{,}8r}$, sehingga $u \sim e^{+0{,}9r}$. Fungsi itu memenuhi persamaan diferensial di setiap titik tetapi meledak di tak hingga. Hanya energi $-1/2n^2$ yang menghasilkan fungsi yang dapat diterima. Inilah yang "dilihat" metode tembak numerik (subbab 7.13, Gambar 7.6).
:::

::: {.kuis}
**Kuis cepat 7.3**

Berapa derajat polinom $f$ untuk orbital 4d? Untuk $n = 1$, $\ell$ berapa saja yang diizinkan, dan mengapa?
:::
