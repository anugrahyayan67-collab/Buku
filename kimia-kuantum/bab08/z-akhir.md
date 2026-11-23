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

## Subbab 8.2: Teorema variasi

1. Mengapa metode variasi selalu memberi batas atas energi keadaan dasar, sedangkan teori perturbasi dapat memberi energi di bawah nilai eksak?

## Subbab 8.3: Fungsi uji sederhana; atom helium dengan muatan efektif

2. Sebuah fungsi uji memberi energi dengan galat 0,1%, tetapi momen dipolnya meleset 10%. Mengapa hal ini wajar?
3. Bagaimana simetri memungkinkan kita memperoleh batas atas untuk keadaan tereksitasi, padahal fungsi keadaan dasar eksak tidak diketahui?
4. Apa makna fisika muatan inti efektif $\zeta = 27/16$ untuk helium? Mengapa nilainya tidak 1 dan tidak 2?
5. Mengapa fungsi hasil kali dua orbital, betapa pun baiknya orbital itu, tidak dapat memberi energi eksak helium?

## Subbab 8.4: Fungsi variasi linear dan persamaan sekuler

6. Apa keuntungan fungsi variasi linear dibandingkan fungsi uji nonlinear, dan apa harga yang harus dibayar?
7. Apa makna teorema Hylleraas–Undheim–MacDonald bagi perhitungan spektrum elektronik?

## Subbab 8.5: Matriks, nilai eigen, diagonalisasi (dengan Python)

8. Mengapa kimia komputasi memakai fungsi Gauss, padahal fungsi eksponensial (Slater) lebih mirip orbital atom?

## Subbab 8.6: Perturbasi tak terdegenerasi orde pertama

9. Mengapa dua orbital yang energinya berdekatan bercampur kuat, sedangkan yang berjauhan hampir tidak bercampur? Berikan dua contoh kimia.
10. Apa beda makna fisika koreksi energi orde pertama dan orde kedua?

## Subbab 8.7: Orde kedua

11. Mengapa perturbasi orde kedua selalu menurunkan energi keadaan dasar? Hubungkan dengan teorema variasi.
12. Kapan deret perturbasi gagal, dan apa arti "deret asimtotik"?

## Subbab 8.9: Perturbasi tingkat terdegenerasi; keadaan tereksitasi helium

13. Mengapa keadaan triplet helium lebih rendah daripada singlet dari konfigurasi yang sama, padahal Hamiltoniannya tidak memuat spin?
14. Mengapa dalam atom berelektron banyak orbital 2s lebih rendah daripada 2p, padahal dalam hidrogen keduanya sama?

## Subbab 8.10: Efek Stark dan polarisabilitas

15. Mengapa atom tidak mempunyai momen dipol permanen, sedangkan HCl mempunyai? Mengapa HCl dalam keadaan $J = 0$ hanya menunjukkan efek Stark kuadratik?
16. Bagaimana gaya dispersi London muncul di antara dua atom yang tidak mempunyai dipol? Mengapa metode Hartree–Fock tidak dapat menangkapnya?
17. Mengapa molekul berwarna umumnya lebih mudah dipolarisasi daripada molekul tak berwarna yang berukuran sama?

## Subbab 8.11: Perturbasi bergantung waktu; interaksi radiasi dan materi

18. Bagaimana syarat frekuensi Bohr $\hbar\omega = E_f - E_i$ muncul dari teori perturbasi bergantung waktu?

## Subbab 8.12: Momen dipol transisi, aturan seleksi, aturan emas Fermi

19. Mengapa transisi d–d kompleks oktahedral lemah, sedangkan transisi transfer muatan kuat?
20. Bagaimana aturan emas Fermi menjelaskan bahwa keadaan tereksitasi meluruh secara eksponensial, dan bahwa garis spektrum mempunyai lebar alami?
21. Bagaimana teka-teki pembuka bab terjawab: bagaimana energi helium dapat dihitung lebih teliti daripada diukur, tanpa pernah menyelesaikan persamaan Schrödingernya?

# Soal

## Subbab 8.1: Mengapa perlu pendekatan

Pakai satuan atom ($1\ E_h = 27{,}211$ eV $= 2625{,}5$ kJ/mol $= 219\,475$ cm⁻¹; $1\ a_0 = 52{,}918$ pm) dan tetapan di Bab 1. Soal dikelompokkan menurut tingkat: **dasar**, **menengah**, dan **tantangan ★**. Soal bertanda **[P]** dibahas di akhir bab.

**Dasar**

**1.** Nyatakan energi helium tanpa tolakan antarelektron, $-4\ E_h$, dalam eV dan kJ/mol.

**2.** Berapa banyak koordinat ruang yang diperlukan untuk menggambarkan semua partikel (elektron dan inti) molekul H₂O? Berapa bila inti dianggap diam?

**3.** Hitung energi magnet $\mu_BB$ elektron dalam medan 10 T dalam eV, dan bandingkan dengan selisih tingkat elektronik khas 10 eV.

**Menengah**

**4.** Energi total benzena sekitar $-232\ E_h$. Berapa ketelitian relatif yang diperlukan untuk ketelitian kimia (1 kkal/mol)?

**5.** Berapa memori untuk menyimpan fungsi gelombang helium pada kisi 50 titik per koordinat (8 bita per nilai)?

**6.** Elektron dalam kotak 1,00 nm diberi medan $1{,}0 \times 10^7$ V/m sepanjang kotak. Hitung $|H'_{21}| = eF|\langle 2|x|1\rangle|$ dan perbandingannya terhadap $E_2 - E_1 = 1{,}128$ eV. Apakah syarat (8.2) terpenuhi?

**Tantangan ★**

**7.** ★ Pada kisi kasar 10 titik per koordinat, berapa elektron diperlukan agar jumlah nilai fungsi gelombang melampaui $10^{80}$ (jumlah atom di alam semesta teramati)?

## Subbab 8.2: Teorema variasi

**Dasar**

**8.** Hitung integral variasi untuk partikel dalam kotak dengan fungsi uji $x^2(L - x)^2$. Bandingkan dengan parabola $x(L - x)$.

**9.** Gunakan fungsi uji Gauss $e^{-\alpha r^2}$ untuk ion He⁺ ($Z = 2$). Tentukan $\alpha$ optimum dan $W$; bandingkan dengan $-2\ E_h$.

**10.** Untuk osilator harmonik dengan fungsi uji $e^{-\alpha x^2}$, tunjukkan bahwa $W = \hbar^2\alpha/2m + m\omega^2/8\alpha$ dan bahwa minimumnya eksak.

**11.** Fungsi uji $\psi_1 + 0{,}2\psi_2$ dipakai untuk partikel dalam kotak. Hitung $W/E_1$ dan kuadrat tumpang tindihnya dengan $\psi_1$ (setelah normalisasi).

**Menengah**

**12.** [P] Partikel dengan $\hbar = m = 1$ dalam potensial $V = |x|$. Gunakan fungsi uji $e^{-\alpha x^2}$ untuk menaksir energi keadaan dasar dan bandingkan dengan nilai eksak 0,8086.

**13.** Untuk atom hidrogen, gunakan fungsi uji $\phi = z\,e^{-\zeta r}$. (a) Untuk keadaan mana fungsi ini memberi batas atas, dan mengapa? (b) Tunjukkan bahwa $W = \tfrac12\zeta^2 - \tfrac12\zeta$ dan tentukan minimumnya.

**14.** Di titik optimum suatu fungsi uji atom, $\langle V\rangle = -1{,}90\ E_h$. Berapa $\langle T\rangle$ dan $W$?

**15.** Tunjukkan bahwa untuk potensial $V = cr^k$, fungsi uji yang ukurannya dioptimumkan memenuhi $2\langle T\rangle = k\langle V\rangle$.

**Tantangan ★**

**16.** [P] ★ Untuk keadaan 2p atom hidrogen gunakan fungsi uji $z\,e^{-ar^2}$. Diketahui $\langle T\rangle = 5a/2$ dan $\langle V\rangle = -\tfrac43\sqrt{2a/\pi}$. Tentukan $a$ dan $W$, lalu bandingkan dengan $-\tfrac18\ E_h$.

## Subbab 8.3: Fungsi uji sederhana; atom helium dengan muatan efektif

**Dasar**

**17.** Hitung $\zeta$ optimum, energi variasi (dalam eV), dan energi ionisasi Li⁺ → Li²⁺ menurut fungsi satu eksponen.

**18.** Berapa tolakan antarelektron rata-rata helium di titik optimum, dalam eV? Bandingkan dengan nilai pada $\zeta = 2$.

**19.** Hitung $\langle r\rangle$ elektron helium (pm) untuk $\zeta = 27/16$ dan untuk $\zeta = 1{,}70$ (aturan Slater).

**Menengah**

**20.** Untuk H⁻, tunjukkan bahwa fungsi satu eksponen memberi minimum di atas $-0{,}5\ E_h$.

**21.** Hitung $W(1{,}70)$ untuk helium dan bandingkan dengan $W$ optimum. Apa yang dikatakan hasil ini tentang bentuk $W(\zeta)$ di dekat minimum?

**22.** Hitung kerapatan elektron total di inti helium, $\rho(0) = 2\zeta^3/\pi$, untuk $\zeta = 27/16$. (Nilai teliti 3,62 $a_0^{-3}$.)

**23.** Dengan $\zeta = 27/16$, berapa bagian muatan elektron kedua yang berada di dalam bola berjari-jari $1\ a_0$, dan berapa muatan inti efektif yang dirasakan elektron pertama di jarak itu?

**Tantangan ★**

**24.** [P] ★ Fungsi satu eksponen meramalkan ion mirip helium terikat (terhadap pelepasan satu elektron) bila $(Z - \tfrac{5}{16})^2 > Z^2/2$. Hitung muatan inti kritis dan tafsirkan untuk H⁻.

## Subbab 8.4: Fungsi variasi linear dan persamaan sekuler

**Dasar**

**25.** Basis ortonormal dengan $H_{11} = -5$ eV, $H_{22} = -3$ eV, $H_{12} = -1$ eV. Hitung kedua akar persamaan sekuler.

**26.** Dua orbital setara: $\alpha = -11{,}0$ eV, $\beta = -2{,}5$ eV, $S = 0{,}2$. Hitung $W_\pm$.

**27.** Tuliskan determinan sekuler Hückel untuk alil (tiga atom berantai) dengan $x = (\alpha - E)/\beta$ dan selesaikan.

**Menengah**

**28.** Untuk basis $f_1 = x(L - x)$ dan $f_3 = x(L - x)(L - 2x)$ pada partikel dalam kotak, tunjukkan bahwa $H_{13} = S_{13} = 0$, lalu tuliskan kedua akarnya.

**29.** Untuk $H_{11} = 0$, $H_{22} = 1{,}0$ eV, $H_{12} = 0{,}2$ eV (basis ortonormal), hitung akar-akar dan sudut campuran $\theta$.

**30.** Untuk dua basis setara dengan tumpang tindih $S$, tunjukkan bahwa $\alpha - W_+ = -(\beta - \alpha S)/(1 + S)$ dan $W_- - \alpha = -(\beta - \alpha S)/(1 - S)$. Mana yang lebih besar bila $S > 0$?

**31.** Model Hückel imina C=N: $H_\text{NN} = \alpha + 0{,}5\beta$, $H_\text{CC} = \alpha$, $H_\text{CN} = \beta$. Hitung kedua akar dan bagian LUMO yang berada di karbon.

**32.** [P] Osilator kuartik $\tfrac12x^2 + 0{,}1x^4$ ($\hbar = m = \omega = 1$) dalam basis $\{|0\rangle, |2\rangle\}$. Diketahui $H_{00} = 0{,}575$, $H_{22} = 3{,}475$, $H_{02} = 0{,}2121$. Hitung akar-akarnya dan bandingkan dengan 0,559146.

**Tantangan ★**

**33.** ★ Jelaskan mengapa menambah satu fungsi basis tidak pernah menaikkan akar terendah persamaan sekuler.

## Subbab 8.5: Matriks, nilai eigen, diagonalisasi (dengan Python)

**Dasar**

**34.** Diagonalkan $\begin{pmatrix}1 & 2\\ 2 & 1\end{pmatrix}$: nilai eigen dan vektor eigen ternormalisasi.

**35.** Hitung $\mathbf S^{-1/2}$ untuk dua fungsi dengan tumpang tindih $S = 0{,}25$.

**36.** Hitung nilai eigen Hückel siklobutadiena (cincin empat atom). Apa akibatnya bagi empat elektron π?

**Menengah**

**37.** Dengan Python, diagonalkan matriks Hückel naftalena dan hitung energi π total serta celah HOMO–LUMO.

**38.** Basis empat fungsi Gauss bertempera rata untuk atom hidrogen dengan $\alpha_0 = 0{,}1348$ dan $\beta = 4{,}074$ ($\alpha_k = \alpha_0\beta^k$) memberi energi berapa? Bandingkan dengan empat Gauss teroptimum bebas.

**39.** Mengapa basis $\{|0\rangle, |1\rangle\}$ tidak memperbaiki energi keadaan dasar osilator $\tfrac12x^2 + \lambda x^4$ dibandingkan basis $\{|0\rangle\}$?

**40.** Dari Contoh 8.27, batas-s helium sekitar $-2{,}8790\ E_h$. Berapa bagian energi korelasi ($-0{,}0420\ E_h$) yang berupa korelasi radial?

**41.** Hitung sudut rotasi Jacobi yang mendiagonalkan $\begin{pmatrix}-5 & -1\\ -1 & -3\end{pmatrix}$.

**Tantangan ★**

**42.** ★ Untuk rantai Hückel $N$ atom, nilai eigennya $x_k = 2\cos[k\pi/(N + 1)]$. Periksa dengan Python untuk heksatriena ($N = 6$) dan hitung celah HOMO–LUMO.

## Subbab 8.6: Perturbasi tak terdegenerasi orde pertama

**Dasar**

**43.** Partikel dalam kotak diberi potensial $V_0$ hanya di separuh kiri kotak. Hitung $E_n^{(1)}$.

**44.** Osilator harmonik diberi perturbasi $cx^3$. Berapa $E_v^{(1)}$?

**45.** Osilator diberi perturbasi $bx^2$. Hitung $E_v^{(1)}$ dan bandingkan dengan uraian energi eksak.

**46.** Hitung pergeseran energi 1s hidrogen akibat gerak inti, $-(m_e/M)E_{1s}$, dalam cm⁻¹.

**Menengah**

**47.** [P] Inti hidrogen bukan titik, tetapi bola bermuatan seragam berjari-jari 0,84 fm. Tunjukkan bahwa pergeseran orde pertama 1s adalah $\tfrac25Z^4R^2$ (satuan atom) dan hitung dalam Hz.

**48.** Alil dengan heteroatom ($h = 0{,}5$) di atom tengah. Orbital alil: $(1, \sqrt2, 1)/2$, $(1, 0, -1)/\sqrt2$, $(1, -\sqrt2, 1)/2$. Hitung pergeseran orde pertama. Eksak: $x = 1{,}686$; 0; $-1{,}186$.

**49.** Ulangi untuk heteroatom di atom ujung. Eksak: 1,571; 0,242; $-1{,}313$.

**50.** Hitung koreksi relativistik orde pertama total $-Z^4\alpha_\text{f}^2/8$ untuk 1s ion C⁵⁺ dalam cm⁻¹ dan relatif terhadap $-Z^2/2$.

**51.** Mengapa koreksi massa inti orde pertama, $E \approx E^{(0)}(1 - m_e/M)$, gagal untuk positronium ($M = m_e$)? Berapa energi keadaan dasarnya yang benar?

**52.** Dalam Contoh 8.28, hitung koefisien campuran $a_4$ (pakai $\langle 4|x|1\rangle = -0{,}01441L$) dan bandingkan dengan $a_2$.

**Tantangan ★**

**53.** ★ Teorema Hellmann–Feynman menyatakan $dE/d\lambda = \langle\psi(\lambda)|\hat H'|\psi(\lambda)\rangle$ untuk $\hat H = \hat H^{(0)} + \lambda\hat H'$. Tunjukkan bahwa di $\lambda = 0$ teorema ini memberi $E^{(1)}$, dan bahwa turunannya memberi $2E^{(2)}$.

## Subbab 8.7: Orde kedua

**Dasar**

**54.** Dua tingkat berjarak 2,0 eV dikopel oleh 0,10 eV. Hitung pergeseran orde kedua tingkat bawah.

**55.** Ikatan dimodelkan sebagai muatan $e$ pada pegas $k = 500$ N/m dalam medan $1{,}0 \times 10^9$ V/m. Hitung pergeseran energinya.

**56.** Mengapa tolakan tingkat tidak pernah membuat dua tingkat yang terkopel berpotongan?

**Menengah**

**57.** Untuk $\lambda = 0{,}05$, bandingkan deret perturbasi keadaan dasar $\tfrac12x^2 + \lambda x^4$ sampai orde pertama dan kedua dengan nilai eksak 0,532643.

**58.** Hitung $E_0^{(2)}$ untuk osilator dengan perturbasi kubik $gx^3$, $g = 0{,}05$ ($\hbar = m = \omega = 1$).

**59.** Dengan rumus Morse $\omega_ex_e = \omega_e^2/4D_e$ (yang diturunkan dari perturbasi), ramalkan $\omega_ex_e$ HCl ($\omega_e = 2990{,}95$ cm⁻¹, $D_e = 4{,}618$ eV).

**60.** Untuk alil dengan heteroatom ($h = 0{,}5$) di atom ujung, hitung koreksi orde kedua orbital terendah dan bandingkan dengan nilai eksak 1,5707.

**Tantangan ★**

**61.** [P] ★ Untuk dua tingkat $0$ dan $\Delta$ yang dikopel oleh $V$, uraikan akar eksak tingkat bawah sampai $V^4$ dan tunjukkan bahwa $E^{(4)} = +V^4/\Delta^3$.

**62.** ★ Tunjukkan dengan argumen Dyson bahwa deret perturbasi untuk $\tfrac12x^2 + \lambda x^4$ tidak dapat konvergen untuk $\lambda$ sekecil apa pun.

## Subbab 8.8: Helium: perturbasi vs variasi

**Dasar**

**63.** Hitung $E^{(0)} + E^{(1)}$ untuk Li⁺ dalam eV.

**64.** Dengan deret $1/Z$ sampai orde kedua, hitung energi Be²⁺. Nilai eksak $-13{,}65557\ E_h$.

**65.** Nyatakan $E^{(1)}$ helium ($\tfrac54\ E_h$) dalam kJ/mol, dan bandingkan dengan energi ikatan C–C (sekitar 350 kJ/mol).

**Menengah**

**66.** Untuk ion mirip helium manakah $E^{(1)}$ tepat sepersepuluh $|E^{(0)}|$?

**67.** Berapa persen $\varepsilon_2$ yang ditangkap oleh suku $-25/256$ fungsi variasi? Apa yang tidak tertangkap?

**68.** Tunjukkan bahwa $W(\zeta = Z)$ fungsi variasi helium sama dengan $E^{(0)} + E^{(1)}$.

**Tantangan ★**

**69.** ★ Dengan deret $1/Z$ sampai $\varepsilon_3$, cari muatan inti kritis $Z_c$ di bawah mana ion mirip helium tidak terikat terhadap pelepasan satu elektron ($E = -Z^2/2$).

**70.** ★ Jelaskan dengan penskalaan mengapa $\varepsilon_2$ tidak bergantung pada $Z$.

## Subbab 8.9: Perturbasi tingkat terdegenerasi; keadaan tereksitasi helium

**Dasar**

**71.** Partikel pada cincin diberi perturbasi $V_0\cos4\phi$. Tingkat mana yang pecah pada orde pertama, dan berapa pemecahannya?

**72.** Hitung pemecahan singlet–triplet 1s2s helium menurut orde pertama, dalam eV, dan bandingkan dengan nilai eksak.

**73.** Berapa keadaan ruang yang terdegenerasi dalam $\hat H^{(0)}$ untuk konfigurasi 1s3d helium?

**Menengah**

**74.** Bandingkan $J_{1s2s} = 17Z/81$ dengan $\langle 1/r\rangle_{2s} = Z/4$. Berapa perbandingannya dan apa artinya?

**75.** Untuk pasangan antiikatan benzena ($x = -1$) dalam piridina ($h = 0{,}5$), hitung pergeseran orde pertama.

**76.** [P] Kotak persegi dua dimensi (sisi $L$, sudut di titik asal) diberi perturbasi $\hat H' = cxy$. Hitung pemecahan tingkat terdegenerasi $(n_x, n_y) = (1, 2), (2, 1)$.

**77.** Pirazina (N di posisi 1 dan 4 cincin benzena, $h = 0{,}5$): hitung pergeseran orde pertama pasangan $x = 1$. Eksak: 1,351 dan 1,000.

**Tantangan ★**

**78.** ★ Tiga orbital p diberi perturbasi aksial $c(3z^2 - r^2)$. Dengan $\langle p_z|3\cos^2\theta - 1|p_z\rangle = \tfrac45$ dan $\langle p_x|3\cos^2\theta - 1|p_x\rangle = -\tfrac25$, tentukan pemecahannya.

## Subbab 8.10: Efek Stark dan polarisabilitas

**Dasar**

**79.** Nyatakan polarisabilitas helium (1,383 $a_0^3$) dalam Å³ dan dalam C m²/V.

**80.** Hitung momen dipol terinduksi atom argon ($\alpha = 11{,}08\ a_0^3$) dalam medan $1{,}0 \times 10^8$ V/m, dalam debye.

**81.** Hitung pemecahan Stark linear $\pm3F$ tingkat $n = 2$ hidrogen dalam medan $1{,}0 \times 10^6$ V/m, dalam cm⁻¹.

**Menengah**

**82.** Taksir polarisabilitas helium dengan rumus Unsöld, memakai $\langle(z_1 + z_2)^2\rangle = 2\langle z^2\rangle$, $\langle z^2\rangle = 1/\zeta^2$ dengan $\zeta = 27/16$, dan $\Delta E = 0{,}904\ E_h$.

**83.** Berapa volume polarisabilitas elektron dalam kotak 2,0 nm?

**84.** Berapa pergeseran Stark OCS ($J = 0$) dalam medan $2{,}0 \times 10^5$ V/m?

**85.** Hitung $C_6$ London untuk pasangan Ar–Kr.

**86.** Hitung energi dispersi $-C_6/R^6$ untuk Ar–Ar ($C_6 = 64{,}3$) pada 3,8 Å, dalam cm⁻¹ dan kelvin.

**Tantangan ★**

**87.** [P] ★ Turunkan rumus London $C_6 = \tfrac34I\alpha^2$ untuk dua atom sejenis dari pendekatan Unsöld.

**88.** ★ Dengan fungsi $\psi^{(1)}$ Dalgarno–Lewis, tunjukkan bahwa momen dipol terinduksi atom hidrogen adalah $4{,}5F$.

## Subbab 8.11: Perturbasi bergantung waktu; interaksi radiasi dan materi

**Dasar**

**89.** Frekuensi Rabi suatu transisi adalah $\Omega/2\pi = 50$ kHz. Berapa periode Rabi dan lama pulsa $\pi$?

**90.** Pada resonansi, berapa $\Omega t$ ketika peluang transisi orde pertama mencapai 0,1?

**91.** Berapa lebar spektrum (cm⁻¹) pulsa Gauss 50 fs?

**Menengah**

**92.** Ion He⁺ dalam keadaan 1s mengalami perubahan muatan inti mendadak dari 2 menjadi 3. Hitung peluang ion Li²⁺ yang terbentuk berada di 1s.

**93.** Pada penalaan $\delta = 2\Omega$, berapa peluang transisi maksimum?

**94.** Dalam Contoh 8.53, berapa intensitas laser yang diperlukan agar periode Rabi menjadi 1,0 ns?

**95.** Hitung jarak persilangan kurva ionik–kovalen untuk NaBr ($A_\text{Br} = 3{,}364$ eV) dan KCl ($I_\text{K} = 4{,}341$ eV). Mana yang "melempar harpun" dari jarak lebih jauh?

**96.** Jelaskan mengapa transisi tidak terjadi bila perturbasi dinyalakan sangat lambat dibandingkan $1/\omega_{fi}$.

**Tantangan ★**

**97.** [P] ★ Untuk sistem dua tingkat tepat pada resonansi dengan pendekatan gelombang berputar, persamaan (8.52) menjadi $i\dot c_i = (\Omega/2)c_f$ dan $i\dot c_f = (\Omega/2)c_i$. Selesaikan dengan $c_i(0) = 1$.

## Subbab 8.12: Momen dipol transisi, aturan seleksi, aturan emas Fermi

**Dasar**

**98.** Untuk partikel dalam kotak, mana yang diizinkan: 1 → 2, 1 → 3, 2 → 5, 3 → 6?

**99.** Mana yang diizinkan pada atom hidrogen: 4f → 3d, 4f → 2p, 3s → 1s, 4p → 1s?

**100.** Pita serapan Gauss mempunyai $\varepsilon_\text{maks} = 2{,}0 \times 10^4$ L mol⁻¹ cm⁻¹ dan lebar 4000 cm⁻¹. Hitung kekuatan osilatornya.

**Menengah**

**101.** Transisi pada 300 nm mempunyai $|\mu_{fi}| = 5{,}0$ D. Hitung $A$ dan umur radiatifnya.

**102.** Berapa lebar garis alami ($A/2\pi$) keadaan dengan umur 10 ns?

**103.** Dalam kompleks oktahedral (berpusat inversi), mana yang diizinkan dipol: $t_{2g} \to e_g$, $t_{1u} \to t_{2g}$, $a_{1g} \to t_{1u}$?

**104.** Pada spektrum rotasi HCl ($B = 10{,}44$ cm⁻¹), di mana garis $J = 0 \to 1$? Apakah $J = 0 \to 2$ teramati?

**105.** Sebuah keadaan terkopel $0{,}010$ eV dengan kontinu yang kerapatannya 10 keadaan/eV. Hitung laju peluruhan dengan aturan emas dan umurnya.

**106.** Kekuatan osilator 1s → $n$p hidrogen: 0,4162; 0,0791; 0,0290; 0,0139; 0,0078; 0,0048 untuk $n = 2$ sampai 7. Taksir sumbangan kontinu dari aturan TRK.

**Tantangan ★**

**107.** [P] ★ Tunjukkan bahwa $\langle Y_1^0|\cos\theta|Y_0^0\rangle = 1/\sqrt3$ dan $\langle Y_2^0|\cos\theta|Y_0^0\rangle = 0$.

**108.** ★ Turunkan (8.59) dari (8.54) dengan menjumlahkan sumbangan setiap selang frekuensi radiasi dan merata-ratakan orientasi.


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | $-108{,}8$ eV; $-10\,502$ kJ/mol | 55 | $-q^2F^2/2k = -1{,}6 \times 10^{-4}$ eV |
| 2 | 39; 30 | 56 | setiap pasangan didorong menjauh; celah minimum $2|V|$ |
| 3 | $5{,}79 \times 10^{-4}$ eV; perbandingan $5{,}8 \times 10^{-5}$ | 57 | 0,537500 dan 0,530938; galat $+0{,}0049$ dan $-0{,}0017$ |
| 4 | $6{,}9 \times 10^{-6}$ | 58 | $-\tfrac{11}{8}g^2 = -0{,}00344$ |
| 5 | $1{,}56 \times 10^{10}$ nilai, 125 GB | 59 | $D_e = 37\,247$ cm⁻¹; $\omega_ex_e = 60{,}0$ cm⁻¹ (terukur 52,8) |
| 6 | $1{,}80 \times 10^{-3}$ eV; $1{,}6 \times 10^{-3}$; ya | 60 | $x = 1{,}5392 + 0{,}0276 = 1{,}5668$ |
| 7 | $10^{3N} > 10^{80}$: $N \ge 27$ (atom kobalt) | 61 | $E = -V^2/\Delta + V^4/\Delta^3 - \cdots$ |
| 8 | $W = 6\hbar^2/mL^2 = 1{,}216E_1$; lebih buruk daripada parabola ($1{,}013E_1$) | 62 | untuk $\lambda < 0$ potensial tak terbatas ke bawah; deret konvergen di $\lambda > 0$ akan konvergen juga di $-\lambda$ |
| 9 | $\alpha = 8Z^2/9\pi = 1{,}132$; $W = -4Z^2/3\pi = -1{,}698\ E_h$ (galat 15,1%) | 63 | $-7{,}125\ E_h = -193{,}9$ eV |
| 10 | $\alpha = m\omega/2\hbar$, $W = \tfrac12\hbar\omega$ | 64 | $-13{,}65767\ E_h$ (galat $-0{,}0021$) |
| 11 | $W = 1{,}115E_1$; 0,962 | 65 | 3282 kJ/mol, hampir sepuluh kali |
| 12 | $\alpha = (2\pi)^{-1/3} = 0{,}542$; $W = 0{,}8129$ (galat 0,53%) | 66 | $5Z/8 = Z^2/10$: $Z = 6{,}25$ (antara C⁴⁺ dan N⁵⁺) |
| 13 | (a) keadaan $\ell = 1$ terendah (2p), karena ortogonal pada semua keadaan s; (b) $\zeta = \tfrac12$, $W = -\tfrac18\ E_h$ (eksak) | 67 | 62%; korelasi elektron (radial dan sudut) |
| 14 | $0{,}95\ E_h$; $-0{,}95\ E_h$ | 68 | $Z^2 - 2Z^2 + 5Z/8$ |
| 15 | $W(s) = s^2T_1 + s^{-k}V_1$; $dW/ds = 0$ memberi $2T = kV$ | 69 | $Z_c \approx 0{,}93$ (nilai teliti 0,911); H⁻ terikat |
| 16 | $a = 32/225\pi = 0{,}0453$; $W = -16/45\pi = -0{,}1132\ E_h$ (galat 9,5%) | 70 | $\hat H = Z^2[\hat h(\rho) + Z^{-1}/\rho_{12}]$: koefisien $\lambda^2 = Z^{-2}$ dikali $Z^2$ |
| 17 | $\zeta = 2{,}6875$; $-7{,}2227\ E_h = -196{,}5$ eV; $74{,}1$ eV (eksak 75,6 eV) | 71 | $m = \pm2$: $\pm V_0/2$ |
| 18 | 28,7 eV; 34,0 eV | 72 | $2K = 2{,}39$ eV; eksak 0,80 eV |
| 19 | 47,0 pm; 46,7 pm | 73 | $2 \times 5 = 10$ |
| 20 | $\zeta = 11/16$, $W = -0{,}4727\ E_h > -0{,}5$ | 74 | 0,840; elektron 2s menembus awan 1s sehingga tolakan berkurang 16% |
| 21 | $-2{,}84750$ lawan $-2{,}84766\ E_h$; minimum sangat datar (selisih $1{,}6 \times 10^{-4}\ E_h$) | 75 | $x = -0{,}833$ dan $-1$ |
| 22 | 3,06 $a_0^{-3}$ (15% terlalu rendah) | 76 | $E^{(1)} = cL^2(0{,}25 \pm 0{,}0324)$; fungsi $(\psi_{12} \pm \psi_{21})/\sqrt2$ |
| 23 | $q = 1 - e^{-2\zeta}(1 + 2\zeta + 2\zeta^2) = 0{,}655$; $Z_\text{ef} = 1{,}34$ | 77 | $\psi_a$: $1 + 2h/3 = 1{,}333$; $\psi_b$: 1 |
| 24 | $Z_c = (5/16)/(1 - 1/\sqrt2) = 1{,}067$; H⁻ ($Z = 1$) diramalkan tak terikat | 78 | $p_z$: $+\tfrac45c\langle r^2\rangle$; $p_x$, $p_y$: $-\tfrac25c\langle r^2\rangle$ (tetap terdegenerasi); pusat berat tetap |
| 25 | $-4 \mp \sqrt2$: $-5{,}414$ dan $-2{,}586$ eV | 79 | 0,205 Å³; $2{,}28 \times 10^{-41}$ C m²/V |
| 26 | $-11{,}25$ eV dan $-10{,}63$ eV | 80 | $1{,}83 \times 10^{-32}$ C m $= 5{,}5 \times 10^{-3}$ D |
| 27 | $x^3 - 2x = 0$: $x = 0, \pm\sqrt2$, yaitu $E = \alpha \pm \sqrt2\beta$, $\alpha$ | 81 | $\pm1{,}28$ cm⁻¹ |
| 28 | integran ganjil terhadap $L/2$; $1{,}0132E_1$ dan $4{,}2555E_1$ | 82 | $\alpha \approx 1{,}55\ a_0^3$ (eksak 1,38) |
| 29 | $-0{,}0385$ dan $1{,}0385$ eV; $\theta = -10{,}9°$ | 83 | $16 \times 82{,}9 = 1327$ Å³ |
| 30 | aljabar langsung dari (8.21); destabilisasi lebih besar | 84 | $-14{,}2$ MHz |
| 31 | $x = 1{,}281$ dan $-0{,}781$; LUMO 62% di C | 85 | 75,9 satuan atom |
| 32 | 0,559565 dan 3,490435; galat akar terendah $4{,}2 \times 10^{-4}$ | 86 | $-103$ cm⁻¹, $-148$ K |
| 33 | ruang fungsi uji lama adalah bagian ruang baru; minimum atas ruang yang lebih besar tidak lebih tinggi | 87 | $\langle\hat H'^2\rangle = 6\langle z^2\rangle^2/R^6$, penyebut $2I$, dan $\alpha = 2\langle z^2\rangle/I$ |
| 34 | $-1$: $(1, -1)/\sqrt2$; $3$: $(1, 1)/\sqrt2$ | 88 | $\mu_\text{ind} = -2\langle\psi_{1s}|z|\psi^{(1)}\rangle = \tfrac23(\langle r^2\rangle + \tfrac12\langle r^3\rangle)F = 4{,}5F$ |
| 35 | diagonal 1,0246; luar diagonal $-0{,}1301$ | 89 | 20 µs; 10 µs |
| 36 | $x = 2, 0, 0, -2$; dua elektron di orbital nonikatan terdegenerasi (diradikal, antiaromatik) | 90 | $\Omega t = 2\sqrt{0{,}1} = 0{,}63$ |
| 37 | $x = \pm2{,}303, \pm1{,}618, \pm1{,}303, \pm1, \pm0{,}618$; $E_\pi = 10\alpha + 13{,}683\beta$; celah $1{,}236|\beta|$ | 91 | 294 cm⁻¹ |
| 38 | $-0{,}49875\ E_h$; $-0{,}49928\ E_h$ | 92 | $[8(6)^{3/2}/125]^2 = 0{,}885$ |
| 39 | $x^4$ tidak menghubungkan keadaan berparitas berbeda; $H_{01} = 0$ | 93 | $\tfrac15$ |
| 40 | $0{,}0173/0{,}0420 = 41$% | 94 | $\Omega \propto \sqrt I$: sekitar 130 W/cm² |
| 41 | $\tan2\theta = 1$, $\theta = 22{,}5°$ | 95 | 8,11 Å; 19,8 Å; KCl |
| 42 | $\pm1{,}802$, $\pm1{,}247$, $\pm0{,}445$; celah $0{,}890|\beta|$ | 96 | integral $\int H'e^{i\omega_{fi}t}dt$ hampir nol untuk fungsi yang berubah lambat (teorema adiabatik) |
| 43 | $V_0/2$ untuk semua $n$ | 97 | $c_i = \cos(\Omega t/2)$, $c_f = -i\sin(\Omega t/2)$, $P = \sin^2(\Omega t/2)$ |
| 44 | 0 (integran ganjil) | 98 | 1 → 2, 2 → 5, 3 → 6 |
| 45 | $b(v + \tfrac12)\hbar/m\omega$; eksak $\hbar\omega'(v + \tfrac12)$ dengan $\omega' = \omega\sqrt{1 + 2b/m\omega^2} \approx \omega + b/m\omega$ | 99 | 4f → 3d dan 4p → 1s |
| 46 | $+59{,}8$ cm⁻¹ (energi naik) | 100 | 0,37 |
| 47 | $R = 1{,}59 \times 10^{-5}\ a_0$; $1{,}01 \times 10^{-10}\ E_h = 0{,}67$ MHz | 101 | $A = 2{,}9 \times 10^8$ s⁻¹; 3,4 ns |
| 48 | $x = 1{,}664$; 0; $-1{,}164$ | 102 | 15,9 MHz |
| 49 | $x = 1{,}539$; 0,250; $-1{,}289$ | 103 | $t_{1u} \to t_{2g}$ dan $a_{1g} \to t_{1u}$ (g ↔ u) |
| 50 | $-0{,}00863\ E_h = -1893$ cm⁻¹; $4{,}8 \times 10^{-4}$ | 104 | 20,88 cm⁻¹; tidak ($\Delta J = \pm1$) |
| 51 | $m_e/M = 1$ tidak kecil (ramalan $E = 0$); eksak $\mu = m_e/2$, $E = -0{,}25\ E_h$ | 105 | $9{,}5 \times 10^{12}$ s⁻¹; 0,10 ps |
| 52 | $a_4 = 2{,}6 \times 10^{-4}$; $a_2/a_4 \approx 63$ | 106 | $1 - 0{,}551 = 0{,}449$, dikurangi ekor $n > 7$ (sekitar 0,014): kontinu $\approx 0{,}435$ |
| 53 | $dE/d\lambda|_0 = H'_{nn}$; $d^2E/d\lambda^2|_0 = 2\langle\psi^{(0)}|\hat H'|\psi^{(1)}\rangle = 2E^{(2)}$ | 107 | $\cos\theta\,Y_0^0 = Y_1^0/\sqrt3$ |
| 54 | $-0{,}005$ eV | 108 | $F_0^2 = 2\rho_\omega d\omega/\varepsilon_0$; $\int\sin^2(\Delta t/2)/\Delta^2 d\Delta = \pi t/2$; $\langle\mu_z^2\rangle = |\mu|^2/3$ |
:::


# Pembahasan soal terpilih

**Soal 12.** Untuk Gauss ternormalisasi $(2\alpha/\pi)^{1/4}e^{-\alpha x^2}$: $\langle T\rangle = \alpha/2$ dan $\langle|x|\rangle = 2\sqrt{2\alpha/\pi}\int_0^\infty xe^{-2\alpha x^2}dx = 1/\sqrt{2\pi\alpha}$. Jadi $W(\alpha) = \alpha/2 + (2\pi\alpha)^{-1/2}$. Syarat minimum $\tfrac12 - \tfrac12(2\pi)^{-1/2}\alpha^{-3/2} = 0$ memberi $\alpha^{3/2} = (2\pi)^{-1/2}$, $\alpha = (2\pi)^{-1/3} = 0{,}5419$. Di titik itu $(2\pi\alpha)^{-1/2} = \alpha$, sehingga $W = \tfrac32\alpha = 0{,}8129$. Nilai eksak adalah $2^{-1/3}a_1'$, dengan $a_1' = 1{,}0188$ nol pertama turunan fungsi Airy: 0,8086. Galatnya 0,53%.

*Cara berpikir:* periksa teorema virial untuk $V \propto |x|^1$: $2\langle T\rangle = \langle V\rangle$, dan memang $\alpha = 2(\alpha/2)$. Gauss cocok karena keadaan dasar potensial berbentuk V bersifat simetris, tanpa simpul, dan meluruh cepat; galatnya kecil walaupun fungsi eksaknya (fungsi Airy) sama sekali bukan Gauss.

**Soal 16.** $W(a) = \tfrac52a - \tfrac43\sqrt{2a/\pi}$. Turunannya nol bila $\tfrac52 = \tfrac23\sqrt{2/\pi}\,a^{-1/2}$, yaitu $\sqrt a = \tfrac{4}{15}\sqrt{2/\pi}$ dan $a = 32/225\pi = 0{,}0453$. Maka $\tfrac52a = 16/45\pi$ dan $\tfrac43\sqrt{2a/\pi} = \tfrac43\cdot\tfrac{4}{15}\cdot\tfrac2\pi = 32/45\pi$, sehingga $W = -16/45\pi = -0{,}1132\ E_h$. Galat terhadap $-0{,}125$: 9,5%. Fungsi ini batas atas untuk 2p (bukan 1s) karena berbentuk $z\times$(fungsi bersimetri bola), sehingga ortogonal pada semua keadaan s.

*Cara berpikir:* galat Gauss untuk 2p (9,5%) lebih kecil daripada untuk 1s (15,1%, Contoh 8.5). Fungsi p nol di inti, sehingga ketidakmampuan Gauss membentuk puncak lancip tidak terlalu merugikan; yang tersisa hanyalah ekor yang meluruh terlalu cepat.

**Soal 24.** Ion terikat bila energinya di bawah energi ion satu elektron ditambah elektron bebas diam: $-(Z - \tfrac{5}{16})^2 < -Z^2/2$, yaitu $Z - \tfrac{5}{16} > Z/\sqrt2$, atau $Z(1 - 1/\sqrt2) > \tfrac{5}{16}$. Jadi $Z > 0{,}3125/0{,}2929 = 1{,}067$. H⁻ ($Z = 1$) berada di bawah batas ini, sehingga diramalkan tak terikat.

*Cara berpikir:* perhitungan yang sangat teliti menunjukkan muatan kritis sebenarnya $Z_c = 0{,}911$, cukup jauh di bawah 1, sehingga H⁻ terikat dengan selisih yang nyaman (0,754 eV). Galat fungsi satu eksponen (sekitar $0{,}055\ E_h$, Contoh 8.13) cukup besar untuk menggeser $Z_c$ melewati 1. Pelajarannya: ketika jawaban kualitatif (terikat atau tidak) bergantung pada selisih kecil, fungsi uji harus dibuat lebih lentur, seperti fungsi dua eksponen di Contoh 8.14.

**Soal 32.** Persamaan sekuler $(0{,}575 - W)(3{,}475 - W) - 0{,}2121^2 = 0$, atau $W^2 - 4{,}05W + 1{,}9531 = 0$. Akar: $W = [4{,}05 \mp \sqrt{16{,}4025 - 7{,}8125}]/2 = (4{,}05 \mp 2{,}9309)/2$, yaitu 0,55956 dan 3,49044. Akar terendah hanya $4{,}2 \times 10^{-4}$ di atas nilai eksak.

*Cara berpikir:* unsur diagonal $H_{00} = 0{,}575$ adalah energi perturbasi orde pertama; pergeseran akibat pencampuran dengan $|2\rangle$, $-0{,}0154$, hampir sama dengan $-H_{02}^2/(H_{22} - H_{00}) = -0{,}0155$, yaitu bagian orde kedua dari keadaan $|2\rangle$. Dua fungsi basis yang dipilih dengan simetri yang benar (keduanya genap) sudah cukup; menambah $|1\rangle$ tidak berguna karena ganjil.

**Soal 47.** Di dalam bola bermuatan seragam berjari-jari $R$, potensialnya $-(Z/2R)(3 - r^2/R^2)$; di luar, $-Z/r$. Perturbasinya adalah selisih keduanya, hanya untuk $r < R$: $\Delta V = Z/r - (Z/2R)(3 - r^2/R^2)$. Karena $R \ll a_0$, $|\psi_{1s}|^2 \approx Z^3/\pi$ di seluruh inti:

$$
E^{(1)} \approx \frac{Z^3}{\pi}\int_0^R\Delta V\,4\pi r^2dr = 4Z^4\left[\frac{R^2}{2} - \frac{1}{2R}\left(R^3 - \frac{R^3}{5}\right)\right] = \frac25Z^4R^2 .
$$

Untuk hidrogen, $R = 0{,}84$ fm $= 1{,}59 \times 10^{-5}\ a_0$, $E^{(1)} = 1{,}01 \times 10^{-10}\ E_h$, atau $0{,}67$ MHz. Tandanya positif: muatan yang tersebar menarik elektron lebih lemah daripada muatan titik.

*Cara berpikir:* pergeseran ini kecil tetapi terukur dengan spektroskopi laser hidrogen; perbedaan jari-jari proton yang diperoleh dari hidrogen biasa dan hidrogen muonik (yang muonnya 207 kali lebih dekat ke inti, sehingga efeknya jutaan kali lebih besar) menjadi "teka-teki jari-jari proton" sejak 2010. Bagi kimiawan, efek yang sama sebanding dengan $Z^4$ dan dengan perubahan jari-jari inti antarisotop. Pada unsur berat seperti uranium dan raksa, "efek volume inti" ini menggeser kesetimbangan kimia antarisotop dan ikut menentukan fraksionasi isotop ²³⁵U/²³⁸U di alam.

**Soal 61.** Akar bawah $E = \tfrac\Delta2 - \tfrac\Delta2\sqrt{1 + u}$ dengan $u = 4V^2/\Delta^2$. Deret $\sqrt{1 + u} = 1 + \tfrac u2 - \tfrac{u^2}{8} + \cdots$ memberi

$$
E = -\frac\Delta2\left(\frac{2V^2}{\Delta^2} - \frac{2V^4}{\Delta^4} + \cdots\right) = -\frac{V^2}{\Delta} + \frac{V^4}{\Delta^3} - \cdots
$$

Suku pertama adalah $E^{(2)}$ (8.35); suku kedua $E^{(4)} = +V^4/\Delta^3$. Orde ganjil nol karena perturbasi tidak mempunyai unsur diagonal.

*Cara berpikir:* deret ini konvergen hanya bila $u < 1$, yaitu $|V| < \Delta/2$. Bila kopling lebih besar daripada setengah selisih energi, tidak ada orde yang cukup; diagonalisasi matriks 2 × 2 adalah satu-satunya jalan. Ini sesuai Contoh 8.34: galat orde kedua sudah 21% pada $V/\Delta = 0{,}5$.

**Soal 76.** Dengan $\psi_{n_xn_y} = \psi_{n_x}(x)\psi_{n_y}(y)$, perturbasi $cxy$ berfaktor: $\langle n_x'n_y'|xy|n_xn_y\rangle = \langle n_x'|x|n_x\rangle\langle n_y'|y|n_y\rangle$. Diagonal: $\langle 12|xy|12\rangle = (L/2)(L/2) = L^2/4$, sama untuk $(2,1)$. Luar diagonal: $\langle 12|xy|21\rangle = \langle 1|x|2\rangle\langle 2|y|1\rangle = (16L/9\pi^2)^2 = 0{,}0324L^2$. Matriksnya $cL^2\begin{pmatrix}0{,}25 & 0{,}0324\\ 0{,}0324 & 0{,}25\end{pmatrix}$, dengan akar $cL^2(0{,}25 \pm 0{,}0324)$ dan fungsi $(\psi_{12} \pm \psi_{21})/\sqrt2$.

*Cara berpikir:* perturbasi $xy$ tidak bersimetri terhadap pertukaran sumbu secara terpisah, tetapi bersimetri terhadap pencerminan pada diagonal $x = y$. Kombinasi $\psi_{12} \pm \psi_{21}$ simetris dan antisimetris terhadap diagonal itu, sehingga simetri sudah menentukan fungsi orde nol yang benar sebelum menghitung. Kombinasi $+$ terpusat di sepanjang diagonal $x = y$ (tempat $xy$ besar) dan naik; kombinasi $-$ mempunyai simpul di diagonal dan naik lebih sedikit.

**Soal 87.** Untuk dua atom sejenis dengan $\langle z^2\rangle = \langle x^2\rangle = \langle y^2\rangle$ (simetri bola) dan nilai rata-rata komponen nol, kuadrat (8.49) memberi suku-suku silang yang rata-ratanya nol, sehingga

$$
\langle\hat H'^2\rangle = \frac{1}{R^6}\left(\langle x^2\rangle^2 + \langle y^2\rangle^2 + 4\langle z^2\rangle^2\right) = \frac{6\langle z^2\rangle^2}{R^6} .
$$

Penyebut setiap suku orde kedua adalah energi eksitasi **kedua** atom, yang dalam pendekatan Unsöld $2I$. Jadi $E^{(2)} \approx -6\langle z^2\rangle^2/(2IR^6)$. Pendekatan Unsöld untuk satu atom memberi $\alpha = 2\langle z^2\rangle/I$, sehingga $\langle z^2\rangle = \alpha I/2$, dan

$$
E^{(2)} \approx -\frac{6}{2I}\cdot\frac{\alpha^2I^2}{4}\cdot\frac{1}{R^6} = -\frac{3I\alpha^2}{4R^6} .
$$

*Cara berpikir:* rumus London menyederhanakan dua kali (energi eksitasi rata-rata sama dengan $I$ untuk polarisabilitas dan untuk dispersi), dan kesalahan-kesalahan itu sebagian saling menghapus; hasilnya terlalu rendah 10–30% (Contoh 8.50). Struktur rumusnya yang penting: dispersi sebanding dengan kuadrat polarisabilitas dan dengan energi karakteristik elektron.

**Soal 97.** Turunkan persamaan pertama sekali lagi dan masukkan yang kedua: $i\ddot c_i = (\Omega/2)\dot c_f = (\Omega/2)(-i)(\Omega/2)c_i$, jadi $\ddot c_i = -(\Omega/2)^2c_i$. Dengan $c_i(0) = 1$ dan $\dot c_i(0) = -i(\Omega/2)c_f(0) = 0$: $c_i = \cos(\Omega t/2)$. Dari persamaan pertama, $c_f = (2i/\Omega)\dot c_i = -i\sin(\Omega t/2)$. Jadi $P_{i\to f} = \sin^2(\Omega t/2)$, dan $|c_i|^2 + |c_f|^2 = 1$ pada setiap saat.

*Cara berpikir:* untuk $\Omega t \ll 1$, $\sin^2(\Omega t/2) \approx \Omega^2t^2/4$, tepat rumus orde pertama (8.54) pada resonansi. Teori perturbasi orde pertama adalah awal dari osilasi Rabi; ia gagal ketika populasi keadaan awal mulai berkurang secara berarti.

**Soal 107.** $Y_0^0 = 1/\sqrt{4\pi}$ dan $Y_1^0 = \sqrt{3/4\pi}\cos\theta$. Jadi $\cos\theta\,Y_0^0 = \cos\theta/\sqrt{4\pi} = Y_1^0/\sqrt3$. Karena harmonik bola ortonormal, $\langle Y_1^0|\cos\theta|Y_0^0\rangle = 1/\sqrt3$ dan $\langle Y_2^0|\cos\theta|Y_0^0\rangle = \langle Y_2^0|Y_1^0\rangle/\sqrt3 = 0$.

*Cara berpikir:* perkalian dengan $\cos\theta$ (komponen $z$ vektor satuan) mengubah $\ell$ tepat satu satuan. Inilah isi aturan seleksi $\Delta\ell = \pm1$ (8.57) dan $\Delta J = \pm1$ rotor tegar dalam kasus paling sederhana; hasil yang sama dipakai di Contoh 8.49 untuk efek Stark rotasi.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 8 dan 9. Metode variasi (termasuk variasi linear dan teorema MacDonald) dan teori perturbasi, dengan helium sebagai contoh utama.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 7. Metode pendekatan dengan banyak contoh numerik dan penerapan pada helium.
3. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 6. Teknik pendekatan, perturbasi bergantung waktu, aturan emas Fermi, dan polarisabilitas.
4. A. Szabo dan N. S. Ostlund, *Modern Quantum Chemistry* (Dover, 1996), Bab 1 dan 6. Aljabar matriks untuk metode variasi linear dan teori perturbasi Møller–Plesset.
5. H. A. Bethe dan E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957). Rujukan klasik untuk helium, efek Stark, dan intensitas transisi atom.
6. A. J. Stone, *The Theory of Intermolecular Forces*, edisi ke-2 (Oxford University Press, 2013). Polarisabilitas, gaya dispersi, dan teori perturbasi untuk interaksi antarmolekul.
