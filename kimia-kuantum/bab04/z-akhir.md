# Ringkasan Bab 4

| Gagasan | Rumus | Subbab |
|---|---|---|
| Operator linear | $\hat A(c_1f + c_2g) = c_1\hat Af + c_2\hat Ag$ | 4.1 |
| Komutator kanonik | $[\hat x, \hat p_x] = i\hbar$; $\ [\hat A, \hat B\hat C] = [\hat A, \hat B]\hat C + \hat B[\hat A, \hat C]$ | 4.1 |
| Persamaan nilai eigen | $\hat Af = af$; kombinasi fungsi eigen terdegenerasi tetap fungsi eigen | 4.2 |
| Operator dasar | $\hat x = x$; $\ \hat p_x = -i\hbar\,\partial_x$; $\ \hat L_z = -i\hbar\,\partial_\phi$ | 4.3 |
| Hamiltonian molekul | kinetik inti + kinetik elektron + tarikan e–inti + tolakan e–e + tolakan inti–inti | 4.4 |
| Pemisahan variabel | $\hat H = \hat H_1 + \hat H_2 \Rightarrow \psi = \psi_a\psi_b$, $E = E_a + E_b$ | 4.4 |
| Kotak 3D | $E = \tfrac{h^2}{8m}\left(\tfrac{n_x^2}{a^2} + \tfrac{n_y^2}{b^2} + \tfrac{n_z^2}{c^2}\right)$ | 4.5 |
| Energi Fermi | $E_F = \tfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$ | 4.5 |
| Nilai harap | $\langle A\rangle = \int\psi^*\hat A\psi\,d\tau$ | 4.6 |
| Teorema Ehrenfest | $\tfrac{d}{dt}\langle A\rangle = \tfrac i\hbar\langle[\hat H, \hat A]\rangle$; $\ \tfrac{d\langle x\rangle}{dt} = \tfrac{\langle p\rangle}{m}$, $\ \tfrac{d\langle p\rangle}{dt} = -\langle V'\rangle$ | 4.6 |
| Syarat fungsi gelombang | bernilai tunggal, malar, turunan malar ($V$ berhingga), dapat dinormalisasi | 4.7 |
| Hermitian | $\int f^*\hat Ag = \int g(\hat Af)^*$; nilai eigen riil, fungsi eigen ortogonal | 4.8 |
| Ekspansi | $\psi = \sum c_n\phi_n$, $\ c_n = \langle\phi_n|\psi\rangle$, $\ \sum|c_n|^2 = 1$ | 4.9 |
| Komut ⇔ fungsi eigen bersama | $[\hat A, \hat B] = 0$ | 4.10 |
| Relasi Robertson | $\Delta A\,\Delta B \ge \tfrac12|\langle[\hat A, \hat B]\rangle|$ | 4.10 |
| Paritas; Laporte | $\hat\Pi\psi_{n\ell m} = (-1)^\ell\psi_{n\ell m}$; transisi hanya g ↔ u | 4.11 |
| Pengukuran | hasil = nilai eigen; peluang $|c_n|^2$; sesudahnya keadaan $\phi_n$ | 4.12 |
| Evolusi waktu | $\Psi(t) = e^{-i\hat Ht/\hbar}\Psi(0)$ | 4.13 |
| Notasi Dirac | $\langle m|\hat A|n\rangle = A_{mn}$; $\ \sum|n\rangle\langle n| = \hat 1$; $\ \mathbf{Hc} = E\mathbf c$ | 4.14 |

**Jawaban kuis cepat.** **4.1** $[\hat D, x^3]f = (x^3f)' - x^3f' = 3x^2f$, jadi $3x^2$. Tidak: $[\hat D, e^x] = e^x$. **4.2** Tidak; $\hat A(f + g) = af + bg$, bukan kelipatan $f + g$ jika $a \ne b$. **4.3** $-\hbar^2(\partial_x^2 + \partial_y^2)$; $\tfrac12\kappa(x^2 + y^2 + z^2)$. **4.4** $3 \times \tfrac12h\nu = \tfrac32h\nu$. **4.5** Enam: semua permutasi $(1, 2, 3)$. **4.6** Nol; setiap pengukuran memberi nilai eigen yang sama. **4.7** $\cos(3\phi/2)$ tidak (berubah tanda setelah satu putaran); $\cos 3\phi$ ya. **4.8** $\hat x^2$ ya; $i\hat x$ tidak (anti-Hermitian); $\hat p_x^2$ ya. **4.9** 0,20. **4.10** Ya; ya. **4.11** u; 3d → 4s g → g, terlarang; 3d → 4p g → u, diizinkan. **4.12** Sekitar 100 kali; tidak pernah. **4.13** Postulat 3 (dengan Postulat 2); Postulat 6. **4.14** (a) $\langle\psi|\psi\rangle = 1$; (b) $\langle\phi|\psi\rangle = 0$; (c) $\langle\psi|\hat H|\psi\rangle$; (d) $|\langle n|\psi\rangle|^2$.

# Pertanyaan

1. Mengapa operator besaran fisis harus linear? Apa hubungannya dengan asas superposisi?
2. Mengapa urutan operator penting? Beri contoh dua operator yang tidak komut dan makna fisisnya.
3. Apa arti degenerasi, dan mengapa kita bebas memilih basis dalam ruang terdegenerasi?
4. Orbital $p_x$ dan $p_{+1}$: mana yang "benar"? Kapan masing-masing lebih berguna?
5. Mengapa operator momentum memuat $i$?
6. Mengapa suku tolakan elektron–elektron mencegah pemisahan variabel dalam atom berelektron banyak?
7. Bagaimana simetri menghasilkan degenerasi, dan bagaimana penurunan simetri memecahnya? Beri contoh kimia.
8. Mengapa elektron dalam logam hampir tidak menyumbang pada kapasitas kalor, padahal jumlahnya sangat banyak?
9. Apa beda nilai harap dan nilai eigen? Kapan keduanya sama?
10. Dalam arti apa mekanika Newton adalah limit mekanika kuantum (teorema Ehrenfest)?
11. Mengapa fungsi gelombang harus bernilai tunggal? Apa akibatnya bagi momentum sudut?
12. Mengapa nilai eigen operator Hermitian riil? Mengapa fungsi eigennya ortogonal?
13. Apa arti kelengkapan, dan mengapa dalam praktik basis selalu dipotong? Apa akibatnya?
14. Mengapa dua besaran yang operatornya komut dapat diukur serentak dengan tajam?
15. Bagaimana relasi ketidakpastian Heisenberg mengikuti dari komutator?
16. Mengapa transisi d–d dalam kompleks oktahedral lemah? Mengapa kompleks tetrahedral lebih berwarna?
17. Apa yang terjadi pada fungsi gelombang ketika diukur? Mengapa pengukuran mengganggu?
18. Apa beda superposisi dan campuran statistik? Mengapa benda makroskopik tidak teramati dalam superposisi?
19. Sebutkan postulat-postulat mekanika kuantum dengan kalimatmu sendiri.
20. Mengapa persamaan Schrödinger dapat diubah menjadi soal diagonalisasi matriks? Apa hubungannya dengan kimia komputasi?
21. Mengapa Heisenberg dan Schrödinger, dengan matematika yang tampak berbeda, memperoleh hasil yang sama?

# Soal

## Subbab 4.1: Operator dan aljabarnya

Gunakan tetapan di Bab 1. Soal dikelompokkan menurut tingkat: **dasar**, **menengah**, dan **tantangan ★**. Soal bertanda **[P]** dibahas di akhir bab.

**Dasar**

**1.** Hitung $\hat Af$ untuk (a) $\hat A = d^2/dx^2 + 2x$, $f = x^3$; (b) $\hat A = x\,d/dx$, $f = e^{2x}$; (c) $\hat A = \hat\Pi$, $f = x^2 + x$.

**2.** Apakah operator $\hat Af = \sin f$ linear? Apakah $\hat Bf = x\,df/dx$?

**3.** Hitung $[\hat x, d^2/dx^2]$ dengan fungsi uji.

**Menengah**

**4.** [P] Hitung $[\hat x^n, \hat p_x]$ dan $[\hat x, \hat p_x^n]$ untuk $n$ bulat positif.

**5.** Hitung $(d/dx + x)(d/dx - x)f$ dan $(d/dx - x)(d/dx + x)f$, lalu komutatornya.

**6.** Tunjukkan bahwa $[\hat A, \hat B\hat C] = [\hat A, \hat B]\hat C + \hat B[\hat A, \hat C]$.

**7.** Hitung $[\hat H, x^2]$ untuk $\hat H = -\tfrac{\hbar^2}{2m}\tfrac{d^2}{dx^2} + V(x)$.

**Tantangan ★**

**8.** ★ Tunjukkan bahwa $e^{a\,d/dx}f(x) = f(x + a)$ (operator translasi), dengan deret Taylor. Apa hubungannya dengan $\hat p_x$?

## Subbab 4.2: Fungsi eigen dan nilai eigen

**Dasar**

**9.** Manakah fungsi eigen $d^2/dx^2$: $e^{3x}$, $\cos 2x + \sin 2x$, $x^2$, $\sinh x$? Berapa nilai eigennya?

**10.** Fungsi $e^{-x^2/2}$ adalah fungsi eigen $-d^2/dx^2 + x^2$. Berapa nilai eigennya?

**11.** Apakah $x e^{-x^2/2}$ fungsi eigen operator yang sama? Nilai eigennya?

**Menengah**

**12.** [P] Tunjukkan bahwa $\cos kx$ dan $\sin kx$ adalah fungsi eigen $d^2/dx^2$ yang terdegenerasi, dan bahwa $e^{ikx}$ adalah kombinasinya yang sekaligus fungsi eigen $d/dx$.

**13.** Cari fungsi eigen dan nilai eigen $d/dx$ pada $[0, L]$ dengan syarat $f(0) = f(L)$ (syarat periodik).

**14.** Untuk $\hat A = x\,d/dx$, tunjukkan bahwa $x^n$ fungsi eigen. Berapa nilai eigennya?

**15.** Apakah $\cos kx$ fungsi eigen $\hat p_x^2$? Bila ya, berapa nilai eigennya?

**Tantangan ★**

**16.** ★ Tunjukkan bahwa jika $f$ fungsi eigen $\hat A$ dengan nilai eigen $a$, maka $f$ fungsi eigen $\hat A^2$ dengan nilai eigen $a^2$ dan fungsi eigen $e^{\hat A}$ dengan nilai eigen $e^a$.

## Subbab 4.3: Operator besaran fisika

**Dasar**

**17.** Tuliskan operator untuk $p_x^2 + p_y^2 + p_z^2$ dan energi kinetik dalam koordinat Kartesius.

**18.** Tuliskan operator $\hat L_x = \hat y\hat p_z - \hat z\hat p_y$ dalam bentuk turunan.

**19.** Apakah $e^{3i\phi}$ fungsi eigen $\hat L_z$? Nilai eigennya? Apakah $e^{i\phi}\sin\theta$?

**Menengah**

**20.** Untuk $e^{im\phi}$ pada cincin, mengapa $m$ harus bulat? Mengapa $m = 1/2$ ditolak?

**21.** Tunjukkan bahwa $\hat L_z$ bekerja pada $x + iy$ memberikan $\hbar(x + iy)$.

**22.** Tuliskan operator momen dipol untuk molekul H₂O (inti O, dua H, 10 elektron). Mengapa tidak bergantung pada titik asal?

**Tantangan ★**

**23.** ★ Turunkan $\hat L_z = -i\hbar\,\partial/\partial\phi$ dalam koordinat silinder $(\rho, \phi, z)$ dan tunjukkan hasilnya sama.

## Subbab 4.4: Persamaan Schrödinger tiga dimensi dan banyak partikel

**Dasar**

**24.** Tuliskan operator Hamilton ion H₂⁺ (dua proton dan satu elektron), lengkap dengan energi kinetik inti.

**25.** Tuliskan operator Hamilton atom litium dengan inti diam. Berapa koordinat ruang elektron?

**26.** Berapa suku tolakan elektron–elektron untuk molekul air?

**Menengah**

**27.** Tiga elektron tak berinteraksi dalam kotak satu dimensi (abaikan asas Pauli). Berapa energi keadaan dasar dan tereksitasi pertama dalam $E_1$? Degenerasinya?

**28.** Hitung energi litium jika semua tolakan elektron diabaikan dan ketiga elektron di 1s (abaikan asas Pauli), lalu jika dua di 1s dan satu di 2s. Bandingkan dengan nilai percobaan $-203{,}5$ eV.

**29.** [P] Tunjukkan bahwa jika $\hat H = \hat H_x + \hat H_y$, maka $\psi(x, y) = X(x)Y(y)$ dengan $\hat H_xX = E_xX$, $\hat H_yY = E_yY$ memenuhi $\hat H\psi = (E_x + E_y)\psi$.

**30.** Berapa suku Coulomb dalam operator Hamilton lengkap molekul NH₃ (10 elektron, 4 inti)?

**Tantangan ★**

**31.** ★ Untuk dua partikel dengan massa berbeda yang hanya berinteraksi satu sama lain, $V(|\mathbf r_1 - \mathbf r_2|)$, tunjukkan bahwa dengan koordinat pusat massa dan koordinat relatif Hamiltoniannya terpisah, dengan massa tereduksi $\mu$ untuk gerak relatif.

## Subbab 4.5: Kotak tiga dimensi dan degenerasi

**Dasar**

**32.** Hitung $E_{111}$ dan $E_{222}$ untuk elektron dalam kubus 0,50 nm.

**33.** Berapa degenerasi tingkat $n_x^2 + n_y^2 + n_z^2 = 11$, 14, 21, dan 27?

**34.** Tuliskan fungsi gelombang ternormalisasi $\psi_{123}$ untuk kubus bersisi $L$.

**Menengah**

**35.** Kotak dengan $a = b = L$ dan $c = 2L$. Urutkan lima tingkat terendah beserta degenerasinya.

**36.** Tingkat $n_x^2 + n_y^2 + n_z^2 = 38$ mempunyai degenerasi 9. Tuliskan semua keadaannya dan tunjukkan bagian mana yang "kebetulan".

**37.** [P] Hitung energi Fermi tembaga ($n = 8{,}47 \times 10^{28}$ m⁻³) dan aluminium ($n = 18{,}1 \times 10^{28}$ m⁻³, tiga elektron tiap atom).

**38.** Berapa kira-kira banyaknya keadaan translasi N₂ di bawah $kT$ (298 K) dalam kubus 10 cm? Bandingkan dengan banyaknya molekul pada 1 bar.

**Tantangan ★**

**39.** ★ Untuk kubus besar, tunjukkan bahwa banyaknya keadaan dengan energi di bawah $E$ adalah $N(E) = \tfrac\pi6\left(8mL^2E/h^2\right)^{3/2}$, lalu turunkan rumus energi Fermi untuk $N$ elektron (dua tiap keadaan).

## Subbab 4.6: Nilai harap

**Dasar**

**40.** Hitung $\langle x\rangle$ dan $\langle x^2\rangle$ untuk $\psi = \pi^{-1/4}e^{-x^2/2}$.

**41.** Untuk elektron hidrogen pada keadaan $n = 2$ (energi $-3{,}40$ eV), berapa $\langle V\rangle$ dan $\langle T\rangle$ menurut teorema virial?

**42.** Keadaan $\tfrac{1}{\sqrt3}\psi_1 + \sqrt{\tfrac23}\psi_2$ dalam kotak: hitung $\langle E\rangle$ dalam $E_1$.

**Menengah**

**43.** Untuk $\psi = Ne^{-x^2/4\sigma^2}e^{ik_0x}$, hitung $\langle p_x^2\rangle$.

**44.** [P] Fungsi uji $\psi = e^{-ar^2}$ (dinormalisasi) untuk atom hidrogen memberi (satuan atom) $\langle T\rangle = 3a/2$ dan $\langle V\rangle = -2\sqrt{2a/\pi}$. Cari $a$ yang meminimumkan $\langle E\rangle$ dan energinya.

**45.** [P] Dengan teorema Ehrenfest, tunjukkan bahwa untuk partikel dalam medan seragam $V = -Fx$, $\langle x\rangle$ bergerak tepat seperti partikel klasik dengan percepatan $F/m$.

**46.** Tunjukkan bahwa $\langle p_x\rangle = 0$ untuk setiap keadaan stasioner terikat dalam satu dimensi.

**Tantangan ★**

**47.** ★ Turunkan (4.12) dari persamaan Schrödinger bergantung waktu dan sifat Hermitian $\hat H$.

## Subbab 4.7: Syarat fungsi gelombang yang dapat diterima

**Dasar**

**48.** Manakah yang dapat diterima pada seluruh garis: $e^{-x^4}$, $x e^{-|x|}$, $1/(1 + x^2)$, $\tan x$?

**49.** Untuk partikel pada cincin, manakah yang dapat diterima: $\sin 2\phi$, $e^{i\phi/3}$, $\cos^2\phi$?

**Menengah**

**50.** Apakah $1/\sqrt{1 + x^2}$ dapat dinormalisasi pada seluruh garis? $1/(1 + x^2)$?

**51.** Di mana turunan fungsi gelombang partikel dalam kotak tidak malar, dan mengapa itu diperbolehkan?

**52.** Mengapa $\psi = e^{i\phi/2}$ tidak dapat diterima untuk partikel pada cincin, sedangkan $e^{i\phi}$ dapat?

**Tantangan ★**

**53.** ★ Fungsi $r^\ell e^{-r}$ dalam tiga dimensi: untuk $\ell$ berapa saja ia dapat dinormalisasi? Bagaimana dengan $r^{-1/2}e^{-r}$?

## Subbab 4.8: Operator Hermitian

**Dasar**

**54.** Tunjukkan bahwa operator perkalian dengan fungsi riil $V(x)$ Hermitian.

**55.** Apakah $i\,d/dx$ Hermitian? Apakah $x\,d/dx$?

**Menengah**

**56.** [P] Tunjukkan bahwa jika $\hat A$ Hermitian, $\langle A^2\rangle \ge 0$ untuk setiap keadaan. Apa akibatnya bagi energi kinetik?

**57.** Tunjukkan bahwa $\tfrac12(\hat x\hat p_x + \hat p_x\hat x)$ Hermitian dan $\hat x\hat p_x$ tidak.

**58.** Tunjukkan bahwa komutator dua operator Hermitian adalah $i$ kali operator Hermitian.

**59.** Fungsi $\psi_1$ dan $\psi_2$ adalah fungsi eigen operator Hermitian dengan nilai eigen 2 dan 5. Berapa $\int\psi_1^*\psi_2\,d\tau$?

**Tantangan ★**

**60.** ★ Tunjukkan bahwa $\hat L_z = -i\hbar\,\partial/\partial\phi$ Hermitian untuk fungsi yang bernilai tunggal pada $[0, 2\pi)$. Di mana syarat bernilai tunggal dipakai?

## Subbab 4.9: Ekspansi dalam fungsi eigen; kelengkapan

**Dasar**

**61.** Keadaan $\psi = 0{,}6\phi_1 + 0{,}8i\phi_2$. Berapa peluang hasil $a_1$ dan $a_2$?

**62.** Jika $|c_1|^2 = 0{,}5$, $|c_2|^2 = 0{,}3$, berapa $\sum_{n\ge3}|c_n|^2$?

**63.** Uraikan $\cos^2x$ atas fungsi eigen $d^2/dx^2$ yang periodik ($1$, $\cos 2x$, ...).

**Menengah**

**64.** Untuk fungsi segitiga Contoh 4.32, berapa peluang pengukuran energi memberi nilai di atas $E_1$?

**65.** Hitung $\langle E\rangle$ untuk fungsi parabola dan segitiga dalam satuan $E_1$, dan jelaskan perbedaannya.

**66.** Uraikan $\sin^3x$ atas $\sin nx$.

**67.** Untuk keadaan parabola Contoh 4.35, berapa peluang mendapat $E_5$?

**Tantangan ★**

**68.** ★ Turunkan koefisien $c_n = \dfrac{4\sqrt6}{n^2\pi^2}\sin\dfrac{n\pi}2$ untuk fungsi segitiga.

## Subbab 4.10: Komutator dan pengukuran serentak

**Dasar**

**69.** Apakah $\hat x$ dan $\hat p_y$ komut? $\hat p_x$ dan $\hat p_y$? $\hat x$ dan $\hat y$?

**70.** Untuk partikel pada cincin, apakah $\hat H$ dan $\hat L_z$ komut? Apakah $\cos\phi$ fungsi eigen bersama keduanya?

**Menengah**

**71.** [P] Untuk keadaan dasar osilator, $\psi = \pi^{-1/4}e^{-x^2/2}$ (satuan $\hbar = m = \omega = 1$), hitung $\Delta x$ dan $\Delta p$ dan periksa relasi ketidakpastian.

**72.** Hitung $[\hat H, \hat p_x]$ untuk osilator $V = \tfrac12\kappa x^2$ dan simpulkan persamaan gerak $\langle p_x\rangle$.

**73.** Dari $[\hat L_x, \hat L_y] = i\hbar\hat L_z$, hitung batas bawah $\Delta L_x\Delta L_y$ untuk orbital $d$ dengan $m_\ell = 2$.

**74.** Mengapa energi dan waktu tidak memenuhi relasi Robertson?

**Tantangan ★**

**75.** ★ Tunjukkan bahwa jika $[\hat A, \hat H] = 0$, distribusi peluang hasil pengukuran $A$ (bukan hanya nilai harapnya) tidak berubah terhadap waktu.

## Subbab 4.11: Paritas

**Dasar**

**76.** Apa paritas orbital 2s, 3p, 4d, 5f?

**77.** Manakah integral yang nol: $\langle 2s|x|3s\rangle$, $\langle 2p_x|x|3d_{x^2-y^2}\rangle$, $\langle 1s|xy|3d_{xy}\rangle$?

**78.** Apakah transisi $\sigma_g \to \pi_u$ dalam N₂ diizinkan Laporte? $\pi_u \to \pi_g$? $\sigma_g \to \sigma_g$?

**Menengah**

**79.** [P] Jelaskan mengapa larutan $[\text{Co}(\text{H}_2\text{O})_6]^{2+}$ merah muda pucat sedangkan $[\text{CoCl}_4]^{2-}$ biru tua, dan mengapa menambahkan HCl pekat pada larutan pertama mengubah warnanya.

**80.** Tunjukkan bahwa $[\hat\Pi, \hat H] = 0$ untuk osilator harmonik dan untuk atom hidrogen.

**81.** Mengapa paritas tidak dapat dipakai sebagai label untuk molekul HCl?

**Tantangan ★**

**82.** ★ Tunjukkan bahwa dalam koordinat bola, inversi adalah $\theta \to \pi - \theta$, $\phi \to \phi + \pi$, dan bahwa $\sin\theta e^{i\phi}$ berubah tanda.

## Subbab 4.12: Pengukuran dan superposisi

**Dasar**

**83.** Keadaan $0{,}8\psi_1 + 0{,}6\psi_3$ diukur energinya. Hasil yang mungkin dan peluangnya? Keadaannya setelah hasil $E_3$?

**84.** Elektron pada orbital $2p_y$. Hasil pengukuran $L_z$ dan peluangnya?

**Menengah**

**85.** [P] Sistem dua keadaan pada $(1, 0)$ diukur dengan $\hat B = \sigma_x$, lalu dengan $\sigma_z$, lalu lagi dengan $\sigma_x$. Berapa peluang ketiga hasil semuanya $+1$?

**86.** Mengapa superposisi $(\phi_1 + \phi_2)/\sqrt2$ tidak sama dengan campuran 50:50? Beri pengukuran yang membedakannya.

**87.** Elektron dalam kotak pada keadaan $\psi_2$. Posisinya diukur dan ditemukan sangat dekat $L/4$. Jika energi kemudian diukur, apakah hasilnya pasti $E_2$?

**88.** Untuk $\Psi = (\psi_1 + i\psi_3)/\sqrt2$ dalam kotak, berapa $\langle E\rangle$ dalam satuan $E_1$? Apakah faktor $i$ mengubah hasilnya?

**Tantangan ★**

**89.** ★ Efek Zeno kuantum: sistem dua keadaan berevolusi dari $|\text{A}\rangle$ dengan peluang $\sin^2(\Omega t)$ ke $|\text{B}\rangle$. Jika diukur $N$ kali pada selang $T/N$, tunjukkan bahwa peluang tetap di $|\text{A}\rangle$ menuju 1 untuk $N \to \infty$.

## Subbab 4.13: Postulat mekanika kuantum

**Dasar**

**90.** Sebutkan postulat yang menjamin bahwa hasil pengukuran besaran fisis selalu riil.

**91.** Tuliskan $e^{-i\hat Ht/\hbar}\psi_n$ untuk fungsi eigen $\psi_n$.

**Menengah**

**92.** Tunjukkan bahwa $\hat U = e^{-i\hat Ht/\hbar}$ uniter bila $\hat H$ Hermitian.

**93.** Dalam model dua keadaan NH₃, berapa waktu yang diperlukan molekul untuk berpindah sepenuhnya dari bentuk A ke B?

**94.** Keadaan $\tfrac{1}{\sqrt2}(\psi_1 + i\psi_2)$ dalam kotak: kapan pertama kali $\langle x\rangle$ mencapai nilai terkecilnya?

**95.** Berapa periode denyut superposisi $\psi_1$ dan $\psi_2$ untuk elektron dalam kotak 0,50 nm?

**Tantangan ★**

**96.** ★ Tunjukkan bahwa postulat-postulat menjamin $\sum_n(\text{peluang}) = 1$ pada setiap waktu, dengan memakai kesatuan $\hat U$ dan kelengkapan.

## Subbab 4.14: Notasi Dirac dan representasi matriks

**Dasar**

**97.** Tuliskan dalam notasi Dirac: normalisasi, ortogonalitas, nilai harap $\hat H$, dan peluang di keadaan $|n\rangle$.

**98.** Tuliskan matriks $\hat H$ partikel dalam kotak dalam basis fungsi eigennya (tiga fungsi pertama).

**Menengah**

**99.** [P] (Python) Diagonalkan matriks $\hat x$ partikel dalam kotak dalam basis empat fungsi pertama. Bandingkan dengan basis tiga fungsi (Contoh 4.51).

**100.** Polarisabilitas elektron dalam kotak sebanding dengan $L^4$. Dari nilai 83 Å³ untuk $L = 1$ nm, hitung untuk $L = 0{,}5$ nm dan 2 nm.

**101.** Tunjukkan bahwa unsur matriks operator Hermitian memenuhi $A_{mn} = A_{nm}^*$.

**Tantangan ★**

**102.** ★ Dengan model partikel pada cincin, elektron π benzena (cincin $R = 0{,}139$ nm, 6 elektron) mempunyai energi $m^2\hbar^2/2m_eR^2$. Hitung energi transisi HOMO ($|m| = 1$) → LUMO ($|m| = 2$) dan panjang gelombangnya.


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | (a) $6x + 2x^4$; (b) $2xe^{2x}$; (c) $x^2 - x$ | 52 | tidak bernilai tunggal: berubah tanda setelah satu putaran |
| 2 | tidak; ya | 53 | $\ell > -3/2$; ya ($\int re^{-2r}dr$ berhingga) |
| 3 | $-2\,d/dx$ | 54 | $\int f^*Vg = \int g(Vf)^*$ |
| 4 | $i\hbar n\hat x^{n-1}$; $i\hbar n\hat p_x^{n-1}$ | 55 | ya; tidak |
| 5 | $f'' - x^2f - f$; $f'' - x^2f + f$; $[\ ,\ ] = -2$ | 56 | $\langle A^2\rangle = \int|\hat A\psi|^2 \ge 0$; $\langle T\rangle \ge 0$ |
| 6 | uraikan kedua ruas | 57 | $(\hat x\hat p)^\dagger = \hat p\hat x$ |
| 7 | $-\tfrac{\hbar^2}{2m}(2 + 4x\,d/dx)$ | 58 | $[\hat A, \hat B]^\dagger = -[\hat A, \hat B]$ |
| 8 | $e^{ia\hat p_x/\hbar}$ menggeser fungsi sejauh $a$ | 59 | 0 |
| 9 | 9; −4; bukan; 1 | 60 | suku batas $[f^*g]_0^{2\pi} = 0$ |
| 10 | 1 | 61 | 0,36; 0,64 |
| 11 | ya; 3 | 62 | 0,2 |
| 12 | $-k^2$; $e^{ikx} = \cos kx + i\sin kx$, nilai eigen $d/dx$ adalah $ik$ | 63 | $\tfrac12 + \tfrac12\cos 2x$ |
| 13 | $e^{2\pi inx/L}$; $2\pi in/L$ | 64 | 0,0145 |
| 14 | $n$ | 65 | 1,013; 1,216; segitiga bersudut tajam |
| 15 | Ya; $\hbar^2k^2$ | 66 | $\tfrac34\sin x - \tfrac14\sin 3x$ |
| 16 | kerjakan berulang; deret Taylor | 67 | $6{,}4 \times 10^{-5}$ |
| 17 | $-\hbar^2\nabla^2$; $-\tfrac{\hbar^2}{2m}\nabla^2$ | 68 | integral parsial pada dua separuh |
| 18 | $-i\hbar(y\,\partial_z - z\,\partial_y)$ | 69 | ya; ya; ya |
| 19 | ya, $3\hbar$; ya, $\hbar$ | 70 | ya; tidak (hanya $\hat H$) |
| 20 | bernilai tunggal; $e^{i\pi} = -1$ | 71 | $1/\sqrt2$; $1/\sqrt2$; hasil kali $1/2$: batas tepat tercapai |
| 21 | $-i\hbar(x\cdot i - y\cdot 1) = \hbar(x + iy)$ | 72 | $i\hbar\kappa x$; $d\langle p\rangle/dt = -\kappa\langle x\rangle$ |
| 22 | $e(8\mathbf R_\text{O} + \mathbf R_{\text{H}_1} + \mathbf R_{\text{H}_2}) - e\sum\mathbf r_i$; muatan total nol | 73 | $\hbar^2$ |
| 23 | $\partial_\phi = -y\partial_x + x\partial_y$ | 74 | waktu bukan operator, melainkan parameter |
| 24 | tiga suku kinetik, dua tarikan, satu tolakan inti–inti | 75 | fungsi eigen bersama; $|c_n(t)|^2$ tetap |
| 25 | 3 kinetik, 3 tarikan $-3ke^2/r_i$, 3 tolakan; 9 koordinat | 76 | g; u; g; u |
| 26 | 45 | 77 | pertama nol; dua lainnya tidak nol secara paritas |
| 27 | $3E_1$; $6E_1$, degenerasi 3 | 78 | ya; ya; tidak |
| 28 | $-367{,}4$ eV; $-275{,}5$ eV | 79 | oktahedral: d–d terlarang Laporte; tetrahedral: tidak ada pusat inversi; Cl⁻ membentuk kompleks tetrahedral |
| 29 | $\hat H_x$ tidak menyentuh $y$ | 80 | $V(-x) = V(x)$; $V(r)$ tidak berubah oleh inversi |
| 30 | 91 | 81 | tidak ada pusat inversi |
| 31 | $\hat H = -\tfrac{\hbar^2}{2M}\nabla_R^2 - \tfrac{\hbar^2}{2\mu}\nabla_r^2 + V(r)$ | 82 | $\sin(\pi - \theta) = \sin\theta$, $e^{i\pi} = -1$ |
| 32 | 4,51 eV; 18,0 eV | 83 | $E_1$ (0,64), $E_3$ (0,36); $\psi_3$ |
| 33 | 3; 6; 6; 4 | 84 | $\pm\hbar$, masing-masing ½ |
| 34 | $(2/L)^{3/2}\sin\tfrac{\pi x}{L}\sin\tfrac{2\pi y}{L}\sin\tfrac{3\pi z}{L}$ | 85 | $\tfrac12 \times \tfrac12 \times \tfrac12 = \tfrac18$ |
| 35 | $2{,}25$ (1); $3{,}00$ (1); $4{,}25$ (1); $5{,}25$ (2); $6{,}00$ (1) dalam $h^2/8mL^2$ | 86 | suku interferensi; ukur besaran yang tidak komut, misalnya posisi |
| 36 | (1,1,6)×3 dan (2,3,5)×6; gabungan keduanya kebetulan | 87 | tidak; keadaan setelah pengukuran posisi tersebar atas banyak $\psi_n$ |
| 37 | 7,03 eV; 11,7 eV | 88 | 5; tidak |
| 38 | $\approx 10^{29}$; $2{,}5 \times 10^{22}$ molekul: keadaan jauh lebih banyak | 89 | $[\cos^2(\Omega T/N)]^N \to 1$ |
| 39 | volume seperdelapan bola; $E_F = \tfrac{\hbar^2}{2m}(3\pi^2N/L^3)^{2/3}$ | 90 | Postulat 2 (operator Hermitian) |
| 40 | 0; 1/2 | 91 | $e^{-iE_nt/\hbar}\psi_n$ |
| 41 | $-6{,}80$ eV; $+3{,}40$ eV | 92 | $\hat U^\dagger = e^{i\hat Ht/\hbar} = \hat U^{-1}$ |
| 42 | 3 | 93 | $h/2\Delta = 21$ ps |
| 43 | $\hbar^2k_0^2 + \hbar^2/4\sigma^2$ | 94 | $t = T/4 = h/4(E_2 - E_1)$ |
| 44 | $a = 8/9\pi = 0{,}283$; $E = -4/3\pi = -0{,}424\ E_h = -11{,}5$ eV | 95 | 0,92 fs |
| 45 | $d^2\langle x\rangle/dt^2 = F/m$ | 96 | $\sum|c_n(t)|^2 = \langle\Psi(t)|\Psi(t)\rangle = 1$ |
| 46 | $\psi$ dapat dipilih riil | 97 | $\langle\psi|\psi\rangle = 1$; $\langle m|n\rangle = 0$; $\langle\psi|\hat H|\psi\rangle$; $|\langle n|\psi\rangle|^2$ |
| 47 | $\tfrac{d}{dt}\langle\Psi|\hat A|\Psi\rangle = \tfrac{i}{\hbar}\langle[\hat H, \hat A]\rangle$ | 98 | $\text{diag}(1, 4, 9)E_1$ |
| 48 | ya; ya; ya; tidak | 99 | 0,185; 0,395; 0,605; 0,815 ($L$) |
| 49 | ya; tidak; ya | 100 | 5,2 Å³; 1330 Å³ |
| 50 | tidak; ya | 101 | dari (4.14) |
| 51 | di dinding; potensial tak hingga di sana | 102 | 5,92 eV; 210 nm |
:::


# Pembahasan soal terpilih

**Soal 4.** Dengan induksi dan (4.2): $[\hat x^n, \hat p_x] = \hat x^{n-1}[\hat x, \hat p_x] + [\hat x^{n-1}, \hat p_x]\hat x = i\hbar\hat x^{n-1} + [\hat x^{n-1}, \hat p_x]\hat x$. Jika $[\hat x^{n-1}, \hat p_x] = i\hbar(n - 1)\hat x^{n-2}$, maka hasilnya $i\hbar\hat x^{n-1} + i\hbar(n - 1)\hat x^{n-1} = i\hbar n\hat x^{n-1}$. Langsung juga: $(-i\hbar)[x^n(f') - (x^nf)'] = i\hbar nx^{n-1}f$. Dengan cara yang sama $[\hat x, \hat p_x^n] = i\hbar n\hat p_x^{n-1}$.

*Cara berpikir:* komutator dengan $\hat p_x$ bekerja seperti $i\hbar\,d/d\hat x$, dan komutator dengan $\hat x$ seperti $i\hbar\,d/d\hat p_x$. Untuk fungsi yang dapat diuraikan menjadi deret pangkat, $[f(\hat x), \hat p_x] = i\hbar f'(\hat x)$. Inilah jembatan antara komutator kuantum dan kurung Poisson mekanika klasik.

**Soal 12.** $\tfrac{d^2}{dx^2}\cos kx = -k^2\cos kx$ dan $\tfrac{d^2}{dx^2}\sin kx = -k^2\sin kx$: nilai eigen sama, $-k^2$. Kombinasi $\cos kx + i\sin kx = e^{ikx}$ memenuhi $\tfrac{d}{dx}e^{ikx} = ik\,e^{ikx}$, sedangkan $\cos kx$ sendiri tidak.

*Cara berpikir:* $d/dx$ dan $d^2/dx^2$ komut, sehingga dalam ruang terdegenerasi $\{\cos kx, \sin kx\}$ kita dapat memilih basis yang sekaligus fungsi eigen keduanya: $e^{\pm ikx}$. Untuk partikel bebas ini berarti memilih keadaan dengan momentum tertentu dalam tingkat energi yang terdegenerasi.

**Soal 29.** $\hat H\psi = \hat H_x[X(x)Y(y)] + \hat H_y[X(x)Y(y)]$. Karena $\hat H_x$ hanya memuat $x$ dan turunan terhadap $x$, $Y(y)$ berperilaku seperti tetapan: $\hat H_x[XY] = Y\hat H_xX = E_xXY$. Begitu pula $\hat H_y[XY] = X\hat H_yY = E_yXY$. Jumlahnya $(E_x + E_y)XY$.

*Cara berpikir:* inilah alasan formal di balik pendekatan orbital: jika tolakan elektron diganti dengan medan rata-rata, Hamiltonian menjadi jumlah suku satu-elektron, fungsi gelombang menjadi hasil kali orbital, dan energi menjadi jumlah energi orbital (dengan koreksi untuk tolakan yang dihitung ganda, Bab 9).

**Soal 37.** Tembaga: $(3\pi^2n)^{1/3} = (3\pi^2 \times 8{,}47 \times 10^{28})^{1/3} = 1{,}36 \times 10^{10}$ m⁻¹; $E_F = \hbar^2k_F^2/2m_e = 1{,}127 \times 10^{-18}$ J $= 7{,}03$ eV. Aluminium: $k_F = 1{,}75 \times 10^{10}$ m⁻¹, $E_F = 11{,}7$ eV.

*Cara berpikir:* $E_F \propto n^{2/3}$. Aluminium, dengan tiga elektron valensi tiap atom dan atom yang lebih rapat, mempunyai energi Fermi jauh lebih tinggi. Nilai-nilai ini cocok dengan lebar pita yang diukur dengan spektroskopi fotoelektron sinar-X, sebuah kemenangan model kotak tiga dimensi yang paling sederhana.

**Soal 44.** $\langle E\rangle(a) = \tfrac32a - 2\sqrt{2/\pi}\,a^{1/2}$. Turunkan: $\tfrac32 - \sqrt{2/\pi}\,a^{-1/2} = 0$, sehingga $a^{1/2} = \tfrac23\sqrt{2/\pi}$, $a = \tfrac{8}{9\pi} = 0{,}283$. Masukkan: $\langle E\rangle = \tfrac32\cdot\tfrac{8}{9\pi} - 2\sqrt{\tfrac2\pi}\cdot\tfrac23\sqrt{\tfrac2\pi} = \tfrac{4}{3\pi} - \tfrac{8}{3\pi} = -\tfrac{4}{3\pi} = -0{,}424\ E_h = -11{,}5$ eV.

*Cara berpikir:* fungsi Gauss tidak dapat meniru taring $e^{-r}$ di inti, sehingga energinya 15% di atas nilai tepat $-0{,}5\ E_h$, tetapi tidak pernah di bawahnya (teorema variasi, Bab 8). Di titik optimum $\langle V\rangle = -2\langle T\rangle$: teorema virial berlaku untuk fungsi uji yang dioptimalkan terhadap skala. Pengamatan ini adalah asal usul pemakaian kombinasi beberapa fungsi Gauss untuk meniru satu orbital Slater (basis STO-3G, Bab 17).

**Soal 45.** $V = -Fx$, sehingga $-\langle dV/dx\rangle = F$. Dengan (4.13): $d\langle p\rangle/dt = F$ dan $d\langle x\rangle/dt = \langle p\rangle/m$, jadi $d^2\langle x\rangle/dt^2 = F/m$.

*Cara berpikir:* untuk gaya yang tetap atau linear terhadap $x$, $\langle F(x)\rangle = F(\langle x\rangle)$ tepat, sehingga pusat paket mengikuti lintasan klasik tanpa penyimpangan, sementara lebar paketnya tetap menyebar secara kuantum. Elektron yang dipercepat dalam tabung sinar katode atau ion dalam spektrometer massa waktu terbang mengikuti mekanika Newton karena alasan ini.

**Soal 56.** $\langle A^2\rangle = \int\psi^*\hat A(\hat A\psi)\,d\tau$. Dengan kehermitan, pindahkan satu $\hat A$ ke kiri: $= \int(\hat A\psi)^*(\hat A\psi)\,d\tau = \int|\hat A\psi|^2d\tau \ge 0$. Untuk energi kinetik, $\hat T = \hat p^2/2m$ dengan $\hat p$ Hermitian, sehingga $\langle T\rangle \ge 0$, dan sama dengan nol hanya jika $\hat p\psi = 0$, yaitu $\psi$ tetap di seluruh ruang, yang tidak dapat dinormalisasi.

*Cara berpikir:* energi kinetik setiap keadaan terikat positif. Itulah sebabnya energi keadaan dasar selalu di atas dasar potensial (energi titik nol), dan sebabnya dalam teorema virial $\langle T\rangle = -E > 0$ untuk keadaan terikat.

**Soal 71.** $|\psi|^2 = \pi^{-1/2}e^{-x^2}$ adalah sebaran Gauss dengan $\sigma^2 = 1/2$, jadi $\Delta x = 1/\sqrt2$. $\langle p^2\rangle = \int|\psi'|^2dx = \pi^{-1/2}\int x^2e^{-x^2}dx = \tfrac12$, dan $\langle p\rangle = 0$, jadi $\Delta p = 1/\sqrt2$. Hasil kalinya $\tfrac12 = \hbar/2$.

*Cara berpikir:* keadaan dasar osilator mencapai batas Heisenberg dengan tanda sama dengan; ia adalah "keadaan paling klasik" yang mungkin. Keadaan koheren laser dan paket getaran dalam femtokimia mewarisi sifat ini.

**Soal 79.** $[\text{Co}(\text{H}_2\text{O})_6]^{2+}$ oktahedral, mempunyai pusat inversi; transisi d–d g → g terlarang Laporte, sehingga serapannya lemah ($\varepsilon$ sekitar 5) dan warnanya pucat. Dalam HCl pekat terbentuk $[\text{CoCl}_4]^{2-}$ tetrahedral tanpa pusat inversi; orbital d bercampur dengan p sehingga transisi menjadi jauh lebih kuat ($\varepsilon$ sekitar 600), dan larutan menjadi biru tua.

*Cara berpikir:* perubahan warna merah muda → biru ini dipakai pada silika gel indikator kelembapan dan pada demonstrasi kesetimbangan Le Chatelier. Intensitasnya, bukan hanya warnanya, memberi tahu geometri.

**Soal 85.** Dari $(1, 0)$, pengukuran $\sigma_x$ memberi $+1$ dengan peluang ½ dan meninggalkan $(1, 1)/\sqrt2$. Pengukuran $\sigma_z$ pada keadaan ini memberi $+1$ dengan peluang ½ dan meninggalkan $(1, 0)$. Pengukuran $\sigma_x$ lagi memberi $+1$ dengan peluang ½. Peluang total $1/8$.

*Cara berpikir:* setiap pengukuran operator yang tidak komut dengan sebelumnya "mengocok ulang" peluang. Jika pengukuran $\sigma_z$ di tengah dihilangkan, dua pengukuran $\sigma_x$ berurutan pasti memberi hasil sama, dan peluangnya ½. Menyisipkan pengukuran mengubah statistik: inti percobaan Stern–Gerlach berurutan (Bab 9).

**Soal 99.** Unsur $\langle m|x|n\rangle$ dari rumus Contoh 3.21 dengan diagonal $1/2$; matriks 4 × 4 yang dihasilkan didiagonalkan dengan `numpy.linalg.eigvalsh`: 0,185; 0,395; 0,605; 0,815 (dalam $L$). Basis tiga fungsi memberi 0,235; 0,500; 0,765.

*Cara berpikir:* nilai eigen makin rapat dan makin mendekati tepi kotak ketika basis membesar, menuju spektrum malar $[0, L]$ operator posisi yang sesungguhnya. Pola nilai eigen yang simetris terhadap $L/2$ berasal dari paritas.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 3 dan 7. Operator, nilai harap, kotak tiga dimensi, operator Hermitian, dan postulat dengan sangat sistematis.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 4. Postulat mekanika kuantum dengan banyak contoh.
3. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 1. Pendekatan berbasis notasi Dirac dan representasi matriks.
4. J. J. Sakurai dan J. Napolitano, *Modern Quantum Mechanics*, edisi ke-3 (Cambridge University Press, 2020), Bab 1. Dasar formal: ket, bra, operator, pengukuran, dengan percobaan Stern–Gerlach sebagai titik tolak.
5. C. Cohen-Tannoudji, B. Diu, dan F. Laloë, *Quantum Mechanics*, Jilid 1 (Wiley, 1977), Bab II–III. Uraian lengkap tentang ruang keadaan dan postulat, dengan banyak pelengkap.
