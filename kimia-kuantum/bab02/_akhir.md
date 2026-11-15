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
18. Apa yang dimaksud pendekatan harmonik, dan suku deret Taylor mana yang diabaikan?
19. Mengapa sinyal yang meluruh cepat terhadap waktu menghasilkan garis spektrum yang lebar?
20. Mengapa nilai rata-rata sebuah besaran tidak harus sama dengan salah satu nilai yang mungkin terukur?
21. Mengapa satuan atom disebut satuan "alami" untuk kimia? Berapa orde besaran angka-angka khas molekul dalam satuan itu?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{euler}}.** $(\cos\theta + i\sin\theta)^3 = e^{3i\theta} = \cos 3\theta + i\sin 3\theta$. Uraikan ruas kiri dengan rumus binomial:

$$
\cos^3\theta + 3i\cos^2\theta\sin\theta - 3\cos\theta\sin^2\theta - i\sin^3\theta .
$$

Samakan bagian khayal: $\sin 3\theta = 3\cos^2\theta\sin\theta - \sin^3\theta = 3(1 - \sin^2\theta)\sin\theta - \sin^3\theta = 3\sin\theta - 4\sin^3\theta$.

Untuk jumlah kosinus, $\sum_k\cos(2\pi k/N) = \text{Re}\sum_kz^k$ dengan $z = e^{2\pi i/N} \ne 1$. Deret geometri: $\sum_{k=0}^{N-1}z^k = (1 - z^N)/(1 - z) = 0$ karena $z^N = 1$.

*Cara berpikir:* jumlah nol itu berarti teras matriks Hückel cincin, yang semua unsur diagonalnya $\alpha$, tepat $N\alpha$: rata-rata energi semua orbital π sama dengan $\alpha$. Orbital ikatan dan antiikatan "seimbang", sebuah aturan jumlah yang berguna untuk memeriksa perhitungan.

**Soal {{kotak2}}.** Dari $y(0) = 0$: $y = A\sin kx$. Turunannya $y' = Ak\cos kx$, dan $y'(L) = 0$ menuntut $\cos kL = 0$, sehingga $kL = \pi/2, 3\pi/2, \ldots$, yaitu $k = (n - \tfrac12)\pi/L$. Penyelesaian pertama adalah seperempat gelombang sinus yang mendatar di $x = L$; yang kedua tiga perempat gelombang.

*Cara berpikir:* syarat batas yang berbeda memilih himpunan $k$ yang berbeda, tetapi selalu diskret. Syarat "turunan nol" adalah syarat pada pipa organa yang ujungnya terbuka; ia juga muncul untuk fungsi gelombang yang simetris terhadap bidang tengah, karena fungsi genap mempunyai turunan nol di pusat simetri.

**Soal {{hermite5}}.** Dengan $\nu = 5$ pakai deret ganjil ($a_0 = 0$): $a_3 = \dfrac{2(1 - 5)}{6}a_1 = -\dfrac43a_1$; $a_5 = \dfrac{2(3 - 5)}{20}a_3 = -\dfrac15a_3 = \dfrac{4}{15}a_1$; $a_7 = 0$. Koefisien tertinggi 32 memberi $a_1 = 120$, sehingga $H_5 = 32x^5 - 160x^3 + 120x$. Faktorkan: $8x(4x^4 - 20x^2 + 15)$; dengan $u = x^2$, $4u^2 - 20u + 15 = 0$ memberi $u = 0{,}919$ dan $4{,}081$, sehingga akarnya $x = 0$, $\pm0{,}959$, $\pm2{,}020$: lima akar riil.

*Cara berpikir:* keadaan getaran ke-5 mempunyai lima simpul. Semua akar terletak di dalam daerah yang diizinkan secara klasik untuk energi itu ($|x| < \sqrt{2\nu + 1} = 3{,}32$).

**Soal {{norm2s}}.** $\int|\psi|^2d\tau = 4\pi N^2\int_0^\infty(2 - r)^2r^2e^{-r}dr$. Uraikan $(2 - r)^2r^2 = 4r^2 - 4r^3 + r^4$ dan pakai (2.8) dengan $a = 1$: $4(2) - 4(6) + 24 = 8$. Jadi $32\pi N^2 = 1$, $N = 1/\sqrt{32\pi} = 0{,}0997$.

*Cara berpikir:* ekspansi polinom lalu integral suku demi suku dengan rumus $n!/a^{n+1}$ adalah resep untuk semua integral radial atom hidrogen. Faktor normalisasi 2s ternyata sama dengan 2p$_z$; kebetulan yang tidak berlaku untuk $n$ yang lebih tinggi.

**Soal {{gram3}}.** Kurangkan proyeksi $x^3$ pada fungsi-fungsi sebelumnya. $\langle 1|x^3\rangle = 0$ dan $\langle x^2 - \tfrac13|x^3\rangle = 0$ karena paritas (ganjil). Tinggal $\langle x|x^3\rangle = \int_{-1}^1x^4dx = 2/5$ dan $\langle x|x\rangle = 2/3$:

$$
u_3 = x^3 - \frac{2/5}{2/3}x = x^3 - \frac35x .
$$

Dikali $5/2$: $\tfrac12(5x^3 - 3x) = P_3(x)$.

*Cara berpikir:* paritas menghemat dua dari tiga proyeksi. Polinom Legendre berganti-ganti genap dan ganjil, persis seperti fungsi gelombang dalam potensial simetris: fungsi dengan paritas berbeda otomatis ortogonal.

**Soal {{siklobuta}}.** Matriks Hückel cincin empat atom (dalam satuan $\beta$, $\alpha = 0$):

$$
\begin{pmatrix}0 & 1 & 0 & 1\\ 1 & 0 & 1 & 0\\ 0 & 1 & 0 & 1\\ 1 & 0 & 1 & 0\end{pmatrix}, \qquad x = 2, 0, 0, -2 .
$$

Empat elektron: dua di orbital $x = 2$, dua sisanya di dua orbital $x = 0$ yang terdegenerasi. Menurut aturan Hund, keduanya menempati orbital berbeda dengan spin sejajar: dua elektron tak berpasangan (diradikal triplet). Energi π total $4\alpha + 4\beta$, sama dengan dua etilena: tidak ada energi delokalisasi.

*Cara berpikir:* inilah inti **antiaromatisitas** (Bab 13). Siklobutadiena nyata menghindari keadaan ini dengan berubah bentuk menjadi persegi panjang, yang memecah degenerasi, dan hanya dapat diamati pada suhu sangat rendah dalam matriks gas mulia.

**Soal {{lj}}.** $\varepsilon = 120 \times 1{,}381 \times 10^{-23} = 1{,}657 \times 10^{-21}$ J dan $\sigma^2 = 1{,}156 \times 10^{-19}$ m², sehingga $k = 57{,}1\varepsilon/\sigma^2 = 0{,}82$ N/m. Dengan $\mu = 19{,}97 \times 1{,}6605 \times 10^{-27} = 3{,}32 \times 10^{-26}$ kg:

$$
\tilde\nu = \frac{1}{2\pi c}\sqrt{\frac{0{,}82}{3{,}32 \times 10^{-26}}} = 26\ \text{cm}^{-1} .
$$

*Cara berpikir:* tetapan gaya ikatan van der Waals hampir seribu kali lebih kecil dari ikatan kovalen (HCl: 517 N/m). Kedalaman sumurnya, 120 K atau 83 cm⁻¹, hanya tiga kuanta getaran harmonik; dengan energi titik nol, dimer Ar₂ hanya mempunyai beberapa tingkat getaran terikat dan pada suhu kamar hampir seluruhnya terurai.

**Soal {{corot}}.** Dengan $kT/hc = 207{,}2$ cm⁻¹, hitung bobot $w_J = (2J + 1)e^{-1{,}9225J(J+1)/207{,}2}$ untuk $J = 0$ sampai sekitar 80, normalkan, lalu $\langle J\rangle = \sum Jp_J = 8{,}69$, $\langle J^2\rangle - \langle J\rangle^2 = 23{,}2$, $\sigma_J = 4{,}81$. Bobot terbesar di $J = 7$.

*Cara berpikir:* sebaran ini tidak simetris (ekor panjang ke $J$ besar), sehingga rata-rata (8,7) lebih besar dari modus (7), sama seperti sebaran Maxwell dan fungsi distribusi radial 1s. Puncak pita rotasi–getaran CO teramati di sekitar $J = 7$ (Bab 6).

**Soal {{auh2}}.** $0{,}1745 \times 27{,}211 = 4{,}748$ eV dan $0{,}1745 \times 2625{,}5 = 458{,}1$ kJ/mol. Medan $10^9/5{,}142 \times 10^{11} = 1{,}9 \times 10^{-3}$ a.u.

*Cara berpikir:* 4,748 eV adalah $D_e$ (dari dasar sumur); $D_0$ yang terukur, 4,478 eV, lebih kecil sebesar energi titik nol 0,27 eV (Contoh 1.46 di Bab 1). Medan $10^9$ V/m, sangat kuat untuk laboratorium, hanya dua per seribu medan atom: cukup kecil untuk diperlakukan sebagai perturbasi.

# Bacaan lanjut

1. D. A. McQuarrie, *Mathematical Methods for Scientists and Engineers* (University Science Books, 2003). Matematika yang dipakai kimia fisika, ditulis oleh kimiawan; banyak contoh dari kimia kuantum.
2. M. L. Boas, *Mathematical Methods in the Physical Sciences*, edisi ke-3 (Wiley, 2006). Acuan baku untuk bilangan kompleks, deret, persamaan diferensial, matriks, dan transformasi Fourier.
3. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 2, 7, dan 8. Matematika yang diperkenalkan saat diperlukan, dengan contoh atom dan molekul.
4. J. R. Barrante, *Applied Mathematics for Physical Chemistry*, edisi ke-3 (Pearson, 2004). Ringkas dan praktis untuk mahasiswa kimia.
5. J. Kiusalaas, *Numerical Methods in Engineering with Python 3* (Cambridge University Press, 2013). Untuk diagonalisasi, integrasi numerik, dan penyelesaian persamaan diferensial dengan Python.
