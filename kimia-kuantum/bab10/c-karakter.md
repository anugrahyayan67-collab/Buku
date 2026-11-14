## 10.5 Karakter dan tabel karakter

### Teras sebagai sidik jari

Matriks representasi bergantung pada pilihan basis: basis $(s_1, s_2)$ dan basis $(s_+, s_-)$ di subbab 10.4 memberikan matriks yang tampak berbeda untuk representasi yang sama. Kita memerlukan besaran yang tidak berubah oleh perubahan basis. Besaran itu adalah **karakter**, yaitu teras matriks:

$$
\chi(R) = \mathrm{Tr}\,\mathbf D(R) = \sum_k D_{kk}(R) . \qquad \text{(10.7)}
$$

Dua sifat teras membuat karakter sangat praktis. Pertama, karakter **tidak berubah oleh transformasi keserupaan**, karena teras hasil kali matriks tidak berubah bila urutannya diputar secara siklis: $\mathrm{Tr}(\mathbf U^{-1}\mathbf D\mathbf U) = \mathrm{Tr}(\mathbf D\mathbf U\mathbf U^{-1}) = \mathrm{Tr}\,\mathbf D$. Representasi yang hanya berbeda pilihan basis mempunyai karakter yang sama. Kedua, **operasi sekelas mempunyai karakter yang sama**: bila $B = X^{-1}AX$, maka $\mathbf D(B) = \mathbf D(X)^{-1}\mathbf D(A)\mathbf D(X)$, dan terasnya sama dengan teras $\mathbf D(A)$. Jadi untuk mencirikan representasi cukup satu bilangan per kelas, bukan satu matriks per operasi.

Contohnya, basis $(s_1, s_2)$ hidrogen H₂O memberikan karakter $\chi(E) = 2$, $\chi(C_2) = 0$, $\chi(\sigma_v) = 0$, $\chi(\sigma_v') = 2$. Ada cara cepat untuk mendapatkan angka-angka ini tanpa menulis matriks: dalam matriks permutasi, unsur diagonal bernilai 1 hanya untuk basis yang tidak berpindah, sehingga **karakter = banyaknya fungsi basis yang tetap di tempatnya** (dengan tanda $-1$ bila fungsi itu berubah tanda). $C_2$ dan $\sigma_v$ memindahkan kedua H, sehingga karakternya nol.

### Membaca tabel karakter

Untuk setiap grup titik, semua irrep dan karakternya telah disusun dalam **tabel karakter**. Berikut tabel untuk $C_{2v}$ dan $C_{3v}$:

| $C_{2v}$ | $E$ | $C_2$ | $\sigma_v(xz)$ | $\sigma_v'(yz)$ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|---|
| $A_1$ | 1 | 1 | 1 | 1 | $z$ | $x^2$, $y^2$, $z^2$ |
| $A_2$ | 1 | 1 | $-1$ | $-1$ | $R_z$ | $xy$ |
| $B_1$ | 1 | $-1$ | 1 | $-1$ | $x$, $R_y$ | $xz$ |
| $B_2$ | 1 | $-1$ | $-1$ | 1 | $y$, $R_x$ | $yz$ |

| $C_{3v}$ | $E$ | $2C_3$ | $3\sigma_v$ | Linear, rotasi | Kuadrat |
|---|---|---|---|---|---|
| $A_1$ | 1 | 1 | 1 | $z$ | $x^2 + y^2$, $z^2$ |
| $A_2$ | 1 | 1 | $-1$ | $R_z$ | |
| $E$ | 2 | $-1$ | 0 | $(x, y)$, $(R_x, R_y)$ | $(x^2 - y^2, xy)$, $(xz, yz)$ |

Tabel karakter terdiri atas empat bagian:

1. **Baris judul**: nama grup dan kelas-kelasnya, dengan banyak anggota kelas di depan lambang operasi ($2C_3$ berarti dua operasi $C_3$ dan $C_3^2$).
2. **Lambang Mulliken** setiap irrep di kolom pertama.
3. **Karakter** setiap irrep untuk setiap kelas. Kolom $E$ selalu berisi dimensi irrep, karena $\mathbf D(E)$ adalah matriks satuan.
4. **Fungsi basis**: kolom linear berisi $x$, $y$, $z$ (yang bertransformasi seperti translasi dan seperti komponen momen dipol) dan $R_x$, $R_y$, $R_z$ (rotasi terhadap sumbu itu); kolom kuadrat berisi hasil kali dua koordinat, yang bertransformasi seperti orbital d dan seperti komponen polarisabilitas. Fungsi dalam kurung, seperti $(x, y)$, bersama-sama menjadi basis satu irrep berdimensi dua.

Kolom fungsi adalah bagian yang paling sering dipakai. Untuk mengetahui irrep sebuah orbital atom pusat, cukup cari koordinatnya: dalam H₂O, $p_x$ adalah $b_1$, $p_y$ adalah $b_2$, $p_z$ dan $s$ adalah $a_1$, dan $d_{xy}$ adalah $a_2$.

### Lambang Mulliken

Nama irrep mengikuti aturan yang diusulkan Robert Mulliken:

- **Dimensi**: $A$ atau $B$ untuk dimensi satu, $E$ untuk dua, $T$ (kadang $F$) untuk tiga, $G$ untuk empat, $H$ untuk lima. (Jangan keliru antara irrep $E$ dan operasi identitas $E$; konteks membedakannya.)
- **$A$ atau $B$**: $A$ simetris terhadap putaran $C_n$ sumbu utama (karakter $+1$), $B$ antisimetris (karakter $-1$).
- **Indeks 1 dan 2**: simetris (1) atau antisimetris (2) terhadap $C_2$ yang tegak lurus sumbu utama, atau, bila tidak ada, terhadap $\sigma_v$.
- **Indeks $g$ dan $u$** (dari bahasa Jerman *gerade* dan *ungerade*): simetris atau antisimetris terhadap inversi, persis seperti label paritas di subbab 4.11.
- **Aksen $'$ dan $''$**: simetris atau antisimetris terhadap $\sigma_h$, untuk grup tanpa pusat inversi seperti $D_{3h}$.

Menurut kesepakatan, **huruf besar** dipakai untuk keadaan molekul dan mode getaran ($A_1$, $^1B_{2u}$), sedangkan **huruf kecil** untuk orbital ($a_1$, $t_{2g}$, $e_{1g}$). Orbital dengan label sama diberi nomor urut menurut energi, dari bawah: $1a_1$, $2a_1$, $3a_1$.

### Sifat-sifat representasi tak tereduksi

Tabel karakter tidak disusun dengan coba-coba. Struktur matematikanya dikendalikan oleh beberapa aturan yang dapat dipakai untuk memeriksa, bahkan melengkapi, sebuah tabel:

1. **Banyaknya irrep sama dengan banyaknya kelas.** Tabel karakter selalu persegi.
2. **Jumlah kuadrat dimensi sama dengan orde grup:**

$$
\sum_i d_i^2 = h . \qquad \text{(10.8)}
$$

3. **Baris-baris karakter ortogonal.** Bila $g_c$ adalah banyak anggota kelas $c$,

$$
\sum_{c} g_c\,\chi_i(c)^*\chi_j(c) = h\,\delta_{ij} . \qquad \text{(10.9)}
$$

4. **Kolom-kolom karakter juga ortogonal**: $\sum_i \chi_i(c)^*\chi_i(c') = (h/g_c)\,\delta_{cc'}$.
5. Setiap grup mempunyai irrep **simetri total** yang semua karakternya 1.

Aturan (10.9) mengatakan bahwa bila kita memandang deretan karakter sebuah irrep sebagai vektor dengan $h$ komponen (satu komponen per operasi), vektor-vektor untuk irrep yang berbeda saling tegak lurus, dan panjang kuadrat setiap vektor adalah $h$. Inilah kunci rumus reduksi di subbab 10.6.

::: {.dalam}
**Lebih dalam · Teorema ortogonalitas besar**

Semua aturan di atas berasal dari satu teorema tentang unsur-unsur matriks irrep. Untuk dua irrep $\Gamma^{(i)}$ dan $\Gamma^{(j)}$ yang dipilih uniter,

$$
\sum_R D^{(i)}_{mn}(R)^*\,D^{(j)}_{m'n'}(R) = \frac{h}{d_i}\,\delta_{ij}\,\delta_{mm'}\,\delta_{nn'} .
$$

Bacalah sebagai berikut. Untuk setiap irrep $i$ dan setiap posisi $(m, n)$ dalam matriksnya, susun vektor berkomponen $h$ dari unsur $D^{(i)}_{mn}(R)$ untuk semua $R$. Teorema itu menyatakan bahwa semua vektor ini saling ortogonal. Banyaknya vektor adalah $\sum_i d_i^2$, dan dalam ruang berdimensi $h$ paling banyak ada $h$ vektor yang saling ortogonal; teorema yang lebih lengkap menunjukkan bahwa jumlahnya tepat $h$, sehingga diperoleh (10.8).

Ambil $m = n$ dan $m' = n'$, lalu jumlahkan atas $m$ dan $m'$. Ruas kiri menjadi $\sum_R \chi_i(R)^*\chi_j(R)$, sedangkan ruas kanan menjadi $(h/d_i)\delta_{ij}\sum_m\delta_{mm} = (h/d_i)\delta_{ij}d_i = h\delta_{ij}$. Karena operasi sekelas berkarakter sama, penjumlahan atas $R$ dapat dikelompokkan per kelas, dan diperoleh (10.9). Bukti teorema itu sendiri memakai dua lema Schur dan dapat dibaca di buku teori grup dalam Bacaan lanjut.
:::

Tabel karakter grup-grup lain yang sering dipakai dalam bab ini adalah sebagai berikut (kolom fungsi hanya memuat yang penting).

| $D_{3h}$ | $E$ | $2C_3$ | $3C_2$ | $\sigma_h$ | $2S_3$ | $3\sigma_v$ | Fungsi |
|---|---|---|---|---|---|---|---|
| $A_1'$ | 1 | 1 | 1 | 1 | 1 | 1 | $x^2 + y^2$, $z^2$ |
| $A_2'$ | 1 | 1 | $-1$ | 1 | 1 | $-1$ | $R_z$ |
| $E'$ | 2 | $-1$ | 0 | 2 | $-1$ | 0 | $(x, y)$; $(x^2 - y^2, xy)$ |
| $A_1''$ | 1 | 1 | 1 | $-1$ | $-1$ | $-1$ | |
| $A_2''$ | 1 | 1 | $-1$ | $-1$ | $-1$ | 1 | $z$ |
| $E''$ | 2 | $-1$ | 0 | $-2$ | 1 | 0 | $(R_x, R_y)$; $(xz, yz)$ |

| $T_d$ | $E$ | $8C_3$ | $3C_2$ | $6S_4$ | $6\sigma_d$ | Fungsi |
|---|---|---|---|---|---|---|
| $A_1$ | 1 | 1 | 1 | 1 | 1 | $x^2 + y^2 + z^2$ |
| $A_2$ | 1 | 1 | 1 | $-1$ | $-1$ | |
| $E$ | 2 | $-1$ | 2 | 0 | 0 | $(2z^2 - x^2 - y^2,\ x^2 - y^2)$ |
| $T_1$ | 3 | 0 | $-1$ | 1 | $-1$ | $(R_x, R_y, R_z)$ |
| $T_2$ | 3 | 0 | $-1$ | $-1$ | 1 | $(x, y, z)$; $(xy, xz, yz)$ |

| $D_{2h}$ | $E$ | $C_2(z)$ | $C_2(y)$ | $C_2(x)$ | $i$ | $\sigma(xy)$ | $\sigma(xz)$ | $\sigma(yz)$ | Fungsi |
|---|---|---|---|---|---|---|---|---|---|
| $A_g$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | $x^2$, $y^2$, $z^2$ |
| $B_{1g}$ | 1 | 1 | $-1$ | $-1$ | 1 | 1 | $-1$ | $-1$ | $R_z$; $xy$ |
| $B_{2g}$ | 1 | $-1$ | 1 | $-1$ | 1 | $-1$ | 1 | $-1$ | $R_y$; $xz$ |
| $B_{3g}$ | 1 | $-1$ | $-1$ | 1 | 1 | $-1$ | $-1$ | 1 | $R_x$; $yz$ |
| $A_u$ | 1 | 1 | 1 | 1 | $-1$ | $-1$ | $-1$ | $-1$ | |
| $B_{1u}$ | 1 | 1 | $-1$ | $-1$ | $-1$ | $-1$ | 1 | 1 | $z$ |
| $B_{2u}$ | 1 | $-1$ | 1 | $-1$ | $-1$ | 1 | $-1$ | 1 | $y$ |
| $B_{3u}$ | 1 | $-1$ | $-1$ | 1 | $-1$ | 1 | 1 | $-1$ | $x$ |

| $O_h$ | $E$ | $8C_3$ | $6C_2$ | $6C_4$ | $3C_2$ | $i$ | $6S_4$ | $8S_6$ | $3\sigma_h$ | $6\sigma_d$ | Fungsi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $A_{1g}$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | $x^2 + y^2 + z^2$ |
| $A_{2g}$ | 1 | 1 | $-1$ | $-1$ | 1 | 1 | $-1$ | 1 | 1 | $-1$ | |
| $E_g$ | 2 | $-1$ | 0 | 0 | 2 | 2 | 0 | $-1$ | 2 | 0 | $(2z^2 - x^2 - y^2,\ x^2 - y^2)$ |
| $T_{1g}$ | 3 | 0 | $-1$ | 1 | $-1$ | 3 | 1 | 0 | $-1$ | $-1$ | $(R_x, R_y, R_z)$ |
| $T_{2g}$ | 3 | 0 | 1 | $-1$ | $-1$ | 3 | $-1$ | 0 | $-1$ | 1 | $(xy, xz, yz)$ |
| $A_{1u}$ | 1 | 1 | 1 | 1 | 1 | $-1$ | $-1$ | $-1$ | $-1$ | $-1$ | |
| $A_{2u}$ | 1 | 1 | $-1$ | $-1$ | 1 | $-1$ | 1 | $-1$ | $-1$ | 1 | |
| $E_u$ | 2 | $-1$ | 0 | 0 | 2 | $-2$ | 0 | 1 | $-2$ | 0 | |
| $T_{1u}$ | 3 | 0 | $-1$ | 1 | $-1$ | $-3$ | $-1$ | 0 | 1 | 1 | $(x, y, z)$ |
| $T_{2u}$ | 3 | 0 | 1 | $-1$ | $-1$ | $-3$ | 1 | 0 | 1 | $-1$ | |

Pada $O_h$, kolom $6C_2$ berisi putaran 180° terhadap sumbu yang membagi dua sudut antara dua sumbu Kartesius, sedangkan $3C_2$ adalah $C_4^2$ terhadap sumbu Kartesius.

::: {.contoh}
**Contoh 10.20 · Dimensi irrep dari orde grup**

Gunakan (10.8) untuk menentukan dimensi irrep $C_{3v}$ (tiga kelas, $h = 6$) dan $T_d$ (lima kelas, $h = 24$) tanpa melihat tabel.

**Penyelesaian.** $C_{3v}$: tiga bilangan bulat positif yang kuadratnya berjumlah 6, salah satunya 1 (irrep simetri total). Satu-satunya kemungkinan $1 + 1 + 4 = 6$: dimensi 1, 1, dan 2. $T_d$: lima bilangan yang kuadratnya berjumlah 24, salah satunya 1. Coba $1 + 1 + 4 + 9 + 9 = 24$: dimensi 1, 1, 2, 3, 3. (Kombinasi lain, seperti $1 + 1 + 1 + 1 + 20$, gagal karena 20 bukan kuadrat; $1 + 4 + 9 + 9 + 1$ adalah susunan yang sama.)

**Memahami hasil.** Dari orde dan banyak kelas saja kita tahu bahwa molekul tetrahedral dapat mempunyai tingkat energi berdegenerasi dua dan tiga, tetapi tidak empat. Untuk $O_h$, $2(1 + 1 + 4 + 9 + 9) = 48$, juga dengan degenerasi maksimum tiga. Degenerasi empat dan lima hanya dimungkinkan oleh grup ikosahedral ($G$ dan $H$ di $I_h$), dan itulah yang dimanfaatkan C₆₀ (Contoh 10.24).
:::

::: {.contoh}
**Contoh 10.21 · Memeriksa ortogonalitas**

Periksa dengan (10.9) bahwa baris $E$ dan $A_2$ dalam $C_{3v}$ ortogonal, bahwa baris $E$ ternormalisasi, dan bahwa baris $T_1$ dan $T_2$ dalam $T_d$ ortogonal.

**Penyelesaian.** $C_{3v}$, $E$ dengan $A_2$: $1(2)(1) + 2(-1)(1) + 3(0)(-1) = 2 - 2 + 0 = 0$. $E$ dengan dirinya: $1(4) + 2(1) + 3(0) = 6 = h$. $T_d$, $T_1$ dengan $T_2$: $1(3)(3) + 8(0)(0) + 3(-1)(-1) + 6(1)(-1) + 6(-1)(1) = 9 + 3 - 6 - 6 = 0$.

**Memahami hasil.** Jangan lupa faktor $g_c$; tanpanya hasil penjumlahan salah. Pemeriksaan ortogonalitas adalah cara cepat menemukan salah ketik dalam tabel karakter yang disalin dengan tangan, dan cara untuk melengkapi tabel yang barisnya hilang satu.
:::

::: {.contoh}
**Contoh 10.22 · Orbital d dalam medan oktahedral dan tetrahedral**

Dari tabel $O_h$ dan $T_d$, tentukan irrep kelima orbital d atom logam di pusat kompleks oktahedral dan tetrahedral.

**Penyelesaian.** Orbital d sebanding dengan fungsi kuadrat: $d_{xy} \propto xy$, $d_{xz} \propto xz$, $d_{yz} \propto yz$, $d_{x^2-y^2} \propto x^2 - y^2$, dan $d_{z^2} \propto 2z^2 - x^2 - y^2$. Pada $O_h$, kolom fungsi menempatkan $(2z^2 - x^2 - y^2,\ x^2 - y^2)$ di $E_g$ dan $(xy, xz, yz)$ di $T_{2g}$. Pada $T_d$, pasangan yang sama berada di $E$ dan trio yang sama di $T_2$.

**Memahami hasil.** Dalam kompleks oktahedral, kelima orbital d terbagi menjadi dua kelompok berdegenerasi, $e_g$ (dua) dan $t_{2g}$ (tiga). Simetri tidak mengatakan mana yang lebih tinggi; itu ditentukan oleh interaksi dengan ligan (orbital $e_g$ mengarah langsung ke ligan sehingga naik, Bab 14). Tetapi simetri menjamin bahwa tidak ada pembelahan lebih lanjut selama kompleks benar-benar oktahedral. Bila kompleks memanjang sepanjang $z$ (simetri turun ke $D_{4h}$), $e_g$ terpecah menjadi $a_{1g}$ ($z^2$) dan $b_{1g}$ ($x^2 - y^2$), sedangkan $t_{2g}$ menjadi $b_{2g}$ ($xy$) dan $e_g$ ($xz$, $yz$). Itulah efek Jahn–Teller dalam bahasa teori grup.
:::

::: {.dalam}
**Lebih dalam · Karakter putaran untuk momentum sudut $\ell$**

Untuk orbital dengan bilangan kuantum $\ell$, kita tidak perlu menulis setiap fungsi untuk menentukan karakternya. Pilih sumbu putar sebagai sumbu $z$; harmonik bola $Y_\ell^m \propto e^{im\phi}$ hanya dikalikan $e^{-im\alpha}$ oleh putaran $\alpha$ (subbab 6.5). Karakter putaran adalah jumlah semua faktor itu, sebuah deret geometri:

$$
\chi_\ell(\alpha) = \sum_{m=-\ell}^{\ell} e^{-im\alpha} = \frac{\sin\left[(\ell + \tfrac12)\alpha\right]}{\sin(\alpha/2)}, \qquad \chi_\ell(0) = 2\ell + 1 .
$$

Untuk operasi tak sejati, tulis operasi itu sebagai inversi dikali putaran ($\sigma_h = iC_2$, $S_4 = iC_4^3$, $S_6 = iC_3^2$), lalu kalikan dengan paritas $(-1)^\ell$. Untuk $\ell = 2$ dalam $O_h$, rumus ini memberi karakter $5, -1, 1, -1, 1, 5, -1, -1, 1, 1$, yang tereduksi menjadi $E_g + T_{2g}$, sesuai dengan Contoh 10.22.
:::

::: {.contoh}
**Contoh 10.23 · Orbital f dalam kompleks oktahedral**

Gunakan rumus karakter putaran dengan $\ell = 3$ untuk menentukan bagaimana tujuh orbital f terpecah dalam medan $O_h$.

**Penyelesaian.** Dengan $\chi_3(\alpha) = \sin(3{,}5\alpha)/\sin(\alpha/2)$: $\chi(0) = 7$; $\chi(120°) = \sin 420°/\sin 60° = 1$; $\chi(180°) = \sin 630°/\sin 90° = -1$; $\chi(90°) = \sin 315°/\sin 45° = -1$. Karena $\ell$ ganjil, karakter operasi tak sejati bertanda berlawanan dengan putaran pasangannya: $\chi(i) = -7$, $\chi(S_4) = -\chi(C_4) = 1$, $\chi(S_6) = -\chi(C_3) = -1$, $\chi(\sigma_h) = -\chi(C_2) = 1$, $\chi(\sigma_d) = 1$. Deret karakter $7, 1, -1, -1, -1, -7, 1, -1, 1, 1$ tereduksi (dengan rumus di subbab 10.6) menjadi $A_{2u} + T_{1u} + T_{2u}$.

**Memahami hasil.** Orbital f dalam kompleks lantanida oktahedral terpecah menjadi tiga kelompok berdegenerasi 1, 3, dan 3. Pembelahannya sangat kecil (puluhan sampai ratusan cm⁻¹), karena orbital 4f terlindung jauh di dalam atom oleh kulit 5s dan 5p. Itulah sebabnya pita serapan ion lantanida tajam seperti garis atom, sedangkan pita kompleks logam transisi d lebar.
:::

::: {.contoh}
**Contoh 10.24 · Mengapa C₆₀ menerima tepat enam elektron**

Perhitungan orbital molekul C₆₀ menunjukkan bahwa orbital terisi tertinggi (HOMO) bersimetri $h_u$ dan orbital kosong terendah (LUMO) bersimetri $t_{1u}$. Berapa elektron yang mengisi HOMO, dan berapa elektron yang dapat diterima LUMO?

**Penyelesaian.** Irrep $H$ berdimensi lima, jadi HOMO terdiri atas lima orbital berdegenerasi yang menampung $2 \times 5 = 10$ elektron. Irrep $T$ berdimensi tiga, jadi LUMO dapat menerima $2 \times 3 = 6$ elektron.

**Memahami hasil.** Voltametri siklik C₆₀ dalam larutan memperlihatkan enam gelombang reduksi satu elektron yang reversibel, dari C₆₀⁻ sampai C₆₀⁶⁻, sesuai dengan pengisian LUMO berdegenerasi tiga. Garam K₃C₆₀, dengan LUMO terisi setengah, bersifat logam dan menjadi superkonduktor di bawah sekitar 19 K. Kedua gejala ini adalah akibat langsung dimensi irrep, sebuah bilangan yang ditentukan oleh simetri ikosahedral semata.
:::

::: {.kuis}
**Kuis cepat 10.5**

\(a) Grup $D_{3h}$ mempunyai enam kelas dan orde 12. Berapa dimensi irrep-irrepnya? (b) Apa irrep orbital $p_z$ atom B dalam BF₃? (c) Mengapa karakter $\chi(E)$ selalu sama dengan dimensi irrep?
:::

## 10.6 Representasi tak tereduksi dan rumus reduksi

### Rumus reduksi

Setiap representasi tereduksi $\Gamma$ dapat diuraikan menjadi irrep: $\Gamma = \sum_j n_j\Gamma^{(j)}$, dengan $n_j$ bilangan bulat tak negatif yang menyatakan berapa kali irrep $j$ muncul. Karena karakter tidak bergantung pada basis, kita boleh membayangkan matriksnya sudah dalam bentuk diagonal blok; terasnya adalah jumlah teras blok-bloknya:

$$
\chi(R) = \sum_j n_j\,\chi_j(R) .
$$

Kalikan kedua ruas dengan $\chi_i(R)^*$ dan jumlahkan atas semua operasi. Menurut ortogonalitas (10.9), di ruas kanan hanya suku $j = i$ yang bertahan, dan suku itu bernilai $n_i h$. Hasilnya adalah **rumus reduksi**:

$$
n_i = \frac1h\sum_R \chi(R)\,\chi_i(R)^* = \frac1h\sum_c g_c\,\chi(c)\,\chi_i(c)^* . \qquad \text{(10.10)}
$$

Rumus ini adalah alat kerja terpenting dalam bab ini. Masukannya hanya karakter representasi yang hendak diuraikan, yang biasanya mudah dihitung dengan menghitung "berapa yang tidak berpindah"; keluarannya adalah susunan irrep. Untuk grup dengan karakter riil, tanda konjugat dapat diabaikan.

::: {.strategi}
**Strategi · Mereduksi representasi**

1. Tentukan grup titik dan susun kelas-kelasnya seperti dalam tabel karakter.
2. Untuk satu operasi dari setiap kelas, hitung karakter $\chi(R)$ representasi yang ditinjau. Untuk basis berupa atom atau orbital yang dipermutasikan: banyak yang tidak berpindah, dikalikan $\pm1$ bila tanda fungsinya berubah.
3. Untuk setiap irrep, kalikan karakter-karakter itu dengan karakter irrep dan banyak anggota kelas, jumlahkan, lalu bagi dengan $h$.
4. Periksa: setiap $n_i$ harus bilangan bulat tak negatif, dan $\sum_i n_id_i$ harus sama dengan $\chi(E)$, dimensi representasi.
:::

::: {.contoh}
**Contoh 10.25 · Orbital H pada NH₃**

Reduksi representasi dengan basis tiga orbital 1s hidrogen NH₃.

**Penyelesaian.** Karakter: $E$ membiarkan ketiganya, $\chi = 3$; $C_3$ memindahkan semuanya, $\chi = 0$; $\sigma_v$ membiarkan satu H (yang terletak di bidangnya), $\chi = 1$. Dengan (10.10):

$$
n(A_1) = \tfrac16[1(3)(1) + 2(0)(1) + 3(1)(1)] = 1, \quad n(A_2) = \tfrac16[3 + 0 - 3] = 0, \quad n(E) = \tfrac16[1(3)(2) + 2(0)(-1) + 3(1)(0)] = 1 .
$$

Jadi $\Gamma_H = A_1 + E$. Periksa dimensi: $1 + 2 = 3$.

**Memahami hasil.** Hasil ini sesuai dengan transformasi basis di Contoh 10.18: satu kombinasi bersimetri total dan sepasang kombinasi yang bertransformasi seperti $(x, y)$. Rumus reduksi memberi tahu *berapa banyak* irrep dari setiap jenis tanpa mencari matriks transformasinya. Untuk menemukan kombinasinya sendiri, kita memerlukan operator proyeksi (subbab 10.7).
:::

::: {.contoh}
**Contoh 10.26 · Empat hidrogen metana**

Reduksi representasi dengan basis orbital 1s keempat H metana dalam $T_d$.

**Penyelesaian.** Karakter per kelas: $E$: 4; $C_3$ (sumbu sepanjang satu ikatan C–H): 1; $C_2$: 0; $S_4$: 0; $\sigma_d$ (bidang memuat dua H): 2. Dengan $h = 24$:

- $n(A_1) = \tfrac1{24}[4 + 8(1) + 0 + 0 + 6(2)] = \tfrac{24}{24} = 1$;
- $n(A_2) = \tfrac1{24}[4 + 8 + 0 + 0 - 12] = 0$;
- $n(E) = \tfrac1{24}[8 - 8 + 0 + 0 + 0] = 0$;
- $n(T_1) = \tfrac1{24}[12 + 0 + 0 + 0 - 12] = 0$;
- $n(T_2) = \tfrac1{24}[12 + 0 + 0 + 0 + 12] = 1$.

Jadi $\Gamma_H = A_1 + T_2$.

**Memahami hasil.** Orbital valensi C adalah $2s$ ($a_1$) dan $2p_x$, $2p_y$, $2p_z$ ($t_2$, karena $(x, y, z)$ berada di $T_2$). Simetri keempat kombinasi H cocok persis dengan simetri keempat orbital valensi karbon. Akibatnya metana mempunyai empat orbital molekul ikatan, satu $a_1$ dan tiga $t_2$ yang berdegenerasi, bukan empat ikatan yang identik. Spektrum fotoelektron metana memperlihatkan dua pita, bukan satu (subbab 10.8).
:::

::: {.contoh}
**Contoh 10.27 · Sembilan koordinat atom H₂O**

Bangun representasi dengan basis sembilan vektor perpindahan Kartesius (tiga untuk setiap atom) H₂O dan reduksi. Pakai fakta bahwa setiap atom yang tidak berpindah menyumbang teras matriks 3 × 3 operasinya.

**Penyelesaian.** Atom yang tidak berpindah: $E$: 3; $C_2$: 1 (hanya O); $\sigma_v(xz)$: 1 (bidang ini tegak lurus bidang molekul, hanya memuat O); $\sigma_v'(yz)$: 3. Teras per atom (10.3): $E$: 3; $C_2$: $1 + 2\cos180° = -1$; $\sigma$: 1. Karakter: $\chi = (9, -1, 1, 3)$. Reduksi:

$$
n(A_1) = \tfrac14(9 - 1 + 1 + 3) = 3, \quad n(A_2) = \tfrac14(9 - 1 - 1 - 3) = 1, \quad n(B_1) = \tfrac14(9 + 1 + 1 - 3) = 2, \quad n(B_2) = \tfrac14(9 + 1 - 1 + 3) = 3 .
$$

$\Gamma_{3N} = 3A_1 + A_2 + 2B_1 + 3B_2$; periksa $3 + 1 + 2 + 3 = 9$.

**Memahami hasil.** Representasi ini memuat semua gerak atom: translasi, rotasi, dan getaran. Dengan mengurangkan translasi ($A_1 + B_1 + B_2$, dari $z$, $x$, $y$) dan rotasi ($A_2 + B_1 + B_2$, dari $R_z$, $R_y$, $R_x$), sisanya $2A_1 + B_2$ adalah tiga getaran air. Prosedur ini adalah inti subbab 10.9.
:::

::: {.contoh}
**Contoh 10.28 · Reduksi dengan Python**

Tulis fungsi Python untuk rumus reduksi (10.10) dan pakai untuk mereduksi representasi enam orbital σ ligan dalam kompleks oktahedral, dengan karakter $(6, 0, 0, 2, 2, 0, 0, 0, 4, 2)$ dalam urutan kelas tabel $O_h$.

**Penyelesaian.**

```python
import numpy as np
g = np.array([1, 8, 6, 6, 3, 1, 6, 8, 3, 6])          # banyak anggota kelas O_h
Oh = {'A1g': [1,1,1,1,1,1,1,1,1,1],   'A2g': [1,1,-1,-1,1,1,-1,1,1,-1],
      'Eg':  [2,-1,0,0,2,2,0,-1,2,0], 'T1g': [3,0,-1,1,-1,3,1,0,-1,-1],
      'T2g': [3,0,1,-1,-1,3,-1,0,-1,1],
      'A1u': [1,1,1,1,1,-1,-1,-1,-1,-1], 'A2u': [1,1,-1,-1,1,-1,1,-1,-1,1],
      'Eu':  [2,-1,0,0,2,-2,0,1,-2,0], 'T1u': [3,0,-1,1,-1,-3,-1,0,1,1],
      'T2u': [3,0,1,-1,-1,-3,1,0,1,-1]}
def reduksi(chi, tabel=Oh, g=g):
    h = g.sum()
    return {k: int(round((g * np.array(chi) * np.array(v)).sum() / h))
            for k, v in tabel.items()}
hasil = reduksi([6, 0, 0, 2, 2, 0, 0, 0, 4, 2])
print({k: n for k, n in hasil.items() if n})      # {'A1g': 1, 'Eg': 1, 'T1u': 1}
```

**Memahami hasil.** Keenam orbital σ ligan membentuk kombinasi $a_{1g} + e_g + t_{1u}$. Bandingkan dengan orbital valensi logam: $4s$ ($a_{1g}$), $3d_{z^2}$ dan $3d_{x^2-y^2}$ ($e_g$), dan $4p$ ($t_{1u}$). Orbital $d_{xy}$, $d_{xz}$, $d_{yz}$ ($t_{2g}$) tidak mempunyai pasangan σ dari ligan, sehingga tetap tak mengikat dalam ikatan σ. Kesimpulan ini adalah dasar teori medan ligan (Bab 14), dan diperoleh hanya dengan tiga baris aritmetika.
:::

### Hasil kali langsung

Bila $f$ bertransformasi menurut irrep $\Gamma_a$ dan $g$ menurut $\Gamma_b$, hasil kali $fg$ bertransformasi menurut **hasil kali langsung** $\Gamma_a \times \Gamma_b$, yang karakternya adalah hasil kali karakter:

$$
\chi_{a \times b}(R) = \chi_a(R)\,\chi_b(R) . \qquad \text{(10.11)}
$$

Hasil kali langsung biasanya tereduksi, dan diuraikan dengan (10.10). Beberapa aturan praktis:

- Hasil kali dengan irrep simetri total tidak mengubah apa pun: $A_1 \times \Gamma = \Gamma$.
- Hasil kali dua irrep satu dimensi adalah irrep satu dimensi, dengan aturan $g \times g = u \times u = g$, $g \times u = u$, $' \times ' = '' \times '' = '$, $' \times '' = ''$, dan untuk indeks $A \times A = B \times B = A$, $A \times B = B$.
- Hasil kali sebuah irrep dengan dirinya sendiri selalu memuat irrep simetri total tepat satu kali (untuk irrep riil).
- Untuk irrep berdimensi lebih dari satu, dimensi hasil kali $d_ad_b$ dibagi ke beberapa irrep; misalnya dalam $C_{3v}$, $E \times E = A_1 + A_2 + E$ (dimensi $2 \times 2 = 1 + 1 + 2$).

### Teorema integral lenyap

Sekarang kita sampai pada hasil teori grup yang paling banyak dipakai. Tinjau integral $I = \int f\,d\tau$ atas seluruh ruang. Nilainya tidak berubah bila kita mengenakan operasi simetri $R$ pada fungsi $f$, karena operasi itu hanya memindahkan titik-titik ruang tanpa mengubah volume: $\int \hat O_Rf\,d\tau = \int f\,d\tau$. Jumlahkan atas semua $h$ operasi dan bagi dengan $h$:

$$
I = \int\left[\frac1h\sum_R\hat O_Rf\right]d\tau .
$$

Fungsi dalam kurung siku adalah "rata-rata $f$ atas grup". Bila $f$ bertransformasi menurut irrep $\Gamma$ yang **bukan** simetri total, rata-rata ini nol. Sebabnya: untuk irrep satu dimensi, $\hat O_Rf = \chi(R)f$, dan rata-ratanya $f\cdot\frac1h\sum_R\chi(R)$, yang menurut ortogonalitas dengan baris simetri total (10.9) bernilai nol. Untuk irrep berdimensi lebih, argumen yang sama berlaku untuk setiap unsur diagonal matriks. Jadi:

::: {.inti}
**Teorema integral lenyap**

Integral $\int f\,d\tau$ atas seluruh ruang **pasti nol** kecuali $f$ memuat komponen yang bersimetri total. Untuk hasil kali beberapa fungsi,

$$
\int f_af_bf_c\,d\tau = 0 \quad \text{kecuali} \quad \Gamma_a \times \Gamma_b \times \Gamma_c \ \text{memuat} \ A_1 . \qquad \text{(10.12)}
$$

Kasus khusus yang penting:

- **Tumpang tindih** $\int\phi_a\phi_b\,d\tau \ne 0$ hanya bila $\Gamma_a = \Gamma_b$.
- **Unsur matriks Hamiltonian** $\int\phi_a\hat H\phi_b\,d\tau \ne 0$ hanya bila $\Gamma_a = \Gamma_b$, karena $\hat H$ bersimetri total.
- **Momen dipol transisi** $\int\psi_f\,\hat\mu_q\,\psi_i\,d\tau \ne 0$ hanya bila $\Gamma_f \times \Gamma_q \times \Gamma_i$ memuat $A_1$, dengan $\Gamma_q$ irrep komponen $q = x$, $y$, atau $z$.
:::

Teorema ini adalah perluasan langsung dari pernyataan "integral fungsi ganjil pada selang simetris adalah nol" (subbab 2.2 dan 4.11). Paritas adalah grup dengan dua unsur, $\{E, i\}$; teori grup menerapkan logika yang sama pada semua operasi molekul sekaligus.

::: {.awas}
**Awas · "Diizinkan" tidak berarti "besar"**

Teorema integral lenyap hanya bekerja satu arah. Bila hasil kali langsung tidak memuat $A_1$, integralnya **pasti** nol. Bila memuat $A_1$, integralnya **boleh** tidak nol, tetapi bisa saja kecil, atau bahkan nol karena alasan lain (misalnya kedua fungsi berada di daerah ruang yang berbeda jauh). Teori grup memberi tahu di mana tidak perlu menghitung; besarnya integral yang diizinkan tetap harus dihitung atau diukur.
:::

::: {.contoh}
**Contoh 10.29 · Hasil kali langsung $E \times E$**

Hitung karakter $E \times E$ dalam $C_{3v}$ dan uraikan. Apa makna hasilnya bagi dua elektron yang menempati orbital $e$?

**Penyelesaian.** Karakter $E$ adalah $(2, -1, 0)$; kuadratnya $(4, 1, 0)$. Reduksi: $n(A_1) = \tfrac16[4 + 2(1) + 0] = 1$; $n(A_2) = \tfrac16[4 + 2 - 0] = 1$; $n(E) = \tfrac16[8 - 2 + 0] = 1$. Jadi $E \times E = A_1 + A_2 + E$.

**Memahami hasil.** Konfigurasi $e^2$ (misalnya dua elektron di orbital $e$ molekul $C_{3v}$) menghasilkan keadaan-keadaan dengan simetri ruang $A_1$, $A_2$, dan $E$. Mana yang singlet dan mana yang triplet ditentukan oleh asas Pauli: bagian ruang yang antisimetris terhadap pertukaran elektron ($A_2$) berpasangan dengan spin triplet, sedangkan yang simetris ($A_1$ dan $E$) dengan singlet. Inilah analog molekul dari lambang suku atom (subbab 9.12), dan aturan Hund meramalkan $^3A_2$ sebagai keadaan dasar.
:::

::: {.contoh}
**Contoh 10.30 · Integral mana yang pasti nol dalam H₂O?**

Dalam H₂O ($C_{2v}$), tentukan apakah integral berikut pasti nol: (a) tumpang tindih $\langle 2p_x(\text{O})|s_1 + s_2\rangle$; (b) $\langle 2p_y(\text{O})|s_1 - s_2\rangle$; (c) $\langle 2s|\hat z|2p_z\rangle$; (d) $\langle 2s|\hat x|2p_z\rangle$; (e) $\langle 2p_x|\hat H|2p_y\rangle$.

**Penyelesaian.** (a) $B_1 \times A_1 = B_1$: pasti nol. (b) $B_2 \times B_2 = A_1$: boleh tidak nol. (c) $A_1 \times A_1 \times A_1 = A_1$: boleh tidak nol. (d) $A_1 \times B_1 \times A_1 = B_1$: pasti nol. (e) $B_1 \times A_1 \times B_2 = A_2$: pasti nol.

**Memahami hasil.** Hasil (a) berarti orbital $2p_x$ oksigen, yang tegak lurus bidang molekul, tidak dapat membentuk ikatan dengan atom H sama sekali: ia menjadi orbital tak mengikat, salah satu "pasangan elektron bebas" air. Hasil (b) memungkinkan $2p_y$ membentuk ikatan dengan kombinasi $s_1 - s_2$. Hasil (c) dan (d) adalah aturan seleksi: transisi $2s \to 2p_z$ hanya dapat dirangsang cahaya yang terpolarisasi sepanjang $z$. Tanpa menghitung satu integral pun, kita sudah memangkas sebagian besar unsur matriks yang perlu dihitung.
:::

::: {.kuis}
**Kuis cepat 10.6**

\(a) Reduksi representasi dengan karakter $(4, 0, 2, 2)$ dalam $C_{2v}$. (b) Hitung $T_2 \times T_2$ dalam $T_d$ dan periksa dimensinya. (c) Dalam $O_h$, apakah $\int d_{xy}\,\hat z\,d_{xz}\,d\tau$ pasti nol?
:::
