## 7.7 Orbital kompleks dan orbital riil

### Dua basis untuk ruang yang sama

Fungsi $\psi_{n\ell m} = R_{n\ell}Y_\ell^m$ dengan $m \ne 0$ bernilai kompleks dan merupakan fungsi eigen $\hat L_z$. Karena semua $2\ell + 1$ fungsi dengan $n$ dan $\ell$ yang sama berdegenerasi, kombinasi linear apa pun juga fungsi eigen $\hat H$ dan $\hat L^2$. Kimia hampir selalu memakai kombinasi **riil** (subbab 6.5):

$$
\psi_{n\text{p}_x} = \frac{1}{\sqrt2}(\psi_{n1,-1} - \psi_{n11}), \qquad \psi_{n\text{p}_y} = \frac{i}{\sqrt2}(\psi_{n1,-1} + \psi_{n11}), \qquad \psi_{n\text{p}_z} = \psi_{n10} . \qquad \text{(7.16)}
$$

Untuk $\ell = 2$, pasangan $m = \pm1$ menghasilkan $d_{xz}$ dan $d_{yz}$, pasangan $m = \pm2$ menghasilkan $d_{x^2-y^2}$ dan $d_{xy}$, dan $m = 0$ adalah $d_{z^2}$. Transformasi dari basis kompleks ke basis riil adalah transformasi **uniter**: ia mempertahankan normalisasi dan ortogonalitas, sehingga kedua basis sama sah.

### Kapan memakai yang mana

* **Orbital kompleks** adalah fungsi eigen $\hat L_z$; rapat peluangnya simetris terhadap sumbu $z$ (berbentuk donat untuk $|m| > 0$). Basis ini alami bila ada medan magnet sepanjang $z$ (efek Zeeman, subbab 7.12), bila momentum sudut perlu dijumlahkan (Bab 9), atau untuk molekul linear.
* **Orbital riil** mempunyai arah yang jelas (sepanjang sumbu atau di antara sumbu). Basis ini alami untuk ikatan berarah, hibridisasi (Bab 12), dan medan ligan (Bab 14), karena simetri molekul biasanya ditentukan oleh sumbu-sumbu Kartesius.

Dalam atom bebas tanpa medan, pilihan basis tidak mengubah apa pun yang dapat diukur: energi sama, dan subkulit penuh tetap bersimetri bola (teorema Unsöld).

::: {.contoh}
**Contoh 7.26 · Fungsi 2p$_x$ lengkap**

Tuliskan $\psi_{2\text{p}_x}$ hidrogen ternormalisasi dalam koordinat Kartesius.

**Penyelesaian.** $\psi_{2\text{p}_x} = R_{21}(r)\sqrt{\tfrac{3}{4\pi}}\sin\theta\cos\phi = \tfrac{1}{2\sqrt6}re^{-r/2}\sqrt{\tfrac{3}{4\pi}}\sin\theta\cos\phi$. Dengan $r\sin\theta\cos\phi = x$: $\psi_{2\text{p}_x} = \tfrac{1}{4\sqrt{2\pi}}\,x\,e^{-r/2}$.

**Memahami hasil.** Nama "p$_x$" bukan sekadar label: fungsi itu memang sebanding dengan $x$ dikali fungsi yang bersimetri bola. Bidang simpulnya adalah $x = 0$ (bidang $yz$). Bentuk Kartesius ini yang dipakai dalam fungsi basis Gauss kimia komputasi: $x\,e^{-\alpha r^2}$ untuk fungsi p, $xy\,e^{-\alpha r^2}$ untuk fungsi d (Bab 17).
:::

::: {.contoh}
**Contoh 7.27 · Momentum sudut orbital riil**

Untuk elektron pada orbital $2\text{p}_x$, hitung $\langle L_z\rangle$, $\langle L_z^2\rangle$, dan $\langle L^2\rangle$.

**Penyelesaian.** $2\text{p}_x$ adalah campuran sama besar $m = +1$ dan $m = -1$ (koefisien $\mp1/\sqrt2$). $\langle L_z\rangle = \tfrac12(\hbar) + \tfrac12(-\hbar) = 0$; $\langle L_z^2\rangle = \tfrac12\hbar^2 + \tfrac12\hbar^2 = \hbar^2$; $\langle L^2\rangle = 2\hbar^2$ (tajam, karena $\ell = 1$ untuk kedua komponen).

**Memahami hasil.** Elektron di $\text{p}_x$ tidak "berputar" ke arah mana pun secara rata-rata, tetapi momentum sudutnya tidak nol. Dalam molekul dan kompleks, medan ligan memaksa elektron menempati orbital riil, sehingga $\langle L_z\rangle = 0$: momentum sudut orbital "dipadamkan" (*quenched*), dan kemagnetan kompleks logam transisi deret pertama hampir seluruhnya berasal dari spin (Bab 14).
:::

::: {.contoh}
**Contoh 7.28 · Isi $m$ orbital d riil**

Tentukan komponen $m$ dari $d_{xy}$, $d_{x^2-y^2}$, $d_{xz}$, dan $d_{z^2}$, dan hasil yang mungkin bila $L_z$ diukur pada elektron di $d_{xy}$.

**Penyelesaian.** $d_{x^2-y^2} = (Y_2^2 + Y_2^{-2})/\sqrt2$ dan $d_{xy} = -i(Y_2^2 - Y_2^{-2})/\sqrt2$: keduanya hanya memuat $m = \pm2$. $d_{xz}$ dan $d_{yz}$ memuat $m = \pm1$. $d_{z^2} = Y_2^0$. Pengukuran $L_z$ pada $d_{xy}$ memberi $+2\hbar$ atau $-2\hbar$, masing-masing dengan peluang ½.

**Memahami hasil.** Orbital-orbital yang memuat $|m|$ yang sama hanya berbeda orientasi terhadap sumbu $z$: $d_{xy}$ adalah $d_{x^2-y^2}$ yang diputar 45°. Itulah sebabnya, dalam medan ligan oktahedral, $d_{xy}$, $d_{xz}$, dan $d_{yz}$ tetap setara satu sama lain, tetapi $d_{x^2-y^2}$ setara dengan $d_{z^2}$, bukan dengan $d_{xy}$ (Bab 14).
:::

::: {.contoh}
**Contoh 7.29 · Membangun $p_x$ dan $p_y$ dari orbital kompleks**

Bagian sudut orbital $p$ kompleks adalah $Y_1^{\pm1} = \mp\sqrt{3/8\pi}\,\sin\theta\,e^{\pm i\phi}$. Tunjukkan bahwa kombinasi $p_x = (Y_1^{-1} - Y_1^{1})/\sqrt2$ dan $p_y = i(Y_1^{-1} + Y_1^{1})/\sqrt2$ riil, dan tentukan arahnya.

**Penyelesaian.** Dengan $e^{\pm i\phi} = \cos\phi \pm i\sin\phi$:

$$
Y_1^{-1} - Y_1^{1} = \sqrt{\tfrac{3}{8\pi}}\sin\theta\,(e^{-i\phi} + e^{i\phi}) = 2\sqrt{\tfrac{3}{8\pi}}\sin\theta\cos\phi ,
$$

sehingga $p_x = \sqrt{3/4\pi}\,\sin\theta\cos\phi = \sqrt{3/4\pi}\,(x/r)$. Dengan cara yang sama $p_y = \sqrt{3/4\pi}\,(y/r)$. Keduanya riil, berarah sepanjang sumbu $x$ dan $y$, dan tetap ternormalkan karena $Y_1^{\pm1}$ ortonormal.

**Memahami hasil.** $p_x$ dan $p_y$ bukan fungsi eigen $\hat L_z$; masing-masing adalah campuran setara $m = +1$ dan $m = -1$. Tetapi karena keduanya mempunyai energi dan $\ell$ yang sama, campuran apa pun tetap merupakan keadaan stasioner. Kimiawan memakai orbital riil karena arahnya jelas dan cocok untuk menggambarkan ikatan; fisikawan memakai orbital kompleks bila ada medan magnet yang memilih sumbu $z$.
:::

::: {.kuis}
**Kuis cepat 7.7**

Apakah $2\text{p}_x$ fungsi eigen $\hat L_z$? Apakah fungsi eigen $\hat L_x$? Mengapa orbital riil berenergi sama dengan orbital kompleks dalam atom hidrogen bebas?
:::

## 7.8 Bentuk orbital s, p, d, f

### Membaca bentuk orbital

Bentuk orbital ditentukan oleh dua faktor: bagian sudut (harmonik bola riil) yang menentukan lobus dan bidang atau kerucut simpul, dan bagian radial yang menentukan ukuran dan kulit-kulit konsentris. Gambar 7.3 memperlihatkan penampang beberapa orbital pada bidang $xz$, dengan tanda fungsi gelombang (biru positif, jingga negatif) dan simpul (garis putus-putus).

![Gambar 7.3 Penampang fungsi gelombang hidrogen pada bidang $xz$. Biru: $\psi > 0$; jingga: $\psi < 0$; garis putus-putus: simpul. Orbital 2s dan 3p mempunyai simpul radial (lingkaran); 3d$_{z^2}$ mempunyai dua kerucut simpul (pada 54,7°); 4f$_{z^3}$ mempunyai dua kerucut dan satu bidang simpul.](fig/c_orbital.png){width=95%}

Beberapa ciri yang perlu diingat:

* **Orbital s** bersimetri bola, dengan $n - 1$ simpul radial. Tanda fungsi gelombang berganti di setiap simpul.
* **Orbital p** mempunyai satu bidang simpul melalui inti dan dua lobus bertanda berlawanan. Orbital 3p mempunyai tambahan satu simpul radial, sehingga setiap lobus terbagi dua bagian bertanda berlawanan.
* **Orbital d** mempunyai dua permukaan simpul sudut. Empat di antaranya ($d_{xy}$, $d_{xz}$, $d_{yz}$, $d_{x^2-y^2}$) berbentuk daun semanggi dengan dua bidang simpul; $d_{z^2}$ mempunyai dua kerucut simpul dan "cincin" bertanda negatif di bidang $xy$.
* **Orbital f** mempunyai tiga permukaan simpul sudut. Himpunan yang paling sering dipakai (himpunan umum) adalah $f_{z^3}$, $f_{xz^2}$, $f_{yz^2}$, $f_{xyz}$, $f_{z(x^2-y^2)}$, $f_{x(x^2-3y^2)}$, dan $f_{y(3x^2-y^2)}$; himpunan kubik dipakai untuk kompleks oktahedral.

### Tanda dan tumpang tindih

Tanda fungsi gelombang tidak dapat diukur langsung (rapat peluang adalah $|\psi|^2$), tetapi menjadi penting ketika dua orbital digabungkan. Integral tumpang tindih $\int\psi_A\psi_B\,d\tau$ dapat positif, negatif, atau nol tergantung tanda lobus yang bertemu. Pada ikatan kimia (Bab 11), orbital yang tumpang tindih positif membentuk orbital ikatan, dan simetri menentukan pasangan mana yang tumpang tindihnya nol.

::: {.contoh}
**Contoh 7.30 · Simpul orbital 4f$_{z^3}$**

Bagian sudut $f_{z^3}$ sebanding dengan $5\cos^3\theta - 3\cos\theta$. Tentukan semua simpul sudutnya, dan banyaknya simpul radial 4f.

**Penyelesaian.** $\cos\theta(5\cos^2\theta - 3) = 0$: $\cos\theta = 0$ (bidang $xy$) dan $\cos\theta = \pm\sqrt{3/5} = \pm0{,}775$ ($\theta = 39{,}2°$ dan $140{,}8°$, dua kerucut). Simpul radial $n - \ell - 1 = 0$.

**Memahami hasil.** Tiga simpul sudut, sesuai $\ell = 3$. Orbital 4f tidak mempunyai simpul radial dan sangat "kompak": dalam lantanida, elektron 4f terkubur di dalam kulit 5s²5p⁶ dan hampir tidak ikut berikatan. Itulah sebabnya sifat kimia lantanida sangat mirip satu sama lain, dan warna ion-ionnya (transisi f–f) tajam serta hampir tidak dipengaruhi ligan.
:::

::: {.contoh}
**Contoh 7.31 · Mengapa hanya lima orbital d?**

Bentuk $d_{z^2-x^2}$ dan $d_{z^2-y^2}$ tampak setara dengan $d_{x^2-y^2}$. Mengapa tidak ada enam orbital d?

**Penyelesaian.** Fungsi $z^2 - x^2$, $z^2 - y^2$, dan $x^2 - y^2$ tidak bebas linear: $(z^2 - y^2) - (z^2 - x^2) = x^2 - y^2$. Hanya dua di antaranya yang bebas. Kombinasi $(z^2 - x^2) + (z^2 - y^2) = 2z^2 - x^2 - y^2 = 3z^2 - r^2$, yaitu $d_{z^2}$. Jadi ruang yang direntang $\{z^2 - x^2, z^2 - y^2\}$ sama dengan $\{3z^2 - r^2, x^2 - y^2\}$.

**Memahami hasil.** Polinom kuadrat dalam $x$, $y$, $z$ ada enam ($x^2$, $y^2$, $z^2$, $xy$, $xz$, $yz$), tetapi kombinasi $x^2 + y^2 + z^2 = r^2$ bersimetri bola, yaitu "orbital s" yang tersembunyi. Sisanya lima, sesuai $2\ell + 1$. Dalam basis Gauss Kartesius, enam fungsi d dipakai, dan salah satunya sebenarnya fungsi s; beberapa program memakai lima fungsi d "sferis" untuk menghindarinya (Bab 17).
:::

::: {.contoh}
**Contoh 7.32 · Tumpang tindih dan simetri**

Atom H dengan orbital 1s terletak pada sumbu $z$ dari atom lain. Manakah orbital atom kedua yang tumpang tindihnya dengan 1s pasti nol: $2s$, $2p_z$, $2p_x$, $3d_{z^2}$, $3d_{xz}$?

**Penyelesaian.** 1s bersimetri terhadap rotasi di sekeliling sumbu $z$ dan terhadap pencerminan di bidang $xz$ dan $yz$. Orbital yang berubah tanda pada pencerminan $x \to -x$ ($2p_x$, $3d_{xz}$) memberi tumpang tindih nol: sumbangan lobus positif dan negatif saling meniadakan. Tumpang tindih dengan $2s$, $2p_z$, dan $3d_{z^2}$ dapat tidak nol.

**Memahami hasil.** Orbital-orbital yang simetris terhadap sumbu ikatan membentuk ikatan σ; yang mempunyai satu bidang simpul memuat sumbu ikatan ($p_x$, $p_y$, $d_{xz}$, $d_{yz}$) membentuk ikatan π, dan hanya dengan orbital yang sejenis. Aturan pemilihan pasangan ini, yang di sini dibaca dari gambar, akan dirumuskan dengan teori grup di Bab 10.
:::

::: {.contoh}
**Contoh 7.33 · Kerucut simpul orbital $d_{z^2}$**

Bagian sudut orbital $3d_{z^2}$ sebanding dengan $3\cos^2\theta - 1$. Pada sudut berapa terdapat bidang simpul (berbentuk kerucut)? Mengapa bentuk ini penting dalam senyawa kompleks oktahedral?

**Penyelesaian.** Simpul terjadi bila $3\cos^2\theta - 1 = 0$, yaitu $\cos\theta = \pm1/\sqrt3$, $\theta = 54{,}74°$ dan $125{,}26°$. Dua kerucut simpul memisahkan dua cuping di sumbu $z$ (bertanda positif) dari "cincin" di bidang $xy$ (bertanda negatif).

**Memahami hasil.** Sudut 54,74° adalah separuh sudut tetrahedral (109,47°), dan disebut juga "sudut ajaib" dalam NMR padatan, karena kopling dipol antarinti sebanding dengan faktor $3\cos^2\theta - 1$ yang sama. Dalam kompleks oktahedral, cuping $d_{z^2}$ mengarah tepat ke dua ligan di sumbu $z$, sehingga orbital ini (bersama $d_{x^2 - y^2}$) naik energinya oleh tolakan ligan (Bab 14).
:::

::: {.kuis}
**Kuis cepat 7.8**

Berapa banyak simpul total pada orbital 5f? Berapa banyak kerucut simpul pada $3d_{z^2}$, dan pada sudut berapa?
:::

## 7.9 Nilai harap dan teorema virial

### Rumus-rumus umum

Dengan fungsi radial dan integral (2.8), nilai harap pangkat $r$ dapat dihitung untuk setiap orbital. Hasilnya (satuan atom):

$$
\langle r\rangle = \frac{3n^2 - \ell(\ell + 1)}{2Z}, \quad \langle r^2\rangle = \frac{n^2[5n^2 + 1 - 3\ell(\ell + 1)]}{2Z^2}, \quad \left\langle\frac1r\right\rangle = \frac{Z}{n^2}, \quad \left\langle\frac{1}{r^2}\right\rangle = \frac{Z^2}{n^3(\ell + \tfrac12)} . \qquad \text{(7.17)}
$$

Ukuran atom tumbuh seperti $n^2$ dan menyusut seperti $1/Z$. Untuk $n$ yang sama, orbital dengan $\ell$ besar sedikit lebih kecil rata-ratanya, meskipun kurang menembus ke dekat inti.

### Teorema virial

Untuk potensial Coulomb, $\langle V\rangle = -Z\langle 1/r\rangle = -Z^2/n^2 = 2E_n$. Karena $E = \langle T\rangle + \langle V\rangle$:

$$
\langle V\rangle = 2E_n, \qquad \langle T\rangle = -E_n . \qquad \text{(7.18)}
$$

Ini teorema virial untuk potensial $V \propto r^{-1}$ ($2\langle T\rangle = -\langle V\rangle$; Contoh 4.20 dan 5.17). Ia berlaku untuk setiap keadaan stasioner atom hidrogen, dan, dalam bentuk yang sama, untuk setiap atom dan molekul pada geometri setimbang, karena semua interaksi di dalamnya bersifat Coulomb. Dalam pembentukan ikatan kimia, energi total turun; menurut teorema virial, energi kinetik elektron **naik** dan energi potensial turun dua kali lebih banyak (Bab 11).

::: {.contoh}
**Contoh 7.34 · Ukuran orbital**

Hitung $\langle r\rangle$ (bohr dan pm) untuk 1s, 2s, 2p, 3d, dan 4f hidrogen.

**Penyelesaian.** Dengan (7.17): 1s $1{,}5$ bohr (79,4 pm); 2s 6 (318 pm); 2p 5 (265 pm); 3d $\tfrac12(27 - 6) = 10{,}5$ (556 pm); 4f $\tfrac12(48 - 12) = 18$ (953 pm).

**Memahami hasil.** Orbital tereksitasi hidrogen sangat besar: atom H pada $n = 3$ hampir tujuh kali lebih besar daripada pada $n = 1$. Dalam atom berelektron banyak, muatan inti efektif yang besar memampatkan orbital dalam; misalnya orbital 3d tembaga hanya sekitar 50 pm, sehingga tidak dapat ditaksir dengan rumus hidrogen tanpa penyaringan (Bab 9).
:::

::: {.contoh}
**Contoh 7.35 · Energi kinetik dan potensial 2p**

Untuk elektron 2p hidrogen, hitung $\langle 1/r\rangle$, $\langle V\rangle$, dan $\langle T\rangle$ langsung dari $R_{21}$, lalu periksa (7.18).

**Penyelesaian.** $\langle 1/r\rangle = \tfrac1{24}\int_0^\infty r^3e^{-r}dr = \tfrac{3!}{24} = \tfrac14$. $\langle V\rangle = -\tfrac14$ hartree. $E_2 = -\tfrac18$, sehingga $\langle T\rangle = E - \langle V\rangle = \tfrac18$. Memang $\langle V\rangle = 2E$ dan $\langle T\rangle = -E$.

**Memahami hasil.** Nilai $\langle 1/r\rangle = Z/n^2$ sama untuk 2s dan 2p, meskipun $\langle r\rangle$ berbeda (6 dan 5 bohr). Rata-rata $1/r$ peka terhadap daerah dekat inti; rata-rata $r$ peka terhadap ekor jauh. Pada 2s, puncak dalam (menaikkan $\langle 1/r\rangle$) diimbangi tepat oleh ekor yang lebih panjang (menurunkannya), sehingga energinya sama dengan 2p.
:::

::: {.contoh}
**Contoh 7.36 · Lebar awan 1s**

Hitung $\Delta r = \sqrt{\langle r^2\rangle - \langle r\rangle^2}$ untuk 1s, dan suseptibilitas diamagnetik molar atom H, $\chi_m = -\mu_0N_Ae^2\langle r^2\rangle/6m_e$.

**Penyelesaian.** $\langle r^2\rangle = \tfrac12(5 + 1) = 3$, $\langle r\rangle^2 = 2{,}25$; $\Delta r = 0{,}866$ bohr. $\chi_m = -\mu_0N_Ae^2(3a_0^2)/6m_e = -2{,}99 \times 10^{-11}$ m³/mol.

**Memahami hasil.** Ketidakpastian jarak elektron 1s hampir sebesar jaraknya sendiri. Diamagnetisme sebanding dengan $\langle r^2\rangle$, sehingga didominasi orbital terluar; nilai terukur untuk He ($-2{,}4 \times 10^{-11}$ m³/mol) berorde sama. Pergeseran kimia NMR (Bab 16) bersumber dari arus diamagnetik semacam ini di sekitar inti.
:::

::: {.contoh}
**Contoh 7.37 · Kecepatan elektron dan kimia relativistik**

Dari $\langle T\rangle = Z^2/2$ untuk 1s, kecepatan rms elektron 1s adalah $v = Z$ dalam satuan atom (satuan kecepatan $\alpha c$). Hitung $v/c$ untuk H, Cs ($Z = 55$), dan Au ($Z = 79$), dan faktor kenaikan massa relativistik $\gamma$.

**Penyelesaian.** $v/c = Z/137{,}04$: H 0,0073; Cs 0,40; Au 0,58. $\gamma = 1/\sqrt{1 - v^2/c^2}$: H 1,00003; Cs 1,09; Au 1,22.

**Memahami hasil.** Jari-jari orbital berbanding terbalik dengan massa, sehingga orbital 1s emas menyusut sekitar 18%. Orbital s yang lebih luar, yang harus ortogonal terhadapnya, ikut menyusut dan turun energinya, sedangkan orbital d mengembang. Akibatnya celah 5d–6s emas mengecil sampai serapannya masuk daerah biru: emas berwarna kuning karena relativitas, sedangkan perak (dengan celah yang lebih besar) berwarna putih. Raksa cair pada suhu kamar adalah akibat lain dari efek yang sama (Bab 9).
:::

::: {.contoh}
**Contoh 7.38 · Energi kinetik dan potensial He⁺**

Untuk He⁺ pada keadaan dasar, hitung $\langle T\rangle$, $\langle V\rangle$, dan $\langle r\rangle$ dengan rumus penskalaan, lalu bandingkan dengan hidrogen.

**Penyelesaian.** $E_1 = -Z^2/2 = -2$ hartree. Menurut (7.18): $\langle T\rangle = 2$ hartree $= 54{,}4$ eV dan $\langle V\rangle = -4$ hartree $= -108{,}8$ eV. $\langle r\rangle = 3/(2Z) = 0{,}75$ bohr.

**Memahami hasil.** Dibandingkan hidrogen, energi kinetik dan potensial keduanya naik empat kali, sedangkan ukuran mengecil dua kali. Elektron yang lebih dekat ke inti bergerak lebih cepat (asas ketidakpastian) dan ditarik lebih kuat; teorema virial menjamin keduanya seimbang dalam perbandingan $1 : -2$ untuk setiap $Z$.
:::

::: {.contoh}
**Contoh 7.39 · Ukuran dan sebaran orbital kulit $n = 2$ dan $n = 3$**

Dengan $\langle r\rangle = \tfrac12[3n^2 - \ell(\ell + 1)]$ dan $\langle r^2\rangle = \tfrac12n^2[5n^2 + 1 - 3\ell(\ell + 1)]$ (satuan bohr), hitung $\langle r\rangle$ dan sebaran $\Delta r = \sqrt{\langle r^2\rangle - \langle r\rangle^2}$ untuk 2s, 2p, 3s, 3p, dan 3d.

**Penyelesaian.**

| Orbital | $\langle r\rangle$ | $\langle r^2\rangle$ | $\Delta r$ |
|---|---|---|---|
| 2s | 6,0 | 42 | 2,45 |
| 2p | 5,0 | 30 | 2,24 |
| 3s | 13,5 | 207 | 4,97 |
| 3p | 12,5 | 180 | 4,87 |
| 3d | 10,5 | 126 | 3,97 |

**Memahami hasil.** Dalam satu kulit, orbital dengan $\ell$ lebih besar rata-rata **lebih dekat** ke inti dan lebih sempit sebarannya, walaupun energinya sama dalam hidrogen. Orbital s menyebar paling luas karena punya simpul-simpul radial dan cuping kecil di dekat inti. Dalam atom berelektron banyak, cuping dalam itulah yang menembus kulit dalam (subbab 7.6) dan menurunkan energi orbital s di bawah p dan d.
:::

::: {.kuis}
**Kuis cepat 7.9**

Berapa $\langle T\rangle$ dan $\langle V\rangle$ (eV) untuk elektron 3d hidrogen? Mengapa $\langle 1/r\rangle$ sama untuk 3s, 3p, dan 3d?
:::
