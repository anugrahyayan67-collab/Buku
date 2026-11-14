## 8.6 Perturbasi tak terdegenerasi orde pertama

### Menyusun deret

Metode variasi meminta kita menebak fungsi gelombang. Teori perturbasi menempuh jalan lain: ia memulai dari masalah yang **sudah** dapat diselesaikan, lalu menghitung secara sistematis bagaimana energi dan fungsi gelombang berubah ketika ditambahkan gangguan kecil. Tulislah Hamiltonian sebagai

$$
\hat H = \hat H^{(0)} + \lambda\hat H' . \qquad \text{(8.29)}
$$

$\hat H^{(0)}$ adalah Hamiltonian **tak terganggu**, yang fungsi eigen dan nilai eigennya kita ketahui:

$$
\hat H^{(0)}\psi_n^{(0)} = E_n^{(0)}\psi_n^{(0)} ,
$$

dengan $\{\psi_n^{(0)}\}$ ortonormal dan lengkap. $\hat H'$ adalah **perturbasi**. Parameter $\lambda$ hanyalah alat pembukuan: ia menghubungkan secara malar masalah tak terganggu ($\lambda = 0$) dengan masalah sebenarnya ($\lambda = 1$), dan pangkatnya menandai "orde" setiap suku. Di akhir perhitungan kita ambil $\lambda = 1$.

Di subbab ini kita anggap tingkat $n$ yang ditinjau **tak terdegenerasi**: tidak ada tingkat lain dengan energi $E_n^{(0)}$ yang sama. (Kasus terdegenerasi dibahas di subbab 8.9.) Bila $\lambda$ kecil, energi dan fungsi gelombang yang sebenarnya hanya sedikit berbeda dari nilai tak terganggu, sehingga masuk akal untuk menguraikannya dalam deret pangkat $\lambda$:

$$
\psi_n = \psi_n^{(0)} + \lambda\psi_n^{(1)} + \lambda^2\psi_n^{(2)} + \cdots , \qquad E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2E_n^{(2)} + \cdots \qquad \text{(8.30)}
$$

$E_n^{(k)}$ dan $\psi_n^{(k)}$ adalah koreksi orde ke-$k$. Masukkan kedua deret ke persamaan Schrödinger $\hat H\psi_n = E_n\psi_n$:

$$
\left(\hat H^{(0)} + \lambda\hat H'\right)\left(\psi_n^{(0)} + \lambda\psi_n^{(1)} + \lambda^2\psi_n^{(2)} + \cdots\right) = \left(E_n^{(0)} + \lambda E_n^{(1)} + \cdots\right)\left(\psi_n^{(0)} + \lambda\psi_n^{(1)} + \cdots\right) .
$$

Persamaan ini harus berlaku untuk **setiap** nilai $\lambda$ kecil, sehingga koefisien setiap pangkat $\lambda$ di kedua ruas harus sama. Mengumpulkan suku-suku:

$$
\lambda^0: \quad \hat H^{(0)}\psi_n^{(0)} = E_n^{(0)}\psi_n^{(0)} ,
$$

$$
\lambda^1: \quad \left(\hat H^{(0)} - E_n^{(0)}\right)\psi_n^{(1)} = \left(E_n^{(1)} - \hat H'\right)\psi_n^{(0)} , \qquad \text{(8.31)}
$$

$$
\lambda^2: \quad \left(\hat H^{(0)} - E_n^{(0)}\right)\psi_n^{(2)} = \left(E_n^{(1)} - \hat H'\right)\psi_n^{(1)} + E_n^{(2)}\psi_n^{(0)} . \qquad \text{(8.32)}
$$

Persamaan orde nol sudah kita ketahui. Masih ada satu kebebasan yang harus ditetapkan: kita boleh menambahkan kelipatan $\psi_n^{(0)}$ ke setiap koreksi tanpa mengubah persamaan. Pilihan yang paling praktis adalah **normalisasi antara**, $\langle\psi_n^{(0)}|\psi_n\rangle = 1$, yang berarti semua koreksi ortogonal terhadap fungsi tak terganggu:

$$
\langle\psi_n^{(0)}|\psi_n^{(k)}\rangle = 0 , \qquad k = 1, 2, \ldots
$$

### Koreksi energi orde pertama

Kalikan (8.31) dari kiri dengan $\psi_n^{(0)*}$ dan integralkan. Di ruas kiri, karena $\hat H^{(0)}$ Hermitian,

$$
\langle\psi_n^{(0)}|\hat H^{(0)} - E_n^{(0)}|\psi_n^{(1)}\rangle = \langle(\hat H^{(0)} - E_n^{(0)})\psi_n^{(0)}|\psi_n^{(1)}\rangle = 0 .
$$

Ruas kanan menjadi $E_n^{(1)}\langle\psi_n^{(0)}|\psi_n^{(0)}\rangle - \langle\psi_n^{(0)}|\hat H'|\psi_n^{(0)}\rangle$. Menyamakannya dengan nol:

$$
E_n^{(1)} = \langle\psi_n^{(0)}|\hat H'|\psi_n^{(0)}\rangle = \int\psi_n^{(0)*}\hat H'\psi_n^{(0)}\,d\tau \equiv H'_{nn} . \qquad \text{(8.33)}
$$

Hasil ini sangat sederhana dan sangat bermakna: **koreksi energi orde pertama adalah nilai rata-rata perturbasi dalam keadaan tak terganggu**. Fungsi gelombang dianggap "beku", dan energinya bergeser sebesar rata-rata gangguan yang dirasakannya. Kita sudah memakainya secara intuitif di Contoh 8.1: helium tanpa tolakan ditambah tolakan rata-rata.

### Koreksi fungsi gelombang orde pertama

Fungsi $\psi_n^{(1)}$ dapat diuraikan dalam fungsi-fungsi tak terganggu yang lengkap. Karena ia ortogonal pada $\psi_n^{(0)}$, suku $m = n$ tidak ada:

$$
\psi_n^{(1)} = \sum_{m\ne n}a_m\psi_m^{(0)} .
$$

Masukkan ke (8.31), lalu kalikan dari kiri dengan $\psi_m^{(0)*}$ ($m \ne n$) dan integralkan. Ruas kiri: $\hat H^{(0)}$ bekerja pada setiap $\psi_k^{(0)}$ dan memberi $E_k^{(0)}$, sehingga hanya suku $k = m$ yang tersisa, $(E_m^{(0)} - E_n^{(0)})a_m$. Ruas kanan: $E_n^{(1)}\langle\psi_m^{(0)}|\psi_n^{(0)}\rangle - H'_{mn} = -H'_{mn}$. Jadi $a_m = H'_{mn}/(E_n^{(0)} - E_m^{(0)})$, dan

$$
\psi_n^{(1)} = \sum_{m\ne n}\frac{H'_{mn}}{E_n^{(0)} - E_m^{(0)}}\,\psi_m^{(0)} , \qquad H'_{mn} = \langle\psi_m^{(0)}|\hat H'|\psi_n^{(0)}\rangle . \qquad \text{(8.34)}
$$

Perturbasi **mencampurkan** keadaan-keadaan lain ke dalam keadaan $n$. Besarnya campuran setiap keadaan $m$ ditentukan oleh dua hal: kopling $H'_{mn}$ (seberapa kuat gangguan menghubungkan kedua keadaan) dan selisih energi $E_n^{(0)} - E_m^{(0)}$ (seberapa jauh kedua keadaan). Keadaan yang dekat dan terkopel kuat mendominasi; keadaan yang jauh hampir tidak berpengaruh. Ini persis pelajaran matriks 2 × 2 di subbab 8.4. Syarat agar deret masuk akal adalah bahwa setiap koefisien campuran kecil, yaitu syarat (8.2), dan sekarang terlihat mengapa syarat itu gagal untuk tingkat terdegenerasi: penyebutnya nol.

::: {.inti}
**Perturbasi orde pertama**

Untuk tingkat tak terdegenerasi $n$ dengan $\hat H = \hat H^{(0)} + \hat H'$:

$$
E_n \approx E_n^{(0)} + H'_{nn} , \qquad \psi_n \approx \psi_n^{(0)} + \sum_{m\ne n}\frac{H'_{mn}}{E_n^{(0)} - E_m^{(0)}}\psi_m^{(0)} .
$$

Energi orde pertama adalah rata-rata gangguan dalam keadaan tak terganggu. Fungsi gelombang orde pertama mencampurkan keadaan lain dengan bobot "kopling dibagi selisih energi".
:::

::: {.awas}
**Energi orde pertama memakai fungsi orde nol**

Kesalahan umum adalah menghitung $E_n^{(1)}$ dengan fungsi gelombang yang sudah dikoreksi. Tidak: $E^{(1)}$ memakai $\psi^{(0)}$; fungsi $\psi^{(1)}$ baru diperlukan untuk $E^{(2)}$ dan $E^{(3)}$ (subbab 8.7). Kesalahan lain adalah memakai satuan yang tidak sama untuk $H'_{mn}$ dan selisih energi di (8.34); koefisien campuran harus tak berdimensi.
:::

::: {.contoh}
**Contoh 8.28 · Kotak dengan dasar miring**

Elektron dalam kotak sepanjang $L$ diberi potensial tambahan $V(x) = V_0x/L$ (misalnya akibat medan listrik). (a) Hitung $E_n^{(1)}$. (b) Untuk kotak 1,00 nm ($E_1 = 0{,}376$ eV) dan $V_0 = 0{,}10$ eV, hitung koefisien campuran keadaan $n = 2$ ke dalam keadaan dasar. Pakai $\langle 2|x|1\rangle = -16L/9\pi^2 = -0{,}1801L$. (c) Mengapa keadaan $n = 3$ tidak tercampur?

**Penyelesaian.** (a) $E_n^{(1)} = (V_0/L)\langle n|x|n\rangle = (V_0/L)(L/2) = V_0/2$ untuk **setiap** $n$, karena posisi rata-rata dalam setiap keadaan kotak adalah tengah kotak.

(b) $H'_{21} = (V_0/L)\langle 2|x|1\rangle = -0{,}1801V_0 = -0{,}0180$ eV. $E_1^{(0)} - E_2^{(0)} = E_1 - 4E_1 = -1{,}128$ eV. Jadi $a_2 = -0{,}0180/(-1{,}128) = +0{,}0160$.

(c) $\langle 3|x|1\rangle = 0$: kedua fungsi genap terhadap titik tengah, sedangkan $x - L/2$ ganjil. Hanya keadaan dengan $n$ genap yang tercampur ke keadaan dasar.

**Memahami hasil.** Pada orde pertama semua tingkat naik sama besar, sehingga selisih tingkat, dan karena itu spektrum serapan, tidak berubah. Fungsi gelombangnya berubah: $\psi_1 + 0{,}016\psi_2$ lebih besar di separuh kiri kotak (tempat $\psi_2$ positif) dan lebih kecil di kanan, sehingga elektron bergeser ke arah potensial rendah. Pergeseran muatan ini adalah **polarisasi**, dan menurunkan energi pada orde kedua (subbab 8.10). Gambar 8.4 membandingkan fungsi perturbasi orde pertama dengan hasil diagonalisasi eksak untuk gangguan yang jauh lebih kuat.
:::

![Gambar 8.4 Keadaan dasar partikel dalam kotak dengan dasar miring $V = V_0x/L$, untuk $V_0 = 5E_1$ (gangguan kuat, agar perubahan terlihat). Garis tipis: fungsi tak terganggu $\psi_1^{(0)}$. Garis putus-putus: $\psi_1^{(0)} + \psi_1^{(1)}$ dari (8.34). Garis tebal: hasil diagonalisasi eksak dalam basis 30 fungsi. Arsiran menunjukkan potensial. Elektron bergeser ke sisi yang potensialnya rendah; perturbasi orde pertama menangkap hampir seluruh pergeseran itu.](fig/c_miring.png){width=70%}

::: {.contoh}
**Contoh 8.29 · Osilator anharmonik: suku kuartik**

Getaran ikatan nyata tidak tepat harmonik. Tambahkan suku kuartik pada osilator ($\hbar = m = \omega = 1$): $\hat H' = \lambda x^4$. (a) Dengan operator tangga, hitung $\langle v|x^4|v\rangle$. (b) Tuliskan $E_v^{(1)}$. (c) Untuk $\lambda = 0{,}1$, bandingkan $E_v^{(0)} + E_v^{(1)}$ dengan nilai eksak dari Contoh 8.24 untuk $v = 0, 1, 2$.

**Penyelesaian.** (a) Dengan $x = (\hat a + \hat a^\dagger)/\sqrt2$ (subbab 5.6), $x^4 = \tfrac14(\hat a + \hat a^\dagger)^4$. Dari 16 susunan empat operator, hanya yang mempunyai dua $\hat a$ dan dua $\hat a^\dagger$ yang memberi kontribusi diagonal. Keenam susunan itu memberi, dengan $\hat a^\dagger|v\rangle = \sqrt{v+1}|v+1\rangle$ dan $\hat a|v\rangle = \sqrt v|v-1\rangle$:

$$
\langle v|x^4|v\rangle = \tfrac14\left[(v+1)(v+2) + (v+1)^2 + (v+1)v + v(v+1) + v^2 + v(v-1)\right] = \tfrac34\left(2v^2 + 2v + 1\right) .
$$

(b) $E_v^{(1)} = \tfrac34\lambda(2v^2 + 2v + 1)$; dalam satuan biasa, $\tfrac34\lambda(\hbar/m\omega)^2(2v^2 + 2v + 1)$.

(c)

| $v$ | $E^{(0)} + E^{(1)}$ | eksak | galat |
|---|---|---|---|
| 0 | 0,5750 | 0,5591 | 0,0159 |
| 1 | 1,8750 | 1,7695 | 0,1055 |
| 2 | 3,4750 | 3,1386 | 0,3364 |

**Memahami hasil.** Koreksi orde pertama tumbuh seperti $v^2$, karena osilasi yang lebih besar lebih "merasakan" dinding kuartik. Bagian $v^2$ itu membuat jarak antartingkat tidak tetap, persis bentuk suku anharmonisitas di (5.24), walaupun dengan tanda yang berlawanan dari yang teramati pada ikatan kimia: suku $x^4$ positif menyempitkan sumur sehingga tingkat-tingkat merenggang, sedangkan sumur ikatan nyata melebar ke arah disosiasi. Di subbab 8.7 kita akan melihat bahwa suku kubik, pada orde kedua, membalik tanda itu. Galat yang membesar dengan $v$ juga memperingatkan bahwa perturbasi orde rendah paling dapat dipercaya untuk tingkat-tingkat terendah.
:::

::: {.contoh}
**Contoh 8.30 · Dari benzena ke piridina**

Dalam metode Hückel, mengganti satu atom C benzena dengan N dimodelkan sebagai perturbasi pada unsur diagonal atom itu: $\alpha_\text{N} = \alpha + h\beta$ dengan $h \approx 0{,}5$ (nitrogen lebih elektronegatif, dan $\beta < 0$). Matriks perturbasinya hanya mempunyai satu unsur tak nol, $H'_{11} = h\beta$. (a) Tunjukkan bahwa koreksi orde pertama untuk orbital $k$ adalah $E_k^{(1)} = h\beta c_{1k}^2$, dengan $c_{1k}$ koefisien orbital $k$ pada atom 1. (b) Hitung koreksi untuk orbital benzena terendah ($x = 2$, semua koefisien $1/\sqrt6$) dan tertinggi ($x = -2$). (c) Diagonalisasi eksak memberi $x = 2{,}1074$ dan $-1{,}9337$. Bandingkan.

**Penyelesaian.** (a) $E_k^{(1)} = \langle k|\hat H'|k\rangle = \sum_{r,s}c_{rk}c_{sk}H'_{rs} = c_{1k}^2h\beta$.

(b) Untuk kedua orbital, $c_{11}^2 = 1/6$, sehingga $E^{(1)} = h\beta/6 = 0{,}0833\beta$. Orbital terendah: $x = 2 + 0{,}0833 = 2{,}0833$. Orbital tertinggi: $x = -2 + 0{,}0833 = -1{,}9167$.

(c) Untuk orbital terendah, orde pertama menangkap 78% pergeseran eksak (0,083 dari 0,107). Untuk orbital tertinggi, orde pertama justru melampaui pergeseran eksak (0,083 lawan 0,066). Kedua selisih adalah efek orde kedua, yang dihitung di Contoh 8.36.

**Memahami hasil.** Rumus $\delta E_k = c_{rk}^2\,\delta\alpha_r$ adalah inti teori orbital molekul perturbasi (Coulson dan Longuet-Higgins, 1947): menaikkan elektronegativitas atom $r$ menurunkan setiap orbital sebanding dengan kerapatan orbital itu pada atom $r$. Orbital yang mempunyai simpul di atom $r$ tidak terpengaruh. Untuk dua orbital benzena yang terdegenerasi ($x = \pm1$), rumus orde pertama biasa tidak dapat dipakai; di subbab 8.9 kita akan melihat bahwa nitrogen memecah pasangan itu, dan bahwa itulah sebabnya spektrum fotoelektron piridina menunjukkan lebih banyak pita daripada benzena.
:::

::: {.contoh}
**Contoh 8.31 · Koreksi relativistik orde pertama**

Untuk ion mirip hidrogen, teori relativitas menambahkan dua perturbasi utama pada orbital 1s (selain spin–orbit, yang nol untuk orbital s): koreksi massa–kecepatan $-\hat p^4/8m_e^3c^2$ dan suku Darwin. Dalam satuan atom (dengan $c = 1/\alpha_\text{f}$, $\alpha_\text{f} = 1/137{,}036$), nilai rata-ratanya untuk 1s adalah $-\tfrac58Z^4\alpha_\text{f}^2$ dan $+\tfrac12Z^4\alpha_\text{f}^2$, sehingga jumlahnya $-\tfrac18Z^4\alpha_\text{f}^2$. Hitung koreksi total untuk hidrogen (dalam cm⁻¹) dan untuk ion emas ($Z = 79$), dan bandingkan dengan energi tak terganggu $-Z^2/2$.

**Penyelesaian.** $\alpha_\text{f}^2 = 5{,}325 \times 10^{-5}$. Hidrogen: $-\tfrac18(5{,}325 \times 10^{-5}) = -6{,}66 \times 10^{-6}\ E_h = -1{,}46$ cm⁻¹, perbandingan terhadap $-0{,}5\ E_h$ sebesar $1{,}3 \times 10^{-5}$. Emas: $Z^4 = 3{,}895 \times 10^7$, koreksi $-259\ E_h$, sedangkan $-Z^2/2 = -3120\ E_h$: perbandingannya 8,3%. Suku massa–kecepatan sendiri sebesar $-1296\ E_h$, atau 42% dari energi tak terganggu.

**Memahami hasil.** Untuk atom ringan, efek relativistik adalah perturbasi kecil yang hanya terlihat dalam spektroskopi resolusi tinggi. Untuk atom berat, koreksinya tumbuh seperti $Z^4$, dan suku-suku penyusunnya sudah terlalu besar untuk diperlakukan sebagai perturbasi: perlu persamaan Dirac. Kontraksi relativistik orbital s (dan 6s pada khususnya) menjelaskan warna kuning emas, mengapa raksa cair pada suhu kamar, dan sebagian besar tegangan aki timbal–asam. Kimia unsur periode 6 dan 7 tidak dapat dipahami tanpa relativitas (subbab 17.15).
:::

::: {.contoh}
**Contoh 8.32 · Massa inti sebagai perturbasi: penemuan deuterium**

Dalam atom hidrogen, inti juga bergerak. Di kerangka pusat massa momentum inti sama besar dan berlawanan dengan momentum elektron, sehingga energi kinetik inti $\hat p^2/2M$ dapat dipandang sebagai perturbasi pada Hamiltonian dengan inti diam: $\hat H' = (m_e/M)\hat T$. (a) Dengan teorema virial ($\langle T\rangle = -E_n$), tunjukkan bahwa $E_n^{(1)} = -(m_e/M)E_n^{(0)}$. (b) Hitung pergeseran garis Lyman-α (2p → 1s, 121,57 nm) dan Balmer-α (3 → 2, 656,28 nm) antara hidrogen ($M/m_e = 1836{,}15$) dan deuterium ($M/m_e = 3670{,}48$), dalam cm⁻¹ dan nm.

**Penyelesaian.** (a) $E_n^{(1)} = (m_e/M)\langle T\rangle = -(m_e/M)E_n^{(0)}$, sehingga $E_n \approx E_n^{(0)}(1 - m_e/M)$. Ini tepat suku pertama uraian $\mu/m_e = 1/(1 + m_e/M)$: teori perturbasi orde pertama menemukan kembali koreksi massa tereduksi (subbab 6.8).

(b) Setiap energi transisi dikalikan $(1 - m_e/M)$, sehingga selisih D − H adalah $\Delta E_\text{trans}(m_e/M_\text{H} - m_e/M_\text{D})$, dengan $m_e/M_\text{H} - m_e/M_\text{D} = 2{,}722 \times 10^{-4}$. Lyman-α ($\Delta E = 0{,}375\ E_h$): $1{,}021 \times 10^{-4}\ E_h = 22{,}4$ cm⁻¹; dengan $\Delta\lambda = \lambda^2\Delta\tilde\nu$, $\Delta\lambda = 0{,}033$ nm. Balmer-α ($\Delta E = 5/72\ E_h$): 4,15 cm⁻¹, $\Delta\lambda = 0{,}179$ nm. Garis deuterium berada pada panjang gelombang yang lebih **pendek**.

**Memahami hasil.** Pada tahun 1931, Urey, Brickwedde, dan Murphy menguapkan hidrogen cair perlahan-lahan untuk memekatkan isotop berat yang diduga ada, lalu menemukan garis-garis lemah di sisi biru setiap garis Balmer, bergeser hampir tepat 0,18 nm dari Balmer-α. Itulah penemuan deuterium (Nobel Kimia 1934). Satu koreksi perturbasi orde pertama yang sederhana memisahkan dua isotop; dalam kimia, perbedaan massa yang sama menimbulkan efek isotop kinetik dan pergeseran frekuensi getaran yang dibahas di subbab 5.10.
:::

::: {.contoh}
**Contoh 8.33 · Tonjolan di tengah kotak**

Model elektron bebas untuk rantai terkonjugasi yang di tengahnya terdapat heteroatom: tambahkan tonjolan potensial $V_0$ selebar $b$ di tengah kotak sepanjang $L$. (a) Tunjukkan bahwa $E_n^{(1)} = V_0\left[b/L - (-1)^n\sin(n\pi b/L)/n\pi\right]$. (b) Hitung untuk $b = L/10$ dan $n = 1$ sampai 4. (c) Apa akibatnya bagi selisih HOMO–LUMO?

**Penyelesaian.** (a) $E_n^{(1)} = V_0(2/L)\int\sin^2(n\pi x/L)\,dx$ di antara $L/2 - b/2$ dan $L/2 + b/2$. Dengan $\sin^2u = \tfrac12(1 - \cos2u)$, integralnya $\tfrac b2 - \tfrac{L}{4n\pi}\left[\sin(n\pi + n\pi b/L) - \sin(n\pi - n\pi b/L)\right] = \tfrac b2 - \tfrac{L}{2n\pi}\cos(n\pi)\sin(n\pi b/L)$. Kalikan dengan $2V_0/L$ dan pakai $\cos n\pi = (-1)^n$.

(b) Dalam satuan $V_0$: $n = 1$: 0,1984; $n = 2$: 0,0065; $n = 3$: 0,1858; $n = 4$: 0,0243.

(c) Tingkat dengan $n$ ganjil (maksimum di tengah) bergeser sekitar $2V_0b/L$, sedangkan tingkat dengan $n$ genap (simpul di tengah) hampir tidak bergeser. Bila HOMO bernomor ganjil dan LUMO genap, heteroatom yang menarik elektron ($V_0 < 0$) menurunkan HOMO saja, sehingga celah **membesar** dan serapan bergeser ke biru. Bila HOMO genap dan LUMO ganjil, yang turun LUMO, celah **mengecil**, dan serapan bergeser ke merah.

**Memahami hasil.** Arah pergeseran warna ditentukan oleh di mana orbital perbatasan mempunyai simpul, bukan hanya oleh "kuatnya" heteroatom. Aturan ini, yang dalam bahasa Hückel dikenal sebagai aturan Dewar–Knott untuk zat warna, dipakai perancang zat warna untuk memilih posisi substitusi yang menggeser serapan ke arah yang diinginkan.
:::

::: {.kuis}
**Kuis cepat 8.6**

(a) Untuk osilator harmonik dengan perturbasi $\hat H' = cx^3$, berapa $E_v^{(1)}$, dan mengapa? (b) Dalam piridina, apakah orbital yang mempunyai simpul di atom N ikut bergeser pada orde pertama? (c) Mengapa (8.34) tidak dapat dipakai bila $E_m^{(0)} = E_n^{(0)}$?
:::

## 8.7 Orde kedua

### Rumus energi orde kedua

Kalikan persamaan orde kedua (8.32) dari kiri dengan $\psi_n^{(0)*}$ dan integralkan. Ruas kiri nol (sifat Hermitian, seperti sebelumnya). Di ruas kanan, $\langle\psi_n^{(0)}|\psi_n^{(1)}\rangle = 0$ (normalisasi antara), sehingga yang tersisa adalah $-\langle\psi_n^{(0)}|\hat H'|\psi_n^{(1)}\rangle + E_n^{(2)} = 0$:

$$
E_n^{(2)} = \langle\psi_n^{(0)}|\hat H'|\psi_n^{(1)}\rangle .
$$

Masukkan (8.34):

$$
E_n^{(2)} = \sum_{m\ne n}\frac{H'_{nm}H'_{mn}}{E_n^{(0)} - E_m^{(0)}} = \sum_{m\ne n}\frac{|H'_{mn}|^2}{E_n^{(0)} - E_m^{(0)}} . \qquad \text{(8.35)}
$$

Bandingkan dengan (8.24): energi orde kedua adalah jumlah dari pergeseran "dua tingkat" untuk setiap pasangan $(n, m)$. Setiap keadaan lain menyumbang sebanding dengan kuadrat koplingnya, dibagi selisih energinya.

### Tiga sifat penting

**1. Untuk keadaan dasar, $E^{(2)}$ selalu negatif.** Bila $n$ adalah keadaan terendah, semua penyebut $E_n^{(0)} - E_m^{(0)}$ negatif, sedangkan pembilang $|H'_{mn}|^2$ positif. Jadi gangguan apa pun, pada orde kedua, menurunkan energi keadaan dasar. Ini masuk akal: sistem "memanfaatkan" gangguan dengan menyesuaikan fungsi gelombangnya, dan penyesuaian itu selalu menguntungkan (bandingkan dengan teorema variasi: fungsi yang dapat menyesuaikan diri tidak mungkin lebih buruk daripada fungsi beku).

**2. Tolakan tingkat.** Untuk dua tingkat $n$ dan $m$ yang terkopel, sumbangan pasangan itu adalah $+|H'_{mn}|^2/(E_n - E_m)$ untuk tingkat $n$ dan $+|H'_{mn}|^2/(E_m - E_n)$ untuk tingkat $m$: sama besar, berlawanan tanda. Tingkat bawah didorong turun, tingkat atas didorong naik. Kopling selalu membuat tingkat-tingkat saling menjauh, dan tidak pernah membuat mereka berpotongan. Inilah asal **kaidah tak-berpotongan** kurva energi potensial (*avoided crossing*), stabilisasi orbital ikatan dalam teori orbital molekul, dan banyak efek kimia lain.

**3. Penyebut kecil, efek besar.** Keadaan yang energinya dekat mendominasi jumlah. Inilah alasan kimiawan memusatkan perhatian pada **orbital perbatasan** (HOMO dan LUMO): interaksi antara HOMO satu molekul dan LUMO molekul lain mempunyai penyebut terkecil dan karena itu sumbangan orde kedua terbesar (subbab 13.10).

::: {.inti}
**Perturbasi orde kedua**

$$
E_n^{(2)} = \sum_{m\ne n}\frac{|H'_{mn}|^2}{E_n^{(0)} - E_m^{(0)}}
$$

Untuk keadaan dasar $E^{(2)} < 0$. Setiap pasangan tingkat terkopel saling menolak; tingkat yang berdekatan dan terkopel kuat memberi sumbangan terbesar.
:::

### Energi orde ketiga dan aturan $2n + 1$

Dengan cara yang sama, persamaan orde ketiga memberi

$$
E_n^{(3)} = \langle\psi_n^{(1)}|\hat H' - E_n^{(1)}|\psi_n^{(1)}\rangle . \qquad \text{(8.36)}
$$

Hanya $\psi^{(1)}$ yang diperlukan, bukan $\psi^{(2)}$. Ini contoh **aturan $2n + 1$** Wigner: mengetahui fungsi gelombang sampai orde $n$ cukup untuk menghitung energi sampai orde $2n + 1$. Aturan ini adalah saudara kembar sifat (8.5) metode variasi, bahwa galat energi orde kedua dalam galat fungsi gelombang.

### Pendekatan Unsöld

Jumlah (8.35) melibatkan semua keadaan, termasuk keadaan kontinu (ionisasi) pada atom dan molekul. Jumlah ini sering sulit dihitung langsung. Unsöld (1927) mengusulkan jalan pintas: ganti semua penyebut dengan satu energi rata-rata $\Delta E$. Untuk keadaan dasar,

$$
E_1^{(2)} \approx -\frac{1}{\Delta E}\sum_{m\ne1}|H'_{m1}|^2 = -\frac{\langle\hat H'^2\rangle - \langle\hat H'\rangle^2}{\Delta E} . \qquad \text{(8.37)}
$$

Langkah terakhir memakai relasi kelengkapan $\sum_m|m\rangle\langle m| = 1$ (subbab 4.9): $\sum_{m\ne1}H'_{1m}H'_{m1} = \langle 1|\hat H'^2|1\rangle - \langle 1|\hat H'|1\rangle^2$. Jadi energi orde kedua dihitung dari **varians** perturbasi dalam keadaan dasar saja, tanpa perlu keadaan tereksitasi. Pilihan $\Delta E$ adalah titik lemahnya; biasanya dipakai energi ionisasi atau energi eksitasi rata-rata. Satu hal pasti: karena setiap penyebut sesungguhnya sekurang-kurangnya $E_2^{(0)} - E_1^{(0)}$, mengambil $\Delta E = E_2^{(0)} - E_1^{(0)}$ memberi batas: $|E_1^{(2)}| \le (\langle\hat H'^2\rangle - \langle\hat H'\rangle^2)/(E_2^{(0)} - E_1^{(0)})$.

### Apakah deret perturbasi konvergen?

Tidak selalu. Deret perturbasi sering bersifat **asimtotik**: beberapa suku pertama makin kecil dan mendekati jawaban, tetapi setelah orde tertentu suku-sukunya membesar lagi. Contoh klasiknya osilator kuartik (Contoh 8.35). Argumen Dyson menjelaskan mengapa: bila $\lambda$ negatif, potensial $\tfrac12x^2 + \lambda x^4$ jatuh ke $-\infty$ di jauh, dan tidak ada keadaan terikat. Deret pangkat dalam $\lambda$ yang konvergen untuk $\lambda > 0$ kecil juga akan konvergen untuk $\lambda < 0$ kecil, padahal di sana fisikanya berubah total; jadi deretnya tidak mungkin konvergen. Dalam praktik kimia, orde kedua (MP2, subbab 17.11) sering memberi keseimbangan terbaik antara biaya dan ketelitian, dan orde yang lebih tinggi tidak selalu lebih baik.

::: {.contoh}
**Contoh 8.34 · Dua tingkat: eksak lawan orde kedua**

Dua tingkat $E_1^{(0)} = 0$ dan $E_2^{(0)} = \Delta$ dikopel oleh $H'_{12} = V$ (tanpa unsur diagonal). Bandingkan pergeseran eksak tingkat bawah, dari (8.22), dengan $E^{(2)} = -V^2/\Delta$ untuk $V/\Delta = 0{,}05$; 0,1; 0,2; 0,5; 1.

**Penyelesaian.** Eksak: $E_- = \Delta/2 - \sqrt{\Delta^2/4 + V^2}$.

| $V/\Delta$ | eksak ($\Delta$) | orde kedua ($\Delta$) | galat |
|---|---|---|---|
| 0,05 | $-0{,}002494$ | $-0{,}002500$ | 0,25% |
| 0,1 | $-0{,}009902$ | $-0{,}010000$ | 1,0% |
| 0,2 | $-0{,}03852$ | $-0{,}04000$ | 3,9% |
| 0,5 | $-0{,}2071$ | $-0{,}2500$ | 21% |
| 1 | $-0{,}6180$ | $-1{,}000$ | 62% |

**Memahami hasil.** Orde kedua sangat baik selama kopling kurang dari sepersepuluh selisih energi, dan galatnya kira-kira $(V/\Delta)^2 \times 100\%$. Ketika kopling sebanding dengan selisih, rumus perturbasi melebih-lebihkan pergeseran: pembagian dengan $\Delta$ yang tetap mengabaikan bahwa tingkat-tingkat itu sendiri sudah saling menjauh. Untuk kasus seperti itu (dua orbital yang hampir sama energinya), diagonalisasi matriks kecil adalah cara yang benar, dan teori perturbasi dipakai untuk sisa keadaan yang jauh.
:::

![Gambar 8.5 Kiri: energi dua tingkat terkopel sebagai fungsi selisih tingkat tak terganggu $\delta = E_2^{(0)} - E_1^{(0)}$, dengan kopling tetap $V$. Garis tipis: tingkat tak terganggu yang berpotongan. Garis tebal: tingkat eksak, yang saling menghindar dengan celah minimum $2|V|$. Garis putus-putus: perturbasi orde kedua, yang baik jauh dari persilangan dan gagal di dekatnya. Kanan: energi keadaan dasar osilator $\tfrac12x^2 + \lambda x^4$ terhadap $\lambda$: eksak, dan deret perturbasi yang dipotong pada orde 1, 2, 3, dan 4.](fig/c_orde2.png){width=95%}

::: {.contoh}
**Contoh 8.35 · Osilator kuartik: deret yang asimtotik**

Untuk $\hat H = \tfrac12p^2 + \tfrac12x^2 + \lambda x^4$, koefisien deret perturbasi keadaan dasar (dihitung dengan rekursi Rayleigh–Schrödinger dalam basis osilator) adalah

$$
E_0 = \tfrac12 + \tfrac34\lambda - \tfrac{21}{8}\lambda^2 + \tfrac{333}{16}\lambda^3 - \tfrac{30\,885}{128}\lambda^4 + \cdots
$$

(a) Periksa koefisien orde kedua dengan (8.35). (b) Jumlahkan deret untuk $\lambda = 0{,}1$ orde demi orde dan bandingkan dengan nilai eksak 0,559146.

**Penyelesaian.** (a) $x^4$ menghubungkan $|0\rangle$ dengan $|2\rangle$ dan $|4\rangle$. Dengan operator tangga: $\langle 2|x^4|0\rangle = \tfrac14\cdot6\sqrt2 = 3/\sqrt2$ dan $\langle 4|x^4|0\rangle = \tfrac14\sqrt{24} = \sqrt6/2$. Selisih energinya $-2$ dan $-4$. Jadi $E^{(2)} = \lambda^2[(9/2)/(-2) + (6/4)/(-4)] = \lambda^2(-\tfrac94 - \tfrac38) = -\tfrac{21}{8}\lambda^2$.

(b) Penjumlahan orde demi orde:

| Orde | Suku | Jumlah | Galat |
|---|---|---|---|
| 0 | 0,5 | 0,5 | $-0{,}0591$ |
| 1 | $+0{,}075$ | 0,575 | $+0{,}0159$ |
| 2 | $-0{,}02625$ | 0,54875 | $-0{,}0104$ |
| 3 | $+0{,}02081$ | 0,56956 | $+0{,}0104$ |
| 4 | $-0{,}02413$ | 0,54543 | $-0{,}0137$ |

**Memahami hasil.** Suku-sukunya mengecil sampai orde kedua, lalu membesar lagi: deretnya asimtotik. Jawaban terbaik diperoleh dengan berhenti di sekitar suku terkecil, dan galatnya tidak dapat dibuat lebih kecil daripada kira-kira besar suku itu, berapa pun ordenya. Bandingkan dengan diagonalisasi (Contoh 8.24), yang konvergen ke nilai eksak dengan basis 10 fungsi saja. Untuk gangguan yang tidak kecil, metode variasi linear lebih dapat diandalkan; teori perturbasi unggul bila gangguannya benar-benar kecil, atau bila kita menginginkan rumus analitis.
:::

::: {.contoh}
**Contoh 8.36 · Piridina pada orde kedua**

Lanjutkan Contoh 8.30. Dalam basis orbital benzena yang dipilih sedemikian sehingga dari setiap pasangan terdegenerasi hanya satu orbital yang mempunyai koefisien pada atom 1 (koefisien kuadrat $\tfrac13$), unsur kopling perturbasi antara orbital $k$ dan $m$ adalah $H'_{mk} = h\beta c_{1m}c_{1k}$. Hitung koreksi orde kedua untuk orbital terendah ($x = 2$) dalam satuan $\beta$.

**Penyelesaian.** Dengan $E = \alpha + x\beta$, penyebut $E_k - E_m = (x_k - x_m)\beta$, sehingga dalam satuan $\beta$,

$$
\delta x^{(2)} = \sum_{m\ne k}\frac{h^2c_{1k}^2c_{1m}^2}{x_k - x_m} = h^2\cdot\frac16\left[\frac{1/3}{2 - 1} + \frac{1/3}{2 - (-1)} + \frac{1/6}{2 - (-2)}\right] = 0{,}25\cdot\frac16\cdot0{,}4861 = 0{,}0203 .
$$

Jadi $x \approx 2 + 0{,}0833 + 0{,}0203 = 2{,}1036$, dibandingkan dengan nilai eksak 2,1074.

Untuk orbital tertinggi ($x = -2$) semua penyebut negatif, dan jumlah yang sama memberi $\delta x^{(2)} = -0{,}0203$, sehingga $x \approx -2 + 0{,}0833 - 0{,}0203 = -1{,}9370$, dibandingkan dengan nilai eksak $-1{,}9337$.

**Memahami hasil.** Orde kedua menutup 84% sisa galat orde pertama orbital terendah; galat yang tersisa (0,004) adalah orde ketiga dan seterusnya. Untuk orbital tertinggi, koreksi orde kedua bertanda berlawanan dan memperbaiki lompatan orde pertama yang terlalu jauh: tolakan tingkat mendorong orbital teratas naik dalam energi, menjauhi orbital-orbital di bawahnya. Sumbangan terbesar datang dari orbital $x = 1$, tetangga terdekat dalam energi, sesuai sifat ketiga di atas. Karena $\beta < 0$, $\delta x > 0$ berarti energi turun: orde kedua menurunkan orbital terendah lebih jauh, sesuai sifat pertama. Secara kimia, orbital π terendah piridina lebih terlokalisasi pada nitrogen daripada orbital benzena padanannya: koreksi fungsi gelombang (8.34) mencampurkan orbital lain sehingga koefisien pada atom 1 membesar.
:::

::: {.contoh}
**Contoh 8.37 · Osilator bermuatan dalam medan listrik dan model Drude**

Partikel bermuatan $q$ dan bermassa $m$ terikat pegas ($k = m\omega^2$) diletakkan dalam medan $F$, sehingga $\hat H' = -qF\hat x$. (a) Hitung $E_0^{(1)}$ dan $E_0^{(2)}$. (b) Tunjukkan bahwa hasilnya eksak. (c) Polarisabilitas didefinisikan oleh $E = E_0 - \tfrac12\alpha F^2$. Hitung volume polarisabilitas $\alpha/4\pi\varepsilon_0$ untuk elektron dengan $\hbar\omega = 10$ eV.

**Penyelesaian.** (a) $E_0^{(1)} = -qF\langle 0|x|0\rangle = 0$ (paritas). Operator $x$ hanya menghubungkan $|0\rangle$ dengan $|1\rangle$, dengan $|\langle 1|x|0\rangle|^2 = \hbar/2m\omega$. Jadi $E_0^{(2)} = q^2F^2(\hbar/2m\omega)/(-\hbar\omega) = -q^2F^2/2m\omega^2 = -q^2F^2/2k$.

(b) Melengkapkan kuadrat: $\tfrac12kx^2 - qFx = \tfrac12k(x - qF/k)^2 - q^2F^2/2k$. Osilator hanya bergeser ke $x_0 = qF/k$, dan energinya turun tepat $q^2F^2/2k$, untuk setiap tingkat $v$.

(c) $\alpha = q^2/k = e^2/m_e\omega^2$. Dengan $\omega = (10\ \text{eV})/\hbar = 1{,}519 \times 10^{16}$ s⁻¹: $\alpha/4\pi\varepsilon_0 = (2{,}307 \times 10^{-28}\ \text{J m})/(9{,}109 \times 10^{-31} \times 2{,}307 \times 10^{32}) = 1{,}10 \times 10^{-30}$ m³ $= 1{,}10$ Å³.

**Memahami hasil.** Teori perturbasi orde kedua eksak di sini karena hanya satu keadaan yang terkopel dan semua orde lebih tinggi lenyap. "Elektron pada pegas" (model Drude–Lorentz, subbab 2.3) dengan frekuensi pada daerah UV menghasilkan polarisabilitas sekitar 1 Å³, orde besaran yang benar untuk atom dan molekul kecil (hidrogen 0,67 Å³, metana 2,6 Å³). Pesannya: polarisabilitas berbanding terbalik dengan kuadrat energi eksitasi; molekul yang menyerap pada panjang gelombang lebih panjang (celah HOMO–LUMO kecil) lebih mudah dipolarisasi.
:::

::: {.dalam}
**Lebih dalam: anharmonisitas Morse dari teori perturbasi**

Uraikan potensial ikatan di sekitar $r_e$ ($y = r - r_e$):

$$
V(y) = \tfrac12ky^2 + \tfrac16k_3y^3 + \tfrac{1}{24}k_4y^4 + \cdots
$$

Suku kubik ganjil, sehingga orde pertamanya nol; pada orde kedua ia menghubungkan $|v\rangle$ dengan $|v \pm 1\rangle$ dan $|v \pm 3\rangle$. Penjumlahan (8.35) dengan operator tangga memberi, dengan $s = \hbar/2\mu\omega$,

$$
E_v^{(2)}(\text{kubik}) = -\frac{k_3^2s^3}{36\,\hbar\omega}\left(30v^2 + 30v + 11\right) .
$$

Suku kuartik pada orde pertama (Contoh 8.29): $E_v^{(1)}(\text{kuartik}) = \tfrac{k_4}{24}s^2\left(6v^2 + 6v + 3\right)$. Koefisien $v^2$ dari jumlah keduanya adalah $-\omega_ex_e$ (dalam satuan energi), karena $G(v) = \omega_e(v + \tfrac12) - \omega_ex_e(v + \tfrac12)^2$ memuat $-\omega_ex_ev^2$:

$$
\omega_ex_e = \frac{5k_3^2s^3}{6\hbar\omega} - \frac{k_4s^2}{4} .
$$

Untuk potensial Morse $V = D_e(1 - e^{-ay})^2 = D_e\left(a^2y^2 - a^3y^3 + \tfrac{7}{12}a^4y^4 - \cdots\right)$: $k = 2D_ea^2$, $k_3 = -6D_ea^3$, $k_4 = 14D_ea^4$. Dengan $s/\hbar\omega = 1/2\mu\omega^2 = 1/4D_ea^2$, suku pertama menjadi $\tfrac56(36D_e^2a^6)s^2/4D_ea^2 = 7{,}5D_ea^4s^2$ dan suku kedua $3{,}5D_ea^4s^2$. Selisihnya

$$
\omega_ex_e = 4D_ea^4s^2 = \frac{4D_ea^4\hbar^2}{4\mu^2\omega^2} = \frac{\hbar^2a^2}{2\mu} = \frac{(\hbar\omega)^2}{4D_e} ,
$$

tepat rumus Morse (5.27). Suku kubik, yang membuat sumur melebar ke arah disosiasi, mendominasi dan membuat tingkat-tingkat merapat; suku kuartik positif melawan sedikit. Untuk H₂ ($\omega_e = 4401{,}2$ cm⁻¹, $D_e = 38\,288$ cm⁻¹) rumus ini memberi $\omega_ex_e = 126{,}5$ cm⁻¹, dibandingkan 121,3 cm⁻¹ terukur. Spektroskopis menggunakan hubungan ini terbalik: dari $\omega_ex_e$ dan tetapan interaksi rotasi–getaran $\alpha_e$ yang terukur, mereka menentukan $k_3$ dan $k_4$, yaitu bentuk kurva energi potensial di sekitar minimum.
:::

::: {.terapan}
**Interaksi donor–akseptor dan efek anomerik**

Metode analisis orbital ikatan alami (NBO) menghitung energi stabilisasi antara orbital terisi "donor" $i$ (pasangan elektron bebas atau ikatan) dan orbital kosong "akseptor" $j$ (orbital antiikatan) dengan rumus orde kedua $E^{(2)} = -2F_{ij}^2/(\varepsilon_j - \varepsilon_i)$, dengan $F_{ij}$ unsur matriks Fock dan faktor 2 untuk dua elektron donor. Dengan nilai khas $F_{ij} = 0{,}06\ E_h$ dan $\varepsilon_j - \varepsilon_i = 0{,}8\ E_h$, $E^{(2)} \approx -0{,}009\ E_h$, sekitar $-24$ kJ/mol. Interaksi pasangan bebas oksigen dengan orbital $\sigma^*_\text{C–O}$ yang sejajar dengannya (hiperkonjugasi negatif) adalah penjelasan populer untuk **efek anomerik**, yaitu kecenderungan substituen elektronegatif pada C1 cincin piranosa untuk mengambil posisi aksial walaupun posisi itu lebih sesak. Efek ini hanya muncul bila geometri membuat $F_{ij}$ besar, yaitu bila kedua orbital sejajar; itulah sebabnya ia bergantung tajam pada konformasi.
:::

::: {.kuis}
**Kuis cepat 8.7**

(a) Mengapa energi keadaan dasar tidak pernah naik karena perturbasi orde kedua? (b) Untuk keadaan tereksitasi tertinggi dari suatu himpunan tingkat berhingga, apa tanda $E^{(2)}$? (c) Dua orbital dengan selisih energi 4 eV dikopel oleh 0,4 eV. Taksir pergeseran masing-masing, dan perkirakan galat taksiran itu.
:::

