## 10.3 Tabel perkalian grup

### Empat syarat grup

Dalam matematika, **grup** adalah himpunan unsur $\{A, B, C, \ldots\}$ bersama satu cara "mengalikan" dua unsur, yang memenuhi empat syarat:

1. **Ketertutupan.** Hasil kali dua unsur grup juga unsur grup: bila $A$ dan $B$ di dalam grup, $AB$ juga di dalam grup.
2. **Asosiatif.** $(AB)C = A(BC)$.
3. **Identitas.** Ada unsur $E$ sehingga $EA = AE = A$ untuk setiap $A$.
4. **Invers.** Setiap $A$ mempunyai invers $A^{-1}$ di dalam grup, dengan $AA^{-1} = A^{-1}A = E$.

Banyaknya unsur disebut **orde** grup, dilambangkan $h$. Untuk operasi simetri, "perkalian" berarti melakukan dua operasi berturut-turut. Kita memakai kesepakatan yang sama dengan perkalian operator (subbab 4.1): $AB$ berarti **$B$ dilakukan lebih dahulu, lalu $A$**.

Mengapa himpunan operasi simetri sebuah molekul selalu memenuhi keempat syarat itu? Ketertutupan jelas: jika $B$ membawa molekul ke kedudukan yang tak dapat dibedakan, dan $A$ juga, maka $A$ sesudah $B$ pun demikian; gabungannya pasti salah satu operasi dalam daftar lengkap. Asosiatif berlaku karena operasi adalah perkalian matriks (subbab 10.1). Identitas adalah $E$. Invers setiap operasi juga operasi simetri: putaran $C_n^k$ dibatalkan oleh $C_n^{n-k}$, pencerminan dan inversi adalah invers dirinya sendiri ($\sigma^2 = i^2 = E$), dan $S_n^k$ dibatalkan oleh $S_n^{-k}$.

### Tabel perkalian $C_{2v}$

Semua hasil kali dalam sebuah grup dapat disusun dalam **tabel perkalian**: baris $A$ dan kolom $B$ berisi $AB$. Untuk H₂O, dengan sumbu seperti di Contoh 10.1, efek setiap operasi pada titik $(x, y, z)$ adalah:

$$
E: (x, y, z), \quad C_2: (-x, -y, z), \quad \sigma_v(xz): (x, -y, z), \quad \sigma_v'(yz): (-x, y, z) .
$$

Melakukan dua operasi berturut-turut sama dengan mengalikan tanda-tanda koordinatnya. Misalnya $\sigma_v(xz)$ lalu $\sigma_v'(yz)$: $(x, y, z) \to (x, -y, z) \to (-x, -y, z)$, yaitu $C_2$. Dengan cara yang sama diperoleh seluruh tabel:

| $C_{2v}$ | $E$ | $C_2$ | $\sigma_v(xz)$ | $\sigma_v'(yz)$ |
|---|---|---|---|---|
| $E$ | $E$ | $C_2$ | $\sigma_v$ | $\sigma_v'$ |
| $C_2$ | $C_2$ | $E$ | $\sigma_v'$ | $\sigma_v$ |
| $\sigma_v(xz)$ | $\sigma_v$ | $\sigma_v'$ | $E$ | $C_2$ |
| $\sigma_v'(yz)$ | $\sigma_v'$ | $\sigma_v$ | $C_2$ | $E$ |

Dua hal tampak dari tabel ini. Pertama, tabelnya simetris terhadap diagonal: $AB = BA$ untuk semua pasangan. Grup seperti ini disebut **abelian** (komutatif). Kedua, setiap baris dan setiap kolom memuat setiap unsur tepat satu kali, seperti teka-teki sudoku. Sifat kedua ini berlaku untuk semua grup.

::: {.dalam}
**Lebih dalam · Teorema penyusunan ulang**

*Klaim:* dalam setiap baris tabel perkalian, setiap unsur grup muncul tepat satu kali.

*Bukti.* Tinjau baris $A$, yang berisi $AB_1, AB_2, \ldots, AB_h$. Misalkan dua di antaranya sama: $AB_j = AB_k$. Kalikan dari kiri dengan $A^{-1}$ (yang ada menurut syarat 4): $B_j = B_k$. Jadi hasil kali yang berbeda selalu berasal dari kolom yang berbeda, dan tidak ada unsur yang muncul dua kali. Karena ada $h$ isian dan $h$ unsur, setiap unsur muncul tepat sekali. Bukti untuk kolom sama, dengan perkalian dari kanan.

*Akibat yang berguna:* bila $f(R)$ suatu fungsi pada unsur grup, maka $\sum_R f(AR) = \sum_R f(R)$ untuk setiap $A$, karena $AR$ hanya menyusun ulang urutan penjumlahan. Teorema ini adalah kunci bukti teorema integral lenyap (subbab 10.6) dan sifat operator proyeksi (subbab 10.7).
:::

### Grup yang tidak komutatif: $C_{3v}$

Pada NH₃, urutan operasi menentukan hasil. Beri nomor tiga posisi atom H: posisi 1, 2, dan 3, berurutan berlawanan arah jarum jam bila dilihat dari atas (dari N). Putaran $C_3$ memindahkan isi posisi 1 ke posisi 2, isi posisi 2 ke 3, dan isi posisi 3 ke 1. Bidang $\sigma_1$ memuat posisi 1 sehingga menukar isi posisi 2 dan 3; demikian pula $\sigma_2$ dan $\sigma_3$.

Tinjau $C_3\sigma_1$: lakukan $\sigma_1$ dahulu, lalu $C_3$. Mulai dengan atom berlabel a, b, c di posisi 1, 2, 3. Setelah $\sigma_1$: (a, c, b). Setelah $C_3$, setiap atom maju satu posisi: atom di posisi 3 pindah ke 1, sehingga diperoleh (b, a, c). Bandingkan dengan susunan awal (a, b, c): atom c tetap di posisi 3, atom a dan b bertukar. Itulah $\sigma_3$. Jadi $C_3\sigma_1 = \sigma_3$.

Sekarang urutan terbalik, $\sigma_1C_3$: $C_3$ dahulu memberikan (c, a, b), lalu $\sigma_1$ menukar isi posisi 2 dan 3: (c, b, a). Atom b tetap di posisi 2: itulah $\sigma_2$. Jadi $\sigma_1C_3 = \sigma_2 \ne C_3\sigma_1$ (Gambar 10.3).

![Gambar 10.3 Operasi pada NH₃ tidak komutatif. Atas: $\sigma_1$ lalu $C_3$ menghasilkan susunan yang sama dengan $\sigma_3$. Bawah: $C_3$ lalu $\sigma_1$ menghasilkan susunan yang sama dengan $\sigma_2$. Molekul dilihat dari atas sepanjang sumbu $C_3$; garis putus-putus menandai bidang cermin.](fig/c_c3v.png){width=90%}

Dengan cara yang sama diperoleh tabel lengkap $C_{3v}$ (baris $A$, kolom $B$, isi $AB$):

| $C_{3v}$ | $E$ | $C_3$ | $C_3^2$ | $\sigma_1$ | $\sigma_2$ | $\sigma_3$ |
|---|---|---|---|---|---|---|
| $E$ | $E$ | $C_3$ | $C_3^2$ | $\sigma_1$ | $\sigma_2$ | $\sigma_3$ |
| $C_3$ | $C_3$ | $C_3^2$ | $E$ | $\sigma_3$ | $\sigma_1$ | $\sigma_2$ |
| $C_3^2$ | $C_3^2$ | $E$ | $C_3$ | $\sigma_2$ | $\sigma_3$ | $\sigma_1$ |
| $\sigma_1$ | $\sigma_1$ | $\sigma_2$ | $\sigma_3$ | $E$ | $C_3$ | $C_3^2$ |
| $\sigma_2$ | $\sigma_2$ | $\sigma_3$ | $\sigma_1$ | $C_3^2$ | $E$ | $C_3$ |
| $\sigma_3$ | $\sigma_3$ | $\sigma_1$ | $\sigma_2$ | $C_3$ | $C_3^2$ | $E$ |

Tabel ini tidak simetris terhadap diagonal: $C_{3v}$ **nonabelian**. Hasil kali dua pencerminan selalu putaran, dan hasil kali putaran dengan pencerminan selalu pencerminan, sesuai dengan aturan determinan: $(-1)(-1) = +1$ dan $(+1)(-1) = -1$.

### Subgrup dan teorema Lagrange

Sebagian unsur sebuah grup dapat membentuk grup tersendiri, disebut **subgrup**. Dari tabel $C_{3v}$ terlihat bahwa $\{E, C_3, C_3^2\}$ tertutup terhadap perkalian: inilah grup $C_3$. Setiap $\{E, \sigma_k\}$ juga subgrup, yaitu grup $C_s$. Orde subgrup-subgrup itu, 3 dan 2, adalah pembagi orde grup induknya, 6. Ini bukan kebetulan: **teorema Lagrange** menyatakan bahwa orde setiap subgrup selalu membagi habis orde grup. Teorema ini membatasi penurunan simetri yang mungkin: grup berorde 6 tidak mungkin mempunyai subgrup berorde 4 atau 5.

### Kelas

Dua unsur $A$ dan $B$ disebut **sekawan** (*conjugate*) bila ada unsur $X$ dalam grup sehingga

$$
B = X^{-1}AX . \qquad \text{(10.4)}
$$

Himpunan semua unsur yang saling sekawan disebut **kelas**. Makna fisisnya sederhana: $X^{-1}AX$ adalah operasi $A$ yang "dilihat dari sudut pandang lain". Bila $X$ memutar molekul, $X^{-1}AX$ adalah operasi sejenis $A$ yang unsurnya ikut diputar oleh $X$. Jadi operasi-operasi dalam satu kelas adalah operasi sejenis yang unsur-unsurnya dipertukarkan oleh simetri molekul itu sendiri. Di NH₃, ketiga bidang $\sigma_v$ dipertukarkan oleh $C_3$, sehingga ketiganya satu kelas. Putaran $C_3$ dan $C_3^2$ juga satu kelas, karena pencerminan mengubah arah putar berlawanan jarum jam menjadi searah jarum jam. Identitas selalu menjadi kelas tersendiri, karena $X^{-1}EX = E$.

Dalam grup abelian, $X^{-1}AX = X^{-1}XA = A$, sehingga setiap unsur menjadi kelas tersendiri. Itulah sebabnya keempat operasi $C_{2v}$ membentuk empat kelas. Dalam tabel karakter, operasi sekelas dikumpulkan dalam satu kolom dengan koefisien banyak anggotanya: $C_{3v}$ ditulis $E$, $2C_3$, $3\sigma_v$.

::: {.contoh}
**Contoh 10.11 · Memeriksa tabel $C_{2v}$**

Tunjukkan dengan koordinat bahwa $C_2\sigma_v(xz) = \sigma_v'(yz)$ dan bahwa setiap unsur $C_{2v}$ adalah invers dirinya sendiri.

**Penyelesaian.** $\sigma_v(xz)$: $(x, y, z) \to (x, -y, z)$; lalu $C_2$: $(x, -y, z) \to (-x, y, z)$. Hasilnya sama dengan $\sigma_v'(yz)$. Untuk invers: $C_2C_2$ membalik tanda $x$ dan $y$ dua kali sehingga kembali ke $(x, y, z)$; demikian pula setiap pencerminan yang dilakukan dua kali. Jadi $C_2^{-1} = C_2$, $\sigma_v^{-1} = \sigma_v$, $\sigma_v'^{-1} = \sigma_v'$.

**Memahami hasil.** Grup yang setiap unsurnya merupakan invers dirinya sendiri selalu abelian, karena $AB = (AB)^{-1} = B^{-1}A^{-1} = BA$. Grup $C_{2h}$ ($E$, $C_2$, $i$, $\sigma_h$) dan $D_2$ ($E$, tiga $C_2$ yang saling tegak lurus) juga bersifat demikian, dan ketiganya mempunyai tabel perkalian yang sama bentuknya. Grup seperti itu disebut **isomorf**. Grup yang isomorf mempunyai tabel karakter yang sama; yang berbeda hanyalah nama operasi dan fungsi basisnya.
:::

::: {.contoh}
**Contoh 10.12 · Perkalian dengan matriks**

Pakai matriks (10.2) untuk memeriksa $C_3\sigma_1 = \sigma_3$ dengan sumbu $z$ sepanjang $C_3$, bidang $\sigma_1$ adalah bidang $yz$ (memuat H₁ di sumbu $+y$), dan H₂, H₃ pada sudut 210° dan 330° dari sumbu $x$.

**Penyelesaian.** $\sigma_1 = \sigma(yz) = \mathrm{diag}(-1, 1, 1)$. Dengan $\cos 120° = -\tfrac12$ dan $\sin 120° = \tfrac{\sqrt3}{2}$:

$$
C_3\sigma_1 = \begin{pmatrix}-\tfrac12 & -\tfrac{\sqrt3}{2} & 0\\ \tfrac{\sqrt3}{2} & -\tfrac12 & 0\\ 0 & 0 & 1\end{pmatrix}\begin{pmatrix}-1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1\end{pmatrix} = \begin{pmatrix}\tfrac12 & -\tfrac{\sqrt3}{2} & 0\\ -\tfrac{\sqrt3}{2} & -\tfrac12 & 0\\ 0 & 0 & 1\end{pmatrix} .
$$

Pencerminan pada bidang vertikal yang memuat arah bersudut $\phi$ dari sumbu $x$ mempunyai matriks $\begin{pmatrix}\cos2\phi & \sin2\phi\\ \sin2\phi & -\cos2\phi\end{pmatrix}$ di blok $xy$. Untuk $\phi = 330°$, $2\phi = 660° \equiv 300°$, sehingga $\cos2\phi = \tfrac12$ dan $\sin2\phi = -\tfrac{\sqrt3}{2}$. Hasilnya sama persis dengan matriks di atas: $C_3\sigma_1 = \sigma_3$.

**Memahami hasil.** Perhitungan dengan pelabelan atom dan dengan matriks memberi jawaban yang sama, sebagaimana mestinya. Pelabelan atom lebih cepat untuk tabel perkalian; matriks lebih aman untuk operasi yang rumit seperti $S_6$ atau putaran terhadap sumbu miring. Matriks juga membuka jalan ke konsep berikutnya: representasi.
:::

::: {.contoh}
**Contoh 10.13 · Menentukan kelas $C_{3v}$**

Dengan tabel perkalian $C_{3v}$, hitung $X^{-1}\sigma_1X$ untuk semua $X$, lalu $X^{-1}C_3X$ untuk $X = \sigma_1$.

**Penyelesaian.** Invers: $C_3^{-1} = C_3^2$, $(C_3^2)^{-1} = C_3$, $\sigma_k^{-1} = \sigma_k$.

- $X = C_3$: $C_3^2\sigma_1C_3 = C_3^2(\sigma_1C_3) = C_3^2\sigma_2 = \sigma_3$.
- $X = C_3^2$: $C_3\sigma_1C_3^2 = C_3(\sigma_1C_3^2) = C_3\sigma_3 = \sigma_2$.
- $X = \sigma_2$: $\sigma_2\sigma_1\sigma_2 = \sigma_2(\sigma_1\sigma_2) = \sigma_2C_3 = \sigma_3$.
- $X = \sigma_1$ atau $E$: $\sigma_1$ sendiri.

Jadi $\{\sigma_1, \sigma_2, \sigma_3\}$ satu kelas. Untuk putaran: $\sigma_1C_3\sigma_1 = (\sigma_1C_3)\sigma_1 = \sigma_2\sigma_1 = C_3^2$, sehingga $\{C_3, C_3^2\}$ satu kelas.

**Memahami hasil.** Grup $C_{3v}$ mempunyai tiga kelas: $\{E\}$, $\{C_3, C_3^2\}$, dan $\{\sigma_1, \sigma_2, \sigma_3\}$. Di subbab 10.5 kita akan melihat bahwa banyaknya kelas sama dengan banyaknya representasi tak tereduksi. Dalam grup $C_3$ saja (tanpa cermin), $C_3$ dan $C_3^2$ tidak sekawan, sehingga grup itu mempunyai tiga kelas berisi satu unsur dan tiga representasi berdimensi satu (dua di antaranya kompleks).
:::

::: {.contoh}
**Contoh 10.14 · $C_{2h}$ dan hubungan $i = \sigma_hC_2$**

Untuk *trans*-N₂F₂, sumbu $C_2$ sepanjang $z$ tegak lurus bidang molekul $xy$. Tunjukkan bahwa $\{E, C_2, i, \sigma_h\}$ tertutup dan susunlah tabel perkaliannya.

**Penyelesaian.** $C_2$: $(-x, -y, z)$; $\sigma_h$: $(x, y, -z)$; $i$: $(-x, -y, -z)$. Maka $\sigma_hC_2$: $(x, y, z) \to (-x, -y, z) \to (-x, -y, -z) = i$. Juga $iC_2 = \sigma_h$, $i\sigma_h = C_2$, dan setiap unsur kuadratnya $E$. Tabelnya:

| $C_{2h}$ | $E$ | $C_2$ | $i$ | $\sigma_h$ |
|---|---|---|---|---|
| $E$ | $E$ | $C_2$ | $i$ | $\sigma_h$ |
| $C_2$ | $C_2$ | $E$ | $\sigma_h$ | $i$ |
| $i$ | $i$ | $\sigma_h$ | $E$ | $C_2$ |
| $\sigma_h$ | $\sigma_h$ | $i$ | $C_2$ | $E$ |

**Memahami hasil.** Setiap molekul yang mempunyai sumbu $C_2$ dan bidang $\sigma_h$ yang tegak lurus padanya otomatis sentrosimetris. Itulah sebabnya semua grup $C_{nh}$ dan $D_{nh}$ dengan $n$ genap mempunyai pusat inversi, sedangkan $D_{3h}$ (BF₃) tidak. Tabel ini isomorf dengan tabel $C_{2v}$: pasangkan $i \leftrightarrow \sigma_v$ dan $\sigma_h \leftrightarrow \sigma_v'$.
:::

::: {.contoh}
**Contoh 10.15 · Subgrup $T_d$**

Grup $T_d$ berorde 24. (a) Orde berapa saja yang mungkin untuk subgrupnya? (b) Sebutkan turunan metana dengan substituen atom tunggal yang grupnya merupakan subgrup $T_d$ berorde 6, 4, 2, dan 1.

**Penyelesaian.** (a) Pembagi 24: 1, 2, 3, 4, 6, 8, 12, 24. (b) CH₃Cl: $C_{3v}$ (orde 6); CH₂Cl₂: $C_{2v}$ (orde 4); CH₂ClBr: $C_s$ (orde 2); CHFClBr: $C_1$ (orde 1).

**Memahami hasil.** Substitusi dengan atom tunggal tidak pernah menghasilkan $C_3$ (orde 3) atau $C_2$ (orde 2) saja, karena atom tunggal tidak dapat merusak bidang cermin yang memuat ikatannya; subgrup murni putaran memerlukan substituen yang "terpuntir", seperti ligan bidentat pada kompleks kiral (subbab 10.11). Grup $D_{2d}$ (orde 8) dan $S_4$ (orde 4) juga subgrup $T_d$: tetrahedron yang ditekan sepanjang salah satu sumbu $S_4$ menjadi $D_{2d}$, misalnya [CuCl₄]²⁻ yang terdistorsi. Rantai penurunan simetri $T_d \to D_{2d} \to C_{2v}$ atau $T_d \to C_{3v} \to C_s$ menentukan bagaimana tingkat berdegenerasi terpecah ketika molekul terdistorsi (subbab 10.5).
:::

::: {.kuis}
**Kuis cepat 10.3**

\(a) Dalam $C_{3v}$, berapa $\sigma_2\sigma_3$? (b) Apakah $\{E, C_3, \sigma_1\}$ sebuah subgrup? (c) Mengapa $E$ selalu membentuk kelas sendiri?
:::

## 10.4 Representasi matriks

### Dari operasi ke matriks

Di subbab 10.1, setiap operasi kita tulis sebagai matriks 3 × 3 yang bekerja pada koordinat $(x, y, z)$. Yang istimewa dari himpunan matriks itu adalah bahwa perkaliannya meniru tabel perkalian grup: bila $AB = C$ dalam grup, maka $\mathbf D(A)\mathbf D(B) = \mathbf D(C)$ untuk matriksnya. Setiap himpunan matriks yang meniru tabel perkalian dengan cara ini disebut **representasi** grup, dan himpunan benda yang ditransformasikan matriks itu disebut **basis** representasi.

Basisnya tidak harus koordinat $x$, $y$, $z$. Basis dapat berupa orbital atom, vektor perpindahan atom (untuk getaran), fungsi gelombang, atau apa saja yang berubah secara linear ketika operasi simetri dikenakan. Pilihan basis menentukan ukuran matriks: basis dengan $n$ anggota menghasilkan matriks $n \times n$ dan representasi berdimensi $n$.

### Bagaimana fungsi bertransformasi

Untuk orbital, yang kita perlukan adalah bagaimana sebuah fungsi berubah ketika molekul dikenai operasi. Kesepakatannya: operator $\hat O_R$ yang bersesuaian dengan operasi $R$ menghasilkan fungsi baru yang nilainya di titik $R\mathbf r$ sama dengan nilai fungsi lama di $\mathbf r$, yaitu fungsi itu "dibawa ikut" oleh operasi:

$$
\hat O_R f(\mathbf r) = f(R^{-1}\mathbf r) . \qquad \text{(10.5)}
$$

Untuk operasi-operasi $C_{2v}$, yang semuanya invers dirinya sendiri, $R^{-1} = R$, dan aturannya sederhana: ganti setiap koordinat dalam rumus fungsi dengan koordinat hasil operasi. Orbital $p_x$ atom O sebanding dengan $x\,g(r)$, dengan $g(r)$ bergantung hanya pada jarak dari O. Di bawah $C_2$, $x \to -x$ sedangkan $r$ tetap, sehingga $p_x \to -p_x$: cuping positif berpindah ke tempat cuping negatif. Di bawah $\sigma_v(xz)$, $x$ tetap, sehingga $p_x \to p_x$. Dengan cara ini, setiap orbital O dalam H₂O memberikan satu bilangan untuk setiap operasi:

| Orbital O | $E$ | $C_2$ | $\sigma_v(xz)$ | $\sigma_v'(yz)$ |
|---|---|---|---|---|
| $2s$, $2p_z$ | 1 | 1 | 1 | 1 |
| $2p_x$ | 1 | $-1$ | 1 | $-1$ |
| $2p_y$ | 1 | $-1$ | $-1$ | 1 |

Setiap baris adalah representasi berdimensi satu: matriks 1 × 1, yaitu bilangan $\pm1$, yang hasil kalinya meniru tabel $C_{2v}$. Periksa, misalnya, baris $p_y$: $C_2\sigma_v = \sigma_v'$ dan $(-1)(-1) = +1$, cocok. Baris paling atas, yang semuanya 1, disebut **representasi simetri total**; setiap grup mempunyainya.

### Representasi tereduksi dan tak tereduksi

Sekarang ambil basis yang lebih menarik: kedua orbital 1s hidrogen dalam H₂O, $s_1$ dan $s_2$. Operasi $E$ dan $\sigma_v'(yz)$ (bidang molekul) membiarkan keduanya di tempat; $C_2$ dan $\sigma_v(xz)$ menukarnya. Matriksnya:

$$
\mathbf D(E) = \mathbf D(\sigma_v') = \begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix}, \qquad \mathbf D(C_2) = \mathbf D(\sigma_v) = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix} .
$$

Matriks $\mathbf D(C_2)$ tidak diagonal: $s_1$ dan $s_2$ dicampur. Tetapi bila kita ganti basisnya dengan kombinasi $s_+ = (s_1 + s_2)/\sqrt2$ dan $s_- = (s_1 - s_2)/\sqrt2$, pertukaran $s_1 \leftrightarrow s_2$ membiarkan $s_+$ tetap dan membalik tanda $s_-$. Dalam basis baru semua matriks diagonal:

$$
\mathbf D'(C_2) = \mathbf D'(\sigma_v) = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}, \qquad \mathbf D'(E) = \mathbf D'(\sigma_v') = \begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix} .
$$

Representasi dua dimensi itu terurai menjadi dua representasi satu dimensi yang berjalan sendiri-sendiri: $s_+$ bertransformasi seperti $2s$ dan $2p_z$ (semua $+1$), sedangkan $s_-$ bertransformasi seperti $2p_y$ $(1, -1, -1, 1)$.

Secara umum, perubahan basis dengan matriks $\mathbf U$ mengubah setiap matriks representasi menjadi $\mathbf D'(R) = \mathbf U^{-1}\mathbf D(R)\mathbf U$, yang disebut **transformasi keserupaan**. Bila ada satu $\mathbf U$ yang membuat **semua** matriks $\mathbf D'(R)$ berbentuk diagonal blok dengan susunan blok yang sama,

$$
\mathbf D'(R) = \begin{pmatrix}\mathbf D^{(1)}(R) & \mathbf 0\\ \mathbf 0 & \mathbf D^{(2)}(R)\end{pmatrix} \quad \text{untuk setiap } R , \qquad \text{(10.6)}
$$

maka representasi itu disebut **tereduksi**, dan ditulis sebagai jumlah langsung $\Gamma = \Gamma^{(1)} \oplus \Gamma^{(2)}$, atau singkatnya $\Gamma = \Gamma^{(1)} + \Gamma^{(2)}$. Bila tidak ada transformasi yang dapat memperkecil blok lagi, representasi itu **tak tereduksi** (*irreducible representation*, disingkat irrep). Representasi tak tereduksi adalah "atom" teori grup: setiap representasi dapat diuraikan menjadi irrep, dan uraiannya tunggal.

Mengapa ini penting bagi kimia? Karena fungsi-fungsi yang menjadi basis satu irrep berdimensi $d$ dipetakan satu sama lain oleh operasi simetri, dan Hamiltonian yang komut dengan semua operasi tidak dapat membedakannya. Fungsi-fungsi itu **harus** berenergi sama. Inilah asal degenerasi yang dipaksakan simetri: dimensi irrep sama dengan derajat degenerasi.

::: {.contoh}
**Contoh 10.16 · Representasi $C_{2v}$ dengan basis $(x, y, z)$**

Tuliskan matriks keempat operasi $C_{2v}$ dalam basis $(x, y, z)$ dan periksa bahwa $\mathbf D(C_2)\mathbf D(\sigma_v) = \mathbf D(\sigma_v')$.

**Penyelesaian.** Dari efek pada koordinat: $\mathbf D(E) = \mathrm{diag}(1, 1, 1)$, $\mathbf D(C_2) = \mathrm{diag}(-1, -1, 1)$, $\mathbf D(\sigma_v) = \mathrm{diag}(1, -1, 1)$, $\mathbf D(\sigma_v') = \mathrm{diag}(-1, 1, 1)$. Perkalian matriks diagonal adalah perkalian unsur demi unsur: $\mathrm{diag}(-1, -1, 1)\,\mathrm{diag}(1, -1, 1) = \mathrm{diag}(-1, 1, 1) = \mathbf D(\sigma_v')$.

**Memahami hasil.** Semua matriksnya sudah diagonal, sehingga representasi tiga dimensi ini langsung terurai menjadi tiga representasi satu dimensi: $x$ dengan $(1, -1, 1, -1)$, $y$ dengan $(1, -1, -1, 1)$, dan $z$ dengan $(1, 1, 1, 1)$. Dalam grup abelian, semua irrep berdimensi satu, sehingga tidak ada degenerasi yang dipaksakan simetri. Molekul $C_{2v}$ seperti H₂O tidak mempunyai orbital berdegenerasi, kecuali secara kebetulan.
:::

::: {.contoh}
**Contoh 10.17 · Basis $(x, y, z)$ pada $C_{3v}$**

Dengan matriks dari Contoh 10.12, tunjukkan bahwa dalam basis $(x, y, z)$ representasi $C_{3v}$ berbentuk diagonal blok 2 + 1, dan bahwa blok 2 × 2 tidak dapat dipecah lagi.

**Penyelesaian.** Matriks $C_3$, $C_3^2$, dan ketiga $\sigma_v$ semuanya berbentuk $\begin{pmatrix}\mathbf A & 0\\ 0 & 1\end{pmatrix}$ dengan $\mathbf A$ berukuran 2 × 2, karena tidak ada operasi yang mencampur $z$ dengan $x$ atau $y$. Jadi $z$ sendiri adalah basis representasi satu dimensi $(1, 1, 1)$, dan $(x, y)$ basis representasi dua dimensi. Untuk memecah blok $(x, y)$, kita perlu satu kombinasi $ax + by$ yang hanya dikalikan bilangan oleh setiap operasi. Untuk $C_3$, itu berarti $(a, b)$ vektor eigen matriks putaran 120°; nilai eigennya $e^{\pm 2\pi i/3}$, kompleks, dengan vektor eigen $x \pm iy$. Tetapi $\sigma_1$ mengubah $x + iy$ menjadi $-x + iy = -(x - iy)$, bukan kelipatan $x + iy$. Tidak ada kombinasi yang menjadi vektor eigen bersama semua operasi, sehingga blok $(x, y)$ tak tereduksi.

**Memahami hasil.** Dalam molekul $C_{3v}$, apa pun yang bertransformasi seperti pasangan $(x, y)$ (misalnya orbital $p_x$ dan $p_y$ atom N dalam NH₃) harus berdegenerasi. Hal ini tidak berarti $p_x$ dan $p_y$ "tidak berinteraksi" dengan H; artinya, apa pun interaksinya, keduanya terpengaruh sama besar. Pecahnya degenerasi menuntut penurunan simetri, misalnya bila satu H diganti D (simetri turun ke $C_s$).
:::

::: {.contoh}
**Contoh 10.18 · Tiga orbital H dalam NH₃**

Bangun representasi dengan basis $(s_1, s_2, s_3)$, orbital 1s ketiga H dalam NH₃, lalu tunjukkan bahwa basis baru

$$
\phi_1 = \tfrac{1}{\sqrt3}(s_1 + s_2 + s_3), \quad \phi_2 = \tfrac{1}{\sqrt6}(2s_1 - s_2 - s_3), \quad \phi_3 = \tfrac{1}{\sqrt2}(s_2 - s_3)
$$

membuat matriksnya diagonal blok 1 + 2.

**Penyelesaian.** Setiap operasi hanya mempermutasikan atom H, sehingga matriksnya matriks permutasi. Dengan $C_3$ memindahkan isi posisi $j$ ke posisi $j + 1$, $\hat O_{C_3}s_1 = s_2$, $\hat O_{C_3}s_2 = s_3$, $\hat O_{C_3}s_3 = s_1$, dan $\sigma_1$ menukar $s_2 \leftrightarrow s_3$:

$$
\mathbf D(C_3) = \begin{pmatrix}0 & 0 & 1\\ 1 & 0 & 0\\ 0 & 1 & 0\end{pmatrix}, \qquad \mathbf D(\sigma_1) = \begin{pmatrix}1 & 0 & 0\\ 0 & 0 & 1\\ 0 & 1 & 0\end{pmatrix} .
$$

Dalam basis $(\phi_1, \phi_2, \phi_3)$, dengan $\mathbf U$ berisi koefisien kombinasi, perhitungan $\mathbf U^{\mathsf T}\mathbf D\mathbf U$ memberikan

$$
\mathbf D'(C_3) = \begin{pmatrix}1 & 0 & 0\\ 0 & -\tfrac12 & -\tfrac{\sqrt3}{2}\\ 0 & \tfrac{\sqrt3}{2} & -\tfrac12\end{pmatrix}, \qquad \mathbf D'(\sigma_1) = \begin{pmatrix}1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & -1\end{pmatrix} .
$$

Kombinasi $\phi_1$ tidak dicampur dengan apa pun; $\phi_2$ dan $\phi_3$ dicampur satu sama lain saja.

**Memahami hasil.** Blok 2 × 2 itu sama persis dengan blok $(x, y)$ di Contoh 10.17 (dengan $\phi_2$ berperan seperti $y$, ke arah H₁, dan $\phi_3$ seperti $-x$). Artinya pasangan $(\phi_2, \phi_3)$ bertransformasi seperti pasangan $(p_y, -p_x)$ atom N, dan $\phi_1$ seperti $p_z$ atau $2s$. Kesamaan pola transformasi inilah yang menentukan orbital N mana yang dapat bergabung dengan kombinasi H mana (subbab 10.8).
:::

::: {.contoh}
**Contoh 10.19 · Memeriksa homomorfisme dengan Python**

Tulislah program singkat yang membangun keenam matriks $C_{3v}$ dalam basis $(x, y, z)$ dan memeriksa bahwa hasil kali setiap pasangan matriks adalah salah satu dari keenam matriks itu.

**Penyelesaian.**

```python
import numpy as np
def putar(t):                     # C_n terhadap z, sudut t (radian)
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
def cermin(phi):                  # bidang vertikal memuat arah phi
    c, s = np.cos(2*phi), np.sin(2*phi)
    return np.array([[c, s, 0], [s, -c, 0], [0, 0, 1]])
d = np.radians
G = {'E': np.eye(3), 'C3': putar(d(120)), 'C3^2': putar(d(240)),
     's1': cermin(d(90)), 's2': cermin(d(210)), 's3': cermin(d(330))}
def nama(M):
    return next(k for k, v in G.items() if np.allclose(M, v))
for a in G:
    print(a.ljust(5), [nama(G[a] @ G[b]) for b in G])
```

Keluarannya adalah baris-baris tabel perkalian $C_{3v}$ di subbab 10.3, misalnya baris `C3` berisi `['C3', 'C3^2', 'E', 's3', 's1', 's2']`.

**Memahami hasil.** Fungsi `nama` selalu menemukan pasangan, artinya himpunan matriks itu tertutup terhadap perkalian, dan susunan hasilnya sama dengan tabel yang diperoleh dengan melacak atom. Pemeriksaan seperti ini berguna untuk grup besar, seperti $O_h$ dengan 48 operasi, ketika melacak atom dengan tangan mudah keliru.
:::

::: {.kuis}
**Kuis cepat 10.4**

\(a) Dalam $C_{2v}$, apa representasi satu dimensi yang basisnya orbital $3d_{xy}$ atom pusat? (b) Mengapa representasi dengan basis $(s_1, s_2)$ hidrogen H₂O disebut tereduksi? (c) Apakah molekul $C_{3v}$ dapat mempunyai orbital berdegenerasi tiga yang dipaksakan simetri?
:::
