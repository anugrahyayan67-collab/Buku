# Ringkasan Bab 2

| Gagasan | Rumus | Subbab |
|---|---|---|
| Bilangan kompleks | $z = x + iy = re^{i\theta}$; $\ z^*z = |z|^2$ | 2.1 |
| Rumus Euler | $e^{i\theta} = \cos\theta + i\sin\theta$; $\ \cos\theta = (e^{i\theta} + e^{-i\theta})/2$ | 2.1 |
| Akar satuan | $z_k = e^{2\pi ik/N}$, $k = 0, \ldots, N - 1$ | 2.1 |
| Integral eksponen | $\int_0^\infty x^ne^{-ax}\,dx = n!/a^{n+1}$ | 2.2 |
| Integral Gauss | $\int e^{-ax^2}dx = \sqrt{\pi/a}$; $\ \int x^2e^{-ax^2}dx = \tfrac{1}{2a}\sqrt{\pi/a}$ | 2.2 |
| Integral parsial | $\int_a^bfg'\,dx = [fg]_a^b - \int_a^bf'g\,dx$ | 2.2 |
| Paritas | integral fungsi ganjil pada selang simetris $= 0$ | 2.2 |
| PD orde dua koefisien tetap | $y = e^{sx}$, $s^2 + ps + q = 0$ | 2.3 |
| Berayun / meluruh | $y'' = -k^2y$: $\sin kx, \cos kx$; $\ y'' = \kappa^2y$: $e^{\pm\kappa x}$ | 2.3 |
| Kuantisasi dari syarat batas | $y(0) = y(L) = 0 \Rightarrow k = n\pi/L$ | 2.3 |
| Persamaan Hermite | $a_{k+2} = 2(k - \nu)a_k/[(k + 2)(k + 1)]$; deret berhenti bila $\nu = n$ | 2.4 |
| Koordinat bola | $d\tau = r^2\sin\theta\,dr\,d\theta\,d\phi$; $\ \int f(r)\,d\tau = 4\pi\int f r^2dr$ | 2.5 |
| Hasil kali dalam | $\langle f|g\rangle = \int f^*g\,d\tau$; $\ \langle\phi_m|\phi_n\rangle = \delta_{mn}$ | 2.6 |
| Ekspansi | $f = \sum c_n\phi_n$, $\ c_n = \langle\phi_n|f\rangle$ | 2.6 |
| Determinan | tukar dua baris → tanda berubah; dua baris sama → 0 | 2.7 |
| Sistem homogen | penyelesaian tak trivial $\iff \det\mathbf A = 0$ | 2.7 |
| Nilai eigen | $\mathbf{Ac} = \lambda\mathbf c$; $\ \det(\mathbf A - \lambda\mathbf I) = 0$; $\sum\lambda$ = teras | 2.8 |
| Matriks Hermitian | nilai eigen riil; vektor eigen ortogonal | 2.8 |
| Deret Taylor | $f(x) = \sum f^{(n)}(x_0)(x - x_0)^n/n!$; $\ k = V''(r_e)$ | 2.9 |
| Fourier | $\Delta x\,\Delta k \ge \tfrac12$; FID $e^{-t/T_2}$ ↔ lebar $1/\pi T_2$ | 2.9 |
| Statistik | $\langle x\rangle = \int xP\,dx$; $\ \sigma^2 = \langle x^2\rangle - \langle x\rangle^2$ | 2.10 |
| Satuan atom | $m_e = e = \hbar = 4\pi\varepsilon_0 = 1$; $1\,a_0 = 52{,}918$ pm; $1\,E_h = 27{,}211$ eV | 2.11 |

**Jawaban kuis cepat.** **2.1** (a) 1. (b) 0 (identitas Euler). (c) $|2 + i|^2\phi^2 = 5\phi^2$. **2.2** (a) $5! = 120$. (b) Tidak; integrannya tidak ganjil terhadap $x = 0$ karena fungsi Gauss bergeser ke $x = 1$ (nilainya $\sqrt\pi$). (c) $-b^2\sin(ax)\sin(by)$. **2.3** (a) $c_1e^{3x} + c_2e^{-3x}$. (b) $\cos kL = 0$, jadi $k = (n - \tfrac12)\pi/L$. **2.4** Untuk $\nu = 3$ hanya deret ganjil yang berhenti; deret genap dengan $a_0 \ne 0$ tidak berhenti, tumbuh seperti $e^{x^2}$, dan fungsi gelombangnya tidak dapat dinormalisasi. **2.5** (a) $4\pi$, luas permukaan bola satuan (sudut ruang penuh). (b) Karena volume kulit $4\pi r^2dr$ menuju nol di inti. **2.6** (a) Ya pada $[0, 2\pi]$; tidak pada $[0, \pi/2]$ ($\int = 1/2$). (b) Ya: $0{,}36 + 0{,}64 = 1$. **2.7** (a) 1. (b) 0. (c) Ya: $A_{12} = 2i = (A_{21})^* = (-2i)^*$. **2.8** (a) 5 dengan $(1, 0)$ dan $-2$ dengan $(0, 1)$. (b) 3. **2.9** (a) $1 - x^2/2 + x^4/24$; $\cos 0{,}2 \approx 0{,}980\,067$. (b) Lebar garis menjadi dua kali. **2.10** $\langle x\rangle = 5{,}0$; $\langle x^2\rangle = 25$; $\sigma = 0$. **2.11** (a) $-1/8 = -0{,}125\ E_h$. (b) 1,890 bohr. (c) 1.

# Pertanyaan

1. Mengapa fungsi gelombang boleh bernilai kompleks, sedangkan hasil pengukuran selalu riil? Besaran apa yang menghubungkan keduanya?
2. Apa beda faktor fase global dan fase relatif? Mana yang dapat diamati?
3. Mengapa bentuk eksponen kompleks $e^{ikx}$ lebih mudah dipakai daripada $\cos kx$ untuk menurunkan persamaan gelombang?
4. Mengapa pasangan akar satuan $e^{2\pi ik/N}$ dan $e^{-2\pi ik/N}$ menghasilkan tingkat energi Hückel yang terdegenerasi pada molekul siklik?
5. Mengapa integral parsial dalam mekanika kuantum hampir selalu mempunyai suku batas nol?
6. Faktor apa dalam elemen luas atau elemen volume yang membuat integral Gauss dan integral sudut orbital menjadi mudah?
7. Bagaimana paritas memungkinkan kita menyatakan sebuah integral nol tanpa menghitungnya? Beri contoh aturan seleksi.
8. Apa perbedaan mendasar antara masalah syarat awal dan masalah syarat batas? Mana yang menghasilkan kuantisasi?
9. Dalam metode deret pangkat untuk osilator harmonik, mengapa deret harus berhenti? Apa hubungannya dengan kuantisasi energi?
10. Mengapa fungsi distribusi radial orbital 1s nol di inti, padahal rapat peluangnya terbesar di sana?
11. Mengapa koordinat bola cocok untuk atom, dan koordinat silinder untuk molekul linear?
12. Dalam arti apa fungsi adalah vektor? Apa padanan hasil kali titik, panjang, dan komponen?
13. Mengapa ortonormalitas basis membuat koefisien ekspansi mudah dihitung?
14. Apa makna fisis integral tumpang tindih, dan mengapa nilainya tidak pernah melebihi satu (untuk fungsi ternormalisasi)?
15. Sifat determinan mana yang mewujudkan asas larangan Pauli?
16. Mengapa persamaan sekuler $\det(\mathbf H - E\mathbf S) = 0$ (Bab 8) muncul dari sistem persamaan linear homogen?
17. Mengapa besaran fisis dinyatakan oleh matriks Hermitian? Sebutkan dua sifat nilai dan vektor eigennya.
18. Apa yang dimaksud hampiran harmonik, dan suku deret Taylor mana yang diabaikan?
19. Mengapa sinyal yang meluruh cepat terhadap waktu menghasilkan garis spektrum yang lebar?
20. Mengapa nilai rata-rata sebuah besaran tidak harus sama dengan salah satu nilai yang mungkin terukur?
21. Mengapa satuan atom disebut satuan "alami" untuk kimia? Berapa orde besaran angka-angka khas molekul dalam satuan itu?

# Soal

## Subbab 2.1: Bilangan kompleks dan rumus Euler

Gunakan tetapan dan tabel konversi di Bab 1 bila diperlukan. Soal dikelompokkan menurut tingkat: **dasar**, **menengah**, dan **tantangan ★**. Soal bertanda **[P]** dibahas di akhir bab. Untuk soal bertanda (Python), gunakan NumPy.

**Dasar**

**1.** Hitung $(2 + 3i)(4 - i)$ dan $(2 + 3i)/(4 - i)$.

**2.** Nyatakan $-1 + i$ dan $-3i$ dalam bentuk kutub $re^{i\theta}$.

**3.** Sederhanakan $i^{27}$ dan $(1 + i)/(1 - i)$.

**4.** Jika $\psi = (1 + i)e^{ikx}$, berapa $\psi^*$ dan $|\psi|^2$?

**Menengah**

**5.** Tentukan ketiga akar $z^3 = -8$ dalam bentuk Kartesius.

**6.** Hitung $(\cos 30° + i\sin 30°)^6$ dengan rumus de Moivre.

**7.** Tunjukkan bahwa jumlah kelima akar kelima dari satu adalah nol. Apa makna geometrinya?

**8.** Dengan $E_k = \alpha + 2\beta\cos(2\pi k/N)$, hitung tingkat energi π siklobutadiena ($N = 4$) dan anion siklopentadienil ($N = 5$), dalam $x = (E - \alpha)/\beta$.

**Tantangan ★**

**9.** ★ [P] Dengan rumus Euler, turunkan $\sin 3\theta = 3\sin\theta - 4\sin^3\theta$, lalu tunjukkan bahwa $\sum_{k=0}^{N-1}\cos(2\pi k/N) = 0$ untuk $N \ge 2$.

## Subbab 2.2: Turunan, integral parsial, integral Gauss

**Dasar**

**10.** Untuk $f(x, y) = x^2\sin y$, hitung $\partial f/\partial x$, $\partial f/\partial y$, dan $\partial^2f/\partial x\,\partial y$.

**11.** Hitung $\int_0^\infty x^3e^{-2x}\,dx$ dengan (2.8).

**12.** Hitung $\int_{-\infty}^\infty e^{-3x^2}\,dx$ dan $\int_{-\infty}^\infty x^2e^{-3x^2}\,dx$.

**13.** Hitung $\int_0^\pi x\sin x\,dx$ dengan integral parsial.

**Menengah**

**14.** Hitung $\langle x^2\rangle = \dfrac2L\int_0^Lx^2\sin^2(\pi x/L)\,dx$ untuk $L = 1$.

**15.** Fungsi $\psi = Ne^{-x^2/2}$. Tentukan $N$, $\langle x^2\rangle$, dan $\langle x^4\rangle$.

**16.** Apakah $\int_{-\infty}^\infty xe^{-(x - 1)^2}\,dx$ nol? Hitung nilainya dengan substitusi $u = x - 1$.

**17.** Hitung $\int_0^\infty x^2e^{-x^2}\,dx$ dengan memanfaatkan paritas.

**18.** Tanpa menghitung, tentukan mana yang nol: (a) $\int_{-1}^1x^2\sin x\,dx$; (b) $\int_{-\pi}^\pi\cos x\sin 2x\,dx$; (c) $\int_{-\infty}^\infty x^2e^{-x^2}\cos x\,dx$.

**Tantangan ★**

**19.** ★ Turunkan $\int_{-\infty}^\infty x^{2n}e^{-ax^2}\,dx = \dfrac{(2n - 1)!!}{2^na^n}\sqrt{\dfrac\pi a}$ dengan menurunkan terhadap $a$ berulang kali. Periksa untuk $n = 2$.

**20.** ★ Lengkapkan kuadrat untuk menunjukkan $\int_{-\infty}^\infty e^{-ax^2 + bx}\,dx = \sqrt{\pi/a}\,e^{b^2/4a}$.

## Subbab 2.3: Persamaan diferensial orde dua

**Dasar**

**21.** Tuliskan penyelesaian umum (a) $y'' = 9y$; (b) $y'' + 9y = 0$; (c) $y'' - 4y' + 4y = 0$.

**22.** Selesaikan $y'' + 4y = 0$ dengan $y(0) = 1$, $y'(0) = 2$.

**23.** Selesaikan $y'' + 2y' + 10y = 0$.

**Menengah**

**24.** Untuk $y'' = -k^2y$ dengan $y(0) = y(L) = 0$ dan $k = \sqrt{2m_eE}/\hbar$, hitung dua energi terendah elektron untuk $L = 0{,}50$ nm.

**25.** [P] Untuk $y'' = -k^2y$ dengan $y(0) = 0$ dan $y'(L) = 0$, nilai $k$ mana yang diizinkan? Gambarkan dua penyelesaian pertama.

**26.** Ulangi Contoh 2.16 untuk $k_1 = 0{,}20$ min⁻¹ dan $k_2 = 0{,}10$ min⁻¹.

**27.** Tunjukkan bahwa $y = e^{ikx}$ dan $y = e^{-ikx}$ bebas linear, lalu nyatakan $\sin kx$ sebagai kombinasinya.

**Tantangan ★**

**28.** ★ Untuk $y'' = \kappa^2y$ pada $x > 0$ dengan syarat $y \to 0$ ketika $x \to \infty$ dan $y(0) = 1$, tentukan penyelesaiannya. Pada jarak berapa $y$ turun menjadi $1/e$ jika $\kappa = \sqrt{2m_e(1\ \text{eV})}/\hbar$?

**29.** ★ Reaksi $\text{A} \to \text{B} \to \text{C}$ dengan $k_1 = k_2 = k$. Tunjukkan bahwa $[\text{B}] = kt\,e^{-kt}$ dan tentukan $t_\text{maks}$ serta $[\text{B}]_\text{maks}$.

## Subbab 2.4: Penyelesaian dengan deret pangkat

**Dasar**

**30.** Turunkan rekursi (2.19) untuk persamaan Hermite.

**31.** Dengan rekursi (2.19), tentukan $H_0$ dan $H_1$ (koefisien tertinggi $2^n$).

**Menengah**

**32.** [P] Tentukan $H_5$ dari rekursi dan periksa banyaknya akar riilnya.

**33.** Selesaikan $y' = y$ dengan deret pangkat dan $y(0) = 1$.

**34.** Persamaan Legendre $(1 - x^2)y'' - 2xy' + \ell(\ell + 1)y = 0$ mempunyai rekursi $a_{k+2} = \dfrac{k(k + 1) - \ell(\ell + 1)}{(k + 2)(k + 1)}a_k$. Tentukan penyelesaian polinom untuk $\ell = 2$ dan $\ell = 3$.

**35.** Untuk persamaan Hermite dengan $\nu = 1{,}5$, hitung $a_3$, $a_5$, $a_7$ deret ganjil dengan $a_1 = 1$.

**Tantangan ★**

**36.** ★ Tunjukkan bahwa untuk $k$ besar rekursi Legendre memberikan $a_{k+2}/a_k \to 1$, sehingga deret tak hingga divergen di $x = \pm1$. Mengapa hal ini memaksa $\ell$ bulat?

## Subbab 2.5: Koordinat bola dan silinder

**Dasar**

**37.** Nyatakan $(0, 3, 4)$ dalam koordinat bola dan $(r, \theta, \phi) = (3, 90°, 60°)$ dalam koordinat Kartesius.

**38.** Hitung luas permukaan bola satuan dengan $\int_0^{2\pi}\int_0^\pi\sin\theta\,d\theta\,d\phi$.

**39.** Hitung peluang elektron 1s berada di luar bola berjari-jari $2a_0$.

**40.** Berapa volume kulit bola berjari-jari $a_0 = 52{,}9$ pm dan tebal 1 pm?

**Menengah**

**41.** [P] Orbital 2s hidrogen (satuan atom) adalah $N(2 - r)e^{-r/2}$. Tentukan $N$.

**42.** Hitung $\langle r\rangle$ untuk orbital 2p$_z$ Contoh 2.24 dan $\langle 1/r\rangle$ untuk orbital 1s (satuan atom).

**43.** Hitung $\langle r^2\rangle$ dan $\sigma_r$ untuk orbital 1s.

**44.** Tunjukkan bahwa orbital 2p$_z$ dan 1s ortogonal hanya karena integral sudutnya, $\int_0^\pi\cos\theta\sin\theta\,d\theta = 0$.

**Tantangan ★**

**45.** ★ Turunkan $d\tau = r^2\sin\theta\,dr\,d\theta\,d\phi$ dari determinan jakobian $\partial(x, y, z)/\partial(r, \theta, \phi)$.

**46.** ★ Dalam koordinat silinder, hitung $\int e^{-\rho^2}\,d\tau$ untuk silinder tak hingga panjang satu satuan dan bandingkan dengan integral Gauss dua dimensi.

## Subbab 2.6: Vektor dan hasil kali dalam fungsi

**Dasar**

**47.** Hitung sudut antara $(1, 0, 1)$ dan $(1, 1, 0)$.

**48.** Apakah $f = x$ dan $g = x^2$ ortogonal pada $[-1, 1]$? Pada $[0, 1]$?

**49.** Elektron di $\vec r = (a_0, 0, 0)$ bergerak dengan $\vec p = (0, m_ev, 0)$, $v = \alpha c$. Hitung $\vec L = \vec r \times \vec p$ dalam satuan $\hbar$.

**Menengah**

**50.** Normalkan $f = 3\phi_1 + 4i\phi_2$ ($\phi_1$, $\phi_2$ ortonormal) dan hitung $|c_1|^2$, $|c_2|^2$.

**51.** [P] Lanjutkan Contoh 2.28: ortogonalkan $x^3$ terhadap $1, x, x^2 - \tfrac13$ pada $[-1, 1]$.

**52.** Hitung integral tumpang tindih $S$ antara $e^{-x^2/2}$ dan $e^{-(x - 2)^2/2}$ yang masing-masing dinormalkan.

**53.** Hitung $c_1$ untuk fungsi segitiga ternormalisasi $f(x) = \sqrt{12/L^3}\,x$ ($0 \le x \le L/2$), $\sqrt{12/L^3}\,(L - x)$ ($L/2 \le x \le L$) pada basis Contoh 2.26.

**Tantangan ★**

**54.** ★ Buktikan ketaksamaan Schwarz dengan meninjau $\langle f - \lambda g|f - \lambda g\rangle \ge 0$ untuk $\lambda = \langle g|f\rangle/\langle g|g\rangle$.

## Subbab 2.7: Matriks dan determinan

**Dasar**

**55.** Untuk $\mathbf A = \begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix}$ dan $\mathbf B = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$, hitung $\mathbf{AB}$, $\mathbf{BA}$, dan $[\mathbf A, \mathbf B]$.

**56.** Hitung $\det\begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 4\\ 5 & 6 & 0\end{pmatrix}$.

**57.** Hitung invers $\begin{pmatrix}4 & 1\\ 2 & 3\end{pmatrix}$.

**Menengah**

**58.** Hitung $\sigma_y\sigma_z$, $\sigma_z\sigma_y$, dan $\sigma_x^2$ (matriks Pauli).

**59.** Hitung determinan Hückel alil $\begin{vmatrix} -x & 1 & 0\\ 1 & -x & 1\\ 0 & 1 & -x\end{vmatrix}$ pada $x = -0{,}5$.

**60.** Tuliskan determinan Slater tiga elektron dalam spin-orbital $a$, $b$, $c$ dan uraikan menjadi enam suku.

**61.** Tunjukkan bahwa $\mathbf R(\theta)\mathbf R(\phi) = \mathbf R(\theta + \phi)$ untuk matriks rotasi dua dimensi.

**Tantangan ★**

**62.** ★ Tunjukkan bahwa $\det\mathbf U = e^{i\gamma}$ (modulus satu) untuk setiap matriks uniter $\mathbf U$.

## Subbab 2.8: Nilai eigen dan vektor eigen matriks

**Dasar**

**63.** Cari nilai eigen dan vektor eigen $\begin{pmatrix}3 & 1\\ 1 & 3\end{pmatrix}$ dan $\begin{pmatrix}1 & 2\\ 2 & 1\end{pmatrix}$.

**64.** Cari nilai eigen $\sigma_x$ dan vektor eigennya.

**65.** Sebuah matriks $2 \times 2$ mempunyai teras 5 dan determinan 6. Berapa nilai eigennya?

**Menengah**

**66.** Cari nilai eigen $\begin{pmatrix}2 & 0 & 0\\ 0 & 3 & 4\\ 0 & 4 & 9\end{pmatrix}$.

**67.** [P] Tuliskan matriks Hückel siklobutadiena dan cari nilai eigennya. Berapa elektron tak berpasangan yang diramalkan untuk keadaan dasarnya?

**68.** (Python) Cari nilai eigen Hückel heksatriena dan bandingkan dengan $2\cos[k\pi/(N + 1)]$.

**69.** (Python) Cari nilai eigen Hückel trimetilenametana (satu C pusat terikat pada tiga C).

**70.** Ulangi Contoh 2.38 dengan $\alpha_A = -18{,}6$ eV, $\alpha_B = -13{,}6$ eV, $\beta = -4{,}0$ eV.

**Tantangan ★**

**71.** ★ Buktikan bahwa vektor eigen matriks Hermitian dengan nilai eigen berbeda ortogonal.

**72.** ★ (Python) Untuk anion siklopentadienil (6 elektron π), hitung energi π total dan bandingkan dengan tiga ikatan π terlokalisasi.

## Subbab 2.9: Deret Taylor dan deret Fourier

**Dasar**

**73.** Hitung $\cos 0{,}2$ dengan tiga suku deret Taylor dan bandingkan dengan nilai tepat.

**74.** Uraikan $\ln(1 + x)$ sampai $x^3$ dan $(1 + x)^{-1/2}$ sampai $x^2$.

**75.** Garis NMR mempunyai lebar 2,0 Hz. Berapa $T_2$-nya?

**Menengah**

**76.** Potensial Lennard-Jones $V = 4\varepsilon[(\sigma/r)^{12} - (\sigma/r)^6]$. Tunjukkan bahwa minimumnya di $r_e = 2^{1/6}\sigma$ dan tetapan gayanya $k = 57{,}1\varepsilon/\sigma^2$.

**77.** [P] Untuk Ar₂, $\varepsilon/k_B = 120$ K dan $\sigma = 0{,}34$ nm. Hitung $k$ dan bilangan gelombang getaran harmonik ($\mu = 19{,}97$ u).

**78.** Untuk H₂, potensial Morse dengan $D_e = 4{,}747$ eV dan $a = 1{,}944$ Å⁻¹. Hitung $k$ dan $\tilde\nu$ ($\mu = 0{,}504$ u).

**79.** Hitung koefisien Fourier $b_n$ untuk $f(x) = x$ pada $(-\pi, \pi)$.

**80.** Interferometer FT-IR mempunyai beda lintasan optis maksimum 4,0 cm. Berapa kira-kira resolusinya?

**Tantangan ★**

**81.** ★ Tunjukkan bahwa transformasi Fourier $e^{-x^2/4\sigma^2}$ sebanding dengan $e^{-\sigma^2k^2}$, dengan melengkapkan kuadrat.

## Subbab 2.10: Peluang, nilai rata-rata, simpangan baku

**Dasar**

**82.** Sebuah sistem mempunyai tiga tingkat dengan energi 0, $kT$, dan $2kT$ (tanpa degenerasi). Hitung peluang setiap tingkat, $\langle E\rangle$, dan $\sigma_E$ (dalam $kT$).

**83.** Hitung peluang nilai acak bersebaran Gauss jatuh dalam $\pm2\sigma$ dan $\pm3\sigma$.

**84.** Hitung kelajuan rata-rata He, H₂, dan UF₆ pada 298 K.

**Menengah**

**85.** Untuk sebaran eksponensial dengan umur $\tau$, hitung peluang umur sebuah molekul antara $\tau$ dan $2\tau$.

**86.** [P] (Python) Populasi rotasi CO pada 298 K sebanding dengan $(2J + 1)e^{-BJ(J+1)hc/kT}$ dengan $B = 1{,}9225$ cm⁻¹. Hitung $\langle J\rangle$, $\sigma_J$, dan $J$ terpadat.

**87.** Untuk partikel dalam kotak pada keadaan $n = 2$, berapa peluang partikel berada di separuh kiri kotak? Di seperempat pertama?

**88.** Hitung $\sigma_x$ partikel dalam kotak untuk $n = 1$ dan $n = 10$, dan bandingkan dengan $L/\sqrt{12}$.

**Tantangan ★**

**89.** ★ Buktikan bahwa untuk sebaran apa pun $\langle x^2\rangle \ge \langle x\rangle^2$. Kapan tanda sama dengan berlaku?

## Subbab 2.11: Satuan atom

**Dasar**

**90.** Nyatakan 1,00 Å dalam bohr dan 1,00 eV dalam hartree.

**91.** Nyatakan momen dipol H₂O (1,85 D) dalam satuan atom.

**92.** Berapa 1,00 fs dalam satuan atom waktu?

**Menengah**

**93.** [P] Energi disosiasi H₂ menurut perhitungan adalah 0,1745 $E_h$. Nyatakan dalam eV dan kJ/mol. Medan listrik $10^9$ V/m berapa dalam satuan atom?

**94.** Tuliskan energi ion He⁺ pada $n = 2$ dalam satuan atom.

**95.** Berapa laju cahaya dalam satuan atom? Berapa $v/c$ elektron 1s pada atom raksa ($Z = 80$) menurut model Bohr?

**Tantangan ★**

**96.** ★ Tunjukkan dengan analisis dimensi bahwa satu-satunya kombinasi $m_e$, $e$, $\hbar$, $4\pi\varepsilon_0$ yang berdimensi panjang adalah $a_0$, dan yang berdimensi energi adalah $E_h$.


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | $11 + 10i$; $(5 + 14i)/17 = 0{,}294 + 0{,}824i$ | 49 | $(0, 0, \hbar)$ |
| 2 | $\sqrt2\,e^{i3\pi/4}$; $3e^{-i\pi/2}$ | 50 | $(3\phi_1 + 4i\phi_2)/5$; 0,36; 0,64 |
| 3 | $-i$; $i$ | 51 | $x^3 - \tfrac35x$, sebanding dengan $P_3 = \tfrac12(5x^3 - 3x)$ |
| 4 | $(1 - i)e^{-ikx}$; 2 | 52 | $e^{-1} = 0{,}368$ |
| 5 | $1 + \sqrt3\,i$; $-2$; $1 - \sqrt3\,i$ | 53 | $c_1 = 4\sqrt6/\pi^2 = 0{,}993$ |
| 6 | $-1$ | 54 | $\langle f|f\rangle - |\langle g|f\rangle|^2/\langle g|g\rangle \ge 0$ |
| 7 | deret geometri $(1 - z^5)/(1 - z) = 0$; titik berat segi lima di titik asal | 55 | $\begin{pmatrix}2 & 1\\ 4 & 3\end{pmatrix}$; $\begin{pmatrix}3 & 4\\ 1 & 2\end{pmatrix}$; $\begin{pmatrix}-1 & -3\\ 3 & 1\end{pmatrix}$ |
| 8 | $N = 4$: 2, 0, 0, −2; $N = 5$: 2; 0,618 (dua); −1,618 (dua) | 56 | 1 |
| 9 | ambil bagian khayal $(\cos\theta + i\sin\theta)^3$; jumlah akar satuan nol | 57 | $\begin{pmatrix}0{,}3 & -0{,}1\\ -0{,}2 & 0{,}4\end{pmatrix}$ |
| 10 | $2x\sin y$; $x^2\cos y$; $2x\cos y$ | 58 | $i\sigma_x$; $-i\sigma_x$; $\mathbf I$ |
| 11 | $3/8 = 0{,}375$ | 59 | $-0{,}875$ |
| 12 | 1,023; 0,171 | 60 | $a_1b_2c_3 - a_1c_2b_3 - b_1a_2c_3 + b_1c_2a_3 + c_1a_2b_3 - c_1b_2a_3$ |
| 13 | $\pi$ | 61 | perkalian memberi rumus jumlah sudut |
| 14 | 0,2827 | 62 | $|\det\mathbf U|^2 = \det(\mathbf U^\dagger\mathbf U) = 1$ |
| 15 | $\pi^{-1/4} = 0{,}751$; 0,5; 0,75 | 63 | 4 dan 2, $(1, \pm1)/\sqrt2$; 3 dan −1, $(1, \pm1)/\sqrt2$ |
| 16 | tidak; $\sqrt\pi = 1{,}772$ | 64 | $\pm1$; $(1, \pm1)/\sqrt2$ |
| 17 | $\sqrt\pi/4 = 0{,}443$ | 65 | 2 dan 3 |
| 18 | (a) nol; (b) nol; (c) tidak nol | 66 | 1; 2; 11 |
| 19 | $n = 2$: $\tfrac34\sqrt\pi\,a^{-5/2}$ | 67 | $x = 2, 0, 0, -2$; dua (dalam dua orbital $x = 0$) |
| 20 | $-a(x - b/2a)^2 + b^2/4a$ | 68 | ±1,802; ±1,247; ±0,445 |
| 21 | (a) $c_1e^{3x} + c_2e^{-3x}$; (b) $A\sin 3x + B\cos 3x$; (c) $(c_1 + c_2x)e^{2x}$ | 69 | $\pm\sqrt3$, 0, 0 |
| 22 | $\cos 2x + \sin 2x$ | 70 | −20,82 dan −11,38 eV; $c_A^2 = 0{,}765$ |
| 23 | $e^{-x}(A\cos 3x + B\sin 3x)$ | 71 | $(\lambda_1 - \lambda_2)\mathbf c_1^\dagger\mathbf c_2 = 0$ |
| 24 | 1,50 eV; 6,02 eV | 72 | $6\alpha + 6{,}472\beta$; delokalisasi $0{,}472\beta$ dibanding $6\alpha + 6\beta$ |
| 25 | $k = (n - \tfrac12)\pi/L$, $n = 1, 2, \ldots$ | 73 | 0,980 067 lawan 0,980 067 |
| 26 | $t_\text{maks} = 6{,}93$ min; $[\text{B}]_\text{maks} = 0{,}50$ | 74 | $x - x^2/2 + x^3/3$; $1 - x/2 + 3x^2/8$ |
| 27 | $\sin kx = (e^{ikx} - e^{-ikx})/2i$ | 75 | 0,16 s |
| 28 | $e^{-\kappa x}$; $1/\kappa = 0{,}195$ nm | 76 | $k = 72\varepsilon/(2^{1/3}\sigma^2)$ |
| 29 | $t = 1/k$; $1/e = 0{,}368$ | 77 | 0,82 N/m; 26 cm⁻¹ |
| 30 | $(k + 2)(k + 1)a_{k+2} - 2ka_k + 2\nu a_k = 0$ | 78 | 575 N/m; 4400 cm⁻¹ |
| 31 | $H_0 = 1$; $H_1 = 2x$ | 79 | $b_n = 2(-1)^{n+1}/n$ |
| 32 | $32x^5 - 160x^3 + 120x$; lima akar | 80 | 0,25 cm⁻¹ |
| 33 | $\sum x^k/k! = e^x$ | 81 | eksponen $-(x/2\sigma + i\sigma k)^2 - \sigma^2k^2$ |
| 34 | $\propto 1 - 3x^2$; $\propto x - \tfrac53x^3$ | 82 | 0,665; 0,245; 0,090; 0,425; 0,651 |
| 35 | $-1/6$; $-1/40$; $-0{,}004\,17$ | 83 | 95,4%; 99,7% |
| 36 | deret seperti $\sum x^k$ divergen di $\cos\theta = \pm1$; fungsi sudut harus berhingga di kutub | 84 | 1256; 1770; 134 m/s |
| 37 | $(5;\ 36{,}87°;\ 90°)$; $(1{,}50;\ 2{,}60;\ 0)$ | 85 | 0,233 |
| 38 | $4\pi$ | 86 | 8,69; 4,81; 7 |
| 39 | 0,238 | 87 | 1/2; 1/4 |
| 40 | $3{,}5 \times 10^{-32}$ m³ | 88 | 0,181$L$; 0,288$L$; 0,289$L$ |
| 41 | $1/\sqrt{32\pi} = 0{,}0997$ | 89 | $\sigma^2 = \langle(x - \langle x\rangle)^2\rangle \ge 0$; bila semua hasil sama |
| 42 | $5a_0$; $1/a_0$ | 90 | 1,890 bohr; 0,036 75 $E_h$ |
| 43 | $3a_0^2$; $0{,}866a_0$ | 91 | 0,728 a.u. |
| 44 | integral sudut nol | 92 | 41,3 a.u. |
| 45 | determinan $= r^2\sin\theta$ | 93 | 4,748 eV; 458,1 kJ/mol; 0,0019 a.u. |
| 46 | $\pi$ | 94 | $-0{,}5\ E_h$ |
| 47 | 60° | 95 | 137,04; 0,58 |
| 48 | ya; tidak ($\langle f|g\rangle = 1/4$) | 96 | selesaikan pangkat-pangkat dimensi |
:::


# Pembahasan soal terpilih

**Soal 9.** $(\cos\theta + i\sin\theta)^3 = e^{3i\theta} = \cos 3\theta + i\sin 3\theta$. Uraikan ruas kiri dengan rumus binomial:

$$
\cos^3\theta + 3i\cos^2\theta\sin\theta - 3\cos\theta\sin^2\theta - i\sin^3\theta .
$$

Samakan bagian khayal: $\sin 3\theta = 3\cos^2\theta\sin\theta - \sin^3\theta = 3(1 - \sin^2\theta)\sin\theta - \sin^3\theta = 3\sin\theta - 4\sin^3\theta$.

Untuk jumlah kosinus, $\sum_k\cos(2\pi k/N) = \text{Re}\sum_kz^k$ dengan $z = e^{2\pi i/N} \ne 1$. Deret geometri: $\sum_{k=0}^{N-1}z^k = (1 - z^N)/(1 - z) = 0$ karena $z^N = 1$.

*Cara berpikir:* jumlah nol itu berarti teras matriks Hückel cincin, yang semua unsur diagonalnya $\alpha$, tepat $N\alpha$: rata-rata energi semua orbital π sama dengan $\alpha$. Orbital ikatan dan antiikatan "seimbang", sebuah aturan jumlah yang berguna untuk memeriksa perhitungan.

**Soal 25.** Dari $y(0) = 0$: $y = A\sin kx$. Turunannya $y' = Ak\cos kx$, dan $y'(L) = 0$ menuntut $\cos kL = 0$, sehingga $kL = \pi/2, 3\pi/2, \ldots$, yaitu $k = (n - \tfrac12)\pi/L$. Penyelesaian pertama adalah seperempat gelombang sinus yang mendatar di $x = L$; yang kedua tiga perempat gelombang.

*Cara berpikir:* syarat batas yang berbeda memilih himpunan $k$ yang berbeda, tetapi selalu diskret. Syarat "turunan nol" adalah syarat pada pipa organa yang ujungnya terbuka; ia juga muncul untuk fungsi gelombang yang simetris terhadap bidang tengah, karena fungsi genap mempunyai turunan nol di pusat simetri.

**Soal 32.** Dengan $\nu = 5$ pakai deret ganjil ($a_0 = 0$): $a_3 = \dfrac{2(1 - 5)}{6}a_1 = -\dfrac43a_1$; $a_5 = \dfrac{2(3 - 5)}{20}a_3 = -\dfrac15a_3 = \dfrac{4}{15}a_1$; $a_7 = 0$. Koefisien tertinggi 32 memberi $a_1 = 120$, sehingga $H_5 = 32x^5 - 160x^3 + 120x$. Faktorkan: $8x(4x^4 - 20x^2 + 15)$; dengan $u = x^2$, $4u^2 - 20u + 15 = 0$ memberi $u = 0{,}919$ dan $4{,}081$, sehingga akarnya $x = 0$, $\pm0{,}959$, $\pm2{,}020$: lima akar riil.

*Cara berpikir:* keadaan getaran ke-5 mempunyai lima simpul. Semua akar terletak di dalam daerah yang diizinkan secara klasik untuk energi itu ($|x| < \sqrt{2\nu + 1} = 3{,}32$).

**Soal 41.** $\int|\psi|^2d\tau = 4\pi N^2\int_0^\infty(2 - r)^2r^2e^{-r}dr$. Uraikan $(2 - r)^2r^2 = 4r^2 - 4r^3 + r^4$ dan pakai (2.8) dengan $a = 1$: $4(2) - 4(6) + 24 = 8$. Jadi $32\pi N^2 = 1$, $N = 1/\sqrt{32\pi} = 0{,}0997$.

*Cara berpikir:* ekspansi polinom lalu integral suku demi suku dengan rumus $n!/a^{n+1}$ adalah resep untuk semua integral radial atom hidrogen. Faktor normalisasi 2s ternyata sama dengan 2p$_z$; kebetulan yang tidak berlaku untuk $n$ yang lebih tinggi.

**Soal 51.** Kurangkan proyeksi $x^3$ pada fungsi-fungsi sebelumnya. $\langle 1|x^3\rangle = 0$ dan $\langle x^2 - \tfrac13|x^3\rangle = 0$ karena paritas (ganjil). Tinggal $\langle x|x^3\rangle = \int_{-1}^1x^4dx = 2/5$ dan $\langle x|x\rangle = 2/3$:

$$
u_3 = x^3 - \frac{2/5}{2/3}x = x^3 - \frac35x .
$$

Dikali $5/2$: $\tfrac12(5x^3 - 3x) = P_3(x)$.

*Cara berpikir:* paritas menghemat dua dari tiga proyeksi. Polinom Legendre berganti-ganti genap dan ganjil, persis seperti fungsi gelombang dalam potensial simetris: fungsi dengan paritas berbeda otomatis ortogonal.

**Soal 67.** Matriks Hückel cincin empat atom (dalam satuan $\beta$, $\alpha = 0$):

$$
\begin{pmatrix}0 & 1 & 0 & 1\\ 1 & 0 & 1 & 0\\ 0 & 1 & 0 & 1\\ 1 & 0 & 1 & 0\end{pmatrix}, \qquad x = 2, 0, 0, -2 .
$$

Empat elektron: dua di orbital $x = 2$, dua sisanya di dua orbital $x = 0$ yang terdegenerasi. Menurut aturan Hund, keduanya menempati orbital berbeda dengan spin sejajar: dua elektron tak berpasangan (diradikal triplet). Energi π total $4\alpha + 4\beta$, sama dengan dua etilena: tidak ada energi delokalisasi.

*Cara berpikir:* inilah inti **antiaromatisitas** (Bab 13). Siklobutadiena nyata menghindari keadaan ini dengan berubah bentuk menjadi persegi panjang, yang memecah degenerasi, dan hanya dapat diamati pada suhu sangat rendah dalam matriks gas mulia.

**Soal 77.** $\varepsilon = 120 \times 1{,}381 \times 10^{-23} = 1{,}657 \times 10^{-21}$ J dan $\sigma^2 = 1{,}156 \times 10^{-19}$ m², sehingga $k = 57{,}1\varepsilon/\sigma^2 = 0{,}82$ N/m. Dengan $\mu = 19{,}97 \times 1{,}6605 \times 10^{-27} = 3{,}32 \times 10^{-26}$ kg:

$$
\tilde\nu = \frac{1}{2\pi c}\sqrt{\frac{0{,}82}{3{,}32 \times 10^{-26}}} = 26\ \text{cm}^{-1} .
$$

*Cara berpikir:* tetapan gaya ikatan van der Waals hampir seribu kali lebih kecil dari ikatan kovalen (HCl: 517 N/m). Kedalaman sumurnya, 120 K atau 83 cm⁻¹, hanya tiga kuanta getaran harmonik; dengan energi titik nol, dimer Ar₂ hanya mempunyai beberapa tingkat getaran terikat dan pada suhu kamar hampir seluruhnya terurai.

**Soal 86.** Dengan $kT/hc = 207{,}2$ cm⁻¹, hitung bobot $w_J = (2J + 1)e^{-1{,}9225J(J+1)/207{,}2}$ untuk $J = 0$ sampai sekitar 80, normalkan, lalu $\langle J\rangle = \sum Jp_J = 8{,}69$, $\langle J^2\rangle - \langle J\rangle^2 = 23{,}2$, $\sigma_J = 4{,}81$. Bobot terbesar di $J = 7$.

*Cara berpikir:* sebaran ini tidak simetris (ekor panjang ke $J$ besar), sehingga rata-rata (8,7) lebih besar dari modus (7), sama seperti sebaran Maxwell dan fungsi distribusi radial 1s. Puncak pita rotasi–getaran CO teramati di sekitar $J = 7$ (Bab 6).

**Soal 93.** $0{,}1745 \times 27{,}211 = 4{,}748$ eV dan $0{,}1745 \times 2625{,}5 = 458{,}1$ kJ/mol. Medan $10^9/5{,}142 \times 10^{11} = 1{,}9 \times 10^{-3}$ a.u.

*Cara berpikir:* 4,748 eV adalah $D_e$ (dari dasar sumur); $D_0$ yang terukur, 4,478 eV, lebih kecil sebesar energi titik nol 0,27 eV (Contoh 1.46 di Bab 1). Medan $10^9$ V/m, sangat kuat untuk laboratorium, hanya dua per seribu medan atom: cukup kecil untuk diperlakukan sebagai perturbasi.

# Bacaan lanjut

1. D. A. McQuarrie, *Mathematical Methods for Scientists and Engineers* (University Science Books, 2003). Matematika yang dipakai kimia fisika, ditulis oleh kimiawan; banyak contoh dari kimia kuantum.
2. M. L. Boas, *Mathematical Methods in the Physical Sciences*, edisi ke-3 (Wiley, 2006). Acuan baku untuk bilangan kompleks, deret, persamaan diferensial, matriks, dan transformasi Fourier.
3. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 2, 7, dan 8. Matematika yang diperkenalkan saat diperlukan, dengan contoh atom dan molekul.
4. J. R. Barrante, *Applied Mathematics for Physical Chemistry*, edisi ke-3 (Pearson, 2004). Ringkas dan praktis untuk mahasiswa kimia.
5. J. Kiusalaas, *Numerical Methods in Engineering with Python 3* (Cambridge University Press, 2013). Untuk diagonalisasi, integrasi numerik, dan penyelesaian persamaan diferensial dengan Python.
