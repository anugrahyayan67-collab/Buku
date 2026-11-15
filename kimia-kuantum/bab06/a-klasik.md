# Bab 6 Momentum Sudut dan Rotor Tegar

Di antara bintang-bintang terdapat awan gas dingin, bersuhu hanya sekitar 10 K, yang terlalu gelap untuk dilihat dengan teleskop optik. Namun teleskop radio menangkap pancaran yang sangat tajam dari awan itu pada frekuensi 115,271 GHz, atau panjang gelombang 2,6 mm. Dari satu angka itu, astronom tahu bahwa pemancarnya adalah molekul karbon monoksida, bahwa panjang ikatannya 113 pm, dan bahwa di awan tersebut sedang terbentuk bintang-bintang baru. Lebih dari dua ratus jenis molekul telah dikenali di ruang antarbintang dengan cara ini, dari H₂O dan NH₃ sampai molekul organik dengan belasan atom. Bagaimana sebuah frekuensi dapat menjadi sidik jari molekul, dan bagaimana ia dapat memberi tahu panjang ikatan sampai ketelitian seperseribu pikometer?

Jawabannya adalah **kuantisasi momentum sudut**. Molekul yang berputar tidak dapat berputar sembarang cepat; momentum sudutnya hanya boleh bernilai $\sqrt{J(J+1)}\,\hbar$ dengan $J$ bilangan bulat, dan energi rotasinya membentuk tangga $BJ(J+1)$ yang anak tangganya ditentukan oleh momen inersia. Frekuensi transisi antar anak tangga karena itu langsung memberikan momen inersia, dan dari situ panjang ikatan.

Momentum sudut jauh lebih luas daripada rotasi molekul. Matematika yang sama, harmonik bola $Y_\ell^m(\theta, \phi)$, menjadi bagian sudut setiap orbital atom: orbital s, p, d, dan f tidak lain adalah harmonik bola dengan $\ell = 0$, 1, 2, dan 3. Aturan seleksi spektroskopi, struktur tabel periodik, kopling spin, dan efek medan magnet semuanya berakar pada aljabar momentum sudut yang dikembangkan dalam bab ini.

::: {.strategi}
**Pertanyaan pembuka**

1. Mengapa momentum sudut terkuantisasi, padahal tidak ada dinding yang membatasi gerak melingkar?
2. Mengapa orbital p ada tiga, orbital d ada lima, dan orbital f ada tujuh?
3. Apa arti "kuantisasi ruang", dan mengapa vektor momentum sudut tidak pernah tepat sejajar dengan sumbu $z$?
4. Mengapa garis-garis spektrum rotasi molekul diatom berjarak hampir sama, dan bagaimana panjang ikatan dibaca dari jarak itu?
5. Mengapa hidrogen terdiri atas dua jenis molekul, orto dan para, yang dapat dipisahkan? (Dasar lengkapnya, partikel identik dan teorema spin–statistik, dibahas di subbab 9.3.)
:::

::: {.tujuan}
**Tujuan belajar**

Setelah mempelajari bab ini, kamu mampu:

1. Menghitung momentum sudut klasik dan menghubungkannya dengan energi rotasi dan momen inersia.
2. Menurunkan operator momentum sudut dalam koordinat Kartesius dan bola, serta komutatornya.
3. Menyelesaikan masalah partikel pada cincin dan menerapkannya pada elektron π molekul siklik.
4. Menyelesaikan masalah partikel pada bola dengan pemisahan variabel dan memperoleh harmonik bola.
5. Menuliskan, menormalisasi, dan menggambar harmonik bola, termasuk bentuk riilnya (orbital p dan d).
6. Menjelaskan kuantisasi ruang dengan model vektor dan menghitung sudut-sudut yang diizinkan.
7. Menurunkan nilai eigen momentum sudut dengan operator tangga, termasuk kemungkinan nilai setengah bulat.
8. Memisahkan masalah dua benda menjadi gerak pusat massa dan gerak relatif, serta menghitung efek massa tereduksi.
9. Menghitung tingkat energi rotor tegar dan tetapan rotasi molekul diatom.
10. Menurunkan aturan seleksi rotasi dan menafsirkan spektrum gelombang mikro untuk memperoleh panjang ikatan.
11. Menghitung populasi rotasi, fungsi partisi rotasi, dan efek statistik spin inti.
12. Menganalisis distorsi sentrifugal dan spektrum rotasi–getaran untuk memperoleh tetapan molekul.
:::

::: {.mat}
**Prasyarat**

Dari *Fisika Umum*: Bab 8 (gerak rotasi, momen inersia, momentum sudut). Dari buku ini: bilangan kompleks dan rumus Euler (subbab 2.1), koordinat bola dan Laplasian (subbab 2.5, persamaan 2.23), deret pangkat dan persamaan Legendre (subbab 2.4), operator, komutator, dan fungsi eigen bersama (Bab 4), operator tangga osilator (subbab 5.6), dan massa tereduksi (subbab 5.1 dan 5.7).
:::

## 6.1 Momentum sudut klasik

### Definisi

Partikel bermassa $m$ di posisi $\mathbf r$ dengan momentum $\mathbf p$ mempunyai **momentum sudut** terhadap titik asal

$$
\mathbf L = \mathbf r \times \mathbf p, \qquad L_x = yp_z - zp_y, \quad L_y = zp_x - xp_z, \quad L_z = xp_y - yp_x . \qquad \text{(6.1)}
$$

$\mathbf L$ tegak lurus pada bidang yang dibentuk $\mathbf r$ dan $\mathbf p$, dan besarnya $L = rp\sin\alpha$, dengan $\alpha$ sudut antara keduanya. Untuk gerak melingkar berjari-jari $r$ dengan kecepatan sudut $\omega$, $p = m\omega r$ tegak lurus $\mathbf r$, sehingga $L = mr^2\omega = I\omega$, dengan $I = mr^2$ **momen inersia**.

### Kekekalan dan energi rotasi

Laju perubahan momentum sudut adalah torsi: $d\mathbf L/dt = \mathbf r \times \mathbf F$. Bila gaya bersifat **sentral** (searah $\mathbf r$, seperti gaya Coulomb inti pada elektron atau gaya antara dua atom dalam molekul diatom), torsinya nol dan $\mathbf L$ kekal. Inilah alasan mengapa momentum sudut begitu penting dalam fisika atom: dalam atom, gaya inti pada elektron adalah gaya sentral, sehingga momentum sudut menjadi besaran yang "baik", yang nilainya dapat dipakai untuk melabeli keadaan.

Energi kinetik benda berotasi dapat ditulis dengan momentum sudut:

$$
E_\text{rot} = \tfrac12I\omega^2 = \frac{L^2}{2I} . \qquad \text{(6.2)}
$$

Bentuk ini sejajar dengan $E = p^2/2m$ untuk translasi: $L$ menggantikan $p$ dan $I$ menggantikan $m$. Dalam mekanika kuantum, kita cukup mengetahui nilai yang diizinkan untuk $L^2$ untuk memperoleh tingkat energi rotasi.

### Momentum sudut dan momen magnet

Muatan yang berputar adalah arus melingkar, dan arus melingkar mempunyai momen magnet. Untuk partikel bermuatan $q$ dan bermassa $m$ pada orbit melingkar, arusnya $q\omega/2\pi$ dan luas orbit $\pi r^2$, sehingga momen magnetnya $\mu = q\omega r^2/2 = (q/2m)L$. Untuk elektron ($q = -e$):

$$
\boldsymbol\mu = -\frac{e}{2m_e}\mathbf L . \qquad \text{(6.3)}
$$

Perbandingan $\mu/L$ ini disebut **rasio giromagnetik**. Karena momentum sudut terkuantisasi dalam satuan $\hbar$, momen magnet orbital elektron terkuantisasi dalam satuan **magneton Bohr** $\mu_B = e\hbar/2m_e = 9{,}274 \times 10^{-24}$ J/T. Hubungan ini adalah dasar efek Zeeman (Bab 7) dan resonansi magnetik (Bab 16).

::: {.contoh}
**Contoh 6.1 · Komponen momentum sudut**

Partikel bermassa 2,0 kg berada di $\mathbf r = (1{,}0;\ 2{,}0;\ 0)$ m dengan kecepatan $\mathbf v = (0;\ 1{,}0;\ 3{,}0)$ m/s. Hitung $\mathbf L$ dan besarnya.

**Penyelesaian.** $\mathbf p = (0;\ 2{,}0;\ 6{,}0)$ kg m/s. $L_x = yp_z - zp_y = (2{,}0)(6{,}0) - 0 = 12$; $L_y = zp_x - xp_z = 0 - (1{,}0)(6{,}0) = -6{,}0$; $L_z = xp_y - yp_x = (1{,}0)(2{,}0) - 0 = 2{,}0$ (semua dalam kg m²/s). $|\mathbf L| = \sqrt{144 + 36 + 4} = 13{,}6$ kg m²/s.

**Memahami hasil.** Ketiga komponen dapat diketahui serentak dalam fisika klasik. Dalam mekanika kuantum tidak demikian: komponen-komponen $\hat L_x$, $\hat L_y$, dan $\hat L_z$ tidak komut satu sama lain (subbab 6.2), sehingga paling banyak satu komponen dapat tajam bersama besarnya.
:::

::: {.contoh}
**Contoh 6.2 · Molekul CO yang berputar**

Momen inersia CO adalah $1{,}456 \times 10^{-46}$ kg m². Di subbab 6.9 kita akan melihat bahwa molekul CO pada tingkat rotasi $J = 7$ (tingkat terpadat pada suhu kamar) mempunyai $L = \sqrt{J(J+1)}\,\hbar = \sqrt{56}\,\hbar$. Hitung kecepatan sudut, periode putaran, dan energi rotasinya.

**Penyelesaian.** $L = 7{,}483 \times 1{,}0546 \times 10^{-34} = 7{,}89 \times 10^{-34}$ J s. $\omega = L/I = 5{,}42 \times 10^{12}$ rad/s, periode $2\pi/\omega = 1{,}16$ ps. $E = L^2/2I = 2{,}14 \times 10^{-21}$ J $= 108$ cm⁻¹.

**Memahami hasil.** Molekul CO berputar hampir satu triliun kali tiap detik, tetapi masih sekitar 75 kali lebih lambat daripada getaran ikatannya (periode 15,6 fs). Perbedaan skala waktu ini yang memungkinkan rotasi dan getaran diperlakukan terpisah dalam pendekatan pertama. Energi 108 cm⁻¹ sebanding dengan $kT = 207$ cm⁻¹, sesuai dengan ekuipartisi: rata-rata $kT$ untuk dua derajat kebebasan rotasi.
:::

::: {.contoh}
**Contoh 6.3 · Momen magnet orbit Bohr**

Pada orbit Bohr pertama, elektron mempunyai $L = \hbar$. Hitung momen magnetnya dan energi interaksinya dalam medan 1 T. Bandingkan dengan $kT$ pada 298 K.

**Penyelesaian.** $\mu = e\hbar/2m_e = 9{,}274 \times 10^{-24}$ J/T. Energi $\mu B = 9{,}27 \times 10^{-24}$ J $= 0{,}467$ cm⁻¹ $= 5{,}79 \times 10^{-5}$ eV. Dibandingkan dengan $kT = 4{,}12 \times 10^{-21}$ J, perbandingannya $2{,}3 \times 10^{-3}$.

**Memahami hasil.** Energi magnetik elektron dalam medan laboratorium sangat kecil dibandingkan energi termal, sehingga keterarahan momen magnet hanya beberapa per seribu. Itulah sebabnya kemagnetan paramagnet lemah dan menurun dengan suhu (hukum Curie), dan mengapa spektroskopi resonansi magnetik (Bab 16) bekerja dengan selisih populasi yang kecil.
:::

::: {.kuis}
**Kuis cepat 6.1**

Mengapa momentum sudut elektron terhadap inti kekal dalam atom hidrogen, tetapi tidak kekal terhadap inti tertentu dalam molekul H₂⁺?
:::

## 6.2 Operator momentum sudut dan komutatornya

### Operator Kartesius

Dengan aturan penggantian $p_x \to -i\hbar\,\partial/\partial x$ (Bab 4), definisi (6.1) menjadi

$$
\hat L_x = -i\hbar\left(y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y}\right), \quad \hat L_y = -i\hbar\left(z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z}\right), \quad \hat L_z = -i\hbar\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right) . \qquad \text{(6.4)}
$$

Tidak ada masalah urutan di sini: $y$ dan $\hat p_z$ komut, sehingga $y\hat p_z = \hat p_zy$. Kuadrat besarnya adalah $\hat L^2 = \hat L_x^2 + \hat L_y^2 + \hat L_z^2$.

### Komutator

Hitung $[\hat L_x, \hat L_y]$ dengan memakai $[x, \hat p_x] = i\hbar$ dan komutator lain yang nol. Tulis $\hat L_x = y\hat p_z - z\hat p_y$ dan $\hat L_y = z\hat p_x - x\hat p_z$:

$$
[\hat L_x, \hat L_y] = [y\hat p_z, z\hat p_x] - [y\hat p_z, x\hat p_z] - [z\hat p_y, z\hat p_x] + [z\hat p_y, x\hat p_z] .
$$

Suku kedua nol (tidak ada pasangan $x$–$\hat p_x$, $y$–$\hat p_y$, atau $z$–$\hat p_z$ yang bertemu), demikian juga suku ketiga. Suku pertama: $[y\hat p_z, z\hat p_x] = y[\hat p_z, z]\hat p_x = y(-i\hbar)\hat p_x$. Suku keempat: $[z\hat p_y, x\hat p_z] = x[z, \hat p_z]\hat p_y = x(i\hbar)\hat p_y$. Jumlahnya $i\hbar(x\hat p_y - y\hat p_x) = i\hbar\hat L_z$. Dengan permutasi siklis:

$$
\boxed{\ [\hat L_x, \hat L_y] = i\hbar\hat L_z, \qquad [\hat L_y, \hat L_z] = i\hbar\hat L_x, \qquad [\hat L_z, \hat L_x] = i\hbar\hat L_y\ } \qquad \text{(6.5)}
$$

Komponen-komponen momentum sudut **tidak komut**, sehingga tidak ada keadaan (selain $\mathbf L = 0$) dengan dua komponen tajam sekaligus. Tetapi setiap komponen komut dengan kuadrat besarnya:

$$
[\hat L^2, \hat L_x] = [\hat L^2, \hat L_y] = [\hat L^2, \hat L_z] = 0 . \qquad \text{(6.6)}
$$

Buktinya untuk $\hat L_z$: $[\hat L_x^2, \hat L_z] = \hat L_x[\hat L_x, \hat L_z] + [\hat L_x, \hat L_z]\hat L_x = -i\hbar(\hat L_x\hat L_y + \hat L_y\hat L_x)$, dan $[\hat L_y^2, \hat L_z] = i\hbar(\hat L_y\hat L_x + \hat L_x\hat L_y)$; jumlahnya nol, dan $[\hat L_z^2, \hat L_z] = 0$. Jadi kita dapat mencari fungsi eigen bersama $\hat L^2$ dan **satu** komponen, yang menurut konvensi dipilih $\hat L_z$.

### Bentuk dalam koordinat bola

Dengan aturan rantai seperti di Contoh 4.7, operator-operator itu dapat ditulis dalam $(r, \theta, \phi)$. Hasilnya tidak memuat $r$ sama sekali:

$$
\hat L_z = -i\hbar\frac{\partial}{\partial\phi}, \qquad \hat L^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right] . \qquad \text{(6.7)}
$$

Bandingkan dengan Laplasian dalam koordinat bola (persamaan 2.23): bagian sudutnya tepat $-\hat L^2/\hbar^2r^2$. Jadi

$$
\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) - \frac{\hat L^2}{\hbar^2r^2} . \qquad \text{(6.8)}
$$

Energi kinetik partikel dalam tiga dimensi terbagi menjadi bagian radial dan bagian rotasi $\hat L^2/2mr^2$, persis seperti $L^2/2I$ dalam (6.2). Untuk potensial sentral $V(r)$, $\hat L^2$ dan $\hat L_z$ komut dengan Hamiltonian, sehingga keadaan stasioner dapat dilabeli dengan nilai eigen keduanya. Inilah alasan mengapa orbital atom diberi label $\ell$ dan $m$.

::: {.dalam}
**Menurunkan $\hat L^2$ dalam koordinat bola**

Satu jalan: tuliskan $\hat L_x$ dan $\hat L_y$ dengan aturan rantai seperti $\hat L_z$ di Contoh 4.7. Hasilnya
$$
\hat L_x = i\hbar\left(\sin\phi\,\partial_\theta + \cot\theta\cos\phi\,\partial_\phi\right), \qquad \hat L_y = i\hbar\left(-\cos\phi\,\partial_\theta + \cot\theta\sin\phi\,\partial_\phi\right) .
$$
Kuadratkan masing-masing (hati-hati: $\partial_\theta$ bekerja pada $\cot\theta$, dan $\partial_\phi$ bekerja pada $\sin\phi$ dan $\cos\phi$), lalu jumlahkan. Suku-suku silang saling menghapus karena $\sin^2\phi + \cos^2\phi = 1$, dan yang tersisa adalah $\hat L_x^2 + \hat L_y^2 = -\hbar^2(\partial_\theta^2 + \cot\theta\,\partial_\theta + \cot^2\theta\,\partial_\phi^2)$. Tambahkan $\hat L_z^2 = -\hbar^2\partial_\phi^2$ dan pakai $1 + \cot^2\theta = 1/\sin^2\theta$ serta $\partial_\theta^2 + \cot\theta\,\partial_\theta = \tfrac{1}{\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta)$. Hasilnya (6.7). Jalan yang lebih pendek: bandingkan Laplasian (2.23) dengan $\nabla^2 = \hat p^2/(-\hbar^2)$ dan identitas klasik $p^2 = p_r^2 + L^2/r^2$.
:::

::: {.contoh}
**Contoh 6.4 · Fungsi eigen $\hat L^2$ dan $\hat L_z$**

Tunjukkan bahwa $f = \sin\theta\,e^{i\phi}$ adalah fungsi eigen $\hat L_z$ dan $\hat L^2$. Berapa nilai eigennya?

**Penyelesaian.** $\hat L_zf = -i\hbar(i)\sin\theta\,e^{i\phi} = \hbar f$. Untuk $\hat L^2$: $\partial_\theta f = \cos\theta\,e^{i\phi}$, sehingga $\tfrac{1}{\sin\theta}\partial_\theta(\sin\theta\cos\theta)e^{i\phi} = \tfrac{\cos^2\theta - \sin^2\theta}{\sin\theta}e^{i\phi}$. Bagian $\phi$: $\tfrac{1}{\sin^2\theta}\partial_\phi^2f = -\tfrac{1}{\sin\theta}e^{i\phi}$. Jumlahnya $\tfrac{\cos^2\theta - \sin^2\theta - 1}{\sin\theta}e^{i\phi} = \tfrac{-2\sin^2\theta}{\sin\theta}e^{i\phi} = -2f$. Jadi $\hat L^2f = 2\hbar^2f$.

**Memahami hasil.** Nilai eigen $L^2 = 2\hbar^2 = \ell(\ell+1)\hbar^2$ dengan $\ell = 1$, dan $L_z = \hbar$, jadi $m = 1$. Fungsi ini adalah bagian sudut orbital $p_{+1}$. Perhatikan bahwa $L = \sqrt2\,\hbar$, bukan $\hbar$: besar momentum sudut selalu lebih besar daripada komponen $z$ maksimumnya.
:::

::: {.contoh}
**Contoh 6.5 · Komutator momentum sudut dengan posisi**

Hitung $[\hat L_z, x]$, $[\hat L_z, y]$, dan $[\hat L_z, z]$. Apa makna hasilnya?

**Penyelesaian.** $[\hat L_z, x] = [x\hat p_y - y\hat p_x, x] = -y[\hat p_x, x] = -y(-i\hbar) = i\hbar y$. Dengan cara yang sama, $[\hat L_z, y] = [x\hat p_y, y] = x(-i\hbar) = -i\hbar x$, dan $[\hat L_z, z] = 0$.

**Memahami hasil.** $\hat L_z$ "memutar" $x$ menjadi $y$ dan $y$ menjadi $-x$: inilah aksi rotasi infinitesimal terhadap sumbu $z$, dan $z$ tidak berubah. Momentum sudut adalah **pembangkit rotasi**, seperti momentum adalah pembangkit translasi (soal ★ Bab 4). Hasil ini akan menghasilkan aturan seleksi $\Delta m = 0, \pm1$ untuk transisi dipol (subbab 6.10 dan Bab 7).
:::

::: {.contoh}
**Contoh 6.6 · Bagian sudut Laplasian**

Gunakan (6.8) untuk menghitung $\nabla^2$ dari $f = r\cos\theta$ (yaitu $z$) dan periksa dengan koordinat Kartesius.

**Penyelesaian.** Bagian radial: $\tfrac{1}{r^2}\partial_r(r^2\cos\theta) = \tfrac{2\cos\theta}{r}$. Bagian sudut: $\hat L^2\cos\theta = 2\hbar^2\cos\theta$ (fungsi $\ell = 1$, $m = 0$), sehingga $-\tfrac{\hat L^2}{\hbar^2r^2}(r\cos\theta) = -\tfrac{2\cos\theta}{r}$. Jumlahnya nol. Dalam Kartesius, $\nabla^2z = 0$ jelas.

**Memahami hasil.** Fungsi $r^\ell Y_\ell^m$ selalu memenuhi $\nabla^2f = 0$ (fungsi harmonik): suku radial $\ell(\ell+1)r^{\ell-2}$ tepat dibatalkan oleh suku sudut. Inilah asal nama **harmonik bola**: harmonik bola adalah bagian sudut polinom homogen $x$, $y$, $z$ berderajat $\ell$ yang memenuhi persamaan Laplace. Orbital $p_z \propto z$ dan $d_{xy} \propto xy$ adalah contohnya.
:::

::: {.contoh}
**Contoh 6.7 · Mengapa $\hat L$ komut dengan Hamiltonian atom**

Tunjukkan bahwa untuk $\hat H = -\tfrac{\hbar^2}{2m}\nabla^2 + V(r)$, berlaku $[\hat H, \hat L_z] = 0$ dan $[\hat H, \hat L^2] = 0$.

**Penyelesaian.** Dengan (6.8), $\nabla^2$ terdiri atas bagian radial (yang tidak menyentuh $\theta$ dan $\phi$) dan $-\hat L^2/\hbar^2r^2$. Operator $\hat L_z = -i\hbar\partial_\phi$ dan $\hat L^2$ hanya memuat sudut, sehingga komut dengan setiap fungsi $r$ dan dengan $\partial_r$. Keduanya juga komut dengan $\hat L^2$ menurut (6.6). Jadi setiap suku $\hat H$ komut dengan $\hat L_z$ dan $\hat L^2$.

**Memahami hasil.** Komutasi dengan Hamiltonian adalah versi kuantum dari kekekalan (teorema Ehrenfest, subbab 4.6). Untuk potensial sentral, $\ell$ dan $m$ adalah "bilangan kuantum yang baik", dan keadaan stasioner dapat dipilih sebagai fungsi eigen bersama $\hat H$, $\hat L^2$, dan $\hat L_z$. Dalam molekul, simetri bola hilang; untuk molekul linear, hanya $\hat L_z$ terhadap sumbu molekul yang tetap komut, dan bilangan kuantumnya ($\lambda = 0, \pm1, \ldots$, dengan lambang σ, π, δ) menjadi label orbital molekul diatom (Bab 11).
:::

::: {.kuis}
**Kuis cepat 6.2**

Bila $L_z$ suatu keadaan tajam, apakah $L_x$ dapat tajam juga? Apakah $L^2$ dapat tajam juga? Mengapa $\hat L^2$ tidak memuat $r$?
:::
