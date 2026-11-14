## 14.9 Lambang suku ion bebas dan pemecahannya

### Mengapa gambaran satu elektron tidak cukup

Untuk [Ti(H₂O)₆]³⁺ kita mengharapkan, dan memang melihat, satu pita d–d. Tetapi [V(H₂O)₆]³⁺ (d²) memperlihatkan dua pita spin diizinkan, di 17 800 dan 25 700 cm⁻¹, dan [Ni(H₂O)₆]²⁺ (d⁸) tiga pita, di 8500, 13 800, dan 25 300 cm⁻¹. Gambaran satu elektron hanya mengenal satu jenis lompatan, $t_{2g} \to e_g$, dengan energi $\Delta_o$. Pita-pita tambahan berasal dari **tolakan antarelektron d**. Satu konfigurasi seperti $t_{2g}^1e_g^1$ menghasilkan beberapa keadaan dengan energi berbeda, bergantung pada bagaimana kedua elektron mengatur orbital dan spinnya, persis seperti konfigurasi 2p² atom karbon menghasilkan suku $^3P$, $^1D$, dan $^1S$ (subbab 9.12).

Dalam kompleks, ada dua interaksi yang bersaing: tolakan antarelektron d, yang ukurannya dinyatakan dengan parameter Racah $B$ (sekitar 600–1100 cm⁻¹) dan $C \approx 4B$, dan medan ligan $\Delta_o$ (7000–40 000 cm⁻¹). Keduanya sebanding dalam orde besaran. Kita dapat mendekati masalah dari dua ujung: **medan lemah**, yaitu memulai dari suku ion bebas lalu menambahkan medan ligan sebagai perturbasi; atau **medan kuat**, yaitu memulai dari konfigurasi $t_{2g}^xe_g^y$ lalu menambahkan tolakan elektron. Jawaban yang benar terletak di antara keduanya dan diperoleh dengan mendiagonalkan kedua interaksi sekaligus (subbab 14.10).

### Suku ion bebas $d^n$

Untuk dua elektron d (d²), ada $\binom{10}{2} = 45$ keadaan mikro. Pengelompokannya menurut $L$ dan $S$ (subbab 9.12) menghasilkan lima suku: $^3F$, $^3P$, $^1G$, $^1D$, dan $^1S$, dengan $7 \times 3 + 3 \times 3 + 9 + 5 + 1 = 45$ keadaan. Energinya, dinyatakan dengan parameter Racah $A$, $B$, $C$ (kombinasi integral Slater $F^0$, $F^2$, $F^4$), adalah

$$
\begin{aligned}
E(^3F) &= A - 8B, & E(^3P) &= A + 7B, & E(^1D) &= A - 3B + 2C,\\
E(^1G) &= A + 4B + 2C, & E(^1S) &= A + 14B + 7C .
\end{aligned}
\qquad \text{(14.36)}
$$

Parameter $A$ menggeser semua suku sama banyak dan tidak tampak dalam spektrum. Selisih antara suku berspin sama hanya bergantung pada $B$; selisih antara suku berspin berbeda bergantung pada $B$ dan $C$. Hubungan dengan integral Slater adalah $A = F_0 - 49F_4$, $B = F_2 - 5F_4$, $C = 35F_4$, dengan $F_2 = F^2/49$ dan $F_4 = F^4/441$. Racah memilih kombinasi ini justru agar selisih suku berspin sama hanya memuat satu parameter.

Suku dasar untuk setiap $d^n$ ditentukan aturan Hund: $S$ terbesar, lalu $L$ terbesar.

| $d^n$ | d¹ | d² | d³ | d⁴ | d⁵ | d⁶ | d⁷ | d⁸ | d⁹ |
|---|---|---|---|---|---|---|---|---|---|
| Suku dasar | $^2D$ | $^3F$ | $^4F$ | $^5D$ | $^6S$ | $^5D$ | $^4F$ | $^3F$ | $^2D$ |
| Banyak keadaan mikro | 10 | 45 | 120 | 210 | 252 | 210 | 120 | 45 | 10 |

Pola $D$–$F$–$F$–$D$–$S$ berulang, karena $d^n$ dan $d^{10-n}$ mempunyai suku yang sama: $n$ elektron dan $n$ lubang tidak dapat dibedakan dari segi momentum sudut (**prinsip lubang**). Suku tereksitasi dengan spin yang sama dengan suku dasar penting bagi spektroskopi: untuk d² dan d⁸ ada $^3P$ di $15B$ di atas $^3F$; untuk d³ dan d⁷ ada $^4P$ di $15B$ di atas $^4F$; untuk d⁵ tidak ada suku sekstet lain sama sekali.

::: {.contoh}
**Contoh 14.38 · Suku-suku V³⁺ dan Ni²⁺**

(a) Dengan $B = 861$ cm⁻¹ dan $C = 4{,}42B$ untuk V³⁺ bebas, hitung energi suku-suku d² relatif terhadap $^3F$. (b) Untuk Ni²⁺ bebas, $B = 1041$ cm⁻¹. Berapa jarak $^3P$ di atas $^3F$?

**Penyelesaian.** (a) $C = 3806$ cm⁻¹. Dari (14.36), relatif terhadap $^3F$: $^1D$: $5B + 2C = 11\,920$; $^3P$: $15B = 12\,920$; $^1G$: $12B + 2C = 17\,940$; $^1S$: $22B + 7C = 45\,580$ cm⁻¹. (b) $15B = 15\,620$ cm⁻¹.

**Memahami hasil.** Tolakan antarelektron d memisahkan suku-suku sejauh puluhan ribu cm⁻¹, sebanding dengan $\Delta_o$. Suku $^3P$ adalah satu-satunya suku triplet tereksitasi, sehingga hanya transisi dari pecahan $^3F$ ke pecahan $^3F$ lainnya dan ke $^3P$ yang diizinkan spin. Untuk Ni²⁺, $^3P$ di 15 620 cm⁻¹ ion bebas akan bergeser dan bercampur dalam kompleks; itulah asal pita ketiga [Ni(H₂O)₆]²⁺ di sekitar 25 000 cm⁻¹.
:::

::: {.contoh}
**Contoh 14.39 · Menghitung keadaan mikro dan suku d³**

(a) Hitung banyaknya keadaan mikro d³. (b) Suku-suku d³ adalah $^4F$, $^4P$, $^2H$, $^2G$, $^2F$, dua $^2D$, dan $^2P$. Periksa bahwa jumlah keadaannya cocok. (c) Program diagonalisasi subbab 14.10 dengan $B = 1$, $C = 4$, dan $\Delta_o = 0$ memberi energi relatif terhadap $^4F$: $^4P$ 15, $^2G$ 16, $^2P$ dan $^2H$ 21, $^2D$ 23 dan 57, $^2F$ 36. Nyatakan dalam $B$ dan $C$.

**Penyelesaian.** (a) $\binom{10}{3} = 120$. (b) $(2S + 1)(2L + 1)$: $4 \times 7 + 4 \times 3 + 2 \times 11 + 2 \times 9 + 2 \times 7 + 2(2 \times 5) + 2 \times 3 = 28 + 12 + 22 + 18 + 14 + 20 + 6 = 120$. (c) $^4P$: $15B$; $^2G$: $4B + 3C$; $^2P$, $^2H$: $9B + 3C$; $^2F$: $24B + 3C$; kedua $^2D$: $5B + 5C + 15B \mp \sqrt{193B^2 + 8BC + 4C^2}$, yaitu $40 \mp 17$ untuk $B = 1$, $C = 4$.

**Memahami hasil.** Dua suku $^2D$ dengan $L$ dan $S$ yang sama saling bercampur, sehingga energinya mengandung akar kuadrat; suku lain dapat ditulis linear. Suku $^2G$ di $4B + 3C$ akan memberi keadaan $^2E_g$ yang menjadi asal garis laser rubi (subbab 14.11). Bahwa program numerik dan rumus analitik memberi angka yang sama adalah pemeriksaan penting bagi keduanya.
:::

### Pemecahan suku dalam medan oktahedral

Medan ligan bekerja pada koordinat ruang elektron, bukan pada spinnya. Karena itu suku dengan $L$ tertentu terpecah persis seperti himpunan orbital dengan $\ell = L$, dan **multiplisitas spinnya tidak berubah**. Rumus karakter (14.8) dengan $L$ menggantikan $\ell$ memberi tabel pemecahan yang sama untuk semua $d^n$:

| Suku | $L$ | Dalam $O_h$ |
|---|---|---|
| $S$ | 0 | $A_{1g}$ |
| $P$ | 1 | $T_{1g}$ |
| $D$ | 2 | $E_g + T_{2g}$ |
| $F$ | 3 | $A_{2g} + T_{1g} + T_{2g}$ |
| $G$ | 4 | $A_{1g} + E_g + T_{1g} + T_{2g}$ |
| $H$ | 5 | $E_g + 2T_{1g} + T_{2g}$ |
| $I$ | 6 | $A_{1g} + A_{2g} + E_g + T_{1g} + 2T_{2g}$ |

: Tabel 14.7 Pemecahan suku Russell–Saunders dalam medan oktahedral. Semua pecahan diberi label $g$ karena konfigurasi $d^n$ genap terhadap inversi.

Perhatikan bahwa suku $P$ ($L = 1$) tidak terpecah, karena orbital p tidak terpecah (Contoh 14.3). Huruf besar dipakai untuk keadaan banyak elektron, dan multiplisitas spin ditulis di kiri atas: $^3F$ terpecah menjadi $^3A_{2g}$, $^3T_{1g}$, dan $^3T_{2g}$.

Teori grup memberi jenis dan banyaknya pecahan; energinya memerlukan perhitungan. Untuk suku $D$ hasilnya sederhana. Ion d¹ mempunyai $^2D \to {}^2T_{2g}$ ($-4Dq$) + $^2E_g$ ($+6Dq$), persis pemecahan orbital. Untuk suku $F$ d², perhitungan (yang di sini tidak diuraikan) memberi

$$
{}^3T_{1g}(F):\ -6Dq, \qquad {}^3T_{2g}:\ +2Dq, \qquad {}^3A_{2g}:\ +12Dq . \qquad \text{(14.37)}
$$

Pusat berat berbobot degenerasi tetap: $3(-6) + 3(2) + 1(12) = 0$.

### Aturan pembalikan

Dua aturan sederhana menghubungkan semua $d^n$:

1. **Lubang.** $d^{10-n}$ mempunyai pemecahan yang sama dengan $d^n$ tetapi **terbalik**. Untuk d¹, satu elektron lebih suka $t_{2g}$, sehingga $^2T_{2g}$ di bawah. Untuk d⁹, satu lubang lebih suka orbital yang energinya tertinggi bagi elektron, yaitu $e_g$; keadaan dasarnya $^2E_g$.
2. **Geometri.** Pemecahan tetrahedral berlawanan tanda dengan oktahedral ($\Delta_t = -\tfrac49\Delta_o$ dalam bentuk operator). Jadi d¹ tetrahedral berperilaku seperti d⁹ oktahedral.
3. **Setengah penuh.** Suku spin tinggi $d^{n+5}$ berperilaku seperti $d^n$: lima elektron berspin sama yang mengisi semua orbital membentuk teras bersetangkup bola. d⁶ spin tinggi ($^5D$) seperti d¹, d⁷ spin tinggi ($^4F$) seperti d², d⁸ seperti d³, d⁹ seperti d⁴.

Dengan ketiga aturan ini, pola pemecahan suku dasar hanya ada dua macam: pola $D$ (d¹, d⁴, d⁶, d⁹) dan pola $F$ (d², d³, d⁷, d⁸), masing-masing dengan arah normal atau terbalik. d⁵ spin tinggi istimewa: suku dasar $^6S$ menjadi $^6A_{1g}$ yang tidak terpecah, dan **tidak ada keadaan sekstet lain**. Semua transisi d–d Mn²⁺ dan Fe³⁺ spin tinggi terlarang spin. Inilah jawaban pertanyaan pembuka: larutan Mn²⁺ hampir tak berwarna karena semua pita d–d-nya terlarang ganda.

::: {.contoh}
**Contoh 14.40 · Lambang keadaan dasar**

Tentukan lambang keadaan dasar dalam medan oktahedral untuk [Cr(H₂O)₆]³⁺, [Fe(H₂O)₆]²⁺, [Mn(H₂O)₆]²⁺, [Co(H₂O)₆]²⁺, [Ni(H₂O)₆]²⁺, [Cu(H₂O)₆]²⁺, [Co(NH₃)₆]³⁺, dan [Fe(CN)₆]³⁻. Untuk masing-masing, ramalkan apakah ada sumbangan orbital pada momen magnet dan apakah ada efek Jahn–Teller.

**Penyelesaian.** Dengan konfigurasi kuat ($t_{2g}^xe_g^y$) atau suku dasar ion bebas dan aturan pembalikan:

| Kompleks | Konfigurasi | Keadaan dasar | Sumbangan orbital | Jahn–Teller |
|---|---|---|---|---|
| [Cr(H₂O)₆]³⁺ | $t_{2g}^3$ | $^4A_{2g}$ | tidak | tidak |
| [Fe(H₂O)₆]²⁺ | $t_{2g}^4e_g^2$ | $^5T_{2g}$ | ya | lemah |
| [Mn(H₂O)₆]²⁺ | $t_{2g}^3e_g^2$ | $^6A_{1g}$ | tidak | tidak |
| [Co(H₂O)₆]²⁺ | $t_{2g}^5e_g^2$ | $^4T_{1g}$ | ya, besar | lemah |
| [Ni(H₂O)₆]²⁺ | $t_{2g}^6e_g^2$ | $^3A_{2g}$ | tidak | tidak |
| [Cu(H₂O)₆]²⁺ | $t_{2g}^6e_g^3$ | $^2E_g$ | tidak | kuat |
| [Co(NH₃)₆]³⁺ | $t_{2g}^6$ | $^1A_{1g}$ | tidak (diamagnetik) | tidak |
| [Fe(CN)₆]³⁻ | $t_{2g}^5$ | $^2T_{2g}$ | ya | lemah |

**Memahami hasil.** Satu lambang memadatkan banyak informasi. Huruf $A$ berarti tidak berdegenerasi orbital: momen magnet mendekati spin saja dan tidak ada distorsi Jahn–Teller. $E$ berarti degenerasi ganda dari orbital $e_g$: Jahn–Teller kuat, tetapi momentum sudut orbital padam. $T$ berarti degenerasi tiga: momentum sudut orbital tidak padam, dan efek Jahn–Teller lemah. Pengamatan subbab 14.5 dan 14.6 kini terangkum dalam satu tabel.
:::

### Pendekatan medan kuat

Dari ujung yang lain, mulailah dengan konfigurasi. Untuk d² oktahedral ada tiga konfigurasi: $t_{2g}^2$ ($-8Dq$), $t_{2g}^1e_g^1$ ($+2Dq$), dan $e_g^2$ ($+12Dq$). Setiap konfigurasi menghasilkan beberapa keadaan. Kesetangkupan ruangnya adalah hasil kali langsung kesetangkupan kedua orbital, dan asas Pauli menentukan multiplisitas spin yang diperbolehkan:

$$
\begin{aligned}
t_{2g}^2:&\quad T_{2g} \otimes T_{2g} = A_{1g} + E_g + T_{1g} + T_{2g} \ \to\ {}^3T_{1g} + {}^1A_{1g} + {}^1E_g + {}^1T_{2g},\\
t_{2g}^1e_g^1:&\quad T_{2g} \otimes E_g = T_{1g} + T_{2g} \ \to\ {}^3T_{1g} + {}^3T_{2g} + {}^1T_{1g} + {}^1T_{2g},\\
e_g^2:&\quad E_g \otimes E_g = A_{1g} + A_{2g} + E_g \ \to\ {}^3A_{2g} + {}^1A_{1g} + {}^1E_g .
\end{aligned}
\qquad \text{(14.38)}
$$

Untuk konfigurasi $t_{2g}^1e_g^1$, kedua elektron berada di orbital berbeda, sehingga setiap kesetangkupan ruang boleh dipasangkan dengan spin singlet maupun triplet. Untuk $t_{2g}^2$ dan $e_g^2$, kedua elektron berada dalam himpunan orbital yang sama, dan fungsi total harus antisetangkup: bagian ruang yang **setangkup** terhadap pertukaran elektron berpasangan dengan spin singlet, bagian **antisetangkup** dengan triplet.

Pemeriksaannya: triplet medan kuat adalah dua $^3T_{1g}$, satu $^3T_{2g}$, dan satu $^3A_{2g}$, sama persis dengan pecahan $^3F$ ($^3A_{2g} + {}^3T_{1g} + {}^3T_{2g}$) ditambah $^3P$ ($^3T_{1g}$) dari medan lemah. Singlet medan kuat: dua $^1A_{1g}$, dua $^1E_g$, satu $^1T_{1g}$, dua $^1T_{2g}$; medan lemah dari $^1G$, $^1D$, dan $^1S$: $(A_{1g} + E_g + T_{1g} + T_{2g}) + (E_g + T_{2g}) + A_{1g}$, juga sama. Keadaan tidak hilang atau bertambah dalam perjalanan dari satu ujung ke ujung lain; mereka hanya berpindah energi.

::: {.contoh}
**Contoh 14.41 · Bagian setangkup dan antisetangkup $T_{2g} \otimes T_{2g}$**

Karakter bagian setangkup dan antisetangkup hasil kali langsung $\Gamma \otimes \Gamma$ adalah $\chi_\pm(R) = \tfrac12[\chi(R)^2 \pm \chi(R^2)]$. Dalam grup $O$ (kelas $E$, $8C_3$, $6C_2'$, $6C_4$, $3C_2$), $T_2$ mempunyai karakter 3, 0, 1, −1, −1. Tentukan kedua bagian dan simpulkan keadaan $t_{2g}^2$.

**Penyelesaian.** $\chi(R)^2$: 9, 0, 1, 1, 1. Untuk $\chi(R^2)$ perlu kelas $R^2$: $E^2 = E$; $C_3^2$ di kelas $C_3$; $C_2'^2 = E$; $C_4^2 = C_2$; $C_2^2 = E$. Jadi $\chi(R^2)$ = 3, 0, 3, −1, 3. Maka

- setangkup: $\tfrac12(9 + 3, 0 + 0, 1 + 3, 1 - 1, 1 + 3)$ = 6, 0, 2, 0, 2;
- antisetangkup: $\tfrac12(9 - 3, 0, 1 - 3, 1 + 1, 1 - 3)$ = 3, 0, −1, 1, −1.

Bagian antisetangkup adalah tepat $T_1$. Bagian setangkup (dimensi 6) direduksi menjadi $A_1 + E + T_2$ (periksa: $1 + 2 + 3 = 6$; karakter pada $C_2'$: $1 + 0 + 1 = 2$; pada $C_2$: $1 + 2 - 1 = 2$).

**Memahami hasil.** Karena fungsi spin triplet setangkup, bagian ruangnya harus antisetangkup: $^3T_{1g}$. Fungsi spin singlet antisetangkup, sehingga bagian ruangnya setangkup: $^1A_{1g}$, $^1E_g$, $^1T_{2g}$. Inilah bentuk teori grup dari aturan Hund dan asas Pauli. Keadaan dasar d² oktahedral, $^3T_{1g}$, dengan demikian terbukti dari dua arah: dari $^3F$ medan lemah dan dari $t_{2g}^2$ medan kuat.
:::

### Diagram korelasi

Gambar 14.8 menghubungkan kedua ujung untuk d². Di kiri, medan ligan nol: suku-suku ion bebas. Di kanan, tolakan elektron nol: tiga konfigurasi berjarak $10Dq$. Di antaranya, setiap keadaan dihitung dengan diagonalisasi lengkap. Garis-garis berkesetangkupan dan berspin sama **tidak pernah berpotongan** (aturan tak-silang, subbab 11.9 untuk analognya pada molekul diatom): keduanya saling tolak dan "membelok". Inilah yang terjadi pada dua $^3T_{1g}$: yang bawah berasal dari $^3F$ dan berakhir di $t_{2g}^2$, yang atas dari $^3P$ dan berakhir di $t_{2g}^1e_g^1$.

![Gambar 14.8 Diagram korelasi d² oktahedral dari medan lemah (kiri, suku ion bebas) ke medan kuat (kanan, konfigurasi $t_{2g}^2$, $t_{2g}e_g$, $e_g^2$). Garis biru: triplet; garis jingga: singlet. Parameter dalam perhitungan diubah serentak dari ($B$, $Dq$) = (861, 0) menuju (0, 2000) cm⁻¹ dengan $C = 4{,}42B$.](fig/c_korelasi.png){width=88%}

::: {.kuis}
**Kuis cepat 14.9**

Suku apa yang menjadi keadaan dasar d⁵ spin rendah oktahedral ($t_{2g}^5$)? Apakah transisi pertamanya diizinkan spin?
:::

## 14.10 Diagram Orgel dan Tanabe–Sugano

### Masalah dua keadaan $T_{1g}$

Pemecahan medan lemah (14.37) hanya berlaku bila $Dq \ll B$. Begitu medan ligan sebanding dengan tolakan elektron, kedua keadaan $^3T_{1g}$, satu dari $^3F$ dan satu dari $^3P$, bercampur karena berkesetangkupan sama. Matriks Hamiltonian pada basis keduanya, dengan energi relatif terhadap $^3F$ ion bebas, adalah

$$
\begin{pmatrix}
-6Dq & 4Dq\\
4Dq & 15B
\end{pmatrix}
\qquad (\text{d}^2,\ \text{d}^7\ \text{spin tinggi}) , \qquad \text{(14.39)}
$$

dengan unsur di luar diagonal $4Dq$ yang berasal dari medan ligan yang menghubungkan kedua suku. Untuk d³ dan d⁸ (pola terbalik), tanda $Dq$ dibalik: diagonal $+6Dq$ dan $15B$, dengan $^3A_{2g}$ ($^4A_{2g}$ untuk d³) sebagai keadaan dasar di $-12Dq$ dan $^3T_{2g}$ di $-2Dq$. Nilai eigen (14.39):

$$
E_\pm = \tfrac12(15B - 6Dq) \pm \tfrac12\sqrt{(15B + 6Dq)^2 + 64Dq^2} . \qquad \text{(14.40)}
$$

Akar bawah adalah $^3T_{1g}(F)$, akar atas $^3T_{1g}(P)$. Keduanya saling menolak; jarak terdekatnya tidak pernah lebih kecil dari $2 \times 4Dq$ ketika diagonalnya hampir sama. Kombinasi (14.37), (14.39), dan (14.40) memberikan rumus lengkap pita spin diizinkan untuk keempat ion pola $F$.

::: {.inti}
**Rumus pita spin diizinkan pola $F$**

d³ dan d⁸ oktahedral (keadaan dasar $A_{2g}$):
$$
\nu_1 = 10Dq,\qquad \nu_{2,3} = 12Dq + E_\mp,\qquad E_\mp = \tfrac12(15B + 6Dq) \mp \tfrac12\sqrt{(15B - 6Dq)^2 + 64Dq^2},
$$
sehingga $\nu_2 + \nu_3 = 30Dq + 15B$. d² dan d⁷ spin tinggi (keadaan dasar $T_{1g}(F)$): $\nu_1 = 2Dq - E_-$, $\nu_2 = E_+ - E_-$, $\nu_3 = 12Dq - E_-$, dengan $E_\pm$ dari (14.40).
:::

![Gambar 14.9 Diagram Orgel untuk ion pola $F$. Kanan: d² dan d⁷ spin tinggi oktahedral (juga d³ dan d⁸ tetrahedral). Kiri: d³ dan d⁸ oktahedral (juga d² dan d⁷ tetrahedral). Energi dihitung dari (14.39) dengan $B = 860$ cm⁻¹. Garis putus-putus menunjukkan kedua $T_1$ seandainya tidak bercampur; pencampuran membuat keduanya saling menjauh.](fig/c_orgel.png){width=88%}

**Diagram Orgel** (Gambar 14.9) menggambarkan energi keadaan-keadaan berspin sama dengan suku dasar sebagai fungsi $Dq$, dengan ion pola normal di satu sisi dan pola terbalik di sisi lain. Diagram ini sederhana dan cukup untuk menafsirkan pita spin diizinkan kompleks spin tinggi. Kelemahannya: ia tidak memuat keadaan berspin lain, sehingga tidak dapat menerangkan pita terlarang spin atau peralihan ke spin rendah.

::: {.contoh}
**Contoh 14.42 · Menentukan $Dq$ dan $B$ untuk [Ni(H₂O)₆]²⁺**

Tiga pita [Ni(H₂O)₆]²⁺ berada di 8500, 13 800, dan 25 300 cm⁻¹. (a) Tentukan $Dq$ dan $B$. (b) Ramalkan kembali $\nu_2$ dan $\nu_3$ dari nilai itu. (c) Hitung rasio nefelauksetik ($B_\text{bebas} = 1041$ cm⁻¹).

**Penyelesaian.** (a) Untuk d⁸, $\nu_1 = 10Dq$, sehingga $Dq = 850$ cm⁻¹. Dari jumlah $\nu_2 + \nu_3 = 30Dq + 15B$: $15B = 39\,100 - 25\,500 = 13\,600$, $B = 907$ cm⁻¹.

(b) Dengan $Dq = 850$ dan $B = 907$: $15B + 6Dq = 18\,705$, $15B - 6Dq = 8505$, $\sqrt{8505^2 + 64(850)^2} = \sqrt{7{,}234 \times 10^7 + 4{,}624 \times 10^7} = 10\,889$. Jadi $E_\mp = 9353 \mp 5445$: 3908 dan 14 797. Maka $\nu_2 = 10\,200 + 3908 = 14\,110$ dan $\nu_3 = 10\,200 + 14\,797 = 24\,990$ cm⁻¹.

(c) $\beta = 907/1041 = 0{,}87$.

**Memahami hasil.** Ramalan meleset sekitar 300 cm⁻¹ untuk $\nu_2$ dan $\nu_3$, karena hanya dua parameter yang dipakai untuk tiga pita, dan karena kopling spin–orbit Ni²⁺ ($\lambda = -315$ cm⁻¹) ikut menggeser dan memecah pita. Pita $\nu_2$ pada spektrum [Ni(H₂O)₆]²⁺ memang tampak berpuncak ganda: $^3T_{1g}(F)$ hampir berdegenerasi dengan keadaan singlet $^1E_g$, dan keduanya bercampur melalui kopling spin–orbit. Ketelitian 2% sudah cukup untuk banyak keperluan, dan $\beta = 0{,}87$ menunjukkan bahwa ikatan Ni–O cukup ionik.
:::

::: {.contoh}
**Contoh 14.43 · [V(H₂O)₆]³⁺: pita pertama bukan $\Delta_o$**

[V(H₂O)₆]³⁺ menyerap di 17 800 dan 25 700 cm⁻¹ (pita ketiga, $^3A_{2g}$, tertutup pita transfer muatan). Tentukan $Dq$ dan $B$ dengan rumus d², lalu bandingkan $10Dq$ dengan $\nu_1$.

**Rencana.** Dua persamaan taklinear $\nu_1 = 2Dq - E_-$ dan $\nu_2 = E_+ - E_-$ dengan dua tak diketahui. Selesaikan secara numerik.

**Penyelesaian.**

```python
import numpy as np
from scipy.optimize import fsolve

def d2(Dq, B):
    Em, Ep = np.linalg.eigvalsh([[-6*Dq, 4*Dq], [4*Dq, 15*B]])
    return 2*Dq - Em, Ep - Em, 12*Dq - Em        # nu1, nu2, nu3

Dq, B = fsolve(lambda p: np.array(d2(*p)[:2]) - [17800, 25700], [1800, 700])
print(Dq, B, d2(Dq, B))
```

Hasilnya $Dq = 1910$ cm⁻¹, $B = 613$ cm⁻¹, dan $\nu_3 = 36\,900$ cm⁻¹. Jadi $\Delta_o = 19\,100$ cm⁻¹, sedangkan $\nu_1 = 17\,800$ cm⁻¹. Rasio nefelauksetik $613/861 = 0{,}71$.

**Memahami hasil.** Pita pertama 1300 cm⁻¹ di bawah $\Delta_o$. Keadaan dasar $^3T_{1g}(F)$ telah terdorong ke bawah oleh pencampurannya dengan $^3T_{1g}(P)$, sehingga transisi pertama tidak lagi tepat $8Dq$ atau $10Dq$. Inilah alasan nilai $\Delta_o$ untuk V³⁺ dalam Tabel 14.1 adalah 19 100 cm⁻¹, bukan 17 800. Ramalan $\nu_3 = 36\,900$ cm⁻¹ (271 nm) berada di ultraviolet, tempat pita transfer muatan yang jauh lebih kuat menutupinya.
:::

::: {.contoh}
**Contoh 14.44 · Krom(III): parameter dari dua pita**

[Cr(H₂O)₆]³⁺ menyerap di 17 400 dan 24 600 cm⁻¹; [Cr(NH₃)₆]³⁺ di 21 550 dan 28 500 cm⁻¹. Tentukan $Dq$ dan $B$ untuk keduanya ($B_\text{bebas} = 918$ cm⁻¹).

**Penyelesaian.** Untuk d³, $\nu_1 = 10Dq$: $Dq = 1740$ dan 2155 cm⁻¹. $\nu_2 = 12Dq + E_-$ memberi satu persamaan untuk $B$, yang diselesaikan dengan bagi dua atau `brentq`: [Cr(H₂O)₆]³⁺ $B = 729$ cm⁻¹ ($\beta = 0{,}79$); [Cr(NH₃)₆]³⁺ $B = 657$ cm⁻¹ ($\beta = 0{,}72$). Pita ketiga diramalkan di 38 500 dan 46 000 cm⁻¹.

**Memahami hasil.** Penggantian air oleh amonia menaikkan $\Delta_o$ 24% dan menurunkan $B$ 10%: amonia adalah donor σ yang lebih kuat **dan** lebih kovalen. Kedua nilai $\beta$ sangat cocok dengan rumus Jørgensen (Contoh 14.32). Pita ketiga ($^4A_{2g} \to {}^4T_{1g}(P)$) di ultraviolet jauh dan biasanya tidak teramati.
:::

### Diagram Tanabe–Sugano

Pada 1954 Tanabe dan Sugano menyelesaikan masalah ini secara lengkap untuk semua $d^n$: matriks Hamiltonian tolakan elektron ditambah medan ligan didiagonalkan untuk **semua** keadaan, semua spin. Hasilnya disajikan dengan dua pilihan cerdik:

1. Energi dan medan ligan dinyatakan dalam satuan $B$: sumbu tegak $E/B$, sumbu datar $\Delta_o/B$. Dengan $C/B$ ditetapkan (sekitar 4,5), satu diagram berlaku untuk semua ion dengan $d^n$ yang sama.
2. Energi selalu diukur dari **keadaan dasar**, sehingga keadaan dasar menjadi sumbu datar dan energi transisi dibaca langsung sebagai tinggi garis di atas sumbu.

Untuk d⁴–d⁷, keadaan dasar berganti pada $\Delta_o/B$ tertentu (persilangan spin, subbab 14.5); pada titik itu semua garis patah karena acuan nolnya berganti. Gambar 14.10 memperlihatkan diagram untuk d², d³, d⁶, dan d⁸, yang kita hitung sendiri dengan program di bawah.

![Gambar 14.10 Diagram Tanabe–Sugano untuk d² ($C/B = 4{,}42$), d³ ($C/B = 4{,}5$), d⁶ ($C/B = 4{,}8$), dan d⁸ ($C/B = 4{,}71$), dihitung dengan diagonalisasi lengkap kulit $d^n$. Garis tebal: keadaan berspin sama dengan keadaan dasar (spin diizinkan); garis tipis: keadaan berspin lain. Pada d⁶, garis tegak di $\Delta_o/B = 20{,}0$ menandai peralihan dari $^5T_{2g}$ ke $^1A_{1g}$.](fig/c_tanabe.png){width=96%}

::: {.contoh}
**Contoh 14.45 · Program Tanabe–Sugano**

Tulis program Python yang mendiagonalkan Hamiltonian kulit $d^n$ dengan tolakan elektron (parameter $B$, $C$) dan medan oktahedral ($Dq$), lalu memeriksa (a) suku-suku d² ion bebas dan (b) titik persilangan spin d⁶ dengan $C/B = 4{,}8$.

**Rencana.** Basisnya determinan Slater dari sepuluh spin-orbital $d_m\alpha$, $d_m\beta$ dengan $m = 2, \ldots, -2$ (subbab 9.6). Integral dua elektron di antara orbital kompleks diberikan oleh koefisien Gaunt $c^k$ dan integral Slater $F^k$, dengan $F^2 = 49B + 7C$, $F^4 = 63C/5$, dan $A = 0$. Medan oktahedral pada basis $m$: diagonal $Dq$, $-4Dq$, $6Dq$, $-4Dq$, $Dq$ dan $\langle 2|V|{-2}\rangle = 5Dq$. Hamiltonian dibangun dengan operator cipta–musnah. Spin setiap tingkat ditentukan dengan membandingkan sektor $M_S$: tingkat dengan spin $S$ muncul di semua sektor $|M_S| \le S$.

**Penyelesaian.**

```python
import numpy as np, itertools
from functools import lru_cache
from sympy.physics.wigner import wigner_3j

M = [2, 1, 0, -1, -2]
SO = [(m, s) for s in (1, -1) for m in M]            # 10 spin-orbital

@lru_cache(None)
def ck(k, m1, m2):                                    # koefisien Gaunt c^k(2m1, 2m2)
    return float((-1)**m1 * 5 * wigner_3j(2, k, 2, 0, 0, 0)
                 * wigner_3j(2, k, 2, -m1, m1 - m2, m2))

def integral(B, C, Dq):
    F = {2: 49*B + 7*C, 4: 63*C/5}
    h, g = np.zeros((10, 10)), np.zeros((10,) * 4)
    for p, (m1, s1) in enumerate(SO):
        for q, (m2, s2) in enumerate(SO):
            if s1 == s2 and m1 == m2:
                h[p, q] = {2: 1, 1: -4, 0: 6, -1: -4, -2: 1}[m1] * Dq
            if s1 == s2 and abs(m1) == 2 and m2 == -m1:
                h[p, q] = 5 * Dq
    for p, q, r, t in itertools.product(range(10), repeat=4):
        (m1, s1), (m2, s2), (m3, s3), (m4, s4) = SO[p], SO[q], SO[r], SO[t]
        if s1 == s3 and s2 == s4 and m1 + m2 == m3 + m4:
            g[p, q, r, t] = sum(ck(k, m1, m3) * ck(k, m4, m2) * F[k] for k in (2, 4))
    return h, g

def operasi(ops, det):                    # terapkan a+ / a dari kanan ke kiri
    d, tanda = list(det), 1
    for p, cipta in reversed(ops):
        if cipta == (p in d):
            return 0, None
        i = sum(x < p for x in d)
        tanda *= (-1)**i
        d.insert(i, p) if cipta else d.remove(p)
    return tanda, tuple(d)

def matriks(n, h, g, dua_Ms):
    dets = [d for d in itertools.combinations(range(10), n)
            if sum(SO[p][1] for p in d) == dua_Ms]
    idx = {d: i for i, d in enumerate(dets)}
    H = np.zeros((len(dets), len(dets)))
    for d in dets:
        for p, q in itertools.product(range(10), repeat=2):        # satu elektron
            if h[p, q]:
                t, d2 = operasi([(p, 1), (q, 0)], d)
                if t: H[idx[d2], idx[d]] += t * h[p, q]
        for r, s in itertools.permutations(d, 2):                  # dua elektron
            for p, q in itertools.product(range(10), repeat=2):
                if g[p, q, r, s]:
                    t, d2 = operasi([(p, 1), (q, 1), (s, 0), (r, 0)], d)
                    if t: H[idx[d2], idx[d]] += 0.5 * t * g[p, q, r, s]
    return H

def tingkat(n, B, C, Dq):
    """Daftar (energi relatif keadaan dasar, S), satu entri per keadaan ruang."""
    h, g = integral(B, C, Dq)
    sek = {t: np.sort(np.linalg.eigvalsh(matriks(n, h, g, t)))
           for t in range(n % 2, min(n, 10 - n) + 1, 2)}
    hasil = []
    for t, E in sek.items():
        atas = list(sek.get(t + 2, []))
        for e in E:
            j = next((j for j, x in enumerate(atas) if abs(x - e) < 1e-6), None)
            if j is None: hasil.append((e, t / 2))
            else: atas.pop(j)
    E0 = min(e for e, S in hasil)
    return sorted((round(e - E0, 1), S) for e, S in hasil)

print(sorted(set(tingkat(2, 1.0, 4.0, 0.0))))       # (a)
for D in (19.9, 20.1):                                # (b) Delta_o/B di sekitar 20
    print(D, tingkat(6, 1.0, 4.8, D/10)[:2])
```

(a) Keluarannya $(0, S{=}1)$, $(13, 0)$, $(15, 1)$, $(20, 0)$, $(50, 0)$: dengan $B = 1$ dan $C = 4$, relatif terhadap $^3F$, (14.36) memberi $^1D$ = 13, $^3P$ = 15, $^1G$ = 20, $^1S$ = 50. Tepat. (b) Pada $\Delta_o/B = 19{,}9$ keadaan dasar berspin 2; pada 20,1 berspin 0. Persilangan d⁶ terletak di $\Delta_o/B = 20{,}0$.

**Memahami hasil.** Program sekitar enam puluh baris ini memuat seluruh teori subbab 14.9–14.10: aturan Condon–Slater (subbab 9.14) terkandung dalam operasi cipta–musnah, suku Russell–Saunders muncul dengan sendirinya ketika $Dq = 0$, dan diagram Tanabe–Sugano diperoleh dengan mengulang perhitungan untuk banyak nilai $Dq$. Matriks terbesar (d⁵, $M_S = \tfrac12$) berukuran 100 × 100, sehingga seluruh diagram selesai dalam beberapa detik. Program yang sama, ditambah kopling spin–orbit dan medan bersetangkup rendah, adalah inti perangkat lunak analisis spektrum kompleks yang dipakai di laboratorium spektroskopi.
:::

### Membaca diagram Tanabe–Sugano

Ada tiga keterampilan yang perlu dilatih:

1. **Mencari pita spin diizinkan.** Dari sumbu datar (keadaan dasar), naik tegak lurus pada nilai $\Delta_o/B$ kompleks. Setiap garis tebal yang dilintasi adalah keadaan tereksitasi berspin sama; tingginya $E/B$ adalah energi pita dalam satuan $B$.
2. **Mencocokkan spektrum.** Dari dua pita teramati, hitung rasio energinya. Cari $\Delta_o/B$ yang memberi rasio yang sama pada diagram. Dari tinggi garis, hitung $B$; dari $\Delta_o/B$, hitung $\Delta_o$.
3. **Membaca lebar pita.** Garis yang curam (energinya bergantung kuat pada $\Delta_o$) menghasilkan pita lebar, karena getaran ikatan membuat $\Delta_o$ berfluktuasi. Garis yang sejajar keadaan dasar menghasilkan pita tajam (subbab 14.11).

::: {.contoh}
**Contoh 14.46 · [Co(NH₃)₆]³⁺ spin rendah**

[Co(NH₃)₆]³⁺ (d⁶ spin rendah, keadaan dasar $^1A_{1g}$) menyerap di 21 000 cm⁻¹ ($^1A_{1g} \to {}^1T_{1g}$) dan 29 500 cm⁻¹ ($\to {}^1T_{2g}$). (a) Dengan hampiran medan kuat, $E(^1T_{1g}) \approx \Delta_o - C$ dan $E(^1T_{2g}) \approx \Delta_o + 16B - C$, taksir $B$ dan $\Delta_o$ dengan $C = 4{,}8B$. (b) Dengan program Contoh 14.45 (dan pencocokan numerik dua pita), diperoleh $Dq = 2303$ cm⁻¹ dan $B = 635$ cm⁻¹. Bandingkan. (c) Program yang sama meramalkan keadaan $^3T_{1g}$ terendah di 14 500 cm⁻¹. Apa artinya?

**Penyelesaian.** (a) Selisih kedua pita $16B = 8500$ cm⁻¹, $B = 531$ cm⁻¹, $C = 2550$ cm⁻¹, $\Delta_o \approx 21\,000 + 2550 = 23\,550$ cm⁻¹. (b) Program memberi $\Delta_o = 23\,030$ cm⁻¹ dan $B = 635$ cm⁻¹; selisih dengan hampiran: $\Delta_o$ 2%, $B$ 20%. Rasio nefelauksetik $635/1065 = 0{,}60$. (c) Ada pita terlarang spin $^1A_{1g} \to {}^3T_{1g}$ sekitar 14 500 cm⁻¹ (690 nm), yang sangat lemah.

**Memahami hasil.** Hampiran medan kuat memberi $\Delta_o$ yang baik tetapi $B$ yang kurang tepat, karena keadaan $^1T_{2g}$ bercampur dengan keadaan $^1T_{2g}$ dari konfigurasi lain. $\beta = 0{,}60$ jauh lebih kecil daripada Cr³⁺ dan Ni²⁺: Co(III) membentuk ikatan sangat kovalen dengan amonia, sesuai nilai $k(\text{Co}^{3+}) = 0{,}33$ yang besar dalam rumus Jørgensen. Pita terlarang spin memang teramati di sekitar 13 000–15 000 cm⁻¹ dengan $\varepsilon$ kurang dari 1 L mol⁻¹ cm⁻¹.
:::

::: {.contoh}
**Contoh 14.47 · [Mn(H₂O)₆]²⁺: pita tajam di tengah pita lebar**

Spektrum [Mn(H₂O)₆]²⁺ yang sangat lemah ($\varepsilon < 0{,}05$) memperlihatkan pita di 18 900 ($^4T_{1g}(G)$), 23 100 ($^4T_{2g}(G)$), 25 000 (tajam; $^4A_{1g}$, $^4E_g(G)$), 27 900 ($^4T_{2g}(D)$), dan 29 700 cm⁻¹ (tajam; $^4E_g(D)$). Dua pita tajam itu tidak bergantung pada $\Delta_o$: $E = 10B + 5C$ dan $17B + 5C$. (a) Tentukan $B$ dan $C$. (b) Program Contoh 14.45 dengan nilai ini dan $Dq = 840$ cm⁻¹ meramalkan 19 230, 22 530, 25 000, 27 930, dan 29 700 cm⁻¹. Nilailah kecocokannya.

**Penyelesaian.** (a) $7B = 29\,700 - 25\,000 = 4700$, $B = 671$ cm⁻¹; $5C = 25\,000 - 6710$, $C = 3660$ cm⁻¹; $C/B = 5{,}45$. (b) Selisih dengan pengamatan: +330, −570, 0, +30, 0 cm⁻¹. Kedua pita tajam cocok tepat (dipakai untuk mencocokkan); pita-pita lebar meleset kurang dari 3%.

**Memahami hasil.** Pita di 25 000 cm⁻¹ tajam karena keadaan $^4A_{1g}$ dan $^4E_g(G)$ berasal dari konfigurasi $t_{2g}^3e_g^2$, sama dengan keadaan dasar $^6A_{1g}$; transisinya hanya membalik spin tanpa memindahkan elektron antara $t_{2g}$ dan $e_g$, sehingga energinya tidak bergantung pada $\Delta_o$ dan tidak "merasakan" getaran ikatan. Untuk Mn²⁺, nilai $\Delta_o \approx 8400$ cm⁻¹ diperoleh hanya dari pita-pita terlarang spin, karena tidak ada pita lain. Bahwa semua pita lemah sekali (warna merah muda yang hampir tak terlihat) adalah tanda sidik jari d⁵ spin tinggi.
:::

::: {.kuis}
**Kuis cepat 14.10**

Dalam diagram Tanabe–Sugano d⁶, mengapa semua garis patah pada $\Delta_o/B = 20$? Berapa banyak pita spin diizinkan yang diharapkan untuk [Fe(H₂O)₆]²⁺ (spin tinggi)?
:::
