# Ringkasan Bab 7

| Gagasan | Rumus (satuan atom) | Subbab |
|---|---|---|
| Hamiltonian | $\hat H = -\tfrac12\nabla^2 - Z/r$; $\ a_0 = 52{,}918$ pm, $E_h = 27{,}211$ eV | 7.1 |
| Pemisahan | $\psi_{n\ell m} = R_{n\ell}(r)Y_\ell^m(\theta, \phi)$ | 7.2 |
| Persamaan radial | $-\tfrac12u'' + \left[-\tfrac Zr + \tfrac{\ell(\ell+1)}{2r^2}\right]u = Eu$, $\ u = rR$ | 7.2 |
| Bentuk penyelesaian | $u = r^{\ell+1}e^{-Zr/n}f(r)$; $\ f$ polinom berderajat $n - \ell - 1$ | 7.3 |
| Energi | $E_n = -\tfrac{\mu}{m_e}\tfrac{Z^2}{2n^2}$; $\ \ell = 0, \ldots, n - 1$; degenerasi $n^2$ | 7.3, 7.4 |
| Simpul | radial $n - \ell - 1$; sudut $\ell$; total $n - 1$ | 7.5 |
| Rapat di inti | $|\psi_{ns}(0)|^2 = Z^3/\pi n^3$; nol untuk $\ell > 0$ | 7.5 |
| Distribusi radial | $P(r) = r^2R_{n\ell}^2$; $\ r_\text{mp} = n^2/Z$ untuk $\ell = n - 1$ | 7.6 |
| Orbital riil | $p_x = (p_{-1} - p_{+1})/\sqrt2$, $\ p_y = i(p_{-1} + p_{+1})/\sqrt2$ | 7.7 |
| Nilai harap | $\langle r\rangle = [3n^2 - \ell(\ell+1)]/2Z$; $\ \langle 1/r\rangle = Z/n^2$ | 7.9 |
| Teorema virial | $\langle V\rangle = 2E$; $\ \langle T\rangle = -E$ | 7.9 |
| Mirip hidrogen; Moseley | $E \propto Z^2$, ukuran $\propto 1/Z$; $\ E_{K\alpha} \approx \tfrac34(Z - 1)^2(13{,}6\ \text{eV})$ | 7.10 |
| Aturan seleksi | $\Delta\ell = \pm1$, $\ \Delta m = 0, \pm1$, $\ \Delta n$ sembarang | 7.11 |
| Laju peluruhan | $A = \omega^3|\mathbf d|^2/3\pi\varepsilon_0\hbar c^3$; $\ \tau(2p) = 1{,}60$ ns | 7.11 |
| Zeeman normal | $E_Z = m_\ell\mu_BB$; triplet berjarak $\mu_BB$ | 7.12 |
| Numerov radial | $g = 2(V - E) + \ell(\ell+1)/r^2$; mulai dari $u = r^{\ell+1}$ | 7.13 |

**Jawaban kuis cepat.** **7.1** $-Z/r = -1$ hartree; karena hanya bergantung pada jarak dari inti, sehingga gayanya selalu menuju pusat. **7.2** Karena $\hat L^2$ yang muncul di persamaan radial hanya bergantung pada $\ell$; 16. **7.3** Derajat 1 ($n - \ell - 1$); hanya $\ell = 0$, karena $\ell \le n - 1$. **7.4** 16; 1,51 eV. **7.5** Dua simpul radial dan dua sudut; nol di inti berasal dari faktor $r^\ell$ yang ada pada setiap orbital dengan $\ell > 0$, bukan dari akar polinom radial. **7.6** 9 bohr; 4s, karena mempunyai lobus-lobus dalam di dekat inti. **7.7** Bukan; ya, dengan nilai eigen nol (Contoh 6.23); karena keduanya kombinasi linear fungsi-fungsi yang berdegenerasi. **7.8** Empat; dua kerucut, pada 54,7° dan 125,3°. **7.9** $\langle T\rangle = 1{,}51$ eV, $\langle V\rangle = -3{,}02$ eV; karena $\langle V\rangle = -Z\langle 1/r\rangle = 2E_n$ hanya bergantung pada $n$. **7.10** $a_0/3 = 17{,}6$ pm; $-13{,}6$ eV. **7.11** Dari keadaan 3p, yang dapat meluruh ke 1s dengan $\Delta\ell = -1$. **7.12** Tidak; ia campuran $m = +1$ dan $m = -1$ yang kini berenergi berbeda; karena $\ell = 0$ hanya mempunyai $m = 0$. **7.13** Karena $u \propto r^{\ell+1}$ adalah perilaku penyelesaian yang dapat diterima di dekat inti, sedangkan $u = 1$ membuat $R = 1/r$ tak hingga; karena elektron 3d hampir tidak menembus teras 1s², sehingga merasakan muatan efektif $+1$ seperti di hidrogen.

# Pertanyaan

1. Mengapa massa tereduksi, bukan massa elektron, yang muncul dalam energi atom hidrogen? Seberapa besar perbedaannya?
2. Apa keuntungan satuan atom? Apa yang harus diingat ketika membandingkan hasil dengan percobaan?
3. Mengapa elektron tidak jatuh ke inti menurut mekanika kuantum?
4. Bagaimana syarat kenormalan menghasilkan bilangan kuantum $n$? Bandingkan dengan osilator harmonik.
5. Mengapa $\ell$ dibatasi oleh $n - 1$?
6. Mengapa energi atom hidrogen tidak bergantung pada $\ell$, padahal persamaan radialnya bergantung? Apa yang merusak degenerasi ini dalam atom lain?
7. Apa beda simpul radial dan simpul sudut? Mengapa jumlah totalnya $n - 1$?
8. Mengapa hanya orbital s yang mempunyai rapat elektron tidak nol di inti? Sebutkan dua akibatnya yang dapat diukur.
9. Mengapa fungsi distribusi radial 1s nol di inti, padahal $|\psi|^2$ terbesar di sana?
10. Apa arti penembusan, dan bagaimana ia menjelaskan urutan energi s < p < d dalam atom berelektron banyak?
11. Kapan orbital kompleks lebih berguna daripada orbital riil, dan sebaliknya?
12. Mengapa tanda fungsi gelombang penting, padahal yang terukur adalah $|\psi|^2$?
13. Mengapa ada lima orbital d dan tujuh orbital f?
14. Apa isi teorema virial untuk atom hidrogen? Apa artinya bagi energi kinetik elektron ketika ikatan kimia terbentuk?
15. Mengapa hukum Moseley memastikan bahwa tabel periodik harus diurutkan menurut nomor atom?
16. Mengapa unsur berat memerlukan kimia kuantum relativistik?
17. Jelaskan aturan seleksi $\Delta\ell = \pm1$ dengan dua cara: momentum sudut foton dan paritas.
18. Mengapa keadaan 2s hidrogen metastabil? Apa analognya dalam kimia molekul?
19. Mengapa efek Zeeman normal selalu memberi tepat tiga garis?
20. Apa yang dapat dilakukan metode numerik yang tidak dapat dilakukan penyelesaian eksak? Berikan dua contoh dari bab ini.
21. Bagaimana teka-teki pembuka bab (2s dan 2p berenergi sama pada H, tetapi tidak pada Li) terjawab?

# Soal

## Subbab 7.1: Masalah gaya sentral

Gunakan satuan atom kecuali dinyatakan lain ($a_0 = 52{,}918$ pm, $E_h = 27{,}211$ eV $= 2625{,}5$ kJ/mol). Soal dikelompokkan menurut tingkat: **dasar**, **menengah**, dan **tantangan ★**. Soal bertanda **[P]** dibahas di akhir bab.

**Dasar**

**1.** Berapa energi potensial elektron pada jarak 0,5 bohr dari proton, dalam hartree dan eV?

**2.** Nyatakan 1 hartree dalam kJ/mol dan cm⁻¹.

**3.** Nyatakan $E = -0{,}125\ E_h$ dalam eV dan kJ/mol.

**Menengah**

**4.** Hitung perbandingan tarikan gravitasi dan tarikan Coulomb antara proton dan elektron.

**5.** Satuan waktu atom adalah $\hbar/E_h = 2{,}419 \times 10^{-17}$ s. Berapa periode "orbit" 1s, $2\pi$ satuan waktu, dalam attodetik?

**6.** [P] Dengan $E(r) \approx 1/2r^2 - Z/r$, taksir jari-jari dan energi keadaan dasar ion mirip hidrogen bermuatan $Z$.

**Tantangan ★**

**7.** ★ Mengapa taksiran asas ketidakpastian di atas memberi hasil eksak untuk hidrogen? Apakah itu juga terjadi untuk osilator harmonik dengan $E(x) = 1/2x^2 + x^2/2$?

## Subbab 7.2: Pemisahan variabel

**Dasar**

**8.** Tunjukkan bahwa dengan $u = rR$, $\tfrac{1}{r^2}\tfrac{d}{dr}\left(r^2\tfrac{dR}{dr}\right) = \tfrac1r\tfrac{d^2u}{dr^2}$.

**9.** Berapa banyak orbital (tanpa spin) dengan $n = 5$?

**10.** Apakah $\psi = e^{-r} + (2 - r)e^{-r/2}$ keadaan stasioner?

**Menengah**

**11.** Periksa bahwa $\psi = (2 - r)e^{-r/2}$ memenuhi (7.3) dengan $Z = 1$ dan tentukan $E$.

**12.** Tentukan minimum potensial efektif untuk $\ell = 1$, $Z = 1$.

**13.** Tunjukkan bahwa penyelesaian $u \propto r^{-\ell}$ untuk $\ell = 1$ tidak dapat dinormalisasi di dekat inti.

**Tantangan ★**

**14.** ★ Tunjukkan bahwa minimum $V_\text{ef}$ untuk $\ell$ umum terletak di $r = \ell(\ell + 1)/Z$ dengan nilai $-Z^2/2\ell(\ell + 1)$, dan bahwa tingkat terendah $E_{\ell+1}$ selalu di atasnya.

## Subbab 7.3: Persamaan radial dan penyelesaiannya

**Dasar**

**15.** Berapa derajat polinom $f$ untuk 4d dan 5f?

**16.** Untuk $Z = 2$ dan $n = 4$, berapa $\kappa$ dan $E$?

**17.** Tuliskan $u$ (tanpa normalisasi) untuk 3d dari (7.7).

**Menengah**

**18.** [P] Dengan rekursi (7.9), bangun $f$ untuk $n = 3$, $\ell = 0$, dan tunjukkan bahwa $R_{30} \propto (27 - 18r + 2r^2)e^{-r/3}$.

**19.** Apakah ada keadaan terikat hidrogen dengan $E = -0{,}3$ hartree?

**20.** Tunjukkan bahwa untuk $k$ besar, $a_{k+1}/a_k \to 2\kappa/k$ sama dengan perbandingan koefisien deret $e^{2\kappa r}$.

**Tantangan ★**

**21.** ★ Periksa (7.8) untuk 1s ($\ell = 0$, $\kappa = 1$, $f = 1$) dan tunjukkan bahwa ia memaksa $Z = 1$.

## Subbab 7.4: Tingkat energi dan degenerasi

**Dasar**

**22.** Hitung $E_n$ hidrogen (eV, dengan massa tereduksi) untuk $n = 1$ sampai 4.

**23.** Berapa panjang gelombang batas deret Balmer dan Lyman (vakum)?

**24.** Berapa degenerasi tingkat $n = 5$ bila spin diperhitungkan?

**Menengah**

**25.** Hitung panjang gelombang Brackett-α ($5 \to 4$).

**26.** Berapa selisih energi ionisasi D dan H (meV)?

**27.** Pada $n$ berapa transisi $n \to n - 1$ hidrogen jatuh di 10 GHz?

**Tantangan ★**

**28.** ★ Hitung frekuensi transisi 1s → 2s (diukur dengan spektroskopi dua foton) menurut (7.11). Nilai terukur 2466,061 THz; dari mana selisihnya?

## Subbab 7.5: Fungsi radial dan simpul

**Dasar**

**29.** Berapa simpul radial dan sudut orbital 4d?

**30.** Di mana simpul radial 3p (bohr dan pm)?

**31.** Di mana simpul radial 2s He⁺?

**Menengah**

**32.** Hitung $|\psi_{2s}(0)|^2/|\psi_{1s}(0)|^2$ untuk hidrogen.

**33.** Hitung $|\psi_{1s}(0)|^2$ He⁺ dibandingkan H.

**34.** Periksa normalisasi $R_{10} = 2e^{-r}$.

**Tantangan ★**

**35.** ★ Fungsi radial 4s sebanding dengan $L_3^1(r/2)$. Tentukan ketiga simpul radialnya secara numerik.

## Subbab 7.6: Fungsi distribusi radial

**Dasar**

**36.** Berapa $r_\text{mp}$ untuk 3d dan 4f hidrogen?

**37.** Berapa $r_\text{mp}$ 1s He⁺?

**38.** Tunjukkan bahwa $P(r) = 4r^2e^{-2r}$ maksimum di $r = 1$.

**Menengah**

**39.** Berapa peluang elektron 1s berada di dalam $r < 2$ bohr? Di luar $r > 3$ bohr?

**40.** Berapa peluang elektron 2p berada di dalam $r_\text{mp} = 4$ bohr?

**41.** [P] Tentukan jari-jari paling mungkin (puncak terbesar) 3s hidrogen.

**Tantangan ★**

**42.** ★ Mengapa $\langle r\rangle$ lebih besar daripada $r_\text{mp}$ untuk 1s? Apakah hal ini berlaku untuk setiap orbital?

## Subbab 7.7: Orbital kompleks dan orbital riil

**Dasar**

**43.** Tuliskan $\psi_{2\text{p}_y}$ dalam koordinat Kartesius.

**44.** Berapa $\langle L_z^2\rangle$ untuk elektron di $d_{xy}$?

**45.** Apakah $d_{z^2}$ fungsi eigen $\hat L_z$?

**Menengah**

**46.** Nyatakan $p_{+1}$ dengan $p_x$ dan $p_y$.

**47.** Elektron dalam keadaan $(2\text{p}_x + 2\text{p}_z)/\sqrt2$. Berapa peluang hasil $L_z = +\hbar$, 0, dan $-\hbar$?

**48.** Tunjukkan bahwa $2\text{p}_x$ dan $2\text{p}_y$ ortogonal.

**Tantangan ★**

**49.** ★ Tunjukkan bahwa $|p_{+1}|^2 + |p_{-1}|^2 = |p_x|^2 + |p_y|^2$. Apa makna fisisnya?

## Subbab 7.8: Bentuk orbital s, p, d, f

**Dasar**

**50.** Di mana bidang simpul $d_{x^2-y^2}$?

**51.** Berapa banyak bidang simpul $f_{xyz}$, dan bidang apa saja?

**52.** Berapa banyak simpul total 5f?

**Menengah**

**53.** Manakah yang tumpang tindihnya dengan orbital s pada sumbu $z$ dapat tidak nol: $p_z$, $d_{z^2}$, $d_{xy}$, $f_{z^3}$?

**54.** Polinom kubik dalam $x$, $y$, $z$ ada 10. Mengapa hanya ada 7 orbital f?

**55.** Tunjukkan bahwa $d_{xy}$ adalah $d_{x^2-y^2}$ yang diputar 45° terhadap sumbu $z$.

**Tantangan ★**

**56.** ★ Pada bidang $xz$, sepanjang garis $\theta = 54{,}7°$, berapa nilai $d_{z^2}$? Apa nilainya sepanjang garis yang sama untuk $d_{xz}$?

## Subbab 7.9: Nilai harap dan teorema virial

**Dasar**

**57.** Hitung $\langle r\rangle$ untuk 3s dan 3p.

**58.** Hitung $\langle T\rangle$ dan $\langle V\rangle$ untuk $n = 3$ (eV).

**59.** Hitung $\langle r\rangle$ 1s He⁺.

**Menengah**

**60.** Hitung $\langle 1/r\rangle$ untuk 1s langsung dari $R_{10}$.

**61.** Hitung $\langle r^2\rangle$ dan $\Delta r$ untuk 2p.

**62.** [P] Hitung $\langle 1/r^2\rangle$ untuk 1s langsung dan bandingkan dengan (7.17). Dari $\langle p^2\rangle = 2\langle T\rangle$, berapa kecepatan rms elektron 1s (m/s)?

**Tantangan ★**

**63.** ★ Tunjukkan bahwa $\langle r\rangle = n(n + \tfrac12)$ untuk orbital tanpa simpul radial ($\ell = n - 1$), sedangkan $r_\text{mp} = n^2$.

## Subbab 7.10: Atom mirip hidrogen

**Dasar**

**64.** Berapa energi tingkat $n = 1$ dan $n = 2$ He⁺ (eV)?

**65.** Berapa $r_\text{mp}$ 1s Li²⁺ (pm)?

**66.** Berapa energi ionisasi Be³⁺?

**Menengah**

**67.** Perkirakan energi Kα nikel ($Z = 28$). Nilai terukur 7,48 keV.

**68.** Garis Kα suatu unsur di 5,41 keV. Unsur apa?

**69.** Hitung panjang gelombang He⁺ $3 \to 2$.

**Tantangan ★**

**70.** ★ Tingkat $n = 2$ He⁺ berenergi sama dengan 1s H. Apa akibatnya bagi tumbukan He²⁺ dengan atom H?

## Subbab 7.11: Spektrum hidrogen dan aturan seleksi

**Dasar**

**71.** Ke keadaan mana saja elektron 4d boleh meluruh dengan satu foton?

**72.** Pada suhu kamar, deret mana yang tampak dalam spektrum serapan gas hidrogen atomik?

**73.** Mengapa transisi 3s → 1s terlarang?

**Menengah**

**74.** [P] Hitung $\int_0^\infty R_{10}R_{21}r^3dr$ dan dari situ $\langle 1s|z|2p_0\rangle$.

**75.** Keadaan 3p hidup 5,4 ns. Berapa lebar alami garis yang dipancarkannya (MHz)?

**76.** Dengan unsur matriks dipol yang sama, berapa kali lebih lambat transisi di 600 nm dibandingkan di 121,6 nm?

**Tantangan ★**

**77.** ★ Mengapa keadaan 2s praktis tidak meluruh ke 2p, meskipun $\Delta\ell = 1$ diizinkan?

## Subbab 7.12: Efek Zeeman

**Dasar**

**78.** Berapa $\mu_BB$ dalam cm⁻¹ untuk $B = 0{,}50$ T?

**79.** Berapa frekuensi Larmor orbital dalam 1,5 T?

**80.** Tingkat 4f terpecah menjadi berapa tingkat dalam medan magnet (tanpa spin)?

**Menengah**

**81.** Hitung pemecahan panjang gelombang Lyman-α (121,57 nm) dalam medan 5,0 T.

**82.** Bagaimana polarisasi garis $\Delta m = 0$ bila diamati tegak lurus medan?

**83.** Mengapa garis D natrium tidak menunjukkan triplet Zeeman normal?

**Tantangan ★**

**84.** ★ Dalam medan 10 T dan suhu 4 K, hitung perbandingan populasi tingkat $m = +1$ terhadap $m = 0$ suatu tingkat p.

## Subbab 7.13: Penyelesaian numerik persamaan radial

**Dasar**

**85.** Bagaimana program subbab 7.13 diubah untuk He⁺? Berapa $E_{1s}$ yang seharusnya keluar?

**86.** Mengapa integrasi dimulai dengan $u = r^{\ell+1}$?

**87.** Bila $h$ dibuat dua kali lebih besar (0,016), berapa kira-kira galat 1s?

**Menengah**

**88.** Hidrogen dikurung dalam bola berjari-jari 6 bohr. Berapa energi keadaan p terendah? (Petunjuk: simpul 3p.)

**89.** Apa keuntungan kisi logaritmik $r = e^x$ untuk persamaan radial?

**90.** Dalam model litium, apa yang terjadi pada energi 2s bila $\alpha$ diperbesar?

**Tantangan ★**

**91.** [P] ★ Dalam plasma, potensial proton disaring: $V = -e^{-r/\lambda}/r$ (potensial Debye–Yukawa). Hitung energi 1s untuk $\lambda = 100$, 10, 5, 2, dan 1 bohr.


# Jawaban

::: {.panjang}
| No. | Jawaban | No. | Jawaban |
|---|---|---|---|
| 1 | $-2\ E_h = -54{,}4$ eV | 47 | $\tfrac14$; $\tfrac12$; $\tfrac14$ |
| 2 | 2625,5 kJ/mol; 219 475 cm⁻¹ | 48 | integral $\cos\phi\sin\phi$ atas $[0, 2\pi]$ nol |
| 3 | $-3{,}40$ eV; $-328$ kJ/mol | 49 | transformasi uniter mempertahankan rapat total |
| 4 | $4{,}4 \times 10^{-40}$ | 50 | bidang $x = y$ dan $x = -y$ |
| 5 | 152 as | 51 | 3: $xy$, $xz$, $yz$ |
| 6 | $r = 1/Z$; $E = -Z^2/2$ | 52 | 4 (1 radial, 3 sudut) |
| 7 | kebetulan faktor numerik; osilator: $x = 1$, $E = 1$ (eksak $\tfrac12$), tidak eksak | 53 | $p_z$, $d_{z^2}$, $f_{z^3}$ |
| 8 | langsung | 54 | 3 kombinasi ($r^2x$, $r^2y$, $r^2z$) adalah fungsi jenis p |
| 9 | 25 | 55 | $\cos2(\phi - 45°) = \sin2\phi$ |
| 10 | tidak; campuran dua energi berbeda | 56 | 0 (simpul); tidak nol (maksimum sudutnya di 45°) |
| 11 | $E = -\tfrac18$ | 57 | 13,5; 12,5 bohr |
| 12 | $r = 2$; $V_\text{ef} = -\tfrac14$ | 58 | 1,51; $-3{,}02$ eV |
| 13 | $\int u^2dr = \int r^{-2}dr$ divergen di 0 | 59 | 0,75 bohr = 39,7 pm |
| 14 | $-Z^2/2(\ell+1)^2 > -Z^2/2\ell(\ell+1)$ | 60 | $4\int re^{-2r}dr = 1$ |
| 15 | 1; 1 | 61 | 30; 2,24 bohr |
| 16 | $\kappa = \tfrac12$; $E = -\tfrac18$ | 62 | 2; $2{,}19 \times 10^6$ m/s |
| 17 | $u = r^3e^{-r/3}$ | 63 | dari (7.17) dan (7.15) |
| 18 | $f = 1 - \tfrac23r + \tfrac{2}{27}r^2$ | 64 | $-54{,}4$; $-13{,}6$ |
| 19 | tidak: $n = 1/\kappa = 1{,}29$ bukan bulat | 65 | 17,6 pm |
| 20 | $(2\kappa)^{k+1}/(k+1)! \div (2\kappa)^k/k!$ | 66 | 217,7 eV |
| 21 | $2[Z - 1] = 0$ | 67 | 7,44 keV |
| 22 | $-13{,}598$; $-3{,}400$; $-1{,}511$; $-0{,}850$ | 68 | $Z = 24$, kromium |
| 23 | 364,7 nm; 91,18 nm | 69 | 164,1 nm |
| 24 | 50 | 70 | perpindahan elektron resonan H(1s) → He⁺($n = 2$) sangat efisien |
| 25 | 4052 nm | 71 | 2p, 3p (dan 4p, tetapi berenergi sama) |
| 26 | 3,7 meV | 72 | Lyman (dari 1s) |
| 27 | $n \approx 87$ | 73 | $\Delta\ell = 0$ |
| 28 | 2466,04 THz; struktur halus dan pergeseran Lamb | 74 | 1,290; $0{,}745\,a_0$ |
| 29 | 1; 2 | 75 | 29 MHz |
| 30 | 6 bohr = 317,5 pm | 76 | $(600/121{,}6)^3 = 120$ |
| 31 | 1 bohr | 77 | $\omega$ sangat kecil (1 GHz); $A \propto \omega^3$ sekitar $10^{-9}$ s⁻¹ |
| 32 | $\tfrac18$ | 78 | 0,233 cm⁻¹ |
| 33 | 8 kali | 79 | 21,0 GHz |
| 34 | $4\int r^2e^{-2r}dr = 1$ | 80 | 7 |
| 35 | 1,87; 6,61; 15,52 bohr | 81 | 0,0035 nm |
| 36 | 9 bohr (476 pm); 16 bohr | 82 | linear, sejajar medan |
| 37 | 0,5 bohr | 83 | spin elektron (efek Zeeman anomal) |
| 38 | $dP/dr = 0$ | 84 | 0,19 |
| 39 | 0,762; 0,062 | 85 | `V = -2 / r`; $-2$ hartree |
| 40 | 0,371 | 86 | perilaku penyelesaian yang dapat diterima di dekat inti |
| 41 | 13,07 bohr | 87 | $\approx 1 \times 10^{-3}$ hartree |
| 42 | ekor eksponensial panjang; ya untuk orbital tanpa simpul ($\langle r\rangle = n(n + \tfrac12)$ vs $n^2$) | 88 | $-\tfrac1{18} = -0{,}0556$ hartree |
| 43 | $\tfrac{1}{4\sqrt{2\pi}}\,y\,e^{-r/2}$ | 89 | rapat di dekat inti, renggang di luar |
| 44 | $4\hbar^2$ | 90 | naik (penyaringan lebih efektif, menuju hidrogen) |
| 45 | ya, $m = 0$ | 91 | $-0{,}490$; $-0{,}407$; $-0{,}327$; $-0{,}148$; $-0{,}010$ |
| 46 | $-(p_x + ip_y)/\sqrt2$ |  |  |
:::


# Pembahasan soal terpilih

**Soal 6.** $dE/dr = -1/r^3 + Z/r^2 = 0$ memberi $r = 1/Z$. Masukkan: $E = Z^2/2 - Z^2 = -Z^2/2$.

*Cara berpikir:* penskalaan $r \propto 1/Z$ dan $E \propto Z^2$ sudah terlihat dari analisis dimensi ini, tanpa menyelesaikan persamaan apa pun. Taksiran semacam ini juga menunjukkan mengapa elektron dalam atom berat sangat terikat dan sangat dekat ke inti: untuk emas, elektron 1s berada sekitar $1/79$ bohr dari inti dan terikat sekitar $79^2/2 \approx 3100$ hartree (lebih dari 80 keV).

**Soal 18.** Dengan $\kappa = \tfrac13$, $\ell = 0$, $Z = 1$: $a_1 = \tfrac{2[\tfrac13 - 1]}{(1)(2)}a_0 = -\tfrac23$; $a_2 = \tfrac{2[\tfrac23 - 1]}{(2)(3)}a_1 = \left(-\tfrac19\right)\left(-\tfrac23\right) = \tfrac{2}{27}$; $a_3 = \tfrac{2[1 - 1]}{(3)(4)}a_2 = 0$. Jadi $f = 1 - \tfrac23r + \tfrac{2}{27}r^2 = \tfrac{1}{27}(27 - 18r + 2r^2)$, dan $R = u/r = f\,e^{-r/3}$.

*Cara berpikir:* deret berhenti tepat pada $k = n - \ell - 1 = 2$. Tanda koefisien berganti-ganti, sehingga polinomnya mempunyai dua akar positif: dua simpul radial 3s (Contoh 7.14).

**Soal 41.** $P(r) = r^2R_{30}^2 \propto r^2(27 - 18r + 2r^2)^2e^{-2r/3}$. Turunan $P$ nol di simpul ($r = 1{,}90$ dan $7{,}10$) dan di tiga maksimum. Secara numerik, maksimum terbesar di $r = 13{,}07$ bohr (692 pm); dua maksimum kecil di sekitar 0,74 dan 4,19 bohr.

*Cara berpikir:* jari-jari paling mungkin 3s (13,07) lebih besar daripada 3d (9), tetapi 3s mempunyai dua lobus dalam yang menembus dekat inti. Gambar 7.2 memperlihatkan keduanya: 3s "lebih besar dan lebih dalam" sekaligus. Ukuran dan penembusan adalah dua sifat berbeda.

**Soal 62.** $\langle 1/r^2\rangle = \int_0^\infty4r^2e^{-2r}r^{-2}dr = 4\int_0^\infty e^{-2r}dr = 2$, sama dengan $Z^2/n^3(\ell + \tfrac12) = 1/(1 \cdot \tfrac12) = 2$. Dari $\langle T\rangle = \tfrac12$ hartree, $\langle p^2\rangle = 1$, sehingga $v_\text{rms} = 1$ satuan atom $= 2{,}19 \times 10^6$ m/s.

*Cara berpikir:* kecepatan rms elektron 1s sama dengan kecepatan orbit Bohr pertama ($\alpha c$). Nilai $\langle 1/r^2\rangle$ muncul dalam koreksi relativistik dan dalam kopling spin–orbit (Bab 9); ia berbanding terbalik dengan $\ell + \tfrac12$, sehingga koreksi terbesar untuk orbital s.

**Soal 74.** $\int_0^\infty R_{10}R_{21}r^3dr = \int_0^\infty 2e^{-r}\cdot\tfrac{1}{2\sqrt6}re^{-r/2}r^3dr = \tfrac{1}{\sqrt6}\int_0^\infty r^4e^{-3r/2}dr = \tfrac{1}{\sqrt6}\cdot\tfrac{4!}{(3/2)^5} = \tfrac{24}{7{,}594\sqrt6} = 1{,}290$. Bagian sudut $\int Y_0^0\cos\theta\,Y_1^0\,d\Omega = 1/\sqrt3$. Hasil kalinya $0{,}745 = 128\sqrt2/243$.

*Cara berpikir:* unsur matriks dipol transisi sepanjang 0,75 bohr: elektron yang "bergoyang" antara 1s dan 2p menggeser pusat muatannya sekitar 40 pm. Kekuatan osilator transisi Lyman-α, $f = \tfrac23\Delta E|\langle 1s|\mathbf r|2p\rangle|^2 = 0{,}416$, adalah salah satu yang terbesar di antara transisi atom.

**Soal 91.** Ganti satu baris program: `V = -np.exp(-r/lam)/r`. Dengan kisi 0,002 sampai 80 bohr: $\lambda = 100$: $-0{,}490$; $\lambda = 10$: $-0{,}407$; $\lambda = 5$: $-0{,}327$; $\lambda = 2$: $-0{,}148$; $\lambda = 1$: $-0{,}0103$ hartree. Keadaan 2s hilang (tidak terikat) sebelum $\lambda = 2$.

*Cara berpikir:* penyaringan muatan oleh elektron dan ion bebas di sekitarnya melemahkan ikatan; di bawah $\lambda_c \approx 0{,}84$ bohr tidak ada keadaan terikat sama sekali. Dalam plasma rapat (interior bintang, plasma laser), garis-garis spektrum tingkat tinggi menghilang satu per satu ketika tingkatnya melewati batas ionisasi: **penurunan energi ionisasi** yang teramati sebagai berakhirnya deret Balmer lebih awal daripada di laboratorium. Degenerasi $\ell$ juga pecah, karena potensialnya tidak lagi $1/r$ murni.

# Bacaan lanjut

1. I. N. Levine, *Quantum Chemistry*, edisi ke-7 (Pearson, 2014), Bab 6. Penyelesaian lengkap atom hidrogen, orbital riil, dan efek Zeeman.
2. D. A. McQuarrie, *Quantum Chemistry*, edisi ke-2 (University Science Books, 2008), Bab 7. Atom hidrogen dengan banyak gambar dan latihan.
3. H. A. Bethe dan E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957; Dover, 2008). Rujukan klasik: nilai harap, unsur matriks, laju transisi, struktur halus, dan efek medan luar.
4. P. Atkins dan R. Friedman, *Molecular Quantum Mechanics*, edisi ke-5 (Oxford University Press, 2011), Bab 3. Atom hidrogen dan atom mirip hidrogen dengan sudut pandang kimia.
5. G. W. F. Drake (ed.), *Springer Handbook of Atomic, Molecular, and Optical Physics* (Springer, 2006). Data spektroskopi hidrogen dan ion mirip hidrogen dengan ketelitian tinggi.
6. P. Pyykkö, "Relativistic effects in chemistry: more common than you thought", *Annual Review of Physical Chemistry* 63, 45–64 (2012). Pengantar efek relativistik yang disinggung di Contoh 7.30.
