## 9.11 Penjumlahan momentum sudut

### Mengapa perlu menjumlahkan

Konfigurasi elektron seperti $1s^2 2s^2 2p^2$ (karbon) tidak menentukan satu keadaan, melainkan sekelompok keadaan dengan energi berbeda. Dua elektron 2p dapat menempati orbital p mana pun dengan spin mana pun (selama asas Pauli dipatuhi), dan tolakan antarelektron membedakan susunan-susunan itu. Keadaan-keadaan yang dihasilkan diberi label menurut **momentum sudut total**, karena dalam atom (tanpa medan luar) momentum sudut total kekal: Hamiltonian, termasuk tolakan antarelektron, tidak berubah bila seluruh atom diputar. Untuk memberi label, kita perlu tahu bagaimana momentum sudut beberapa elektron bergabung.

### Aturan penjumlahan

Misalkan dua momentum sudut $\hat{\mathbf j}_1$ dan $\hat{\mathbf j}_2$ yang bekerja pada koordinat berbeda (dua elektron berbeda, atau orbit dan spin satu elektron), sehingga komponen-komponennya saling komut. Jumlahnya $\hat{\mathbf J} = \hat{\mathbf j}_1 + \hat{\mathbf j}_2$ memenuhi komutator momentum sudut yang sama (9.5), sehingga mempunyai bilangan kuantum $J$ dan $M$ dengan semua sifat yang sudah kita kenal. Hasil pokoknya:

$$
J = j_1 + j_2,\ j_1 + j_2 - 1,\ \ldots,\ |j_1 - j_2| , \qquad M = m_1 + m_2 . \qquad \text{(9.35)}
$$

Deret ini disebut **deret Clebsch–Gordan**. Aturan kedua jelas, karena $\hat J_z = \hat j_{1z} + \hat j_{2z}$. Aturan pertama dapat dipahami dengan menghitung. Nilai $M$ terbesar adalah $j_1 + j_2$, yang hanya dapat dicapai dengan satu cara, sehingga harus ada keadaan dengan $J = j_1 + j_2$; keadaan ini mempunyai $2J + 1$ nilai $M$. Nilai $M = j_1 + j_2 - 1$ dapat dicapai dengan dua cara; satu kombinasinya sudah dipakai oleh $J = j_1 + j_2$, sehingga yang lain harus milik $J = j_1 + j_2 - 1$. Demikian seterusnya, sampai jumlah cara berhenti bertambah di $|j_1 - j_2|$. Pemeriksaan jumlah keadaan:

$$
\sum_{J=|j_1-j_2|}^{j_1+j_2}(2J + 1) = (2j_1 + 1)(2j_2 + 1) .
$$

Dalam gambaran model vektor (subbab 6.6), dua vektor dengan panjang tertentu dijumlahkan; hanya sudut-sudut tertentu di antara keduanya yang diizinkan, sehingga panjang jumlahnya terkuantisasi.

### Basis terkopel dan tak terkopel

Ada dua cara memilih fungsi basis untuk sistem dua momentum sudut. Basis **tak terkopel** $|j_1m_1\rangle|j_2m_2\rangle$ menetapkan komponen $z$ masing-masing. Basis **terkopel** $|j_1j_2;JM\rangle$ menetapkan momentum sudut total dan komponen $z$-nya. Keduanya sah; yang lebih berguna bergantung pada Hamiltonian. Bila ada interaksi yang bergantung pada sudut antara kedua vektor, seperti kopling spin–orbit $\hat{\mathbf L}\cdot\hat{\mathbf S}$ (subbab 9.13), basis terkopel adalah fungsi eigen yang benar. Hubungan antara kedua basis diberikan oleh **koefisien Clebsch–Gordan**:

$$
|j_1j_2;JM\rangle = \sum_{m_1+m_2=M}\langle j_1m_1j_2m_2|JM\rangle\,|j_1m_1\rangle|j_2m_2\rangle . \qquad \text{(9.36)}
$$

Koefisien-koefisien ini tersedia dalam tabel dan dalam pustaka program (misalnya `sympy.physics.quantum.cg`), tetapi untuk kasus kecil mudah dihitung dengan operator tangga, seperti kita lakukan untuk dua spin di subbab 9.4 (Contoh 9.39).

### Kopling dalam atom: skema LS

Dalam atom ringan, tolakan antarelektron jauh lebih kuat daripada kopling spin–orbit. Momentum sudut orbital semua elektron karena itu bergabung lebih dulu menjadi $\mathbf L$, spin semua elektron menjadi $\mathbf S$, dan baru kemudian $\mathbf L$ dan $\mathbf S$ bergabung menjadi $\mathbf J$:

$$
\mathbf L = \sum_i\boldsymbol\ell_i , \qquad \mathbf S = \sum_i\mathbf s_i , \qquad \mathbf J = \mathbf L + \mathbf S . \qquad \text{(9.37)}
$$

Ini adalah **kopling LS** atau kopling Russell–Saunders. Untuk atom sangat berat, kopling spin–orbit setiap elektron lebih kuat, dan $\boldsymbol\ell_i$ serta $\mathbf s_i$ setiap elektron bergabung lebih dulu menjadi $\mathbf j_i$, lalu $\mathbf j_i$ dijumlahkan (**kopling jj**). Kita akan membahas atom ringan dengan kopling LS.

::: {.inti}
**Penjumlahan momentum sudut**

Dua momentum sudut $j_1$ dan $j_2$ bergabung menjadi $J = j_1 + j_2, \ldots, |j_1 - j_2|$, dengan $M = m_1 + m_2$. Jumlah keadaan tidak berubah: $\sum(2J + 1) = (2j_1 + 1)(2j_2 + 1)$. Dalam atom ringan: $\mathbf L = \sum\boldsymbol\ell_i$, $\mathbf S = \sum\mathbf s_i$, $\mathbf J = \mathbf L + \mathbf S$ (kopling LS).
:::

::: {.contoh}
**Contoh 9.38 · Konfigurasi 2p3d**

Sebuah atom tereksitasi mempunyai satu elektron 2p dan satu elektron 3d di luar kulit tertutup. (a) Nilai $L$ dan $S$ apa saja yang mungkin? (b) Berapa keadaan seluruhnya, dihitung dua cara?

**Penyelesaian.** (a) $\ell_1 = 1$, $\ell_2 = 2$: $L = 3, 2, 1$ (F, D, P). $s_1 = s_2 = \tfrac12$: $S = 1, 0$. Karena kedua elektron di subkulit berbeda (tidak ekuivalen), asas Pauli tidak membatasi kombinasi: suku-sukunya $^1$P, $^1$D, $^1$F, $^3$P, $^3$D, $^3$F.

(b) Tak terkopel: elektron p mempunyai $3 \times 2 = 6$ spin-orbital, elektron d $5 \times 2 = 10$; jumlah $6 \times 10 = 60$. Terkopel: $(2L + 1)(2S + 1)$ dijumlahkan: singlet $3 + 5 + 7 = 15$, triplet $3(3 + 5 + 7) = 45$, total 60.

**Memahami hasil.** Penghitungan ganda ini adalah alat pemeriksa yang sangat berguna: jumlah keadaan tidak bergantung pada basis. Untuk elektron yang tidak ekuivalen, semua kombinasi $L$ dan $S$ muncul. Untuk elektron ekuivalen (subkulit yang sama), asas Pauli membuang sebagian, seperti akan kita lihat di subbab 9.12.
:::

::: {.contoh}
**Contoh 9.39 · Koefisien Clebsch–Gordan untuk satu elektron p**

Gabungkan $\ell = 1$ dan $s = \tfrac12$. (a) Nilai $j$ apa saja? (b) Tuliskan $|j = \tfrac32, m_j = \tfrac32\rangle$ dan turunkan $|\tfrac32, \tfrac12\rangle$ dengan $\hat J_- = \hat L_- + \hat S_-$. (c) Cari $|\tfrac12, \tfrac12\rangle$ dari ortogonalitas.

**Penyelesaian.** (a) $j = \tfrac32, \tfrac12$; jumlah keadaan $4 + 2 = 6 = 3 \times 2$.

(b) Hanya satu kombinasi mempunyai $m_j = \tfrac32$: $|\tfrac32, \tfrac32\rangle = |1, 1\rangle\alpha$. Terapkan $\hat J_-$. Ruas kiri: $\hbar\sqrt{\tfrac32\cdot\tfrac52 - \tfrac32\cdot\tfrac12}\,|\tfrac32, \tfrac12\rangle = \sqrt3\,\hbar|\tfrac32, \tfrac12\rangle$. Ruas kanan: $\hat L_-|1, 1\rangle\alpha + |1, 1\rangle\hat S_-\alpha = \sqrt2\,\hbar|1, 0\rangle\alpha + \hbar|1, 1\rangle\beta$. Jadi

$$
|\tfrac32, \tfrac12\rangle = \sqrt{\tfrac23}\,|1, 0\rangle\alpha + \sqrt{\tfrac13}\,|1, 1\rangle\beta .
$$

(c) $|\tfrac12, \tfrac12\rangle$ dibentuk dari fungsi yang sama dan harus ortogonal: $|\tfrac12, \tfrac12\rangle = \sqrt{\tfrac13}\,|1, 0\rangle\alpha - \sqrt{\tfrac23}\,|1, 1\rangle\beta$ (tanda dipilih menurut kesepakatan Condon–Shortley).

**Memahami hasil.** Keadaan $j = \tfrac12$ sebuah elektron p bukan "orbital p dengan spin tertentu", melainkan campuran orbital $p_0$ berspin atas dan $p_{+1}$ berspin bawah. Dalam atom berat, kopling spin–orbit yang kuat membuat fungsi-fungsi terkopel seperti ini menjadi orbital yang sebenarnya: orbital $6p_{1/2}$ timbal dan bismut bersimetri bola dalam kerapatannya, berbeda dari orbital p biasa, dan perbedaan ini ikut menjelaskan "efek pasangan inert" pada unsur-unsur itu.
:::

::: {.contoh}
**Contoh 9.40 · Sudut antara L dan S**

Untuk elektron p ($\ell = 1$, $s = \tfrac12$), hitung sudut antara vektor $\mathbf L$ dan $\mathbf S$ dalam keadaan $j = \tfrac32$ dan $j = \tfrac12$, memakai $\mathbf L\cdot\mathbf S = \tfrac12[j(j + 1) - \ell(\ell + 1) - s(s + 1)]\hbar^2$.

**Penyelesaian.** $|\mathbf L| = \sqrt2\,\hbar$, $|\mathbf S| = \tfrac{\sqrt3}{2}\hbar$, hasil kali panjangnya $1{,}225\hbar^2$. Untuk $j = \tfrac32$: $\mathbf L\cdot\mathbf S = \tfrac12(\tfrac{15}{4} - 2 - \tfrac34)\hbar^2 = \tfrac12\hbar^2$, $\cos\theta = 0{,}408$, $\theta = 65{,}9°$. Untuk $j = \tfrac12$: $\mathbf L\cdot\mathbf S = \tfrac12(\tfrac34 - 2 - \tfrac34)\hbar^2 = -\hbar^2$, $\cos\theta = -0{,}816$, $\theta = 144{,}7°$.

**Memahami hasil.** "Sejajar" dan "berlawanan" dalam bahasa kimia tidak pernah berarti sudut 0° dan 180°; model vektor mengizinkan hanya sudut-sudut tertentu yang tidak ekstrem. Nilai $\mathbf L\cdot\mathbf S$ inilah yang menentukan energi kopling spin–orbit (subbab 9.13): $+\tfrac12\hbar^2$ dan $-\hbar^2$, dengan selisih $\tfrac32\hbar^2$.
:::

::: {.kuis}
**Kuis cepat 9.11**

(a) Gabungkan $j_1 = 2$ dan $j_2 = \tfrac32$: nilai $J$ apa saja, dan berapa keadaan seluruhnya? (b) Untuk tiga elektron berspin $\tfrac12$, nilai $S$ apa saja yang mungkin? (c) Mengapa dalam atom ringan $\mathbf L$ dan $\mathbf S$ dijumlahkan terpisah lebih dulu?
:::

## 9.12 Lambang suku dan aturan Hund

### Lambang suku

Keadaan atom dalam kopling LS diberi label **lambang suku**

$$
{}^{2S+1}L_J , \qquad \text{(9.38)}
$$

dengan $L$ ditulis sebagai huruf besar (S, P, D, F, G, H, ... untuk $L = 0, 1, 2, 3, 4, 5, \ldots$, sejajar dengan huruf orbital), $2S + 1$ disebut **multiplisitas** spin (singlet, doblet, triplet, kuartet, ...), dan $J$ ditulis sebagai indeks bawah. Suku $^{2S+1}L$ tanpa $J$ terdiri atas $(2L + 1)(2S + 1)$ keadaan; ketika kopling spin–orbit diperhitungkan, ia pecah menjadi **tingkat-tingkat** dengan $J$ berbeda, masing-masing berdegenerasi $2J + 1$. Contoh: $^3$P (9 keadaan) pecah menjadi $^3P_0$, $^3P_1$, $^3P_2$ ($1 + 3 + 5 = 9$).

**Kulit tertutup** mempunyai $M_L = \sum m_\ell = 0$ dan $M_S = \sum m_s = 0$ dalam satu-satunya susunan yang mungkin, sehingga $L = S = 0$: suku $^1S_0$. Gas mulia, Be, Mg, Zn, dan semua ion dengan konfigurasi kulit tertutup mempunyai keadaan dasar $^1S_0$. Karena itu, untuk menentukan suku, cukup perhatikan elektron-elektron di subkulit yang belum penuh. Subkulit yang diisi $N$ elektron dan subkulit yang kekurangan $N$ elektron ("$N$ lubang") mempunyai suku yang sama: $p^2$ dan $p^4$, $d^3$ dan $d^7$.

### Elektron ekuivalen: metode keadaan mikro

Untuk dua elektron di subkulit yang **sama**, misalnya $2p^2$, asas Pauli melarang sebagian kombinasi. Cara yang aman adalah mendaftar semua **keadaan mikro** (determinan Slater) yang diizinkan: pilih dua spin-orbital berbeda dari enam ($m_\ell = 1, 0, -1$, masing-masing $\alpha$ atau $\beta$), sehingga ada $\binom62 = 15$ keadaan mikro. Kelompokkan menurut $M_L$ dan $M_S$ (Contoh 9.41), lalu "kupas" suku-suku mulai dari $M_L$ terbesar. Hasilnya untuk $p^2$:

$$
p^2:\ {}^1D\ (5) + {}^3P\ (9) + {}^1S\ (1) = 15 . \qquad \text{(9.39)}
$$

Bandingkan dengan elektron tak ekuivalen $2p3p$, yang menghasilkan $^1$S, $^1$P, $^1$D, $^3$S, $^3$P, $^3$D (36 keadaan): asas Pauli membuang $^3$D, $^1$P, dan $^3$S. Daftar untuk konfigurasi lain yang sering dipakai:

| Konfigurasi | Suku | Keadaan mikro |
|---|---|---|
| $p^1$, $p^5$ | $^2$P | 6 |
| $p^2$, $p^4$ | $^3$P, $^1$D, $^1$S | 15 |
| $p^3$ | $^4$S, $^2$D, $^2$P | 20 |
| $d^1$, $d^9$ | $^2$D | 10 |
| $d^2$, $d^8$ | $^3$F, $^3$P, $^1$G, $^1$D, $^1$S | 45 |
| $d^5$ | $^6$S, $^4$G, $^4$F, $^4$D, $^4$P, ... (16 suku) | 252 |

### Aturan Hund

Suku mana yang paling rendah? Hund (1925) merumuskan aturan empiris yang, untuk **keadaan dasar**, hampir selalu benar:

1. Suku dengan **multiplisitas spin terbesar** ($S$ maksimum) paling rendah.
2. Di antara suku dengan $S$ itu, yang **$L$-nya terbesar** paling rendah.
3. Untuk subkulit yang terisi **kurang dari setengah**, tingkat dengan $J$ **terkecil** paling rendah; untuk yang **lebih dari setengah**, $J$ **terbesar** paling rendah. (Untuk tepat setengah, $L = 0$ dan hanya ada satu $J$.)

Aturan pertama berasal dari pertukaran: elektron berspin sejajar menempati orbital ruang berbeda dan saling menghindar (lubang Fermi), sehingga tolakan Coulomb-nya lebih kecil. Analisis yang lebih teliti menunjukkan bahwa yang sebenarnya terjadi agak lebih halus: karena elektron sejajar saling menghindar, perisai inti berkurang dan semua elektron dapat mendekat ke inti; penurunan energi terutama datang dari tarikan inti yang lebih kuat, bukan dari tolakan yang lebih kecil. Apa pun rinciannya, akarnya adalah antisimetri. Aturan kedua dapat dibayangkan secara klasik: elektron-elektron yang "berputar ke arah yang sama" (momentum sudut orbital besar) lebih jarang bertemu. Aturan ketiga berasal dari tanda kopling spin–orbit (subbab 9.13).

Cara cepat menentukan suku dasar: isi orbital $m_\ell = \ell, \ell - 1, \ldots$ satu per satu dengan spin sejajar (aturan 1), kembali dari $m_\ell = \ell$ dengan spin berlawanan setelah setengah penuh; jumlahkan $m_\ell$ untuk memperoleh $L$ (aturan 2) dan $m_s$ untuk $S$; pilih $J$ menurut aturan 3.

::: {.inti}
**Lambang suku dan aturan Hund**

Suku ${}^{2S+1}L_J$; kulit tertutup $^1S_0$. Keadaan dasar: $S$ maksimum, lalu $L$ maksimum, lalu $J = |L - S|$ (kurang dari setengah penuh) atau $J = L + S$ (lebih dari setengah penuh). Untuk elektron ekuivalen, gunakan keadaan mikro agar asas Pauli dipatuhi.
:::

::: {.contoh}
**Contoh 9.41 · Suku-suku konfigurasi $p^2$**

Daftarkan 15 keadaan mikro $p^2$ menurut $M_L$ dan $M_S$, lalu tentukan suku-sukunya.

**Penyelesaian.** Tulis setiap keadaan mikro sebagai pasangan $(m_\ell^{\pm}, m_\ell^{\pm})$, dengan $\pm$ menandai spin. Hitung jumlah keadaan mikro untuk setiap $(M_L, M_S)$ dengan $M_L \ge 0$, $M_S \ge 0$ (sisanya simetris):

| | $M_S = 1$ | $M_S = 0$ |
|---|---|---|
| $M_L = 2$ | 0 | 1: $(1^+1^-)$ |
| $M_L = 1$ | 1: $(1^+0^+)$ | 2: $(1^+0^-)$, $(1^-0^+)$ |
| $M_L = 0$ | 1: $(1^+{-1}^+)$ | 3: $(1^+{-1}^-)$, $(1^-{-1}^+)$, $(0^+0^-)$ |

Keadaan $M_L = 2$, $M_S = 0$ (tanpa pasangan $M_S = 1$) harus milik suku dengan $L = 2$, $S = 0$: $^1$D, yang mengambil satu keadaan dari setiap baris $M_L = 2, 1, 0$ pada kolom $M_S = 0$. Sisa terbesar: $M_L = 1$, $M_S = 1$, yaitu $^3$P, yang mengambil satu keadaan dari setiap $(M_L, M_S)$ dengan $M_L \le 1$, $|M_S| \le 1$. Yang tersisa hanya satu keadaan $M_L = 0$, $M_S = 0$: $^1$S. Jumlah: $5 + 9 + 1 = 15$.

**Memahami hasil.** Keadaan mikro $(1^+1^+)$, yaitu dua elektron di orbital $m_\ell = 1$ dengan spin sama, tidak ada (asas Pauli), sehingga tidak ada $^3$D. Menurut aturan Hund, $^3$P adalah suku dasar karbon, silikon, oksigen ($p^4$), dan belerang. Metode yang sama, walau lebih panjang, menghasilkan suku-suku $d^n$ yang menjadi dasar spektroskopi senyawa logam transisi (diagram Tanabe–Sugano, subbab 14.10).
:::

::: {.contoh}
**Contoh 9.42 · Spektrum karbon dan aturan Hund**

Tingkat-tingkat energi konfigurasi $2p^2$ karbon (cm⁻¹ di atas keadaan dasar): $^3P_0$ 0; $^3P_1$ 16,4; $^3P_2$ 43,4; $^1D_2$ 10 192,6; $^1S_0$ 21 648,0. Periksa ketiga aturan Hund.

**Penyelesaian.** Aturan 1: $^3$P (triplet) paling rendah, di bawah kedua singlet. Aturan 2: di antara singlet, $^1$D ($L = 2$) di bawah $^1$S ($L = 0$); aturan Hund hanya dijamin untuk suku dasar, tetapi di sini berlaku juga. Aturan 3: $p^2$ kurang dari setengah penuh, sehingga $J$ terkecil ($J = 0$) paling rendah: $^3P_0$, benar.

**Memahami hasil.** Pemecahan antarsuku (ribuan cm⁻¹, akibat tolakan antarelektron) jauh lebih besar daripada pemecahan antartingkat dalam satu suku (puluhan cm⁻¹, akibat spin–orbit), sesuai asumsi kopling LS untuk atom ringan. Keadaan $^1$D karbon, 1,26 eV di atas keadaan dasar, penting dalam kimia: karbena dan atom karbon reaktif di atmosfer antarbintang dapat berada dalam keadaan singlet atau triplet, dengan reaktivitas yang sangat berbeda.
:::

![Gambar 9.6 Suku-suku konfigurasi $2p^2$ karbon. Kiri: ramalan satu konfigurasi dengan satu parameter $F_2$ (dicocokkan pada jarak $^3$P–$^1$D, Contoh 9.51). Tengah: nilai terukur; urutan $^3$P < $^1$D < $^1$S sesuai aturan Hund. Kanan: pembesaran suku $^3$P, yang pecah oleh kopling spin–orbit menjadi $J = 0$, 1, 2 dengan selang yang hampir mengikuti aturan Landé.](fig/c_karbon.png){width=82%}

::: {.contoh}
**Contoh 9.43 · Ion logam transisi: suku dasar dan momen magnet**

Tentukan suku dasar dan jumlah elektron tak berpasangan untuk Ti²⁺ ($d^2$), Mn²⁺ ($d^5$), Fe²⁺ ($d^6$), dan Cu²⁺ ($d^9$) sebagai ion bebas. Hitung momen magnet "spin saja" $\mu = \sqrt{n(n + 2)}\,\mu_B$.

**Penyelesaian.** Isi $m_\ell = 2, 1, 0, -1, -2$:

- Ti²⁺ $d^2$: $m_\ell = 2, 1$ sejajar, $L = 3$, $S = 1$, kurang dari setengah: $J = 2$, suku $^3F_2$; $n = 2$, $\mu = 2{,}83\mu_B$.
- Mn²⁺ $d^5$: kelima orbital satu elektron sejajar, $L = 0$, $S = \tfrac52$: $^6S_{5/2}$; $n = 5$, $\mu = 5{,}92\mu_B$.
- Fe²⁺ $d^6$: lima sejajar ditambah satu berlawanan di $m_\ell = 2$: $L = 2$, $S = 2$, lebih dari setengah: $J = 4$, $^5D_4$; $n = 4$, $\mu = 4{,}90\mu_B$.
- Cu²⁺ $d^9$: satu lubang di $m_\ell = -2$, $L = 2$, $S = \tfrac12$, $J = \tfrac52$: $^2D_{5/2}$; $n = 1$, $\mu = 1{,}73\mu_B$.

**Memahami hasil.** Momen magnet terukur garam-garam Mn²⁺ dan Fe³⁺ (keduanya $d^5$) sekitar $5{,}9\mu_B$, sangat dekat dengan nilai spin saja, karena $L = 0$. Untuk ion lain, momentum sudut orbital sebagian besar "dipadamkan" oleh medan ligan (Contoh 8.42), sehingga rumus spin saja tetap merupakan pendekatan yang baik untuk logam transisi deret pertama. Dalam kompleks, medan ligan yang kuat dapat memaksa elektron berpasangan melawan aturan Hund (spin rendah); persaingan antara energi pertukaran dan pemecahan medan ligan ini adalah tema utama subbab 14.5.
:::

::: {.contoh}
**Contoh 9.44 · Aurora hijau dan merah**

Konfigurasi $2p^4$ oksigen mempunyai suku $^3$P (dasar; tingkat $J = 2, 1, 0$ di 0; 158,3; 227,0 cm⁻¹), $^1$D$_2$ (15 867,9 cm⁻¹), dan $^1$S$_0$ (33 792,6 cm⁻¹). (a) Periksa aturan Hund ketiga untuk $^3$P. (b) Hitung panjang gelombang transisi $^1$S → $^1$D dan $^1$D → $^3P_2$. (c) Mengapa keduanya terlarang, dan mengapa hanya teramati di atmosfer atas?

**Penyelesaian.** (a) $p^4$ lebih dari setengah penuh: $J$ terbesar ($J = 2$) paling rendah. Benar: urutannya **terbalik** dibandingkan karbon.

(b) $^1$S → $^1$D: $33\,792{,}6 - 15\,867{,}9 = 17\,924{,}7$ cm⁻¹, $\lambda = 557{,}9$ nm (dalam vakum; 557,7 nm di udara), hijau. $^1$D → $^3P_2$: 15 867,9 cm⁻¹, 630,2 nm (630,0 nm di udara), merah.

(c) Ketiga suku berasal dari konfigurasi yang sama, sehingga paritasnya sama (Laporte); $^1$D → $^3$P juga melanggar $\Delta S = 0$. Keadaan $^1$S hidup sekitar 0,8 s dan $^1$D sekitar 110 s. Di atmosfer bawah, atom tereksitasi bertumbukan ribuan kali sebelum sempat memancar. Hanya pada ketinggian 100–300 km udara cukup renggang.

**Memahami hasil.** Warna aurora adalah lambang suku oksigen yang kasatmata. Garis hijau terang berasal dari ketinggian sekitar 100–150 km, garis merah dari 200 km ke atas, tempat tumbukan lebih jarang lagi sehingga keadaan $^1$D yang berumur dua menit sempat memancar. Atom oksigen $^1$D juga merupakan zat antara penting dalam kimia atmosfer: dihasilkan oleh fotolisis ozon, ia bereaksi dengan H₂O membentuk radikal OH, "deterjen" atmosfer.
:::

::: {.kuis}
**Kuis cepat 9.12**

(a) Tentukan suku dasar N ($2p^3$) dan F ($2p^5$). (b) Mengapa semua konfigurasi kulit tertutup memberi $^1S_0$? (c) Berapa keadaan mikro konfigurasi $d^3$, dan apa suku dasarnya?
:::

