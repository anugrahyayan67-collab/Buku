# Ringkasan Bab 8

| Gagasan | Rumus | Subbab |
|---|---|---|
| Teorema variasi | $W = \langle\phi|\hat H|\phi\rangle/\langle\phi|\phi\rangle \ge E_1$; galat energi orde $\varepsilon^2$ | 8.2 |
| Batas atas keadaan tereksitasi | $\langle\psi_1|\phi\rangle = 0 \Rightarrow W \ge E_2$ (dijamin oleh simetri) | 8.2 |
| Penskalaan dan virial | $W(\zeta) = \zeta^2T_1 + \zeta V_1$; di optimum $\langle T\rangle = -\tfrac12\langle V\rangle$ | 8.2 |
| Helium, muatan efektif | $W = \zeta^2 - 2Z\zeta + \tfrac58\zeta$; $\ \zeta = Z - \tfrac{5}{16}$; $\ W = -(Z - \tfrac{5}{16})^2$ | 8.3 |
| Variasi linear | $\sum_k(H_{ik} - WS_{ik})c_k = 0$; $\ \det(\mathbf H - W\mathbf S) = 0$; $\ W_k \ge E_k$ | 8.4 |
| Dua fungsi basis | $W_\pm = (\alpha \pm \beta)/(1 \pm S)$; $\ W_\pm = \bar H \pm\sqrt{(\Delta H/2)^2 + H_{12}^2}$ | 8.4 |
| Bentuk matriks | $\mathbf{HC} = \mathbf{SCW}$; $\ \mathbf C^T\mathbf{SC} = \mathbf 1$; $\ \mathbf X = \mathbf S^{-1/2}$ | 8.5 |
| Perturbasi orde pertama | $E_n^{(1)} = H'_{nn}$; $\ \psi_n^{(1)} = \sum_{m\ne n}H'_{mn}\psi_m^{(0)}/(E_n^{(0)} - E_m^{(0)})$ | 8.6 |
| Orde kedua | $E_n^{(2)} = \sum_{m\ne n}|H'_{mn}|^2/(E_n^{(0)} - E_m^{(0)})$; $\ E_1^{(2)} < 0$; Unsöld: $-(\langle H'^2\rangle - \langle H'\rangle^2)/\Delta E$ | 8.7 |
| Deret helium | $E = -Z^2 + \tfrac58Z - 0{,}1577 + 0{,}0087/Z + \cdots$ | 8.8 |
| Perturbasi terdegenerasi | $\det(H'_{ij} - E^{(1)}\delta_{ij}) = 0$; helium 1s$n\ell$: $E = E^{(0)} + J \pm K$ | 8.9 |
| Efek Stark | $E = E^{(0)} - \mu_0F - \tfrac12\alpha F^2$; $\ \alpha = 2\sum_m|\mu_{m1}|^2/(E_m - E_1)$; H: $\alpha = \tfrac92\ a_0^3$, $n = 2$: $\pm3F$ | 8.10 |
| Dispersi London | $E = -C_6/R^6$; $\ C_6 \approx \tfrac32\alpha_A\alpha_BI_AI_B/(I_A + I_B)$ | 8.10 |
| Perturbasi bergantung waktu | $c_f = (i\hbar)^{-1}\int_0^tH'_{fi}e^{i\omega_{fi}t'}dt'$; $\ P = |\mu_{fi}F_0/\hbar|^2\sin^2(\Delta t/2)/\Delta^2$ | 8.11 |
| Osilasi Rabi | $P = \Omega^2/(\Omega^2 + \delta^2)\sin^2(\sqrt{\Omega^2 + \delta^2}\,t/2)$; $\ \Omega = |\mu_{fi}|F_0/\hbar$ | 8.11 |
| Aturan emas, laju, kekuatan | $W = (2\pi/\hbar)|H'_{fi}|^2\rho$; $\ A = \omega^3|\mu_{fi}|^2/3\pi\varepsilon_0\hbar c^3$; $\ f = (2m_e\omega/3\hbar e^2)|\mu_{fi}|^2$, $\sum f = N$ | 8.12 |
| Aturan seleksi | kotak: $\Delta n$ ganjil; atom: $\Delta\ell = \pm1$, $\Delta m = 0, \pm1$; g ↔ u; $\Delta S = 0$ | 8.12 |

**Jawaban kuis cepat.** **8.1** Dalam H₂⁺ elektron ditarik dua inti, sehingga potensialnya tidak bersimetri bola terhadap titik mana pun dan tidak terpisahkan dalam koordinat bola (persamaan itu terpisahkan dalam koordinat eliptik, tetapi penyelesaiannya tidak berbentuk tertutup sederhana). $\mu_BB = 5{,}8 \times 10^{-5}$ eV pada 1 T, sekitar $6 \times 10^{-6}$ kali 10 eV: sangat kecil. **8.2** (a) Ada kesalahan: hasil di bawah $-0{,}5\ E_h$ melanggar teorema variasi (salah hitung, atau fungsi uji tidak memenuhi syarat). (b) Untuk keadaan ganjil terendah ($v = 1$), karena fungsi ganjil ortogonal pada keadaan dasar yang genap; dengan $\alpha$ optimum hasilnya bahkan eksak. (c) Belum: $-\langle V\rangle/\langle T\rangle = 2{,}1 \ne 2$, sehingga penskalaan masih dapat menurunkan $W$. **8.3** (a) Elektron lain hanya sebagian waktu berada lebih dekat ke inti, sehingga perisainya kurang dari satu muatan penuh. (b) $\zeta = 2{,}6875$; $I = 74{,}1$ eV. (c) Teorema tetap berlaku, tetapi fungsi satu eksponen terlalu kaku: memaksa kedua elektron ke orbital yang sama, padahal dalam H⁻ satu elektron terikat erat dan yang lain menyebar jauh. **8.4** (a) Berderajat tiga; tiga batas atas sekaligus. (b) $-12$ dan $-8$ eV. (c) $-12/1{,}1 = -10{,}91$ eV dan $-8/0{,}9 = -8{,}89$ eV; antiikatan naik lebih banyak daripada ikatan turun. **8.5** (a) `eigh` memanfaatkan sifat Hermitian: menjamin nilai eigen riil dan vektor eigen ortonormal, mengurutkannya, dan lebih cepat serta stabil. (b) Buang kombinasi basis yang bersesuaian dengan nilai eigen kecil itu (ortogonalisasi kanonik), atau buang salah satu fungsi yang hampir sama. (c) Sekitar $2^3 = 8$ kali. **8.6** (a) Nol, karena $x^3|\psi_v|^2$ ganjil. (b) Tidak; $c_{rk} = 0$ di atom N. (c) Penyebutnya nol; diperlukan teori perturbasi terdegenerasi. **8.7** (a) Untuk keadaan dasar semua penyebut negatif dan semua pembilang positif. (b) Positif: semua penyebut positif, tingkat teratas didorong naik. (c) $\pm0{,}4^2/4 = \pm0{,}04$ eV; galat sekitar $(V/\Delta)^2 = 1$%. **8.8** (a) Dengan penskalaan $\rho = Zr$, perturbasi menjadi $(1/Z)/\rho_{12}$ dan seluruh Hamiltonian dikali $Z^2$, sehingga koefisien orde kedua dikali $Z^2\cdot Z^{-2} = 1$. (b) Tidak; teori perturbasi bukan metode variasi dan dapat jatuh di kedua sisi nilai eksak. (c) 62%; sisanya korelasi elektron, yang tidak dapat digambarkan fungsi hasil kali. **8.9** (a) Elektron tereksitasi dapat berada di salah satu dari empat orbital $n = 2$, dan dapat elektron 1 atau elektron 2: $4 \times 2 = 8$. (b) $K$ adalah suku interferensi antara dua penugasan label elektron; partikel klasik dapat dibedakan sehingga suku semacam itu tidak muncul. (c) $\cos\phi$ terpusat di $\phi = 0, \pi$, tempat $V_0\cos2\phi = +V_0$; $\sin\phi$ terpusat di $\pm\pi/2$, tempat $V = -V_0$. **8.10** (a) Keadaan dasar He tak terdegenerasi dan berparitas tertentu sehingga $\langle z\rangle = 0$; tingkat $n = 2$ hidrogen memuat 2s dan 2p yang terdegenerasi dengan paritas berlawanan, yang dicampur oleh medan pada orde pertama. (b) Menjadi empat kali, karena $C_6 \propto \alpha^2$. (c) β-karotena: transisi kuat pada energi rendah (penyebut kecil, momen dipol transisi besar). **8.11** (a) Panjang gelombang cahaya tampak (400–700 nm) jauh lebih besar daripada molekul, sehingga medan seragam; panjang gelombang sinar-X (sekitar 0,1 nm) sebanding dengan ukuran atom. (b) Peluang menjadi dua kali ($\propto F_0^2$); frekuensi Rabi naik $\sqrt2$ kali ($\propto F_0$). (c) Kedua Hamiltonian bersimetri bola, sehingga keadaan s tetap s; $\langle 2p|1s\rangle = 0$ karena ortogonalitas bagian sudut. **8.12** (a) 2p → 3d dan 4f → 3d diizinkan; 2s → 3d dan 3p → 4f terlarang ($\Delta\ell = 2$). (b) [Co(H₂O)₆]²⁺ oktahedral berpusat inversi, sehingga transisi d–d terlarang Laporte (pucat); [CoCl₄]²⁻ tetrahedral tanpa pusat inversi, orbital d bercampur dengan p, dan transisinya lebih kuat. (c) Laju pancaran spontan sebanding dengan $\omega^3$, sangat kecil pada frekuensi radio; garis 21 cm hidrogen, yang juga transisi dipol magnet, mempunyai umur sekitar sepuluh juta tahun.

# Pertanyaan

1. Mengapa metode variasi selalu memberi batas atas energi keadaan dasar, sedangkan teori perturbasi dapat memberi energi di bawah nilai eksak?
2. Sebuah fungsi uji memberi energi dengan galat 0,1%, tetapi momen dipolnya meleset 10%. Mengapa hal ini wajar?
3. Bagaimana simetri memungkinkan kita memperoleh batas atas untuk keadaan tereksitasi, padahal fungsi keadaan dasar eksak tidak diketahui?
4. Apa makna fisika muatan inti efektif $\zeta = 27/16$ untuk helium? Mengapa nilainya tidak 1 dan tidak 2?
5. Mengapa fungsi hasil kali dua orbital, betapa pun baiknya orbital itu, tidak dapat memberi energi eksak helium?
6. Apa keuntungan fungsi variasi linear dibandingkan fungsi uji nonlinear, dan apa harga yang harus dibayar?
7. Apa makna teorema Hylleraas–Undheim–MacDonald bagi perhitungan spektrum elektronik?
8. Mengapa kimia komputasi memakai fungsi Gauss, padahal fungsi eksponensial (Slater) lebih mirip orbital atom?
9. Mengapa dua orbital yang energinya berdekatan bercampur kuat, sedangkan yang berjauhan hampir tidak bercampur? Berikan dua contoh kimia.
10. Apa beda makna fisika koreksi energi orde pertama dan orde kedua?
11. Mengapa perturbasi orde kedua selalu menurunkan energi keadaan dasar? Hubungkan dengan teorema variasi.
12. Kapan deret perturbasi gagal, dan apa arti "deret asimtotik"?
13. Mengapa keadaan triplet helium lebih rendah daripada singlet dari konfigurasi yang sama, padahal Hamiltoniannya tidak memuat spin?
14. Mengapa dalam atom berelektron banyak orbital 2s lebih rendah daripada 2p, padahal dalam hidrogen keduanya sama?
15. Mengapa atom tidak mempunyai momen dipol permanen, sedangkan HCl mempunyai? Mengapa HCl dalam keadaan $J = 0$ hanya menunjukkan efek Stark kuadratik?
16. Bagaimana gaya dispersi London muncul di antara dua atom yang tidak mempunyai dipol? Mengapa metode Hartree–Fock tidak dapat menangkapnya?
17. Mengapa molekul berwarna umumnya lebih mudah dipolarisasi daripada molekul tak berwarna yang berukuran sama?
18. Bagaimana syarat frekuensi Bohr $\hbar\omega = E_f - E_i$ muncul dari teori perturbasi bergantung waktu?
19. Mengapa transisi d–d kompleks oktahedral lemah, sedangkan transisi transfer muatan kuat?
20. Bagaimana aturan emas Fermi menjelaskan bahwa keadaan tereksitasi meluruh secara eksponensial, dan bahwa garis spektrum mempunyai lebar alami?
21. Bagaimana teka-teki pembuka bab terjawab: bagaimana energi helium dapat dihitung lebih teliti daripada diukur, tanpa pernah menyelesaikan persamaan Schrödingernya?

# Soal

%%SOAL%%

# Jawaban

%%JAWABAN%%

# Pembahasan soal terpilih

**Soal {{abs}}.** Untuk Gauss ternormalisasi $(2\alpha/\pi)^{1/4}e^{-\alpha x^2}$: $\langle T\rangle = \alpha/2$ dan $\langle|x|\rangle = 2\sqrt{2\alpha/\pi}\int_0^\infty xe^{-2\alpha x^2}dx = 1/\sqrt{2\pi\alpha}$. Jadi $W(\alpha) = \alpha/2 + (2\pi\alpha)^{-1/2}$. Syarat minimum $\tfrac12 - \tfrac12(2\pi)^{-1/2}\alpha^{-3/2} = 0$ memberi $\alpha^{3/2} = (2\pi)^{-1/2}$, $\alpha = (2\pi)^{-1/3} = 0{,}5419$. Di titik itu $(2\pi\alpha)^{-1/2} = \alpha$, sehingga $W = \tfrac32\alpha = 0{,}8129$. Nilai eksak adalah $2^{-1/3}a_1'$, dengan $a_1' = 1{,}0188$ nol pertama turunan fungsi Airy: 0,8086. Galatnya 0,53%.

*Cara berpikir:* periksa teorema virial untuk $V \propto |x|^1$: $2\langle T\rangle = \langle V\rangle$, dan memang $\alpha = 2(\alpha/2)$. Gauss cocok karena keadaan dasar potensial berbentuk V bersifat simetris, tanpa simpul, dan meluruh cepat; galatnya kecil walaupun fungsi eksaknya (fungsi Airy) sama sekali bukan Gauss.

**Soal {{gauss2p}}.** $W(a) = \tfrac52a - \tfrac43\sqrt{2a/\pi}$. Turunannya nol bila $\tfrac52 = \tfrac23\sqrt{2/\pi}\,a^{-1/2}$, yaitu $\sqrt a = \tfrac{4}{15}\sqrt{2/\pi}$ dan $a = 32/225\pi = 0{,}0453$. Maka $\tfrac52a = 16/45\pi$ dan $\tfrac43\sqrt{2a/\pi} = \tfrac43\cdot\tfrac{4}{15}\cdot\tfrac2\pi = 32/45\pi$, sehingga $W = -16/45\pi = -0{,}1132\ E_h$. Galat terhadap $-0{,}125$: 9,5%. Fungsi ini batas atas untuk 2p (bukan 1s) karena berbentuk $z\times$(fungsi bersimetri bola), sehingga ortogonal pada semua keadaan s.

*Cara berpikir:* galat Gauss untuk 2p (9,5%) lebih kecil daripada untuk 1s (15,1%, Contoh 8.5). Fungsi p nol di inti, sehingga ketidakmampuan Gauss membentuk puncak lancip tidak terlalu merugikan; yang tersisa hanyalah ekor yang meluruh terlalu cepat.

**Soal {{zc}}.** Ion terikat bila energinya di bawah energi ion satu elektron ditambah elektron bebas diam: $-(Z - \tfrac{5}{16})^2 < -Z^2/2$, yaitu $Z - \tfrac{5}{16} > Z/\sqrt2$, atau $Z(1 - 1/\sqrt2) > \tfrac{5}{16}$. Jadi $Z > 0{,}3125/0{,}2929 = 1{,}067$. H⁻ ($Z = 1$) berada di bawah batas ini, sehingga diramalkan tak terikat.

*Cara berpikir:* perhitungan yang sangat teliti menunjukkan muatan kritis sebenarnya $Z_c = 0{,}911$, cukup jauh di bawah 1, sehingga H⁻ terikat dengan selisih yang nyaman (0,754 eV). Galat fungsi satu eksponen (sekitar $0{,}055\ E_h$, Contoh 8.13) cukup besar untuk menggeser $Z_c$ melewati 1. Pelajarannya: ketika jawaban kualitatif (terikat atau tidak) bergantung pada selisih kecil, fungsi uji harus dibuat lebih lentur, seperti fungsi dua eksponen di Contoh 8.14.

**Soal {{osil}}.** Persamaan sekuler $(0{,}575 - W)(3{,}475 - W) - 0{,}2121^2 = 0$, atau $W^2 - 4{,}05W + 1{,}9531 = 0$. Akar: $W = [4{,}05 \mp \sqrt{16{,}4025 - 7{,}8125}]/2 = (4{,}05 \mp 2{,}9309)/2$, yaitu 0,55956 dan 3,49044. Akar terendah hanya $4{,}2 \times 10^{-4}$ di atas nilai eksak.

*Cara berpikir:* unsur diagonal $H_{00} = 0{,}575$ adalah energi perturbasi orde pertama; pergeseran akibat pencampuran dengan $|2\rangle$, $-0{,}0154$, hampir sama dengan $-H_{02}^2/(H_{22} - H_{00}) = -0{,}0155$, yaitu bagian orde kedua dari keadaan $|2\rangle$. Dua fungsi basis yang dipilih dengan simetri yang benar (keduanya genap) sudah cukup; menambah $|1\rangle$ tidak berguna karena ganjil.

**Soal {{inti}}.** Di dalam bola bermuatan seragam berjari-jari $R$, potensialnya $-(Z/2R)(3 - r^2/R^2)$; di luar, $-Z/r$. Perturbasinya adalah selisih keduanya, hanya untuk $r < R$: $\Delta V = Z/r - (Z/2R)(3 - r^2/R^2)$. Karena $R \ll a_0$, $|\psi_{1s}|^2 \approx Z^3/\pi$ di seluruh inti:

$$
E^{(1)} \approx \frac{Z^3}{\pi}\int_0^R\Delta V\,4\pi r^2dr = 4Z^4\left[\frac{R^2}{2} - \frac{1}{2R}\left(R^3 - \frac{R^3}{5}\right)\right] = \frac25Z^4R^2 .
$$

Untuk hidrogen, $R = 0{,}84$ fm $= 1{,}59 \times 10^{-5}\ a_0$, $E^{(1)} = 1{,}01 \times 10^{-10}\ E_h$, atau $0{,}67$ MHz. Tandanya positif: muatan yang tersebar menarik elektron lebih lemah daripada muatan titik.

*Cara berpikir:* pergeseran ini kecil tetapi terukur dengan spektroskopi laser hidrogen; perbedaan jari-jari proton yang diperoleh dari hidrogen biasa dan hidrogen muonik (yang muonnya 207 kali lebih dekat ke inti, sehingga efeknya jutaan kali lebih besar) menjadi "teka-teki jari-jari proton" sejak 2010. Bagi kimiawan, efek yang sama sebanding dengan $Z^4$ dan dengan perubahan jari-jari inti antarisotop. Pada unsur berat seperti uranium dan raksa, "efek volume inti" ini menggeser kesetimbangan kimia antarisotop dan ikut menentukan fraksionasi isotop ²³⁵U/²³⁸U di alam.

**Soal {{dua}}.** Akar bawah $E = \tfrac\Delta2 - \tfrac\Delta2\sqrt{1 + u}$ dengan $u = 4V^2/\Delta^2$. Deret $\sqrt{1 + u} = 1 + \tfrac u2 - \tfrac{u^2}{8} + \cdots$ memberi

$$
E = -\frac\Delta2\left(\frac{2V^2}{\Delta^2} - \frac{2V^4}{\Delta^4} + \cdots\right) = -\frac{V^2}{\Delta} + \frac{V^4}{\Delta^3} - \cdots
$$

Suku pertama adalah $E^{(2)}$ (8.35); suku kedua $E^{(4)} = +V^4/\Delta^3$. Orde ganjil nol karena perturbasi tidak mempunyai unsur diagonal.

*Cara berpikir:* deret ini konvergen hanya bila $u < 1$, yaitu $|V| < \Delta/2$. Bila kopling lebih besar daripada setengah selisih energi, tidak ada orde yang cukup; diagonalisasi matriks 2 × 2 adalah satu-satunya jalan. Ini sesuai Contoh 8.31: galat orde kedua sudah 21% pada $V/\Delta = 0{,}5$.

**Soal {{kotak2d}}.** Dengan $\psi_{n_xn_y} = \psi_{n_x}(x)\psi_{n_y}(y)$, perturbasi $cxy$ berfaktor: $\langle n_x'n_y'|xy|n_xn_y\rangle = \langle n_x'|x|n_x\rangle\langle n_y'|y|n_y\rangle$. Diagonal: $\langle 12|xy|12\rangle = (L/2)(L/2) = L^2/4$, sama untuk $(2,1)$. Luar diagonal: $\langle 12|xy|21\rangle = \langle 1|x|2\rangle\langle 2|y|1\rangle = (16L/9\pi^2)^2 = 0{,}0324L^2$. Matriksnya $cL^2\begin{pmatrix}0{,}25 & 0{,}0324\\ 0{,}0324 & 0{,}25\end{pmatrix}$, dengan akar $cL^2(0{,}25 \pm 0{,}0324)$ dan fungsi $(\psi_{12} \pm \psi_{21})/\sqrt2$.

*Cara berpikir:* perturbasi $xy$ tidak bersimetri terhadap pertukaran sumbu secara terpisah, tetapi bersimetri terhadap pencerminan pada diagonal $x = y$. Kombinasi $\psi_{12} \pm \psi_{21}$ simetris dan antisimetris terhadap diagonal itu, sehingga simetri sudah menentukan fungsi orde nol yang benar sebelum menghitung. Kombinasi $+$ terpusat di sepanjang diagonal $x = y$ (tempat $xy$ besar) dan naik; kombinasi $-$ mempunyai simpul di diagonal dan naik lebih sedikit.

**Soal {{london}}.** Untuk dua atom sejenis dengan $\langle z^2\rangle = \langle x^2\rangle = \langle y^2\rangle$ (simetri bola) dan nilai rata-rata komponen nol, kuadrat (8.49) memberi suku-suku silang yang rata-ratanya nol, sehingga

$$
\langle\hat H'^2\rangle = \frac{1}{R^6}\left(\langle x^2\rangle^2 + \langle y^2\rangle^2 + 4\langle z^2\rangle^2\right) = \frac{6\langle z^2\rangle^2}{R^6} .
$$

Penyebut setiap suku orde kedua adalah energi eksitasi **kedua** atom, yang dalam pendekatan Unsöld $2I$. Jadi $E^{(2)} \approx -6\langle z^2\rangle^2/(2IR^6)$. Pendekatan Unsöld untuk satu atom memberi $\alpha = 2\langle z^2\rangle/I$, sehingga $\langle z^2\rangle = \alpha I/2$, dan

$$
E^{(2)} \approx -\frac{6}{2I}\cdot\frac{\alpha^2I^2}{4}\cdot\frac{1}{R^6} = -\frac{3I\alpha^2}{4R^6} .
$$

*Cara berpikir:* rumus London menyederhanakan dua kali (energi eksitasi rata-rata sama dengan $I$ untuk polarisabilitas dan untuk dispersi), dan kesalahan-kesalahan itu sebagian saling menghapus; hasilnya terlalu rendah 10–30% (Contoh 8.47). Struktur rumusnya yang penting: dispersi sebanding dengan kuadrat polarisabilitas dan dengan energi karakteristik elektron.

**Soal {{rabi}}.** Turunkan persamaan pertama sekali lagi dan masukkan yang kedua: $i\ddot c_i = (\Omega/2)\dot c_f = (\Omega/2)(-i)(\Omega/2)c_i$, jadi $\ddot c_i = -(\Omega/2)^2c_i$. Dengan $c_i(0) = 1$ dan $\dot c_i(0) = -i(\Omega/2)c_f(0) = 0$: $c_i = \cos(\Omega t/2)$. Dari persamaan pertama, $c_f = (2i/\Omega)\dot c_i = -i\sin(\Omega t/2)$. Jadi $P_{i\to f} = \sin^2(\Omega t/2)$, dan $|c_i|^2 + |c_f|^2 = 1$ pada setiap saat.

*Cara berpikir:* untuk $\Omega t \ll 1$, $\sin^2(\Omega t/2) \approx \Omega^2t^2/4$, tepat rumus orde pertama (8.54) pada resonansi. Teori perturbasi orde pertama adalah awal dari osilasi Rabi; ia gagal ketika populasi keadaan awal mulai berkurang secara berarti.

**Soal {{harmonik}}.** $Y_0^0 = 1/\sqrt{4\pi}$ dan $Y_1^0 = \sqrt{3/4\pi}\cos\theta$. Jadi $\cos\theta\,Y_0^0 = \cos\theta/\sqrt{4\pi} = Y_1^0/\sqrt3$. Karena harmonik bola ortonormal, $\langle Y_1^0|\cos\theta|Y_0^0\rangle = 1/\sqrt3$ dan $\langle Y_2^0|\cos\theta|Y_0^0\rangle = \langle Y_2^0|Y_1^0\rangle/\sqrt3 = 0$.

*Cara berpikir:* perkalian dengan $\cos\theta$ (komponen $z$ vektor satuan) mengubah $\ell$ tepat satu satuan. Inilah isi aturan seleksi $\Delta\ell = \pm1$ (8.57) dan $\Delta J = \pm1$ rotor tegar dalam kasus paling sederhana; hasil yang sama dipakai di Contoh 8.46 untuk efek Stark rotasi.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 8 dan 9. Metode variasi (termasuk variasi linear dan teorema MacDonald) dan teori perturbasi, dengan helium sebagai contoh utama.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 7. Metode pendekatan dengan banyak contoh numerik dan penerapan pada helium.
3. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 6. Teknik pendekatan, perturbasi bergantung waktu, aturan emas Fermi, dan polarisabilitas.
4. A. Szabo dan N. S. Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Bab 1 dan 6. Aljabar matriks untuk metode variasi linear dan teori perturbasi Møller–Plesset.
5. H. A. Bethe dan E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957). Rujukan klasik untuk helium, efek Stark, dan intensitas transisi atom.
6. A. J. Stone, *The Theory of Intermolecular Forces*, edisi ke-2 (Oxford University Press, 2013). Polarisabilitas, gaya dispersi, dan teori perturbasi untuk interaksi antarmolekul.
