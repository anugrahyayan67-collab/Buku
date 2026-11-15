## 9.3 Partikel identik dan teorema spin–statistik

### Tak dapat dibedakan secara mendasar

Dua kelereng yang dibuat persis sama tetap dapat dibedakan: kita dapat mengikuti lintasan masing-masing, dan dengan begitu selalu tahu kelereng mana yang mana. Dalam mekanika kuantum, partikel tidak mempunyai lintasan. Ketika dua elektron saling mendekat dan fungsi gelombangnya bertumpang tindih, tidak ada cara, bahkan secara prinsip, untuk mengatakan elektron mana yang keluar ke kiri dan mana ke kanan setelah tumbukan. Elektron-elektron bersifat **identik** dalam arti yang paling kuat: semua sifat fisika yang dapat diukur harus sama bila label kedua elektron ditukar.

Tinjau dua partikel identik dengan fungsi gelombang $\Psi(1, 2)$, dengan "1" menyatakan semua koordinat (ruang dan spin) partikel pertama. Definisikan **operator pertukaran** $\hat P_{12}$:

$$
\hat P_{12}\Psi(1, 2) = \Psi(2, 1) . \qquad \text{(9.12)}
$$

Karena partikel identik, Hamiltoniannya simetris terhadap pertukaran (Hamiltonian helium, persamaan (8.1), tidak berubah bila indeks 1 dan 2 ditukar), sehingga $[\hat H, \hat P_{12}] = 0$, dan fungsi eigen $\hat H$ dapat dipilih sebagai fungsi eigen $\hat P_{12}$ juga. Menukar dua kali mengembalikan keadaan semula, $\hat P_{12}^2 = 1$, sehingga nilai eigen $\hat P_{12}$ hanya $+1$ atau $-1$:

$$
\Psi(2, 1) = +\Psi(1, 2)\quad\text{(simetris)} \qquad\text{atau}\qquad \Psi(2, 1) = -\Psi(1, 2)\quad\text{(antisimetris)} .
$$

Alam ternyata tidak membiarkan pilihan ini terbuka. Untuk setiap jenis partikel, tandanya tetap, dan karena $\hat P_{12}$ komut dengan $\hat H$, tanda itu tidak pernah berubah selama evolusi waktu.

### Teorema spin–statistik

Partikel yang fungsi gelombangnya **antisimetris** disebut **fermion**; yang **simetris** disebut **boson**. Pauli (1940), dengan memadukan mekanika kuantum dan relativitas khusus, membuktikan hubungan yang dalam antara jenis ini dan spin:

::: {.inti}
**Teorema spin–statistik**

Partikel berspin setengah bulat ($\tfrac12, \tfrac32, \ldots$) adalah **fermion**: fungsi gelombangnya berubah tanda bila dua partikel identik dipertukarkan. Partikel berspin bulat ($0, 1, 2, \ldots$) adalah **boson**: fungsi gelombangnya tidak berubah. Elektron, proton, dan neutron adalah fermion; foton adalah boson.
:::

Untuk partikel majemuk (inti, atom, molekul) yang dipertukarkan sebagai satu kesatuan, tandanya adalah $(-1)^N$, dengan $N$ jumlah fermion penyusunnya. Dalam mekanika kuantum nonrelativistik yang kita pakai, pernyataan ini tidak dapat diturunkan; ia adalah postulat tambahan (Postulat 7 di subbab 4.13), dan sejauh ini tidak pernah dilanggar oleh percobaan mana pun.

### Akibat yang terukur: "gaya" pertukaran

Simetri pertukaran bukan sekadar soal tanda; ia mengubah di mana partikel-partikel cenderung berada. Ambil dua partikel bebas dalam kotak satu dimensi, satu di keadaan $\psi_a$ dan satu di $\psi_b$, dan abaikan spin dan interaksinya. Ada tiga kemungkinan fungsi gelombang:

$$
\Psi_\text{D} = \psi_a(x_1)\psi_b(x_2) , \qquad \Psi_\pm = \frac{1}{\sqrt2}\left[\psi_a(x_1)\psi_b(x_2) \pm \psi_b(x_1)\psi_a(x_2)\right] , \qquad \text{(9.13)}
$$

untuk partikel yang dapat dibedakan (D), boson ($+$), dan fermion ($-$) tanpa spin. Hitunglah rata-rata kuadrat jarak antarpartikel, $\langle(x_1 - x_2)^2\rangle = \langle x_1^2\rangle + \langle x_2^2\rangle - 2\langle x_1x_2\rangle$. Dua suku pertama sama untuk ketiga fungsi: $\langle x^2\rangle_a + \langle x^2\rangle_b$. Suku silangnya berbeda: untuk $\Psi_\text{D}$, $\langle x_1x_2\rangle = \langle x\rangle_a\langle x\rangle_b$; untuk $\Psi_\pm$, uraian kuadrat menghasilkan tambahan suku "pertukaran":

$$
\langle(x_1 - x_2)^2\rangle_\pm = \langle(x_1 - x_2)^2\rangle_\text{D} \mp 2|\langle x\rangle_{ab}|^2 , \qquad \langle x\rangle_{ab} = \int\psi_a^*x\,\psi_b\,dx . \qquad \text{(9.14)}
$$

Boson cenderung **berdekatan**, fermion cenderung **berjauhan**, dibandingkan partikel yang dapat dibedakan, padahal tidak ada gaya di antara mereka. Efek ini sering disebut "gaya pertukaran", walaupun sebenarnya bukan gaya, melainkan akibat geometri fungsi gelombang yang simetris atau antisimetris. Untuk fermion, $\Psi_-$ nol tepat ketika $x_1 = x_2$: dua fermion dengan spin sama tidak pernah berada di titik yang sama, dan di sekitar setiap fermion ada daerah yang "dihindari" fermion lain, yaitu **lubang Fermi** (lubang pertukaran) yang sudah kita temui pada helium tereksitasi di subbab 8.9.

::: {.contoh}
**Contoh 9.7 · Fermion atau boson?**

Tentukan apakah partikel berikut fermion atau boson: (a) inti ⁴He dan atom ⁴He; (b) atom ³He; (c) atom ⁷Li dan ⁶Li; (d) atom hidrogen dan deuterium; (e) molekul H₂ sebagai satu kesatuan.

**Penyelesaian.** Hitung jumlah fermion (proton, neutron, elektron). (a) Inti ⁴He: 2p + 2n = 4, boson; atom: tambah 2e, 6, boson. (b) ³He: 2p + 1n + 2e = 5, fermion. (c) ⁷Li: 3p + 4n + 3e = 10, boson; ⁶Li: 9, fermion. (d) H: 1p + 1e = 2, boson; D: 1p + 1n + 1e = 3, fermion. (e) H₂: 4, boson.

**Memahami hasil.** Perbedaan satu neutron mengubah perilaku kolektif secara total. Helium-4 cair menjadi superfluida (mengalir tanpa kekentalan) di bawah 2,17 K, karena atom-atom boson dapat menempati keadaan kuantum yang sama dalam jumlah makroskopik (kondensasi Bose–Einstein). Helium-3 cair baru menjadi superfluida di sekitar 2,5 mK, setelah atom-atom fermionnya berpasangan menjadi "boson majemuk", mirip pasangan elektron dalam superkonduktor. Gas atom ⁷Li dan ⁶Li yang didinginkan dengan laser sampai nanokelvin juga berperilaku sangat berbeda; kedua isotop ini menjadi bahan baku utama penelitian gas kuantum.
:::

::: {.contoh}
**Contoh 9.8 · Dua partikel dalam kotak: jarak rata-rata**

Dua partikel dalam kotak sepanjang $L$ menempati $n = 1$ dan $n = 2$. Diketahui $\langle x\rangle_n = L/2$, $\langle x^2\rangle_n = L^2(\tfrac13 - 1/2n^2\pi^2)$, dan $\langle x\rangle_{12} = -16L/9\pi^2$. Hitung akar rata-rata kuadrat jarak antarpartikel untuk partikel yang dapat dibedakan, boson, dan fermion.

**Penyelesaian.** $\langle x^2\rangle_1 + \langle x^2\rangle_2 = L^2(0{,}2827 + 0{,}3207) = 0{,}6034L^2$; $2\langle x\rangle_1\langle x\rangle_2 = 0{,}5L^2$. Jadi $\langle(x_1 - x_2)^2\rangle_\text{D} = 0{,}1033L^2$. Suku pertukaran $2|\langle x\rangle_{12}|^2 = 2(0{,}1801)^2L^2 = 0{,}0649L^2$. Boson: $0{,}0384L^2$; fermion: $0{,}1682L^2$. Akar-akarnya: 0,321$L$; 0,196$L$; 0,410$L$.

**Memahami hasil.** Tanpa gaya apa pun, fermion rata-rata 28% lebih berjauhan daripada partikel yang dapat dibedakan, dan boson 39% lebih berdekatan. Dalam atom dan molekul, efek ini membuat elektron-elektron berspin sama saling menghindar sehingga tolakan Coulomb-nya berkurang, asal mula aturan Hund (subbab 9.12). Gambar 9.2 memperlihatkan rapat peluang dua partikel dalam bidang $(x_1, x_2)$: fermion kosong di sepanjang diagonal $x_1 = x_2$, boson menumpuk di sana.
:::

![Gambar 9.2 Rapat peluang $|\Psi(x_1, x_2)|^2$ untuk dua partikel dalam kotak di keadaan $n = 1$ dan $n = 2$. Kiri: partikel yang dapat dibedakan. Tengah: boson (fungsi simetris), dengan peluang besar di sepanjang diagonal $x_1 = x_2$ (garis putus-putus). Kanan: fermion (fungsi antisimetris), dengan peluang nol di diagonal: lubang Fermi.](fig/c_identik.png){width=95%}

::: {.contoh}
**Contoh 9.9 · Menghitung keadaan dua partikel**

Dua partikel ditempatkan pada tiga keadaan satu partikel $a$, $b$, $c$ (misalnya tiga orbital, abaikan spin). Berapa banyak keadaan dua partikel yang berbeda bila partikelnya (a) dapat dibedakan, (b) boson, (c) fermion?

**Penyelesaian.** (a) Setiap partikel dapat di salah satu dari tiga keadaan: $3 \times 3 = 9$. (b) Boson: fungsi simetris, termasuk keduanya di keadaan yang sama: $aa$, $bb$, $cc$, $ab$, $ac$, $bc$, yaitu 6. (c) Fermion: fungsi antisimetris, keduanya tidak boleh di keadaan yang sama: $ab$, $ac$, $bc$, yaitu 3.

**Memahami hasil.** Secara umum, untuk $g$ keadaan dan dua partikel: $g^2$, $g(g + 1)/2$, dan $g(g - 1)/2$. Dengan $g$ besar ketiganya mendekati $g^2/2$ (setelah membagi dengan $2!$ untuk yang identik), sehingga statistik klasik berlaku pada suhu tinggi, ketika banyak keadaan tersedia per partikel. Pada suhu rendah atau kerapatan tinggi, $g$ efektif kecil dan perbedaannya menentukan segalanya: statistik Fermi–Dirac menjelaskan elektron dalam logam, statistik Bose–Einstein menjelaskan radiasi benda hitam (subbab 1.3) dan helium superfluida. Bobot statistik orto- dan para-hidrogen (subbab 6.11) adalah contoh kimia dari perhitungan yang sama, untuk spin inti.
:::

::: {.kuis}
**Kuis cepat 9.3**

(a) Apakah molekul D₂ boson atau fermion? Apakah inti deuteron boson atau fermion? (b) Mengapa $\Psi_-$ di (9.13) nol bila $\psi_a = \psi_b$? (c) Apakah "gaya pertukaran" dapat diukur dengan dinamometer? Jelaskan.
:::

## 9.4 Atom helium dan fungsi spin

### Fungsi spin dua elektron

Dengan spin, fungsi gelombang dua elektron adalah fungsi dari koordinat ruang dan spin keduanya. Bila Hamiltonian tidak memuat spin, fungsi itu dapat ditulis sebagai hasil kali fungsi ruang $\psi(\mathbf r_1, \mathbf r_2)$ dan fungsi spin $\sigma(1, 2)$. Ada empat hasil kali fungsi spin satu elektron: $\alpha(1)\alpha(2)$, $\alpha(1)\beta(2)$, $\beta(1)\alpha(2)$, $\beta(1)\beta(2)$. Dua yang di tengah tidak simetris maupun antisimetris terhadap pertukaran, tetapi jumlah dan selisihnya simetris dan antisimetris. Himpunan yang lebih berguna adalah

$$
\text{triplet } (S = 1):\quad \begin{cases}\alpha(1)\alpha(2) & M_S = +1\\ \frac{1}{\sqrt2}[\alpha(1)\beta(2) + \beta(1)\alpha(2)] & M_S = 0\\ \beta(1)\beta(2) & M_S = -1\end{cases} \qquad \text{singlet } (S = 0):\quad \frac{1}{\sqrt2}[\alpha(1)\beta(2) - \beta(1)\alpha(2)] . \qquad \text{(9.15)}
$$

Ketiga fungsi triplet simetris terhadap pertukaran; fungsi singlet antisimetris. Nama "triplet" dan "singlet" berasal dari jumlah fungsinya, yang dalam medan magnet menghasilkan tiga atau satu tingkat.

Mengapa pengelompokan ini yang benar? Spin total $\hat{\mathbf S} = \hat{\mathbf S}_1 + \hat{\mathbf S}_2$ memenuhi aljabar momentum sudut, dan keempat fungsi di atas adalah fungsi eigen $\hat S^2$ dan $\hat S_z$. Untuk $\hat S_z = \hat S_{1z} + \hat S_{2z}$ hal itu jelas: $M_S$ adalah jumlah $m_s$. Untuk $\hat S^2$, uraikan

$$
\hat S^2 = \hat S_1^2 + \hat S_2^2 + 2\hat{\mathbf S}_1\cdot\hat{\mathbf S}_2 , \qquad 2\hat{\mathbf S}_1\cdot\hat{\mathbf S}_2 = 2\hat S_{1z}\hat S_{2z} + \hat S_{1+}\hat S_{2-} + \hat S_{1-}\hat S_{2+} . \qquad \text{(9.16)}
$$

Bentuk kedua diperoleh dari $\hat S_x = \tfrac12(\hat S_+ + \hat S_-)$ dan $\hat S_y = \tfrac{1}{2i}(\hat S_+ - \hat S_-)$. Operator tangga menukar $\alpha$ dan $\beta$ antara kedua elektron (Contoh 9.10), sehingga fungsi $\alpha\beta \pm \beta\alpha$ adalah fungsi eigen. Hasilnya: $S(S + 1) = 2$ ($S = 1$) untuk ketiga fungsi simetris dan $S(S + 1) = 0$ ($S = 0$) untuk fungsi antisimetris. Penjumlahan dua spin $\tfrac12$ adalah kasus paling sederhana dari penjumlahan momentum sudut (subbab 9.11).

### Fungsi total yang antisimetris

Elektron adalah fermion, sehingga fungsi **total** (ruang × spin) harus antisimetris. Ada dua cara memenuhinya:

$$
\Psi = \psi_\text{simetris}(\mathbf r_1, \mathbf r_2) \times \sigma_\text{singlet} \qquad\text{atau}\qquad \Psi = \psi_\text{antisimetris}(\mathbf r_1, \mathbf r_2) \times \sigma_\text{triplet} . \qquad \text{(9.17)}
$$

**Keadaan dasar helium.** Fungsi ruang $1s(1)1s(2)$ simetris, sehingga harus dipasangkan dengan singlet:

$$
\Psi(1s^2) = 1s(1)1s(2)\cdot\frac{1}{\sqrt2}[\alpha(1)\beta(2) - \beta(1)\alpha(2)] . \qquad \text{(9.18)}
$$

Tidak ada triplet $1s^2$: fungsi ruang antisimetris $1s(1)1s(2) - 1s(2)1s(1)$ adalah nol. Keadaan dasar helium adalah singlet, dengan spin total nol dan tanpa momen magnet; helium diamagnetik.

**Keadaan tereksitasi.** Untuk konfigurasi 1s2s, kedua fungsi ruang di persamaan (8.44) tersedia. Fungsi ruang simetris $\psi_+$ berpasangan dengan singlet (suku $^1$S), dan fungsi ruang antisimetris $\psi_-$ berpasangan dengan triplet (suku $^3$S). Teori perturbasi terdegenerasi di subbab 8.9 memberi energi $E^{(0)} + J + K$ untuk singlet dan $E^{(0)} + J - K$ untuk triplet. Sekarang terlihat mengapa ada **tiga** keadaan triplet dan **satu** singlet, dan mengapa tingkat triplet tidak pecah lebih lanjut dalam Hamiltonian tanpa spin: ketiga fungsi spin triplet berpasangan dengan fungsi ruang yang sama.

Perhatikan apa yang terjadi. Hamiltonian tidak memuat spin sama sekali, tetapi energi bergantung pada spin total. Penyebabnya adalah antisimetri: spin menentukan simetri fungsi ruang, dan simetri fungsi ruang menentukan seberapa dekat elektron-elektron berada, sehingga menentukan tolakan Coulomb-nya.

### Hamiltonian spin efektif

Untuk dua spin $\tfrac12$, $\hat{\mathbf S}_1\cdot\hat{\mathbf S}_2 = \tfrac12(\hat S^2 - \hat S_1^2 - \hat S_2^2)$ bernilai $+\tfrac14\hbar^2$ untuk triplet dan $-\tfrac34\hbar^2$ untuk singlet. Maka kedua energi $J \pm K$ dapat ditulis dalam satu rumus:

$$
E = E^{(0)} + J - \tfrac12K - \frac{2K}{\hbar^2}\hat{\mathbf S}_1\cdot\hat{\mathbf S}_2 . \qquad \text{(9.19)}
$$

Inilah Hamiltonian pertukaran Dirac–Heisenberg: interaksi Coulomb yang dipadukan dengan antisimetri tampak **seolah-olah** interaksi langsung antara dua spin. Dalam bentuk umum $\hat H = -2J_\text{ex}\hat{\mathbf S}_1\cdot\hat{\mathbf S}_2/\hbar^2$, tanda $J_\text{ex}$ menentukan apakah spin-spin cenderung sejajar ($J_\text{ex} > 0$, feromagnetik) atau berlawanan ($J_\text{ex} < 0$, antiferomagnetik). Kemagnetan besi dan kobalt, kopling antara ion-ion logam dalam kompleks berinti banyak, dan keadaan dasar diradikal organik semuanya diatur oleh "interaksi pertukaran" ini, yang besarnya ratusan sampai ribuan kali interaksi magnetik dipol–dipol yang sebenarnya.

::: {.contoh}
**Contoh 9.10 · Memeriksa $\hat S^2$ pada fungsi spin**

Gunakan (9.16) dan (9.7) untuk menghitung $\hat S^2$ pada $\alpha(1)\beta(2)$, lalu tunjukkan bahwa kombinasi $\alpha\beta - \beta\alpha$ mempunyai $S = 0$ dan $\alpha\beta + \beta\alpha$ mempunyai $S = 1$.

**Penyelesaian.** Dengan $\hat S_1^2 = \hat S_2^2 = \tfrac34\hbar^2$ pada setiap fungsi: $(\hat S_1^2 + \hat S_2^2)\alpha\beta = \tfrac32\hbar^2\alpha\beta$. $2\hat S_{1z}\hat S_{2z}\alpha\beta = 2(\tfrac12\hbar)(-\tfrac12\hbar)\alpha\beta = -\tfrac12\hbar^2\alpha\beta$. $\hat S_{1+}\hat S_{2-}\alpha\beta = 0$ (karena $\hat S_{1+}\alpha = 0$). $\hat S_{1-}\hat S_{2+}\alpha\beta = (\hbar\beta)(\hbar\alpha) = \hbar^2\beta\alpha$. Jadi

$$
\hat S^2\alpha\beta = \hbar^2(\alpha\beta + \beta\alpha) , \qquad\text{dan serupa}\qquad \hat S^2\beta\alpha = \hbar^2(\beta\alpha + \alpha\beta) .
$$

Maka $\hat S^2(\alpha\beta - \beta\alpha) = 0$ dan $\hat S^2(\alpha\beta + \beta\alpha) = 2\hbar^2(\alpha\beta + \beta\alpha)$, yaitu $S(S + 1) = 0$ dan 2.

**Memahami hasil.** Fungsi $\alpha\beta$ sendiri, yang secara naif tampak sebagai "satu spin ke atas, satu ke bawah", bukan keadaan dengan spin total tertentu; ia adalah campuran setara singlet dan triplet $M_S = 0$. Ini penting dalam praktik: determinan Slater tunggal seperti $|1s\alpha\,2s\beta|$ bukan fungsi eigen $\hat S^2$ (subbab 9.6), sehingga perhitungan keadaan tereksitasi harus menggabungkan determinan-determinan dengan benar untuk memperoleh singlet dan triplet murni.
:::

::: {.contoh}
**Contoh 9.11 · Ortohelium dan parahelium**

Spektrum helium terdiri atas dua sistem garis yang hampir tidak saling berhubungan. (a) Garis 1083,3 nm berasal dari transisi $2^3$P → $2^3$S, dan garis 2058,7 nm dari $2^1$P → $2^1$S. Hitung energi fotonnya dan bandingkan dengan selisih J yang dihitung di subbab 8.9. (b) Mengapa keadaan $2^3$S tidak dapat memancar ke keadaan dasar $1^1$S dengan transisi dipol listrik?

**Penyelesaian.** (a) $E = hc/\lambda$: 1083,3 nm → 1,1445 eV; 2058,7 nm → 0,6023 eV. Dari subbab 8.9, perturbasi orde pertama memberi selisih $2^3$P − $2^3$S sebesar 2,06 eV dan $2^1$P − $2^1$S sebesar 1,53 eV: orde besaran benar, nilainya terlalu besar.

(b) Ada dua larangan sekaligus: $\Delta S = 1$ (triplet ke singlet, subbab 8.12) dan $\Delta\ell = 0$ (s ke s).

**Memahami hasil.** Karena transisi antara singlet dan triplet hampir terlarang, helium berperilaku seolah-olah dua gas berbeda: "parahelium" (singlet) dan "ortohelium" (triplet). Keadaan $2^3$S bertahan sekitar 7900 s, sehingga helium metastabil dapat dikumpulkan dalam jumlah besar dalam lucutan gas dan dipakai untuk mengionisasi molekul lain melalui tumbukan (spektroskopi ionisasi Penning). Garis 1083 nm dipakai astronom untuk memetakan helium di atmosfer Matahari dan, baru-baru ini, di atmosfer planet di luar Tata Surya yang sedang menguap.
:::

::: {.contoh}
**Contoh 9.12 · Pertukaran dalam kompleks tembaga berinti dua**

Dalam tembaga(II) asetat hidrat, dua ion Cu²⁺ (masing-masing dengan satu elektron tak berpasangan) terkopel antiferomagnetik, sehingga keadaan singlet lebih rendah sekitar 300 cm⁻¹ daripada triplet. (a) Pada 298 K ($k_BT = 207$ cm⁻¹), berapa bagian molekul yang berada dalam keadaan triplet? (b) Pada 77 K ($k_BT = 53{,}5$ cm⁻¹)? (c) Apa akibatnya bagi sifat magnetnya?

**Penyelesaian.** Triplet berbobot 3, singlet 1. Bagian triplet $= 3e^{-\Delta/k_BT}/(1 + 3e^{-\Delta/k_BT})$. (a) $\Delta/k_BT = 1{,}45$: $3(0{,}235)/(1 + 0{,}705) = 0{,}41$. (b) $\Delta/k_BT = 5{,}61$: $0{,}011$.

(c) Hanya molekul triplet yang paramagnetik. Kerentanan magnetnya menurun tajam ketika suhu diturunkan, berlawanan dengan hukum Curie biasa.

**Memahami hasil.** Pengukuran kerentanan magnet terhadap suhu (kurva Bleaney–Bowers) memberi besar celah singlet–triplet, yaitu $2J_\text{ex}$ dalam (9.19). Kopling ini bukan interaksi magnetik langsung antara kedua elektron (yang hanya sekitar 0,2 cm⁻¹ pada jarak 2,6 Å), melainkan hasil pertukaran yang diteruskan melalui ligan jembatan karboksilat ("superpertukaran"). Kimia material magnetik molekul dan situs aktif enzim berinti logam banyak memanfaatkan dan mengukur kopling seperti ini.
:::

::: {.kuis}
**Kuis cepat 9.4**

(a) Fungsi spin $\alpha(1)\beta(2)$: apakah fungsi eigen $\hat S_z$? Apakah fungsi eigen $\hat S^2$? (b) Mengapa keadaan dasar helium harus singlet? (c) Dalam (9.19), bila $K > 0$, spin-spin cenderung sejajar atau berlawanan?
:::

## 9.5 Asas larangan Pauli

### Dari antisimetri ke larangan

Misalkan dua elektron menempati spin-orbital yang **sama** $\chi$. Satu-satunya fungsi hasil kali yang tersedia adalah $\chi(1)\chi(2)$, yang simetris. Kombinasi antisimetris $\chi(1)\chi(2) - \chi(2)\chi(1)$ adalah nol. Jadi keadaan seperti itu tidak ada:

::: {.inti}
**Asas larangan Pauli**

Dua elektron (atau dua fermion identik mana pun) tidak dapat menempati spin-orbital yang sama. Dalam atom, tidak ada dua elektron yang mempunyai keempat bilangan kuantum $n$, $\ell$, $m_\ell$, $m_s$ sama. Setiap orbital ruang menampung paling banyak dua elektron, dan bila dua, spinnya berlawanan (berpasangan, singlet).
:::

Pauli merumuskan asas ini pada tahun 1925, berdasarkan pola dalam spektrum atom, sebelum mekanika kuantum lengkap dan sebelum spin dipahami. Rumusan "tidak ada dua elektron dengan bilangan kuantum yang sama" hanya berlaku untuk fungsi gelombang yang disusun dari orbital; rumusan yang lebih dalam, yang tetap berlaku untuk fungsi gelombang berkorelasi yang paling teliti sekalipun, adalah tuntutan **antisimetri**.

### Kulit dan subkulit

Asas Pauli langsung menentukan kapasitas kulit atom. Untuk setiap $\ell$ ada $2\ell + 1$ nilai $m_\ell$ dan dua nilai $m_s$:

$$
\text{subkulit } \ell:\ 2(2\ell + 1) = 2, 6, 10, 14 \ (\text{s, p, d, f}) , \qquad \text{kulit } n:\ \sum_{\ell=0}^{n-1}2(2\ell + 1) = 2n^2 = 2, 8, 18, 32 . \qquad \text{(9.20)}
$$

Tanpa asas Pauli, semua elektron setiap atom akan berada di 1s dalam keadaan dasar. Atom akan makin kecil dan makin sulit bereaksi ketika $Z$ naik, tidak akan ada kulit valensi, tidak ada periodisitas, dan tidak ada kimia sebagaimana kita kenal. Panjang periode tabel periodik (2, 8, 8, 18, 18, 32) bukan sekadar $2n^2$; urutan pengisian subkulit juga berperan, dan itu dibahas di subbab 9.9.

### Tekanan Pauli dan ukuran materi

Asas Pauli juga menjelaskan mengapa materi menempati ruang. Bila dua atom dengan kulit tertutup didesakkan, orbital-orbitalnya bertumpang tindih, dan agar fungsi gelombang total tetap antisimetris, sebagian elektron terpaksa menempati orbital yang lebih tinggi energinya (Contoh 8.19). Hasilnya adalah tolakan jarak pendek yang sangat curam, **tolakan Pauli**, yang menjadi bagian $R^{-12}$ potensial Lennard-Jones, yang menetapkan jari-jari van der Waals atom, dan yang membuat zat cair dan padat hampir tak termampatkan. Dalam teori VSEPR (subbab 12.11), "tolakan antarpasangan elektron" sebagian besar adalah tolakan Pauli.

Pada skala yang lebih besar, gas elektron dalam logam dan gas elektron dalam bintang katai putih menahan diri dari pemampatan karena elektron tidak dapat semuanya menempati keadaan energi terendah. Bila $N$ elektron bebas mengisi keadaan-keadaan momentum dari bawah, dua per keadaan ruang, energi tertinggi yang terisi pada suhu nol mutlak adalah **energi Fermi**

$$
E_F = \frac{\hbar^2}{2m_e}\left(3\pi^2n\right)^{2/3} , \qquad \text{(9.21)}
$$

dengan $n$ kerapatan elektron. Rumus ini adalah perluasan partikel dalam kotak tiga dimensi (subbab 4.5) untuk sangat banyak elektron.

::: {.dalam}
**Lebih dalam: menurunkan energi Fermi**

Tempatkan $N$ elektron bebas dalam kotak kubus bersisi $L$. Keadaan satu elektron diberi label tiga bilangan bulat positif $(n_x, n_y, n_z)$, dengan energi $E = (\hbar^2\pi^2/2m_eL^2)(n_x^2 + n_y^2 + n_z^2)$ (subbab 4.5). Untuk $N$ yang sangat besar, titik-titik $(n_x, n_y, n_z)$ dapat dianggap mengisi ruang secara malar, satu titik per satuan volume. Pada suhu nol, elektron mengisi semua keadaan dengan $n_x^2 + n_y^2 + n_z^2 \le n_F^2$, yaitu seperdelapan bola berjari-jari $n_F$ (hanya oktan positif), dan setiap titik menampung dua elektron (asas Pauli):

$$
N = 2\cdot\frac18\cdot\frac43\pi n_F^3 \quad\Longrightarrow\quad n_F = \left(\frac{3N}{\pi}\right)^{1/3} .
$$

Maka $E_F = (\hbar^2\pi^2/2m_eL^2)n_F^2 = (\hbar^2/2m_e)(3\pi^2N/L^3)^{2/3}$, dan dengan $n = N/L^3$ diperoleh (9.21). Energi Fermi hanya bergantung pada kerapatan elektron, bukan pada ukuran sampel; ia naik seperti $n^{2/3}$ karena makin padat elektron, makin tinggi tangga keadaan yang harus diisi.
:::

::: {.contoh}
**Contoh 9.13 · Enam elektron dalam kotak**

Enam elektron π heksatriena dimodelkan sebagai partikel bebas dalam kotak. (a) Berapa energi total keadaan dasar dalam satuan $E_1$? (b) Seandainya elektron adalah boson tanpa spin, berapa? (c) Berapa energi foton terendah yang dapat diserap dalam kedua kasus?

**Penyelesaian.** (a) Dua elektron per tingkat: $n = 1, 2, 3$ terisi penuh, $E = 2(1 + 4 + 9)E_1 = 28E_1$. (b) Semua di $n = 1$: $6E_1$. (c) Fermion: HOMO $n = 3$ → LUMO $n = 4$, $\Delta E = (16 - 9)E_1 = 7E_1$. Boson: $n = 1 \to 2$, $3E_1$.

**Memahami hasil.** Asas Pauli menaikkan energi keadaan dasar hampir lima kali lipat, dan menggeser serapan ke panjang gelombang lebih pendek. Model elektron bebas untuk poliena dan zat warna sianin (subbab 3.8) memakai asas ini secara diam-diam ketika mengisi dua elektron per tingkat. Dalam gambaran ini, energi tambahan dari asas Pauli adalah energi kinetik: elektron-elektron terpaksa menempati keadaan dengan lebih banyak simpul, yang berarti panjang gelombang lebih pendek dan momentum lebih besar.
:::

::: {.contoh}
**Contoh 9.14 · Energi Fermi natrium**

Natrium (massa jenis 0,968 g/cm³, $M = 22{,}99$ g/mol) menyumbangkan satu elektron valensi per atom ke gas elektron bebas. Hitung (a) kerapatan elektron, (b) energi Fermi, (c) kelajuan elektron pada energi Fermi, dan (d) suhu Fermi $E_F/k_B$.

**Penyelesaian.** (a) $n = (0{,}968/22{,}99)(6{,}022 \times 10^{23}) = 2{,}54 \times 10^{22}$ cm⁻³ $= 2{,}54 \times 10^{28}$ m⁻³. (b) $(3\pi^2n)^{2/3} = (7{,}51 \times 10^{29})^{2/3} = 8{,}26 \times 10^{19}$ m⁻²; $E_F = (1{,}0546 \times 10^{-34})^2(8{,}26 \times 10^{19})/(2 \times 9{,}109 \times 10^{-31}) = 5{,}04 \times 10^{-19}$ J $= 3{,}15$ eV. (c) $v_F = \sqrt{2E_F/m_e} = 1{,}05 \times 10^6$ m/s. (d) $T_F = 3{,}65 \times 10^4$ K.

**Memahami hasil.** Bahkan pada nol mutlak, elektron konduksi natrium bergerak dengan kelajuan sekitar seperseratus kelajuan cahaya, dan energinya setara dengan gas klasik bersuhu 36 000 K. Karena $k_BT$ pada suhu kamar hanya 0,026 eV, hanya sebagian kecil elektron di dekat energi Fermi yang dapat menyerap energi termal. Inilah sebabnya kapasitas kalor elektron logam jauh lebih kecil daripada ramalan teori kinetik klasik, sebuah teka-teki yang baru terpecahkan dengan statistik Fermi–Dirac. Energi Fermi 3,15 eV juga sebanding dengan fungsi kerja natrium (2,3 eV, subbab 1.4): keduanya mengukur kedalaman "lautan" elektron dalam logam.
:::

::: {.contoh}
**Contoh 9.15 · Mengisi kulit dengan asas Pauli**

(a) Daftarkan keempat bilangan kuantum semua elektron yang dapat menempati kulit $n = 2$. (b) Berapa elektron yang dapat mempunyai $n = 3$ dan $m_\ell = +1$? (c) Berapa elektron dalam atom yang dapat mempunyai $n = 4$, $\ell = 3$, $m_s = -\tfrac12$?

**Penyelesaian.** (a) $\ell = 0$: $m_\ell = 0$, $m_s = \pm\tfrac12$ (2 elektron). $\ell = 1$: $m_\ell = -1, 0, 1$, masing-masing $m_s = \pm\tfrac12$ (6 elektron). Jumlah 8. (b) $m_\ell = +1$ mungkin untuk $\ell = 1$ dan $\ell = 2$, masing-masing dengan dua nilai $m_s$: 4 elektron. (c) $\ell = 3$ mempunyai 7 nilai $m_\ell$; dengan $m_s$ tertentu: 7 elektron.

**Memahami hasil.** Penghitungan sederhana ini adalah dasar semua penulisan konfigurasi elektron. Kulit $n = 2$ yang terisi penuh pada neon (8 elektron) adalah kulit oktet kimia dasar; kecenderungan atom periode 2 untuk mencapai delapan elektron valensi (aturan oktet) adalah cerminan langsung dari $2n^2$ untuk $n = 2$. Aturan 18 elektron untuk senyawa logam transisi (subbab 14.13) berasal dari kapasitas gabungan $ns$, $np$, dan $(n-1)d$: $2 + 6 + 10 = 18$.
:::

::: {.kuis}
**Kuis cepat 9.5**

(a) Berapa elektron yang dapat ditampung subkulit 5g ($\ell = 4$)? (b) Apakah konfigurasi $1s^3$ dilarang oleh asas Pauli? Bagaimana dengan $1s^2 2s^2 2p^7$? (c) Mengapa dua atom neon tidak membentuk molekul Ne₂ yang stabil, padahal argon cair ada?
:::

